## <font style="color:rgb(51, 51, 51);">1.基础命令</font>
```bash
yum update
 yum install -y yum-utils device-mapper-persistent-data lvm2
 yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
 yum install docker-ce #社区版
 docker -v
```

<font style="color:rgb(51, 51, 51);">设置国内ustc镜像</font>

vi /etc/docker/daemon.json

```dockerfile
{
    "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}
```

<font style="color:rgb(51, 51, 51);">启动</font>

```dockerfile
systemctl start docker
systemctl restart docker
```

```dockerfile
状态
systemctl status docker
停止
systemctl stop docker
开机自启动
systemctl enable docker
查看概要
docker info
帮助
docker --help
```

## <font style="color:rgb(51, 51, 51);">2.镜像</font>
### <font style="color:rgb(51, 51, 51);">获取镜像</font>
```dockerfile
docker pull ubuntu
```

### <font style="color:rgb(51, 51, 51);">查看镜像</font>
```dockerfile
docker images
```

<font style="color:rgb(51, 51, 51);">各个选项说明:</font>

+ **<font style="color:rgb(51, 51, 51);">REPOSITORY：</font>**<font style="color:rgb(51, 51, 51);">表示镜像的仓库源</font>
+ **<font style="color:rgb(51, 51, 51);">TAG：</font>**<font style="color:rgb(51, 51, 51);">镜像的标签</font>
+ **<font style="color:rgb(51, 51, 51);">IMAGE ID：</font>**<font style="color:rgb(51, 51, 51);">镜像ID</font>
+ **<font style="color:rgb(51, 51, 51);">CREATED：</font>**<font style="color:rgb(51, 51, 51);">镜像创建时间</font>
+ **<font style="color:rgb(51, 51, 51);">SIZE：</font>**<font style="color:rgb(51, 51, 51);">镜像大小</font>

### <font style="color:rgb(51, 51, 51);">搜索</font>
docker search xxx

**<font style="color:rgb(51, 51, 51);">NAME:</font>**<font style="color:rgb(51, 51, 51);"> 镜像仓库源的名称</font>

**<font style="color:rgb(51, 51, 51);">DESCRIPTION:</font>**<font style="color:rgb(51, 51, 51);"> 镜像的描述</font>

**<font style="color:rgb(51, 51, 51);">OFFICIAL:</font>**<font style="color:rgb(51, 51, 51);"> 是否 docker 官方发布</font>

**<font style="color:rgb(51, 51, 51);">stars:</font>**<font style="color:rgb(51, 51, 51);"> 类似 Github 里面的 star，表示点赞、喜欢的意思。</font>

**<font style="color:rgb(51, 51, 51);">AUTOMATED:</font>**<font style="color:rgb(51, 51, 51);"> 自动构建。</font>

### <font style="color:rgb(51, 51, 51);">用版本为15.10的ubuntu系统镜像</font>
<font style="color:rgb(51, 51, 51);">来运行容器时，命令如下：</font>

```dockerfile
runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash 
root@d77ccb2e5cca:/#
```

<font style="color:rgb(51, 51, 51);">参数说明：</font>

+ **<font style="color:rgb(51, 51, 51);">-i</font>**<font style="color:rgb(51, 51, 51);">: 交互式操作。</font>
+ **<font style="color:rgb(51, 51, 51);">-t</font>**<font style="color:rgb(51, 51, 51);">: 终端。</font>
+ **<font style="color:rgb(51, 51, 51);">ubuntu:15.10</font>**<font style="color:rgb(51, 51, 51);">: 这是指用 ubuntu 15.10 版本镜像为基础来启动容器。</font>
+ **<font style="color:rgb(51, 51, 51);">/bin/bash</font>**<font style="color:rgb(51, 51, 51);">：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。</font>

### <font style="color:rgb(51, 51, 51);">删除镜像</font>
<font style="color:rgb(51, 51, 51);">镜像删除使用 </font>**<font style="color:rgb(51, 51, 51);">docker rmi</font>**<font style="color:rgb(51, 51, 51);"> 命令，比如我们删除 hello-world 镜像：</font>

```dockerfile
  docker rmi hello-world
```

