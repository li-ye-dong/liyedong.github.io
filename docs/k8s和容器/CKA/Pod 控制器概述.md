<font style="color:rgb(51, 51, 51);">在k8s中，pod的创建方式分为两类：</font>

**<font style="color:rgb(51, 51, 51);">静态Pod</font>**<font style="color:rgb(51, 51, 51);">：</font><font style="color:rgb(51, 51, 51);">	</font><font style="color:rgb(51, 51, 51);">也称之为</font><font style="color:rgb(65, 131, 196);">无控制器管理的自主式pod</font><font style="color:rgb(51, 51, 51);">，直接由特定节点上的 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubelet</font>`<font style="color:rgb(51, 51, 51);"> 守护进程管理， 不需要API 服务器看到它们，对于静态 Pod 而言，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubelet</font>`<font style="color:rgb(51, 51, 51);"> 直接监控每个 Pod，这种pod删除后就没有了，也不会重建。</font>

**<font style="color:rgb(51, 51, 51);">控制器管理的pod</font>**<font style="color:rgb(51, 51, 51);">： 控制器可以控制pod的副本数，扩容与裁剪，版本更新与回滚等。</font>

<font style="color:rgb(119, 119, 119);">k8s的1.17之前版本中, kubectl run命令默认通过Deployment控制器创建Pod</font>

<font style="color:rgb(119, 119, 119);">在v1.18版本中, kubectl run命令改为创建静态pod</font>

<font style="color:rgb(51, 51, 51);">pod控制器是管理pod的中间层，使用了pod控制器之后，我们只需要告诉pod控制器，需要多少个什么样的pod就可以了，它就会创建出满足条件的pod，并确保每一个pod处于用户期望的状态，如果pod在运行中出现故障，控制器会基于指定的策略重新启动或重建pod</font>

<font style="color:rgb(51, 51, 51);">在k8s中，pod控制器的种类有很多，每种pod控制器的应用场景都不一样，常见的有下面这些：</font>

+ <font style="color:rgb(51, 51, 51);">ReplicationController：比较原始的pod控制器，目前已经被废弃，由ReplicaSet代替</font>
+ <font style="color:rgb(51, 51, 51);">ReplicaSet：保证指定数量的pod运行，并支持pod数量变更，镜像版本变更</font>
+ <font style="color:rgb(51, 51, 51);">Deployment：通过控制ReplicaSet来控制pod，包含ReplicaSet所有功能，还支持滚动升级，版本回退</font>
+ <font style="color:rgb(51, 51, 51);">Horizontal Pod Autoscaler：可以根据集群负载自动调整pod数量，实现pod容缩</font>
+ <font style="color:rgb(51, 51, 51);">DaemonSet： 确保全部（或者一些）Node 上运行一个 Pod 的副本，当有 Node 加入集群时，也会为他们新增一个 Pod ，当有 Node 从集群移除时，这些 Pod 也会被回收，删除 DaemonSet 将会删除它创建的所有 Pod</font>
+ <font style="color:rgb(51, 51, 51);">Job：它创建的pod只要完成就立即退出</font>

<font style="color:rgb(119, 119, 119);">容器按照持续运行的时间可分为两类：服务类容器和工作类容器</font>

    - <font style="color:rgb(119, 119, 119);">服务类容器通常持续提供服务，需要一直运行，比如 </font>**<font style="color:rgb(119, 119, 119);">http server</font>**<font style="color:rgb(119, 119, 119);">，</font>**<font style="color:rgb(119, 119, 119);">daemon</font>**<font style="color:rgb(119, 119, 119);"> 等 </font>
    - <font style="color:rgb(119, 119, 119);">工作类容器则是一次性任务，比如批处理程序，完成后容器就退出 </font>
+ <font style="color:rgb(51, 51, 51);">Cronjob：它创建的pod会周期性的执行，用于执行周期性任务（常用在数据备份工作）</font>

