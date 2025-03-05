#### <font style="color:rgb(51, 51, 51);">Pod概念介绍</font>
<font style="color:rgb(51, 51, 51);">Pod（碗豆菜）是kubernetes集群进行管理的最小单元，程序必须部署在容器中，而容器必须存在于Pod中，kubernetes集群启动以后，集群中的各个组件也都是以Pod方式运行。</font>

| <font style="color:rgb(51, 51, 51);">Pod可以认为是容器的封装，一个Pod中可以存在一个或多个容器，这些容器共享Pod中的存储、网络等资源，所以我们可以把Pod看做一台物理服务器一样（Pod不是进程，而是容器运行的环境），其中包含一个或多个应用容器， 这些容器中运行着用户应用程序。</font> |
| :--- |
| <font style="color:rgb(51, 51, 51);">举例说明Pod、Container、应用程序三者之间的关系：麻屋子,红帐子,里面住着白胖子。Pod就是麻屋子,Container就是红帐子,应用程序就是里面的白胖子。</font> |


**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：在test空间下创建并运行一个nginx的pod</font>

| **<font style="color:rgb(51, 51, 51);">命令</font>** | **<font style="color:rgb(51, 51, 51);">作用</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">run</font> | <font style="color:rgb(51, 51, 51);">在集群中运行一个Pod</font> |


```bash
# kubectl run nginx --image=nginx:1.18.0  -n test 


查看test下的pod信息
# kubectl get pod -n test


查看nginx内部信息
# kubectl describe  pod nginx -n test


删除test空间下的nginx
# kubectl delete pod nginx -n test
# kubectl get pod  -n test
```

#### <font style="color:rgb(51, 51, 51);">Pod案例演示</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过yaml文件在test空间创建一个nginx的pod</font>

<font style="color:rgb(119, 119, 119);">kubectl explain pod </font>

<font style="color:rgb(119, 119, 119);">kubectl explain pod.metadata </font>

<font style="color:rgb(119, 119, 119);">kubectl explain pod.spec </font>

<font style="color:rgb(119, 119, 119);">kubectl explain pod.spec.containers</font>

```bash
# vim nginx.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: test
spec:
  containers:
  - name: nginx
    image: nginx:1.18.0
```

```bash
执行test_ngx_pod.yaml文件创建资源
# kubectl create -f nginx.yaml


查看pod信息
# kubectl get pod -n test


通过yaml文件查看资源
# kubectl get -f nginx.yaml
```

  
 

