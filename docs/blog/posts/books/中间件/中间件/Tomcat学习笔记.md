## 1.JVM介绍


JVM是Java Virtual Machine（Java虚拟机）的缩写



Java虚拟机本质是就是一个程序，当它在命令行上启动的时候，就开始执行保存在某字节码文件中的指令。Java语言的可移植性正是建立在Java虚拟机的基础上。任何平台只要装有针对于该平台的Java虚拟机，字节码文件（.class）就可以在该平台上运行。这就是“一次编译，多次运行”。



## 2.Tomcat介绍


### a.什么是Tomcat


Tomcat和我们此前学习的 Nginx 类似，也是一个Web服务器。



### b.Tomcat与Nginx有什么区别？


tomcat是一个java版的web服务器



Nginx仅支持静态资源，而Tomcat则支持Java开发的 jsp 动态资源和静态资源。 Nginx适合做前端负载均衡，而Tomcat适合做后端应用服务处理。 通常情况下，企业会使用 Nginx+tomcat 结合使用，由Nginx处理静态资源，Tomcat处理动态资源。



## 3.Tomcat快速安装
| 机器名 | ip地址 | 软件包 |
| :--- | :--- | :--- |
| tomcat01 | 192.168.107.200 | tomcat+nfs |
| tomcat02 | 192.168.107.201 | tomcat+nfs |
| lb01 | 192.168.107.202 | nginx+mariadb+redis+nfs |




安装方法1:



```shell
rpm -ivh jdk-8u102-linux-x64.rpm
mkdir /app -p
tar xf apache-tomcat-8.0.27.tar.gz -C /app
/app/apache-tomcat-8.0.27/bin/startup.sh
```



安装方法2:



```shell
#适合debian和ubuntu等其他linux发行版
tar xf jdk-8u171-linux-x64.tar.gz -C /app/
ln -s /app/jdk1.8.0_171 /app/jdk
sed -i.ori '$a export JAVA_HOME=/app/jdk\nexport PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH\nexport CLASSPATH=.$CLASSPATH:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$JAVA_HOME/lib/tools.jar' /etc/profile
source /etc/profile
mkdir /app/
tar xf apache-tomcat-8.5.92.tar.gz -C /app
mv apache-tomcat-8.5.92 tomcat
/app/tomcat/bin/startup.sh
```



## 4.Tomcat启动慢解决方案


```shell
没优化之前启动时间
[root@tomcat logs]# grep 'Server startup' catalina.out
03-Aug-2019 03:15:18.225 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in 591050 ms
优化之后启动时间
[root@tomcat logs]# grep 'Server startup' catalina.out
03-Aug-2019 03:15:18.225 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in 591050 ms
03-Aug-2019 03:22:14.112 INFO [main] org.apache.catalina.startup.Catalina.start Server startup in 1326 ms
优化方法：
vi /usr/java/jdk1.8.0_102/jre/lib/security/java.security
securerandom.source=file:/dev/urandom
```



## 5.tomcat目录结构介绍


```shell
[root@tomcat apache-tomcat-8.0.27]# ll
total 92
drwxr-xr-x 2 root root  4096 Aug  3 03:05 bin  #主要包含启动、关闭tomcat脚本和脚本依赖文件  非常重要
drwxr-xr-x 3 root root   198 Aug  3 03:05 conf #tomcat配置文件目录          非常重要
drwxr-xr-x 2 root root  4096 Aug  3 03:05 lib  #tomcat运行需要加载的jar包    非常重要
-rw-r--r-- 1 root root 57011 Sep 28  2015 LICENSE #license文件，不重要
drwxr-xr-x 2 root root   197 Aug  3 03:15 logs  #在运行过程中产生的日志文件   非常重要
-rw-r--r-- 1 root root  1444 Sep 28  2015 NOTICE #不重要
-rw-r--r-- 1 root root  6741 Sep 28  2015 RELEASE-NOTES #版本特性，不重要
-rw-r--r-- 1 root root 16204 Sep 28  2015 RUNNING.txt   #帮助文件，不重要
drwxr-xr-x 2 root root    30 Aug  3 03:05 temp    #存放临时文件
drwxr-xr-x 7 root root    81 Sep 28  2015 webapps #站点目录   非常重要
drwxr-xr-x 3 root root    22 Aug  3 03:05 work    #tomcat运行时产生的缓存文件
```



## 6.tomcat配置文件


核心配置文件： **/app/apache-tomcat-8.0.27/conf/server.xml**



