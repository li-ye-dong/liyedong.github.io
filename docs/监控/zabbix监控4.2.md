# zabbix监控
## 1.zabbix-server安装
```shell
yum install epel-release -y
getenforce 
sed -i 's/SELINUX=.*/SELINUX=disables/' /etc/selinux/config && setenforce 0
systemctl stop firewalld && systemctl disable firewalld
wget https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
rpm -ivh zabbix-release-4.0-1.el7.noarch.rpm
yum install mariadb-server mariadb zabbix-server-mysql zabbix-web-mysql -y
systemctl start mariadb && systemctl enable mariadb
mysql_secure_installation
#全选y password设置为root
mysql -u root -p
create database zabbix character set utf8 collate utf8_bin;
grant all privileges on zabbix.* to zabbix@localhost identified by 'zabbix';
#导入zabbix数据库
zcat /usr/share/doc./zabbix-server-mysql-4.0.47/create.sql.gz | mysql -uzabbix -p zabbix
vi /etc./zabbix./zabbix_server.conf
    DBPassword=zabbix
vi /etc/httpd/conf.d./zabbix.conf
     #第20行
     php_value date.timezone Asia/Shanghai
systemctl start zabbix-server httpd && systemctl enable zabbix-server httpd
```

![](../images/1709986856653-f52bb8c1-6a72-4429-87bb-a715f237994f.png)



![](../images/1709986863762-98cadec4-8a14-43ef-9624-cd1457857f12.png)



![](../images/1709986870007-f70a87bf-4490-44b2-a684-1651b69f51b0.png)

![](../images/1709986875337-0e85f816-7e07-473f-8a96-4e148f78f824.png)



![](../images/1709986879709-5449e366-1b83-455f-b127-1a47ebdbe172.png)

![](../images/1709986884261-021f9120-a6cc-4581-a147-5c21500c5374.png)

![](../images/1709986890626-ea3fdb17-4dd4-4a68-b5d7-cd503ad781fa.png)







## 2.zabbix-agent安装
```shell
yum install zabbix-agent -y
systemctl start zabbix-agent && systemctl enable zabbix-agent
```

![](../images/1709986902543-c295fd06-0d1f-4fc4-b405-fce775a2548b.png)

![](../images/1709986906858-df92e19c-6265-4dc6-b3e8-5cde047e0325.png)







## 3.中文设置
![](../images/1709986911095-43a1a226-a4cd-47fb-bb3d-a3a9ca17ff2a.png)

![](../images/1709986915519-8a19209c-98c8-4fcb-ae9f-3922cd3c581c.png)



## 4.中文乱码
```plain
使用windows电脑
win+r输入fonts
复制一个文件到服务器中
```



```shell
#修改为ttf格式
mv simsun.ttc simsun.ttf
mv simsun.ttf /usr/share./zabbix/assets/fonts/simsun.ttf
vim /usr/share./zabbix/include/defines.inc.php
    define('ZBX_GRAPH_FONT_NAME','simsun'); // font file name
#刷新网页
```

![](../images/1709986921828-49bd1ab4-4fc6-447b-8b21-91610adc5423.png)





## 5.zabbix-agent节点安装
```shell
wget http://repo.zabbix.com./zabbix/4.0/rhel/7/x86_64./zabbix-agent-4.0.47-1.el7.x86_64.rpm
rpm -ivh zabbix-agent-4.0.47-1.el7.x86_64.rpm
sed -i 's/SELINUX=.*/SELINUX=disables/' /etc/selinux/config && setenforce 0
vim /etc/zabbix/zabbix_agentd.conf
    Server=192.168.107.199
    ServerActive=192.168.107.199
    Hostname=Tomcat01
vim /etc/zabbix/zabbix_agentd.conf
    Server=192.168.107.199
    ServerActive=192.168.107.199
    Hostname=Tomcat02
vim /etc/zabbix/zabbix_agentd.conf
    Server=192.168.107.199
    ServerActive=192.168.107.199
    Hostname=lb01
systemctl restart zabbix-agent
```



