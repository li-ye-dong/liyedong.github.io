<font style="color:rgb(51, 51, 51);">容器探测类似于对容器进行健康检查，用来探测容器中的程序是否可以正常工作，如果探测到容器出现故障，k8s会尝试重启容器，如果重启失败，k8s不会将流量分配给该容器，不承担业务流量。</font>

<font style="color:rgb(51, 51, 51);">k8s提供了两种探针来实现容器的探测，可通过下边命令查看：</font>

```yaml
# kubectl explain pod.spec.containers  

livenessProbe   存活性探针，用于检测容器当前是否处于正常运行状态，如果不是，容器将会被重启。

readinessProbe  就绪性探针，用于检测容器当前是否可以接收请求，如果不能，k8s不会转发流量。
```

<font style="color:rgb(51, 51, 51);">以上两种探针目前均支持多种探测方式，可通过下边命令查看：</font>

```yaml
# kubectl explain pod.spec.containers.livenessProbe
# kubectl explain pod.spec.containers.readinessProbe
FIELDS:
exec                    命令探测方式
tcpSocket               端口探测方式
httpGet                 URL请求探测方式
initialDelaySeconds     容器启动后等待多少秒执行第一次探测
timeoutSeconds          探测超时时间，默认1秒，最小可设置1秒
failureThreshold        连续探测失败多少次才被认定失败，默认3次为失败，最小可设置1
periodSeconds           执行探测频率，默认是10秒，最小可设置1秒
successThreshold        连续探测成功多少次才被认定为成功，默认1次
```

  
 **<font style="color:rgb(51, 51, 51);">以livenessProbe存活性探针给大家介绍两种常用的探测方式：</font>**

#### <font style="color:rgb(51, 51, 51);">Pod 容器探测 exec</font>
<font style="color:rgb(51, 51, 51);">方式一：exec命令探测方式，在容器内执行一次命令，如果命令执行的退出码为0，则认位程序正常，否则不正常。</font>

```yaml
# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test
spec:
    replicas: 1
    selector:         #标签选择器(基于选择器匹配Pod)
      matchLabels:    #标签类型
        app: deploy-nginx    #匹配pod的标签(表示deploy管理带有此标签的Pod)
    template:         #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx   #pod的标签
      spec:
        containers:
        - name: nginx
          image: nginx:1.18.0       #镜像版本
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议
          livenessProbe:       存活性探针
            exec:              命令探测方式
              command: [/bin/ls,/etc/hello.txt]  探测一个不存在的文件


               
创建Pod
# kubectl create -f deploy_nginx.yml


查看Pod信息
# kubectl get pod -n test


查看Pod详细信息
# kubectl describe pod -n test


删除deploy
# kubectl delete -f deploy_nginx.yml



探测一个存在的文件
# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test
spec:
    replicas: 1
    selector:         #标签选择器(基于选择器匹配Pod)
      matchLabels:    #标签类型
        app: deploy-nginx    #匹配pod的标签(表示deploy管理带有此标签的Pod)
    template:         #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx   #pod的标签
      spec:
        containers:
        - name: nginx
          image: nginx:1.18.0       #镜像版本
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议
          livenessProbe:       存活性探针
            exec:              命令探测方式
              command: [/bin/ls,/usr/share/nginx/html/index.html]  探测一个存在的文件



创建Pod
# kubectl create -f deploy_nginx.yml


查看Pod详细信息
# kubectl describe pod -n test


删除Deploy
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod 容器探测 tcpSocket</font>
<font style="color:rgb(51, 51, 51);">方式二：tcpSocket端口探测方式，访问容器的端口，如果能够建立连接，则认位程序正常，否则不正常。</font>

```yaml
# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test
spec:
    replicas: 1
    selector:         #标签选择器(基于选择器匹配Pod)
      matchLabels:    #标签类型
        app: deploy-nginx    #匹配pod的标签(表示deploy管理带有此标签的Pod)
    template:         #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx   #pod的标签
      spec:
        containers:
        - name: nginx
          image: nginx:1.18.0       #镜像版本
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议
          livenessProbe:       存活性探针
            tcpSocket:         端口探测方式
              port: 8080       探测一个不存在的端口

提示：删除前边的探测方式，探测方式不能指定超过2种类型



创建pod
# kubectl create -f deploy_nginx.yml


查看pod描述信息
# kubectl describe pod -n test
...
Liveness probe failed: dial tcp 10.244.1.10:8080: connect: connection refused
#提示：活性探针失败，8080拒绝连接


删除deploy
# kubectl delete -f deploy_nginx.yml


探测一个存在的端口
# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test
spec:
    replicas: 1
    selector:         #标签选择器(基于选择器匹配Pod)
      matchLabels:    #标签类型
        app: deploy-nginx    #匹配pod的标签(表示deploy管理带有此标签的Pod)
    template:         #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx   #pod的标签
      spec:
        containers:
        - name: nginx
          image: nginx:1.18.0       #镜像版本
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议
          livenessProbe:       存活性探针
            tcpSocket:         端口探测方式
              port: 80         探测一个存在的端口



创建pod
# kubectl create -f deploy_nginx.yml



查看pod详细信息
# kubectl describe -f deploy_nginx.yml


删除deploy
# kubectl delete -f deploy_nginx.yml
```

  
 

