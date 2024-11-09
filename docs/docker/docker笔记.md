## 1.基础命令

```shell
 yum update
 yum install -y yum-utils device-mapper-persistent-data lvm2
 yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
 yum install docker-ce #社区版
 docker -v
```

设置国内ustc镜像

```
vi /etc/docker/daemon.json
```

```
{
    "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}
```

启动

```
systemctl start docker
systemctl restart docker
```

状态

```
systemctl status docker
```

停止

```
systemctl stop docker
```

开机自启动

```
systemctl enable docker
```

查看概要

```
docker info
```

帮助

```
docker --help
```

## 2.镜像

### 获取镜像

```
docker pull ubuntu
```

### 查看镜像

```
docker images
```

各个选项说明:

- **REPOSITORY：**表示镜像的仓库源
- **TAG：**镜像的标签
- **IMAGE ID：**镜像ID
- **CREATED：**镜像创建时间
- **SIZE：**镜像大小

### 搜索

```
docker search xxx
```

**NAME:** 镜像仓库源的名称

**DESCRIPTION:** 镜像的描述

**OFFICIAL:** 是否 docker 官方发布

**stars:** 类似 Github 里面的 star，表示点赞、喜欢的意思。

**AUTOMATED:** 自动构建。

### 用版本为15.10的ubuntu系统镜像

来运行容器时，命令如下：

```
runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash 
root@d77ccb2e5cca:/#
```

参数说明：

- **-i**: 交互式操作。
- **-t**: 终端。
- **ubuntu:15.10**: 这是指用 ubuntu 15.10 版本镜像为基础来启动容器。
- **/bin/bash**：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。

### 删除镜像

镜像删除使用 **docker rmi** 命令，比如我们删除 hello-world 镜像：

```
 docker rmi hello-world
```

### 创建镜像

当我们从 docker 镜像仓库中下载的镜像不能满足我们的需求时，我们可以通过以下两种方式对镜像进行更改。

- 1、从已经创建的容器中更新镜像，并且提交这个镜像
- 2、使用 Dockerfile 指令来创建一个新的镜像

### 更新镜像

更新镜像之前，我们需要使用镜像来创建一个容器。

```
runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash
root@e218edb10161:/# 
```

在运行的容器内使用 **apt-get update** 命令进行更新。

在完成操作之后，输入 exit 命令来退出这个容器。

此时 ID 为 e218edb10161 的容器，是按我们的需求更改的容器。我们可以通过命令 docker commit 来提交容器副本。

```
runoob@runoob:~$ docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8
```

各个参数说明：

- **-m:** 提交的描述信息
- **-a:** 指定镜像作者
- **e218edb10161：**容器 ID
- **runoob/ubuntu:v2:** 指定要创建的目标镜像名



### 构建镜像

我们使用命令 **docker build** ， 从零开始来创建一个新的镜像。为此，我们需要创建一个 Dockerfile 文件，其中包含一组指令来告诉 Docker 如何构建我们的镜像。

```
runoob@runoob:~$ cat Dockerfile 
FROM    centos:6.7
MAINTAINER      Fisher "fisher@sudops.com"

RUN     /bin/echo 'root:123456' |chpasswd
RUN     useradd runoob
RUN     /bin/echo 'runoob:123456' |chpasswd
RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
EXPOSE  22
EXPOSE  80
CMD     /usr/sbin/sshd -D
```

每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。

第一条FROM，指定使用哪个镜像源

RUN 指令告诉docker 在镜像内执行命令，安装了什么。。。

然后，我们使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像。

```
runoob@runoob:~$ docker build -t runoob/centos:6.7 .
Sending build context to Docker daemon 17.92 kB
Step 1 : FROM centos:6.7
 ---&gt; d95b5ca17cc3
Step 2 : MAINTAINER Fisher "fisher@sudops.com"
 ---&gt; Using cache
 ---&gt; 0c92299c6f03
Step 3 : RUN /bin/echo 'root:123456' |chpasswd
 ---&gt; Using cache
 ---&gt; 0397ce2fbd0a
Step 4 : RUN useradd runoob
......
```

参数说明：

- **-t** ：指定要创建的目标镜像名
- **.** ：Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径

使用docker images 查看创建的镜像已经在列表中存在,镜像ID为860c279d2fec

