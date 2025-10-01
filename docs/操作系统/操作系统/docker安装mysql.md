```shell
docker pull mysql:5.7 
docker images 
mkdir -p /home/service/mysql/data 
mkdir -p /home/service/mysql/conf/my.cnf 
vi /home/service/mysql/conf/my.cnf
[mysqld]
user=mysql
character-set-server=utf8
default_authentication_plugin=mysql_native_password
default-time_zone = '+8:00'
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
```



```shell
docker run -p 3306:3306 --name mysql -v /home/service/mysql/logs:/logs -v /home/service/mysql/data:/mysql_data -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7

docker exec -it mysql bash

mysql -uroot -p 

CREATE USER 'admin'@'%' IDENTIFIED BY '123456';

GRANT ALL ON *.* TO 'admin'@'%'; 

flush privileges; 
```

# Docker安装mysql
docker pull mysql:5.7   
docker images   
mkdir -p /home/service/mysql/data   
mkdir -p /home/service/mysql/conf  
cd /home/service/mysql/conf  
touch my.cnf  
将以下内容粘入  




<font style="color:rgb(38, 44, 49);">[mysqld]</font>

<font style="color:rgb(38, 44, 49);">user=mysql</font>

<font style="color:rgb(38, 44, 49);">character-set-server=utf8</font>

<font style="color:rgb(38, 44, 49);">default_authentication_plugin=mysql_native_password</font>

<font style="color:rgb(38, 44, 49);">default-time_zone = '+8:00'</font>

<font style="color:rgb(38, 44, 49);">[</font><font style="color:rgb(38, 44, 49);">client</font><font style="color:rgb(38, 44, 49);">]</font>

<font style="color:rgb(38, 44, 49);">default-character-set=utf8</font>

<font style="color:rgb(38, 44, 49);">[mysql]</font>

<font style="color:rgb(38, 44, 49);">default-character-set=utf8</font>

  
docker run -p 3306:3306 --name mysql -v /home/service/mysql/logs:/logs -v /home/service/mysql/data:/mysql_data -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7  
  
docker exec -it mysql bash   
  
mysql -uroot -p   
  
CREATE USER 'admin'@'%' IDENTIFIED BY 'Wing1Q2W#E';  
GRANT ALL ON *.* TO 'admin'@'%';   
flush privileges;   
  
docker ps 查看启动状态  
navicat直接连接即可，云服务器需要开启防火墙

