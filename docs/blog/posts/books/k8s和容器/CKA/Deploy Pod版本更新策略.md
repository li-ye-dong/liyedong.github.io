<font style="color:rgb(51, 51, 51);">Deploy支持两种镜像更新的策略：通过strategy属性进行配置</font>

<font style="color:rgb(119, 119, 119);">kubectl explain deploy.spec.strategy</font>

+ <font style="color:rgb(51, 51, 51);">Recreate：重建更新策略，一次性将所有旧版本pod全部重建成新版本pod</font>
+ <font style="color:rgb(51, 51, 51);">RollingUpdat：滚动更新策略（默认策略），先删除一部分旧版本pod，在更新成新版本pod</font>

```yaml
下面是对strategy属性的详细描述

strategy:          #指定新的pod替换旧的pod策略，支持两个属性
  type:            #指定策略类型，支持两种策略
    Recreate:      #在创建出新pod之前会先删掉所有已经存在的pod
    RollingUpdat:  #滚动更新，先删除一部分，就启动一部分pod，在更新过程中，存在两个版本pod
  rollingUpdate:   #当type为RollingUpdat时生效，用于为RollingUpdat设置参数，支持两个属性
    maxUnavailable:  #用来指定在升级过程中最多可删除的pod数量，默认为25%
    maxSurge:        #用来指定在升级过程中最多可新建的pod数量，默认为25%
```

  
 

#### <font style="color:rgb(51, 51, 51);">Pod版本更新 Recreate</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过Recreate对Pod进行重建更新</font>

```yaml
修改deploy_nginx.yml文件设置Pod更新策略

# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test
spec:
    strategy:          # Pod更新策略
      type: Recreate   # 重建更新
    replicas: 3        # 指定Pod数量

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
          image: nginx:1.18.0       
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议



创建pod
# kubectl create -f deploy_nginx.yml


另外开一个终端动态观察pod的信息
# kubectl get pod -n test -w


更新镜像版本
# kubectl edit deploy deploy-nginx -n test
...
    spec:
      containers:
      - image: nginx:1.18.1    指定新版本
#或者编辑配置文件，直接apply

提示：观察pod的重建过程
#第一步：将Running的pod先终止（Terminating）

#第二步：接下来Pod处于等待状态（Pending）

#第三步：重新创建容器（ContainerCreating）

#第四步：新的容器被创建且以成功运行（Running ）


查看镜像版本
# kubectl get deploy -n test -o wide


删除depoly
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod版本更新 RollingUpdate</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过RollingUpdat对Pod进行滚动更新（默认策略，无需指定，只需要将前边配置文件中的其他更新策略删除即可）</font>

```yaml
# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test
spec:
    replicas: 6 
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
          image: nginx:1.18.1
          imagePullPolicy: IfNotPresent    #镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议



创建pod（--record 记录整个deploy更新历史）
# kubectl create -f deploy_nginx.yml --record




另外一个终端动态查看pod信息
# kubectl get pod -n test -w



更新镜像版本
# kubectl edit deploy deploy-nginx -n test
    spec:
      containers:
      - image: nginx:1.20.0
#或者编辑配置文件，直接apply



查看RS信息
# kubectl get rs -n test -o wide

提示：当pod滚动更新后，rs也会随之跟着更新，原有rs中的pod会被删除，但是原有的rs并不会删除，用于做版本回退


显示当前升级版本的状态
# kubectl rollout status deploy deploy-nginx -n test
```

  
 