```
runoob@runoob:~$ docker images 
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
runoob/centos       6.7                 860c279d2fec        About a minute ago   190.6 MB
runoob/ubuntu       v2                  70bf1840fd7c        17 hours ago         158.5 MB
ubuntu              14.04               90d5884b1ee0        6 days ago           188 MB
php                 5.6                 f40e9e0f10c8        10 days ago          444.8 MB
nginx               latest              6f8d099c3adc        12 days ago          182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago          324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago          194.4 MB
ubuntu              15.10               4e3b13c8a266        5 weeks ago          136.3 MB
hello-world         latest              690ed74de00f        6 months ago         960 B
centos              6.7                 d95b5ca17cc3        6 months ago         190.6 MB
training/webapp     latest              6fae60ef3446        12 months ago        348.8 MB
```

我们可以使用新的镜像来创建容器

```
runoob@runoob:~$ docker run -t -i runoob/centos:6.7  /bin/bash
[root@41c28d18b5fb /]# id runoob
uid=500(runoob) gid=500(runoob) groups=500(runoob)
```

从上面看到新镜像已经包含我们创建的用户 runoob。

### 设置镜像标签

我们可以使用 docker tag 命令，为镜像添加一个新的标签。

```
runoob@runoob:~$ docker tag 860c279d2fec runoob/centos:dev
```

docker tag 镜像ID，这里是 860c279d2fec ,用户名称、镜像源名(repository name)和新的标签名(tag)。

使用 docker images 命令可以看到，ID为860c279d2fec的镜像多一个标签。

```
runoob@runoob:~$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
runoob/centos       6.7                 860c279d2fec        5 hours ago         190.6 MB
runoob/centos       dev                 860c279d2fec        5 hours ago         190.6 MB
runoob/ubuntu       v2                  70bf1840fd7c        22 hours ago        158.5 MB
ubuntu              14.04               90d5884b1ee0        6 days ago          188 MB
php                 5.6                 f40e9e0f10c8        10 days ago         444.8 MB
nginx               latest              6f8d099c3adc        13 days ago         182.7 MB
mysql               5.6                 f2e8d6c772c0        3 weeks ago         324.6 MB
httpd               latest              02ef73cf1bc0        3 weeks ago         194.4 MB
ubuntu              15.10               4e3b13c8a266        5 weeks ago         136.3 MB
hello-world         latest              690ed74de00f        6 months ago        960 B
centos              6.7                 d95b5ca17cc3        6 months ago        190.6 MB
training/webapp     latest              6fae60ef3446        12 months ago       348.8 MB
```





## 3.容器

### 启动容器

```
docker run -it ubuntu /bin/bash
```

参数说明：

- **-i**: 交互式操作。
- **-t**: 终端。
- **ubuntu**: ubuntu 镜像。
- **/bin/bash**：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。

### 启动已停止运行的容器

查看所有的容器命令如下：

```
docker ps -a
```

### 开启容器

```
docker start id号
```

### 后台运行

在大部分的场景下，我们希望 docker 的服务是在后台运行的，我们可以过 **-d** 指定容器的运行模式。

```
docker run -itd --name ubuntu-test ubuntu /bin/bash
```

**注：**加了 **-d** 参数默认不会进入容器，想要进入容器需要使用指令 **docker exec**（下面会介绍到）。

### 后台运行

在大部分的场景下，我们希望 docker 的服务是在后台运行的，我们可以过 **-d** 指定容器的运行模式。

```
$ docker run -itd --name ubuntu-test ubuntu /bin/bash
```

停止的容器可以通过 docker restart 重启：

```
$ docker restart <容器 ID>
```

### 进入容器

在使用 **-d** 参数时，容器启动后会进入后台。此时想要进入容器，可以通过以下指令进入：

- **docker attach**
- **docker exec**：推荐大家使用 docker exec 命令，因为此命令会退出容器终端，但不会导致容器的停止。

**attach 命令**

下面演示了使用 docker attach 命令。

```
$ docker attach 1e560fca3906 
```

**注意：** 如果从这个容器退出，会导致容器的停止。

**exec 命令**

下面演示了使用 docker exec 命令。

```
docker exec -it 243c32535da7 /bin/bash
```

**注意：** 如果从这个容器退出，容器不会停止，这就是为什么推荐大家使用 **docker exec** 的原因。

更多参数说明请使用 **docker exec --help** 命令查看。

### 导出和导入容器

**导出容器**

如果要导出本地某个容器，可以使用 **docker export** 命令。

```
$ docker export 1e560fca3906 > ubuntu.tar
```