## 6.监控tomcat
```shell
添加zabbix存储库

rpm -ivh https://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm
安装zabbix-java-getway （如果没有jdk，请先安装jdk）
yum -y install zabbix-java-gateway
修改配置文件（默认端口是10052，可根据服务器情况调整）

vim /etc/zabbix/zabbix_java_gateway.conf
启动zabbix-java-getway

systemctl start zabbix-java-gateway.service
开机启动

systemctl enable zabbix-java-gateway
查看java进程中是否有zabbix-java-getway的端口

netstat -lntp|grep java

vi /etc/zabbix/zabbix_java_gateway.conf 						#将以下内容取消注释并修改为如下
    ...
    LISTEN_IP="0.0.0.0"											#监控地址（默认地址）					
    LISTEN_PORT=10052											#监听端口
    PID_FILE="/var/run/zabbix/zabbix_java.pid"					#进程文件路径
    START_POLLERS=5												#开启的工作进程数
    ...
vi /etc/zabbix/zabbix_server.conf								#将以下内容取消注释并修改为如下(默认的情况下，zabbix server未启用javaPollers)
    ...
    JavaGateway=127.0.0.1										#JavaGateway的地址（本机安装可使用127.0.0.1）
    JavaGatewayPort=10052										#JavaGateway的端口号					
    StartJavaPollers=5											#开启的进程数量（大于客户端的数量）
    ...
systemctl restart zabbix-java-gateway
systemctl restart zabbix-server
```



```shell
vi /app/tomcat/bin/catalina.sh #在开头添加以下配置
CATALINA_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=12345 -Djava.rmi.server.hostname=192.168.107.200"
#-Djava.rmi.server.hostname=192.168.107.200 为tomcat所在主机ip
/app/tomcat/bin/shutdown.sh
/app/tomcat/bin/startup.sh
```

![](../images/1709986970358-2e96cd78-629d-4f17-ac1d-7f713b88d3d7.png)



![](../images/1709986975836-e3ad0433-c148-4117-8e12-b099b7070ee1.png)

![](../images/1709986985216-591ed25d-3779-4d83-96f6-bcd1116adc61.png)







### 开启tomcat的gzip功能
![](../images/1709986990432-45e9236e-53e7-45d7-9903-e973b04245d2.png)



```xml
vi /app/tomcat/conf/server.xml

在Connector节点中加上如下属性
compression=“on” 打开压缩功能
compressionMinSize=“50” 启用压缩的输出内容大小，默认为2KB
noCompressionUserAgents=“gozilla, traviata” 对于以下的浏览器，不启用压缩
compressableMimeType=“text/html,text/xml,text/javascript,text/css,text/plain”　哪些资源类型需要压缩




    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443"
               maxParameterCount="1000"
               compression="on"
               compressionMinSize="2048"
               noCompressionUserAgents="gozilla, traviata"
               compressableMimeType="text/html,text/xml,text/javascript,application/javascript,text/css,text/plain,text/json"
               />




 /app/tomcat/bin/shutdown.sh

 /app/tomcat/bin/startup.sh
```



## 7.监控nginx
### 配置nginx的stub_status模块
```shell
yum安装的nginx添加模块
/usr/local/nginx -V
cp -r /usr/local/nginx /usr/local/nginx_bak
wget http://nginx.org/download/nginx-1.24.0.tar.gz
tar -xzvf nginx-1.24.0.tar.gz -C /usr/local/
./configure --with-http_stub_status_module --prefix=/usr/local/nginx
make
make install
cp -rn /usr/local/nginx /usr/local/nginx_bak#复制新编译的文件到nginx目录下
mv /usr/local/nginx /usr/local/nginx_bak2
mv /usr/local/nginx_bak /usr/local/nginx#重命名nginx
[root@master local]# /usr/local/nginx/sbin/nginx -V
nginx version: nginx/1.24.0
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-44) (GCC)
configure arguments: --with-http_stub_status_module --prefix=/usr/local/nginx

/usr/local/nginx/sbin/nginx


vi /usr/local/nginx/conf/nginx.conf
```