```xml
<?xml version="1.0" encoding="UTF-8"?>
<Server port="8005" shutdown="SHUTDOWN">
  <Listener className="org.apache.catalina.startup.VersionLoggerListener" />
  <Listener className="org.apache.catalina.core.AprLifecycleListener" SSLEngine="on" />
  <Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener" />
  <Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener" />
  <Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener" />
  <GlobalNamingResources>
    <Resource name="UserDatabase" auth="Container"
              type="org.apache.catalina.UserDatabase"
              description="User database that can be updated and saved"
              factory="org.apache.catalina.users.MemoryUserDatabaseFactory"
              pathname="conf/tomcat-users.xml" />
  </GlobalNamingResources>
  <Service name="Catalina">
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443"
               maxParameterCount="1000"
               />
    <Engine name="Catalina" defaultHost="localhost">
      <Realm className="org.apache.catalina.realm.LockOutRealm">
        <Realm className="org.apache.catalina.realm.UserDatabaseRealm"
               resourceName="UserDatabase"/>
      </Realm>

      <Host name="localhost"  appBase="webapps"
            unpackWARs="true" autoDeploy="true">
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="localhost_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />
      </Host>
    </Engine>
  </Service>
</Server>
```



```xml
这是一个 Apache Tomcat 服务器的配置文件，通常称为 `server.xml`，它包含了 Tomcat 服务器的配置信息。以下是对该配置文件内容的解释：

1. `<Server>` 元素：
   - `port="8005"`：Tomcat Shutdown 端口，用于远程关闭 Tomcat 服务器。
   - `shutdown="SHUTDOWN"`：关闭命令，用于远程关闭 Tomcat 服务器。

2. `<Listener>` 元素（多个）：
   - 定义了一系列的监听器，用于监听 Tomcat 服务器的事件。
   - `org.apache.catalina.startup.VersionLoggerListener`：用于记录 Tomcat 版本信息。
   - `org.apache.catalina.core.AprLifecycleListener`：用于支持 Apache Portable Runtime（APR），用于性能优化和安全。
   - `org.apache.catalina.core.JreMemoryLeakPreventionListener`：用于检测和预防内存泄漏。
   - `org.apache.catalina.mbeans.GlobalResourcesLifecycleListener`：用于管理全局资源的生命周期。
   - `org.apache.catalina.core.ThreadLocalLeakPreventionListener`：用于预防线程本地内存泄漏。

3. `<GlobalNamingResources>` 元素：
   - 定义全局的命名资源，这些资源可以在整个服务器中使用。
   - 在此示例中，定义了一个名为 "UserDatabase" 的资源，用于配置用户数据库。

4. `<Service>` 元素：
   - 定义 Tomcat 服务，通常名为 "Catalina"。
   - 包含一个或多个 `<Connector>` 和一个 `<Engine>`。

5. `<Connector>` 元素：
   - 定义用于接收客户端请求的连接器，例如 HTTP 连接器。
   - `port="8080"`：监听端口号。
   - `protocol="HTTP/1.1"`：使用的协议。
   - `connectionTimeout="20000"`：连接超时时间（毫秒）。
   - `redirectPort="8443"`：重定向端口，用于 HTTPS。
   - `maxParameterCount="1000"`：最大参数个数。

6. `<Engine>` 元素：
   - 定义用于处理客户端请求的引擎。
   - `name="Catalina"`：引擎名称。
   - `defaultHost="localhost"`：默认主机名。

7. `<Realm>` 元素：
   - 定义认证和授权信息。
   - `className="org.apache.catalina.realm.LockOutRealm"`：使用 LockOutRealm 基础。
   - 内部嵌套 `<Realm>` 元素用于配置用户数据库的 Realm。

8. `<Host>` 元素：
   - 定义虚拟主机。
   - `name="localhost"`：虚拟主机名。
   - `appBase="webapps"`：应用基础目录。
   - `unpackWARs="true"`：是否解压 WAR 文件。
   - `autoDeploy="true"`：是否自动部署应用。

9. `<Valve>` 元素：
   - 定义阀门，用于在请求处理过程中执行特定的任务。
   - 在此示例中，`org.apache.catalina.valves.AccessLogValve` 用于记录访问日志。

这个 `server.xml` 配置文件用于定义 Tomcat 服务器的全局设置、服务、连接器和虚拟主机。通过编辑和配置此文件，可以调整 Tomcat 服务器的行为和性能。注意，在编辑 `server.xml` 文件之前，务必备份原始配置以防止意外错误。
```



