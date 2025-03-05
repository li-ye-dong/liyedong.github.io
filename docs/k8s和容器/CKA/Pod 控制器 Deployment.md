<font style="color:rgb(51, 51, 51);">为了更好的解决服务编排问题，k8s在v1.2版本开始，引入了Deployment（Deploy）控制器，该pod控制器不会去直接管理pod，而是通过管理ReplicaSet来间接的管理pod，所以Deployment比ReplicaSet功能更强大</font>

**<font style="color:rgb(51, 51, 51);">Deployment功能如下</font>**<font style="color:rgb(51, 51, 51);">：</font>

+ <font style="color:rgb(51, 51, 51);">支持RS所有功能</font>
+ <font style="color:rgb(51, 51, 51);">支持发布的停止、继续</font>
+ <font style="color:rgb(51, 51, 51);">支持版本滚动更新和版本回退</font>

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过deploy创建基本的pod</font>

```yaml
# vim deploy_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test
spec:
    replicas: 3       #创建pod的副本数量，默认为1
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
          image: nginx:1.17.0


创建deploy
# kubectl create -f deplo_nginx.yml


查看deploy详细信息
# kubectl get deploy -n test
# kubectl get deploy -n test -o wide

UP-TO-DATE：最新版本的pod数量
AVAILABLE：当前可用的pod数量



查看rs控制器信息，应为deploy通过控制rs管理pod，所以rs控制器也会被创建出来（rs的名称在deploy基础上随机添加）
# kubectl get rs -n test 



查看pod信息（pod名称是在rs基础上随机添加）
# kubectl get po -n test


过滤Pod标签
# kubectl describe pod -n test | grep Labels

删除deploy
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod 镜像拉取策略</font>
<font style="color:rgb(51, 51, 51);">imagePullPolicy用于设置镜像拉取策略，k8s支持三种拉取策略，可通过下边命令查看：</font>

```yaml
# kubectl explain pod.spec.containers.imagePullPolicy
- Always       总是从远程仓库拉取镜像
- IfNotPresent 本地有则使用本地镜像，本地没有则从远程仓库拉取镜像
- Never        只使用本地镜像，从不去远程仓库拉取，本地如果没有就报错
```

<font style="color:rgb(119, 119, 119);">默认值说明：如果镜像标签为具体版本号，默认策略是IfNotPresent，如果镜像标签为latest，默认策略是Always</font>

#### <font style="color:rgb(51, 51, 51);">Pod 镜像拉取策略 Never</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：创建pod，并指定镜像拉取策略为Never，只使用本地镜像，从不去远程仓库拉取，本地如果没有就报错。</font>

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
          image: nginx:1.20.0       指定一个本地不存的镜像版本
          imagePullPolicy: Never    设置镜像拉取策略



创建pod
# kubectl create -f deploy_nginx.yml


查看pod信息
# kubectl get pod -n test


查看pod详细描述信息
# kubectl describe pod -n test


删除deploy
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod 镜像拉取策略 IfNotPresent</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：创建pod，并指定镜像拉取策略为IfNotPresent，本地有则使用本地镜像，本地没有则从远程仓库拉取镜像</font>

```yaml
基于上边的案例，将策略改为IfNotPresent即可

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
          image: nginx:1.20.0       
          imagePullPolicy: IfNotPresent    设置镜像拉取策略



创建pod
# kubectl create -f deploy_nginx.yml


查看pod信息
# kubectl get pod -n test


查看pod详细信息
# kubectl describe pod -n test


删除deploy
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod 端口设置</font>
<font style="color:rgb(51, 51, 51);">ports属性用于配置容器需要暴露的端口列表</font>

```yaml
通过下边命令可以获取ports可以使用的子属性

# kubectl explain pod.spec.containers.ports
containerPort   容器要监听的端口（必须）
name            端口名称，如果指定，必须保证名称在该pod中是唯一的（一般不省略）
hostPort        容器要在主机上公开的端口（一般省略）
hostIP          要将外部端口帮定到的主机IP（一般省略）
protocol        端口协议，必须是TCP、UDP或SCTP，默认为TCP
```

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：创建Pod并指定容器暴露80端口</font>

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
          image: nginx:1.20.0       
          imagePullPolicy: IfNotPresent    #设置镜像拉取策略
          ports:                #定义容器端口
          - containerPort: 80   端口（必须为数组类型）
            protocol: TCP       端口协议



