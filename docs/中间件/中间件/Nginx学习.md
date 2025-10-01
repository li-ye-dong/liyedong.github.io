## 1.Tengine介绍
由淘宝对Nginx进行二次开发的一个分支服务器，一般用在高并发长场景



官网



```html
https://tengine.taobao.org/
```



## 2.安装Nginx
### A.yum源安装
```shell
vi /etc/yum.repos.d/nginx.repo #配置nginx较新版本yum源
    [nginx]
    name=nginx repo
    baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
    gpgcheck=0
    enabled=1
#或者下载拓展源epel-release，版本较旧 
#yum install epel-release -y
yum list | grep nginx
yum install nginx -y
whereis nginx
```



### B.源码安装
```shell
yum intall wget
wget url
tar xf xxx.gz -C /usr/local
cd /usr/local/nginx-1.2.5
./configure --prefix=/usr/local/nginx
#缺少pcre  yum install pcre-devel
#缺少zlib    yum install zlib-devel
make #编译
make install #安装
```



### C.查看Nginx进程
```shell
netstat -lnp|grep 80 #查看80端口占用情况
ps -ef|grep nginx #查看nginx进程
```



## 3.Nginx配置文件详解
```shell
[root@master nginx]# ll
总用量 4
drwxr-xr-x. 2 root root 4096 8月  21 10:21 conf #配置文件目录
drwxr-xr-x. 2 root root   40 8月  21 09:40 html #html目录
drwxr-xr-x. 2 root root    6 8月  21 09:40 logs #日志
drwxr-xr-x. 2 root root   19 8月  21 09:40 sbin #启动脚本
```



### A.nginx.conf全局配置
```shell
user nobody;
#定义运行nginx服务的用户,还可以加上组,如 user nobody nobody;
worker_processes 1;
#定义nginx子进程数量，即提供服务的进程数量，该数值建议和服务cpu核数保持一致。
#除了可以定义数字外，还可以定义为auto，表示让系统自动调整。
error_log logs/error.log;
#定义错误日志的路径，可以是相对路径（相对prefix路径的），也可以是绝对路径。
#该配置可以在此处定义，也可以定义到http、server、location里
error_log logs/error.log notice;
#定义错误日志路径以及日志级别.
##错误日志级别：常见的错误日志级别有[debug|info|notice|warn|error|crit|alert|emerg]，级别越高记录的信息越少。
#如果不定义默认是error
pid logs/nginx.pid;
#定义nginx进程pid文件所在路径，可以是相对路径，也可以是绝对路径。
worker_rlimit_nofile 100000;
#定义nginx最多打开文件数限制。如果没设置的话，这个值为操作系统（ulimit -n）的限制保持一致。
#把这个值设高，nginx就不会有“too many open files”问题了。
```



### B.events配置项结构
```shell
events配置部分
worker_connections 1024;
#定义每个work_process同时开启的最大连接数，即允许最多只能有这么多连接。
accept_mutex on;
#当某一个时刻只有一个网络连接请求服务器时，服务器上有多个睡眠的进程会被同时叫醒，这样会损耗一定的服务器性能。
#Nginx中的accept_mutex设置为on，将会对多个Nginx进程（worker processer）接收连接时进行序列化，防止多个进程争抢资源。
#默认就是on。
multi_accept on;
#nginx worker processer可以做到同时接收多个新到达的网络连接，前提是把该参数设置为on。
#默认为off，即每个worker process一次只能接收一个新到达的网络连接。
use epoll;
#Nginx服务器提供了多个事件驱动器模型来处理网络消息。
#其支持的类型有：select、poll、kqueue、epoll、rtsing、/dev/poll以及eventport。

#select：只能在Windows下使用，这个事件模型不建议在高负载的系统使用

#poll:Nginx默认首选，但不是在所有系统下都可用

#kqueue:这种方式在FreeBSD 4.1+, OpenBSD2.9+, NetBSD 2.0, 和 MacOS X系统中是最高效的

#epoll: 这种方式是在Linux 2.6+内核中最高效的方式

#rtsig:实时信号，可用在Linux 2.2.19的内核中，但不适用在高流量的系统中

#/dev/poll: Solaris 7 11/99+,HP/UX 11.22+, IRIX 6.5.15+, and Tru64 UNIX 5.1A+操作系统最高效的方式

#eventport: Solaris 10最高效的方式
```



### C.http配置项
```nginx
MIME-Type
include       mime.types;  //cat conf/mime.types
#定义nginx能识别的网络资源媒体类型（如，文本、html、js、css、流媒体等）

default_type  application/octet-stream;
#定义默认的type，如果不定义该项，默认为text/plain.
log_format
log_format main  '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';

#其中main为日志格式的名字，后面的为nginx的内部变量组成的一串字符串。
access_log logs/access.log main;
#定义日志的路径以及采用的日志格式，该参数可以在server配置块中定义。
sendfile on;
#是否调用sendfile函数传输文件，默认为off，使用sendfile函数传输，可以减少user mode和kernel mode的切换，从而提升服务器性能。
#对于普通应用设为 on，如果用来进行下载等应用磁盘IO重负载应用，可设置为off，以平衡磁盘与网络I/O处理速度，降低系统的负载。
sendfile_max_chunk 128k;
#该参数限定Nginx worker process每次调用sendfile()函数传输数据的最大值，默认值为0，如果设置为0则无限制。
tcp_nopush on;
#当tcp_nopush设置为on时，会调用tcp_cork方法进行数据传输。
#使用该方法会产生这样的效果：当应用程序产生数据时，内核不会立马封装包，而是当数据量积累到一定量时才会封装，然后传输。这样有助于解决网络堵塞问题。
#默认值为on。举例：快递员收快递、发快递，包裹累积到一定量才会发，节省运输成本。
keepalive_timeout 65 60;
#该参数有两个值，第一个值设置nginx服务器与客户端会话结束后仍旧保持连接的最长时间，单位是秒，默认为75s。
#第二个值可以省略，它是针对客户端的浏览器来设置的，可以通过curl -I看到header信息中有一项Keep-Alive: timeout=60，如果不设置就没有这一项。
#第二个数值设置后，浏览器就会根据这个数值决定何时主动关闭连接，Nginx服务器就不操心了。但有的浏览器并不认可该参数。
send_timeout
#这个超时时间是发送响应的超时时间，即Nginx服务器向客户端发送了数据包，但客户端一直没有去接收这个数据包。
#如果某个连接超过send_timeout定义的超时时间，那么Nginx将会关闭这个连接。
client_max_body_size 10m;
#浏览器在发送含有较大HTTP包体的请求时，其头部会有一个Content-Length字段，client_max_body_size是用来限制Content-Length所示值的大小的。
#这个限制包体的配置不用等Nginx接收完所有的HTTP包体，就可以告诉用户请求过大不被接受。会返回413状态码。
#例如，用户试图上传一个1GB的文件，Nginx在收完包头后，发现Content-Length超过client_max_body_size定义的值，
#就直接发送413(Request Entity Too Large)响应给客户端。
gzip on；
#是否开启gzip压缩。
gzip_min_length 1k;
#设置允许压缩的页面最小字节数，页面字节数从header头得content-length中进行获取。默认值是20。建议设置成大于1k的字节数，小于1k可能会越压越大。
gzip_buffers 4 16k;
#设置系统获取几个单位的buffer用于存储gzip的压缩结果数据流。4 16k代表分配4个16k的buffer。
gzip_http_version 1.1;
#用于识别 http 协议的版本，早期的浏览器不支持 Gzip 压缩，用户会看到乱码，所以为了支持前期版本加上了这个选项。
#如果你用了Nginx反向代理并期望也启用Gzip压缩的话，由于末端通信是http/1.1，故请设置为 1.1。
gzip_comp_level 6;
#gzip压缩比，1压缩比最小处理速度最快，9压缩比最大但处理速度最慢(传输快但比较消耗cpu)
gzip_types mime-type ... ;
#匹配mime类型进行压缩，无论是否指定,”text/html”类型总是会被压缩的。
#在conf/mime.conf里查看对应的type。

#示例：gzip_types       text/plain application/x-javascript text/css text/html application/xml;
gzip_proxied any;
#Nginx作为反向代理的时候启用，决定开启或者关闭后端服务器返回的结果是否压缩，匹配的前提是后端服务器必须要返回包含”Via”的 header头。

#以下为可用的值：
#off - 关闭所有的代理结果数据的压缩
#expired - 启用压缩，如果header头中包含 "Expires" 头信息
#no-cache - 启用压缩，如果header头中包含 "Cache-Control:no-cache" 头信息
#no-store - 启用压缩，如果header头中包含 "Cache-Control:no-store" 头信息
#private - 启用压缩，如果header头中包含 "Cache-Control:private" 头信息
#no_last_modified - 启用压缩,如果header头中不包含 "Last-Modified" 头信息
#no_etag - 启用压缩 ,如果header头中不包含 "ETag" 头信息
#auth - 启用压缩 , 如果header头中包含 "Authorization" 头信息
#any - 无条件启用压缩
#gzip_vary on；
#和http头有关系，会在响应头加个 Vary: Accept-Encoding ，可以让前端的缓存服务器缓存经过gzip压缩的页面，例如，用Squid缓存经过Nginx压缩的数据。
```



### D.server配置项
```nginx
   server {
    listen       80;  //监听端口为80，可以自定义其他端口，也可以加上IP地址，如，listen 127.0.0.1:8080;
    server_name  localhost; //定义网站域名，可以写多个，用空格分隔。
    #charset koi8-r; //定义网站的字符集，一般不设置，而是在网页代码中设置。
    #access_log  logs/host.access.log  main; //定义访问日志，可以针对每一个server（即每一个站点）设置它们自己的访问日志。

    ##在server{}里有很多location配置段
    location / {
        root   html;  //定义网站根目录，目录可以是相对路径也可以是绝对路径。
        index  index.html index.htm; //定义站点的默认页。
    }

    #error_page  404              /404.html;  //定义404页面

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;  //当状态码为500、502、503、504时，则访问50x.html
    location = /50x.html {
        root   html;  //定义50x.html所在路径
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #定义访问php脚本时，将会执行本location{}部分指令
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;  //proxy_pass后面指定要访问的url链接，用proxy_pass实现代理。
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;  //定义FastCGI服务器监听端口与地址，支持两种形式，1 IP:Port， 2 unix:/path/to/sockt
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;  //定义SCRIPT_FILENAME变量，后面的路径/scripts为上面的root指定的目录
    #    include        fastcgi_params; //引用prefix/conf/fastcgi_params文件，该文件定义了fastcgi相关的变量
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    # 
    #location ~ /\.ht {   //访问的url中，以/.ht开头的，如，www.example.com/.htaccess，会被拒绝，返回403状态码。
    #    deny  all;  //这里的all指的是所有的请求。
    #}
}


# another virtual host using mix of IP-, name-, and port-based configuration
#
#server {
#    listen       8000;  //监听8000端口
#    listen       somename:8080;  //指定ip:port
#    server_name  somename  alias  another.alias;  //指定多个server_name

#    location / {
#        root   html;
#        index  index.html index.htm;
#    }
#}


# HTTPS server
#
#server {
#    listen       443 ssl;  //监听443端口，即ssl
#    server_name  localhost;

### 以下为ssl相关配置
#    ssl_certificate      cert.pem;    //指定pem文件路径
#    ssl_certificate_key  cert.key;  //指定key文件路径

#    ssl_session_cache    shared:SSL:1m;  //指定session cache大小
#    ssl_session_timeout  5m;  //指定session超时时间
#    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;   //指定ssl协议
#    ssl_ciphers  HIGH:!aNULL:!MD5;  //指定ssl算法
#    ssl_prefer_server_ciphers  on;  //优先采取服务器算法
#    location / {
#        root   html;
#        index  index.html index.htm;
#    }
#}
```



