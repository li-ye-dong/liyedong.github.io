<font style="color:rgb(92, 89, 98);">Django默认使用免费的SQLite数据库，你无需进行任何设置开箱即可使用。但是在生产环境中部署正式项目时，你应该使用性能更优越的企业级数据库，比如MySQL和Postgres。本文将介绍SQLite的优缺点以及如何在Django项目中连接MySQL和Postgres数据库。</font>

## <font style="color:rgb(39, 38, 43);">SQLite的应用场景及优缺点</font>
<font style="color:rgb(92, 89, 98);">SQLite是一个轻量级的开源免费的数据库。它是一种嵌入式数据库，只是一个.db格式的文件，无需安装，配置和启动。SQLite试图为单独的应用程序和设备提供本地的数据存储。</font>

<font style="color:rgb(92, 89, 98);">SQLite常见应用场景包括中小型网站，嵌入式设备和应用软件(如android)，文件档案管理和桌面程序(exe)文件数据库。SQLite支持多种编程语言(如python)和操作系统(windows, iOS, unix, linux)，移植性非常好。</font>

<font style="color:rgb(92, 89, 98);">如果你需要开发一个高流量或高并发的网站，SQLite将不能满足你的需求。同时如果你要开发一个Web APP, 不同用户通过网络对数据库进行读写操作，那么SQLite也将不能胜任（比如分布式数据库)。这时我们需要考虑企业级的专业数据库了，比如MySQL和Postgres。</font>

## <font style="color:rgb(39, 38, 43);">如何使用MySQL数据库</font>
<font style="color:rgb(92, 89, 98);">MySQL是最流行的开源免费的关系型数据库，可作为客户端/服务器数据库提供企业级的数据库服务。Django项目中配置使用MySQL一共分四步：</font>

### <font style="color:rgb(39, 38, 43);">第一步: 安装MySQL</font>
<font style="color:rgb(92, 89, 98);">Windows用户可以直接从MySQL网站上下载相应版本安装。Linux用户可以使用如下命令安装</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">mysql-server</font>`<font style="color:rgb(92, 89, 98);">。</font>

```python
sudo apt-get install mysql-server # ubuntu系统
```

### <font style="color:rgb(39, 38, 43);">第二步 创建数据库名和用户</font>
<font style="color:rgb(92, 89, 98);">打开MySQL终端，输入以下命令先创建数据库和用户，并给创建的用户授权。数据库名字，用户名和密码待会会用到。第一步和第二步非常重要。</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">mydb.*</font>`<font style="color:rgb(92, 89, 98);">表示授权操作mydb中所有的表。</font>

```python
# 创建数据库，设置字符
CREATE DATABASE mydb CHARACTER SET utf8;
# 创建用户及密码
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';
# 授权
GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'localhost' IDENTIFIED BY 'mypass'
```

### <font style="color:rgb(39, 38, 43);">第三步 安装第三方库mysqlclient</font>
<font style="color:rgb(92, 89, 98);">Django项目中操作MySQL，官方推荐</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">mysqlclient</font>`<font style="color:rgb(92, 89, 98);">这个库。</font>

```python
pip install mysqlclient
```

### <font style="color:rgb(39, 38, 43);">第四步 修改配置文件settings.py</font>
<font style="color:rgb(92, 89, 98);">修改项目文件夹里的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">的文件，添加创建的数据库和用户信息。</font>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'mydb',         # 数据库名，Django不会帮你创建，需要自己进入数据库创建。
        'USER': 'myuser',       # 设置的数据库用户名
        'PASSWORD': 'mypass',   # 设置的密码
        'HOST': 'localhost',    # 本地主机或数据库服务器的ip
        'PORT': '3306',         # 数据库使用的端口
    }
}
```

<font style="color:rgb(92, 89, 98);">另一种设置方式是使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">OPTIONS</font>`<font style="color:rgb(92, 89, 98);">和配置文件</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">my.cnf</font>`<font style="color:rgb(92, 89, 98);">进行设置。</font>

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}