#### <font style="color:rgb(51, 51, 51);">Pod 资源清单介绍</font>
```yaml
以下是比较详细的资源清单介绍

KIND:     Pod  #资源类型类型
VERSION:  v1   #资源版本
DESCRIPTION:   #资源描述
FIELDS:        #资源可配置的属性，如下

apiVersion: v1      #必选的一级属性，版本号，例如v1
kind: Pod           #必选的一级属性，资源类型，例如Pod
metadata:           #必选的一级属性，元数据
    name:           #必选的二级属性，Pod名称
    namespace: dev  #二级属性，Pod所属的名称空间，例如dev，默认为default名称空间
    labels:         #二级属性，自定义标签列表
     - name:        #三级属性，标签名称
spec:               #必选的一级属性，Pod中容器的详细定义
 containers:        #必选的二级属性，Pod中容器列表
 - name:            #必选的三级属性，容器名称
   image:           #必选的三级属性，容器镜像名称
   imagePullPolicy: #三级属性，镜像的拉取策略
   command:         #三级属性，容器的启动命令列表，如不指定，使用打包时使用的启动命令
   args:            #三级属性，容器的启动命令参数列表
   workingDir:      #三级属性，容器的工作目录
   volumeMounts:    #三级属性，挂载到容器内部的存储卷配置
   - name:          #四级属性，引用pod定义的共享存储卷的名称
     mountPath:     #四级属性，存储卷在容器内mount的绝对路径，应少于512字节
     readOnly:      #四级属性，是否为只读模式
   ports:           #三级属性，需要暴露的端口库号列表
   - name:          #四级属性，端口的名称
     containerPort: #四级属性，容器需要监听的端口号
     hostPort:      #四级属性，容器所在的主机需要监听的端口号，默认与Container相同
     protocol:      #四级属性，端口协议，支持TCP/UDP,默认为TCP
   env:             #三级属性，容器运行前需要设置的环境变量列表
   - name:          #四级属性，环境变量名称
     value:         #四级属性，环境变量的值
   resources:       #三级属性，资源限制和请求的设置        
     limits:        #四级属性，资源最大限制的设置
        CPU:        #五级属性，CPU资源限制，单位为core数，将用于docker run --cpu-shares参数
        memory:     #五级属性，内存资源限制，单位可以为Mib/Gib，将用于docker run --memory参数
     requests:      #四级属性，资源最小请求的设置
        CPU:        #五级属性，CPU请求，容器启动的初始可用数量
        memory:     #五级属性，内存请求，容器启动的初始可用数量
   lifecycle:       #三级属性，生命周期钩子
     postStart:     #四级属性，容器启动后立即执行此钩子，如果执行失败，会根据重启策略进行重启
     preStop:       #四级属性，容器终止前执行此钩子，无论结果如何，容器都会终止
   livenessProbe:   #三级属性，对Pod内个容器健康检查设置，当探测容器无响应后将自动重启该容器
   tcpSocket:       #三级属性，对Pod内容器健康检查方式
   initialDelaySeconds:     #三级属性，容器启动完成后，首次探测时间，单位为秒
   timeoutSeconds:          #三级属性，对容器健康检查探测等待相应的超时时间，单位秒，默认1秒
   periodSeconds:           #三级属性，对容器监控检查的定期探测时间设置，单位秒，默认10秒一次
 restartPolicy:     #二级属性，Pod的重启策略
 nodeName:          #二级属性，设置pod调度到指定的node节点上
 nodeSelector:      #二级属性，设置Pod调度到指定的label的node节点上
 imagePullSecrets:  #二级属性，拉取镜像时，使用secret名称，以key:secretkey格式指定
 hostNetwork:       #二级属性，是否使用主机网络模式，默认为false，如果设置为true，表示使用宿主机网络
 volumes:           #二级属性，在该Pod上定义共享存储卷列表
 - name:            #三级属性，共享存储卷名称
   emptyDir:        #三级属性，类型为emptyDir的存储卷，与Pod同生命周期的一个临时目录，为空值
   hostPath:        #三级属性，类型为hostPath的存储卷，挂载集群与定义的secret对象到容器内部
     path:          #四级属性，Pod所在宿主机的目录，将被用于容器中挂载的目录
   secret:          #三级属性，类型为secret的存储卷，挂载集群与定义的secret对象到容器内部
   configMap:       #三级属性，类型为configMap的存储卷，挂载预定义的configMap对象到容器内部
```

  
 