这样将导出容器快照到本地文件。

**导入容器快照**

可以使用 docker import 从容器快照文件中再导入为镜像，以下实例将快照文件 ubuntu.tar 导入到镜像 test/ubuntu:v1:

```
$ cat docker/ubuntu.tar | docker import - test/ubuntu:v1
```

此外，也可以通过指定 URL 或者某个目录来导入，例如：

```
$ docker import http://example.com/exampleimage.tgz example/imagerepo
```

### 删除容器

删除容器使用 **docker rm** 命令：

```
$ docker rm -f 1e560fca3906
```

下面的命令可以清理掉所有处于终止状态的容器。

```
$ docker container prune
```

## 4.文件拷贝

将文件拷贝到容器内可以使用cp

```
docker cp 需要拷贝的文件或者目录  容器名称:容器目录
```

也可以将文件从容器中拷贝出来

```
docker cp 容器名称:容器目录 需要拷贝的文件或目录
```

## 5.目录挂载

我们可以在创建容器的时候，将宿主机的目录与容器内的目录进行映射，这样我们就可以通过修改宿主机某个目录的文件从而去影响容器。
创建容器添加-v参数后边为宿主机目录:容器目录，例如:

```
docker run -di -v /usr/local/myhtml:/usr/local/myhtml --name=mycentos3 centos:7
```

如果你共享的是多级的目录，可能会出现权限不足的提示。
这是因为CentOS7中的安全模块selinux把权限禁掉了，我们需要添加参数--privileged=true 来解决挂载的目录没有权限的问题

## 6.查看一个json信息

```
docker inspect 容器名
```

### 过滤（查看IP）

```
docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名
```

## 7.mysql部署

### 拉取镜像

```
docker pull centos/mysql-57-centos7
```

### 创建容器

```
docker run -di --name=tensquare_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 j
```

-p:端口映射   宿主机映射端口:容器运行端口

-e:代表添加环境变量 MYSQL_ROOT_PASSWORD 是root用户的登录密码

### 进入mysql容器

```
docker exec -it tensquare_mysql /bin/bash
```

### 登录mysql

```
mysql -u root -p
```

## 8.tomcat部署

### 拉取镜像

```
docker pull tomcat:7-jre7
```

### 创建容器

```
docker run -di --name=mytomcat -p 9000:8080 -v /usr/local/webapps:/usr/local/tomcat/webapps tomcat:7-jre7
```

-p:端口映射   宿主机映射端口:容器运行端口

## 9.Nginx部署

### 拉取镜像

```
docker pull nginx
```

### 创建容器

```
docker run -di --name=mynginx -p 80:80 nginx
```

## 10.Redis部署

### 拉取镜像

```
docker pull redis
```

### 创建容器

```
docker run -di --name=myredis -p 6379:6379 redis
```

## 11.备份和迁移

### 容器保存为镜像

```
docker commit mynginx mynginx_img
```



### 镜像备份

将镜像保存为tar文件

```
docker save -o mynginx.tar mynginx_img
```



### 镜像恢复和迁移

先删除mynginx_img镜像，然后执行命令恢复

```
docker load -i mynginx.tar
```

-i:输入的文件

## 12.Dockerfile

### 介绍

Dockerfile是由一系列命令和参数构成的脚本，这些命令应用于基础镜像并最终创建一个新的镜像。
1、对于开发人员:可以为开发团队提供一个完全一致的开发环境;
2、对于测试人员:可以直接拿开发时所构建的镜像或者通过Dockerfile文件构建一个新的镜像开始工作了;
3、对于运维人员:在部署时，可以实现应用的无缝移植。

### dockerfile 的命令摘要

- FROM- 镜像从那里来

- MAINTAINER- 镜像维护者信息

- RUN- 构建镜像执行的命令，每一次RUN都会构建一层

- CMD- 容器启动的命令，如果有多个则以最后一个为准，也可以为ENTRYPOINT提供参数

- VOLUME- 定义数据卷，如果没有定义则使用默认

- USER- 指定后续执行的用户组和用户

- WORKDIR- 切换当前执行的工作目录

- HEALTHCHECH- 健康检测指令

- ARG- 变量属性值，但不在容器内部起作用

- EXPOSE- 暴露端口

- ENV- 环境变量属性值，容器内部也会起作用

- ADD- 添加文件，如果是压缩文件也解压

- COPY- 添加文件，以复制的形式

- ENTRYPOINT- 容器进入时执行的命令