```nginx
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    proxy_cache_path /opt/nginx/cache levels=1:2 keys_zone=one:10m;
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

        location /status {        #加上这个location模块
            stub_status on;
            access_log off;
            allow 127.0.0.1;
            allow 192.168.107.0/24;
            deny all;
        }
    }
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
}
```



```shell
/usr/local/nginx/sbin/nginx -s reload
curl localhost/status
            Active connections: 3
            server accepts handled requests
             10 10 12
            Reading: 0 Writing: 1 Waiting: 2
```



### 配置zabbix监控
```shell
vi /etc/zabbix/zabbix_agentd.d/nginx_status.conf 
UserParameter=Nginx.Active.Connections,/usr/bin/curl -s localhost/status 2>/dev/null |grep 'Active connections:'|awk '{print $NF}'
#在zabbix-server端
yum install zabbix-get -y
[root@master ~]# zabbix_get -s 192.168.107.202 -p 10050 -k "Nginx.Active.Connections"
1 #取值成功
```

![](../images/1709987003231-ff3a6d93-4d44-4a95-9cf5-17a23b9f0889.png)

![](../images/1709987353651-6d31707f-4708-44b2-84f9-93d8cfd8d94a.png)



![](../images/1709987360370-c6fa823d-5d7a-4df4-bb24-77f5e3a4fcec.png)



```shell
#监控Nginx活动连接数
UserParameter=Nginx.Active.Connections,/usr/bin/curl -s localhost/status 2>/dev/null |grep 'Active connections:'|awk '{print $NF}'
#监控Nginx总共处理的连接数
UserParameter=Nginx.Accepts.Connections,/usr/bin/curl -s localhost/status 2>/dev/null|sed -n '3p'|awk '{print $1}'
#监控Nginx成功创建的握手次数
UserParameter=Nginx.Handled.Connections,/usr/bin/curl -s localhost/status 2>/dev/null|sed -n '3p'|awk '{print $2}'
#监控Nginx总共处理的请求次数
UserParameter=Nginx.requests.Connections,/usr/bin/curl -s  localhost/status 2>/dev/null|sed -n '3p'|awk '{print $3}'
#Nginx读取到客户端的连接数
UserParameter=Nginx.Reading,/usr/bin/curl -s  localhost/status 2>/dev/null|sed -n '4p'|awk '{print $2}'
#Nginx响应数据到客户端的数量
UserParameter=Nginx.Writing,/usr/bin/curl -s localhost/status 2>/dev/null|sed -n '4p'|awk '{print $4}'
#Nginx处理完并等候状态的驻留连接
UserParameter=Nginx.Waiting,/usr/bin/curl -s localhost/status 2>/dev/null|sed -n '4p'|awk '{print $6}'
```

![](../images/1709987369350-252f260b-a904-48cb-95db-16f50c8fc84f.png)



![](../images/1709987376757-eadf13ce-77c5-494f-8fb7-f114b06b9488.png)





## 8.监控redis
```shell
关闭selinux
sed -i 's/SELINUX=.*/SELINUX=disables/' /etc/selinux/config && setenforce 0
getenforce 
添加zabbix存储库
rpm -ivh http://repo.zabbix.com/zabbix/4.2/rhel/7/x86_64/zabbix-release-4.2-1.el7.noarch.rpm

yum install zabbix-agent -y
vi /etc/zabbix/zabbix_agentd.conf
    Server=192.168.107.199
    ServerActive=192.168.107.199
    Hostname=Redis01   
    #host为主机名，需要和web界面名称一致   server和serveractive的ip都为zabbix-server端
systemctl start zabbix-agent
systemctl enable zabbix-agent
systemctl start redis
systemctl enable redis
```



```shell
vi /etc/zabbix/zabbix_agentd.d/redis.conf

UserParameter=redis[*],redis-cli -h 127.0.0.1 -p 6379 -a redispwd --no-auth-warning info | grep $1":" | cut -d ':' -f 2
UserParameter=redis-ping,redis-cli -h 127.0.0.1 -p 6379 -a redispwd --no-auth-warning ping | grep -c PONG
UserParameter=redis.version, redis-server --version | cut -d " " -f 3 | cut -d "=" -f 2

systemctl restart zabbix-agent
```