# my.cnf
[client]
database = mydb
user = myuser
password = mypass
default-character-set = utf8
```

<font style="color:rgb(92, 89, 98);">设置好后，连续使用如下命令如果没有出现错误，那么恭喜你已经在Django项目中使用MySQL数据库啦。</font>

```python
python manage.py makemigrations                                                              
python manage.py migrate
```

<font style="color:rgb(92, 89, 98);">进入MySQL数据库终端，你会看见Django已经创建了很多数据表，比如</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">auth_user</font>`<font style="color:rgb(92, 89, 98);">表。</font>

```python
mysql> use mydb
Database changed

mysql> show tables;
+----------------------------+
 | Tables_in_django_mysql     |
  +----------------------------+
  | auth_group                 |
  | auth_group_permissions     |
  | auth_permission            |
  | auth_user                  |
  | auth_user_groups           |
  | auth_user_user_permissions |
```

## <font style="color:rgb(39, 38, 43);">如何使用PostgreSQL数据库</font>
<font style="color:rgb(92, 89, 98);">PostgreSQL在全球是仅次于MySQL的开源免费的关系型数据库，功能更加强大，是Django首选的关系型数据库。Django项目中配置使用PostgreSQL数据库一共分四步：</font>

### <font style="color:rgb(39, 38, 43);">第一步: 安装PostgreSQL</font>
<font style="color:rgb(92, 89, 98);">Windows用户可以直接从https://www.postgresql.org/download/ 下载相应版本安装。Linux用户可以使用如下命令安装PostgreSQL及其所依赖的python环境。</font>

```python
sudo apt-get install postgresql postgresql-contrib # ubuntu系统
sudo apt-get install libpq-dev python3-dev #安装依赖环境
```

### <font style="color:rgb(39, 38, 43);">第二步 创建数据库名和用户</font>
<font style="color:rgb(92, 89, 98);">Postgres数据库的默认用户是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">postgres</font>`<font style="color:rgb(92, 89, 98);">, 他有超级用户权限，相当于MySQL的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">root</font>`<font style="color:rgb(92, 89, 98);">用户。</font>

<font style="color:rgb(92, 89, 98);">打开postgres命令行终端(Linux下输入:</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">sudo -u postgres psql</font>`<font style="color:rgb(92, 89, 98);">)，连续输入以下命令先创建数据库和用户，并给创建的用户授权。数据库名字，用户名和密码待会会用到。</font>

```python
# 创建名为myapp的数据库
CREATE DATABASE mydb; 
# 创建用户名和密码
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypass'; 
# 给创建的用户授权
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

# 以下设置可手动进行设置，也可以在postgresql.conf中进行配置
# 设置客户端字符为utf-8，防止乱码
ALTER ROLE myuser SET client_encoding TO 'utf8';
# 事务相关设置 - 推荐
ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
# 设置数据库时区为UTC - 推荐
ALTER ROLE myuser SET timezone TO 'UTC';
```

### <font style="color:rgb(39, 38, 43);">第三步 安装第三方库</font>[<font style="color:rgb(39, 38, 43);">psycopg2</font>](https://www.psycopg.org/)
<font style="color:rgb(92, 89, 98);">Django项目中操作MySQL，官方推荐</font>[<font style="color:rgb(92, 89, 98);">psycopg2</font>](https://www.psycopg.org/)<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">这个库。</font>

```python
pip install psycopg2
```

### <font style="color:rgb(39, 38, 43);">第四步 修改配置文件settings.py</font>
<font style="color:rgb(92, 89, 98);">修改项目文件夹里的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">的文件，添加创建的数据库和用户信息。</font>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',   # 数据库引擎
        'NAME': 'mydb',         # 数据库名，Django不会帮你创建，需要自己进入数据库创建。
        'USER': 'myuser',     # 设置的数据库用户名
        'PASSWORD': 'mypass',     # 设置的密码
        'HOST': 'localhost',    # 本地主机或数据库服务器的ip
        'PORT': '',         # 数据库使用的端口
    }
}
```

<font style="color:rgb(92, 89, 98);">设置好后，连续使用如下命令如果没有出现错误，那么恭喜你已经在Django项目中使用PostgreSQL数据库啦。</font>

```python
python manage.py makemigrations                                                              
python manage.py migrate
```

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本文总结了SQLite的优缺点，并详细介绍了如何在Django中配置使用MySQL和PostgreSQL数据库。</font>