### <font style="color:rgb(51, 51, 51);">创建镜像</font>
<font style="color:rgb(51, 51, 51);">当我们从 docker 镜像仓库中下载的镜像不能满足我们的需求时，我们可以通过以下两种方式对镜像进行更改。</font>

+ <font style="color:rgb(51, 51, 51);">1、从已经创建的容器中更新镜像，并且提交这个镜像</font>
+ <font style="color:rgb(51, 51, 51);">2、使用 Dockerfile 指令来创建一个新的镜像</font>

### <font style="color:rgb(51, 51, 51);">更新镜像</font>
<font style="color:rgb(51, 51, 51);">更新镜像之前，我们需要使用镜像来创建一个容器。</font>

```dockerfile
runoob@runoob:~$ docker run -t -i ubuntu:15.10 /bin/bash
root@e218edb10161:/#
```

<font style="color:rgb(51, 51, 51);">在运行的容器内使用 </font>**<font style="color:rgb(51, 51, 51);">apt-get update</font>**<font style="color:rgb(51, 51, 51);"> 命令进行更新。</font>

<font style="color:rgb(51, 51, 51);">在完成操作之后，输入 exit 命令来退出这个容器。</font>

<font style="color:rgb(51, 51, 51);">此时 ID 为 e218edb10161 的容器，是按我们的需求更改的容器。我们可以通过命令 docker commit 来提交容器副本。</font>

```dockerfile
runoob@runoob:~$ docker commit -m="has update" -a="runoob" e218edb10161 runoob/ubuntu:v2
sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8
```

<font style="color:rgb(51, 51, 51);">各个参数说明：</font>

+ **<font style="color:rgb(51, 51, 51);">-m:</font>**<font style="color:rgb(51, 51, 51);"> 提交的描述信息</font>
+ **<font style="color:rgb(51, 51, 51);">-a:</font>**<font style="color:rgb(51, 51, 51);"> 指定镜像作者</font>
+ **<font style="color:rgb(51, 51, 51);">e218edb10161：</font>**<font style="color:rgb(51, 51, 51);">容器 ID</font>
+ **<font style="color:rgb(51, 51, 51);">runoob/ubuntu:v2:</font>**<font style="color:rgb(51, 51, 51);"> 指定要创建的目标镜像名</font>

### <font style="color:rgb(51, 51, 51);">构建镜像</font>
<font style="color:rgb(51, 51, 51);">我们使用命令 </font>**<font style="color:rgb(51, 51, 51);">docker build</font>**<font style="color:rgb(51, 51, 51);"> ， 从零开始来创建一个新的镜像。为此，我们需要创建一个 Dockerfile 文件，其中包含一组指令来告诉 Docker 如何构建我们的镜像。</font>

```dockerfile
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

<font style="color:rgb(51, 51, 51);">每一个指令都会在镜像上创建一个新的层，每一个指令的前缀都必须是大写的。</font>

<font style="color:rgb(51, 51, 51);">第一条FROM，指定使用哪个镜像源</font>

<font style="color:rgb(51, 51, 51);">RUN 指令告诉docker 在镜像内执行命令，安装了什么。。。</font>

<font style="color:rgb(51, 51, 51);">然后，我们使用 Dockerfile 文件，通过 docker build 命令来构建一个镜像。</font>

```dockerfile
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

<font style="color:rgb(51, 51, 51);">参数说明：</font>

+ **<font style="color:rgb(51, 51, 51);">-t</font>**<font style="color:rgb(51, 51, 51);"> ：指定要创建的目标镜像名</font>
+ **<font style="color:rgb(51, 51, 51);">.</font>**<font style="color:rgb(51, 51, 51);"> ：Dockerfile 文件所在目录，可以指定Dockerfile 的绝对路径</font>

<font style="color:rgb(51, 51, 51);">使用docker images 查看创建的镜像已经在列表中存在,镜像ID为860c279d2fec</font>