一个tomcat实例一个server



一个server中包含多个Connector，Connector的主要功能是接受、响应用户请求。



service的作用是：将connector关联至engine(catalina引擎)



一个host就是一个站点，类似于nginx的多站点



context类似于nginx中location的概念



[Tomcat中的Connector配置讲解](https://www.jb51.net/article/157199.htm)



## 7.Tomcat部署zrlog


```shell
vim  /app/apache-tomcat-8.0.27/conf/server.xml
      <Host name="blog.liyedong.com"  appBase="/html"
            unpackWARs="true" autoDeploy="true">
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
               prefix="blog.liyedong.com_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />
      </Host>
      
/app/tomcat/bin/shutdown.sh
/app/tomcat/bin/startup.sh
mv ROOT.war /html
```



```shell
systemctl start mariadb.service
systemctl enable mariadb.service
mysql_secure_installation #安全初始化
mysql
create database zrlog;
grant all on zrlog.* to zrlog@'192.168.220.%' identified by '123456';
```



## 8.配置basic认证


```xml
vim /app/tomcat/conf/tomcat-users.xml
<role rolename="manager-gui"/>
<role rolename="admin-gui"/>
<user username="tomcat" password="123456" roles="admin-gui,manager-gui"/>
```



### 修改默认本地访问管理网站


默认本地ip才能访问这些管理网站，开放内网访问，添加访问管理网站的ip，在对应的context.xml文件，将192.168网段的ip全部允许访问



```xml
vi /app/tomcat/webapps/docs/META-INF/context.xml
vi /app/tomcat/webapps/examples/META-INF/context.xml
vi /app/tomcat/webapps/host-manager/META-INF/context.xml
vi /app/tomcat/webapps/manager/META-INF/context.xml
<Context antiResourceLocking="false" >
  <Valve className="org.apache.catalina.valves.RemoteAddrValve"
     allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1|192\.168\.\d+\.\d+" />
</Context>
```



### 配置zrlog的admin进行basic认证


```xml
vim /html/ROOT/WEB-INF/web.xml
<web-app>
......    
    <security-constraint>
        <web-resource-collection>
            <web-resource-name>test</web-resource-name>
            <url-pattern>/admin/login/*</url-pattern>
        </web-resource-collection>
        
        <auth-constraint>
            <role-name>test100</role-name>
        </auth-constraint>
    </security-constraint> 
    <login-config>
        <auth-method>BASIC</auth-method>
        <realm-name>Default</realm-name>
    </login-config>
</web-app>

vim /app/tomcat/conf/tomcat-users.xml
<role rolename="manager-gui"/>
<role rolename="admin-gui"/>
<role rolename="test100"/>
<user username="tomcat" password="123456" roles="manager-gui,admin-gui,test100"/>
```



## 9.Nginx+Tomcat集群架构实战


### tomcat2主机配置


```shell
#推送
scp -rp /html root@192.168.107.201:/ #将html目录推送到tomcat2主机的根目录下
[root@master conf]# scp -rp server.xml tomcat-users.xml root@192.168.107.201:`pwd`
```



### lb1主机安装nginx


```shell
yum search nginx
yum install pcp-pmda-nginx.x86_64
whereis nginx
[root@master ~]# whereis nginx
nginx: /usr/local/nginx
grep -Ev '^$|#' /usr/local/nginx/conf/nginx.conf.default >/usr/local/nginx/conf/nginx.conf #去掉nginx配置文件注释
```



```shell
vim /usr/local/nginx/conf/nginx.conf

worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    upstream tomcat{
        server 192.168.107.200:8080 weight=1;
        server 192.168.107.201:8080 weight=1;
    }
    server {
        listen       80;
        server_name  localhost;
        location / {
            proxy_http_version  1.1; #使用http1.1版本
            proxy_pass http://tomcat; 
            proxy_set_header Host $host; #负载均衡以后继续传递host字段	
            proxy_set_header X-Real-IP $remote_addr; #传递真是ip
        }
    }
}
```



```shell
/usr/local/nginx/sbin/nginx -t
/usr/local/nginx/sbin/nginx #启动nginx
/usr/local/nginx/sbin/nginx -c /path/to/nginx.conf #启动nginx并且指定配置文件
/usr/local/nginx/sbin/nginx -s stop
/usr/local/nginx/sbin/nginx -s reload
tail -f /app/tomcat/logs/blog.liyedong.com_access_log.2023-08-16.txt #实时查看日志文件，观察负载均衡
```



```plain
#解决访问日志源ip丢失问题
vim /app/tomcat/conf/server.xml
  pattern="#%{X-Real-IP}i %l %u %t &quot;%r&quot; %s %b" />
#  %{X-Real-IP}i  请求头的X-Real-IP字段
#  %{xxx}i 请求头的
#  %{xxx}o 响应头的
/app/tomcat/bin/shutdown.sh
/app/tomcat/bin/startup.sh
```



## 10.tomcat+nfs实现文件共享


```shell
#lb01安装nfs
yum install nfs-utils.x86_64 -y
mkdir /data
vim /etc/exports
/data 192.168.107.0/24(rw,sync,no_root_squash,no_all_squash)
systemctl restart nfs
systemctl enable nfs

#tomcat01和tomcat02
yum install nfs-utils -y
showmount -e 192.168.107.202
mkdir /html/ROOT/attached
mount -t nfs 192.168.107.202:/data /html/ROOT/attached
```



## 11.nginx缓存


```nginx
mkdir /opt/nginx/cache -p
useradd nginx;
chown -R nginx:nginx /opt/nginx/cache                        #对缓存文件进行提权
chown -R nginx:nginx /usr/local/nginx/proxy_temp/     #将nginx临时文件目录授权给nginx用户

user nginx;
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    proxy_cache_path /opt/nginx/cache levels=1:2 keys_zone=one:10m;#levels=1:2使用二级目录缓存
    upstream tomcat{
        server 192.168.107.200:8080 weight=1;
        server 192.168.107.201:8080 weight=1;
    }
    server {
        listen       80;
        server_name  localhost;
        location / {
            proxy_pass http://tomcat;
            proxy_http_version  1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
        location ~ .*\.(gif|jpg|png|css|js|woff|flv|ico|swf)(.*) {
          proxy_cache one;
          proxy_cache_key $uri;
          proxy_cache_valid 200 302 1h;
          proxy_cache_valid 301 1d;
          proxy_cache_valid any 1m;
          expires 30d;
          add_header     Nginx-Cache   "$upstream_cache_status";
          proxy_pass http://tomcat;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```



### 缓冲区权限不足错误


因为使用缓存的前提是需要开启缓冲区，上述配置文件中，没有进行缓冲区配置，因为默认缓冲区配置是开启的，如果要读写，需将权限赋给nginx用户。



如果出现一下错误，是因为nginx用户没有权限读取"/usr/local/nginx/proxy_temp/9/20/0000000209"下的文件，需要使用



```shell
chown -R nginx:nginx /usr/local/nginx/proxy_temp/ #对缓冲区文件夹提权
```



```plain
2023/08/17 09:17:46 [crit] 75841#0: *444 open() "/usr/local/nginx/proxy_temp/9/20/0000000209" failed (13: Permission denied) while reading upstream, client: 192.168.107.1, server: localhost, request: "GET /favicon.ico?t=1624781874000 HTTP/1.1", upstream: "http://192.168.107.201:8080/favicon.ico?t=1624781874000", host: "blog.liyedong.com", referrer: "http://blog.liyedong.com/"
```



## 12.Nginx+Tomcat集群实现全栈Https


```nginx
[root@lb01 ~]# cat /etc/nginx/nginx.conf
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    #proxy_cache_path /opt/nginx/cache levels=1:2 keys_zone=one:10m;
    proxy_cache_path /opt/nginx/cache  keys_zone=one:10m;
    upstream tomcat {
      server 10.0.0.11:8080;
      server 10.0.0.12:8080;
    }
    
server {
    listen 443 ssl; 
    server_name blog.oldqiang.com; 
    ssl_certificate /opt/Nginx/1_blog.oldqiang.com_bundle.crt; 
    ssl_certificate_key /opt/Nginx/2_blog.oldqiang.com.key; 
    ssl_session_timeout 5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; 
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; 
    ssl_prefer_server_ciphers on;
    location / {
          proxy_pass http://tomcat;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
    }
    location  ~   ^.*\.(js|css|ico|gif|jpg|jpeg|png)$  {
          proxy_cache one;
          proxy_cache_key $uri;
          add_header     Nginx-Cache   "$upstream_cache_status";
          proxy_cache_valid 200 304 1h;
          proxy_cache_valid 404 1m;
          proxy_pass http://tomcat;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
        }
}
    server {
        listen       80;
        server_name  localhost;
        location / {
             return       302 https://blog.oldqiang.com$request_uri;
        }
    }
}
```



## 13.使用maven编译java程序


```shell
#安装配置maven
wget --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.8.8/binaries/apache-maven-3.8.8-bin.tar.gz


tar xf apache-maven-3.8.8-bin.tar.gz -C /usr/local/
ln -s /usr/local/apache-maven-3.8.8 /usr/local/maven
#文件结尾添加两行
sed -i '$a export M2_HOME=/usr/local/maven\nexport PATH=${M2_HOME}/bin:$PATH' /etc/profile
source /etc/profile
#验证
mvn -v

#配置maven仓库
vim /usr/local/maven/conf/settings.xml
<mirror>
    <id>aliyunmaven</id>
    <mirrorOf>*</mirrorOf>
    <name>阿里云公共仓库</name>
    <url>https://maven.aliyun.com/repository/public</url>
</mirror>

#清理并打包
mvn clean package


#lb01
vim /usr/local/nginx/conf/nginx.conf
server {
    listen       80;
    server_name  jeesns.liyedong.com;
    location / {
    proxy_http_version  1.1; #使用http1.1版本
    proxy_pass http://tomcat;
    proxy_set_header Host $host; #负载均衡以后继续传递host字段
    proxy_set_header X-Real-IP $remote_addr; #传递真是ip
}
}
/usr/local/nginx/sbin/nginx -t
/usr/local/nginx/sbin/nginx -s reload

scp /app/tomcat/conf/server.xml root@192.168.107.201:/app/tomcat//conf/server.xml
scp /jobjeesns/ROOT.war root@192.168.107.201:/jobjeesns/ROOT.war
```



## 14.使用redis实现session共享


```shell
vim /app/tomcat/conf/context.xml
<Manager className="org.redisson.tomcat.RedissonSessionManager"
configPath="${catalina.base}/conf/redisson.conf" readMode="MEMORY" updateMode="DEFAULT"/>
vim  /app/tomcat/conf/redisson.conf
{
   "singleServerConfig":{
      "idleConnectionTimeout":10000,
      "connectTimeout":10000,
      "timeout":3000,
      "retryAttempts":3,
      "retryInterval":1500,
      "password":null,
      "subscriptionsPerConnection":5,
      "clientName":null,
      "address": "redis://192.168.107.202:6379",
      "subscriptionConnectionMinimumIdleSize":1,
      "subscriptionConnectionPoolSize":50,
      "connectionMinimumIdleSize":32,
      "connectionPoolSize":64,
      "database":0,
      "dnsMonitoringInterval":5000
   },
   "threads":0,
   "nettyThreads":0,
   "codec":{
      "class":"org.redisson.codec.JsonJacksonCodec"
   },
   "transportMode":"NIO"
}

#准备两个jar包
#下载https://github.com/redisson/redisson/tree/master/redisson-tomcat
/app/tomcat/lib/redisson-all-3.14.0.jar
/app/tomcat/lib/redisson-tomcat-8-3.14.0.jar

#重启tomcat生效


#推送到tomcat02
scp -rp /app/tomcat/conf/context.xml root@192.168.107.201:/app/tomcat/conf/context.xml
scp -rp /app/tomcat/lib/redisson-all-3.14.0.jar /app/tomcat/lib/redisson-tomcat-8-3.14.0.jar root@192.168.107.201:/app/tomcat/lib
#重启tomcat生效
```



```shell
#lb01
yum install epel-release -y
yum install redis -y
systemctl start redis
systemctl enable redis
vim /etc/redis.conf
	bind 192.168.107.202 127.0.0.1
systemctl restart redis
```



## 15.Tomcat监控


```shell
vi /app/tomcat/bin/catalina.sh						#在开头添加以下配置
	CATALINA_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=12345 -Djava.rmi.server.hostname=192.168.107.200"


a：安装zabbix-java-gateway，10052
b：配置重启zabbix-java-gateway
	LISTEN_IP="0.0.0.0"											#监控地址（默认地址）					
	LISTEN_PORT=10052											#监听端口
	PID_FILE="/var/run/zabbix/zabbix_java.pid"					#进程文件路径
	START_POLLERS=5												#开启的工作进程数
c：配置重启zabbix-server
	...
	JavaGateway=127.0.0.1										#JavaGateway的地址（本机安装可使用127.0.0.1）
	JavaGatewayPort=10052										#JavaGateway的端口号					
	StartJavaPollers=5											#开启的进程数量（大于客户端的数量）
d：zabbix-web添加jmx监控
```

