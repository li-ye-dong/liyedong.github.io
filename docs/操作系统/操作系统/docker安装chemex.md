# <font style="color:rgb(51, 51, 51);"></font>
<font style="color:rgb(51, 51, 51);">Docker 部署方式不会建立数据库容器，也意味着你必须有一个已有的数据库，在启动 chemex 后需要对 </font><font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">.env</font><font style="color:rgb(51, 51, 51);"> 文件做配置。</font>

docker pull celaraze/chemex:latest

<font style="color:rgb(119, 119, 119);">注意 your_path 为你的宿主机某个目录，chemex 根目录有一个 .env.example 的环境变量配置文件，复制这个文件到 your_path 下并改名为 .env，然后修改 .env 中的数据库连接信息。</font>

```plain
mkdir /chemex
touch /chemex/.env
docker run -itd --name chemex --restart=always -p 8000:8000 -v /chemex/.env:/var/www/html/laravel/.env  celaraze/chemex:latest
docker exec -it chemex /bin/bash
cat .env.example > .env
exit
vi /chemex/.env

#数据库类型，不需要修改（兼容mariadb）
DB_CONNECTION=mysql
# 数据库地址
DB_HOST=192.168.107.55
# 数据库端口号，mysql默认是3306
DB_PORT=3306
# 数据库名称，如果没有此数据库，后续会提示创建
DB_DATABASE=chemex
# 数据库用户名
DB_USERNAME=chemex
# 数据库密码
DB_PASSWORD=123456

docker restart chemex
```

<font style="color:rgb(51, 51, 51);">即可通过 </font><font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">http://127.0.0.1:8000</font><font style="color:rgb(51, 51, 51);"> 访问 chemex。</font>

<font style="color:rgb(119, 119, 119);">初始化数据库：如果您是第一次使用 chemex，则需要执行数据库迁移。</font><font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">docker exec -it chemex /bin/bash</font><font style="color:rgb(119, 119, 119);"> 进入 docker 容器执行命令： </font><font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">cd /var/www/html/laravel && php artisan chemex:install</font><font style="color:rgb(119, 119, 119);">。</font>