### E.范例
```nginx
user nobody; # 定义运行nginx服务的用户,还可以加上组,如 user nobody nobody

worker_processes  8; #开启8个工作进程
worker_cpu_affinity 00000001 00000010 00000100 00001000 00010000 00100000 01000000 10000000; #将8个工作进程固定在8个cpu上

#以下为4核CPU的范例
#worker_processes  4;
#worker_cpu_affinity 0001 0010 0100 1000;

error_log logs/error.log crit; #定义错误日志的路径和级别。错误日志级别：常见的错误日志级别有[debug|info|notice|warn|error|crit|alert|emerg]，级别越高记录的信息越少。

pid logs/nginx.pid; #定义nginx进程pid文件所在路径，可以是相对路径，也可以是绝对路径。

worker_rlimit_nofile 1024000; #定义nginx最多打开文件数限制。如果没设置的话，这个值为操作系统（ulimit -n）的限制保持一致。

events {

    use epoll; #Nginx服务器提供了多个事件驱动器模型来处理网络消息。epol这种方式是在Linux 2.6+内核中最高效的方式
    worker_connections  65535; #定义每个work_process同时开启的最大连接数，即允许最多只能有这么多连接。
    accept_mutex on; #当某一个时刻只有一个网络连接请求服务器时，服务器上有多个睡眠的进程会被同时叫醒，这样会损耗一定的服务器性能。Nginx中的accept_mutex设置为on，将会对多个Nginx进程（worker processer）接收连接时进行序列化，防止多个进程争抢资源。
    multi_accept on; #nginx worker processer可以做到同时接收多个新到达的网络连接，前提是把该参数设置为on。默认为off，即每个worker process一次只能接收一个新到达的网络连接。
} 

http {
    include        /etc/nginx/mime.types; # 定义nginx能识别的网络资源媒体类型（如，文本、html、js、css、流媒体等
    default_type  application/octet-stream; #定义默认的type，如果不定义该项，默认为text/plain.
    client_max_body_size 1024M; #定义允许最大可以上传多大的文件，超过该值就会报413
    log_format main  '$remote_addr $http_x_forwarded_for [$time_local]'
    '$host "$request_uri" $status'
    '"$http_referer" "$http_user_agent"';
    #这里定义日志的格式，其中main为日志格式的名字，后面的为nginx的内部变量组成的一串字符串。
    sendfile        on; #使用内核的FD文件传输功能，可以减少user mode和kernel mode的切换，从而提升服务器性能。
    sendfile_max_chunk 128k; #该参数限定Nginx worker process每次调用sendfile()函数传输数据的最大值，默认值为0，如果设置为0则无限制。
    tcp_nopush      on; #设置为on时，会调用tcp_cork方法进行数据传输。当应用程序产生数据时，内核不会立马封装包，而是当数据量积累到一定量时才会封装，然后传输。
    tcp_nodelay     on; #不缓存data-sends（关闭 Nagle 算法），这个能够提高高频发送小数据报文的实时性。
    server_tokens   off;#将Nginx版本信息关闭，提升安全性。
    keepalive_timeout 65 60; #该参数有两个值，第一个值设置nginx服务器与客户端会话结束后仍旧保持连接的最长时间，单位是秒，默认为75s。第二个值可以省略，它是针对客户端的浏览器来设置的，可以通过curl -I看到header信息中有一项Keep-Alive: timeout=60，如果不设置就没有这一项。第二个数值设置后，浏览器就会根据这个数值决定何时主动关闭连接，Nginx服务器就不操心了。但有的浏览器并不认可该参数。
    send_timeout 10; #这个超时时间是发送响应的超时时间，即Nginx服务器向客户端发送了数据包，但客户端一直没有去接收这个数据包。如果某个连接超过send_timeout定义的超时时间，那么Nginx将会关闭这个连接。
    client_header_timeout 15; #客户端如果在该指定时间内没有加载完头部数据，则断开连接，单位是秒，默认60，可以设置为15。
    client_body_timeout 120;  #客户端如果在该指定时间内没有加载完body数据，则断开连接，单位是秒，默认60，建议大一点，因为有时候下载大文件时间会比较久。
    client_body_buffer_size 128k; #当客户端以POST方法提交一些数据到服务端时，会先写入到client_body_buffer中，如果buffer写满会写到临时文件里。
    client_header_buffer_size 4k; #客户端请求头部的缓冲区大小，这个可以根据你的系统分页大小来设置，一般一个请求头的大小不会超过1k，不过由于一般系统分页都要大于1k,所以还是要大一些。
    large_client_header_buffers 4 8k; #对于比较大的header（超过client_header_buffer_size）将会使用该部分buffer，两个数值，第一个是个数，第二个是每个buffer的大小。
    open_file_cache max=204800 inactive=20s; #max设定缓存文件的数量，inactive设定经过多长时间文件没被请求后删除缓存。
    open_file_cache_min_uses 1; #open_file_cache指令中的inactive参数时间内文件的最少使用次数，如,将该参数设置为1，则表示，如果文件在inactive时间内一次都没被使用，它将被移除。
    open_file_cache_valid 30s; #指多长时间检查一次缓存的有效信息。建议设置为30s。

    gzip on;  #开启gzip功能
    gzip_min_length 1024;  #设置请求资源超过该数值才进行压缩，单位字节
    gzip_buffers 16 8k; #设置压缩使用的buffer大小，第一个数字为数量，第二个为每个buffer的大小
    gzip_comp_level 6; #设置压缩级别，范围1-9,9压缩级别最高，也最耗费CPU资源
    gzip_types text/plain text/xhtml text/css text/js text/csv application/javascript application/x-javascript application/json application/xml text/xml application/atom+xml application/rss+xml application/vnd.android.package-archive application/vnd.iphone; #指定哪些类型的文件需要压缩
    gzip_disable "MSIE 6\."; #IE6浏览器不启用压缩
    gzip_proxied any; #Nginx作为反向代理的时候启用，决定开启或者关闭后端服务器返回的结果是否压缩，匹配的前提是后端服务器必须要返回包含”Via”的 header头。
    
    include conf.d/*.conf; #要加载conf.d/下的所有.conf配置文件
}


##以下为conf.d/example.conf的内容
server {

    listen      443;  #监听端口为443，可以自定义其他端口，也可以加上IP地址，如，listen 127.0.0.1:8080;
    server_name  aaa.com aaa.net; #定义网站域名，可以写多个，用空格分隔。
    #以下配置为开启ssl认证
    ssl_certificate sslkey/www.crt; #指定crt文件路径
    ssl_certificate_key sslkey/www.key; #指定私钥文件路径
    ssl_session_cache   shared:SSL:10m; #设置ssl会话使用的缓存为10M
    ssl_session_timeout 10m; #ssl会话超时时间为10分钟
    ssl_protocols TLSv1.1 TLSv1.2; #ssl版本，不要加1.0了，1.0不安全
    ssl_ciphers AES256-SHA256:AES128-SHA256:AES256-SHA:AES128-SHA:!aNULL:!eNULL:!MD5:!DH:!ECDH:!DHE:!ECDHE:!RC4:!EXPORT; #开启或者关闭指定算法,这些是安全漏洞工具建议的配置
    ssl_prefer_server_ciphers on; #如果不指定默认为off，当为on时，服务器加密算法将优于客户端加密算法。

    access_log  logs/host.access.log  main; #定义访问日志，可以针对每一个server（即每一个站点）设置它们自己的访问日志。

    ##在server{}里有很多location配置段
    location / {
        root   html;  #定义网站根目录，目录可以是相对路径也可以是绝对路径。
        index  index.html index.htm; #定义站点的默认页。
    }

    error_page  404              /404.html;  #定义404页面
    error_page   500 502 503 504  /50x.html;  #当状态码为500、502、503、504时，则访问50x.html
    location = /50x.html {
        root   html;  #定义50x.html所在路径
    }

    #定义哪些目录下的php不能访问，一般要限制所有可写的目录下的php
    location ~ .*(data|config|template|attachments|forumdata|attachment|images|log|conf|cache)/.*\.php$ {
        deny all;
    }

    #设置防盗链，不记录日志，缓存过期时间为7天
    location ~* ^.+\.(swf|jpg|gif|bmp|png|jpeg|zip|rar)$ {
         expires 7d;
         access_log /dev/null;
         valid_referers none blocked server_names *.aaa.net *.aaa.com;
         if ($invalid_referer) {
              return 403;
         }
    }
    #js、css不记录日志，缓存过期时间为7天
    location ~ .*\.(js|css)$
    {
            expires      7d;
            access_log off;
    }

    #针对php的配置
    location ~ \.php$ {
            #fastcgi_pass   unix:/tmp/55188_71-fpm.sock;
            fastcgi_pass   127.0.0.1:9005; #这个是php-fpm的监听端口，nginx会把php的请求转发给php-fpm处理
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            fastcgi_param  X-Real-IP $remote_addr;
            include        fastcgi_params;
        }

    #针对admin.php做限制
    location  /admin.php 
    {
    allow 12.13.12.12; #允许的ip
        allow 22.22.22.0/24; #允许的ip段
        deny all;
    }

}

## 反向代理示例
server {
    listen 80;
    server_name bbb.com;
    proxy_buffering on; #该参数设置是否开启proxy的buffer功能, 如果这个设置为off，那么proxy_buffers和proxy_busy_buffers_size这两个指令将会失效
    proxy_buffer_size 4k; #该参数用来设置header缓存的大小，不能低于4k
    proxy_buffers 8 4k; #这个参数设置存储被代理服务器上的数据所占用的buffer的个数和每个buffer的大小。
    proxy_busy_buffers_size 16k; #在所有的buffer里，我们需要规定一部分buffer把自己存的数据传给A，这部分buffer就叫做busy_buffer，该参数用来设置处于busy状态的buffer有多大。
    proxy_temp_path /tmp/nginx_proxy_tmp 1 2; #定义proxy的临时文件存在目录以及目录的层级，1表示层级1的目录名为一个数字(0-9),2表示层级2目录名为2个数字(00-99)
    proxy_max_temp_file_size 100M; #设置临时文件的总大小
    proxy_temp_file_write_size 16k; #设置同时写入临时文件的数据量的总大小
    
    location /
    {
        proxy_pass http://123.23.13.11/; #后端服务器的ip地址
        proxy_set_header Host   $host; #访问后端服务器时，用哪个域名访问呢，这里的$host就是server_name。
        proxy_set_header X-Real-IP      $remote_addr; # 用来设置被代理端接收到的远程客户端IP，如果不设置，则header信息中并不会透传远程真实客户端的IP地址。
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; #同上
    }
}
```



## 4.架构分析
### A.Nginx模块化
Nginx基于模块化设计，每个模块是一个功能实现，分布式开发，团队协作



核心模块、标准HTTP模块、可选HTTP模块、邮件模块、第三方模块



编译后的源码目录objs/ngx_modules.c



### B.Nginx的web请求机制
##### 同步机制
```plain
同步、异步发生在当客户端发起请求后，服务端处理客户端的请求时。
同步机制，是指客户端发送请求后，需要等待服务端（内核）返回信息后，再继续发送下一个请求。
在同步机制中，所有的请求在服务器端得到同步，即发送方和接收方对请求的处理步调是一致的。
```



##### 异步机制
```plain
异步机制，是指客户端发出一个请求后，不等待服务端（内核）返回信息，就继续发送下一个请求。
在异步机制中，所有来自发送方的请求形成一个队列，接收方处理完后再通知发送方。


举例：一家酒店前台，在旺季的高峰时间段会接很多预定酒席的电话。
如果是同步机制情况下，前台每接一个电话后先不挂掉电话，而是去查询有无剩余酒席，查到结果后，告诉客户。
如果是异步机制情况下，前台每接一个预定电话直接回复客户，一会回复，此时前台把查询这件事情交给了另外的同事，
该前台挂掉电话后，继续处理其他客户的事情，当另外的同事查询到结果后再通知给前台，前台再通知客户。
```



##### 阻塞
```plain
阻塞与非阻塞发生在IO调度中，比如内核到磁盘IO。
阻塞方式下，进程/线程在获取最终结果之前，被系统挂起了，也就是所谓的阻塞了，在阻塞过程中该进程什么都干不了，
直到最终结果反馈给它时，它才恢复运行状态。
```



##### 非阻塞
```plain
非阻塞方式和阻塞相反，进程/线程在获取最终结果之前，并没有进入被挂起的状态，而是该进程可以继续执行新的任务。
当有最终结果反馈给该进程时，它再把结果交给客户端。

举例：依然是酒店前台接待预定酒席电话的案例。
此时角色不再是前台，而是她的查询有无剩余酒席的同事。如果是阻塞方式，该同事在查询有无剩余酒席的过程中，需要傻傻地
等待酒店管理系统给他返回结果，在此期间不能做其他事情。
如果是非阻塞，该同事在等待酒店管理系统给他返回结果这段时间，可以做其他事情，比如可以通知前台剩余酒席的情况。
```



##### Nginx的请求机制
```plain
Nginx之所以可以支持高并发，是因为Nginx用的是异步非阻塞的机制，而Nginx是靠事件驱动模型来实现这种机制的。

在Nginx的事件驱动模型下，客户端发起的所有请求在服务端都会被标记为一个事件，Nginx会把这些事件收集到“事件收集器”里，
然后再把这些事件交给内核去处理。
```



### C.事件驱动模型
```plain
事件驱动模型是实现异步非阻塞的一个手段。事件驱动模型中，一个进程（线程）就可以了。

对于web服务器来说，客户端A的请求连接到服务端时，服务端的某个进程（Nginx worker process）会处理该请求，
此进程在没有返回给客户端A结果时，它又去处理了客户端B的请求。
服务端把客户端A以及客户端B发来的请求作为事件交给了“事件收集器”，
而“事件收集器”再把收集到的事件交由“事件发送器”发送给“事件处理器”进行处理。
最后“事件处理器”处理完该事件后，通知服务端进程，服务端进程再把结果返回给客户端A、客户端B。

在这个过程中，服务端进程做的事情属于用户级别的，而事件处理这部分工作属于内核级别的。
也就是说这个事件驱动模型是需要操作系统内核来作为支撑的。
```



#### Nginx的事件驱动模型
```plain
Nginx的事件驱动模型，支持select、poll、epoll、rtsig、kqueue、/dev/poll、eventport等。
最常用的是前三种，其中kqueue模型用于支持BSD系列平台的事件驱动模型。kqueue是poll模型的一个变种，本质上和epoll一样。
/dev/poll是Unix平台的事件驱动模型，其主要在Solaris7及以上版本、HP/UX11.22及以上版本、IRIX6.5.15及以上版本、
Tru64 Unix 5.1A及以上版本的平台使用。
eventport是用于支持Solaris10及以上版本的事件驱动模型。
```



#### select模型
```plain
Linux和Windows都支持，使用select模型的步骤是：

1. 创建所关注事件的描述符集合，对于一个描述符，可以关注其上面的读(Read)事件、写(Write)事件以及异常发生(Exception)事件。
在select模型中，要创建这3类事件描述符集合。

2. 调用底层提供的select()函数，等待事件发生。

3. 轮询所有事件描述符集合中的每一个事件描述符，检查是否有相应的事件发生，如果有就进行处理。
```



#### poll模型
```plain
poll模型是Linux平台上的事件驱动模型，在Linux2.1.23中引入的，Windows平台不支持该模型。

poll模型和select模型工作方式基本相同，区别在于，select模型创建了3个描述符集合，而poll模型只创建一个描述符集合。
```



#### epoll模型
```plain
epoll模型属于poll模型的变种，在Linux2.5.44中引入。epoll比poll更加高效，原因在于它不需要轮询整个描述符集合，
而是Linux内核会关注事件集合，当有变动时，内核会发来通知。
```



### D.Nginx架构
```plain
Nginx服务器使用 master/worker 多进程模式。
主进程(Master process)启动后，会接收和处理外部信号；
主进程启动后通过fork() 函数产生一个或多个子进程(work process)，每个子进程会进行进程初始化、
模块调用以及对事件的接收和处理等工作。
```



#### 主进程
```plain
主要功能是和外界通信和对内部其他进程进行管理，具体来说有以下几点：

* 读取Nginx配置文件并验证其有效性和正确性

* 建立、绑定和关闭socket

* 按照配置生成、管理工作进程

* 接收外界指令，比如重启、关闭、重载服务等指令

* 日志文件管理
```



#### 子进程（worker process)
```plain
是由主进程生成，生成数量可以在配置文件中定义。该进程主要工作有：

* 接收客户端请求

* 将请求依次送入各个功能模块进行过滤处理

* IO调用，获取响应数据

* 与后端服务器通信，接收后端服务器处理结果

* 数据缓存，访问缓存索引，查询和调用缓存数据

* 发送请求结果，响应客户端请求

* 接收主进程指令，如重启、重载、退出等
```





## 5.虚拟主机配置
```nginx
user nobody; # 定义运行nginx服务的用户,还可以加上组,如 user nobody nobody
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    include vhost/*.conf; #包含vhost下的.conf文件
}
```



```nginx
mkdir /usr/local/nginx/conf/vhost
vi /usr/local/nginx/conf/vhost/www.1.com.conf
    server{
    listen 80;
    server_name www.1.com;
    root /data/wwwroot/www.1.com;
    index index.html index.htm;
    }
vi /usr/local/nginx/conf/vhost/www.1.com.conf
    server{
    listen 80;
    server_name *.2.com 2.com;
    root /data/wwwroot/www.2.com;
    index index.html index.htm;
    }
vi /usr/local/nginx/conf/vhost/default.conf
    server{
        listen 80 default_server;
        deny all;
    }
mkdir -p /data/wwwroot
```



