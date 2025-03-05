# K8s Service 四层负载均衡
本章主要学习k8s的流量负载组件：Service与ingress，Service用于4层流量的负载，ingress用于7层流量负载。



#### Service介绍
kubernetes集群中有三类网络，一类是真实存在的，如：Node节点网络、Pod网络，这两种网络均提供真实IP地址。

还有一类是虚拟的Service 网络，提供虚拟cluster IP（VIP）地址，这个地址不会出现在接口上，仅会出现在Service当中。

在kubernetes集群时，由于Pod经常处于用后即焚状态，Pod经常被重新生成，因此Pod对应的IP地址也会经常变化，导致无法直接访问Pod提供的服务。

Kubernetes中使用了Service来解决这一问题，即在Pod前面使用Service对Pod进行代理，无论Pod怎样变化 ，只要有Label，就可以让Service能够联系上Pod，进而实现通过Service访问Pod目的。



#### Kube-proxy介绍
Service的本质就是一条代理规则，真正实现代理功能的其实是kube-proxy代理组件，集群的每个节点都运行着一个kube-proxy服务进程，当创建Service的时候，就等于创建了一条代理规则，而这条规则就是告诉kube-proxy 通过那种模式进行流量转发。



#### kube-proxy代理模式介绍
kube-proxy三种代理模式：UserSpace模式、iptables模式、ipvs模式



#### **UserSpace模式介绍**
最原始的转发模式，用户通过clusterIP（VIP）访问需要经过kube-proxy进行代理转发，这种模式效率低，已经很少用。



#### iptables模式介绍
该模式下kube-proxy不承担四层负载均衡器的角色，kube-proxy 只是作为 controller（控制器）去创建iptables规则，然后用户的请求直接通过iptables转发规则被转发到后端的每个Pod中（真正实现流量转发的是内核的 netfilter模块，基于内核进行流量转发本身效率就高，而且对比与userspace还少了一个kube-proxy转发的环节）。



iptables模式不能提供灵活的负载均衡策略，只是随机的将流量转发到后端的Pod，当后端Pod不可用时也无法进行健康检查。

#### ipvs模式介绍
ipvs（Virtual Server）与iptables类似，都是基于 netfilter 进行流量转发，kube-proxy也不承担四层负载均衡器的角色，只创建ipvs规则，但是ipvs在转发时支持的负载均衡算法非常的灵活，例如：轮询、加权轮询、基于端口转发、最小负载、最少连接等，ipvs 支持服务器健康检查和连接重试等功能。



想要使用ipvs转发模式需要安装ipvs内核模块，否则会降级为iptables模式

```yaml
查看ipvs模块（本实验环境在第二章集群环境部署时已经安装）
[root@master01 ~]# lsmod | grep -e ip_vs -e nf_conntrack_ipv4
nf_conntrack_ipv4
nf_defrag_ipv4 
ip_vs_sh
ip_vs_wrr
ip_vs_rr 
ip_vs
nf_conntrack
libcrc32c 


开启ipvs，编辑kube-proxy文件
[root@master01 ~]# kubectl edit cm kube-proxy -n kube-system
mode: "ipvs"   #修改为ipvs模式
#提示：cm（ConfigMap）在K8s中属于配置资源



删除当前正在使用的kube-proxy的pod（按照标签删除）
[root@master01 ~]# kubectl get pod --show-labels -n kube-system | grep kube-proxy*

[root@master01 ~]# kubectl delete pod -l k8s-app=kube-proxy -n kube-system



查看kube-proxy的pod是否被重建
[root@master ~]# kubectl get po -n kube-system



查看ipvs功能是否开启
[root@master01 ~]# ipvsadm -Ln    
```





#### Service常用访问方式介绍
+ ClusterIP：默认访问方式，分配一个集群内部可以访问的虚拟IP（该方式只能用于集群内部访问，外部无法访问）



+ NodePort：在每个Node上分配一个端口作为外部访问入口，端口范围为30000-32767（该访问适用于外部访问）



