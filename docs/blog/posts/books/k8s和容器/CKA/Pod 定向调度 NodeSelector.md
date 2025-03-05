<font style="color:rgb(51, 51, 51);">nodeSelector用于将pod调度到添加了指定标签的node节点上，该调度规则也是强制调度</font>

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：先为worker02节点打标签，然后创建一个pod，并通过nodeSelector进行调度</font>

```yaml
为node1与node2节点打标签
# kubectl label node worker02 node=worker02


查看节点标签
# kubectl get node worker02 --show-labels


创建Pod并通过NodeSelector进行调度
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
        nodeSelector:          定义nodeSelector
          node: worker02       指定节点标签
        containers:
        - name: nginx
          image: nginx:1.20.0       #指定一个本地不存的镜像版本
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议



创建pod
# kubectl create -f deploy_nginx.yml


查看pod详细信息
# kubectl get pod -n test
# kubectl get pod -n test -o wide


删除deploy
# kubectl delete -f deploy_nginx.yml
```

  
 

