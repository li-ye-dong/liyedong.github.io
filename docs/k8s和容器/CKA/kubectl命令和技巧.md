<font style="color:rgb(51, 51, 51);">kubernetes的本质就是一个集群系统，用户可以在集群中部署各种服务，所谓部署服务就是在kubernetes集群中运行一个一个的容器，并将指定的程序跑在容器中</font>

<font style="color:rgb(51, 51, 51);">在kubernetes中，所有内容都被抽象为资源对象，学习kubernetes主要学习如何管理资源对象</font>

```shell
所有资源可通过下面命令进行查看
kubectl  api-resources
```

#### <font style="color:rgb(51, 51, 51);">K8s资源类型介绍</font>
| **<font style="color:rgb(51, 51, 51);">资源名称</font>** | **<font style="color:rgb(51, 51, 51);">缩写</font>** | **<font style="color:rgb(51, 51, 51);">资源作用</font>** |
| :--- | :--- | :--- |
| <font style="color:rgb(51, 51, 51);">nodes</font> | <font style="color:rgb(51, 51, 51);">no</font> | <font style="color:rgb(51, 51, 51);">集群组成部分</font> |
| <font style="color:rgb(51, 51, 51);">namespaces</font> | <font style="color:rgb(51, 51, 51);">ns</font> | <font style="color:rgb(51, 51, 51);">隔离pod</font> |
| <font style="color:rgb(51, 51, 51);">pods</font> | <font style="color:rgb(51, 51, 51);">po,pod</font> | <font style="color:rgb(51, 51, 51);">装载容器</font> |
| <font style="color:rgb(51, 51, 51);">replicationcontrollers</font> | <font style="color:rgb(51, 51, 51);">rc</font> | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">replicasets</font> | <font style="color:rgb(51, 51, 51);">rs</font> | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">deployments</font> | <font style="color:rgb(51, 51, 51);">deploy</font> | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">daemonsets</font> | <font style="color:rgb(51, 51, 51);">ds</font> | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">jobs</font> | | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">cronjobs</font> | <font style="color:rgb(51, 51, 51);">cj</font> | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">horizontalpodautoscalers</font> | <font style="color:rgb(51, 51, 51);">hpa</font> | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">statefulsets</font> | <font style="color:rgb(51, 51, 51);">sts</font> | <font style="color:rgb(51, 51, 51);">控制pod资源</font> |
| <font style="color:rgb(51, 51, 51);">services</font> | <font style="color:rgb(51, 51, 51);">svc</font> | <font style="color:rgb(51, 51, 51);">统一pod对外接口</font> |
| <font style="color:rgb(51, 51, 51);">ingress</font> | <font style="color:rgb(51, 51, 51);">ing</font> | <font style="color:rgb(51, 51, 51);">统一pod对外接口</font> |
| <font style="color:rgb(51, 51, 51);">volumeattachments</font> | | <font style="color:rgb(51, 51, 51);">存储资源</font> |
| <font style="color:rgb(51, 51, 51);">persistentvolumes</font> | <font style="color:rgb(51, 51, 51);">pv</font> | <font style="color:rgb(51, 51, 51);">存储资源</font> |
| <font style="color:rgb(51, 51, 51);">persistentvolumeclaims</font> | <font style="color:rgb(51, 51, 51);">pvc</font> | <font style="color:rgb(51, 51, 51);">存储资源</font> |
| <font style="color:rgb(51, 51, 51);">configmaps</font> | <font style="color:rgb(51, 51, 51);">cm</font> | <font style="color:rgb(51, 51, 51);">配置资源</font> |
| <font style="color:rgb(51, 51, 51);">secrets</font> | | <font style="color:rgb(51, 51, 51);">配置资源</font> |


#### <font style="color:rgb(51, 51, 51);">k8s集群管理方式介绍</font>
<font style="color:rgb(51, 51, 51);">直接使用kubectl命令去管理k8s集群</font>

kubectl run nginx-pod --image=nginx:1.17.4 --port=80

<font style="color:rgb(51, 51, 51);">将配置写入到yaml文件，通过文件去管理k8s集群</font>

kubectl create/patch -f nginx-pod.yaml

#### <font style="color:rgb(51, 51, 51);">kubectl命令介绍</font>
**<font style="color:rgb(51, 51, 51);">kubectl命令</font>**<font style="color:rgb(51, 51, 51);">：是kubernetes集群的命令行工具，通过它能过够对集群本身进行管理，并能够在集群上进行容器化应用的安装部署。</font>

```shell
获取命令帮助
kubectl --help
```

**<font style="color:rgb(51, 51, 51);">kubectl常用命令如下</font>**

