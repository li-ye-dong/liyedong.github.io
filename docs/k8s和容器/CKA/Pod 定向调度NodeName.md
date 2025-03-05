<font style="color:rgb(51, 51, 51);">定向调度是通过在pod上声明NodeName或者NodeSelector，以此将pod调度到指定的节点上，但是定向调度属于强制调度，即使指定的Node节点不存在，也会向该节点进行调度，只不过pod运行失败而已</font>

<font style="color:rgb(51, 51, 51);">定向调度方式其实是直接跳过了Scheduler的调度逻辑，直接将pod调度到指定名称的节点</font>

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：创建pod，并通过NodeName将Pod调度到worker01节点</font>

<font style="color:rgb(119, 119, 119);">kubectl explain pod.spec.nodeName</font>

```yaml
# vim pod-nodename.yml
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
        nodeName: worker01   定义调度策略，并指定worker01节点
        containers:
        - name: nginx
          image: nginx:1.20.0       #指定一个本地不存的镜像版本
          imagePullPolicy: IfNotPresent    #设置镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议


    
创建pod
# kubectl create -f deploy_nginx.yml


查看pod详细信息
# kubectl get pod -n test -o wide


删除deploy
```

<font style="color:rgb(51, 51, 51);">  
</font><font style="color:rgb(51, 51, 51);"> </font>