```dockerfile
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

<font style="color:rgb(51, 51, 51);">我们可以使用新的镜像来创建容器</font>

```dockerfile
runoob@runoob:~$ docker run -t -i runoob/centos:6.7  /bin/bash
[root@41c28d18b5fb /]# id runoob
uid=500(runoob) gid=500(runoob) groups=500(runoob)
```

<font style="color:rgb(51, 51, 51);">从上面看到新镜像已经包含我们创建的用户 runoob。</font>

### <font style="color:rgb(51, 51, 51);">设置镜像标签</font>
<font style="color:rgb(51, 51, 51);">我们可以使用 docker tag 命令，为镜像添加一个新的标签。</font>

runoob@runoob:~$ docker tag 860c279d2fec runoob/centos:dev

<font style="color:rgb(51, 51, 51);">docker tag 镜像ID，这里是 860c279d2fec ,用户名称、镜像源名(repository name)和新的标签名(tag)。</font>

<font style="color:rgb(51, 51, 51);">使用 docker images 命令可以看到，ID为860c279d2fec的镜像多一个标签。</font>

```dockerfile
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

## <font style="color:rgb(51, 51, 51);">3.容器</font>
### <font style="color:rgb(51, 51, 51);">启动容器</font>
docker run -it ubuntu /bin/bash

<font style="color:rgb(51, 51, 51);">参数说明：</font>

+ **<font style="color:rgb(51, 51, 51);">-i</font>**<font style="color:rgb(51, 51, 51);">: 交互式操作。</font>
+ **<font style="color:rgb(51, 51, 51);">-t</font>**<font style="color:rgb(51, 51, 51);">: 终端。</font>
+ **<font style="color:rgb(51, 51, 51);">ubuntu</font>**<font style="color:rgb(51, 51, 51);">: ubuntu 镜像。</font>
+ **<font style="color:rgb(51, 51, 51);">/bin/bash</font>**<font style="color:rgb(51, 51, 51);">：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。</font>

### <font style="color:rgb(51, 51, 51);">启动已停止运行的容器</font>
<font style="color:rgb(51, 51, 51);">查看所有的容器命令如下：</font>

docker ps -a

### <font style="color:rgb(51, 51, 51);">开启容器</font>
docker start id号

### <font style="color:rgb(51, 51, 51);">后台运行</font>
<font style="color:rgb(51, 51, 51);">在大部分的场景下，我们希望 docker 的服务是在后台运行的，我们可以过 </font>**<font style="color:rgb(51, 51, 51);">-d</font>**<font style="color:rgb(51, 51, 51);"> 指定容器的运行模式。</font>

docker run -itd --name ubuntu-test ubuntu /bin/bash

**<font style="color:rgb(51, 51, 51);">注：</font>**<font style="color:rgb(51, 51, 51);">加了 </font>**<font style="color:rgb(51, 51, 51);">-d</font>**<font style="color:rgb(51, 51, 51);"> 参数默认不会进入容器，想要进入容器需要使用指令 </font>**<font style="color:rgb(51, 51, 51);">docker exec</font>**<font style="color:rgb(51, 51, 51);">（下面会介绍到）。</font>

### <font style="color:rgb(51, 51, 51);">后台运行</font>
<font style="color:rgb(51, 51, 51);">在大部分的场景下，我们希望 docker 的服务是在后台运行的，我们可以过 </font>**<font style="color:rgb(51, 51, 51);">-d</font>**<font style="color:rgb(51, 51, 51);"> 指定容器的运行模式。</font>

$ docker run -itd --name ubuntu-test ubuntu /bin/bash

<font style="color:rgb(51, 51, 51);">停止的容器可以通过 docker restart 重启：</font>

$ docker restart <容器 ID>

### <font style="color:rgb(51, 51, 51);">进入容器</font>
<font style="color:rgb(51, 51, 51);">在使用 </font>**<font style="color:rgb(51, 51, 51);">-d</font>**<font style="color:rgb(51, 51, 51);"> 参数时，容器启动后会进入后台。此时想要进入容器，可以通过以下指令进入：</font>

+ **<font style="color:rgb(51, 51, 51);">docker attach</font>**
+ **<font style="color:rgb(51, 51, 51);">docker exec</font>**<font style="color:rgb(51, 51, 51);">：推荐大家使用 docker exec 命令，因为此命令会退出容器终端，但不会导致容器的停止。</font>

**<font style="color:rgb(51, 51, 51);">attach 命令</font>**

<font style="color:rgb(51, 51, 51);">下面演示了使用 docker attach 命令。</font>