创建pod
# kubectl create -f deploy_nginx.yml


查看pod信息
# kubectl get pod -n test



查看pod描述信息
# kubectl describe pod  -n test
...

    Port:           80/TCP



访问pod中的容器需要访问pod的IP加容器端口
# curl 10.244.2.30:80


删除deploy
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod 资源配额</font>
<font style="color:rgb(51, 51, 51);">resources属性用于限制Pod中的容器对系统的资源的使用量（资源配额），避免容器出现问题大量吞噬系统资源，k8s目前提供了对</font>**<font style="color:rgb(51, 51, 51);">内存</font>**<font style="color:rgb(51, 51, 51);">和</font>**<font style="color:rgb(51, 51, 51);">CPU</font>**<font style="color:rgb(51, 51, 51);">的资源限制</font>

<font style="color:rgb(51, 51, 51);">当我们对Pod中的容器配置资源限额以后，如果容器超出资源使用量，k8s则会认位该容器出现故障，则重新启动该容器</font>

```yaml
resources属性提供了两个子属性用于资源限制，可通过下边命令查看

# kubectl explain pod.spec.containers.resources

limits    #资源上限：限制容器运行时最大的资源使用量，当容器超出该使用量时，容器会被终止，并进行重启

requests  #资源下限：用于限制容器需要的最小资源，如果环境资源不够，容器将无法启动
```

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：创建pod并设置容器资源的上下限</font>

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
          image: nginx:1.20.0       
          imagePullPolicy: IfNotPresent   #设置镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: T
            CP      #端口协议
          resources:           #定义资源限额
            limits:            #资源最大限额
              cpu: 2           #cpu核数最大限制（可以为整数或小数）
              memory: 2G       #内存最大限制（单位可以使用Gi、Mi、G、M等形式）
            requests:          #资源最低限额
              cpu: 1           #所需最低cpu核数
              memory: 10M      #所需最低内存资源（如果不足10M,容器无法启动）



创建pod
# kubectl create -f deploy_nginx.yml


查看pod信息
# kubectl get pod -n test


查看pod描述信息
# kubectl describe pod -n test
...

    Limits:
      cpu:     2
      memory:  2G
    Requests:
      cpu:        1
      memory:     10M
      

删除deploy
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod 多容器创建方式</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：将nginx与mysql放在同一个Pod中运行</font>

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
          image: nginx:1.20.0       #指定一个本地不存的镜像版本
          imagePullPolicy: IfNotPresent    #设置镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议
          resources:           #定义资源限额
            limits:            #资源最大限额
              cpu: 2           #cpu核数最大限制（可以为整数或小数）
              memory: 2G       #内存最大限制（单位可以使用Gi、Mi、G、M等形式）
            requests:          #资源最低限额
              cpu: 1           #所需最低cpu核数
              memory: 10M      #所需最低内存资源（如果不足10M,容器无法启动）


        - name: mysql
          image: mysql:5.7     #镜像版本
          imagePullPolicy: IfNotPresent    #设置镜像拉取策略
          ports:                 #定义端口
          - containerPort: 3306  #端口
            protocol: TCP      #端口协议
          resources:           #定义资源限额
            limits:            #资源最大限额
              cpu: 2           #cpu核数最大限制（可以为整数或小数）
              memory: 2G       #内存最大限制（单位可以使用Gi、Mi、G、M等形式）
            requests:          #资源最低限额
              cpu: 1           #所需最低cpu核数
              memory: 10M      #所需最低内存资源（如果不足10M,容器无法启动）



创建Pod
# kubectl create -f deploy_nginx.yml


查看Pod信息
# kubectl get pod -n test


查看Pod描述信息
# kubectl describe pod   -n test

#原因分析：MySQL以容器的方式运行需要设置环境变量（root密码）



