```python
docker pull mongo
docker images
```

### 运行容器
<font style="color:rgb(51, 51, 51);">安装完成后，我们可以使用以下命令来运行 mongo 容器：</font>

```python
docker run -dit --name mongo -p 27017:27017 mongo --auth
```

<font style="color:rgb(51, 51, 51);">参数说明：</font>

-i:表示运行容器

-t:表示容器启动后进入其命令行

-d:守护式方式创建容器在后台运行

-name:容器名称

-p 27017:27017：端口映射（宿主机端口:容器端口），mongoDB默认是27017端口

–auth：访问mongo需要鉴权(账号密码访问),这个参数要放在最后面，否则会报错

### 测试
##### <font style="color:rgb(79, 79, 79);">进入容器并访问mongoDB</font>
```shell
docker exec -it mongo /bin/mongosh
```

<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">说明：</font>  
<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">如果MongoDB6.0及以上使用：</font>  
<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">docker exec -it </font>mongo<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);"> /bin/mongosh</font>  
<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">如果是6.0以下的版本使用：</font>  
<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">docker exec -it mongo /bin/mongo</font>

<font style="color:rgb(51, 51, 51);">接着使用以下命令添加用户和设置密码，并且尝试连接</font>

您需要使用 docker exec -it <your db name> mongosh 进入 MongoDB 数据库。

 MongoDB v6 版本不再使用 mongod 命令作为[客户端](https://www.zhihu.com/search?q=%E5%AE%A2%E6%88%B7%E7%AB%AF&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2984886323%7D)，而使用 mongosh！

```plain
使用下面的命令创建管理员账户：
use admin
db.createUser({user: "admin", pwd: "admin", roles: [{role: "root", db: "admin"}]})
查看权限
show roles  
db.createUser({ user:'liyedong',pwd:'123456',roles:[ { role:'userAdminAnyDatabase', db: 'admin'},"readWriteAnyDatabase"]});
```

```plain
docker exec -it mongo /bin/bash
使用管理员账户进行身份验证：
mongosh -u liyedong -p liyedong --authenticationDatabase admin
```

```plain
创建数据库与普通账号：
use <database_name>
db.createUser({user: "<username>", pwd: "<password>", roles: [{role: "readWrite", db: "<database_name>"}]})
```