| **<font style="color:rgb(51, 51, 51);">命令</font>** | **<font style="color:rgb(51, 51, 51);">作用</font>** |
| :--- | :--- |
| <font style="color:rgb(65, 131, 196);">create</font> | <font style="color:rgb(65, 131, 196);">创建一个资源</font> |
| <font style="color:rgb(65, 131, 196);">edit</font> | <font style="color:rgb(65, 131, 196);">编辑一个资源</font> |
| <font style="color:rgb(65, 131, 196);">get</font> | <font style="color:rgb(65, 131, 196);">获取一个资源</font> |
| <font style="color:rgb(51, 51, 51);">patch</font> | <font style="color:rgb(51, 51, 51);">更新一个资源</font> |
| <font style="color:rgb(65, 131, 196);">delete</font> | <font style="color:rgb(65, 131, 196);">删除一个资源</font> |
| <font style="color:rgb(65, 131, 196);">explain</font> | <font style="color:rgb(65, 131, 196);">展示资源文档</font> |
| <font style="color:rgb(51, 51, 51);">run</font> | <font style="color:rgb(51, 51, 51);">在集群中运行一个指定的镜像</font> |
| <font style="color:rgb(51, 51, 51);">expose</font> | <font style="color:rgb(51, 51, 51);">暴露资源为service</font> |
| <font style="color:rgb(65, 131, 196);">describe</font> | <font style="color:rgb(65, 131, 196);">显示资源内部信息</font> |
| <font style="color:rgb(65, 131, 196);">logs</font> | <font style="color:rgb(65, 131, 196);">输出容器在pod中的日志</font> |
| <font style="color:rgb(51, 51, 51);">attach</font> | <font style="color:rgb(51, 51, 51);">进入运行中的容器</font> |
| <font style="color:rgb(51, 51, 51);">exec</font> | <font style="color:rgb(51, 51, 51);">执行容器中的一个命令</font> |
| <font style="color:rgb(51, 51, 51);">cp</font> | <font style="color:rgb(51, 51, 51);">在pod内外复制文件</font> |
| <font style="color:rgb(51, 51, 51);">rollout</font> | <font style="color:rgb(51, 51, 51);">管理资源的发布</font> |
| <font style="color:rgb(51, 51, 51);">scale</font> | <font style="color:rgb(51, 51, 51);">扩(缩)容pod的数量</font> |
| <font style="color:rgb(51, 51, 51);">autoscale</font> | <font style="color:rgb(51, 51, 51);">自动调整pod的数量</font> |
| <font style="color:rgb(65, 131, 196);">apply</font> | <font style="color:rgb(65, 131, 196);">通过文件对资源进行配置</font> |
| <font style="color:rgb(51, 51, 51);">label</font> | <font style="color:rgb(51, 51, 51);">更新资源上的标签</font> |
| <font style="color:rgb(51, 51, 51);">cluster-info</font> | <font style="color:rgb(51, 51, 51);">显示集群信息</font> |
| <font style="color:rgb(51, 51, 51);">version</font> | <font style="color:rgb(51, 51, 51);">显示当前Server和Client版本信息</font> |


**<font style="color:rgb(51, 51, 51);">命令格式：</font>**<font style="color:rgb(51, 51, 51);">kubectl [command] [type] [name] [flags]</font>

+ **<font style="color:rgb(51, 51, 51);">command</font>**<font style="color:rgb(51, 51, 51);">：指定要对资源执行的操作，例如：create、get、delete</font>
+ **<font style="color:rgb(51, 51, 51);">type</font>**<font style="color:rgb(51, 51, 51);">：指定资源类型，例如：deployment、pod、service</font>
+ **<font style="color:rgb(51, 51, 51);">name</font>**<font style="color:rgb(51, 51, 51);">：指定资源名称，名称区分大小写</font>
+ **<font style="color:rgb(51, 51, 51);">flags</font>**<font style="color:rgb(51, 51, 51);">：指定额外的可选参数</font>

#### <font style="color:rgb(51, 51, 51);">kubectl命令练习</font>
| **<font style="color:rgb(51, 51, 51);">资源名称</font>** | **<font style="color:rgb(51, 51, 51);">缩写</font>** | **<font style="color:rgb(51, 51, 51);">资源作用</font>** |
| :--- | :--- | :--- |
| <font style="color:rgb(51, 51, 51);">pods</font> | <font style="color:rgb(51, 51, 51);">po</font> | <font style="color:rgb(51, 51, 51);">装载容器</font> |


```shell
查看所有pod
# kubectl get pod

查看指定的pod（根据pod名字查找）
# kubectl get pod nginx-696649f6f9-g5nds

查看指定pod，通过额外参数显示pod详细信息，包括pod的IP地址，pod运行的节点等
# kubectl get pod nginx-696649f6f9-g5nds -o wide

查看指定pod，通过额外参数显示pod信息，以json格式显示
# kubectl get pod nginx-696649f6f9-g5nds -o json

查看指定pod，通过额外参数显示pod信息，以yaml格式显示
# kubectl get pod nginx-696649f6f9-g5nds -o yaml

显示指定pod资源内部信息
# kubectl describe pod nginx-696649f6f9-g5nds

显示当前Server和Client版本信息
# kubectl version

显示集群信息
# kubectl cluster-info
```

#### <font style="color:rgb(51, 51, 51);">kubectl命令补齐</font>
```shell
yum install -y bash-completion

source /usr/share/bash-completion/bash_completion

source <(kubectl completion bash)

kubectl completion bash > ~/.kube/completion.bash.inc

source '/root/.kube/completion.bash.inc'  

source $HOME/.bash_profile

exec	bash
```

  
 **<font style="color:rgb(51, 51, 51);">扩展</font>**<font style="color:rgb(51, 51, 51);">：如果在node节点需要使用kubectl命令需要执行如下操作</font>

```shell
#将master节点上的.kube目录复制到node节点上，该目录在root用户家目录下
# scp -r /root/.kube worker01:/root

#node1节点验证
[root@node1 ~]# kubectl get nodes
NAME     STATUS   ROLES    AGE     VERSION
master   Ready    master   4d23h   v1.17.4
node1    Ready    <none>   4d23h   v1.17.4
node2    Ready    <none>   4d23h   v1.17.4
```

  
 开机默认启动该补全

```yaml
echo "source ~/.kube/completion.bash.inc" > ~/.bashrc
source ~/.bashrc
exec	bash
```