$ docker attach 1e560fca3906 

**<font style="color:rgb(51, 51, 51);">注意：</font>**<font style="color:rgb(51, 51, 51);"> 如果从这个容器退出，会导致容器的停止。</font>

**<font style="color:rgb(51, 51, 51);">exec 命令</font>**

<font style="color:rgb(51, 51, 51);">下面演示了使用 docker exec 命令。</font>

docker exec -it 243c32535da7 /bin/bash

**<font style="color:rgb(51, 51, 51);">注意：</font>**<font style="color:rgb(51, 51, 51);"> 如果从这个容器退出，容器不会停止，这就是为什么推荐大家使用 </font>**<font style="color:rgb(51, 51, 51);">docker exec</font>**<font style="color:rgb(51, 51, 51);"> 的原因。</font>

<font style="color:rgb(51, 51, 51);">更多参数说明请使用 </font>**<font style="color:rgb(51, 51, 51);">docker exec --help</font>**<font style="color:rgb(51, 51, 51);"> 命令查看。</font>

### <font style="color:rgb(51, 51, 51);">导出和导入容器</font>
**<font style="color:rgb(51, 51, 51);">导出容器</font>**

<font style="color:rgb(51, 51, 51);">如果要导出本地某个容器，可以使用 </font>**<font style="color:rgb(51, 51, 51);">docker export</font>**<font style="color:rgb(51, 51, 51);"> 命令。</font>

$ docker export 1e560fca3906 > ubuntu.tar

<font style="color:rgb(51, 51, 51);">这样将导出容器快照到本地文件。</font>

**<font style="color:rgb(51, 51, 51);">导入容器快照</font>**

<font style="color:rgb(51, 51, 51);">可以使用 docker import 从容器快照文件中再导入为镜像，以下实例将快照文件 ubuntu.tar 导入到镜像 test/ubuntu:v1:</font>

$ cat docker/ubuntu.tar | docker import - test/ubuntu:v1

<font style="color:rgb(51, 51, 51);">此外，也可以通过指定 URL 或者某个目录来导入，例如：</font>

$ docker import http://example.com/exampleimage.tgz example/imagerepo

### <font style="color:rgb(51, 51, 51);">删除容器</font>
<font style="color:rgb(51, 51, 51);">删除容器使用 </font>**<font style="color:rgb(51, 51, 51);">docker rm</font>**<font style="color:rgb(51, 51, 51);"> 命令：</font>

$ docker rm -f 1e560fca3906

<font style="color:rgb(51, 51, 51);">下面的命令可以清理掉所有处于终止状态的容器。</font>

$ docker container prune

## <font style="color:rgb(51, 51, 51);">4.文件拷贝</font>
<font style="color:rgb(51, 51, 51);">将文件拷贝到容器内可以使用cp</font>

docker cp 需要拷贝的文件或者目录  容器名称:容器目录

<font style="color:rgb(51, 51, 51);">也可以将文件从容器中拷贝出来</font>

docker cp 容器名称:容器目录 需要拷贝的文件或目录

## <font style="color:rgb(51, 51, 51);">5.目录挂载</font>
<font style="color:rgb(51, 51, 51);">我们可以在创建容器的时候，将宿主机的目录与容器内的目录进行映射，这样我们就可以通过修改宿主机某个目录的文件从而去影响容器。</font><font style="color:rgb(51, 51, 51);">创建容器添加-v参数后边为宿主机目录:容器目录，例如:</font>

docker run -di -v /usr/local/myhtml:/usr/local/myhtml --name=mycentos3 centos:7

<font style="color:rgb(51, 51, 51);">如果你共享的是多级的目录，可能会出现权限不足的提示。</font><font style="color:rgb(51, 51, 51);">这是因为CentOS7中的安全模块selinux把权限禁掉了，我们需要添加参数--privileged=true 来解决挂载的目录没有权限的问题</font>

## <font style="color:rgb(51, 51, 51);">6.查看一个json信息</font>
docker inspect 容器名

### <font style="color:rgb(51, 51, 51);">过滤（查看IP）</font>
docker inspect --format='{{.NetworkSettings.IPAddress}}' 容器名

