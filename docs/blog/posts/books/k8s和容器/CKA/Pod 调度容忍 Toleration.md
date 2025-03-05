<font style="color:rgb(51, 51, 51);">上章节讲解了污点的作用，可以通过在worker节点添加污点用于拒绝pod调度上来，但如果我们非要将一个pod调度到一个有污点的node上，通过容忍（忽略）可以实现</font>

<font style="color:rgb(51, 51, 51);">容忍的配置项说明:</font>

```yaml
可通过下边命令查看容器的配置项
# kubectl explain pod.spec.tolerations
effect              容忍的污点
key                 容忍的污点的key
```

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：继上述案例，创建pod并添加容忍，然后将pod调度到worker01节点</font>

```yaml
# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test

spec:
    replicas: 1
    selector:                   #标签选择器(基于选择器匹配Pod)
      matchLabels:              #标签类型
        app: deploy-nginx       #匹配pod的标签(表示deploy管理带有此标签的Pod)

    template:                   #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx     #pod的标签

      spec:
        tolerations:            添加容忍
        - key: "worker01"       污点的key（必须引起来）
          effect: NoSchedule    污点类型
        containers:
        - name: nginx
          image: nginx:1.17.0   #指定镜像
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:                #定义端口
          - containerPort: 80   #端口
            protocol: TCP       #端口协议



创建pod
# kubectl create -f deploy_nginx.yml



查看pod详细信息
# kubectl describe pod -n test


删除deploy并删除yaml文件中的容忍配置项
# kubectl delete -f deploy_nginx.yml


删除污点
# kubectl taint node worker01 worker01:NoSchedule-
```

<font style="color:rgb(51, 51, 51);">Pod或者ns出现异常,可以尝试通过下边的方式进行删除</font>

```yaml
# kubectl delete pod pod名称 -n ns名称 --force --grace-period=0
```

  
 