删除该Pod
# kubectl delete -f deploy_nginx.yml
```

#### <font style="color:rgb(51, 51, 51);">Pod 环境变量</font>
<font style="color:rgb(51, 51, 51);">evn属性是用于设置容器环境变量的列表，环境变量的定义要根据容器具体需求定义，本章节只讲解如何定义环境变量</font>

```yaml
可通过下方命令获取env文档帮助

# kubectl explain pod.spec.containers.env

 name   定义环境变量名称
 value  定义变量值
```

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：为上述案例中的MySQL添加环境变量设置root密码</font>

```yaml
# vim pod-ngx_mysql.yml
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
          image: nginx:1.20.0       #指定一个本地不存的镜像版本
          imagePullPolicy: IfNotPresent    #设置镜像拉取策略
          ports:               #定义端口
          - containerPort: 80  #端口
            protocol: TCP      #端口协议
          resources:           #定义资源限额
            limits:            #资源最大限额
              cpu: 2           #cpu核数最大限制（可以为整数或小数）
              memory: 2G       #内存最大限制（单位可以使用Gi、Mi、G、M等形式）
            requests:          #资源最低限额
              cpu: 1           #所需最低cpu核数
              memory: 10M      #所需最低内存资源（如果不足10M,容器无法启动）


        - name: mysql
          image: mysql:5.7     #镜像版本
          imagePullPolicy: IfNotPresent    #设置镜像拉取策略
          ports:                 #定义端口
          - containerPort: 3306  #端口
            protocol: TCP      #端口协议
          resources:           #定义资源限额
            limits:            #资源最大限额
              cpu: 2           #cpu核数最大限制（可以为整数或小数）
              memory: 2G       #内存最大限制（单位可以使用Gi、Mi、G、M等形式）
            requests:          #资源最低限额
              cpu: 1           #所需最低cpu核数
              memory: 10M      #所需最低内存资源（如果不足10M,容器无法启动）
          env:                             定义环境变量
          - name: "MYSQL_ROOT_PASSWORD"    变量名称（必须为数组类型）
            value: "123456"                #值




创建Pod
# kubectl create -f deploy_nginx.yml



查看Pod信息
# kubectl get pod -n test



查看Pod详细描述
# kubectl describe pod  -n test
```

#### <font style="color:rgb(51, 51, 51);">Pod 容器进入方式</font>
<font style="color:rgb(51, 51, 51);">格式：</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl exec -n 命名空间 -it pod名称 -c 容器名称 -- /bin/bash</font>`

<font style="color:rgb(119, 119, 119);">kubectl exec -h #命令帮助</font>

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：进入上述案例中创建的mysql容器</font>

```yaml
# kubectl exec -n test -it deploy-nginx-579696c576-jfqz6 -c mysql -- /bin/bash

进入数据库
root@deploy-nginx-579696c576-jfqz6:/# mysql -uroot -p123456
```

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：进入上述案例中创建的nginx容器</font>

```yaml
# kubectl exec -n test -it deploy-nginx-579696c576-jfqz6 -c nginx -- /bin/bash


查看网页根目录
root@deploy-nginx-579696c576-jfqz6:/# ls /usr/share/nginx/
```

#### <font style="color:rgb(51, 51, 51);">Pod 容器执行命令方式</font>
<font style="color:rgb(51, 51, 51);">格式为: </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl exec pod名 -c 容器名 -- 命令</font>`

**<font style="color:rgb(51, 51, 51);">注意:</font>**

+ <font style="color:rgb(51, 51, 51);">-c 容器名为可选项,如果是1个pod中1个容器,则不用指定;</font>
+ <font style="color:rgb(51, 51, 51);">如果是1个pod中多个容器,不指定默认为第1个。</font>

```yaml
# kubectl exec -n test deploy-nginx-579696c576-jfqz6 -c nginx -- ls /usr/share/nginx/html

# kubectl exec -n test deploy-nginx-579696c576-jfqz6 -c mysql -- ls /var/lib/mysql
```

<font style="color:rgb(51, 51, 51);">删除deploy</font>

```yaml
# kubectl delete -f deploy_nginx.yml
```

  
 