## <font style="color:rgb(51, 51, 51);">7.mysql部署</font>
### <font style="color:rgb(51, 51, 51);">拉取镜像</font>
docker pull centos/mysql-57-centos7

### <font style="color:rgb(51, 51, 51);">创建容器</font>
docker run -di --name=tensquare_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 j

<font style="color:rgb(51, 51, 51);">-p:端口映射 宿主机映射端口:容器运行端口</font>

<font style="color:rgb(51, 51, 51);">-e:代表添加环境变量 MYSQL_ROOT_PASSWORD 是root用户的登录密码</font>

### <font style="color:rgb(51, 51, 51);">进入mysql容器</font>
docker exec -it tensquare_mysql /bin/bash

### <font style="color:rgb(51, 51, 51);">登录mysql</font>
mysql -u root -p

## <font style="color:rgb(51, 51, 51);">8.tomcat部署</font>
### <font style="color:rgb(51, 51, 51);">拉取镜像</font>
docker pull tomcat:7-jre7

### <font style="color:rgb(51, 51, 51);">创建容器</font>
docker run -di --name=mytomcat -p 9000:8080 -v /usr/local/webapps:/usr/local/tomcat/webapps tomcat:7-jre7

<font style="color:rgb(51, 51, 51);">-p:端口映射 宿主机映射端口:容器运行端口</font>

## <font style="color:rgb(51, 51, 51);">9.Nginx部署</font>
### <font style="color:rgb(51, 51, 51);">拉取镜像</font>
docker pull nginx

### <font style="color:rgb(51, 51, 51);">创建容器</font>
docker run -di --name=mynginx -p 80:80 nginx

## <font style="color:rgb(51, 51, 51);">10.Redis部署</font>
### <font style="color:rgb(51, 51, 51);">拉取镜像</font>
docker pull redis

### <font style="color:rgb(51, 51, 51);">创建容器</font>
docker run -di --name=myredis -p 6379:6379 redis

## <font style="color:rgb(51, 51, 51);">11.备份和迁移</font>
### <font style="color:rgb(51, 51, 51);">容器保存为镜像</font>
docker commit mynginx mynginx_img

### <font style="color:rgb(51, 51, 51);">镜像备份</font>
<font style="color:rgb(51, 51, 51);">将镜像保存为tar文件</font>

docker save -o mynginx.tar mynginx_img

### <font style="color:rgb(51, 51, 51);">镜像恢复和迁移</font>
<font style="color:rgb(51, 51, 51);">先删除mynginx_img镜像，然后执行命令恢复</font>

docker load -i mynginx.tar

<font style="color:rgb(51, 51, 51);">-i:输入的文件</font>

## <font style="color:rgb(51, 51, 51);">12.Dockerfile</font>
### <font style="color:rgb(51, 51, 51);">介绍</font>
<font style="color:rgb(51, 51, 51);">Dockerfile是由一系列命令和参数构成的脚本，这些命令应用于基础镜像并最终创建一个新的镜像。</font><font style="color:rgb(51, 51, 51);">1、对于开发人员:可以为开发团队提供一个完全一致的开发环境;</font><font style="color:rgb(51, 51, 51);">2、对于测试人员:可以直接拿开发时所构建的镜像或者通过Dockerfile文件构建一个新的镜像开始工作了;</font><font style="color:rgb(51, 51, 51);">3、对于运维人员:在部署时，可以实现应用的无缝移植。</font>