## 13.使用dockerfile创建一个jdk1.8镜像

```
mkdir -p /usr/local/dockerjdk8
cd /usr/local/dockerjdk8/
vi Dockerfile
```

```dockerfile
FROM centos:7
MAINTAINER liyedong	
WORKDIR /usr
RUN mkdir /usr/local/java
ADD jdk8xxxxx.tar.gz /usr/local/java/

ENV JAVA_HOME /usr/local/java/jdk1.8.0_171
ENV JRE_HOME $JAVA_HOME/jre
ENV CLASSPATH $JAVA_HOME/bin/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib:$CLASSPATH
ENV PATH $JAVA_HOME/bin:$PATH
```

### 构建

```
docker build -t 'jdk1.8' .
```

注意：. 代表在当前目录

## 14.Docker私有仓库

### 仓库搭建和配置

拉去私有仓库镜像

```
docker pull registry
```

启动私有仓库容器

```
docker run -di --name=registry -p 5000:5000 registry
```

打开浏览器输入地址

```
http://ip:5000/v2/_catalog
```

看到{"repositories":[]}表示私有仓库搭建成功并且内容为空

修改daemon.json

```
vi /etc/docker/daemon.json
```

添加以下内容，保存退出(让docker信任私有仓库地址)

```json
{"insecure-registries":["ip:5000"]}
```

重启docker

```
systemctl restart docker
```

### 将镜像上传至私有仓库

标记镜像为私有仓库的镜像

```
docker tag jdk1.8 ip:5000/jdk1.8
```

上传标记的镜像

```
docker push ip:5000/jdk1.8
```

## 15.下载私有仓库镜像

### 信任对应的docker地址

修改daemon.json

```
vi /etc/docker/daemon.json
```

添加以下内容，保存退出(让docker信任私有仓库地址)

```json
{"insecure-registries":["ip:5000"]}
```

重启docker

```
systemctl restart docker
```

### 查看镜像仓库

```
http://ip:5000/v2/_catalog
```

### 下拉镜像

```
docker pull ip:5000/jdk1.8
```

## 16.运行一个 web 应用

前面我们运行的容器并没有一些什么特别的用处。

接下来让我们尝试使用 docker 构建一个 web 应用程序。

我们将在docker容器中运行一个 Python Flask 应用来运行一个web应用。

```
runoob@runoob:~# docker pull training/webapp  # 载入镜像
runoob@runoob:~# docker run -d -P training/webapp python app.py
```

参数说明:

- **-d:**让容器在后台运行。
- **-P:**将容器内部使用的网络端口随机映射到我们使用的主机上。

## 17.docker run 和 docker exec 的差异

------

**docker run ：**根据镜像创建一个容器并运行一个命令，操作的对象是 **镜像**；

**docker exec ：**在运行的容器中执行命令，操作的对象是 **容器**。

------



### **docker run 命令**

### **语法**

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

OPTIONS说明：

- **-a stdin:** 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；
- **-d:** 后台运行容器，并返回容器ID；
- **-i:** 以交互模式运行容器，通常与 -t 同时使用；
- **-P:** 随机端口映射，容器内部端口**随机**映射到主机的高端口
- **-p:** 指定端口映射，格式为：主机(宿主)端口:容器端口
- **-t:** 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
- **--name="nginx-lb":** 为容器指定一个名称；
- **--dns 8.8.8.8:** 指定容器使用的DNS服务器，默认和宿主一致；
- **--dns-search example.com:** 指定容器DNS搜索域名，默认和宿主一致；
- **-h "mars":** 指定容器的hostname；
- **-e username="ritchie":** 设置环境变量；
- **--env-file=[]:** 从指定文件读入环境变量；
- **--cpuset="0-2" or --cpuset="0,1,2":** 绑定容器到指定CPU运行；
- **-m :**设置容器使用内存最大值；
- **--net="bridge":** 指定容器的网络连接类型，支持 bridge/host/none/container:<name|id> 四种类型；
- **--link=[]:** 添加链接到另一个容器；
- **--expose=[]:** 开放一个端口或一组端口；
- **--volume , -v:** 绑定一个卷

### 实例

使用docker镜像 nginx:latest 以后台模式启动一个容器，并将容器命名为my-nginx。

```
docker run --name my-nginx -p 8081:80 -d nginx:latest
```

 ![1148440-20190630233839073-453001632](docker%E7%AC%94%E8%AE%B0.assets/1148440-20190630233839073-453001632.png)