## 6.rewrite配置
### nginx 常用全局变量
| 变量 | 说明 |
| --- | --- |
| $args | 请求中的参数，如[www.123.com/1.php?a=1&b=2的$args就是a=1&b=2](http://www.123.com/1.php?a=1&b=2的$args就是a=1&b=2) |
| $content_length | HTTP请求信息里的"Content-Length" |
| $conten_type | HTTP请求信息里的"Content-Type" |
| $document_root | nginx虚拟主机配置文件中的root参数对应的值 |
| $document_uri | 当前请求中不包含指令的URI，如[www.123.com/1.php?a=1&b=2的$document_uri就是1.php,不包含后面的参数](http://www.123.com/1.php?a=1&b=2的$document_uri就是1.php,不包含后面的参数) |
| $host | 主机头，也就是域名 |
| $http_user_agent | 客户端的详细信息，也就是浏览器的标识，用curl -A可以指定 |
| $http_cookie | 客户端的cookie信息 |
| $limit_rate | 如果nginx服务器使用limit_rate配置了显示网络速率，则会显示，如果没有设置， 则显示0 |
| $remote_addr | 客户端的公网ip |
| $remote_port | 客户端的port |
| $remote_user | 如果nginx有配置认证，该变量代表客户端认证的用户名 |
| $request_body_file | 做反向代理时发给后端服务器的本地资源的名称 |
| $request_method | 请求资源的方式，GET/PUT/DELETE等 |
| $request_filename | 当前请求的资源文件的路径名称，相当于是 |
| $request_uri | 请求的链接，包括 |
| $scheme | 请求的协议，如ftp,http,https |
| $server_protocol | 客户端请求资源使用的协议的版本，如HTTP/1.0，HTTP/1.1，HTTP/2.0等 |
| $server_addr | 服务器IP地址 |
| $server_name | 服务器的主机名 |
| $server_port | 服务器的端口号 |
| $uri | 和$document_uri相同 |
| $http_referer | 客户端请求时的referer，通俗讲就是该请求是通过哪个链接跳过来的，用curl -e可以指定 |


### if条件举例
```plain
条件判断语句由Nginx内置变量、逻辑判断符号和目标字符串三部分组成。
其中，内置变量是Nginx固定的非自定义的变量，如，$request_method, $request_uri等。
逻辑判断符号，有=, !=, ~, ~*, !~, !~*
!表示相反的意思，~为匹配符号，它右侧为正则表达式，区分大小写，而~*为不区分大小写匹配。
目标字符串可以是正则表达式，通常不用加引号，但表达式中有特殊符号时，比如空格、花括号、分号等，需要用单引号引起来。
```



#### 示例1
```nginx
nginxif ($request_method = POST)  //当请求的方法为POST时，直接返回405状态码
{
    return 405; //在该示例中并未用到rewrite规则，if中支持用return指令。
}
```



#### 示例2
```nginx
if ($http_user_agent ~ MSIE) //user_agent带有MSIE字符的请求，直接返回403状态码
{
    return 403;
}

如果想同时限制多个user_agent，还可以写成这样

if ($http_user_agent ~ "MSIE|firefox|spider")
{
    return 403;
}
```



#### 示例3
```nginx
if(!-f $request_filename)  //当请求的文件不存在，将会执行下面的rewrite规则
{
    rewrite 语句;
}
```



#### 示例4
```nginx
if($request_uri ~* 'gid=\d{9,12}/')  //\d表示数字，{9,12}表示数字出现的次数是9到12次，如gid=123456789/就是符合条件的。
{
    rewrite 语句;
}
```



### rewrite中的break和last
```nginx
两个指令用法相同，但含义不同，需要放到rewrite规则的末尾，用来控制重写后的链接是否继续被nginx配置执行(主要是rewrite、return指令)。

示例1（连续两条rewrite规则）：
server{
    listen 80; 
    server_name test.com;
    root /tmp/123.com;

    rewrite /1.html /2.html ;
    rewrite /2.html /3.html ;
    
}
当我们请求1.html时，最终访问到的是3.html，两条rewrite规则先后执行。
```



#### break和last在location {}外部
```nginx
格式：rewrite xxxxx  break;

示例2（增加break）：
server{
    listen 80; 
    server_name test.com;
    root /tmp/123.com;

    rewrite /1.html /2.html break;
    rewrite /2.html /3.html;
}
当我们请求1.html时，最终访问到的是2.html
说明break在此示例中，作用是不再执行break以下的rewrite规则。

但，当配置文件中有location时，它还会去执行location{}段的配置（请求要匹配该location）。

示例3（break后面还有location段）：
server{
    listen 80; 
    server_name test.com;
    root /tmp/123.com;

    rewrite /1.html /2.html break;
    rewrite /2.html /3.html;
    location /2.html {
        return 403;
    }
}
当请求1.html时，最终会返回403状态码，说明它去匹配了break后面的location{}配置。

以上2个示例中，可以把break替换为last，它们两者起到的效果一模一样。
```



#### 当break和last在location{}里面
```nginx
示例4（什么都不加）：
server{
    listen 80; 
    server_name test.com;
    root /tmp/123.com;
    
    location / {
        rewrite /1.html /2.html;
        rewrite /2.html /3.html;
    }
    location /2.html
    {
        rewrite /2.html /a.html;
    }
    location /3.html
    {
        rewrite /3.html /b.html;
    }
}
当请求/1.html，最终将会访问/b.html，连续执行location /下的两次rewrite，跳转到了/3.html，然后又匹配location /3.html

示例5（增加break）：
server{
    listen 80; 
    server_name test.com;
    root /tmp/123.com;
    
    location / {
        rewrite /1.html /2.html break;
        rewrite /2.html /3.html;
    }
    location /2.html
    {
        rewrite /2.html /a.html;
    }
    location /3.html
    {
        rewrite /3.html /b.html;
    }
}
当请求/1.html，最终会访问/2.html
在location{}内部，遇到break，本location{}内以及后面的所有location{}内的所有指令都不再执行。


示例6（增加last）:
server{
    listen 80; 
    server_name test.com;
    root /tmp/123.com;
    
    location / {
        rewrite /1.html /2.html last;
        rewrite /2.html /3.html;
    }
    location /2.html
    {
        rewrite /2.html /a.html;
    }
    location /3.html
    {
        rewrite /3.html /b.html;
    }
}
当请求/1.html，最终会访问/a.html
在location{}内部，遇到last，本location{}内后续指令不再执行，而重写后的url再次从头开始，从头到尾匹配一遍规则。
```



#### 结论
+ 当rewrite规则在location{}外，break和last作用一样，遇到break或last后，其后续的rewrite/return语句不再执行。但后续有location{}的话，还会近一步执行location{}里面的语句,当然前提是请求必须要匹配该location。
+ 当rewrite规则在location{}里，遇到break后，本location{}与其他location{}的所有rewrite/return规则都不再执行。
+ 当rewrite规则在location{}里，遇到last后，本location{}里后续rewrite/return规则不执行，但重写后的url再次从头开始执行所有规则，哪个匹配执行哪个。



### nginx的return指令
```plain
该指令一般用于对请求的客户端直接返回响应状态码。在该作用域内return后面的所有nginx配置都是无效的。
可以使用在server、location以及if配置中。

除了支持跟状态码，还可以跟字符串或者url链接。
```



#### 直接返回状态码
```nginx
示例1：
server{
    listen 80;
    server_name www.aming.com;
    return 403;
    rewrite /(.*) /abc/$1;  //该行配置不会被执行。
}

示例2：
server {
.....

if ($request_uri ~ "\.htpasswd|\.bak")
{
    return 404;
    rewrite /(.*) /aaa.txt;  //该行配置不会被执行。
}
//如果下面还有其他配置，会被执行。
.....
}
```



#### 返回字符串
```nginx
示例3：
server{
    listen 80;
    server_name www.aming.com;
    return 200 "hello";
}
说明：如果要想返回字符串，必须要加上状态码，否则会报错。
还可以支持json数据

示例4：
location ^~ /aming {
    default_type application/json ;
    return 200  '{"name":"aming","id":"100"}';
}

也支持写一个变量

示例5：
location /test {
    return 200 "$host $request_uri";
}
```



#### 返回url
```nginx
示例6：
server{
    listen 80;
    server_name www.aming.com;
    return http://www.aminglinux.com/123.html;
    rewrite /(.*) /abc/$1;  //该行配置不会被执行。
}
注意：return后面的url必须是以http://或者https://开头的。
```



#### 生产场景实战
```nginx
背景：网站被黑了，凡是在百度点击到本网站的请求，全部都跳转到了一个赌博网站。
通过nginx解决：
if ($http_referer ~ 'baidu.com') 
{
    return 200 "<html><script>window.location.href='//$host$request_uri';</script></html>";
}

如果写成：
return http://$host$request_uri; 在浏览器中会提示“重定向的次数过多”。
```



### rewrite规则
```nginx
格式：rewrite  regex replacement [flag] 

* rewrite配置可以在server、location以及if配置段内生效

* regex是用于匹配URI的正则表达式，其不会匹配到$host（域名）

* replacement是目标跳转的URI，可以以http://或者https://开头，也可以省略掉$host，直接写$request_uri部分（即请求的链接）

* flag，用来设置rewrite对URI的处理行为，其中有break、last、rediect、permanent，其中break和last在前面已经介绍过，
rediect和permanent的区别在于，前者为临时重定向(302)，而后者是永久重定向(301)，对于用户通过浏览器访问，这两者的效果是一致的。
但是，对于搜索引擎蜘蛛爬虫来说就有区别了，使用301更有利于SEO。所以，建议replacemnet是以http://或者https://开头的flag使用permanent。
```



#### 示例1
```nginx
location / {
    rewrite /(.*) http://www.aming.com/$1 permanent;
}
说明：.*为正则表达式，用()括起来，在后面的URI中可以调用它，第一次出现的()用$1调用，第二次出现的()用$2调用，以此类推。
```



#### 示例2
```nginx
location / {
    rewrite /.* http://www.aming.com$request_uri permanent;
}
说明：在replacement中，支持变量，这里的$request_uri就是客户端请求的链接
```



#### 示例3
```nginx
server{
    listen 80;
    server_name www.123.com;
    root /tmp/123.com;
    index index.html;
    rewrite /(.*) /abc/$1 redirect;
}
说明：本例中的rewrite规则有问题，会造连续循环，最终会失败，解决该问题有两个方案。
关于循环次数，经测试发现，curl 会循环50次，chrome会循环80次，IE会循环120次，firefox会循环20次。
```



#### 示例4
```nginx
server{
    listen 80;
    server_name www.123.com;
    root /tmp/123.com;
    index index.html;
    rewrite /(.*) /abc/$1 break;
}
说明：在rewrite中使用break，会避免循环。
```



#### 示例5
```nginx
server{
    listen 80;
    server_name www.123.com;
    root /tmp/123.com;
    index index.html;
    if ($request_uri !~ '^/abc/')
    {
        rewrite /(.*) /abc/$1 redirect;
    }
}
说明：加一个条件限制，也可以避免产生循环
```



### Rewrite实战
```plain
本部分内容为nginx生产环境中使用的场景示例。
```



#### 域名跳转（域名重定向）
```nginx
示例1（不带条件的）：
server{
    listen 80;
    server_name www.aminglinux.com;
    rewrite /(.*) http://www.aming.com/$1 permanent;
    .......
    
}

示例2（带条件的）：
server{
    listen 80;
    server_name www.aminglinux.com aminglinux.com;
    if ($host != 'www.aminglinux.com')
    {
        rewrite /(.*) http://www.aminglinux.com/$1 permanent;
    }
    .......
    
}
示例3（http跳转到https）：
server{
    listen 80;
    server_name www.aminglinux.com;
    rewrite /(.*) https://www.aminglinux.com/$1 permanent;
    .......
    
}
示例4（域名访问二级目录）
server{
    listen 80;
    server_name bbs.aminglinux.com;
    rewrite /(.*) http://www.aminglinux.com/bbs/$1 last;
    .......
    
}
示例5（静态请求分离）
server{
    listen 80;
    server_name www.aminglinux.com;
    location ~* ^.+.(jpg|jpeg|gif|css|png|js)$
    {
        rewrite /(.*) http://img.aminglinux.com/$1 permanent;
    }

    .......
    
}
或者：
server{
    listen 80;
    server_name www.aminglinux.com;
    if ( $uri ~* 'jpg|jpeg|gif|css|png|js$')
    {
        rewrite /(.*) http://img.aminglinux.com/$1 permanent;
    }

    .......
    
}
```



#### 防盗链
```nginx
示例6
server{
    listen 80;
    server_name www.aminglinux.com;
    location ~* ^.+.(jpg|jpeg|gif|css|png|js|rar|zip|flv)$
    {
        valid_referers none blocked server_names *.aminglinux.com aminglinux.com *.aming.com aming.com;
        if ($invalid_referer)
        {
            rewrite /(.*) http://img.aminglinux.com/images/forbidden.png;
        }
    }

    .......
    
}
说明：*这里是通配，跟正则里面的*不是一个意思，none指的是referer不存在的情况（curl -e 测试），
      blocked指的是referer头部的值被防火墙或者代理服务器删除或者伪装的情况，
      该情况下，referer头部的值不以http://或者https://开头（curl -e 后面跟的referer不以http://或者https://开头）。
或者：
    location ~* ^.+.(jpg|jpeg|gif|css|png|js|rar|zip|flv)$
    {
        valid_referers none blocked server_names *.aminglinux.com *.aming.com aminglinux.com aming.com;
        if ($invalid_referer)
        {
            return 403;
        }
    }
```



#### 伪静态
```nginx
示例7(discuz伪静态)：
location /  {
    rewrite ^([^\.]*)/topic-(.+)\.html$ $1/portal.php?mod=topic&topic=$2 last;
    rewrite ^([^\.]*)/forum-(\w+)-([0-9]+)\.html$ $1/forum.php?mod=forumdisplay&fid=$2&page=$3 last;
    rewrite ^([^\.]*)/thread-([0-9]+)-([0-9]+)-([0-9]+)\.html$ $1/forum.php?mod=viewthread&tid=$2&extra=page%3D$4&page=$3 last;
    rewrite ^([^\.]*)/group-([0-9]+)-([0-9]+)\.html$ $1/forum.php?mod=group&fid=$2&page=$3 last;
    rewrite ^([^\.]*)/space-(username|uid)-(.+)\.html$ $1/home.php?mod=space&$2=$3 last;
    rewrite ^([^\.]*)/(fid|tid)-([0-9]+)\.html$ $1/index.php?action=$2&value=$3 last;
}
```



#### rewrite多个条件的并且
```nginx
示例8：
location /{
    set $rule 0;
    if ($document_uri !~ '^/abc')
    {
        set $rule "${rule}1";
    }
    if ($http_user_agent ~* 'ie6|firefox')
    {
       set $rule "${rule}2";
    }
    if ($rule = "012")
    {
        rewrite /(.*) /abc/$1 redirect;
    }
}
```



## 7.location配置
### A.安装echo模块
```shell
git clone https://github.com/openresty/echo-nginx-module.git
make clean
./configure --prefix=/usr/local/nginx --add-module=/echo-nginx-module
make
make install
/usr/local/nginx/sbin/nginx -s stop
/usr/local/nginx/sbin/nginx


vi /usr/local/nginx/conf/vhost/www.1.com.conf
    location /abc/
    {
        echo 123;
    }
curl -x127.0.0.1:80 www.1.com/abc/ssss
```



### location语法
```nginx
nginx location语法规则：location [=|~|~*|^~] /uri/ { … }
nginx的location匹配的变量是$uri
```

| 符号 | 说明 |
| --- | --- |
| = | 表示精确匹配 |
| ^~ | 表示uri以指定字符或字符串开头 |
| ~ | 表示区分大小写的正则匹配 |
| ~* | 表示不区分大小写的正则匹配 |
| / | 通用匹配，任何请求都会匹配到 |


#### 规则优先级
```plain
=  高于  ^~  高于  ~* 等于 ~  高于  /
```



#### 规则示例
```nginx
location = "/12.jpg" { ... }
如：
www.aminglinux.com/12.jpg 匹配
www.aminglinux.com/abc/12.jpg 不匹配

location ^~ "/abc/" { ... }
如：
www.aminglinux.com/abc/123.html 匹配
www.aminglinux.com/a/abc/123.jpg 不匹配

location ~ "png" { ... }
如：
www.aminglinux.com/aaa/bbb/ccc/123.png 匹配
www.aminglinux.com/aaa/png/123.html 匹配

location ~* "png" { ... }
如：
www.aminglinux.com/aaa/bbb/ccc/123.PNG 匹配
www.aminglinux.com/aaa/png/123.html 匹配


location /admin/ { ... }
如：
www.aminglinux.com/admin/aaa/1.php 匹配
www.aminglinux.com/123/admin/1.php 不匹配
```



#### 小常识
```nginx
有些资料上介绍location支持不匹配 !~，
如： location !~ 'png'{ ... }
这是错误的，location不支持 !~

如果有这样的需求，可以通过if来实现，
如： if ($uri !~ 'png') { ... }

注意：location优先级小于if
```



## 8.nginx代理
### A.正向代理
```plain
Nginx正向代理使用场景并不多见。
需求场景1：
如果在机房中，只有一台机器可以联网，其他机器只有内网，内网的机器想用使用yum安装软件包，在能能联网的机器上配置一个正向代理即可。
```



#### Nginx正向代理配置文件
说明： 以下配置文件为nginx官方提供，该方法只能实现针对http的网站的访问，如果是https就会有问题。要想实现https的正向代理，可以使用一个三方模块，后面介绍。



```nginx
server {
    listen 80 default_server;
    resolver 119.29.29.29;
    location /
    {
        proxy_pass http://$host$request_uri;
    }
}
```



#### Nginx正向代理配置执行说明
+ resolver



```nginx
语法：resolver address;

address为DNS服务器的地址，国内通用的DNS 119.29.29.29为dnspod公司提供。 国际通用DNS 8.8.8.8或者8.8.4.4为google提供。
其他可以参考 http://dns.lisect.com/
    
示例：resolver 119.29.29.29;
```



+ default_server



```plain
之所以要设置为默认虚拟主机，是因为这样就不用设置server_name了，任何域名解析过来都可以正常访问。
```



+ proxy_pass



```plain
该指令用来设置要代理的目标url，正向代理服务器设置就保持该固定值即可。关于该指令的详细解释在反向代理配置中。
```



#### Nginx正向代理支持https
下载三方模块ngx_http_proxy_connect_module，github地址：[https://github.com/chobits/ngx_http_proxy_connect_module](https://github.com/chobits/ngx_http_proxy_connect_module) 注意，不同的Nginx版本，还需要下载不同的patch包。



下面的例子，以1.9.12为例



```shell
wget http://nginx.org/download/nginx-1.9.12.tar.gz
tar -xzvf nginx-1.9.12.tar.gz
cd nginx-1.9.12/
patch -p1 < /path/to/ngx_http_proxy_connect_module/patch/proxy_connect.patch
./configure --add-dynamic-module=/path/to/ngx_http_proxy_connect_module
make && make install
```



#### Nginx正向代理配置文件
```nginx
server {
     listen                         3128;


     # dns resolver used by forward proxying
     resolver                       119.29.29.29;


     # forward proxy for CONNECT request
     proxy_connect;
     proxy_connect_allow            80 443 3000 9070 9074;
     proxy_connect_connect_timeout  10s;
     proxy_connect_read_timeout     10s;
     proxy_connect_send_timeout     10s;


     # forward proxy for non-CONNECT request
     location / {
         proxy_pass http://$host;
         proxy_set_header Host $host;
     }
}
```



#### 测试示例
```shell
$ curl https://github.com/ -v -x 127.0.0.1:3128
*   Trying 127.0.0.1...                                           -.
* Connected to 127.0.0.1 (127.0.0.1) port 3128 (#0)                | curl creates TCP connection with nginx (with proxy_connect module).
* Establish HTTP proxy tunnel to github.com:443                   -'
> CONNECT github.com:443 HTTP/1.1                                 -.
> Host: github.com:443                                         (1) | curl sends CONNECT request to create tunnel.
> User-Agent: curl/7.43.0                                          |
> Proxy-Connection: Keep-Alive                                    -'
>
< HTTP/1.0 200 Connection Established                             .- nginx replies 200 that tunnel is established.
< Proxy-agent: nginx                                           (2)|  (The client is now being proxied to the remote host. Any data sent
<                                                                 '-  to nginx is now forwarded, unmodified, to the remote host)

* Proxy replied OK to CONNECT request
* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  -.
* Server certificate: github.com                                   |
* Server certificate: DigiCert SHA2 Extended Validation Server CA  | curl sends "https://github.com" request via tunnel,
* Server certificate: DigiCert High Assurance EV Root CA           | proxy_connect module will proxy data to remote host (github.com).
> GET / HTTP/1.1                                                   |
> Host: github.com                                             (3) |
> User-Agent: curl/7.43.0                                          |
> Accept: */*                                                     -'
>
< HTTP/1.1 200 OK                                                 .-
< Date: Fri, 11 Aug 2017 04:13:57 GMT                             |
< Content-Type: text/html; charset=utf-8                          |  Any data received from remote host will be sent to client
< Transfer-Encoding: chunked                                      |  by proxy_connect module.
< Server: GitHub.com                                           (4)|
< Status: 200 OK                                                  |
< Cache-Control: no-cache                                         |
< Vary: X-PJAX                                                    |
...                                                               |
... <other response headers & response body> ...                  |
...
```



#### linux机器上配置全局代理
在 /etc/profile 文件中增加如下三项。



```plain
export proxy="http://{proxy_server_ip}:3128"
export http_proxy=$proxy
export https_proxy=$proxy
```



使配置生效



```shell
source /etc/profile
```



对那些没有域名解析通过绑定hosts文件来访问的域名，不让其走http/https代理，需要额外增加环境变量：



```shell
export no_proxy='a.test.com,127.0.0.1,2.2.2.2'
```



### B.反向代理
```nginx
Nginx反向代理在生产环境中使用很多的。

场景1：
域名没有备案，可以把域名解析到香港一台云主机上，在香港云主机做个代理，而网站数据是在大陆的服务器上。

示例1：
server 
{
    listen 80;
    server_name aminglinux.com;
    
    location /
    {
        proxy_pass http://123.23.13.11/;
        proxy_set_header Host   $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```



#### 配置说明
##### 1. proxy_pass
```nginx
在正向代理中，已经使用过该指令。
格式很简单： proxy_pass  URL;
其中URL包含：传输协议（http://, https://等）、主机名（域名或者IP:PORT）、uri。

示例如下：
proxy_pass http://www.aminglinux.com/;
proxy_pass http://192.168.200.101:8080/uri;
proxy_pass unix:/tmp/www.sock;

对于proxy_pass的配置有几种情况需要注意。
示例2：
location /aming/
{
    proxy_pass http://192.168.1.10;
    ...
}


示例3：
location /aming/
{
    proxy_pass http://192.168.1.10/;
    ...
}

示例4：
location /aming/
{
    proxy_pass http://192.168.1.10/linux/;
    ...
}

示例5：
location /aming/
{
    proxy_pass http://192.168.1.10/linux;
    ...
}

假设server_name为www.aminglinux.com
当请求http://www.aminglinux.com/aming/a.html的时候，以上示例2-5分别访问的结果是

示例2：http://192.168.1.10/aming/a.html

示例3：http://192.168.1.10/a.html

示例4：http://192.168.1.10/linux/a.html

示例5：http://192.168.1.10/linuxa.html


总结：代理加上根'/path'的话，会把location的路径也加上。
     加上'/'比较规范，且可读性强
```



##### 2. proxy_set_header
```nginx
proxy_set_header用来设定被代理服务器接收到的header信息。

语法：proxy_set_header field value;
field为要更改的项目，也可以理解为变量的名字，比如host
value为变量的值

如果不设置proxy_set_header，则默认host的值为proxy_pass后面跟的那个域名或者IP（一般写IP），
比如示例4，请求到后端的服务器上时，完整请求uri为：http://192.168.1.10/linux/a.html

如果设置proxy_set_header，如 proxy_set_header host $host;
比如示例4，请求到后端的服务器完整uri为：http://www.aminglinux.com/linux/a.html

proxy_set_header X-Real-IP $remote_addr;和proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
用来设置被代理端接收到的远程客户端IP，如果不设置，则header信息中并不会透传远程真实客户端的IP地址。
可以用如下示例来测试：


示例6(被代理端)C端
server{
    listen 8080;
    server_name www.aminglinux.com;
    root /tmp/123.com_8080;
    index index.html;
        location /linux/ {
        echo "$host";
        echo $remote_addr;
        echo $proxy_add_x_forwarded_for;
    }
}

示例7（代理服务器上）B端
server {
    listen 80;
    server_name www.aminglinux.com;

    location /aming/
    {
    proxy_pass http://192.168.1.10:8080/linux/;
    proxy_set_header host $host;
    proxy_set_header X-Real-IP      $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```



###### 总结
+ A端（客户端）->B端（nginx反向代理服务器）->C端（Server端）；
+ 如果在B端不设置host，那么如果是tomcat同一个端口下的虚拟机主机，则无法正常解析，在nginx端需配上proxy_set_header host $host，设置成功以后，经过反向代理后，发送给C端的时候会带着这个host域名;
+ 如果我们在B端不设置X-Real-IP头，那么我们在C端记录日志就无法记录访问的客户机IP，不利于日志的收集，所以反向代理服务器需要加上proxy_set_header X-Real-IP      $remote_addr;这个配置项。
+ proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;请求经过的代理服务器的 IP 地址列表，可以通过这个变量来查看反向代理的功能是否正常。



##### 3. proxy_redirect
```nginx
该指令用来修改被代理服务器返回的响应头中的Location头域和“refresh”头域。
语法结构为：
proxy_redirect redirect replacement;
proxy_redirect default;
proxy_redirect off;

示例8：
server {
    listen 80;
    server_name www.aminglinux.com;
    index  index.html;

    location /
    {
    proxy_pass http://127.0.0.1:8080;
    proxy_set_header host $host;
    proxy_set_header X-Real-IP      $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

当请求的链接为 http://www.aminglinux.com/aming
结果会返回301，定向到了 http://www.aminglinux.com:8080/aming/

注意：返回301有几个先决条件
1. location后面必须是/; 
2. proxy_pass后面的URL不能加uri,只能是IP或者IP:port结尾，并不能以/结尾；
3. 访问的uri必须是一个真实存在的目录，如，这里的aming必须是存在的
4. 访问的时候，不能以/结尾，只能是 www.aminglinux.com/aming

虽然，这4个条件挺苛刻，但确实会遇到类似的请求。解决方法是，加一行proxy_redirect http://$host:8080/ /;

示例9：
server {
    listen 80;
    server_name www.aminglinux.com;
    index  index.html;

    location /
    {
    proxy_pass http://127.0.0.1:8080;
    proxy_set_header host $host;
    proxy_redirect http://$host:8080/ /;
    proxy_set_header X-Real-IP      $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```



## 9.buffer与cache
### A.buffer
#### proxy_buffering设置
```nginx
proxy_buffering主要是实现被代理服务器的数据和客户端的请求异步。
为了方便理解，我们定义三个角色，A为客户端，B为代理服务器，C为被代理服务器。

当proxy_buffering开启，A发起请求到B，B再到C，C反馈的数据先到B的buffer上，
然后B会根据proxy_busy_buffer_size来决定什么时候开始把数据传输给A。在此过程中，如果所有的buffer被写满，
数据将会写入到temp_file中。

相反，如果proxy_buffering关闭，C反馈的数据实时地通过B传输给A。
```



#### #以下配置，都是针对每一个http请求的。
```nginx
1. proxy_buffering  on;
该参数设置是否开启proxy的buffer功能，参数的值为on或者off。
如果这个设置为off，那么proxy_buffers和proxy_busy_buffers_size这两个指令将会失效。 
但是无论proxy_buffering是否开启，proxy_buffer_size都是生效的

2. proxy_buffer_size  4k;
该参数用来设置一个特殊的buffer大小的。
从被代理服务器（C）上获取到的第一部分响应数据内容到代理服务器（B）上，通常是header，就存到了这个buffer中。 
如果该参数设置太小，会出现502错误码，这是因为这部分buffer不够存储header信息。建议设置为4k。

3. proxy_buffers  8  4k;
这个参数设置存储被代理服务器上的数据所占用的buffer的个数和每个buffer的大小。
所有buffer的大小为这两个数字的乘积。

4. proxy_busy_buffer_size 16k;
在所有的buffer里，我们需要规定一部分buffer把自己存的数据传给A，这部分buffer就叫做busy_buffer。
proxy_busy_buffer_size参数用来设置处于busy状态的buffer有多大。

对于B上buffer里的数据何时传输给A，我个人的理解是这样的：
1）如果完整数据大小小于busy_buffer大小，当数据传输完成后，马上传给A；
2）如果完整数据大小不少于busy_buffer大小，则装满busy_buffer后，马上传给A；

5. proxy_temp_path
语法：proxy_temp_path  path [level1 level2 level3]
定义proxy的临时文件存在目录以及目录的层级。

例：proxy_temp_path /usr/local/nginx/proxy_temp 1 2;
其中/usr/local/nginx/proxy_temp为临时文件所在目录，1表示层级1的目录名为一个数字(0-9),2表示层级2目录名为2个数字(00-99)

6. proxy_max_temp_file_size
设置临时文件的总大小，例如 proxy_max_temp_file_size 100M;

7. proxy_temp_file_wirte_size
设置同时写入临时文件的数据量的总大小。通常设置为8k或者16k。
```



#### proxy_buffer示例
```nginx
server
{
    listen 80;
    server_name www.aminglinux.com;
    proxy_buffering on;
    proxy_buffer_size 4k;
    proxy_buffers 2 4k;
    proxy_busy_buffers_size 4k;
    proxy_temp_path /tmp/nginx_proxy_tmp 1 2;
    proxy_max_temp_file_size 20M;
    proxy_temp_file_write_size 8k;
    
    location /
    {
        proxy_pass      http://192.168.10.110:8080/;
        proxy_set_header Host   $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    }

}
```



### B.cache
#### proxy_cache设置
```nginx
proxy_cache将从C上获取到的数据根据预设规则存放到B上（内存+磁盘）留着备用，
A请求B时，B会把缓存的这些数据直接给A，而不需要再去向C去获取。

proxy_cache相关功能生效的前提是，需要设置proxy_buffering on;
#注意：proxy_buffering默认时开启的，如果需要开启缓存不需要配置该项
```



#### #proxy_cache主要参数
```nginx
1. proxy_cache
语法：proxy_cache zone|off

默认为off，即关闭proxy_cache功能，zone为用于存放缓存的内存区域名称。
例：proxy_cache my_zone;

从nginx 0.7.66版本开始，proxy_cache机制开启后会检测被代理端的HTTP响应头中的"Cache-Control"、"Expire"头域。
如，Cache-Control为no-cache时，是不会缓存数据的。

2. proxy_cache_bypass 
语法：proxy_cache_bypass string;

该参数设定，什么情况下的请求不读取cache而是直接从后端的服务器上获取资源。
这里的string通常为nginx的一些变量。

例：proxy_cahce_bypass $cookie_nocache $arg_nocache$arg_comment;
意思是，如果$cookie_nocache $arg_nocache$arg_comment这些变量的值只要任何一个不为0或者不为空时，
则响应数据不从cache中获取，而是直接从后端的服务器上获取。

3. proxy_no_cache
语法：proxy_no_cache string;

该参数和proxy_cache_bypass类似，用来设定什么情况下不缓存。

例：proxy_no_cache $cookie_nocache $arg_nocache $arg_comment;
表示，如果$cookie_nocache $arg_nocache $arg_comment的值只要有一项不为0或者不为空时，不缓存数据。

4. proxy_cache_key
语法：proxy_cache_key string;

定义cache key，如： proxy_cache_key $scheme$proxy_host$uri$is_args$args; （该值为默认值，一般不用设置）

5. proxy_cache_path
语法：proxy_cache_path path [levels=levels] keys_zone=name:size  [inactive=time] [max_size=size] 

path设置缓存数据存放的路径；

levels设置目录层级，如levels=1:2，表示有两级子目录,第一个目录名取md5值的倒数第一个值，第二个目录名取md5值的第2和3个值。如下图：
```



```nginx
keys_zone设置内存zone的名字和大小，如keys_zone=my_zone:10m

inactive设置缓存多长时间就失效，当硬盘上的缓存数据在该时间段内没有被访问过，就会失效了，该数据就会被删除，默认为10s。

max_size设置硬盘中最多可以缓存多少数据，当到达该数值时，nginx会删除最少访问的数据。

例：proxy_cache_path /data/nginx_cache/ levels=1:2 keys_zone=my_zone:10m inactive=300s max_size=5g
```



#### proxy_cache示例
```nginx
http 
{
    ...;
    
    proxy_cache_path /data/nginx_cache/ levels=1:2 keys_zone=my_zone:10m inactive=300s max_size=5g;
    
    ...;
    
    server
    {
        listen 80;
        server_name www.aminglinux.com;
        #缓冲区默认开启，这个配置可以根据自己是否需要设置大小来进行配置，也可使用默认
        proxy_buffering on;
        proxy_buffer_size 4k;
        proxy_buffers 2 4k;
        proxy_busy_buffers_size 4k;
        proxy_temp_path /tmp/nginx_proxy_tmp 1 2;
        proxy_max_temp_file_size 20M;
        proxy_temp_file_write_size 8k;
    
    
    
        location /
        {
            proxy_cache my_zone;
            proxy_pass      http://192.168.10.110:8080/;
            proxy_set_header Host   $host;
            proxy_set_header X-Real-IP      $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        }

    }
}

说明：核心配置为proxy_cache_path那一行。
```



## 10.Nginx的负载均衡配置
```plain
Nginx通过upstream和proxy_pass实现了负载均衡。本质上也是Nginx的反向代理功能，只不过后端的server为多个。
```



### 案例一（简单的轮询）
```nginx
upstream www {
    server 172.37.150.109:80;
    server 172.37.150.101:80;
    server 172.37.150.110:80;
}

server {
    listen 80;
    server_name www.aminglinux.com;
    location / {
        proxy_pass http://www/;
        proxy_set_header Host   $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

说明：当被代理的机器有多台时，需要使用upstream来定义一个服务器组，
其中www名字可以自定义，在后面的proxy_pass那里引用。
这样nginx会将请求均衡地轮询发送给www组内的三台服务器。
```



### 案例二（带权重轮询+ip_hash算法）
```nginx
upstream www {
    server 172.37.150.109:80 weight=50;
    server 172.37.150.101:80 weight=100;
    server 172.37.150.110:80 weight=50;
    ip_hash;
}

server {
    listen 80;
    server_name www.aminglinux.com;
    location / {
        proxy_pass http://www/;
        proxy_set_header Host   $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

说明：可以给www组内的三台机器配置权重，权重越高，则分配到的请求越多。
ip_hash为nginx负载均衡算法，原理很简单，它根据请求所属的客户端IP计算得到一个数值，然后把请求发往该数值对应的后端。
所以同一个客户端的请求，都会发往同一台后端，除非该后端不可用了。ip_hash能够达到保持会话的效果。
```



### 案例三（upstream其他配置）
```nginx
upstream www {
        server 172.37.150.109:80 weight=50 max_fails=3 fail_timeout=30s;
        server 172.37.150.101:80 weight=100;
        server 172.37.150.110:80 down;
        server 172.37.150.110:80 backup;
}
server
{
    listen 80;
    server_name www.aminglinux.com;
    location / {
        proxy_next_upstream off;
        proxy_pass http://www/;
        proxy_set_header Host   $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

说明：down，表示当前的server不参与负载均衡；
backup，为预留的机器，当其他的server（非backup）出现故障或者忙的时候，才会请求backup机器;
max_fails，允许请求失败的次数，默认为1。当失败次数达到该值，就认为该机器down掉了。 失败的指标是由proxy_next_upstream模块定义，其中404状态码不认为是失败。
fail_timeount，定义失败的超时时间，也就是说在该时间段内达到max_fails，才算真正的失败。默认是10秒。

proxy_next_upstream，通过后端服务器返回的响应状态码，表示服务器死活，可以灵活控制后端机器是否加入分发列表。
语法: proxy_next_upstream error | timeout | invalid_header | http_500 | http_502 | http_503 | http_504 |http_404 | off ...; 
默认值: proxy_next_upstream error timeout

error      # 和后端服务器建立连接时，或者向后端服务器发送请求时，或者从后端服务器接收响应头时，出现错误
timeout    # 和后端服务器建立连接时，或者向后端服务器发送请求时，或者从后端服务器接收响应头时，出现超时
invalid_header  # 后端服务器返回空响应或者非法响应头
http_500   # 后端服务器返回的响应状态码为500
http_502   # 后端服务器返回的响应状态码为502
http_503   # 后端服务器返回的响应状态码为503
http_504   # 后端服务器返回的响应状态码为504
http_404   # 后端服务器返回的响应状态码为404
off        # 停止将请求发送给下一台后端服务器
```



### 案例四（根据不同的uri）
```nginx
    upstream aa.com {         
                      server 192.168.0.121;
                      server 192.168.0.122;  
     }
    upstream bb.com {  
                       server 192.168.0.123;
                       server 192.168.0.124;
    }
    server {
        listen       80;
        server_name  www.aminglinux.com;
        location ~ aa.php
        {
            proxy_pass http://aa.com/;
            proxy_set_header Host   $host;
            proxy_set_header X-Real-IP      $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        location ~ bb.php
        {
              proxy_pass http://bb.com/;
              proxy_set_header Host   $host;
              proxy_set_header X-Real-IP      $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        location /
        {
              proxy_pass http://bb.com/;
              proxy_set_header Host   $host;
              proxy_set_header X-Real-IP      $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}

说明：请求aa.php的，会到aa.com组，请求bb.php的会到bb.com，其他请求全部到bb.com。
```



### 案例五（根据不同的目录）
```nginx
upstream aaa.com
{
            server 192.168.111.6;
}
upstream bbb.com
{
            server 192.168.111.20;
}
server {
        listen 80;
        server_name www.aminglinux.com;
        location /aaa/
        {
            proxy_pass http://aaa.com/aaa/;
            proxy_set_header Host   $host;
            proxy_set_header X-Real-IP      $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        location /bbb/
        {
            proxy_pass http://bbb.com/bbb/;
            proxy_set_header Host   $host;
            proxy_set_header X-Real-IP      $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        location /
        {
            proxy_pass http://bbb.com/;
            proxy_set_header Host   $host;
            proxy_set_header X-Real-IP      $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```



## 11.Nginx访问控制
```plain
Nginx的deny和allow指令是由ngx_http_access_module模块提供，Nginx安装默认内置了该模块。
除非在安装时有指定 --without-http_access_module。
```



### 语法
```nginx
语法：allow/deny address | CIDR | unix: | all

它表示，允许/拒绝某个ip或者一个ip段访问.如果指定unix:,那将允许socket的访问。
注意：unix在1.5.1中新加入的功能。

在nginx中，allow和deny的规则是按顺序执行的。
```



### 示例
```nginx
示例1：
location /
{
    allow 192.168.0.0/24;
    allow 127.0.0.1;
    deny all;
}

说明：这段配置值允许192.168.0.0/24网段和127.0.0.1的请求，其他来源IP全部拒绝。

示例2：
location ~ "admin"
{
    allow 110.21.33.121;
    deny all
}
说明：访问的uri中包含admin的请求，只允许110.21.33.121这个IP的请求。
```



## 12.Nginx基于$document_uri的访问控制
```plain
这就用到了变量$document_uri，根据前面所学内容，该变量等价于$uri，其实也等价于location匹配。
```



### 示例1
```nginx
if ($document_uri ~ "/admin/")
{
    return 403;
}

说明：当请求的uri中包含/admin/时，直接返回403.

if结构中不支持使用allow和deny。

测试链接：
1. www.aminglinux.com/123/admin/1.html 匹配
2. www.aminglinux.com/admin123/1.html  不匹配
3. www.aminglinux.com/admin.php  不匹配
```



### 示例2
```nginx
if ($document_uri = /admin.php)
{
    return 403;
}

说明：请求的uri为/admin.php时返回403状态码。

测试链接：
1. www.aminglinux.com/admin.php 匹配
2. www.aminglinux.com/123/admin.php  不匹配
```



### 示例3
```nginx
if ($document_uri ~ '/data/|/cache/.*\.php$')
{
    return 403;
}

说明：请求的uri包含data或者cache目录，并且是php时，返回403状态码。

测试链接：
1. www.aminglinux.com/data/123.php  匹配
2. www.aminglinux.com/cache1/123.php 不匹配
```



## 13.nginx基于$request_uri访问控制
```plain
$request_uri比$docuemnt_uri多了请求的参数。
主要是针对请求的uri中的参数进行控制。
```



##### 示例
```nginx
if ($request_uri ~ "gid=\d{9,12}")
{
    return 403;
}

说明：\d{9,12}是正则表达式，表示9到12个数字，例如gid=1234567890就符号要求。

测试链接：
1. www.aminglinux.com/index.php?gid=1234567890&pid=111  匹配
2. www.aminglinux.com/gid=123  不匹配

背景知识：
曾经有一个客户的网站cc攻击，对方发起太多类似这样的请求：/read-123405150-1-1.html
实际上，这样的请求并不是正常的请求，网站会抛出一个页面，提示帖子不存在。
所以，可以直接针对这样的请求，return 403状态码。
```



## 14.Nginx基于$user_agent的访问控制
```nginx
user_agent大家并不陌生，可以简单理解成浏览器标识，包括一些蜘蛛爬虫都可以通过user_agent来辨识。
通过观察访问日志，可以发现一些搜索引擎的蜘蛛对网站访问特别频繁，它们并不友好。
为了减少服务器的压力，其实可以把除主流搜索引擎蜘蛛外的其他蜘蛛爬虫全部封掉。
另外，一些cc攻击，我们也可以通过观察它们的user_agent找到规律。
```



##### 示例
```nginx
if ($user_agent ~ 'YisouSpider|MJ12bot/v1.4.2|YoudaoBot|Tomato')
{
    return 403;
}
说明：user_agent包含以上关键词的请求，全部返回403状态码。

测试：
1. curl -A "123YisouSpider1.0"
2. curl -A "MJ12bot/v1.4.1"
```



## 15.Nginx基于$http_referer的访问控制
```plain
在前面讲解rewrite时，曾经用过该变量，当时实现了防盗链功能。
其实基于该变量，我们也可以做一些特殊的需求。
```



##### 示例
```nginx
背景：网站被黑挂马，搜索引擎收录的网页是有问题的，当通过搜索引擎点击到网站时，却显示一个博彩网站。
由于查找木马需要时间，不能马上解决，为了不影响用户体验，可以针对此类请求做一个特殊操作。
比如，可以把从百度访问的链接直接返回404状态码，或者返回一段html代码。

if ($http_referer ~ 'baidu.com')
{
    return 404;
}

或者

if ($http_referer ~ 'baidu.com')
{
    return 200 "<html><script>window.location.href='//$host$request_uri';</script></html>";
}
```



## 16.Nginx的限速
```plain
可以通过ngx_http_limit_conn_module和ngx_http_limit_req_module模块来实现限速的功能。
```



### ngx_http_limit_conn_module
```plain
该模块主要限制下载速度。
```



#### #1. 并发限制
```nginx
配置示例
http
{
    ...
    limit_conn_zone $binary_remote_addr zone=aming:10m;
    ...
    server
    {
        ...
        limit_conn aming 10;
        ...   
    }
}
说明：首先用limit_conn_zone定义了一个内存区块索引aming，大小为10m，它以$binary_remote_addr作为key。
该配置只能在http里面配置，不支持在server里配置。

limit_conn 定义针对aming这个zone，并发连接为10个。在这需要注意一下，这个10指的是单个IP的并发最多为10个。
```



#### #2. 速度限制
```nginx
location ~ /download/ {
    ...
    limit_rate_after 512k;
    limit_rate 150k;
    ...
}
说明：limit_rate_after定义当一个文件下载到指定大小（本例中为512k）之后开始限速；
limit_rate 定义下载速度为150k/s。

注意：这两个参数针对每个请求限速。
```



### ngx_http_limit_req_module
```plain
该模块主要用来限制请求数。
可以用来防ddos攻击
```



#### #1. limit_req_zone
```nginx
语法: limit_req_zone $variable zone=name:size rate=rate;
默认值: none
配置段: http

设置一块共享内存限制域用来保存键值的状态参数。 特别是保存了当前超出请求的数量。 
键的值就是指定的变量（空值不会被计算）。
如limit_req_zone $binary_remote_addr zone=one:10m rate=1r/s;

说明：区域名称为one，大小为10m，平均处理的请求频率不能超过每秒一次,键值是客户端IP。
使用$binary_remote_addr变量， 可以将每条状态记录的大小减少到64个字节，这样1M的内存可以保存大约1万6千个64字节的记录。
如果限制域的存储空间耗尽了，对于后续所有请求，服务器都会返回 503 (Service Temporarily Unavailable)错误。
速度可以设置为每秒处理请求数和每分钟处理请求数，其值必须是整数，
所以如果你需要指定每秒处理少于1个的请求，2秒处理一个请求，可以使用 “30r/m”。
```



#### #2. limit_req
```nginx
语法: limit_req zone=name [burst=number] [nodelay];
默认值: —
配置段: http, server, location

设置对应的共享内存限制域和允许被处理的最大请求数阈值。 
如果请求的频率超过了限制域配置的值，请求处理会被延迟，所以所有的请求都是以定义的频率被处理的。 
超过频率限制的请求会被延迟，直到被延迟的请求数超过了定义的阈值，
这时，这个请求会被终止，并返回503 (Service Temporarily Unavailable) 错误。

这个阈值的默认值为0。如：
limit_req_zone $binary_remote_addr zone=aming:10m rate=1r/s;
server {
    location /upload/ {
        limit_req zone=aming burst=5;
    }
}

限制平均每秒不超过一个请求，同时允许超过频率限制的请求数不多于5个。

如果不希望超过的请求被延迟，可以用nodelay参数,如：

limit_req zone=aming burst=5 nodelay;
```



示例



```nginx
http {
    limit_req_zone $binary_remote_addr zone=aming:10m rate=1r/s;

    server {
        location  ^~ /download/ {  
            limit_req zone=aming burst=5;
        }
    }
}
```



##### 设定白名单IP
```nginx
如果是针对公司内部IP或者lo（127.0.0.1）不进行限速，如何做呢？这就要用到geo模块了。

假如，预把127.0.0.1和192.168.100.0/24网段设置为白名单，需要这样做。
在http { }里面增加：
geo $limited {
    default 1;
    127.0.0.1/32 0;
    192.168.100.0/24 0;
}

map $limited $limit {
    1 $binary_remote_addr;
    0 "";
}

原来的 “limit_req_zone $binary_remote_addr ” 改为“limit_req_zone $limit”

完整示例：

http {
    geo $limited {
        default 1;
        127.0.0.1/32 0;
        192.168.100.0/24 0;
    }

    map $limited $limit {
        1 $binary_remote_addr;
        0 "";
    }
    
    limit_req_zone $limit zone=aming:10m rate=1r/s;

    server {
        location  ^~ /download/ {  
            limit_req zone=aming burst=5;
        }
    }
}
```



## 17.Nginx的用户认证（类似tomcatbasic认证）
```plain
当访问一些私密资源时，最好配置用户认证，增加安全性。
```



##### 步骤和示例
+ 安装httpd



```shell
yum install -y httpd
```



+ 使用htpasswd生产密码文件



```shell
htpasswd -c /usr/local/nginx/conf/htpasswd liyedong #创建新文件
htpasswd /usr/local/nginx/conf/htpasswd liyedong1 #追加或者修改
```



+ 配置nginx用户认证



```nginx
location  /admin/
{
    auth_basic "Auth";
    auth_basic_user_file /usr/local/nginx/conf/htpasswd;
}
```



+ 测试



```shell
mkdir -p /data/wwwroot/www.1.com/admin
echo i am admin > /data/wwwroot/www.1.com/admin/admin.html
http://www.1.com/admin/admin.html
```



## 18.CA证书
### 什么是CA？
```plain
CA 是“Certificate Authority”的缩写，也叫“证书授权中心”。它是负责管理和签发证书的第三方机构，
就好比例子里面的中介C公司。
一般来说，CA必须是所有行业和所有公众都信任的、认可的。因此它必须具有足够的权威性。
就好比A、B两公司都必须信任C公司，才会找C公司作为公章的中介。
```



### 什么是CA证书？
```plain
CA证书，顾名思义，就是CA颁发的证书。

前面已经说了，人人都可以找工具制作证书。但是你一个小破孩制作出来的证书是没啥用处的。
因为你不是权威的CA机关，你自己搞的证书不具有权威性。
这就好比上述的例子里，某个坏人自己刻了一个公章，盖到介绍信上。但是别人一看，
不是受信任的中介公司的公章，就不予理睬。
```



### 什么是证书之间的信任关系？
```plain
在开篇的例子里谈到，引入中介后，业务员要同时带两个介绍信。第一个介绍信包含了两个公章，并注明，公章C信任公章A。
证书间的信任关系，就和这个类似。就是用一个证书来证明另一个证书是真实可信滴。
```



##### 什么是证书信任链？
```plain
实际上，证书之间的信任关系，是可以嵌套的。
比如，C信任A1，A1信任A2，A2信任A3......这个叫做证书的信任链。
只要你信任链上的头一个证书，那后续的证书，都是可以信任滴。
```



### 什么是根证书？
```plain
根证书的洋文叫“root certificate”，为了说清楚根证书是咋回事，再来看个稍微复杂点的例子。
假设C证书信任A和B；然后A信任A1和A2；B信任B1和B2。则它们之间，构成如下的一个树形关系（一个倒立的树）。
```





```plain
处于最顶上的树根位置的那个证书，就是“根证书”。除了根证书，其它证书都要依靠上一级的证书，来证明自己。
那谁来证明“根证书”可靠呢？
实际上，根证书自己证明自己是可靠滴（或者换句话说，根证书是不需要被证明滴）。
聪明的同学此刻应该意识到了：根证书是整个证书体系安全的根本。
所以，如果某个证书体系中，根证书出了问题（不再可信了），那么所有被根证书所信任的其它证书，也就不再可信了。
```



### 证书有啥用？
CA证书的作用有很多，只列出常用的几个。



+ 验证网站是否可信（针对HTTPS）



```plain
通常，我们如果访问某些敏感的网页（比如用户登录的页面），其协议都会使用HTTPS而不是HTTP,因为HTTP协议是明文的，
一旦有坏人在偷窥你的网络通讯，他/她就可以看到网络通讯的内容（比如你的密码、银行帐号、等）。
而 HTTPS 是加密的协议，可以保证你的传输过程中，坏蛋无法偷窥。
但是，千万不要以为，HTTPS协议有了加密，就可高枕无忧了。
假设有一个坏人，搞了一个假的网银的站点，然后诱骗你上这个站点。
假设你又比较单纯，一不留神，就把你的帐号，口令都输入进去了。那这个坏蛋的阴谋就得逞了。
为了防止坏人这么干，HTTPS 协议除了有加密的机制，还有一套证书的机制。通过证书来确保，某个站点确实就是某个站点。
有了证书之后，当你的浏览器在访问某个HTTPS网站时，会验证该站点上的CA证书（类似于验证介绍信的公章）。
如果浏览器发现该证书没有问题（证书被某个根证书信任、证书上绑定的域名和该网站的域名一致、证书没有过期），
那么页面就直接打开，否则的话，浏览器会给出一个警告，告诉你该网站的证书存在某某问题，是否继续访问该站点。
```



## 19.SSL原理
```plain
要想弄明白SSL认证原理，首先要对CA有有所了解，它在SSL认证过程中有非常重要的作用。
说白了，CA就是一个组织，专门为网络服务器颁发证书的，国际知名的CA机构有VeriSign、Symantec，国内的有GlobalSign。
每一家CA都有自己的根证书，用来对它所签发过的服务器端证书进行验证。

如果服务器提供方想为自己的服务器申请证书，它就需要向CA机构提出申请。
服务器提供方向CA提供自己的身份信息，CA判明申请者的身份后，就为它分配一个公钥，
并且CA将该公钥和服务器身份绑定在一起，并为之签字，这就形成了一个服务器端证书。

如果一个用户想鉴别另一个证书的真伪，他就用CA的公钥对那个证书上的签字进行验证，一旦验证通过，该证书就被认为是有效的。
证书实际是由证书签证机关（CA）签发的对用户的公钥的认证。

证书的内容包括：电子签证机关的信息、公钥用户信息、公钥、权威机构的签字和有效期等等。
目前，证书的格式和验证方法普遍遵循X.509国际标准。
```



### #申请证书过程
```plain
首先要有一个CA根证书，然后用CA根证书来签发用户证书。
用户进行证书申请：
1. 先生成一个私钥
2. 用私钥生成证书请求(证书请求里应含有公钥信息)
3. 利用证书服务器的CA根证书来签发证书

这样最终拿到一个由CA根证书签发的证书，其实证书里仅有公钥，而私钥是在用户手里的。
```



### SSL工作流程（单向）
```plain
1.客户端say hello 服务端
2.服务端将证书、公钥等发给客户端
3.客户端CA验证证书，成功继续、不成功弹出选择页面
4.客户端告知服务端所支持的加密算法
5.服务端选择最高级别加密算法明文通知客户端
6.客户端生成随机对称密钥key，使用服务端公钥加密发送给服务端
7.服务端使用私钥解密，获取对称密钥key
8.后续客户端与服务端使用该密钥key进行加密通信
```



### SSL工作流程（双向）
单向认证，仅仅是客户端需要检验服务端证书是否是正确的，而服务端不会检验客户端证书是否是正确的。 双向认证，指客户端验证服务器端证书，而服务器也需要通过CA的公钥证书来验证客户端证书。



双向验证的过程：



```plain
1.客户端say hello 服务端
2.服务端将证书、公钥等发给客户端
3.客户端CA验证证书，成功继续、不成功弹出选择页面
4.客户端将自己的证书和公钥发送给服务端
5.服务端验证客户端证书，如不通过直接断开连接
6.客户端告知服务端所支持的加密算法
7.服务端选择最高级别加密算法使用客户端公钥加密后发送给客户端
8.客户端收到后使用私钥解密并生成随机对称密钥key，使用服务端公钥加密发送给服务端
9.服务端使用私钥解密，获取对称密钥key
10.后续客户端与服务端使用该密钥key进行加密通信
```



## 20.自制ca证书
### 生成CA根证书
```shell
mkdir -p /etc/pki/ca_test //创建CA更证书的目录

cd /etc/pki/ca_test

mkdir root server client newcerts  //创建几个相关的目录

echo 01 > serial   //定义序列号为01

echo 01 > crlnumber  //定义crl号为01

touch index.txt  //创建index.txt

cd ..

vi tls/openssl.cnf  //改配置文件
default_ca     = CA_default 改为 default_ca     = CA_test
[ CA_default ] 改为 [ CA_test ]
dir             = /etc/pki/CA  改为  dir             = /etc/pki/ca_test
certificate	= $dir/cacert.pem  改为 certificate	= $dir/root/ca.crt
private_key	= $dir/private/cakey.pe 改为  private_key	= $dir/root/ca.key

openssl genrsa -out /etc/pki/ca_test/root/ca.key  #生成私钥

openssl req -new -key /etc/pki/ca_test/root/ca.key -out /etc/pki/ca_test/root/ca.csr   
#生成请求文件，会让我们填写一些指标,这里要注意：如果在这一步填写了相应的指标，
#比如Country Name、State or Province Name、hostname。
Country Name (2 letter code) [XX]:
State or Province Name (full name) []:bj
Locality Name (eg, city) [Default City]:bj
Organization Name (eg, company) [Default Company Ltd]:kehua
Organizational Unit Name (eg, section) []:test
Common Name (eg, your name or your server's hostname) []:www.1.com
Email Address []:liyedong@kehua.com
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:123456
An optional company name []:kehua

openssl x509 -req -days 3650 -in /etc/pki/ca_test/root/ca.csr -signkey /etc/pki/ca_test/root/ca.key -out /etc/pki/ca_test/root/ca.crt 
#生成crt文件
```



### 生成server端证书
```shell
cd /etc/pki/ca_test/server

openssl genrsa -out server.key   #生成私钥文件

openssl req -new -key server.key -out server.csr#生成证书请求文件，填写信息需要和ca.csr中的Organization Name保持一致

openssl ca -in server.csr -cert /etc/pki/ca_test/root/ca.crt -keyfile /etc/pki/ca_test/root/ca.key -out server.crt -days 3650  
#用根证书签名server.csr，最后生成公钥文件server.crt，此步骤会有两个地方需要输入y
Sign the certificate? [y/n]:y
1 out of 1 certificate requests certified, commit? [y/n]y
```



### 生成客户端证书
```shell
#如果做ssl的双向认证，还需要给客户端生成一个证书，步骤和上面的基本一致
cd /etc/pki/ca_test/client

openssl genrsa -out  client.key  #生成私钥文件

openssl req -new  -key client.key -out client.csr  #生成请求文件，填写信息需要和ca.csr中的Organization Name保持一致

openssl ca -in client.csr -cert /etc/pki/ca_test/root/ca.crt -keyfile /etc/pki/ca_test/root/ca.key -out client.crt -days 3650 
#签名client.csr, 生成client.crt，此步如果出现
failed to update database
TXT_DB error number 2

需执行：
sed -i 's/unique_subject = yes/unique_subject = no/' /etc/pki/ca_test/index.txt.attr

#执行完，再次重复执行签名client.csr那个操作
```



## 21.Nginx配置SSL
### Nginx配置示例（单向）
```shell
./configure --prefix=/usr/local/nginx --with-http_ssl_module 
#出现错误
#安装
yum -y install openssl openssl-devel
./configure --prefix=/usr/local/nginx --with-http_ssl_module 
make install
```



```nginx
cp /etc/pki/ca_test/server/server.* /usr/local/nginx/conf/
server{
    listen 443 ssl;
    server_name www.1.com;
    root /data/wwwroot/www.1.com;
    index index.html index.htm;
    access_log /tmp/log;
    ssl_certificate server.crt;
    ssl_certificate_key server.key;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers ALL:!DH:!EXPORT:!RC4:+HIGH:+MEDIUM:!eNULL;
    ssl_prefer_server_ciphers on;
    location /admin/
    {
        auth_basic "Auth";
        auth_basic_user_file /usr/local/nginx/conf/htpasswd;
    }
}
```







#### 配置说明
```plain
1. 443端口为ssl监听端口。
2. ssl on表示打开ssl支持。
3. ssl_certificate指定crt文件所在路径，如果写相对路径，必须把该文件和nginx.conf文件放到一个目录下。
4. ssl_certificate_key指定key文件所在路径。
5. ssl_protocols指定SSL协议。
6. ssl_ciphers配置ssl加密算法，多个算法用:分隔，ALL表示全部算法，!表示不启用该算法，+表示将该算法排到最后面去。
7. ssl_prefer_server_ciphers 如果不指定默认为off，当为on时，在使用SSLv3和TLS协议时，服务器加密算法将优于客户端加密算法。
```



### Nginx配置双向认证
```nginx
cp /etc/pki/ca_test/root/ca.crt /usr/local/nginx/conf/
配置示例：
server{
    listen 443 ssl;
    server_name www.1.com;
    root /data/wwwroot/www.1.com;
    index index.html index.htm;
    ssl_certificate server.crt;
    ssl_certificate_key server.key;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers ALL:!DH:!EXPORT:!RC4:+HIGH:+MEDIUM:!eNULL;
    ssl_prefer_server_ciphers on;
    ssl_client_certificate ca.crt;
    ssl_verify_client on;
    location /admin/
    {
        auth_basic "Auth";
        auth_basic_user_file /usr/local/nginx/conf/htpasswd;
    }
}
```







#### 客户端（浏览器）操作
```nginx
如果不进行以下操作，浏览器会出现400错误。400 Bad Request（No required SSL certificate was sent）
首先需要将client.key转换为pfx(p12)格式

cd /etc/pki/ca_test/client
openssl pkcs12 -export -inkey client.key -in client.crt -out client.pfx 
123456
#这一步需要输入一个自定义密码，一会在windows上安装的时候要用到，需要记一下。

然后将client.pfx拷贝到windows下，双击即可安装。
在chrome浏览器中可以查看到该证书
```











## 22.Nginx的错误日志
```plain
Nginx错误日志平时不用太关注，但是一旦出了问题，就需要借助错误日志来判断问题所在。

配置参数格式：error_log /path/to/log level;
```



### Nginx错误日志级别
```plain
常见的错误日志级别有debug | info | notice | warn | error | crit | alert | emerg
级别越高记录的信息越少，如果不定义，默认级别为error.

它可以配置在main、http、server、location段里。

如果在配置文件中定义了两个error_log，在同一个配置段里的话会产生冲突，所以同一个段里只允许配置一个error_log。
但是，在不同的配置段中出现是没问题的。
```



### Nginx错误日志示例
```nginx
error_log  /var/log/nginx/error.log crit;
最好每一个server配置一个错误日志文件 可以方便定位错误，当server段的错误日志配置后，发生错误时就不会再向这个错误日志文件写入日志/usr/local/nginx/logs/error.log
如果要想彻底关闭error_log，需要这样配置
error_log /dev/null;
```



## 23.Nginx访问日志配置
```nginx
web服务器的访问日志是非常重要的，我们可以通过访问日志来分析用户的访问情况，
也可以通过访问日志发现一些异常访问，比如cc攻击。

格式： access_log /path/to/logfile format;

access_log可以配置到http, server, location配置段中。
```



### 配置示例
```nginx
server 
{
    listen 80;
    server_name www.aminglinux.com;
    root /data/wwwroot/www.aminglinux.com;
    index index.html index.php;
    access_log /data/logs/www.aminglinux.com_access.log;
}
说明：若不指定log_format，则按照默认的格式写日志。
```



## 24.Nginx访问日志格式
```plain
Nginx访问日志可以设置自定义的格式，来满足特定的需求。
```



### 访问日志格式示例
```nginx
示例1
    log_format combined_realip '$remote_addr $http_x_forwarded_for [$time_local]'
    '$host "$request_uri" $status'
    '"$http_referer" "$http_user_agent"';

示例2
    log_format main '$remote_addr [$time_local] '
    '$host "$request_uri" $status "$request"'
    '"$http_referer" "$http_user_agent" "$request_time"';

若不配置log_format或者不在access_log配置中指定log_format，则默认格式为：
    '$remote_addr - $remote_user [$time_local] "$request" '
    '$status $body_bytes_sent "$http_referer" '
    '"$http_user_agent";
```



### 配置实例
```nginx
#server端配置 A.conf
log_format combined_realip '$remote_addr $http_x_forwarded_for [$time_local]'
    '$host "$request_uri" $status'
    '"$http_referer" "$http_user_agent"';#定义了一个名为combined_realip的日志格式
server{
    listen 99;
    server_name localhost;
    root /usr/local/nginx/html;
    index index.html index.php;
    access_log /data/logs/localhost.log combined_realip;
}

#代理端配置 B.conf
server
{
    listen 8080;
    server_name localhost;
    location /
    {
        proxy_pass http://192.168.107.254:99/;
        proxy_set_header Host   $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}


tail -f /data/logs/localhost.log
192.168.107.254 192.168.107.1 [23/Aug/2023:09:28:18 +0800]192.168.107.254 "/" 200"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
192.168.107.254 192.168.107.1 [23/Aug/2023:09:28:18 +0800]192.168.107.254 "/favicon.ico" 404"http://192.168.107.254:8080/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
192.168.107.254 192.168.107.1 [23/Aug/2023:09:28:19 +0800]192.168.107.254 "/" 304"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
192.168.107.254 192.168.107.1 [23/Aug/2023:09:28:20 +0800]192.168.107.254 "/" 304"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
192.168.107.1 - [23/Aug/2023:09:29:15 +0800]192.168.107.254 "/" 304"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
192.168.107.254 192.168.107.1 [23/Aug/2023:09:29:36 +0800]192.168.107.254 "/" 304"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
```



### 常见变量
| 变量 | 说明 |
| --- | --- |
| $time_local | 通用日志格式下的本地时间；（服务器时间） |
| $remote_addr | 客户端（用户）IP地址 |
| $status | 请求状态码，如200，404，301，302等 |
| $body_bytes_sent | 发送给客户端的字节数，不包括响应头的大小 |
| $bytes_sent | 发送给客户端的总字节数 |
| $request_length | 请求的长度（包括请求行，请求头和请求正文） |
| $request_time | 请求处理时间，单位为秒，小数的形式 |
| $upstream_addr | 集群轮询地址 |
| $upstream_response_time | 指从Nginx向后端（php-cgi)建立连接开始到接受完数据然后关闭连接为止的时间 |
| $remote_user | 用来记录客户端用户名称 |
| $request | 请求方式（GET或者POST等）+URL（包含 |
| $http_user_agent | 用户浏览器标识 |
| $http_host | 请求的url地址（目标url地址）的host |
| $host | 等同于$http_host |
| $http_referer | 来源页面，即从哪个页面转到本页，如果直接在浏览器输入网址来访问，则referer为空 |
| $uri | 请求中的当前URI(不带请求参数，参数位于 |
| $document_uri | 等同于$uri |
| $request_uri | 比 |
| $http_x_forwarded_for | 如果使用了代理，这个参数会记录代理服务器的ip和客户端的ip |


## 25.Nginx访问日志过滤
```plain
一个网站，会包含很多元素，尤其是有大量的图片、js、css等静态元素。
这样的请求其实可以不用记录日志。
```



##### 配置示例
```nginx
location ~* ^.+\.(gif|jpg|png|css|js)$ 
{
    access_log off;
}

或
location ~* ^.+\.(gif|jpg|png|css|js)$                                      
{
    access_log /dev/null;
}

vi A.conf
    log_format combined_realip '$remote_addr $http_x_forwarded_for [$time_local]'
        '$host "$request_uri" $status'
        '"$http_referer" "$http_user_agent"';#定义了一个名为combined_realip的日志格式
    server{
        listen 99;
        server_name localhost;
        root /usr/local/nginx/html;
        index index.html index.php;
        location ~* ^.+\.(gif|jpg|png|css|js)$
        {
            access_log off;
        }
        access_log /data/logs/localhost.log combined_realip;
    }
tail -f /data/logs/localhost.log
192.168.107.254 192.168.107.1 [23/Aug/2023:09:29:36 +0800]192.168.107.254 "/" 304"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
192.168.107.254 192.168.107.1 [23/Aug/2023:09:44:19 +0800]192.168.107.254 "/1.css1" 404"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
192.168.107.254 192.168.107.1 [23/Aug/2023:09:44:35 +0800]192.168.107.254 "/1.css2" 404"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
```



## 26.Nginx访问日志切割
```plain
如果任由访问日志写下去，日志文件会变得越来越大，甚至是写满磁盘。
所以，我们需要想办法把日志做切割，比如每天生成一个新的日志，旧的日志按规定时间删除即可。

实现日志切割可以通过写shell脚本或者系统的日志切割机制实现。
```



### shell脚本切割Nginx日志
```shell
vi log_rotate.sh

#切割脚本内容：
#!/bin/bash
logdir=/data/logs/  #定义日志路径
prefix=`date -d "-1 day" +%y%m%d`  #定义切割后的日志前缀
cd $logdir
for f in `ls *.log`
do
mv $f $f-$prefix  #把日志改名
done
/usr/local/nginx/sbin/nginx -s reload #/bin/kill -USR1 $(cat /usr/local/nginx/logs/nginx.pid 2>/dev/null) 2>/dev/null 两句命令效果一样
bzip2 *$prefix  #压缩日志
find . -type f -mtime +180 |xargs /bin/rm -f  #删除超过180天的老日志



sh -x log_rotate.sh #执行脚本并且查看详细信息


#添加到每日工作任务中
crontab -e
0 0 * * * /bin/bash /usr/local/nginx/sbin/log_rotate.sh
```



### 系统日志切割机制
```shell
在/etc/logrotate.d/下创建nginx文件，内容为：
vi /etc/logrotate.d/nginx
/data/logs/*log {
    daily
    rotate 30
    missingok
    notifempty
    compress
    sharedscripts
    postrotate
        /bin/kill -USR1 $(cat /usr/local/nginx/logs/nginx.pid 2>/dev/null) 2>/dev/null 
    endscript
}

说明：
1 nginx日志在/data/logs/目录下面，日志名字以log结尾
2 daily表示每天切割
3 rotate 30表示日志保留30天
4 missingok表示忽略错误
5 notifempty表示如果日志为空，不切割
6 compress表示压缩
7 sharedscripts和endscript中间可以引用系统的命令
8 postrotate表示当切割之后要执行的命令
```



## 27.Nginx配置参数优化
```plain
Nginx作为高性能web服务器，即使不特意调整配置参数也可以处理大量的并发请求。
以下的配置参数是借鉴网上的一些调优参数，仅作为参考，不见得适于你的线上业务。
```



### worker进程
+ worker_processes



```plain
该参数表示启动几个工作进程，建议和本机CPU核数保持一致，每一核CPU处理一个进程。
```



+ worker_rlimit_nofile



```plain
它表示Nginx最大可用的文件描述符个数，需要配合系统的最大描述符，建议设置为102400。
还需要在系统里执行ulimit -n 102400才可以。这个配置只是暂时的。
也可以直接修改配置文件/etc/security/limits.conf修改
增加：
* soft nofile 655350
* hard nofile 655350
```



+ worker_connections



```plain
该参数用来配置每个Nginx worker进程最大处理的连接数，这个参数也决定了该Nginx服务器最多能处理多少客户端请求
（worker_processes * worker_connections)，建议把该参数设置为10240，不建议太大。
```



### http和tcp连接
+ use epoll



```plain
使用epoll模式的事件驱动模型，该模型为Linux系统下最优方式。
```



+ multi_accept on



```plain
使每个worker进程可以同时处理多个客户端请求。
```



+ sendfile on



```plain
使用内核的FD文件传输功能，可以减少user mode和kernel mode的切换，从而提升服务器性能。
```



+ tcp_nopush on



```plain
当tcp_nopush设置为on时，会调用tcp_cork方法进行数据传输。
使用该方法会产生这样的效果：当应用程序产生数据时，内核不会立马封装包，而是当数据量积累到一定量时才会封装，然后传输。
```



+ tcp_nodelay on



```plain
不缓存data-sends（关闭 Nagle 算法），这个能够提高高频发送小数据报文的实时性。
(关于Nagle算法)
【假如需要频繁的发送一些小包数据，比如说1个字节，以IPv4为例的话，则每个包都要附带40字节的头，
也就是说，总计41个字节的数据里，其中只有1个字节是我们需要的数据。
为了解决这个问题，出现了Nagle算法。
它规定：如果包的大小满足MSS，那么可以立即发送，否则数据会被放到缓冲区，等到已经发送的包被确认了之后才能继续发送。
通过这样的规定，可以降低网络里小包的数量，从而提升网络性能。】
```



+ keepalive_timeout



```plain
定义长连接的超时时间，建议30s，太短或者太长都不一定合适，当然，最好是根据业务自身的情况来动态地调整该参数。
```



+ keepalive_requests



```plain
定义当客户端和服务端处于长连接的情况下，每个客户端最多可以请求多少次，可以设置很大，比如50000.
```



+ reset_timeout_connection on



```plain
设置为on的话，当客户端不再向服务端发送请求时，允许服务端关闭该连接。
```



+ client_body_timeout



```plain
客户端如果在该指定时间内没有加载完body数据，则断开连接，单位是秒，默认60，可以设置为10。
```



+ send_timeout



```plain
这个超时时间是发送响应的超时时间，即Nginx服务器向客户端发送了数据包，但客户端一直没有去接收这个数据包。
如果某个连接超过send_timeout定义的超时时间，那么Nginx将会关闭这个连接。单位是秒，可以设置为3。
```



### buffer和cache(以下配置都是针对单个请求)
+ client_body_buffer_size



```plain
当客户端以POST方法提交一些数据到服务端时，会先写入到client_body_buffer中，如果buffer写满会写到临时文件里，建议调整为128k。
```



+ client_max_body_size



```plain
浏览器在发送含有较大HTTP body的请求时，其头部会有一个Content-Length字段，client_max_body_size是用来限制Content-Length所示值的大小的。
这个限制body的配置不用等Nginx接收完所有的HTTP包体，就可以告诉用户请求过大不被接受。会返回413状态码。
例如，用户试图上传一个1GB的文件，Nginx在收完包头后，发现Content-Length超过client_max_body_size定义的值，
就直接发送413(Request Entity Too Large)响应给客户端。
将该数值设置为0，则禁用限制，建议设置为10m。
```



+ client_header_buffer_size



```plain
设置客户端header的buffer大小，建议4k。
```



+ large_client_header_buffers



```plain
对于比较大的header（超过client_header_buffer_size）将会使用该部分buffer，两个数值，第一个是个数，第二个是每个buffer的大小。
建议设置为4 8k
```



+ open_file_cache



```plain
该参数会对以下信息进行缓存：
打开文件描述符的文件大小和修改时间信息;
存在的目录信息;
搜索文件的错误信息（文件不存在无权限读取等信息）。
格式：open_file_cache max=size inactive=time;
max设定缓存文件的数量，inactive设定经过多长时间文件没被请求后删除缓存。
建议设置 open_file_cache max=102400 inactive=20s;
```



+ open_file_cache_valid



```plain
指多长时间检查一次缓存的有效信息。建议设置为30s。
```



+ open_file_cache_min_uses



```plain
open_file_cache指令中的inactive参数时间内文件的最少使用次数，
如,将该参数设置为1，则表示，如果文件在inactive时间内一次都没被使用，它将被移除。
建议设置为2。
```



### 压缩
```nginx
对于纯文本的内容，Nginx是可以使用gzip压缩的。使用压缩技术可以减少对带宽的消耗。
由ngx_http_gzip_module模块支持

配置如下：
gzip on; #开启gzip功能
gzip_min_length 1024; #设置请求资源超过该数值才进行压缩，单位字节
gzip_buffers 16 8k; #设置压缩使用的buffer大小，第一个数字为数量，第二个为每个buffer的大小
gzip_comp_level 6; #设置压缩级别，范围1-9,9压缩级别最高，也最耗费CPU资源
gzip_types text/plain application/x-javascript text/css application/xml image/jpeg image/gif image/png; #指定哪些类型的文件需要压缩
gzip_disable "MSIE 6\."; #IE6浏览器不启用压缩

测试：
du -sb /usr/local/nginx/html/1.css #查看字节大小 必须超过1024根据上面的设置
cat index.html >> 1.css
curl -I -H "Accept-Encoding: gzip, deflate" 192.168.107.254:8080/1.css
```



### 日志
+ 错误日志级别调高，比如crit级别，尽量少记录无关紧要的日志。
+ 对于访问日志，如果不要求记录日志，可以关闭，
+ 静态资源的访问日志关闭



### 静态文件过期
```nginx
#对于静态文件，需要设置一个过期时间，这样可以让这些资源缓存到客户端浏览器，
#在缓存未失效前，客户端不再向服务期请求相同的资源，从而节省带宽和资源消耗。

#配置示例如下：
location ~* ^.+\.(gif|jpg|png|css|js)$                                      
{
    expires 1d; #1d表示1天，也可以用24h表示一天。
}
```



### 作为代理服务器
```nginx
Nginx绝大多数情况下都是作为代理或者负载均衡的角色。
因为前面章节已经介绍过以下参数的含义，在这里只提供对应的配置参数：
http
{
    proxy_cache_path /data/nginx_cache/ levels=1:2 keys_zone=my_zone:10m inactive=300s max_size=5g;
    ...;
    server
    {
    proxy_buffering on;
    proxy_buffer_size 4k;
    proxy_buffers 2 4k;
    proxy_busy_buffers_size 4k;
    proxy_temp_path /tmp/nginx_proxy_tmp 1 2;
    proxy_max_temp_file_size 20M;
    proxy_temp_file_write_size 8k;
    
    location /
    {
        proxy_cache my_zone;
        ...;
    }
    }
}
```



### SSL优化
+ 适当减少worker_processes数量，因为ssl功能需要使用CPU的计算。
+ 使用长连接，因为每次建立ssl会话，都会耗费一定的资源（加密、解密）
+ 开启ssl缓存，简化服务端和客户端的“握手”过程。



```nginx
ssl_session_cache   shared:SSL:10m; //缓存为10M
ssl_session_timeout 10m; //会话超时时间为10分钟
```



## 28.调整Linux内核参数
```plain
作为高性能WEB服务器，只调整Nginx本身的参数是不行的，因为Nginx服务依赖于高性能的操作系统。
以下为常见的几个Linux内核参数优化方法。
```



+ 1 net.ipv4.tcp_max_tw_buckets



```plain
对于tcp连接，服务端和客户端通信完后状态变为timewait，假如某台服务器非常忙，连接数特别多的话，那么这个timewait数量就会越来越大。
毕竟它也是会占用一定的资源，所以应该有一个最大值，当超过这个值，系统就会删除最早的连接，这样始终保持在一个数量级。
这个数值就是由net.ipv4.tcp_max_tw_buckets这个参数来决定的。
CentOS7系统，你可以使用sysctl -a |grep tw_buckets来查看它的值，默认为32768，
你可以适当把它调低，比如调整到8000，毕竟这个状态的连接太多也是会消耗资源的。
但你不要把它调到几十、几百这样，因为这种状态的tcp连接也是有用的，
如果同样的客户端再次和服务端通信，就不用再次建立新的连接了，用这个旧的通道，省时省力。
```



+ 2 net.ipv4.tcp_tw_recycle = 1



```plain
该参数的作用是快速回收timewait状态的连接。上面虽然提到系统会自动删除掉timewait状态的连接，但如果把这样的连接重新利用起来岂不是更好。
所以该参数设置为1就可以让timewait状态的连接快速回收，它需要和下面的参数配合一起使用。
```



+ 3 net.ipv4.tcp_tw_reuse = 1



```plain
该参数设置为1，将timewait状态的连接重新用于新的TCP连接，要结合上面的参数一起使用。
```



+ 4 net.ipv4.tcp_syncookies = 1



```plain
tcp三次握手中，客户端向服务端发起syn请求，服务端收到后，也会向客户端发起syn请求同时连带ack确认，
假如客户端发送请求后直接断开和服务端的连接，不接收服务端发起的这个请求，服务端会重试多次，
这个重试的过程会持续一段时间（通常高于30s），当这种状态的连接数量非常大时，服务器会消耗很大的资源，从而造成瘫痪，
正常的连接进不来，这种恶意的半连接行为其实叫做syn flood攻击。
设置为1，是开启SYN Cookies，开启后可以避免发生上述的syn flood攻击。
开启该参数后，服务端接收客户端的ack后，再向客户端发送ack+syn之前会要求client在短时间内回应一个序号，
如果客户端不能提供序号或者提供的序号不对则认为该客户端不合法，于是不会发ack+syn给客户端，更涉及不到重试。
```



+ 5 net.ipv4.tcp_max_syn_backlog



```plain
该参数定义系统能接受的最大半连接状态的tcp连接数。客户端向服务端发送了syn包，服务端收到后，会记录一下，
该参数决定最多能记录几个这样的连接。在CentOS7，默认是256，当有syn flood攻击时，这个数值太小则很容易导致服务器瘫痪，
实际上此时服务器并没有消耗太多资源（cpu、内存等），所以可以适当调大它，比如调整到30000。
```



+ 6 net.ipv4.tcp_syn_retries



```plain
该参数适用于客户端，它定义发起syn的最大重试次数，默认为6，建议改为2。
```



+ 7 net.ipv4.tcp_synack_retries



```plain
该参数适用于服务端，它定义发起syn+ack的最大重试次数，默认为5，建议改为2，可以适当预防syn flood攻击。
```



+ 8 net.ipv4.ip_local_port_range



```plain
该参数定义端口范围，系统默认保留端口为1024及以下，以上部分为自定义端口。这个参数适用于客户端，
当客户端和服务端建立连接时，比如说访问服务端的80端口，客户端随机开启了一个端口和服务端发起连接，
这个参数定义随机端口的范围。默认为32768    61000，建议调整为1025 61000。
```



+ 9 net.ipv4.tcp_fin_timeout



```plain
tcp连接的状态中，客户端上有一个是FIN-WAIT-2状态，它是状态变迁为timewait前一个状态。
该参数定义不属于任何进程的该连接状态的超时时间，默认值为60，建议调整为6。
```



+ 10 net.ipv4.tcp_keepalive_time



```plain
tcp连接状态里，有一个是established状态，只有在这个状态下，客户端和服务端才能通信。正常情况下，当通信完毕，
客户端或服务端会告诉对方要关闭连接，此时状态就会变为timewait，如果客户端没有告诉服务端，
并且服务端也没有告诉客户端关闭的话（例如，客户端那边断网了），此时需要该参数来判定。
比如客户端已经断网了，但服务端上本次连接的状态依然是established，服务端为了确认客户端是否断网，
就需要每隔一段时间去发一个探测包去确认一下看看对方是否在线。这个时间就由该参数决定。它的默认值为7200秒，建议设置为30秒。
```



+ 11 net.ipv4.tcp_keepalive_intvl



```plain
该参数和上面的参数是一起的，服务端在规定时间内发起了探测，查看客户端是否在线，如果客户端并没有确认，
此时服务端还不能认定为对方不在线，而是要尝试多次。该参数定义重新发送探测的时间，即第一次发现对方有问题后，过多久再次发起探测。
默认值为75秒，可以改为3秒。
```



+ 12 net.ipv4.tcp_keepalive_probes



```plain
第10和第11个参数规定了何时发起探测和探测失败后再过多久再发起探测，但并没有定义一共探测几次才算结束。
该参数定义发起探测的包的数量。默认为9，建议设置2。
```



### 设置和范例
```shell
在Linux下调整内核参数，可以直接编辑配置文件/etc/sysctl.conf，然后执行sysctl -p命令生效
vi /etc/sysctl.conf
结合以上分析的各内核参数，范例如下
net.ipv4.tcp_fin_timeout = 6
net.ipv4.tcp_keepalive_time = 30
net.ipv4.tcp_max_tw_buckets = 8000
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 30000
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_synack_retries = 2
net.ipv4.ip_local_port_range = 1025 61000
net.ipv4.tcp_keepalive_intvl = 3
net.ipv4.tcp_keepalive_probes = 2


sysctl -p
```



## 29.监控nginx
```plain
top
ps
netstat
ss
lsof
tcpdump -nn
tcpdump -i eth0
日志
```



## 30.配置Nginx状态
```shell
#Nginx有内置一个状态页，需要在编译的时候指定参数--with-http_stub_status_module参数方可打开。
#也就是说，该功能是由http_stub_status_module模块提供，默认没有加载。
 ./configure --with-http_stub_status_module --with-http_ssl_module --prefix=/usr/local/nginx
 make install
```



### Nginx配置文件示例
```nginx
log_format combined_realip '$remote_addr $http_x_forwarded_for [$time_local]'
    '$host "$request_uri" $status'
    '"$http_referer" "$http_user_agent"';#定义了一个名为combined_realip的日志格式
server{
    listen 99;
    server_name localhost;
    root /usr/local/nginx/html;
    index index.html index.php;
    error_log /data/logs/localhost.err.log debug;
    location ~* ^.+\.(gif|jpg|png|css|js)$
    {
        expires 1d; #1d表示1天，也可以用24h表示一天。
        access_log off;
    }
    location /status/#加上这个location模块
    {
        stub_status on;
        access_log off;
        allow 127.0.0.1;
        allow 192.168.107.0/24;
        deny all;
    }

    access_log /data/logs/localhost.acc.log combined_realip;
}
```







### 配置说明
+ location /status/这样当访问/status/时即可访问到状态页内容。
+ stub_status on即打开了状态页。
+ access_log off不记录日志
+ allow和deny只允许指定IP和IP段访问，因为这个页面需要保护起来，并不公开，当然也可以做用户认证。



### 测试和结果说明
```plain
测试命令：curl -x127.0.0.1:80 192.168.107.254：8080/status/

结果如下：
Active connections: 1 
server accepts handled requests
 11 11 11 
Reading: 0 Writing: 1 Waiting: 0 

说明：
active connections – 活跃的连接数量
server accepts handled requests — 总共处理的连接数、成功创建的握手次数、总共处理的请求次数
需要注意，一个连接可以有多次请求。
reading — 读取客户端的连接数.
writing — 响应数据到客户端的数量
waiting — 开启 keep-alive 的情况下,这个值等于 active – (reading+writing), 意思就是 Nginx 已经处理完正在等候下一次请求指令的驻留连接.
```



## 31.Nginx架构-LNMP
Linux：Linux 操作系统



Nginx：Web 服务器



MariaDB：数据库



PHP：脚本语言



```nginx
配置如下（在server部分添加）：
    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass unix:/tmp/php-fcgi.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

配置说明：
1 fastcgi_params文件在/usr/local/nginx/conf/下面，其内容为fastcgi相关的变量
2 fastcgi_pass后面跟的是php-fpm服务监听地址，可以是IP:PORT，也可以是unix socket地址，也支持upstream的地址
3 fastcgi_index定义索引页，如果在server内其他部分有定义index参数，该配置可以忽略
4 fastcgi_param这行其实可以在fastcgi_params文件里面定义SCRIPT_FILENAME变量，这个变量如果不定义，php的请求是没办法访问的。
```



### 安装MySQL
执行以下命令，查看系统中是否已安装 MariaDB。



```plain
rpm -qa | grep -i mariadb
```



返回结果类似如下内容，则表示已存在 MariaDB。







为避免安装版本不同造成冲突，请执行以下命令移除已安装的 MariaDB。



```plain
 yum -y remove mariadb-5.5.68-1.el7.x86_64 mariadb-server-5.5.68-1.el7.x86_64 mariadb-libs-5.5.68-1.el7.x86_64
```



若返回结果为空，则说明未预先安装，则执行下一步。



2. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `MariaDB.repo` 文件。



```plain
vi /etc/yum.repos.d/MariaDB.repo
```



3. 按 **i** 切换至编辑模式，写入以下内容，添加 MariaDB 软件库。



**说明**



以下配置使用了腾讯云镜像源，腾讯云镜像源同步 MariaDB 官网源进行更新，可能会出现 MariaDB 10.4 版本源失效问题（本文以在 CentOS 7.6 上安装 MariaDB 10.4.22 版本为例），您可前往 [MariaDB 官网](https://downloads.mariadb.org) 获取其他版本及操作系统的 MariaDB 软件库安装信息。



若您的云服务器使用了 [内网服务](https://cloud.tencent.com/document/product/213/5225)，则可以将 `mirrors.cloud.tencent.com` 替换为 `mirrors.tencentyun.com` 内网地址，内网流量不占用公网流量且速度更快。



```bash
# MariaDB 10.4 CentOS repository list - created 2019-11-05 11:56 UTC
# http://downloads.mariadb.org/mariadb/repositories/
[mariadb]
name = MariaDB
baseurl = https://mirrors.cloud.tencent.com/mariadb/yum/10.4/centos7-amd64
gpgkey=https://mirrors.cloud.tencent.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck=1
```



4. 按 **Esc**，输入 **:wq**，保存文件并返回。 
5. 执行以下命令，安装 MariaDB。此步骤耗时较长，请关注安装进度，等待安装完毕。



```plain
yum -y install MariaDB-client MariaDB-server
```



6. 执行以下命令，启动 MariaDB 服务。



```plain
systemctl start mariadb
```



7. 执行以下命令，设置 MariaDB 为开机自启动。



```plain
systemctl enable mariadb
```



8. 执行以下命令，验证 MariaDB 是否安装成功。



```plain
mysql
```



显示结果如下，则成功安装



9. 执行以下命令，退出 MariaDB。



```plain
q
```



### 安装php
1. 依次执行以下命令，更新 yum 中 PHP 的软件源。

```plain
rpm -Uvh https://mirrors.cloud.tencent.com/epel/epel-release-latest-7.noarch.rpm
```



```plain
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```



```plain
2. 执行以下命令，安装 PHP 7.2 所需要的包。
```

```plain
yum -y install mod_php72w.x86_64 php72w-cli.x86_64 php72w-common.x86_64 php72w-mysqlnd php72w-fpm.x86_64
```

```plain
3. 执行以下命令，启动 PHP-FPM 服务。
```

```plain
systemctl start php-fpm
```

```plain
4. 执行以下命令，设置 PHP-FPM 服务为开机自启动。
```

```plain
systemctl enable php-fpm
```



### 安装 Nginx
1. 执行以下命令，在 `/etc/yum.repos.d/` 下创建 `nginx.repo` 文件。



```plain
vi /etc/yum.repos.d/nginx.repo
```



2. 按 **i** 切换至编辑模式，写入以下内容。



```bash
[nginx] 
name = nginx repo 
baseurl = https://nginx.org/packages/mainline/centos/7/$basearch/ 
gpgcheck = 0 
enabled = 1
```



3. 按 **Esc**，输入 **:wq**，保存文件并返回。 
4. 执行以下命令，安装 nginx。



```plain
yum install -y nginx
```



5. 执行以下命令，打开 `default.conf` 文件。



```plain
vim /usr/local/nginx/conf/vhost/A.conf
```



6. 按 **i** 切换至编辑模式，编辑 `default.conf` 文件。 
7. 找到 `server{...}`，并将 `server` 大括号中相应的配置信息替换为如下内容。用于取消对 IPv6 地址的监听，同时配置 Nginx，实现与 PHP 的联动。



```bash
log_format combined_realip '$remote_addr $http_x_forwarded_for [$time_local]'
    '$host "$request_uri" $status'
    '"$http_referer" "$http_user_agent"';#定义了一个名为combined_realip的日志格式
server{
    listen 99;
    server_name localhost;
    root /usr/local/nginx/html;
    index index.html index.php;
    error_log /data/logs/localhost.err.log debug;
    location ~* ^.+\.(gif|jpg|png|css|js)$
    {
        expires 1d; #1d表示1天，也可以用24h表示一天。
        access_log off;
    }
    location /status/
    {
        stub_status on;
        access_log off;
        allow 127.0.0.1;
        allow 192.168.107.0/24;
        deny all;
    }
    location ~ .php$ {
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }
    access_log /data/logs/localhost.acc.log combined_realip;
}
```



8. 按 **Esc**，输入 **:wq**，保存文件并返回。 
9. 执行以下命令启动 Nginx。



```plain
/usr/local/nginx/sbin/nginx -s reload
```



### 测试是否解析php文件
创建测试文件:



```shell
echo '<?php echo "hello world php世界上最好的语言"; ?>' > /usr/local/nginx/html/2.php
vi /usr/local/nginx/conf/vhost/A.conf
```



```nginx
server{
    ...
    location ~ .php$ {
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }
    ...
}
```



测试:



```plain
[root@localhost nginx]# curl localhost/2.php
测试php是否解析[root@localhost nginx]#
```







## 32.Nginx+Tomcat架构
```nginx
配置文件示例
server
{
    listen 80;
    server_name www.liyedong.com;
    
    location ~* "\.(jpg|png|jepg|js|css|xml|bmp|swf|gif|html)$"
    {
        root /data/wwwroot/www.liyedong.com/;
        access_log off;
        expire 7d;
    }
    
    location /
    {
        proxy_pass http://127.0.0.1:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP      $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

说明：
1 首先，把各种静态文件的请求分离出来，单独由nginx处理。
2 其他请求直接代理8080端口，即tomcat服务,也可使用负载均衡。
```



## 33.nginx+keepalived高可用架构
| ip | 192.168.107.254（eth0） | 192.168.107.253(eth0) | 192.168.107.188（虚拟ip） |
| :---: | :---: | :---: | :---: |
| 环境 | centos7+nginx+keepalived | centos7+nginx+keepalived |  |


### 1、keepalived
我们可以通过 keepalived 来实现 Nginx 的高可用，keepalived 是集群管理中保证集群高可用的一个服务软件，用来防止单点故障。Keepalived的作用是检测 web 服务器的状态，如果有一台 web 服务器死机或工作出现故障，Keepalived 将能检测到，并将有故障的 web 服务器从系统中剔除，当web服务器工作正常后 Keepalived 会自动将该 web 服务器加入到服务器群中。这些工作全部都会自动完成，不需要人工干涉，需要人工做的只是修复故障的web服务器。keepalived 可以理解为一个健康检查的软件。



高可用至少需要 2 台服务器，主备都得装上keepalived，当请求访问主服务器时，备份服务器会一直检查主服务器的状态。



keepalived 需要绑定一个虚拟地址 vip ( Virtual IP Address ) ，这个虚拟 ip 地址绑定在哪台服务器上请求就会发送到哪台服务器，一开始会绑定在主服务器上。







### 2、安装 keepalived
首先准备两台服务器，这里我们准备了两台虚拟机。分别在这两台服务器上安装 Nginx 和 keepalived。



安装 keepalived 使用 yum 方式直接安装即可，该方式会自动安装依赖。安装 keepalived 命令：



```shell
yum -y install keepalived
rpm -qa keepalived
cat /etc/keepalived/keepalived.conf	 #keepalived 配置文件
```



### 3、完成高可用配置
```plain
vi /etc/keepalived/keepalived.conf
```



```nginx
global_defs {
    notification_email {   # keepalived服务宕机异常出现的时候，发送通知邮件 可以是多个
      acassen@firewall.loc  #  收件人邮箱1
      failover@firewall.loc   #  收件人邮箱2
      sysadmin@firewall.loc   #  收件人邮箱3
    }
    notification_email_from Alexandre.Cassen@firewall.loc   #邮件发件人
    smtp_ server 192.168.107.254  #主服务器的ip地址。邮件服务器地址
    smtp_connect_timeout 30    # 超时时间
    router_id LVS_DEVEL    # 机器标识 局域网内唯一即可。 LVS_DEVEL这字段在/etc/hosts文件中看；通过它访问到主机
}
vrrp_script chk_http_ port {
    script "/usr/local/nginx/sbin/nginx_check.sh"   #检测脚本
    interval 2   # 检测脚本执行的间隔，即检测脚本每隔2s会自动执行一次
    weight 2  #权重，如果这个脚本检测为真，服务器权重+2
}
vrrp_instance VI_1 {
    state MASTER    # 指定keepalived的角色，MASTER为主，BACKUP为备。备份服务器上需将MASTER 改为BACKUP
    interface eth0  # 通信端口 通过ip addr可以看到，根据自己的机器配置
    virtual_router_id 51 # vrrp实例id  keepalived集群的实例id必须一致，即主、备机的virtual_router_id必须相同
    priority 100         #优先级，数值越大，获取处理请求的优先级越高。主、备机取不同的优先级，主机值较大，备份机值较小
    advert_int 1    #心跳间隔，默认为1s。keepalived多机器集群 通过心跳检测当前服务器是否还正常工作，如果发送心跳没反应，备份服务器就会立刻接管；
    authentication {     # 服务器之间通信密码
        auth type PASS   #设置验证类型和密码，MASTER和BACKUP必须使用相同的密码才能正常通信
        auth pass 1111
    }
    virtual_ipaddress { # 自定义虚拟IP。自定义的虚拟ip得根据真实ip设置。比如真实ip是192.168.91.138，那么虚拟ip可以设置为192.168.91.139~255，前面三个数得一致
        192.168.107.188 # 定义虚拟ip(VIP)，可多设，每行一个
    }
}
```



```plain
vi /etc/keepalived/keepalived.conf
```



```nginx
global_defs {
    notification_email {
      acassen@firewall.loc
      failover@firewall.loc
      sysadmin@firewall.loc
    }
    notification_email_from Alexandre.Cassen@firewall.loc
    smtp_ server 192.168.107.253    #备份服务器的ip地址
    smtp_connect_timeout 30
    router_id LVS_DEVEL    # LVS_DEVEL这字段在/etc/hosts文件中看；通过它访问到主机
}
vrrp_script chk_http_ port {
    script "/usr/local/nginx/sbin/nginx_check.sh"   #检测脚本
    interval 2   # (检测脚本执行的间隔)2s
    weight 2  #权重，如果这个脚本检测为真，服务器权重+2
}
vrrp_instance VI_1 {
    state BACKUP    # 指定keepalived的角色，MASTER为主，BACKUP为备。备份服务器上需将MASTER 改为BACKUP
    interface eth0 # 当前进行vrrp通讯的网络接口卡(当前centos的网卡) 用ifconfig查看你具体的网卡
    virtual_router_id 51 # 虚拟路由编号，主、备机的virtual_router_id必须相同
    priority 90         #优先级，数值越大，获取处理请求的优先级越高。主、备机取不同的优先级，主机值较大，备份机值较小
    advert_int 1    # 检查间隔，默认为1s(vrrp组播周期秒数)，每隔1s发送一次心跳
    authentication {     # 校验方式， 类型是密码，密码1111
        auth type PASS   #设置验证类型和密码，MASTER和BACKUP必须使用相同的密码才能正常通信
        auth pass 1111
    }
    virtual_ipaddress { # 虛拟ip
        192.168.107.188 # 定义虚拟ip(VIP)，可多设，每行一个
    }
}
```



```shell
#编辑脚本
vi /usr/local/nginx/sbin/nginx_check.sh
    #! /bin/bash
    #检测nginx是否启动了
    A=`ps -C nginx -no-header | wc - 1`
    if [ $A -eq 0];then    #如果nginx没有启动就启动nginx 
        /usr/local/nginx/sbin/nginx    #通过Nginx的启动脚本来重启nginx
        sleep 2
        if [`ps -C nginx --no-header| wc -1` -eq 0 ];then   #如果nginx重启失败，则下面就会停掉keepalived服务，进行VIP转移
            killall keepalived
        fi
    fi
```



### 4、开启服务并且测试
```shell
/usr/local/nginx/sbin/nginx -s stop   #因为已经启动了，所以先关闭 Nginx
/usr/local/nginx/sbin/nginx   #启动Nginx
ps -ef | grep nginx  #查看 Nginx 进程的状态
systemctl start keepalived.service    #启动keepalived
ps -ef | grep keepalived  #查看 keepalived 进程的状态
```



开始测试



```plain
ip addr #master启用了虚拟ip backup因为是备用机 所以会在master宕机后才绑定虚拟ip
```











编写两个不一样的php脚本来判断是否会访问到备用机



```plain
echo 'i am master' > /usr/local/nginx/html/testkeeplived.php
echo 'i am backup' > /usr/local/nginx/html/testkeeplived.php
```







```shell
systemctl stop keepalived.service   # 关闭keepalived
/usr/local/nginx/sbin/nginx -s stop  # 关闭Nginx
```











再次启动master主机服务观察backup备用机状态



```shell
/usr/local/nginx/sbin/nginx   #启动Nginx
systemctl start keepalived.service
```











## 34.nginx运维规范
```shell
vi /etc/init.d/nginx
```



```shell
#!/bin/bash
# chkconfig: - 30 21
# description: http service.
# Source Function Library
. /etc/init.d/functions
# Nginx Settings

NGINX_SBIN="/usr/local/nginx/sbin/nginx"
NGINX_CONF="/usr/local/nginx/conf/nginx.conf"
NGINX_PID="/usr/local/nginx/logs/nginx.pid"
RETVAL=0
prog="Nginx"

start() 
{
    echo -n $"Starting $prog: "
    mkdir -p /dev/shm/nginx_temp
    daemon $NGINX_SBIN -c $NGINX_CONF
    RETVAL=$?
    echo
    return $RETVAL
}

stop() 
{
    echo -n $"Stopping $prog: "
    killproc -p $NGINX_PID $NGINX_SBIN -TERM
    rm -rf /dev/shm/nginx_temp
    RETVAL=$?
    echo
    return $RETVAL
}

reload()
{
    echo -n $"Reloading $prog: "
    killproc -p $NGINX_PID $NGINX_SBIN -HUP
    RETVAL=$?
    echo
    return $RETVAL
}

restart()
{
    stop
    start
}

configtest()
{
    $NGINX_SBIN -c $NGINX_CONF -t
    return 0
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  reload)
        reload
        ;;
  restart)
        restart
        ;;
  configtest)
        configtest
        ;;
  *)
        echo $"Usage: $0 {start|stop|reload|restart|configtest}"
        RETVAL=1
esac

exit $RETVAL
```



```shell
chmod 700 /etc/init.d/nginx
/etc/init.d/nginx start
/etc/init.d/nginx stop
/etc/init.d/nginx restart
```



```plain
安装、升级（yum安装or源码安装、编译参数、安装路径等）
服务管理（启动脚本、重启、重载、启动用户）
配置规范
Log格式、路径、命名规则和切割策略
Pid路径
虚拟主机（默认虚拟主机、虚拟主机独立）
静态文件日志和过期缓存时间
防盗链
更改配置（使用自动化工具更改配置文件）
安全规范
后台地址加用户认证
可写目录禁止解析php
禁止访问.bak文件
```

