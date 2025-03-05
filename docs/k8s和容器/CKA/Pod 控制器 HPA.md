# Pod 控制器 HPA
#### HPA 介绍
Horizontal Pod Autoscaler（HPA）可以实现pod数量的自动扩缩容，对比于前边手动对pod数量进行调整，HPA更加的智能。

HPA可以获取每个pod的资源利用率，然后和HPA中定义的资源利用率指标进行对比，同时计算出需要伸缩的具体值，最后实现pod的数量的自动（非手动）调整。

#### metrics-server 资源监控
Metrics-Server是集群核心监控数据的监视器，用于采集节点的CPU和内存资源，从 Kubernetes1.8 开始用来替换之前的heapster，heapster从1.11开始逐渐被废弃。



安装metrics-server可以用来收集集群中的资源使用情况（已经下载，拷贝到主机即可）

```yaml
[root@master01 ~]# wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

文件内容需要修改
#vim components.yaml
...
      - args:
        - --kubelet-insecure-tls     添加该参数忽略证书检测


          
创建metrics-server
[root@master01 ~]# kubectl create -f components.yaml



查看metrics-server运行状态
[root@master01 ~]# kubectl get pod -n kube-system


通过top命令查看节点监控数据：kubectl top  node/pod
[root@master01 ~]# kubectl top node
[root@master01 ~]# kubectl top pod -n kube-system

```

到此为止metrics-server安装成功。

#### HPA 应用案例
**案例**：创建HPA，通过HPA对Pod数量进行弹性自动伸缩

> 通过下边命令可以获取HPA支持的配置属性  
kubectl explain hpa.spec
>

```yaml
[root@master01 ~]# vim hpa-deploy_nginx.yml
apiVersion: autoscaling/v1         #自动扩缩容版本
kind: HorizontalPodAutoscaler
metadata:
    name: hpa-nginx
    namespace: test

spec:
  minReplicas: 1                     #最小的pod数量
  maxReplicas: 10                    #最大的pod数量
  targetCPUUtilizationPercentage: 1  #cpu使用指标,表示10%（生产环境建议定义在6-8）
  scaleTargetRef:              #指定要控制的deploy信息
    apiVersion: apps/v1        #deploy版本
    kind: Deployment           #deploy类型
    name: deploy-nginx         #deploy名称


---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-nginx
  namespace: test

spec:
  selector:                  #标签选择器(基于选择器匹配Pod)
    matchLabels:
      app: deploy-nginx      #标签  

  template:                  #创建Pod模板
    metadata:
      labels:
        app: deploy-nginx    #pod的标签

    spec:
      tolerations:
      - key: worker01
        effect: NoSchedule
      containers:
      - name: nginx
        image: nginx:1.17.0
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 80
        resources:            #资源限额
          limits:             #资源上限
            cpu: 100m         #cpu 1核心的10%的资源（生产环境建议600m-800m）



创建HPA类型的deploy
[root@master01 ~]# # kubectl create -f hpa-deploy_nginx.yml



查看信息
[root@master01 ~]# kubectl get deploy,pod,hpa -n test
```





#### HAP 弹性伸缩
```shell
另开终端动态查看pod信息
[root@master01 ~]# kubectl get po -n test -w


查看Pod地址
# kubectl get pod -n test -o wide


通过压力测试工具访问Pod地址进行压力测试
[root@master01 ~]# yum -y install httpd-tools
[root@master01 ~]# ab -n 300000 -c 100 http://10.244.30.104/index.html

 -n  请求的总数量
 -c  并发数量
```

