# kubernetes 数据存储
#### 数据存储介绍
由于容器的生命周期不稳定，可能随时被创建与销毁，如果容器被销毁后，在容器中产生的数据也会被清除，如果需要对容器内的数据实现持久化保存，我们需要将容器内的数据与pod分离，将数据放在专门的存储卷上





#### 存储卷的分类
kubernetes支持的存储卷类型非常丰富,使用下面的命令查看

```yaml
# kubectl explain pod.spec.volumes
```

或者参考: [https://kubernetes.io/docs/concepts/storage/](https://kubernetes.io/docs/concepts/storage/)



K8s支持的存储类型大体分为如下几类：

+ 本地存储卷 
    - emptyDir    pod删除，数据也会被清除, 用于数据的临时存储
    - hostPath     宿主机目录映射(本地存储卷)
+ 网络存储卷
    - NAS网络附加存储：       nfs等
    - 分布式网络附加存储：   glusterfs，cephfs，rbd（chph中的存储类型），cinder（OpenStack中的存储类型）等
    - SAN块存储：                   iscsi，FC等
    - 云存储：                          aws,azurefile等





#### 本地存储 EmptyDir
EmptyDir是最基础的存储类型，一个EmptyDir就是主机上的一个空目录

EmptyDir是在Pod被分配到Node节点时创建的，它的初始内容为空，并且无需指定宿主机上对应的目录文件，应为k8s会自动分配一个空目录，当Pod销毁时，EmptyDir中的数据也会被永久删除。



EmptyDir用途如下：

+ 临时存储空间，例如用于某些应用程序运行时所需要的临时目录，且无需永久保留
+ 同一个Pod中容器需要从另一个容器中获取数据的目录（多容器间共享数据）



**案例**：接下来通过一个容器之间文件共享的来演示一下EmptyDir

> 在一个Pod中准备两个容器nginx和busybox，然后声明一个EmptyDir分别挂载到两个容器的目录中，然后nginx容器负责向EmptyDir中写日志，busybox通过命令将日志内容读到控制台。
>



```yaml
[root@master01 ~]# vim emptydir_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test

spec:
    selector:                   #标签选择器(基于选择器匹配Pod)
      matchLabels:              #标签类型
        app: deploy-nginx       #匹配pod的标签(表示deploy管理带有此标签的Pod)

    template:                   #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx     #pod的标签

      spec:
        volumes:              声明volume存储卷
        - name: nginx-logs    定义volume卷名称
          emptyDir: {}        类型为emptyDir，{}表示空目录
          
      containers:
      - name: nginx
        image: nginx:1.17.0   #指定镜像
        ports:                #定义端口
        - containerPort: 80   #端口
        volumeMounts:
        - name: nginx-logs           指定挂载的volume名称
          mountPath: /var/log/nginx  容器内挂载点目录


      - name: busybox
        image: busybox:1.30   #指定镜像
        command: ["/bin/sh","-c","tail -f /logs/access.log"]  #动态读取日志文件
        volumeMounts:
        - name: nginx-logs     指定挂载的volume名称
          mountPath: /logs     容器内挂载点目录




创建Pod
[root@master01 ~]# kubectl create -f emptydir_nginx.yml



查看Pod信息
[root@master01 ~]# kubectl get pod -n test -o wide
deploy-nginx-6765b8f99c-wwzj6   2/2     Running   0          16m   10.244.5.42   worker01 



可以通过find命令在对应节点中搜索存储卷目录的所在位置
[root@worker01 ~]# find / -name nginx-logs -type d 



通过kubectl logs 命令动态查看busybox容器输出内容
[root@master01 ~]# kubectl logs -f deploy-nginx-6765b8f99c-wwzj6 -n test -c busybox



在开一个终端，访问nginx
[root@master01 ~]# curl 10.244.5.42



删除Pod
[root@master01 ~]# kubectl delete -f emptydir_nginx.yml

```

总结：EmptyDir存储方式不会永久保存数据，应为EmptyDir的生命周期是跟据Pod的生命周期是一样的，它会随着Pod的结束而销毁，如果想简单的将数据持久化到主机中，可以选择用HostPath。







#### 本地存储 HostPath
HostPath是将Node节点中一个实际目录挂载到Pod中，以供容器使用，这样的设计可以保证Pod销毁了，但是数据以然可以保存在宿主机上，实现数据永久保存。



**案例**：创建nginx，并通过hostPath存储卷方式对nginx实现数据持久化保存。

```yaml
[root@master01 ~]# vim hostpath_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test

spec:
    selector:                   #标签选择器(基于选择器匹配Pod)
      matchLabels:              #标签类型
        app: deploy-nginx       #匹配pod的标签(表示deploy管理带有此标签的Pod)

    template:                   #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx     #pod的标签


      spec:
        volumes:                      声明volume存储卷
        - name: nginx-html            定义volume名称
          hostPath:                   类型hostPath
            type: DirectoryOrCreate   目录存在就使用，不存在就先创建后使用
            path: /nginx/html         指定node节点目录（存放页面）

        - name: nginx-logs            定义volume名称
          hostPath:                   类型hostPath
            type: DirectoryOrCreate   目录存在就使用，不存在就先创建后使用
            path: /nginx/logs         指定node节点目录（存放日志）


        containers:
        - name: nginx
          image: nginx:1.17.0   #指定镜像
          ports:                #定义端口
          - containerPort: 80   #端口

          volumeMounts:
          - name: nginx-html                   指定挂载的volume名称
            mountPath: /usr/share/nginx/html   容器内挂载点目录

          - name: nginx-logs                   指定挂载的volume名称
            mountPath: /var/log/nginx          容器内挂载点目录



关于 hostPath的type属性可用值说明：
 DirectoryOrCreate    目录存在就创建，不存在就先创建后使用
 Directory            目录必须存在
 FileOrcreate         文件存在就使用，不存在就先创建后使用
 File                 文件必须存在
 Socket               套接字必须存在
 CharDevice           字符设备必须存在
 BlockDevice          块设备必须存在



创建Pod
[root@master01 ~]# kubectl create -f hostpath_nginx.yml



查看Pod详细信息
[root@master01 ~]# kubectl get pod -n test -o wide
deploy-nginx-8578d555c9-np9gk   1/1    Running   0          6m46s   10.244.5.48   worker01 



查看worker01节点的hostPath目录
[root@worker01 ~]# ls /nginx
html



创建index.html文件进行访问测试
[root@worker01 ~]# echo hello > /nginx/html/index.html



通过Pod访问
[root@master01 ~]# curl 10.244.5.48



删除Pod验证数据持久化
[root@master01 ~]# kubectl delete -f hostpath_nginx.yml

```

总结：HostPath可以解决数据持久化的问题，但是一旦Node节点故障了，那么数据卷并不会转移到其他的节点，为了解决以上的问题，可以使用网络文件存储系统，比较常见的有NFS、glusterfs等。







#### 网络存储 NFS
NFS是一个网络文件存储系统，可以搭建一台NFS服务器，然后将Pod中的存储直接连到NFS系统上，这样无论Pod在节点上怎么转移，只要该节点跟NFS对接没问题，数据就可以成功访问。





**部署NFS服务端**

可以单独准备一台服务器部署NFS，但是实验环境我们可以直接在master01节点部署

```yaml
安装nfs-utils
[root@master01 ~]# yum -y install nfs-utils



创建共享目录
[root@master01 ~]# mkdir -p /nfs-nginx/html
[root@master01 ~]# mkdir  /nfs-nginx/logs



共享目录
[root@master01 ~]# vim /etc/exports
/nfs-nginx/html 192.168.0.0/24(rw,no_root_squash)
/nfs-nginx/logs 192.168.0.0/24(rw,no_root_squash)



启动nfs服务&&设置服务随机自启
[root@master01 ~]# systemctl start nfs
[root@master01 ~]# systemctl enable nfs

```





**部署NFS客户端**

在集群worker节点上都安装nfs客户端工具，这样worker节点才可以驱动nfs设备，不需要启动服务

```yaml
# yum -y install nfs-utils

# showmount -e 192.168.0.10
Export list for 192.168.0.10:
/nfs-nginx/logs 192.168.0.0/24
/nfs-nginx/html 192.168.0.0/24
```







**案例**：创建nginx，并通过NFS存储卷方式对nginx实现数据持久化保存。

```yaml
[root@master01 ~]# vim nfs_nginx.yml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: deploy-nginx
    namespace: test

spec:
    selector:                   #标签选择器(基于选择器匹配Pod)
      matchLabels:              #标签类型
        app: deploy-nginx       #匹配pod的标签(表示deploy管理带有此标签的Pod)

    template:                   #pod的配置模板
      metadata:
        labels:
          app: deploy-nginx     #pod的标签


      spec:
        volumes:                      声明volume存储卷
        - name: nginx-html            定义volume名称
          nfs:                        类型nfs
            server: 192.168.0.10      NFS服务器地址
            path: /nfs-nginx/html     NFS共享目录

        - name: nginx-logs            定义volume名称
          nfs:                        类型nfs
            server: 192.168.0.10      NFS服务器地址
            path: /nfs-nginx/logs     NFS共享目录


        containers:
        - name: nginx
          image: nginx:1.17.0   #指定镜像
          ports:                #定义端口
          - containerPort: 80   #端口

          volumeMounts:
          - name: nginx-html                   指定挂载的volume名称
            mountPath: /usr/share/nginx/html   容器内挂载点目录

          - name: nginx-logs                   指定挂载的volume名称
            mountPath: /var/log/nginx          容器内挂载点目录





创建Pod
[root@master01 ~]# kubectl create -f nfs_nginx.yml



查看Pod详细信息
[root@master01 ~]# kubectl get pod -n test -o wide



验证nfs共享目录
[root@master01 ~]# ls /nfs-nginx/logs/
access.log  error.log



删除Pod
[root@master01 ~]# kubectl delete -f nfs_nginx.yml



验证数据持久化
[root@master01 ~]# ls /nfs-nginx/logs/
access.log  error.log
```







#### 数据存储 PV与PVC
经过前面的NFS存储已经可以实现数据的持久化保存，而k8s为了能够屏蔽底层的存储细节，方便用户使用，k8s引入了PV和PVC的存储方式

> **PV（Persistent Volume）**：是持久化卷的意思，是对底层共享存储的一种抽象，一般情况下PV由K8s管理员进行创建和配置，它与底层具体的共享存储技术有关，并通过插件完成与共享存储的对接
>
> **PVC（Persistent Volume Claim）**：是持久卷声明的意思，是用户对于存储需求的一种声明，也可以理解为用户向k8s系统发出的一种资源需求申请
>



#### StorageClass PV PVC之间的关系
+ **StorageClass**：存储类型 & PV 生产方式的定义。
+ **PV**：实际的存储卷，可以静态写死，也可以根据 StorageClass 动态生成。
+ **PVC**：Pod 用来申请存储，PVC 指定 StorageClass 时，才会触发 **动态创建 PV**。

一个典型流程

1. 管理员：写好 `fast-ssd` StorageClass。
2. 用户：

```plain
kind: PersistentVolumeClaim
spec:
  storageClassName: fast-ssd
  resources:
    requests:
      storage: 10Gi
```

3. 系统：看到 PVC → 用 `fast-ssd` → 动态创建 PV → 绑定 PVC。
4. Pod 挂载 PVC，用户拿到存储。

#### PV与PVC之间的关系
+ pv提供存储资源(生产者)
+ pvc使用存储资源(消费者)
+ 使用pvc绑定pv







PV资源清单文件介绍

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: 
spec:
  nfs:               存储类型，与底层真正存储对应，如：nfs
  capacity:          存储能力，目前只支持存储空间的设置
    storage: 2Gi     存储空间
  accessModes:       访问模式
  persistentVolumeReclaimPolicy:   回收策略

```

> accessModes（访问模式）：用于描述用户应用对存储资源的访问权限，访问权限包含以下几种方式：
>
> + ReadWriteOnce（RWO）：读写权限，但是只能被单个节点挂载
> + ReadOnlyMany（ROX）： 只读权限，可以被多个节点挂载
> + ReadWriteMany（RWX）：读写权限，可以被多个节点挂载
>
> 注意事项：底层不同的存储类型可能支持的访问模式也不同
>



> persistentVolumeReclaimPolicy（回收策略）：当PV不再被PVC使用之后，对其PV内的数据处理方式，目前支持三种策略
>
> + Retain（保留）：保留数据，需要管理员手工清理数据
> + Recycle（回收）：清除PV中的数据，效果相当于执行rm -rf 
> + Delete（删除）：与PV相连的后端存储完成volume的删除操作，当然这常见于云服务商的存储服务
>
> 注意事项：底层不同的存储类型可能支持的回收策略也不同
>



**案例**：使用NFS作为底层存储，并通过PV的方式实现数据持久化

```yaml
创建共享目录
[root@master ~]# mkdir /nfs-mysql


共享目录
[root@master01 ~]# vim /etc/exports
/nfs-mysql 192.168.0.0/24(rw,no_root_squash)


重启nfs服务
[root@master ~]# systemctl restart nfs
```





#### PV 应用案例
**案例**：创建一个4G 的 PV 存储卷，并使用NFS作为后端存储。

```yaml
[root@master01 ~]# vim pv_mysql.yml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-mysql

spec:
  capacity:             #存储能力，目前只支持存储空间的设置
    storage: 4Gi        #存储空间
  accessModes:          #访问模式
  - ReadWriteMany       #读写权限，可以被多个节点挂载
  persistentVolumeReclaimPolicy: Retain   #回收策略为保留
  nfs:                     #存储类型
    path: /nfs-mysql       #挂载路径
    server: 192.168.0.10   #nfs服务器地址

#提示：PV是全局资源，无需指定命名空间
    
创建pv
[root@master01 ~]# kubectl create -f pv_mysql.yml



查看pv详细信息
[root@master01 ~]# kubectl get pv -o wide



**PV状态**：一个PV的生命周期中，可能会处于4种不同的阶段

1. Avallable（可用）：表示可用状态，还未被任何的PVC绑定

2. Bound（已绑定）：表示PV已经被PVC绑定

3. Released（已释放）：表示PVC被删除，但是资源还未被集群重新声明

4. Falled（失败）：表示该PV的自动回收失败
```





#### PVC 应用案例
PVC是资源的申请，用来声明对存储空间、访问模式、存储类别需求信息，PVC清单文件介绍：

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc
  namespace: dev
spec:
  accessModes:        访问模式
  selector:           标签选择器，采用标签对PV选择
  storageClassName:   存储类别
  resources:          资源
    requests:         请求
      storage:        资源大小
```



**案例**：创建一个PVC，并绑定pv-mysql存储卷

```yaml
[root@master01 ~]# vim pvc_mysql.yml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-mysql
  namespace: test

spec:
  accessModes:       #访问模式，访问模式要与PV模式相同，否则绑定不上
  - ReadWriteMany    #读写权限，可以被多个节点挂载
  resources:         #请求
    requests:        #资源
      storage: 4Gi   #资源大小，在绑定PV时，按照申请资源大小选择符合的PV，如果超出PV空间范围，则无法绑定

#PVC是局部资源，可指定命名空间


创建pvc
[root@master01 ~]# kubectl create -f pvc_mysql.yml



查看pvc信息
[root@master ~]# kubectl get pvc -n test



查看pv信息
[root@master ~]# kubectl get pv
```



**案例**：创建MySQL并挂载PVC实现数据持久化。

```yaml
[root@master01 ~]# vim pv-pvc_mysql.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-mysql
  namespace: test

spec:
  selector:
    matchLabels:
      app: deploy-mysql

  template:
    metadata:
      labels:
        app: deploy-mysql

    spec:
      volumes:                    # 声明volume存储卷
        - name: mysql-data        # 定义volume名称
          persistentVolumeClaim:  # 类型为PVC
            claimName: pvc-mysql  # PVC名称
            readOnly: false       # 访问模式

      containers:
        - name: mysql
          image: mysql:5.7        # 镜像版本
          ports:
            - containerPort: 3306  # 端口
          env:
            - name: MYSQL_ROOT_PASSWORD  # 变量名称
              value: "123456"             # 值

          volumeMounts:
            - name: mysql-data          # 指定挂载的volume名称
              mountPath: /var/lib/mysql  # 容器内挂载点目录





创建pod
[root@master01 ~]# kubectl create -f pv-pvc_mysql.yml




[root@master datastore]# kubectl get po -n test
NAME                            READY   STATUS    RESTARTS   AGE
deploy-mysql-57c47fc979-pdjdr   1/1     Running   0          34s




查看NFS共享存储路径
[root@master datastore]#  ls /nfs-mysql
auto.cnf    client-cert.pem  ibdata1      ibtmp1      performance_schema  server-cert.pem
ca-key.pem  client-key.pem   ib_logfile0  mysql       private_key.pem     server-key.pem
ca.pem      ib_buffer_pool   ib_logfile1  mysql.sock  public_key.pem      sys



删除pod、pvc、pv
[root@master01 ~]# kubectl delete -f pv-pvc_mysql.yml
[root@master01 ~]# kubectl delete -f pvc_mysql.yml
[root@master01 ~]# kubectl delete -f pv_mysql.yml
```

PVC与PV是一一相对应的，PV和PVC之间的相互作用遵循以下生命周期：

+ 资源供应：管理员手动创建底层存储和PV
+ 资源绑定：用户创建PVC，k8s负责根据PVC的声明去寻找PV，并绑定在用户定义好的PVC之后，系统将根据PVC对存储资源的请求在已存在的PV中选择一个满足条件的一旦找到，就将PV与用户定义的PVC进行绑定，用户的应用就可以使用这个PVC如果找不到，PVC一直处于Pending状态，直到管理员创建了一个符合要求的PVPV一旦绑定到某个PVC上，就会被这个PVC独占，不能在与其他的PVC进行绑定
+ 资源使用：用户可在pod中像volume一样使用PVCPod使用volume的定义，将PVC挂载到容器的某个路径进行使用
+ 资源释放：用户删除PVC来释放PV当存储资源使用完毕后，用户可以删除PVC，与该PVC绑定的PV将会被标记为“已释放”，但还不能立刻与其他PVC进行绑定，应为之前PVC写入的数据可能还被留在存储设备上，只有在清除之后该PV才能再次使用
+ 资源回收：k8s根据PV设置的回收策略进行资源的回收对于PV，管理员可以设定回收策略，用于设置与之绑定的PVC释放资源之后如何处理遗留数据的问题，只有PV的存储空间完成回收，才能供新的PVC绑定和使用

