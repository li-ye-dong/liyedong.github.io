## Mongodb基础笔记
## 安装Mongodb
[下载地址](https://www.mongodb.com/try/download/community)

```shell
tar xf mongodb-linux-x86_64-rhel70-4.4.29.tgz
mv mongodb-linux-x86_64-rhel70-4.4.29 /usr/local/mongodb
```

#  关闭THP
关闭THP root用户下 在vi /etc/rc.local最后添加如下代码

```shell
if test -f /sys/kernel/mm/transparent_hugepage/enabled; then
    echo never > /sys/kernel/mm/transparent_hugepage/enabled
fi
if test -f /sys/kernel/mm/transparent_hugepage/defrag; then
    echo never > /sys/kernel/mm/transparent_hugepage/defrag
fi
```

```shell
[root@node01 app]## cat /sys/kernel/mm/transparent_hugepage/enabled 
always madvise [never]
 [root@node01 app]## cat /sys/kernel/mm/transparent_hugepage/defrag
 always madvise [never]
```

 其他系统关闭参照官方文档： 

[https://docs.mongodb.com/manual/tutorial/transparent-huge-pages/](https://docs.mongodb.com/manual/tutorial/transparent-huge-pages/)

 为什么要关闭？ Transparent Huge Pages (THP) is a Linux memory management system that reduces the overhead of Translation Lookaside Buffer (TLB) lookups on machines with large amounts of memory by using larger memory pages. However, database workloads often perform poorly with THP, because they tend to have sparse rather than contiguous memory access patterns. You should disable THP on Linux machines to ensure best performance with MongoDB.  

#  环境准备  
```shell
(1)创建所需用户和组
useradd mongod
passwd mongod
(2)创建mongodb所需目录结构
mkdir -p /mongodb/conf
mkdir -p /mongodb/log
mkdir -p /mongodb/data
(3) 修改权限
chown -R mongod:mongod /mongodb
(4) 切换用户并设置环境变量
su - mongod
vi .bash_profile
export PATH=/usr/local/mongodb/bin:$PATH
source .bash_profile
```

#  使用配置文件  
### 普通配置文件
```shell
## 普通配置文件应用
vim /mongodb/conf/mongodb.conf
logpath=/mongodb/log/mongodb.log
dbpath=/mongodb/data 
port=27017
logappend=true
fork=true


```

### yaml格式配置文件
```yaml
## YAML 配置文件应用--
## 系统日志配置
systemLog:
  ## 日志目标：文件
  destination: file
  ## 日志文件路径
  path: "/mongodb/log/mongodb.log"
  ## 日志以追加模式记录
  logAppend: true

## 存储配置
storage:
  ## 日志
  journal:
    ## 启用日志
    enabled: true
    ## 数据路径
    dbPath: "/mongodb/data"

## 进程管理配置
processManagement:
  ## 启用后台守护进程
  fork: true
  ## pid 文件的位置
  pidFilePath: <string>

## 网络配置
net:
  ## 绑定的 IP 地址
  bindIp: <ip>
  ## 端口号
  port: <port>

## 安全配置
security:
  ## 启用授权
  authorization: enabled

## 复制配置
replication:
  ## oplog 大小（MB）
  oplogSizeMB: <NUM>
  ## 复制集名称
  replSetName: "<REPSETNAME>"
  ## 次要索引预取模式
  secondaryIndexPrefetch: "all"
  ## 本地 ping 阈值（毫秒）
  localPingThresholdMs: <int>

## 分片配置
sharding:
  ## 集群角色
  clusterRole: <string>
  ## 归档已移动块（仅适用于 mongos）
  archiveMovedChunks: <boolean> 
  ## 配置数据库的地址
  configDB: <string>
```

### 启动和关闭mongodb
```shell
## 关闭mongodb
mongod -f /mongodb/conf/mongodb.conf --shutdown
使用配置文件启动mongodb
mongod -f /mongodb/conf/mongodb.conf
```

### 实例
```yaml
systemLog:
  destination: file
  path: "/mongodb/log/mongodb.log"
  logAppend: true
storage:
  journal:
    enabled: true
  dbPath: "/mongodb/data/"
processManagement:
  fork: true
net:
  port: 27017
  bindIp: 本机ip,127.0.0.1
```

## 用户管理
注意  
验证库，建立用户时use到的库，在使用用户时，要加上验证库才能登陆。  
对于管理员用户,必须在admin下创建.

1. 建用户时,use到的库,就是此用户的验证库
2. 登录时,必须明确指定验证库才能登录
3. 通常,管理员用的验证库是admin,普通用户的验证库一般是所管理的库设置为验证库
4. 如果直接登录到数据库,不进行use,默认的验证库是test,不是我们生产建议的.

### 基本语法
```shell
use admin 
mongo 192.168.107.23/admin
 db.createUser
 {
    user: "<name>",
    pwd: "<cleartext password>",
    roles: [
       { role: "<role>",
     db: "<database>" } | "<role>",
    ...
    ]
 }
基本语法说明：
user:用户名
pwd:密码
roles:
    role:角色名
    db:作用对象 
role：root, readWrite,read
验证数据库：
mongo -u test -p 123 10.0.51/test
```

##  实例  
```shell
（1）--创建超级管理员：管理所有数据库（必须use admin再去创建）
$ mongo
 use admin
 db.createUser(
   {
     user: "root",
     pwd: "root123",
     roles: [ { role: "root", db: "admin" } ]
   }
 )
验证用户
db.auth('root','root123')
配置文件中，加入以下配置
security:
   authorization: enabled
重启mongodb
mongod -f /mongodb/conf/mongo.conf --shutdown 
mongod -f /mongodb/conf/mongo.conf 
登录验证
mongo -uroot -proot123  admin
mongo -uroot -proot123  10.0.51/admin
或者
mongo
use admin
db.auth('root','root123')
查看用户:
use admin
db.system.users.find().pretty()
2、创建库管理用户
mongo -uroot -proot123  admin
 use app
 db.createUser(
   {
     user: "admin",
     pwd: "admin",
     roles: [ { role: "dbAdmin", db: "app" } ]
   }
 )
db.auth('admin','admin')
登录测试
mongo -uadmin -padmin 10.4.7.100/app
3、创建对app数据库，读、写权限的用户app01：
（1）超级管理员用户登陆db
mongo -uroot -proot123 admin
（2）选择一个验证库
use app
 (3)创建用户
db.createUser(
   {
   user: "app01",
   pwd: "app01",
   roles: [ { role: "readWrite" , db: "app" } ]
   }
 )
mongo  -uapp01 -papp01 app
4、创建app数据库读写权限的用户并对test数据库具有读权限：
mongo -uroot -proot123 10.0.51/admin
use app
 db.createUser(
   {
     user: "app03",
     pwd: "app03",
     roles: [ { role: "readWrite", db: "app" },
     { role: "read", db: "test" }
     ]
   }
 )
5、查询mongodb中的用户信息
mongo -uroot -proot123 10.0.51/admin
db.system.users.find().pretty()
6、删除用户（root身份登录，use到验证库）
## mongo -uroot -proot123 10.0.51/admin
use app
db.dropUser("admin")
```

##  角色关系图 （Roles）
![](../../images/1709911457288-054dc584-d6b6-4016-836d-101af164e58b.png)

#  MongoDB 基本CRUD  
##  通用方法和帮助获取  
```shell
 a.获取帮助
help
 > help
 db.help()                    
db.mycoll.help()             
sh.help()                    
rs.help()                    
help on db methods
 help on collection methods
 sharding helpers
 replica set helpers
 db.help();
 DB methods:
 db.adminCommand(nameOrDocument) - switches to 'admin' db, and runs 
command [just calls db.runCommand(...)]
 db.aggregate([pipeline], {options}) - performs a collectionless 
aggregation on this database; returns a cursor
 db.auth(username, password)
 db.cloneDatabase(fromhost) - will only function with MongoDB 4.0 and 
below
 ...
 > db.t1.help();
 DBCollection help
 db.t1.find().help() - show DBCursor help
 db.t1.bulkWrite( operations, <optional params> ) - bulk execute write 
operations, optional parameters are: w, wtimeout, j
 db.t1.count( query = {}, <optional params> ) - count the number of 
documents that matches the query, optional parameters are: limit, skip, 
hint, maxTimeMS
 ... 
db.[TAB][TAB]
 db.t1.[TAB][TAB]
 b. 常用操作
//查看当前db版本
test> db.version()
 //显示当前数据库
test> db
> db.getName()
 // 查询所有数据库
test> show dbs
 //切换数据库
> use local
 // 显示当前数据库状态
查看local数据
test> use local
 local> db.stats()
查看当前数据库的连接机器地址
> db.getMongo()
 // 指定数据库进行连接：（默认连接本机test数据库）
## mongo 192.168.1.24/admin
 [mongod@mongodb ~]$ mongo 192.168.1.24/admin
 c. 库和表的操作 
// 建库 
use test
 // 删除
> db.dropDatabase()
 { "dropped" : "test", "ok" : 1 }
 // 创建集合(表)
方法1: 
admin> use app
 app> db.createCollection('a')
 app> db.createCollection('b')
方法2：当插入一个文档的时候，一个集合就会自动创建。
admin> use app
 switched to db app
 app> db.c.insert({username:"mongodb"})
 WriteResult({ "nInserted" : 1 })
 app> show collections
 app> db.c.find()
 { "_id" : ObjectId("5743c9a9bf72d9f7b524713d"), "username" : "mongodb" }
 // 删除集合
app> use app
 switched to db app
 app> db.log.drop() //删除集合
// 重命名集合
app> db.log.renameCollection("log1")
```

##  使用 insert 完成插入操作  
```javascript
操作格式：
db.<集合>.insertOne(<JSON对象>)
  db.<集合>.insertMany([<JSON 1>, <JSON 2>, …<JSON n>])
  示例：
db.fruit.insertOne({name: "apple"})
db.fruit.insertMany([
  {name: "apple"},
  {name: "pear"},
  {name: "orange"}
])
批量插入数据： 
for(i=0;i<10000;i++){ 
  db.log.insert({"uid":i,"name":"mongodb","age":6,"date":new Date()}); }
```

##  使用 find 查询文档  
```javascript
 ## 关于 find:
 find 是 MongoDB 中查询数据的基本指令，相当于 SQL 中的 SELECT 。
find 返回的是游标。
## find 示例：
db.movies.find( { "year" : 1975 } ) //单条件查询
db.movies.find( { "year" : 1989, "title" : "Batman" } ) //多条件and查询
db.movies.find( { $and : [ {"title" : "Batman"}, { "category" : "action" }] } 
) // and的另一种形式
db.movies.find( { $or: [{"year" : 1989}, {"title" : "Batman"}] } ) //多条件or
查询
db.movies.find( { "title" : /^B/} ) //按正则表达式查找
```

###  查询条件对照表  
|  SQL   |  MSQL   |
| --- | --- |
|  a = 1   |  {a: 1}   |
| a <> 1   |  {a: {$ne: 1}}   |
|  a > 1   |  {a: {$gt: 1}}   |
|  a >= 1   |  {a: {$gte: 1}}   |
|  a < 1   |  {a: {$lt: 1}}   |
|  a <= 1   |  {a: {$lte: 1}}   |


###  查询逻辑对照表  
|  SQL   |  MSQL   |
| --- | --- |
|  a = 1 AND b = 1   |  {a: 1, b: 1}或{$and: [{a: 1}, {b: 1}]}   |
|  a = 1 OR b = 1   |  {$or: [{a: 1}, {b: 1}]}   |
|  a IS NULL   |  {a: {$exists: false}}   |
|  a IN (1, 2, 3)   |  {a: {$in: [1, 2, 3]}}   |


###  查询逻辑运算符  
```javascript
● $lt: 存在并小于
● $lte: 存在并小于等于
● $gt: 存在并大于
● $gte: 存在并大于等于
● $ne: 不存在或存在但不等于
● $in: 存在并在指定数组中
● $nin: 不存在或不在指定数组中
● $or: 匹配两个或多个条件中的一个
● $and: 匹配全部条件
```

###  使用 find 搜索子文档  
```javascript
find 支持使用“field.sub_field”的形式查询子文档。假设有一个文档：
db.fruit.insertOne({
 name: "apple",
 from: {
 country: "China",
 province: "Guangdong" }
 })
正确写法： 
db.fruit.find( { "from.country" : "China" } )
```

###  使用 find 搜索数组  
```javascript
find 支持对数组中的元素进行搜索。假设有一个文档：
db.fruit.insert([
 { "name" : "Apple", color: ["red", "green" ] },
 { "name" : "Mango", color: ["yellow", "green"] }
 ])
查看单个条件： 
db.fruit.find({color: "red"})
查询多个条件： 
db.fruit.find({$or: [{color: "red"}, {color: "yellow"}]} )
```

###  使用 find 搜索数组中的对象  
```javascript
考虑以下文档，在其中搜索
db.movies.insertOne( {
 "title" : "Raiders of the Lost Ark",
 "filming_locations" : [ 
{ "city" : "Los Angeles", "state" : "CA", "country" : "USA" },
 { "city" : "Rome", "state" : "Lazio", "country" : "Italy" },
 { "city" : "Florence", "state" : "SC", "country" : "USA" }
 ] 
})
 // 查找城市是 Rome 的记录
db.movies.find({"filming_locations.city": "Rome"})
```

###  使用 find 搜索数组中的对象  
```javascript
在数组中搜索子对象的多个字段时，如果使用 $elemMatch，它表示必须是同一个
子对象满足多个条件。
考虑以下两个查询：
db.getCollection('movies').find({
 "filming_locations.city": "Rome",
 "filming_locations.country": "USA"
 })
 db.movies.insertOne( {
 "title" : "11111",
 "filming_locations" : [ 
{ "city" : "bj", "state" : "CA", "country" : "CHN" },
 { "city" : "Rome", "state" : "Lazio", "country" : "Italy" },
 { "city" : "tlp", "state" : "SC", "country" : "USA" }
 ] 
})
 db.getCollection('movies').find({
 "filming_locations": {
 $elemMatch:{"city":"bj", "country": "CHN"}
 }
 })
```

###  控制 find 返回的字段  
```javascript
find 可以指定只返回指定的字段；
● _id字段必须明确指明不返回，否则默认返回；
● 在 MongoDB 中我们称这为投影（projection）；
● db.movies.find({},{"_id":0, title:1})
```

![](../../images/1709911931253-3035a3a7-adaf-48d7-8682-b888ffaf15a1.png)

##  使用 remove 删除文档  
```javascript
remove 命令需要配合查询条件使用；
● 匹配查询条件的的文档会被删除；
● 指定一个空文档条件会删除所有文档；
● 以下示例：
db.testcol.remove( { a : 1 } ) // 删除a 等于1的记录
db.testcol.remove( { a : { $lt : 5 } } ) // 删除a 小于5的记录
db.testcol.remove( { } ) // 删除所有记录
db.testcol.remove() //报错
```

![](../../images/1709911969965-47725b47-3ba5-402c-a7b9-d632f8de8376.png)

##  使用 update 更新文档  
```javascript
● 使用 updateOne 表示无论条件匹配多少条记录，始终只更新第一条；
● 使用 updateMany 表示条件匹配多少条就更新多少条；
● updateOne/updateMany 方法要求更新条件部分必须具有以下之一，否则将报错：
    • $set/$unset
    • $push/$pushAll/$pop
    • $pull/$pullAll
    • $addToSet
 ● // 报错
db.fruit.updateOne({name: "apple"}, {from: "China"})
 ● 正确
> db.log.updateOne({uid:0},{$set:{name:"liyedong"}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }



$set/$unset：

$set：将指定字段设置为特定的值，如果该字段不存在，则创建它。
$unset：从文档中删除指定字段。
$push/$pushAll/$pop：

$push：将值追加到数组字段中。如果数组不存在，则创建一个新数组。
$pushAll：将多个值一次性追加到数组字段中。在MongoDB 3.6之后已弃用，推荐使用$push。
$pop：从数组字段的开头或结尾删除一个元素。
$pull/$pullAll：

$pull：从数组字段中删除满足特定条件的所有元素。
$pullAll：从数组字段中删除指定的多个值。在MongoDB 3.6之后已弃用，推荐使用$pull。
$addToSet：

将值添加到集合（数组）字段中，但仅当该值不已经存在于该集合中时才添加。如果集合字段不存在，则创建一个新集合字段。

```

##  使用 update 更新数组  
```javascript
● $push: 增加一个对象到数组底部
● $pushAll: 增加多个对象到数组底部
● $pop: 从数组底部删除一个对象
● $pull: 如果匹配指定的值，从数组中删除相应的对象
● $pullAll: 如果匹配任意的值，从数据中删除相应的对象
● $addToSet: 如果不存在则增加一个值到数组
```

##  使用 drop 删除集合  
```javascript
● 使用 db.<集合>.drop() 来删除一个集合
● 集合中的全部文档都会被删除
● 集合相关的索引也会被删除
db.colToBeDropped.drop()
```

##  使用 dropDatabase 删除数据库  
```javascript
● 使用 db.dropDatabase() 来删除数据库
● 数据库相应文件也会被删除，磁盘空间将被释放
use tempDB
 db.dropDatabase()
 show collections // No collections
 show dbs // The db is gone
```

#  通过python操作mongodb  
##  安装 Python MongoDB 驱动程序  
```shell
在 Python 中使用 MongoDB 之前必须先安装用于访问数据库的驱动程序：
wget -O /etc/yum.repos.d/CentOS-Base.repo 
http://mirrors.aliyun.com/repo/Centos-7.repo
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum install -y python3
pip3 install pymongo
在 python 交互模式下导入 pymongo，检查驱动是否已正确安装：
import pymongo 
pymongo.version
```

##  创建连接  
```shell
确定 MongoDB 连接串
使用驱动连接到 MongoDB 集群只需要指定 MongoDB 连接字符串即可。其基本格式可
以参考文档: Connection String URI Format 最简单的形式是
mongodb://数据库服务器主机地址：端口号
如：mongodb://127.0.0.1:27017
 ● 初始化数据库连接
from pymongo import MongoClient 
uri = "mongodb://root:root123@10.0.0.51:27017"
client = MongoClient(uri) 
client
```

##  数据库操作：插入数据  
```shell
初始化数据库和集合
db = client["eshop"]
 user_coll = db["users"]
插入一条新的用户数据
new_user = {"username": "nina", "password": "xxxx", "email": 
"123456@qq.com "}
 result = user_coll.insert_one(new_user)
 result
```

#  MongoDB RS(Replica Set)  
##  复制集的作用  
```shell
MongoDB 复制集的主要意义在于实现服务高可用,它的现实依赖于两个方面的功能：
• 数据写入时将数据迅速复制到另一个独立节点上
• 在接受写入的节点发生故障时自动选举出一个新的替代节点
在实现高可用的同时，复制集实现了其他几个附加作用：
• 数据分发：将数据从一个区域复制到另一个区域，减少另一个区域的读延迟
• 读写分离：不同类型的压力分别在不同的节点上执行
• 异地容灾：在数据中心故障时候快速切换到异地
```

##  典型复制集结构  
```shell
一个典型的复制集由3个以上具有投票权的节点组成，包括：
• 一个主节点（PRIMARY）：接受写入操作和选举时投票
• Arbiter（投票节点）
• 两个（或多个）从节点（SECONDARY）：复制主节点上的新数据和选举时投票
```

·![](../../images/1709912228149-bee27bd1-f279-4fc9-ad20-652d1ceac0b7.png)

##  数据是如何复制的  
```shell
当一个修改操作，无论是插入、更新或删除，到达主节点时，它对数据的操作将被记录下来（经过一些必
要的转换），这些记录称为 oplog。
从节点通过在主节点上打开一个 tailable 游标不断获取新进入主节点的 oplog，并在自己的数据上
回放，以此保持跟主节点的数据一致。
```

![](../../images/1709912247793-4018e268-5afe-4c32-bed5-b5d5974ae117.png)

##  通过选举完成故障恢复  
```shell
具有投票权的节点之间两两互相发送心跳；
● 当5次心跳未收到时判断为节点失联；
● 如果失联的是主节点，从节点会发起选举，选出新的主节点；
● 如果失联的是从节点则不会产生新的选举； 
● 选举基于 RAFT 一致性算法实现，选举成功的必要条件是大多数投票节点存活；
```

![](../../images/1709912268123-40fc4cb1-090a-470b-83d9-962912b45d18.png)

##  影响选举的因素  
```shell
整个集群必须有大多数节点存活；被选举为主节点的节点必须：
• 能够与多数节点建立连接
• 具有较新的 oplog
 • 具有较高的优先级（如果有配置）
```

##  常见选项  
```shell
复制集节点有以下常见的选配项：
• 是否具有投票权（v 参数）：有则参与投票；
• 优先级（priority 参数）：优先级越高的节点越优先成为主节点。优先级为0的节点无法成为主节
点；
• 隐藏（hidden 参数）：复制数据，但对应用不可见。隐藏节点可以具有投票仅，但优先级必须为0； 
• 延迟（slaveDelay 参数）：复制 n 秒之前的数据，保持与主节点的时间差。
```

![](../../images/1709912302148-fa5d1b27-f660-4f29-9e44-669b4f314c94.png)

##  复制集注意事项  
```shell
● 关于硬件：
• 因为正常的复制集节点都有可能成为主节点，它们的地位是一样的，因此硬件配置上必须一致；
• 为了保证节点不会同时宕机，各节点使用的硬件必须具有独立性。
● 关于软件：
• 复制集各节点软件版本必须一致，以避免出现不可预知的问题。
● 增加节点不会增加系统写性能！
```

##  Replcation Set配置过程详解  
###  规划  
```shell
三个以上的mongodb节点（或多实例）
多实例：
（1）多个端口：28017、28018、28019、28020
（2）多套目录：
su - mongod
 mkdir -p /mongodb/28017/conf /mongodb/28017/data /mongodb/28017/log
 mkdir -p /mongodb/28018/conf /mongodb/28018/data /mongodb/28018/log
 mkdir -p /mongodb/28019/conf /mongodb/28019/data /mongodb/28019/log
 mkdir -p /mongodb/28020/conf /mongodb/28020/data /mongodb/28020/log
 (3)配置文件内容准备
cat > /mongodb/28017/conf/mongod.conf <<EOF
systemLog:
  destination: file
  path: /mongodb/28017/log/mongodb.log
  logAppend: true
storage:
  journal:
    enabled: true
  dbPath: /mongodb/28017/data
  directoryPerDB: true
  #engine: wiredTiger
  wiredTiger:
    engineConfig:
      cacheSizeGB: 1
      directoryForIndexes: true
    collectionConfig:
      blockCompressor: zlib
    indexConfig:
      prefixCompression: true
processManagement:
  fork: true
net:
  port: 28017
  bindIp: 10.0.0.51,127.0.0.1
replication:
  oplogSizeMB: 2048
  replSetName: my_repl
EOF
\cp  /mongodb/28017/conf/mongod.conf  /mongodb/28018/conf/
\cp  /mongodb/28017/conf/mongod.conf  /mongodb/28019/conf/
\cp  /mongodb/28017/conf/mongod.conf  /mongodb/28020/conf/
sed 's#28017#28018#g' /mongodb/28018/conf/mongod.conf -i
sed 's#28017#28019#g' /mongodb/28019/conf/mongod.conf -i
sed 's#28017#28020#g' /mongodb/28020/conf/mongod.conf -i------------------------------------------------------------
(4)启动多个实例备用
mongod -f /mongodb/28017/conf/mongod.conf
mongod -f /mongodb/28018/conf/mongod.conf
mongod -f /mongodb/28019/conf/mongod.conf
mongod -f /mongodb/28020/conf/mongod.conf
```

### 配置复制集：
```javascript
（1）1主2从，从库普通从库(PSS)
config = {_id: 'my_repl', members: [
  {_id: 0, host: '10.0.0.51:28017'},
  {_id: 1, host: '10.0.0.51:28018'},
  {_id: 2, host: '10.0.0.51:28019'}]
         }
rs.initiate(config)
（2）1主1从1个arbiter(PSA)
config = {_id: 'my_repl', members: [
  {_id: 0, host: '10.0.0.51:28017'},
  {_id: 1, host: '10.0.0.51:28018'},
  {_id: 2, host:
    '10.0.0.51:28019',"arbiterOnly":true}]
         }
rs.initiate(config)
```

### 复制集测试：
```javascript
my_repl:PRIMARY> db.movies.insert([ { "title" : "Jaws", "year" : 1975,
                                     "imdb_rating" : 8.1 },
                                   ... { "title" : "Batman", "year" : 1989, "imdb_rating" : 7.6 },
                                   ... ] );
BulkWriteResult({
  "writeErrors" : [ ],
  "writeConcernErrors" : [ ],
  "nInserted" : 2,
  "nUpserted" : 0,
  "nMatched" : 0,
  "nModified" : 0,
  "nRemoved" : 0,
  "upserted" : [ ]
})
my_repl:SECONDARY> db.movies.find().pretty();
注：在mongodb复制集当中，默认从库不允许读写。
rs.slaveOk();
my_repl:SECONDARY> db.movies.find().pretty();

```

### 复制集管理操作：
```javascript
（1）查看复制集状态：
rs.status(); //查看整体复制集状态
rs.isMaster(); // 查看当前是否是主节点
（2）添加删除节点
rs.add("ip:port"); // 新增从节点
rs.addArb("ip:port"); // 新增仲裁节点
rs.remove("ip:port"); // 删除一个节点
（3）特殊从节点的配置
• 优先级（priority 参数：0-1000）：
优先级越高的节点越优先成为主节点。
优先级为0的节点无法成为主节点；
• 隐藏（hidden 参数）：复制数据，但对应用不可见。隐藏节点可以具有投票仅，但优先级必须为
0；
• 延迟（slaveDelay 参数）：复制 n 秒之前的数据，保持与主节点的时间差。
配置延时节点（一般延时节点也配置成hidden）
cfg=rs.conf()
cfg.members[1].priority=0
cfg.members[1].slaveDelay=120
cfg.members[1].hidden=true
rs.reconfig(cfg)
改回来：
cfg=rs.conf()
cfg.members[2].priority=1
cfg.members[2].slaveDelay=0
cfg.members[2].hidden=0
cfg.members[2].votes=0
rs.reconfig(cfg)
配置成功后，通过以下命令查询配置后的属性
rs.conf();
```

### 副本集其他操作命令：
```javascript
--查看副本集的配置信息
admin> rs.config()
--查看副本集各成员的状态
admin> rs.status()
--副本集角色切换（不要人为顺便操作，有风险）
admin> rs.stepDown()
注：
admin> rs.freeze(300) //锁定从，使其不会转变成主库
freeze()和stepDown单位都是秒。
--设置副本节点可读：在副本节点执行
admin> rs.slaveOk()
eg：
admin> use app
switched to db app
app> db.createCollection('a')
{ "ok" : 0, "errmsg" : "not master", "code" : 10107 }
--查看副本节点
admin> rs.printSlaveReplicationInfo()
source: 192.168.1.22:27017
  syncedTo: Thu May 26 2016 10:28:56 GMT+0800 (CST)
  0 secs (0 hrs) behind the primary

```