### <font style="color:rgb(51, 51, 51);">dockerfile 的命令摘要</font>
+ <font style="color:rgb(51, 51, 51);">FROM- 镜像从那里来</font>
+ <font style="color:rgb(51, 51, 51);">MAINTAINER- 镜像维护者信息</font>
+ <font style="color:rgb(51, 51, 51);">RUN- 构建镜像执行的命令，每一次RUN都会构建一层</font>
+ <font style="color:rgb(51, 51, 51);">CMD- 容器启动的命令，如果有多个则以最后一个为准，也可以为ENTRYPOINT提供参数</font>
+ <font style="color:rgb(51, 51, 51);">VOLUME- 定义数据卷，如果没有定义则使用默认</font>
+ <font style="color:rgb(51, 51, 51);">USER- 指定后续执行的用户组和用户</font>
+ <font style="color:rgb(51, 51, 51);">WORKDIR- 切换当前执行的工作目录</font>
+ <font style="color:rgb(51, 51, 51);">HEALTHCHECH- 健康检测指令</font>
+ <font style="color:rgb(51, 51, 51);">ARG- 变量属性值，但不在容器内部起作用</font>
+ <font style="color:rgb(51, 51, 51);">EXPOSE- 暴露端口</font>
+ <font style="color:rgb(51, 51, 51);">ENV- 环境变量属性值，容器内部也会起作用</font>
+ <font style="color:rgb(51, 51, 51);">ADD- 添加文件，如果是压缩文件也解压</font>
+ <font style="color:rgb(51, 51, 51);">COPY- 添加文件，以复制的形式</font>
+ <font style="color:rgb(51, 51, 51);">ENTRYPOINT- 容器进入时执行的命令</font>