+ LoadBalancer：通过在集群外部的公有云平台上，例如：阿里云、华为云、AWS等做一个负载均衡，通过外部负载均衡将流量转发到集群中。访问过程：用户----->域名----->云服务提供商提供LB负载均衡设备----->NodeIP:Port(service IP)----->Pod IP：端口

#### Service资源清单文件介绍
> kubectl explain svc   查看service资源支持的属性
>

```yaml
apiVersion: v1    	#版本
kind: Service     	#资源类型
metadata:         	#元数据
  name: 		   	#资源名称
  namespace: 	  	#所属名称空间
spec:             	#描述
  selector:       	#标签选择器，用于确定当前service代理哪些pod
    app:            #标签
  type:             	Service类型
  clusterIP:        	clusterIP访问方式
  ports:            	端口信息
    - protocol: TCP     端口协议
      port:         	访问Service使用的端口
      targetPort:   	pod中容器的端口
      nodePort:     	node端口（Service需要暴露给外部访问的节点端口，端口范围：30000-32767）

```





#### Cluster IP 应用案例
**案例**：通过HPA创建3个Pod并设置标签为app=deploy-nginx（使用前面的hpa-deploy_nginx.yml创建即可）通过Service ClusterIP访问方式进行代理

```yaml
ClusterIP：默认访问方式，由k8s自动分配的虚拟IP，只能在集群内部访问

[root@master01 ~]# vim hpa-deploy_nginx.yml
apiVersion: v1          
kind: Service
metadata:
  name: svc-nginx
  namespace: test

spec:
  type: ClusterIP        service默认访问方式
  ports:                 定义端口信息
  - port: 80             访问service使用的端口，可自定义
    targetPort: 80       pod中容器端口
  selector:              标签选择器（基于标签选择代理的Pod）
    app: deploy-nginx    标签（需要下方代理的Pod标签一致）

---
apiVersion: autoscaling/v1     #自动扩缩容版本
kind: HorizontalPodAutoscaler  #类型
metadata:
    name: hpa-nginx
    namespace: test
spec:
  minReplicas: 3             最小的pod数量
  maxReplicas: 10            #最大的pod数量
  targetCPUUtilizationPercentage: 6    cpu使用指标,表示60%
  scaleTargetRef:            #指定要控制的Pod控制器（deploy）信息
    apiVersion: apps/v1
    kind: Deployment         #deploy控制器类型
    name: deploy-nginx       #deploy控制器名称（要在k8s中存在）

---
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test

spec:
    replicas: 3                 创建pod的副本数量，默认为1
    selector:                   #标签选择器(基于选择器匹配Pod)
      matchLabels:              #标签类型
        app: deploy-nginx       #匹配pod的标签(表示deploy管理带有此标签的Pod)

    template:                   #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx     pod的标签

      spec:
        containers:
        - name: nginx
          image: nginx:1.17.0   #指定镜像
          ports:                #定义端口
          - containerPort: 80   #端口
            protocol: TCP       #端口协议
          resources:            #资源限额
            limits:             #资源上限
              cpu: 600m         cpu 1核心的60%的资源



      
创建Pod
[root@master01 ~]# kubectl create -f hpa-deploy_nginx.yml



查看pod详细信息
[root@master01 ~]# kubectl get pod -n test
[root@master01 ~]# kubectl get pod -n test -o wide



为了更好的验证用户请求被分配到哪个pod中，修改3个Pod中nginx默认首页为具体的Pod IP地址
[root@master01 ~]# kubectl exec -it deployment-6696798b78-6zl8p -n test /bin/bash

[root@master01 ~]# echo "10.244.1.44" > /usr/share/nginx/html/index.html



访问3个pod测试
[root@master01 ~]# curl http://10.244.1.44
10.244.1.44
[root@master01 ~]# curl http://10.244.2.24
10.244.2.24
[root@master01 ~]# curl http://10.244.1.45
10.244.1.45



查看svc信息
[root@master01 ~]# kubectl  get svc -n test
[root@master ~]# kubectl describe svc -n test
Name:              service
Namespace:         dev
Labels:            <none>
Annotations:       <none>
Selector:          app=nginx-pod
Type:              ClusterIP
IP:                10.96.96.96
Port:              <unset>  80/TCP
TargetPort:        80/TCP
Endpoints:         10.244.1.44:80,10.244.1.45:80,10.244.2.24:80   代理的pod地址
Session Affinity:  None
Events:            <none>



查看ipvs的映射规则
[root@master01 ~]# ipvsadm -Ln
...
TCP  10.96.96.96:80 rr
  -> 10.244.1.44:80               Masq    1      0          0         
  -> 10.244.1.45:80               Masq    1      0          0         
  -> 10.244.2.24:80               Masq    1      0          0    
#rr为默认轮询策略：当service接收到请求后，会通过轮询算法将请求分配到对应的三个pod中



访问测试
[root@master01 ~]# while :
do
     curl 10.96.96.96
    sleep 5
done

10.244.2.24
10.244.1.45
10.244.1.44
10.244.2.24
10.244.1.45
10.244.1.44



删除Pod
[root@master ~]# kubectl delete -f hpa-deploy_nginx.yml

```