浏览器访问 http://主机IP:8081，效果如下：



 ![1148440-20190630233942493-1515149082](docker%E7%AC%94%E8%AE%B0.assets/1148440-20190630233942493-1515149082.png)

使用镜像 nginx:latest 以后台模式启动一个容器，并将容器的80端口映射到主机随机端口：

```
docker run -P -d nginx:latest
```

 

使用镜像 nginx:latest 以后台模式启动一个容器，将主机的 80 端口映射到容器的 80 端口，主机的目录 /data 映射到容器的 /data：

```
docker run -p 80:80 -v /data:/data -d nginx:latest
```

 

使用镜像 nginx:latest 以交互模式启动一个容器，在容器内执行/bin/bash命令：

```
docker run -it nginx:latest /bin/bash
```



![1148440-20190630234417187-735526142](docker%E7%AC%94%E8%AE%B0.assets/1148440-20190630234417187-735526142.png)

 

### **docker exec 命令**

### **语法**

```
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

OPTIONS说明：

- **-d :** 分离模式: 在后台运行
- **-i :** 即使没有附加也保持STDIN 打开
- **-t :** 分配一个伪终端

 

在容器名称 my-nginx 中开启一个交互模式的终端：

```
docker exec -it my-nginx /bin/bash
```

 ![1148440-20190630234917321-606588265](docker%E7%AC%94%E8%AE%B0.assets/1148440-20190630234917321-606588265.png)

或者使用容器ID 721eb23901ce 开启一个交互模式的终端：

```
docker exec -it 721eb23901ce /bin/bash
```

![1148440-20190630235318810-1018356735](docker%E7%AC%94%E8%AE%B0.assets/1148440-20190630235318810-1018356735.png)

## 18.自定义镜像

~~~dockerfile
当使用 Docker 构建一个包含 CentOS、JDK 1.8、MySQL 5.7、Redis 和 Nginx 的容器时，可以按照以下步骤进行操作：

1. 在 Docker 主机上安装 Docker。
2. 创建一个 Dockerfile，其中包含以下内容：
# 使用官方的 CentOS 作为基础镜像
FROM centos:centos7

# 安装 JDK 1.8
RUN yum install -y java-1.8.0-openjdk-devel

# 安装 MySQL 5.7
RUN yum install -y https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
RUN yum install -y mysql-community-server

# 安装 Redis
RUN yum install -y epel-release
RUN yum install -y redis

# 安装 Nginx
RUN yum install -y nginx

# 设置环境变量
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk
ENV PATH $PATH:$JAVA_HOME/bin

# 暴露端口
EXPOSE 80 3306 6379

# 启动服务
CMD service mysqld start && service redis start && nginx -g "daemon off;"
```

3. 在 Dockerfile 所在的目录下执行以下命令构建镜像：

```bash
docker build -t myimage .
```

4. 构建完成后，可以运行以下命令创建并启动容器：

```bash
docker run -d -p 80:80 -p 3306:3306 -p 6379:6379 myimage
```

这将创建一个后台运行的容器，将主机的 80 端口映射到容器的 80 端口，3306 端口映射到容器的 3306 端口，6379 端口映射到容器的 6379 端口。

关于 Docker 的更多信息，你可以参考以下链接：
- Docker 官方文档：https://docs.docker.com/
- Docker 教程：https://www.runoob.com/docker/docker-tutorial.html

请注意，以上代码仅供参考，具体配置取决于你的需求和环境。
~~~

```
docker build -t myspringboot .
docker run -d -p 80:80 -p 3306:3306 -p 6379:6379 myimage
```

## 19.共享镜像

##### 如何把Docker镜像拷给别人

比如本地有个名为lyhero11/springbootapp2的镜像，操作如下。
docker save导出镜像:

```shell
docker save -o D:\docker-images\springbootapp2-latest.tar lyhero11/springbootapp2
```

在D:\docker-images\路径下会生成一个tar包springbootapp2-latest.tar，这个就是镜像，可以U盘拷给别人电脑上去。
然后docker load这个镜像：

```shell
docker load -i D:\docker-images\springbootapp2-latest.tar
```

注意：
上面的-o, -i分别代表--output和--input，save镜像的时候不加-o选项会导致load的时候报错：`Error processing tar file(exit status 1): archive/tar: invalid tar header`。而且save出来的镜像大小也不对，笔者这个镜像正常是105M，这样save出来的镜像是200多M.