## <font style="color:rgb(51, 51, 51);">13.使用dockerfile创建一个jdk1.8镜像</font>
```dockerfile
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

### <font style="color:rgb(51, 51, 51);">构建</font>
docker build -t 'jdk1.8' .

<font style="color:rgb(51, 51, 51);">注意：. 代表在当前目录</font>

## <font style="color:rgb(51, 51, 51);">14.Docker私有仓库</font>
### <font style="color:rgb(51, 51, 51);">仓库搭建和配置</font>
<font style="color:rgb(51, 51, 51);">拉去私有仓库镜像</font>

docker pull registry

<font style="color:rgb(51, 51, 51);">启动私有仓库容器</font>

docker run -di --name=registry -p 5000:5000 registry

<font style="color:rgb(51, 51, 51);">打开浏览器输入地址</font>

http://ip:5000/v2/_catalog

<font style="color:rgb(51, 51, 51);">看到{"repositories":[]}表示私有仓库搭建成功并且内容为空</font>

<font style="color:rgb(51, 51, 51);">修改daemon.json</font>

vi /etc/docker/daemon.json

<font style="color:rgb(51, 51, 51);">添加以下内容，保存退出(让docker信任私有仓库地址)</font>

{"insecure-registries":["ip:5000"]}

<font style="color:rgb(51, 51, 51);">重启docker</font>

systemctl restart docker

### <font style="color:rgb(51, 51, 51);">将镜像上传至私有仓库</font>
<font style="color:rgb(51, 51, 51);">标记镜像为私有仓库的镜像</font>

docker tag jdk1.8 ip:5000/jdk1.8

<font style="color:rgb(51, 51, 51);">上传标记的镜像</font>

docker push ip:5000/jdk1.8

## <font style="color:rgb(51, 51, 51);">15.下载私有仓库镜像</font>
### <font style="color:rgb(51, 51, 51);">信任对应的docker地址</font>
<font style="color:rgb(51, 51, 51);">修改daemon.json</font>

vi /etc/docker/daemon.json

<font style="color:rgb(51, 51, 51);">添加以下内容，保存退出(让docker信任私有仓库地址)</font>

{"insecure-registries":["ip:5000"]}

<font style="color:rgb(51, 51, 51);">重启docker</font>

systemctl restart docker

### <font style="color:rgb(51, 51, 51);">查看镜像仓库</font>
http://ip:5000/v2/_catalog

### <font style="color:rgb(51, 51, 51);">下拉镜像</font>
docker pull ip:5000/jdk1.8

## <font style="color:rgb(51, 51, 51);">16.运行一个 web 应用</font>
<font style="color:rgb(51, 51, 51);">前面我们运行的容器并没有一些什么特别的用处。</font>

<font style="color:rgb(51, 51, 51);">接下来让我们尝试使用 docker 构建一个 web 应用程序。</font>

<font style="color:rgb(51, 51, 51);">我们将在docker容器中运行一个 Python Flask 应用来运行一个web应用。</font>

```dockerfile
runoob@runoob:~# docker pull training/webapp  # 载入镜像
runoob@runoob:~# docker run -d -P training/webapp python app.py
```

<font style="color:rgb(51, 51, 51);">参数说明:</font>

+ **<font style="color:rgb(51, 51, 51);">-d:</font>**<font style="color:rgb(51, 51, 51);">让容器在后台运行。</font>
+ **<font style="color:rgb(51, 51, 51);">-P:</font>**<font style="color:rgb(51, 51, 51);">将容器内部使用的网络端口随机映射到我们使用的主机上。</font>

## <font style="color:rgb(51, 51, 51);">17.docker run 和 docker exec 的差异</font>
---

**<font style="color:rgb(51, 51, 51);">docker run ：</font>**<font style="color:rgb(51, 51, 51);">根据镜像创建一个容器并运行一个命令，操作的对象是 </font>**<font style="color:rgb(51, 51, 51);">镜像</font>**<font style="color:rgb(51, 51, 51);">；</font>

**<font style="color:rgb(51, 51, 51);">docker exec ：</font>**<font style="color:rgb(51, 51, 51);">在运行的容器中执行命令，操作的对象是 </font>**<font style="color:rgb(51, 51, 51);">容器</font>**<font style="color:rgb(51, 51, 51);">。</font>

---

### **<font style="color:rgb(51, 51, 51);">docker run 命令</font>**
### **<font style="color:rgb(51, 51, 51);">语法</font>**
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

<font style="color:rgb(51, 51, 51);">OPTIONS说明：</font>

+ **<font style="color:rgb(51, 51, 51);">-a stdin:</font>**<font style="color:rgb(51, 51, 51);"> 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；</font>
+ **<font style="color:rgb(51, 51, 51);">-d:</font>**<font style="color:rgb(51, 51, 51);"> 后台运行容器，并返回容器ID；</font>
+ **<font style="color:rgb(51, 51, 51);">-i:</font>**<font style="color:rgb(51, 51, 51);"> 以交互模式运行容器，通常与 -t 同时使用；</font>
+ **<font style="color:rgb(51, 51, 51);">-P:</font>**<font style="color:rgb(51, 51, 51);"> 随机端口映射，容器内部端口</font>**<font style="color:rgb(51, 51, 51);">随机</font>**<font style="color:rgb(51, 51, 51);">映射到主机的高端口</font>
+ **<font style="color:rgb(51, 51, 51);">-p:</font>**<font style="color:rgb(51, 51, 51);"> 指定端口映射，格式为：主机(宿主)端口:容器端口</font>
+ **<font style="color:rgb(51, 51, 51);">-t:</font>**<font style="color:rgb(51, 51, 51);"> 为容器重新分配一个伪输入终端，通常与 -i 同时使用；</font>
+ **<font style="color:rgb(51, 51, 51);">--name="nginx-lb":</font>**<font style="color:rgb(51, 51, 51);"> 为容器指定一个名称；</font>
+ **<font style="color:rgb(51, 51, 51);">--dns 8.8.8.8:</font>**<font style="color:rgb(51, 51, 51);"> 指定容器使用的DNS服务器，默认和宿主一致；</font>
+ **<font style="color:rgb(51, 51, 51);">--dns-search example.com:</font>**<font style="color:rgb(51, 51, 51);"> 指定容器DNS搜索域名，默认和宿主一致；</font>
+ **<font style="color:rgb(51, 51, 51);">-h "mars":</font>**<font style="color:rgb(51, 51, 51);"> 指定容器的hostname；</font>
+ **<font style="color:rgb(51, 51, 51);">-e username="ritchie":</font>**<font style="color:rgb(51, 51, 51);"> 设置环境变量；</font>
+ **<font style="color:rgb(51, 51, 51);">--env-file=[]:</font>**<font style="color:rgb(51, 51, 51);"> 从指定文件读入环境变量；</font>
+ **<font style="color:rgb(51, 51, 51);">--cpuset="0-2" or --cpuset="0,1,2":</font>**<font style="color:rgb(51, 51, 51);"> 绑定容器到指定CPU运行；</font>
+ **<font style="color:rgb(51, 51, 51);">-m :</font>**<font style="color:rgb(51, 51, 51);">设置容器使用内存最大值；</font>
+ **<font style="color:rgb(51, 51, 51);">--net="bridge":</font>**<font style="color:rgb(51, 51, 51);"> 指定容器的网络连接类型，支持 bridge/host/none/container:<name|id> 四种类型；</font>
+ **<font style="color:rgb(51, 51, 51);">--link=[]:</font>**<font style="color:rgb(51, 51, 51);"> 添加链接到另一个容器；</font>
+ **<font style="color:rgb(51, 51, 51);">--expose=[]:</font>**<font style="color:rgb(51, 51, 51);"> 开放一个端口或一组端口；</font>
+ **<font style="color:rgb(51, 51, 51);">--volume , -v:</font>**<font style="color:rgb(51, 51, 51);"> 绑定一个卷</font>

### <font style="color:rgb(51, 51, 51);">实例</font>
<font style="color:rgb(51, 51, 51);">使用docker镜像 nginx:latest 以后台模式启动一个容器，并将容器命名为my-nginx。</font>

docker run --name my-nginx -p 8081:80 -d nginx:latest

<font style="color:rgb(51, 51, 51);">浏览器访问 http://主机IP:8081，效果如下：</font>

<font style="color:rgb(51, 51, 51);">使用镜像 nginx:latest 以后台模式启动一个容器，并将容器的80端口映射到主机随机端口：</font>

docker run -P -d nginx:latest

<font style="color:rgb(51, 51, 51);">使用镜像 nginx:latest 以后台模式启动一个容器，将主机的 80 端口映射到容器的 80 端口，主机的目录 /data 映射到容器的 /data：</font>

docker run -p 80:80 -v /data:/data -d nginx:latest

<font style="color:rgb(51, 51, 51);">使用镜像 nginx:latest 以交互模式启动一个容器，在容器内执行/bin/bash命令：</font>

docker run -it nginx:latest /bin/bash

### **<font style="color:rgb(51, 51, 51);">docker exec 命令</font>**
### **<font style="color:rgb(51, 51, 51);">语法</font>**
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

<font style="color:rgb(51, 51, 51);">OPTIONS说明：</font>

+ **<font style="color:rgb(51, 51, 51);">-d :</font>**<font style="color:rgb(51, 51, 51);"> 分离模式: 在后台运行</font>
+ **<font style="color:rgb(51, 51, 51);">-i :</font>**<font style="color:rgb(51, 51, 51);"> 即使没有附加也保持STDIN 打开</font>
+ **<font style="color:rgb(51, 51, 51);">-t :</font>**<font style="color:rgb(51, 51, 51);"> 分配一个伪终端</font>

<font style="color:rgb(51, 51, 51);">在容器名称 my-nginx 中开启一个交互模式的终端：</font>

docker exec -it my-nginx /bin/bash

<font style="color:rgb(51, 51, 51);">或者使用容器ID 721eb23901ce 开启一个交互模式的终端：</font>

docker exec -it 721eb23901ce /bin/bash

## <font style="color:rgb(51, 51, 51);">18.自定义镜像</font>
```dockerfile
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
```

```dockerfile
docker build -t myspringboot .
docker run -d -p 80:80 -p 3306:3306 -p 6379:6379 myimage
```

## <font style="color:rgb(51, 51, 51);">19.共享镜像</font>
##### <font style="color:rgb(51, 51, 51);">如何把Docker镜像拷给别人</font>
<font style="color:rgb(51, 51, 51);">比如本地有个名为lyhero11/springbootapp2的镜像，操作如下。</font><font style="color:rgb(51, 51, 51);">docker save导出镜像:</font>

docker save -o D:\docker-images\springbootapp2-latest.tar lyhero11/springbootapp2

<font style="color:rgb(51, 51, 51);">在D:\docker-images\路径下会生成一个tar包springbootapp2-latest.tar，这个就是镜像，可以U盘拷给别人电脑上去。</font><font style="color:rgb(51, 51, 51);">然后docker load这个镜像：</font>

docker load -i D:\docker-images\springbootapp2-latest.tar

<font style="color:rgb(51, 51, 51);">注意：</font><font style="color:rgb(51, 51, 51);">上面的-o, -i分别代表--output和--input，save镜像的时候不加-o选项会导致load的时候报错：</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">Error processing tar file(exit status 1): archive/tar: invalid tar header</font>`<font style="color:rgb(51, 51, 51);">。而且save出来的镜像大小也不对，笔者这个镜像正常是105M，这样save出来的镜像是200多M.</font>

  
 

