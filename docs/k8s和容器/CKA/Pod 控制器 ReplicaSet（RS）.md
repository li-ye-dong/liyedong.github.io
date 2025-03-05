#### <font style="color:rgb(51, 51, 51);">ReplicaSet（RS）特点介绍</font>
<font style="color:rgb(51, 51, 51);">ReplicaSet的主要作用是保证一定数量的pod能够正常的运行，它会持续监听这些pod的运行状态，一旦pod发生故障，就会重启或重建pod，同时还支持对pod数量的扩缩容和版本镜像的变更</font>

<font style="color:rgb(51, 51, 51);">ReplicaSet的资源清单文件查询方式</font>

<font style="color:rgb(119, 119, 119);">kubectl explain rs</font>

<font style="color:rgb(119, 119, 119);">kubectl explain rs.spec</font>

<font style="color:rgb(119, 119, 119);">kubectl explain rs.spec.selector</font>

<font style="color:rgb(119, 119, 119);">kubectl explain rs.spec.template</font>

<font style="color:rgb(119, 119, 119);">kubectl explain rs.spec.template.metadata</font>

<font style="color:rgb(119, 119, 119);">kubectl explain rs.spec.template.spec</font>

#### <font style="color:rgb(51, 51, 51);">ReplicaSet（RS）应用案例</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过RS控制器创建3个Nginx Pod</font>

```yaml
# vim rs_nginx.yml
apiVersion: v1     
kind: ReplicaSet        
metadata:               
    name: rs-nginx
    namespace: test     
spec:                   
    replicas: 3         #创建pod的副本数量，默认为1
    selector:           #标签选择器，通过它指定RS管理哪些pod
      matchLabels:      #标签类型（key=value）
        app: rs-nginx      #匹配pod的标签（表示deploy管理带有此标签的Pod）
    template:           #pod的配置模板，通过模板定义Pod中的容器
      metadata:
        labels:
          app: rs-nginx    #Pod的标签
      spec:
        containers:
        - name: nginx
          image: nginx:1.17.0

          
创建pod
# kubectl create -f rs_nginx.yml


查看pod详细信息
# kubectl get po -n test


过滤Pod标签
# kubectl describe pod -n test | grep Labels


查看pod控制器详细信息
# kubectl get rs -n test -o wide

DESIRED：期望的pod副本数量
CURRENT：当前的pod副本数量
READY：已经准备好提供服务的副本数量
```

#### <font style="color:rgb(51, 51, 51);">ReplicaSet（RS）扩缩容</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过RS控制器实现Pod数量的扩缩容功能</font>

```yaml
通过edit（配置文件形式）可直接修改pod的副本数量
# kubectl edit rs rs-nginx -n test
...
spec:
  replicas: 6     #直接根据需求修改pod的副本数量即可
  
  

查看pod信息
# kubectl get pod -n test
```

#### <font style="color:rgb(51, 51, 51);">ReplicaSet（RS）版本变更</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过RS控制器实现镜像版本变更</font>

```yaml
通过edit（配置文件形式）可直接修改镜像版本
# kubectl edit rs rs-nginx -n test
...
    spec:
      containers:
      - image: nginx:1.18.0   #修改为1.18.0版本


查看rs详细信息
# kubectl get rs -n test -o wide
```

<font style="color:rgb(51, 51, 51);">删除RS方式</font>

```yaml
命令删除方式
# kubectl delete rs rs-nginx -n test


查看rs信息
# kubectl get rs -n test


配置文件删除方式
# kubectl delete -f rs-nginx.yml
```

  
 

