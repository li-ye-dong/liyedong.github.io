# <font style="color:rgb(51, 51, 51);"></font>
```plain
yum install gcc -v
yum install nginx -y
yum install mariadb-server -y
systemctl start mariadb.service
systemctl enable mariadb.service
mysql_secure_installation #安全初始化
mysql
create database chemex;
grant all on chemex.* to chemex@localhost identified by '123456';
flush privileges;
wget https://www.php.net/distributions/php-8.1.24.tar.gz
tar -zxvf php-8.1.24.tar.gz
cd php-8.1.24

./configure --prefix=/usr/local/php8.1 --with-config-file-path=/usr/local/php8.1 --with-config-file-scan-dir=/usr/local/php8.1/etc/php.d --disable-fileinfo --enable-bcmath --enable-shmop --enable-sysvsem --with-curl --enable-mbregex --enable-mbstring --enable-ftp --enable-pcntl --enable-sockets --enable-soap --with-pear --with-gettext --enable-calendar --with-openssl --enable-zts --enable-fpm --with-pdo-mysql=mysqlnd --with-zip --enable-gd

make
make install


第一个指令就是复制我们的 php.ini 文件到指定的配置目录下面，第二个指令就是创建一个软连接把 php 的执行档案到我们的运行目录下，当然我们也可以通过添加 PATH 的形式实现，但是这里就不多说了。
cp ./php.ini-production /usr/local/php8.1/etc/php.ini
ln -s /usr/local/php8.1/bin/php /usr/bin/php


php -v
yum install php-fpm
systemctl start php-fpm
systemctl enable php-fpm



cd /etc/nginx
grep -Ev '^$|#' nginx.conf.default >nginx.conf

[root@localhost nginx]# cat nginx.conf
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;
    include conf.d/*.conf; #包含conf.d下的.conf文件
}

cd conf.d
vi localhost.conf
server {
    listen       80;
    server_name  localhost;
    location / {
        root   html;
        index  index.html index.htm;
    }
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   html;
    }
}
systemctl reload nginx



php测试
mkdir /phphtmltest
echo '<?php echo "hello world php世界上最好的语言"; ?>' > /phphtmltest/test.php

vi localhost.conf
server {
    listen       80;
    server_name  localhost;
    root   /phphtmltest;
    index index.html index.php;
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
}


cd /etc/php-fpm.d
vi www.conf
...
;listen = /run/php-fpm/www.sock
listen = 127.0.0.1:9000
...
systemctl restart php-fpm
```

# <font style="color:rgb(51, 51, 51);"></font>
