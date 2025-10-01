## <font style="color:rgb(51, 51, 51);">安装mariadb</font>
```plain
yum install mariadb-server -y
systemctl start mariadb.service && systemctl enable mariadb.service
mysql_secure_installation #安全初始化
mysql
create database snipeit;
grant all on snipeit.* to 'snipeit'@'%' identified by '123456';
flush privileges;
```

```plain
[root@localhost snipeit]# docker run --rm snipe/snipe-it
Please re-run this container with an environment variable $APP_KEY
An example APP_KEY you could use is:
base64:qIMcVCudpzczC+ozl0HGNb2v4X6vpAQGEdYnJRkXryA=

mkdir /snipeit
vi /snipeit/snipeit.env

# Mysql Parameters
MYSQL_PORT_3306_TCP_ADDR=192.168.107.56
MYSQL_PORT_3306_TCP_PORT=3306

MYSQL_DATABASE=snipeit
MYSQL_USER=snipeit
MYSQL_PASSWORD=123456

# Email Parameters
# - the hostname/IP address of your mailserver
MAIL_PORT_587_TCP_ADDR=smtp.whatever.com
#the port for the mailserver (probably 587, could be another)
MAIL_PORT_587_TCP_PORT=587
# the default from address, and from name for emails
MAIL_ENV_FROM_ADDR=youremail@yourdomain.com
MAIL_ENV_FROM_NAME=Your Full Email Name
# - pick 'tls' for SMTP-over-SSL, 'tcp' for unencrypted
MAIL_ENV_ENCRYPTION=tcp
# SMTP username and password
MAIL_ENV_USERNAME=your_email_username
MAIL_ENV_PASSWORD=your_email_password

# Snipe-IT Settings
APP_ENV=production
APP_DEBUG=false
APP_KEY=base64:qIMcVCudpzczC+ozl0HGNb2v4X6vpAQGEdYnJRkXryA=
APP_URL=http://127.0.0.1:80
APP_TIMEZONE=CST/Shanghai
APP_LOCALE=zh-CN



docker run -d -p 80:80 --name="snipeit"  --env-file=/usr/snipe-it-env.env --mount source=snipe-vol,dst=/var/lib/snipeit snipe/snipe-it
```

## <font style="color:rgb(51, 51, 51);">docker-compose安装</font>
```plain
https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-linux-x86_64
 mv docker-compose-linux-x86_64.docker-compose-linux-x86_64 docker-compose
chmod 755 docker-compose
docker-compose version
```

## <font style="color:rgb(51, 51, 51);">编写docker-compose &&启动容器</font>
```plain
version: "3"
services:
  snipeit:
    image: snipeit #镜像版本
    ports:
    - "80:80"
    container_name: snipeit
    volumes:
    - ./logs:/var/www/html/storage/logs
    - ./apache2.log:/var/log/apache2/
    env_file:
    - snipeit.env
    networks:
    - snipeit-backend
    restart: unless-stopped
    ulimits:
      nofile:
        soft: 1048576
        hard: 1048576
      nproc: 104857
volumes:
  db: {}
 
networks:
  snipeit-backend: {}
  
  
docker-compose up -d    #启动服务
```

  
 