**总结**：Cluster IP的访问方式只能用在集群内部主机之间访问，集群外部主机没办法访问。





#### NodePort 应用案例
在生产环境中，Service是需要暴露给外部访问的，那么就要用到NodePort类型的Service，NodePort的工作原理其实就是在Node节点上暴露一个端口，然后外部主机就可以通过节点IP+暴露端口来访问集群中的pod了



**案例**：将前边案例中的清单文件Cluster IP改为NodePort 类型，实现外部访问。

```yaml
[root@master01 ~]# vim hpa-deploy_nginx.yml
apiVersion: v1
kind: Service
metadata:
  name: svc-nginx
  namespace: test

spec:
  type: NodePort         service类型
  ports:                 #定义端口信息
  - port: 80             #访问service使用的端口，可自定义
    targetPort: 80       #指定pod中容器端口
    nodePort: 30007      #自定义service端口
  selector:              #标签选择器（基于标签选择代理的Pod）
    app: deploy-nginx    #标签（需要与代理的Pod标签一致）

---
apiVersion: autoscaling/v1     #自动扩缩容版本
kind: HorizontalPodAutoscaler  #类型
metadata:
    name: hpa-nginx
    namespace: test
spec:
  minReplicas: 3             #最小的pod数量
  maxReplicas: 10            #最大的pod数量
  targetCPUUtilizationPercentage: 6    #cpu使用指标,表示60%
  scaleTargetRef:            #指定要控制的nginx信息
    apiVersion: apps/v1
    kind: Deployment         #deploy类型
    name: deploy-nginx       #deploy名称

---
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test

spec:
    replicas: 3
    selector:                   #标签选择器(基于选择器匹配Pod)
      matchLabels:              #标签类型
        app: deploy-nginx       #匹配pod的标签(表示deploy管理带有此标签的Pod)

    template:                   #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx     #pod的标签

      spec:
        containers:
        - name: nginx
          image: nginx:1.17.0   #指定镜像
          ports:                #定义端口
          - containerPort: 80   #端口
            protocol: TCP       #端口协议
          resources:            #资源限额
            limits:             #资源上限
              cpu: 600m         #cpu 1核心的60%的资源



创建Pod
[root@master01 ~]# kubectl create -f hpa-deploy_nginx.yml



查看Pod信息
[root@master01 ~]# kubectl get pod -n test



查看Service信息
[root@master01 ~]# kubectl get svc -n test
NAME        TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
svc-nginx   NodePort   10.110.174.205   <none>        80:32388/TCP   13s
提示：
80     #Service端口
32388  #Service绑定的Node节点端口，这个端口是提供外部访问的



外部主机访问测试（通过宿主机主机IP加Node端口，访问集群中任何一台节点IP都可以）
http://192.168.0.13:32388



删除Pod
[root@master01 ~]# kubectl delete -f hpa-deploy_nginx.yml

```