[Template App Redis.xml](https://www.yuque.com/attachments/yuque/0/2024/xml/40598547/1709987456807-9dc342ea-8920-4cc2-ac5c-fccccf42f50c.xml)

![](../images/1709987704435-b360cda8-8c99-4d9f-a6d9-e46961ea44d7.png)

![](../images/1709987714113-b28d4f8e-402e-450c-88f8-07a41205bcc6.png)

![](../images/1709987718878-86c1d50b-acd3-4f9f-86f7-b3c96c93559d.png)

![](../images/1709987723083-07dcd3e0-4de8-45eb-8b70-45953aefaa81.png)











## 9.监控对应服务进程
### zabbix_get获取数据
zabbix监控可以使用默认自带的键值来监控服务进程存活，本文已时间服务器ntp进程为例，监控进程存活，理论适用于所有进程。



使用的键值proc.num[,,,]



格式说明：



:进程名字，默认为“all processes”  
:运行该进程的用户，默认为“all users”  
:进程状态，默认是all，可以进一步设定比如run,sleep等  
:模糊匹配



请确保监控端已安装agent，请将192.168.x.x替换成你自己的客户端地址



1、在服务端执行



由于ntpd服务是通过nginx用户执行的，所以这里运行该进程的用户就填写nginx,进程名字也可以通过模糊搜索进行匹配



```shell
[root@master ~]# zabbix_get -s 192.168.107.202 -k 'proc.num[,nginx,,nginx]'
2
nginx默认一个工作进程，开启缓存再加一个缓存进程，所以有两个
/usr/local/nginx/sbin/nginx -s stop
[root@master ~]# zabbix_get -s 192.168.107.202 -k 'proc.num[,nginx,,nginx]'
0
```

![](../images/1709987753871-7cedf93d-3b25-4077-8b2c-a28d32bfd65d.png)





### 配置触发器
![](../images/1709987766470-dd07c652-8286-4dd5-9dfe-52aa50691126.png)



```shell
/usr/local/nginx/sbin/nginx -s stop
```

![](../images/1709987776052-caa61b6f-f004-4052-a2b3-12ff7ef0792c.png)





```shell
/usr/local/nginx/sbin/nginx
```

![](../images/1709987783065-48fb2dad-0b3f-43a7-9dc1-2dc16a654335.png)





## 10.主动agent和被动agent
### 被动式agent识别
```plain
IP address / DNS name
```



### 主动式agent识别
```plain
明确设置Hostname
没有设置Hostname时使用HostnameItem
默认为system.hostname
```



### Agent配置
```plain
StartAgents设置为0时，禁用被动式agent
注释掉ServerActive时，禁用主动式agent
同时禁用主动和被动模式的时候，agent会报错：
zabbix-agentd[16208]: ERROR: either active or passive checks must be enabled
```



## 12.触发器
### 什么是触发器
```plain
触发器就是用监控项采集的数据来“评估”该监控项状态的逻辑表达式。
触发器表达式通过定义的阈值，和采集的数据进行比较，超出阀值时触发器会被触发。
例如：
CPU负载太高
主机用ICMP不可达
数据库宕机
应用没有运行... ...
```



```plain
触发器的状态：
    OK-一个正常的触发器状态。触发器表达式计算结果为假（False）
    PROBLEM-发生了某些事情，状态异常，比如处理器的负载较高。触发器表达式计算结果为真（True）
    UNKNOWN–通过表达式无法确定触发器的状态，通常是因为错误的数据造成
触发器的计算
    每次Zabbix server接收到作为表达式一部分的监控项的新值时，都会重新计算触发器状态（表达式）
    如果在表达式中使用基于时间的函数(nodata(), date(), dayofmonth(), dayofweek(),time(), now())，触发器就会由Zabbix history syncer进程每30秒重新计算一次
    如果在表达式中同时使用基于时间和非基于时间的函数，当接收到一个新值和每隔30秒都会重新计算触发器的状态
```



## 13.zabbix设置QQ邮箱告警
### 获取授权码
首先在QQ邮箱中，开启POP3/SMTP服务 来获得授权码，QQ邮箱—>设置—>账户—>开启POP3/SMTP服务,获取授权码



```plain
ssssss
```

![](../images/1709987801895-52ba226f-80b3-4748-b483-20a240538491.png)

![](../images/1709987806683-7fce3e7f-c7b9-4623-ae43-ac3db4c51bb1.png)

![](../images/1709987811750-ee31b25f-8357-4654-91e4-8c2dbbb340ac.png)

![](../images/1709987816089-adc87836-e8f5-424d-aba2-660e7ec146ea.png)







### 准备重启脚本
```shell
为zabbix用户分配sudo权限
visudo
zabbix  ALL=(ALL) NOPASSWD: ALL


vi /etc/zabbix/zabbix_agentd.conf
EnableRemoteCommands=1
#Defaults requiretty#这个注释掉
可以更精细化
或者
# visudo 添加：
Defaults:zabbix !requiretty
zabbix ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx



systemctl restart zabbix-agent

zabbix_get -s 192.168.107.202 -k "system.run[sudo /usr/local/nginx/sbin/nginx]"
zabbix_get -s 192.168.107.202 -k "system.run[sudo /usr/local/nginx/sbin/nginx -s stop]"

```

![](../images/1709987994303-644df794-13f5-447d-9f1d-5e39bf59d5ff.png)





### 选择脚本重启时机
![](../images/1709987834561-8cd1d9ab-d89f-42f6-8a5b-3d49910ffeda.png)







![](../images/1709987839473-7a3ae605-072e-4480-b02a-fd954548b671.png)



### 测试脚本和邮箱
```plain
 /usr/local/nginx/sbin/nginx -s stop
```



### 测试邮箱成功
![](../images/1709987864274-583da89e-c7f2-4cf3-8481-59f04659c60b.png)

![](../images/1709987869744-f0ab7d2f-32b6-45c9-995c-67d16a2cd122.png)







### 执行脚本成功，服务恢复
![](../images/1709987874796-161c8382-7d5e-4cbb-8b9d-8d1991ff4fac.png)





## 14.绘制动态拓补图
### 添加主机
![](../images/1709988029608-c00e24df-cb11-4c45-b37b-337814d5aa4f.png)





### 选中两台主机相连，并且添加链接指示器，同时使用宏变量来进行对网卡出入口网速的检测
![](../images/1709988038835-985d744b-7e0d-4466-913a-ab39700335d7.png)





### 停止nginx服务，观察效果
```plain
/usr/local/nginx/sbin/nginx -s stop
```

![](../images/1709988047419-d38d9e45-8850-49b2-85cb-fe832c64e1f9.png)





### 测试成功
![](../images/1709988058727-9e65da66-03f1-4425-a938-22241b37550f.png)





### nginx自动重启脚本成功，告警恢复
![](../images/1709988067265-5b259bee-d50f-4dbb-832b-8bf476e05498.png)





## 15.低级发现规则
![](../images/1709988071907-c3f9ddd5-7707-4e73-b393-3f24b56cbc14.png)

![](../images/1709988079716-96c2536c-2ec1-4987-907d-5d94a58b408e.png)



![](../images/1709988084707-ea73d96a-50de-478b-bb8f-4eb16e1cb416.png)





```plain
#server端进行测试
zabbix_get -s 192.168.107.202 -k vfs.fs.discovery
```



### 添加发现规则监控项原型
![](../images/1709988091967-e9fdd03f-9bd4-4bc1-ba4a-0f72c2ed0857.png)

![](../images/1709988104942-2f6794af-da77-48c8-87f1-1e8d25fd98e6.png)







### 添加触发器原型
![](../images/1709988113263-b14383a5-d01e-4c1f-8330-f410b8cb5add.png)





### 创建图形原型
![](../images/1709988121478-c38c7486-b49d-4f5a-8572-09e714d624f6.png)





### 检测效果
![](../images/1709988126627-6f34abbc-3ec1-4212-b0a1-c7dbf4d4db5e.png)



![](../images/1709988131158-faa70291-f4f9-4f13-ac44-94de56b651ce.png)

![](../images/1709988139721-3cdcae9a-023a-4114-a45a-3440ee97870e.png)



![](../images/1709988143640-7158e485-9638-417d-af13-7d07556664ed.png)







## 16.web场景监控
### 第一页的页面检测
```plain
判断是否具有Zabbix SIA，其他字符串也是可以的
```

![](../images/1709988167071-388f95e8-1904-421c-9af4-002d6acbcea7.png)





### 登录接口
```plain
登录接口的地址为http://192.168.107.199/zabbix/index.php
请求的的数据类型为Formdata
    参数有三个，分别是
    name，password，enter
    Admin，zabbix，Sign in
```

![](../images/1709988185555-80eedbe1-763f-44e6-8cd9-1f3c5f8e080e.png)

![](../images/1709988195252-1e5f81ca-041b-442c-a2cd-168a9ff04609.png)







### 登录接口的检测
```plain
登录成功后根据页面上有的字符串进行判断是否成功，这边选择“监测”这两个字
```

![](../images/1709988210924-585e1f61-3fb4-47e1-809e-dc545602bc34.png)





### 登出接口
```plain
请求地址为http://192.168.107.199.zabbix/index.php
请求数据有两个，类型也有两个
    第一个为query string parameters
    实际上就是使用？跟着请求地址后面作为参数
    另一个就是formdata与登录接口的数据格式一致
检测登出成功，就是返回首页，可以根据登录页的字符串来进行匹配，可以与第一个页面的检测配置一致，这边选择Username字符串作为监测字符串。
```

![](../images/1709988220691-26e723d7-f8ac-4077-a759-9aa3989f9130.png)

![](../images/1709988225395-5d6ff13a-610f-4492-9f72-9f684939309f.png)







### 配置web监测
![](../images/1709988230841-d5da77a7-a317-4aee-be43-6f22e5a4b3dd.png)

![](../images/1709988238363-c4614753-9452-4563-a262-56aaf4ab517c.png)



```plain
配置名称，客户端的请求头，还有变量
```

![](../images/1709988244337-fbd9ceec-edee-4e4e-99e5-3f4ff73f01c4.png)





```plain
配置步骤
```

![](../images/1709988252451-4b71f4c7-18b5-4efd-a44f-24dd8daddf24.png)





### 添加步骤1-页面访问
```plain
根据上面的接口分析，来进行监测，并且设置跟随跳转
```

![](../images/1709988280418-3b1ff6fb-fef3-4412-af6d-fc3e0525250e.png)





### 添加步骤2-登录
```plain
根据对登录接口进行请求，来进行登录
由上面的接口分析得，请求数据为formdata
封装请求数据
根据请求成功返回的html文本流，匹配正则：regex:name="csrf-token" content="([0-9a-z]{16})"
获得sid，退出时需要使用
```



![](../images/1709988290219-ee2bd207-be03-4aa0-b12e-c92cdf3a52c1.png)



### 添加步骤3-登录检测
```plain
根据登录成功后跳转的页面上的字符串来进行判断
```

![](../images/1709988300404-90af4c51-46a5-405d-88f6-d120c221f0b2.png)





### 添加步骤4-登出
```plain
根据登出接口的请求数据来进行数据的封装
```

![](../images/1709988307806-94e3f964-502a-45ab-be7e-ec6ea6c195ef.png)





### 添加步骤5-登出检测
```plain
根据登出后重定向的界面字符串进行匹配，可以跟第一步的字符串一致，这边选择Username这个字符串
```

![](../images/1709988316744-4f3a5e1b-6b66-42dc-a5cf-1d5bd4c7af50.png)





### 查看数据
![](../images/1709988347735-6eb2c7e9-fcde-49ce-bed4-888f1ac5c0b4.png)





## 17.公司门户系统的检测
### 接口分析
```plain
门户首页地址：http://portal.kehua.com/
登录接口地址：http://login.kehua.com:11502/cas/login，参数根据图分析得出
登录检测url：http://portal.kehua.com/web/guest/index
登出url：http://portal.kehua.com/c/portal/logout
登出检测：http://portal.kehua.com/
```

![](../images/1709988354165-ee4606f0-301e-45ac-8418-2ed97a111138.png)

![](../images/1709988359118-96533b79-5374-4cf5-b0fc-53a1e19c9cb4.png)







### 配置
![](../images/1709988363628-6c95f9a1-7674-4b6a-99c8-2bd11ec76376.png)





#### 步骤一
![](../images/1709988382090-21ccb7f1-a75a-4766-adde-a23997899397.png)





#### 步骤二
![](../images/1709988425044-7323ea37-edfa-403b-8c6e-1f8a82d117b8.png)





#### 步骤三
![](../images/1709988434013-dbe0c300-5394-4afb-a9a5-4202669c51cf.png)





#### 步骤四
![](../images/1709988442165-81f7586e-f949-4fd4-9f15-0a5f5a436e75.png)





#### 步骤五
![](../images/1709988453018-57758a32-175a-4a8a-856f-1385d3ae1aed.png)





### 结果查看
![](../images/1709988459785-fbaee9c3-6b31-4042-adb9-fcb35e17d8ce.png)





## 18.配置zabbix proxy
### zabbix-proxy端
```shell
yum install epel-release -y
getenforce 
sed -i 's/SELINUX=.*/SELINUX=disables/' /etc/selinux/config && setenforce 0
systemctl stop firewalld && systemctl disable firewalld
yum install wget -y
wget --no-check-certificate https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-release-4.0-1.el7.noarch.rpm
rpm -ivh zabbix-release-4.0-1.el7.noarch.rpm
yum install fping -y
yum install OpenIPMI-libs.x86_64 -y
yum install OpenIPMI-modalias.x86_64 -y
yum install zabbix-proxy-mysql -y
yum install mariadb-server -y
systemctl start mariadb.service
systemctl enable mariadb.service
mysql_secure_installation #安全初始化
mysql
create database zabbix_proxy character set utf8;    #创建zabbix_proxy数据库
grant all on zabbix_proxy.* to zabbix@localhost identified by 'zabbix'; #授予zabbix用户本地密码登录的权限
flush privileges;  #刷新权限
gunzip /usr/share/doc/zabbix-proxy-mysql-4.0.48/schema.sql.gz

mysql -uzabbix -pzabbix zabbix_proxy < /usr/share/doc/zabbix-proxy-mysql-4.0.48/schema.sql
vi /etc/zabbix/zabbix_proxy.conf
```



```shell
Server=192.168.107.199    zabbix服务端的IP
ServerPort=10051       默认配置
Hostname=Zabbix-proxy   代理的名字，服务端的代理名字要和这里保持一致
LogFile=               日志目录默认
LogFileSize=0          指定日志输出级别默认
DBHost=localhost       数据库IP，如果在同一台机器就填localhost可以
DBName=zabbix_proxy    数据库名
DBUser=zabbix          数据库用户名
DBPassword=zabbix             数据库密码
DBSocket=/tmp/mariadb.sock  socket文件
DBPort=3306            数据库连接端口
DataSenderFrequency=5  与zabbix服务端同步数据的时间间隔，这里设置为5秒
```



```shell
#当agent端重启完后，代理端再重启，否则无法识别agent端的主机名
systemctl restart zabbix-proxy
```



### zabbix-agent端
```plain
 vi /etc/zabbix/zabbix_agentd.conf
```



```shell
Server=192.168.107.198         #zabbix-proxy端IP
ServerActive=192.168.107.198         # zabbix-proxy端IP
Hostname=zabbix-proxy                # 主机名，server的主机名要与这里配置一致
```



```shell
systemctl restart zabbix-agent
```



### zabbix-server
![](../images/1709988476438-01896f1c-6207-4455-b7ec-53aed0fcc479.png)

![](../images/1709988483948-c1a57a4c-1df5-4638-9f19-01fdec58b9ac.png)



![](../images/1709988495988-6332f2d4-97d2-4352-bf3f-4c04bdb33a45.png)

