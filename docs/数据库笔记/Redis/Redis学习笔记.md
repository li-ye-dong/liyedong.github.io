## Redis学习
### 准备环境
| redis01 | redis02 | redis03 |
| :---: | :---: | :---: |
| 192.158.107.222 | 192.158.107.223 | 192.158.107.224 |
| centos7 | centos7 | centos7 |




```plain
环境包
redis-6.2.9.tar.gz
```

[redis-6.2.9.tar.gz.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/40598547/1709984378983-b58ca9b7-61b2-48fc-aaf7-6349415005df.txt)

去掉.txt即可

### 1.redis的编译安装


```shell
systemctl stop firewalld
getenforce #查看selinux
setenforce 0 #临时关闭selinux
#sed -i 's/SELINUX=.*/SELINUX=disables/' /etc/selinux/config && setenforce 0
tar xf redis-6.2.9.tar.gz -C /
make -j2 & make install
cp redis.conf /etc/
ls -l /usr/local/bin/redis-*
/usr/local/bin/redis-server -v

#说明可以通过scp命令将，bin/redis-*的所有文件推送到其他相同系统的服务器上，没必要每次安装
```



### 2.redis配置修改启动和参数调优


```shell
sed -i '/^#/d;/^$/d' /etc/redis.conf
vi /etc/redis.conf
bind 0.0.0.0
daemonize yes#后台运行
pidfile "redis.pid"
logfile "redis.log"
dir /data/redis
requirepass redispwd
mkdir -p /data/redis
redis-server /etc/redis.conf
```



```shell
#调整最大文件打开数
vi /etc/security/limits.conf
* - nofile 65535 
#内核参数修改
vi /etc/sysctl.conf
net.core.somaxconn = 10240
vm.overcommit_memory = 1
sysctl -p

pkill redis
redis-server /etc/redis.conf
tail -f /data/redis/redis.log

#systemctl管理redis
vi /usr/lib/systemd/system/redis.service
[Unit]
Description=redis
After=network.target
[Service]
Type=forking
ExecStart=/usr/local/bin/redis-server /etc/redis.conf
[Install]
WantedBy=multi-user.target

systemctl daemon-reload
```



### 3.redis常用数据类型的基本操作


```shell
1.redis-cli使用和认证登录
客户端工具redis-cli登录
## redis-cli                         #默认127.0.0.1 6379
## redis-cli -h redis的ip
## redis-cli -h xxx -p xxx

redis的认证
>auth redispwd               #登录redis后做认证
## redis-cli -a redispwd     #登录+认证

2.Redis常用数据类型
字符串
列表、集合
hash哈希、发布和订阅


3.Redis字符串操作
>set name aaa              #增加key并赋值
>keys *                        #显示所有的key
>get name                    #获取key的值
>set name bbb              #重新给key赋值
>del name                    #删除key

大小写问题
命令不区分大小写:  >GET name
key区分大小写: >get Name
>set name ccc            
>set Name xxx              

>get name
>GET name

>get name
>get Name

非交互式操作Redis
## redis-cli -a redispwd set name abc888
## redis-cli -a redispwd get name
## redis-cli -a redispwd del name


使用Shell批量写入数据并获取
## for i in $(seq -w 10);do redis-cli -a redispwd set name${i} test${i}; redis-cli -a redispwd get name${i}; done 2>/dev/null


4.Redis列表和集合的基本操作
1).Redis列表
列表特点:
列表是有顺序的
可写入重复的数据

rpush右添加               
如：['s1','s2','s3',...]
>rpush names s1              #依次在列表右侧逐步添加数据，起初列表可以为空
>rpush names s2
>rpush names s3
>rpush names s4
>rpush names s1                #列表中添加一个重复的数据
>lrange names 0 -1            #将列表的值全部读取查看，注意:最前面是L的小写，大小写都可以
>LLEN names                     #列出列表的长度

Redis列表的读取说明
0代表第一个值，1代表第二个值等，2代表第三个值，...
-1代表最后一个值，-2代表倒二个值等
>lrange names 0  2           #读取第1到第3个列表值
>lrange names 0 -2           #读取第1到倒数第2个列表值

列表左添加
如：['...','b3','b2','b1']
>lpush names2 b1          #依次在列表左侧逐步添加数据，起初列表可以为空，注意:最前面是L的小写，大小写都可以
>lpush names2 b2
>lpush names2 b3
>lpush names2 b4
>push names2 b1             #列表中添加一个重复的数据
>lrange names2 0 -1         #将列表的值全部读取查看，注意:最前面是L的小写，大小写都可以
> lrange names2 0 1         #读取第一个到第二个的值

Redis列表元素的删除
移除列表中的其中一个值,如s1：  >LREM names 1 s1                #1是代表移除一个元素，因为列表中元素是可以重复的,需要指定移除几个元素,1,2...
移除列表中所有重复的值,如s1：  >LREM names2 0 b1              #0是代表移除所有个指定的元素

列表弹出元素
>lpop 列表名     #左弹出                     #注意是L的小写
>rpop 列表名    #右弹出

2).Redis集合
集合特点:
无顺序的
不重复的

Redis集合的操作
>sadd jh j1                     #创建集合并添加元素，集合事先可以没有元素
>sadd jh j2
>sadd jh j3
>sadd jh j4
>sadd jh j1                     #集合中添加一个重复的元素，会添加失败，因为集合不允许元素重复
>SMEMBERS jh                #列出集合中的所有元素

Redis集合的删除
>srem jh j1                   #删除集合中的元素j1
>spop jh                       #集合随机弹出一个元素

判断元素是否在集合里
SISMEMBER jh j1
0代表不在，1代表在


5.Redis哈希和订阅类型基础操作
1).Hash哈希类型数据操作
Hash写入
>hset haxi name ha                     #创建一个hash名字haxi,在名字里面插入值（值都是以k-v形式的，可以多插入几对值）
>hset haxi location bj
>hset haxi age 18
>hset haxi sex man
hash获取
获取全部：>HGETALL haxi            #获取hash名字里的所有对儿key的值
获取单个：>HGET haxi name        #获取hash名字里的单个key的值
Hash删除
>HDEL haxi age                          #删除hash名字的单个key
>DEL haxi                                   #删除整个hash
Hash批量添加
>hmset haxi name hx666 age 20 location bj sex boy

2).Redis的发布订阅
>subscribe fabu                                         #订阅一个频道，可以开多个窗口都订阅这个频道
>publish fabu "name shi, age 20,sex boy"    #另外开一个窗口，往这个订阅频道里发送数据，这样订阅频道的窗口都能收到该数据
```



### 4.redis的不同库切换和运维监控命令


### A.Redis不同数据库的切换


```shell
1).配置文件查看Redis有多少个库？ 
默认是16个
[root@localhost ~]## grep databases /etc/redis.conf 
databases 16

2).Redis数据库的切换
>select 0
>select 1
>select 16        #切换不成功

3).不同的库数据是独立的
可以在不同的库存储不同的数据
>select 0                        #默认也是0库，默认操作的都是0库
>set name s0
>get name
>select 2
>set name s2
>get name
```



### B.Redis运维监控命令


```shell
1).查看key
>RANDOMKEY    #随机获取一个key
>KEYS *            #查看所有key，注意阻塞,如果key量特别大时候，容易卡死阻塞，上千万上百万时候容易阻塞
>SCAN 0           #建议使用,每次获取11个key，可以循环获取，直到获取所有key
                       #从编号0开始，中间会有一个编号提示（类似索引编号),按编号提示依次循环获取，直到编号为0即表示获取完所有的key

使用Shell批量写入数据并获取
## for i in $(seq -w 50);do redis-cli -a redispwd set name${i} test${i}; redis-cli -a redispwd get name${i}; done 2>/dev/null

2).监控命令
## redis-cli -a redispwd --stat                                #监控Redis状态
------- data ------ --------------------- load -------------------- - child -
keys       mem      clients blocked requests            connections          
18         855.93K  1       0       49 (+0)             6           
18         855.93K  1       0       50 (+1)             6           
18         855.93K  1       0       51 (+1)             6           

显示多少个key(是把所有数据库的key都加起来)  内存占用多少   客户端有多少   redis的requests请求数是多少  connections是多少连接    
--多几个客户端，多增加几个key就可以马上发现

## redis-cli -a redispwd monitor #监控数据操作
交互式阻塞状态，当有对数据进行操作时候会记录
--操作的命令，增加，删除数据等都会监控到

## redis-cli -a redispwd info  #监控系统可通过info获取数据

3).Info常用信息说明，监控工具例如Zabbix使用
Server:                       #服务器信息
Clients:                      #客户端信息
Memory:                       ## Redis内存占用
   used_memory                #数据占用内存
   used_memory_rss            #实际使用内存
   mem_fragmentation_ratio    #内存碎片化
   maxmemory                  #最大内存限制
Persistence:                  #持久化存储信息
   rdb_*
   aof_enabled:0              #默认aof是关闭的
Stats:                        #状态信息，是监控重点
Replication:                  #主从状态监控和哨兵信息
   role:master
   connected_slaves:0
CPU:                          #sys、user占用
Cluster:                      #Redis集群信息
Keyspace:                     #键的分布信息，key的分布的库和过期时间等信息


4).单独查看某块内容

## redis-cli -a redispwd info Server

## redis-cli -a redispwd info Clients

## redis-cli -a redispwd info Memory

## redis-cli -a redispwd info Persistence

## redis-cli -a redispwd info Stats

## redis-cli -a redispwd info Replication

## redis-cli -a redispwd info CPU

## redis-cli -a redispwd info Cluster

## redis-cli -a redispwd info Keyspace
```



### 5.Redis配置动态更新和写入


### 1).Redis更新配置的两种方式


```shell
a.重启更新，需要修改配置文件，然后重启
b.实时更新，不需要重启

重启更新密码
## vim /etc/redis.conf
requirepass redispwd666

动态更新密码
>config get requirepass
>config set requirepass redispwd
>config rewrite                             #运行时配置写入配置文件
```



### 2).查看redis的相关连接数


```shell
>info clients                              #查看当前的redis连接数
>config get maxclients                 #查看redis允许的最大连接数
```



### 3).大部分配置都能通过config命令进行更改，然后写入配置文件（使用比较方便)


```shell
例如：修改redis最大连接数
> config get maxclients                   #查看默认设置，最大客户端数为10000
1) "maxclients"
2) "10000"

>config set maxclients 20000

> config get maxclients                   
1) "maxclients"
2) "20000"
```



### 6.redis多用户管理


```shell
老版本没有用户名，只有密码
Redis6已经有用户名，默认用户名default

1).列出所有用户，默认只有default超级用户，并查看default用户相关信息
>ACL LIST                      #列出所有用户，默认用户是default
1) "user default on #9cd9ab402f4115ed9921a7e4f7fc89330c8fe9283a8b1cdef203f7a7e622c68f ~* &* +@all"     #default用户呢是有所有权限
>ACL getuser default     #查看default用户的相关信息， default对所有key，所有命令均有权限，最高权限，是默认用户
 1) "flags"
 2) 1) "on"
    2) "allkeys"                            #所有的key都有权限
    3) "allchannels"
    4) "allcommands"
 3) "passwords"
 4) 1) "9cd9ab402f4115ed9921a7e4f7fc89330c8fe9283a8b1cdef203f7a7e622c68f"
 5) "commands"
 6) "+@all"                                 #所有的命令都有权限
 7) "keys"
 8) 1) "*"
 9) "channels"
10) 1) "*"

2).创建用户并给用户授权
> ACL CAT                                   #查看所有的权限
 1) "keyspace"
 2) "read"
 3) "write"
 4) "set"
 5) "sortedset"
 6) "list"
 7) "hash"
 8) "string"
 9) "bitmap"
10) "hyperloglog"
11) "geo"
12) "stream"
13) "pubsub"
14) "admin"
15) "fast"
16) "slow"
17) "blocking"
18) "dangerous"
19) "connection"
20) "transaction"
21) "scripting"


案例：创建test用户只给一个get命令权限、读权限、并且只能get是name开头的key: name*
使用default默认用户登录redis：
## redis-cli -a redispwd
> set name1 n1
> set name2 n2
> set name3 n3
>set k1 v1
>set k2 v2
>ACL SETUSER test on >testpwd ~name* +get               #创建test用户，密码：testpwd   赋给get命令的权限，只对name开头的有get权限
>ACL SETUSER test on >testpwd ~name* +@read           #给test用户增加read权限，设置只对name开头的key有read权限
>ACL getuser test                                                        #查看test用户的相关信息

>ACL SETUSER t1 on >t1pwd ~* +get                           #对所有key都有get权限
>ACL SETUSER t1 on >t1pwd ~* +@read                      #对所有key都有read权限
>ACL getuser t1

认证登录，验证权限:
>auth test testpwd
## redis-cli --user test --pass testpwd

>get name1
"n1"
>get name2
"n2"
>get k1
(error) NOPERM this user has no permissions to access one of the keys used as arguments
>set k3 v3
(error) NOPERM this user has no permissions to run the 'set' command or its subcommand


3).常用权限案例：
案例1:创建用户赋给所有权限：              
>ACL SETUSER test1 on >test1pwd ~* +@all               #用户名:test1  密码:test1pwd
> ACL GETUSER test1                                                #查看test1用户的所有权限

验证权限:
> auth test1 test1pwd
> keys *
1) "name1"
2) "k1"
3) "k2"
4) "name2"
5) "name3"
> get name1
"n1"
> get k1                                                                    #get权限
"v1"
> set a b                                                                  #set权限
> get a
"b"
> config get requirepass                                            #config配置权限
1) "requirepass"
2) "redispwd"
> ACL SETUSER t666 on >t666pwd ~* +@all -config     #创建用户的权限
> acl getuser t666                                                     #查看用户权限


案例2:去除config命令后的所有权限:       
>ACL SETUSER test2 on >test2pwd ~* +@all -config     #用户名:test2  密码:test2pwd
>ACL GETUSER test2                                                 #查看test2用户除了config命令权限之外的所有权限

验证权限:
> auth test2 test2pwd
> config get requirepass                            #没有config权限
(error) NOPERM this user has no permissions to run the 'config' command or its subcommand
> keys *
1) "name1"
2) "k1"
3) "a"
4) "k2"
5) "name2"
6) "name3"
> get name1
"n1"
> set a2 b2
> get a2
"b2"
> ACL SETUSER t777 on >t777pwd ~* +@all      #创建用户的权限
> acl getuser t777                                            #查看用户权限


案例3:创建一个用户，只给info和momitor命令权限： 
>ACL SETUSER monitor on >monitorpwd ~* +info +monitor   #用户名:monitor 密码:monitorpwd

权限认证：
> auth monitor monitorpwd
> KEYS *
(error) NOPERM this user has no permissions to run the 'keys' command or its subcommand
> get name1
(error) NOPERM this user has no permissions to run the 'get' command or its subcommand
> info                                              #有info权限
## Server
redis_version:6.2.1
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:3bc8e110479b329d
.....
> monitor                                      #有monitor权限
阻塞状态，监控redis


列出所有用户:
## redis-cli -a redispwd                 
> ACL LIST                                 #列出所有用户

删除用户:
> ACL DELUSER t666                   #删除用户t666
> ACL LIST

使用acl创建用户写入配置文件
>config rewrite      #重启Redis用户信息才不会丢失
```



### 案例1


```shell
创建test用户只给一个get命令权限、读权限、并且只能get是name开头的key: name*
使用default默认用户登录redis：
## redis-cli -a redispwd
> set name1 n1
> set name2 n2
> set name3 n3
>set k1 v1
>set k2 v2
>ACL SETUSER test on >testpwd ~name* +get               #创建test用户，密码：testpwd   赋给get命令的权限，只对name开头的有get权限
>ACL SETUSER test on >testpwd ~name* +@read           #给test用户增加read权限，设置只对name开头的key有read权限
>ACL getuser test                                                        #查看test用户的相关信息

>ACL SETUSER t1 on >t1pwd ~* +get                           #对所有key都有get权限
>ACL SETUSER t1 on >t1pwd ~* +@read                      #对所有key都有read权限
>ACL getuser t1

认证登录，验证权限:
>auth test testpwd
## redis-cli --user test --pass testpwd

>get name1
"n1"
>get name2
"n2"
>get k1
(error) NOPERM this user has no permissions to access one of the keys used as arguments
>set k3 v3
(error) NOPERM this user has no permissions to run the 'set' command or its subcommand


3).常用权限案例：
案例1:创建用户赋给所有权限：              
>ACL SETUSER test1 on >test1pwd ~* +@all               #用户名:test1  密码:test1pwd
> ACL GETUSER test1                                                #查看test1用户的所有权限

验证权限:
> auth test1 test1pwd
> keys *
1) "name1"
2) "k1"
3) "k2"
4) "name2"
5) "name3"
> get name1
"n1"
> get k1                                                                    #get权限
"v1"
> set a b                                                                  #set权限
> get a
"b"
> config get requirepass                                            #config配置权限
1) "requirepass"
2) "redispwd"
> ACL SETUSER t666 on >t666pwd ~* +@all -config     #创建用户的权限
> acl getuser t666                                                     #查看用户权限
```



### 案例2


```shell
案例2:去除config命令后的所有权限:       
>ACL SETUSER test2 on >test2pwd ~* +@all -config     #用户名:test2  密码:test2pwd
>ACL GETUSER test2                                                 #查看test2用户除了config命令权限之外的所有权限

验证权限:
> auth test2 test2pwd
> config get requirepass                            #没有config权限
(error) NOPERM this user has no permissions to run the 'config' command or its subcommand
> keys *
1) "name1"
2) "k1"
3) "a"
4) "k2"
5) "name2"
6) "name3"
> get name1
"n1"
> set a2 b2
> get a2
"b2"
> ACL SETUSER t777 on >t777pwd ~* +@all      #创建用户的权限
> acl getuser t777                                            #查看用户权限
```



### 案例3


```shell
案例3:创建一个用户，只给info和momitor命令权限： 
>ACL SETUSER monitor on >monitorpwd ~* +info +monitor   #用户名:monitor 密码:monitorpwd

权限认证：
> auth monitor monitorpwd
> KEYS *
(error) NOPERM this user has no permissions to run the 'keys' command or its subcommand
> get name1
(error) NOPERM this user has no permissions to run the 'get' command or its subcommand
> info                                              #有info权限
## Server
redis_version:6.2.1
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:3bc8e110479b329d
.....
> monitor                                      #有monitor权限
阻塞状态，监控redis


列出所有用户:
## redis-cli -a redispwd                 
> ACL LIST                                 #列出所有用户

删除用户:
> ACL DELUSER t666                   #删除用户t666
> ACL LIST

使用acl创建用户写入配置文件
>config rewrite      #重启Redis用户信息才不会丢失sh
```



### 7.redis的慢日志和key的有效期


### 一、redis的慢日志


```shell

问题：如果有人反馈redis慢，如何进行排查？

系统资源情况
查看慢日志情况

1.查看慢日志的默认配置
>CONFIG GET slow*                     #查看慢日志的配置                  
1) "slowlog-max-len"
2) "128"                                      #最多记录128个
3) "slowlog-log-slower-than"
4) "10000"                                  #默认超过10毫秒就会记录

2.设置慢日志的时间是1毫秒，查询超过1毫秒就为慢日志
>config set slowlog-log-slower-than 1000     #设置慢日志的时间是1毫秒,查询超过1毫秒就为慢日志
> CONFIG GET slow*                                 #查看
1) "slowlog-max-len"
2) "128"
3) "slowlog-log-slower-than"
4) "1000"                                               #1毫秒为慢日志


3.使用Shell批量写入数据并获取，多写入些数据，方便我们查询数据大的时候产生慢日志
>flushall
>for i in $(seq -w 100000);do redis-cli -a redispwd set name${i} test${i}; redis-cli -a redispwd get name${i}; done 2>/dev/null

4.产生慢日志
>KEYS *                        #查询一次，当操作时间大于1毫秒，就会产生一条慢日志
>KEYS * 
>KEYS * 
....可以多查询几次，多获取几条慢日志

5.查询慢日志
>SLOWLOG get               #默认获取最近10条
>SLOWLOG get 5            #获取5条
>SLOWLOG len               #慢日志量，查看慢日志的条数
>SLOWLOG reset             #清空慢日志

6.Slowlog各字段意思
127.0.0.1:6379> SLOWLOG get
1) 1) (integer) 115                   #慢日志的id，从0开始，第115个id
   2) (integer) 1668215297        #时间戳，慢日志产生的时间点，可以通过 date -d @1668215297   获取慢日志产生的时间
   3) (integer) 69284                 #慢日志运行的时间69毫秒
   4) 1) "keys"                          #产生慢日志的命令，一般是当数据量太多时候，运行keys *命令会比较慢
      2) "*"
   5) "127.0.0.1:60014"
   6) ""
```



### 二、Redis的key的有效期


```shell
给Redis的key设置有效期,-1表示永久,-2代表Redis回收了（key已经自动删除)
>set name test1            #默认设置的key是永久有效的
>get name
"test1"
>ttl name                      #查看key的状态，生命周期，-1表示永久有效
(integer) -1
>expire name 20           #方法1: 给key设置有效期，单位:秒，设置有效期是20s       

>set name2 test02 EX 20       #方法2: 再创建key时候直接给key设置有效期:20s
```



### 8.Redis禁用危险命令和Redis压测工具


### 1.Redis禁用危险命令


```shell
Redis危险的命令有哪些？
>FLUSHALL           会清空Redis所有数据
>FLUSHDB            会清除当前DB所有数据
>KEYS *               在键过多的时候使用会阻塞业务请求，比如有上千万数据时候，该命令会阻塞卡住

Redis禁用危险命令的配置
禁用需要修改redis的配置文件，然后重启redis
## vi /etc/redis.conf
rename-command FLUSHALL ""
rename-command FLUSHDB ""
rename-command KEYS ""

测试命令是否失效
>keys *
发现运行不了
>flushall 
运行不了
```



### 2.Redis压测工具


```shell
## redis-benchmark --help
-c <clients>       Number of parallel connections (default 50)             #默认的并发是50个
-n <requests>      Total number of requests (default 100000)            #默认有10万个请求
压测工具，基本对redis里的每一个命令都会进行测试一遍，
## redis-benchmark -a redispwd                                                     #用默认的并发50个，一共10万个请求对redis进行压测
## redis-benchmark -a redispwd | tee /tmp/a.log                              #将测试的结果输出到一个log文件

日常输出的一个简介
## vim /tmp/a.log
PING_INLINE:                                                                      #测试PING
  100000 requests completed in 1.10 seconds                          #一共处理了10万个PING请求，在1.1秒中完成
  50 parallel clients                                                              ## 50个并发
  3 bytes payload                                                                 #每个请求数据量是3个字节
  ......
100.000% <= 2.527 milliseconds (cumulative count 100000)    #测试PING的一个延时，<2.5毫秒的有100%

SET:                                                                                   #测试SET命令
  100000 requests completed in 1.07 seconds                         #一共执行了10万次SET操作，在1.07秒中完成
  50 parallel clients                                                              #50个并发
  3 bytes payload                                                                #每个请求数据量是3个字节  
  ......
23.353% <= 0.207 milliseconds (cumulative count 23353)       #%23.353的命令执行时间小于0.207毫秒
69.820% <= 0.303 milliseconds (cumulative count 69820)       #%69.820的命令执行时间小于0.303毫秒
100.000% <= 2.183 milliseconds (cumulative count 100000)    #%100的命令执行时间小于2.183毫秒
Summary:
  throughput summary: 93370.68 requests per second             #redis每秒可以处理93370.68次set请求
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.302     0.072     0.247     0.599     1.111     2.183

GET:                                                                                 #测试GET命令
  100000 requests completed in 1.12 seconds                        #一共执行了10万次GET操作，在1.12秒中完成
  50 parallel clients                                                              #50个并发
  3 bytes payload                                                                #每个请求数据量是3个字节 
  ......
50.000% <= 0.255 milliseconds (cumulative count 52277)        #%50的命令执行时间小于0.255毫秒
75.000% <= 0.375 milliseconds (cumulative count 75710)        #%75的命令执行时间小于0.375毫秒
100.000% <= 2.447 milliseconds (cumulative count 100000)     #%100的命令执行时间小于2.447毫秒
Summary:
  throughput summary: 89445.44 requests per second               #redis每秒可以处理89445.44次get请求    
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.326     0.048     0.255     0.687     1.311     2.447

...测试每一个命令，最终给一个结果：


## redis-benchmark -a redispwd -n 10                 #用默认的并发50个，一共10个请求对redis进行压测
```



### 9.Redis持久化存储的两种方式


### 1.Redis持久化存储的两种方式


```plain
RDB方式   RDB存储是Redis实现的一种存储机制     (默认开启)
AOF方式    AOF存储方式，直接把操作的命令记录下来，保存到一个文件里，类似mysql的binlog日志 (默认关闭)
```



### 2.Redis的RDB持久化存储


```plain
Redis默认是开启了RDB快照方式，提供持久化存储的功能
如果只让Redis做缓存的服务，不需要持久化时候，也可以关闭所有存储功能
```



```shell
Redis的RDB存储方式的配置，默认是开启的
>config get dir                        #查看存储设置的路径
1) "dir"
2) "/data/redis"
>config get dbfilename           #查看rdb存储的文件名，默认是dump.rdb文件   
1) "dbfilename"
2) "dump.rdb"                      #该文件可以保证redis的数据不丢失

## ls /data/redis/
dump.rdb  redis.log  redis.pid

>config get save                   #查看rdb默认的存储机制配置
3600 1 300 100 60 10000      #3600s(1个小时)   1(key的一个变化)     300s(5分钟)  100(key的变化)    60s(1分钟)  10000(key的变化)
key的变化越快，保存的就越频繁。 60s中 key变化了10000个，那么我1分钟就会给你存上， 1小时才变化一个key，就1小时给你存一次
更新得越频繁，保存得越频繁。另外，关闭redis服务器会立马触发rdb存储  

验证一下rdb持久化存储：
## redis-cli -a redispwd                                                      #登录redis先设置一些数据
> set k1 v1
> set k2 v2
> set k3 v3
> keys *
1) "k3"
2) "k2"
3) "k1"
> quit 
## ls /data/redis/
dump.rdb  redis.log  redis.pid

## systemctl stop redis                                                   #停止redis，将持久化存储文件模拟删除
## mv /data/redis/dump.rdb /data/redis/dump.rdb.bak
## ls /data/redis/
dump.rdb.bak  redis.log
## systemctl start redis                                                 #再重新启动redis
## redis-cli -a redispwd                                                 #发现持久化数据文件删除后，数据丢失
> keys *
(empty array)
> quit
恢复数据:
## systemctl stop redis
## mv /data/redis/dump.rdb.bak /data/redis/dump.rdb
## systemctl start redis
## redis-cli -a redispwd
> keys *
1) "k3"
2) "k1"
3) "k2"

设置关闭rdb：需要先删除dump.rdb文件
>config set save ""                       #关闭rdb快照持久化存储,测试的不好使
>config get save                          #查看
>config rewrite                            #写入配置文件，永久设置                           
>config set rdbcompression no      #rdb文件需不需要压缩，当磁盘空间比较大时候，可以设置不用压缩

通过修改配置文件关闭rdb持久化:  
## vi /etc/redis.conf
save ""                                      #添加
#注释下面的：
#save 3600 1
#save 300 100
#save 60 10000
```



#### 案例：关闭rdb持久化


```shell
## rm -f /data/redis/dump.rdb         #先删除rdb快照文件，否则即使关闭持久化，还会通过快照给还原过来
## vim /etc/redis.conf
save ""                                        #添加，关闭持久化
## systemctl restart redis                #重启redis
## redis-cli -a redispwd
> CONFIG GET save                     #查看rdb持久化配置为空
1) "save"
2) ""
> set k11 v11                              #增加几个key的数据
> set k12 v12
> keys *                                      #查看key
1) "k12"
2) "k11"
> quit
## systemctl restart redis               #重启redis
## redis-cli -a redispwd                  #重新登录redis，发现重启后数据丢失
> keys *    
(empty array)
```



### 3.Redis的AOF持久化存储


```shell
AOF存储默认是关闭的
AOF存储是把命令直接写入到文件中，文件会不断扩大

1).开启AOF前先关闭RDB（一般建议关闭，持久化存储用其中一种就行)，也能同时配置，同时配置AOF优先生效
## vim /etc/redis.conf
save ""                                            #添加
#注释下面的：
#save 3600 1
#save 300 100
#save 60 10000
## systemctl restart redis
2).开启AOF存储方式:
>config get append*                        #查看AOF状态，默认是关闭的
1) "appendonly"
2) "no"
>config set appendonly yes               #开启AOF存储
>config rewrite                                #写入配置文件
```



#### 案例：开启AOF存储方式持久化存储


```shell
>config get append*                        #查看AOF状态，默认是关闭的
1) "appendonly"
2) "no"
3) "appendfilename"
4) "appendonly.aof"
5) "appendfsync"
6) "everysec"
>config set appendonly yes               #开启AOF存储
>config rewrite                                #写入配置文件
## grep appendonly /etc/redis.conf      #查看redis配置文件
appendonly yes
appendfilename "appendonly.aof"
## ls /data/redis/appendonly.aof         #查看AOF文件的路径
/data/redis/appendonly.aof
## redis-cli -a redispwd                     #登录redis写入测试数据
> set a1 b1
> set a2 b2
> keys *
1) "a2"
2) "a1"
## tail -12 /data/redis/appendonly.aof    #查看AOF文件记录的命令
set
$2
a1
$2
b1
*3
$3
set
$2
a2
$2
b2
## systemctl restart redis                        #重启redis
## redis-cli -a redispwd                           #重新登录redis，数据还在，数据持久化没问题
> keys *
1) "a1"
2) "a2"
> get a1
"b1"

3).AOF存储是把命令直接写入到文件中，文件会不断扩大
>set a b
>set a b
...
#ll /data/redis/appendonly.aof              #文件是一直在增大的

4).AOF文件的重写
当AOF文件增大到一定程度，我们可以对他进行重写，重写AOF文件可以减小AOF文件的大小，数据不会减少

5).重写方式有两种：手动重写和自动重写
手动重写：
> BGREWRITEAOF                               #手动重写AOF文件，重写后AOF文件会减小

自动重写：
> config get *aof*                               #查看自动重写AOF文件的条件，重写后AOF文件会减小
 1) "aof-rewrite-incremental-fsync"
 2) "yes"
 3) "aof-load-truncated"
 4) "yes"
 5) "aof-use-rdb-preamble"
 6) "yes"
 7) "aof_rewrite_cpulist"
 8) ""
 9) "auto-aof-rewrite-percentage"
10) "100"                                         #当达到100%增量的时候会触发AOF重写
11) "auto-aof-rewrite-min-size"
12) "67108864"                                 #AOF文件>67M时候触发AOF重写
13) "replicaof"
14) ""
自动重写的条件：重写条件是aof文件大小>67M，aof文件增大了一倍


案例演示： 手动重写
## ls -l /data/redis/appendonly*         #先查看一下AOF文件的大小
## redis-cli -a redispwd                     #登录下redis，手动触发重写
> BGREWRITEAOF                          #手动重写AOF文件
## ls -l /data/redis/appendonly*         #再查看一下AOF文件的大小，发现会减小


案例演示： 自动重写
## ls -lh /data/redis/appendonly*        #先查看一下AOF文件的大小
刚开始比较小
## redis-benchmark -a redispwd         #使用压测工具触发写入数据，使AOF文件增sh大    
## ls -lh /data/redis/appendonly*        #不断查看AOF文件的大小，发现逐渐增大，当>67M后，会变小，说明达到触发条件后，进行了自动重写
## ls -lh /data/redis/appendonly*
## ......


注意:自动触发重写  在业务高峰压力大，如果采用自动触发重写，有可能会影响业务，可选择在压力小的时候脚本运行BGREWRITEAOF
```



### 10.使用redis的RDB工具分析key的大小


### 1.什么是Redis的大key？（BigKey）


```shell
1.什么是Redis的大key？（BigKey）
redis存储数据的时候，当某个key的值比较大（包括字符串、列表等数据类型），key的数据越大，占用的内存和空间就越多。
BigKey（大key）
Bigkey指的是redis中一些key value值很大,这些key在序列化与反序列化过程中花费的时间很大!
      操作bigkey的通常比较耗时，也就意味着阻塞Redis可能性越大!占用的流量同时也会变得很大!
      大白话就是：bigkey实际指一个key对应的value很大,占用的空间很大!
string类型的数据：   长度大于10K，认为是大key
list列表类型的数据： 长度大于10240，认为是大key
```



### 2.制造两个不同数据类型的大key


```shell
批量写入1万个key，为了验证一下普通key和大key占用内存的情况，数据量小的时候，不好对比
for i in $(seq -w 10000);do redis-cli -a redispwd set name${i} test${i}; redis-cli -a redispwd get name${i}; done 2>/dev/null

字符串类型的大key：                      #制造一个字符串类型的大key
> set k1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

列表类型的大key:                             #制造一个列表类型的大key
> LPUSH name yyyyyyyy
> LPUSH name yyyyyyyy
> LPUSH name yyyyyyyy
> LPUSH name yyyyyyyy
> LPUSH name yyyyyyyy
> LPUSH name yyyyyyyy
> LPUSH name yyyyyyyy
....
列表左边添加元素，多添加一些

> keys *
1) "name"
2) "k1"
3) "namexxx"
......

127.0.0.1:6379> LLEN name
(integer) 15
127.0.0.1:6379> LRANGE name 0 -1
 1) "yyyyyyyy"
 2) "yyyyyyyy"
 3) "yyyyyyyy"
 4) "yyyyyyyy"
 5) "yyyyyyyy"
 6) "yyyyyyyy"
 7) "yyyyyyyy"
 8) "yyyyyyyy"
 9) "yyyyyyyy"
10) "yyyyyyyy"
11) "yyyyyyyy"
12) "yyyyyyyy"
13) "yyyyyyyy"
14) "yyyyyyyy"
15) "yyyyyyyy"
```



### 3.扫描和分析大key


#### 方法1：


```shell
## redis-cli -a redispwd --bigkeys                                                                #扫描和分析redis的大key工具
....
[00.00%] Biggest string found so far '"name07194"' with 9 bytes
[14.78%] Biggest list   found so far '"name"' with 15 items
[83.13%] Biggest string found so far '"k1"' with 216 bytes
...
-------- summary -------
Sampled 10002 keys in the keyspace!
Total key length in bytes is 90006 (avg len 9.00)
Biggest   list found '"name"' has 15 items
Biggest string found '"k1"' has 216 bytes
```



#### 方法2：


```shell
使用rdb工具分析大key（是通过dump.rdb文件进行分析的）
rdb分析所有key大小，建议拷贝到闲置的服务器进行分析
## yum -y install python36                                                                         #需要依赖python环境
## pip3 install rdbtools==0.1.15 -i https://mirrors.aliyun.com/pypi/simple/       #安装rdb工具
#  rdb -c memory /data/redis/dump.rdb >/tmp/test.csv     #使用rdb工具分析大key并把结果输出到一个文件里，指定rdb文件
有一个警告，可以忽略
## cat /tmp/test.csv |head -5                                                                    #查看文件，主要关心的是key和大小
database,type,key,size_in_bytes,encoding,num_elements,len_largest_element,expiry
0,string,name05565,72,string,9,9,
0,string,name07617,72,string,9,9,
0,string,name07090,72,string,9,9,
0,string,name03368,72,string,9,9,

大小排序
## cat /tmp/test.csv |sort -nrk 4 -t ',' |head -5         
0,list,name,289,quicklist,15,8,
0,string,k1,272,string,216,216,
0,string,name10000,72,string,9,9,
0,string,name09999,72,string,9,9,
0,string,name09998,72,string,9,9,
```



### 4.删除大key，观察性能分析，占用内存大的key已经消失


```shell
> DEL k1
用分析工具查看，该大key已经不显示

## redis-cli -a redispwd --bigkeys
...
[00.00%] Biggest string found so far '"name07052"' with 9 bytes
[28.76%] Biggest list   found so far '"name"' with 15 items
发现占用内存大的k1已经消失
```



### 11.redis主从复制


```shell
1.Redis单台服务器时的缺点
如果持久化，单台数据有丢失风险
读写压力都集中在一台上

2.Redis的主从复制概念
Redis的主从就是多台Redis数据一致
主服务器可用来写入和读取，从服务器仅用来读取，可以通过读写分离，降低写服务器的压力

3.Redis的主从搭建
主redis的配置：
## vim /etc/redis.conf
除了默认配置外，需要确定一下下面的配置:
bind 0.0.0.0
port 6379
dir "/data/redis"
requirepass "redispwd"
pidfile "redis.pid"
logfile "redis.log"
daemonize yes

从redis的配置：
## vim /etc/redis.conf
除了默认配置外，需要确定一下下面的配置:
bind 0.0.0.0
port 6379
dir "/data/redis"
requirepass "redispwd"                   #从redis自己的密码，一般也和主设置的相同
pidfile "redis.pid"
logfile "redis.log"
daemonize yes
                                                      #注意：从redis需要增加下面这两项：
slaveof 192.168.107.222 6379              #指定主redis的ip和端口        
masterauth "redispwd"                      #指定主redis的密码

主从redis的启动：
启动主redis:  ## redis-server /etc/redis.conf
启动从redis:  ## redis-server /etc/redis.conf

验证redis主从：  在主redis上写入数据，在从redis上查看数据是否能同步过来
```



### 12.redis的哨兵模式主从自动切换


### 1.查看主从状态信息


```shell
在主redis上登录查看：  （192.168.107.222）
> info Replication
## Replication
role:master
connected_slaves:1
slave0:ip=192.168.107.223,port=6379,state=online,offset=699,lag=1
master_failover_state:no-failover
master_replid:a4130be34d9eed50eb27ca80a779f59ad993045c
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:699
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:699

在从1redis上登录查看：（192.168.107.223）
> info Replication
## Replication
role:slave
master_host:192.168.107.222
master_port:6379
master_link_status:up
master_last_io_seconds_ago:1
master_sync_in_progress:0
slave_read_repl_offset:783
slave_repl_offset:783
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:a4130be34d9eed50eb27ca80a779f59ad993045c
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:783
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:783

在从2redis上登录查看：（192.168.107.224）
> info Replication
## Replication
role:slave
master_host:192.168.107.222
master_port:6379
master_link_status:up
master_last_io_seconds_ago:4
master_sync_in_progress:0
slave_read_repl_offset:378
slave_repl_offset:378
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:d27ba1044b42b5d58d368229eea4af83a6da38c8
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:378
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:71
repl_backlog_histlen:308
```



### 2.哨兵Sentinel实现主从自动切换


```shell
主从自动切换
Redis主从配置后，当主挂掉后，业务会有异常
Redis提供Sentinel工具实现主从自动切换，实现redis的高可用
Sentinel的启动和观察
## redis-sentinel /etc/sentinel.conf
主挂掉后，从库自动提升为主库主恢复后，自动转为从库，预防来回切换。
要求主从都需要设置masterauth 连接主redis的密码
因为是高可用模式，主也有可能宕机，当它宕机后，即使再恢复后也是作为从角色，为了防止作为从角色时候，
连接主时候认证不了，需要提前加上连接主服务器的认证密码
```



### 3.哨兵Sentinel高可用模式搭建（1主2从3哨兵）


```shell
为了防止哨兵的单节点故障，一般哨兵也做成高可用形式，即多个哨兵同时监控redis的状态，当其中一个哨兵故障时候，其他哨兵也能继续监控。
为了方便哨兵的选举，一般哨兵也是设置成奇数个。一般3个哨兵就没问题。
注意：一般哨兵的部署尽量不要和redis部署在同一台，防止这一台机器挂了后，redis和哨兵同时挂掉，哨兵起不到哨兵的作用了。当然多台机器，
多个哨兵时候也不影响，一台哨兵挂了，还有其它哨兵。
规划：
192.168.107.222   主redis    哨兵1
192.168.107.223   从1redis  哨兵2
192.168.107.224   从2redis  哨兵3

1).先搭建redis的主从（1主2从，前面已经介绍，略)
在主redis上登录查看：  （192.168.107.222）
127.0.0.1:6379> info Replication
## Replication
role:master
connected_slaves:2
slave0:ip=192.168.107.223,port=6379,state=online,offset=3216,lag=1
slave1:ip=192.168.107.224,port=6379,state=online,offset=3216,lag=1
在从1redis上登录查看：（192.168.107.223）
127.0.0.1:6379> info Replication
## Replication
role:slave
master_host:192.168.107.222
master_port:6379
在从2redis上登录查看：（192.168.107.224）
127.0.0.1:6379> info Replication
## Replication
role:slave
master_host:192.168.107.222
master_port:6379

注意：主redis上配置文件中也需要加上下面配置：因为是高可用模式，主也有可能宕机，当它宕机后，即使再恢复后也是作为从角色为了防止作为从角色时候，连接主时候认证不了，需要提前加上连接主服务器的认证密码
## vi /etc/redis.conf     
masterauth "redispwd"                      #指定主redis的密码

2).配置3哨兵
## vi /etc/sentinel.conf                #3个哨兵机器配置都一样
bind 0.0.0.0
daemonize yes
port 26379
dir "/tmp"
logfile "sentinel.log"
sentinel monitor testmaster 192.168.107.222 6379 2
sentinel auth-pass testmaster redispwd
sentinel down-after-milliseconds testmaster 5000
sentinel failover-timeout testmaster 18000

配置文件说明:
#port 26379  哨兵的一个端口
#testmaster是随便起的一个名字,连接的主redis的是:192.168.107.222, 2是代表有2个哨兵认为master有问题才会切换
#redispwd 是连接主redis的密码,      5000 是5秒没响应认为主挂了
#18000 是从提升为主的超时时间18s(可适当调大)

3).启动3哨兵
## redis-sentinel /etc/sentinel.conf      3台都是指定配置文件启动
## ps -ef |grep sentinel                     3台查看进程
root       1742      1  0 11:32 ?        00:00:00 redis-sentinel 0.0.0.0:26379 [sentinel]

4).验证哨兵实现的高可用redis
a).停止主redis服务              192.168.107.222机器停止主redis
## systemctl stop redis            

b).查看其他两个从redis，其中一个已经提升为主
查看从1redis 192.168.107.2233
> info Replication
## Replication
role:master
connected_slaves:1
slave0:ip=192.168.107.224,port=6379,state=online,offset=15033,lag=0
master_failover_state:no-failover
master_replid:3b0ca2f0c9791e973bda766dcee2f91589cce2cf
master_replid2:2423087d35cac94a66bf8f88462c332220b501d5
master_repl_offset:15033
second_repl_offset:12498
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:15033

查看从2redis 192.168.107.224
> info Replication
## Replication
role:slave
master_host:192.168.107.223
master_port:6379
master_link_status:up
master_last_io_seconds_ago:1
master_sync_in_progress:0
slave_read_repl_offset:27010
slave_repl_offset:27010
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:3b0ca2f0c9791e973bda766dcee2f91589cce2cf
master_replid2:2423087d35cac94a66bf8f88462c332220b501d5
master_repl_offset:27010
second_repl_offset:12498
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:27010

并且查看从2redis的配置文件也自动修改成了指定了新主的ip
## tail -2 /etc/redis.conf              #slaveof和replicaof是一样的
replicaof 192.168.107.223 6379
masterauth "redispwd"

c).当主redis恢复，自动作为从服务器，指向新的主redis
## systemctl start redis
## redis-cli -a redispwd
> info Replication
## Replication
role:slave
master_host:192.168.107.223
master_port:6379
master_link_status:up
master_last_io_seconds_ago:0
master_sync_in_progress:0
slave_read_repl_offset:49223
slave_repl_offset:49223
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:3b0ca2f0c9791e973bda766dcee2f91589cce2cf
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:49223
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:48319
repl_backlog_histlen:905


查看原主的配置文件，也进行了修改，重新指定的新的主redis
## tail -2 /etc/redis.conf 
masterauth "redispwd"
replicaof 192.168.107.223 6379



5).验证一下哨兵的高可用性：
a).在原主(192.168.107.222)那台机器上，杀死一个哨兵，模式一个哨兵服务挂掉
## ps -ef |grep sen
root       1742      1  0 11:32 ?        00:00:03 redis-sentinel 0.0.0.0:26379 [sentinel]
root       1779   1362  0 11:47 pts/0    00:00:00 grep --color=auto sen
## kill 1742
## ps -ef |grep sen
root       1781   1362  0 11:47 pts/0    00:00:00 grep --color=auto sen

b).新主redis服务停止：（192.168.107.223）
## systemctl stop redis

c).其他两个从redis查看主从状态（192.168.107.222和192.168.107.224）
192.168.107.222（原主)查看：     可以查看到自己是从，又重新选出了一个新主130机器
127.0.0.1:6379> info Replication
## Replication
role:slave
master_host:192.168.107.224
master_port:6379
master_link_status:up
master_last_io_seconds_ago:2
master_sync_in_progress:0
slave_repl_offset:221763
slave_priority:100
slave_read_only:1
connected_slaves:0
master_failover_state:no-failover
master_replid:56cd835f2f4f8eee9eb1dc711f8b8e57a8b06db7
master_replid2:7ffd1c6815695fef04fce6a7b1ff705f7b8a368e
master_repl_offset:221763
second_repl_offset:210754
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:143078
repl_backlog_histlen:78686
192.168.107.224   #（原从2）上查看：       自己已经变成了主
127.0.0.1:6379> info Replication
## Replication
role:master
connected_slaves:1
slave0:ip=192.168.107.222,port=6379,state=online,offset=244883,lag=1
master_failover_state:no-failover
master_replid:56cd835f2f4f8eee9eb1dc711f8b8e57a8b06db7
master_replid2:7ffd1c6815695fef04fce6a7b1ff705f7b8a368e
master_repl_offset:244883
second_repl_offset:210754
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:15
repl_backlog_histlen:244869

通过这个案例，我们可以看到当其中一个哨兵挂掉后，其他哨兵照样可以监控监控redis，实现redis的高可用性
多哨兵模式也是为了加强哨兵服务的健壮性
```



### 13.redis cluster集群搭建和高可用故障切换演示


### 1.Redis主从模式和cluster分片集群区别


```plain
redis主从模式，是所有Redis数据一致，但是key过多了会影响性能
cluster分片集群，可以将数据分散到多个Redis节点，数据分片存储，能够提高redis的吞吐量
```



### 2.Redis Cluster集群特点


```plain
数据分片
多个入口
故障自动切换
```



### 3.Redis cluster集群的搭建架构


```shell
Redis集群至少需要三主三从
三从是保证主有问题时能够切换
```



### 4.Redis自带集群搭建


#### a).目录和机器规划
| 目录 | /data/cluster | | |
| :---: | :---: | --- | --- |
| 三主 | 192.168.107.222:7000 | 192.168.107.223:7001 | 192.168.107.224:7002 |
| 三从 | 192.168.107.222:8000(7002的从) | 192.168.107.223:8001(7000的从) | 192.168.107.224:8002(7001的从) |




注意：上面设计是为了避免主从都在同一个节点，防止同一个节点挂了后，主从都挂掉，就没法进行主从切换，导致数据丢失



#### b).修改redis的配置文件


```shell
6台redis配置都一样，只是下面两项：端口和路径不一样
redis0上
## mkdir -p /data/cluster/7000
## mkdir -p /data/cluster/8000
redis1上
## mkdir -p /data/cluster/7001
## mkdir -p /data/cluster/8001
redis2上
## mkdir -p /data/cluster/7002
## mkdir -p /data/cluster/800
## vi /data/cluster/7000/redis.conf          各自目录下创建配置文件: 7000 7001  7002  8000  8001  8002
下面配置中注意port和dir的端口和文件目录
```



```shell
cluster-enabled yes
port 7000               
dir "/data/cluster/7000"
logfile "redis.log"
pidfile "redis.pid"
daemonize yes
bind 0.0.0.0
requirepass redispwd
masterauth redispwd
tcp-backlog 1024
tcp-keepalive 0
loglevel notice
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
save 900 1
save 300 10
save 60 10000
dbfilename "dump.rdb"
slave-serve-stale-data yes
slave-read-only yes
repl-diskless-sync no
repl-diskless-sync-delay 5
repl-disable-tcp-nodelay no
slave-priority 100
appendonly no
appendfilename "appendonly.aof"
appendfsync everysec
no-appendfsync-on-rewrite yes
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
aof-load-truncated yes
lua-time-limit 5000
slowlog-log-slower-than 10000
slowlog-max-len 128
latency-monitor-threshold 0
notify-keyspace-events ""
hash-max-ziplist-entries 512
hash-max-ziplist-value 64
list-max-ziplist-entries 512
list-max-ziplist-value 64
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
hll-sparse-max-bytes 3000
activerehashing yes
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
hz 10
aof-rewrite-incremental-fsync yes
```



#### c).先搭建3主集群


```shell
(1).先启动3个主redis   192.168.107.222:7000      192.168.107.223:7001       192.168.107.224:7002
222上：
## redis-server /data/cluster/7000/redis.conf 
## ps -ef |grep redis
root       2285      1  1 22:55 ?        00:00:00 redis-server 0.0.0.0:7000 [cluster]
root       2226   1362  0 22:55 pts/0    00:00:00 grep --color=auto redis

223上：
## redis-server /data/cluster/7001/redis.conf 
## ps -ef |grep redis
root       4385      1  0 22:56 ?        00:00:00 redis-server 0.0.0.0:7001 [cluster]
root       4354   1356  0 22:56 pts/0    00:00:00 grep --color=auto redis

224上：
## redis-server /data/cluster/7002/redis.conf 
## ps -ef |grep redis
root       2298      1  0 22:57 ?        00:00:00 redis-server 0.0.0.0:7002 [cluster]
root       2270   1370  0 22:57 pts/0    00:00:00 grep --color=auto redis

(2).创建3主集群，在任何一个节点上操作都可以
## redis-cli -a redispwd --cluster create 192.168.107.222:7000 192.168.107.223:7001 192.168.107.224:7002
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Performing hash slots allocation on 3 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
...
>>> Performing Cluster Check (using node 192.168.107.222:7000)
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.


(3).查看3主集群：  在任何一个节点上操作都行，下面以7000端口这个redis为例查看集群信息
## redis-cli -a redispwd -p 7000 cluster info
## redis-cli -a redispwd -p 7000 cluster nodes   #注意slot分配

## redis-cli -a redispwd -p 7000 cluster info
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
cluster_state:ok
cluster_slots_assigned:16384
cluster_slots_ok:16384
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:3
cluster_size:3
cluster_current_epoch:3
cluster_my_epoch:1
cluster_stats_messages_ping_sent:174
cluster_stats_messages_pong_sent:169
cluster_stats_messages_sent:343
cluster_stats_messages_ping_received:167
cluster_stats_messages_pong_received:174
cluster_stats_messages_meet_received:2
cluster_stats_messages_received:343

## redis-cli -a redispwd -p 7000 cluster nodes 
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693043947714 2 connected 5461-10922
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693043945000 1 connected 0-5460
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693043946704 3 connected 10923-16383


(4).集群操作，在集群中写入数据   在任何一个节点作为入口都可以，下面以222:7000端口的redis为例写入数据
集群操作需要加-c参数
## redis-cli -p 7000 -a redispwd              #不加-c参数，表示不是以集群方式写入，无法写入    
## redis-cli -p 7000 -a redispwd -c          #增加-c参数，表示是以集群方式写入，可以写入
127.0.0.1:7000> set k1 v1
-> Redirected to slot [12706] located at 192.168.107.224:7002     #可以看到该key,k1是存放到130:7002的redis
OK
192.168.107.224:7002> set k2 v2
-> Redirected to slot [449] located at 192.168.107.222:7000         #可以看到该key,k2是存放在本机128:7000的redis，可以看出数据是分布存储
OK
192.168.107.222:7000> keys *                                                #在128:7000的redis可以看到只存储了k2,是按槽位分配数据,不是按节点分配
1) "k2"
192.168.107.222:7000> get k2
"v2"

在224:7002redis上可以查看存储的另一个k1
## redis-cli -p 7002 -a redispwd -c
127.0.0.1:7002> keys *
1) "k1"
127.0.0.1:7002> get k1
"v1"
```



#### d).增加搭建3从集群，实现redis高可用


```shell
(1).先启动3个从redis   192.168.107.222:8000      192.168.107.223:8001       192.168.107.224:8002
222上：
## redis-server /data/cluster/8000/redis.conf 
## ps -ef |grep redis
root       2285      1  0 23:35 ?        00:00:00 redis-server 0.0.0.0:7000 [cluster]
root       2301      1  0 23:41 ?        00:00:00 redis-server 0.0.0.0:8000 [cluster]
root       2307   1362  0 23:41 pts/0    00:00:00 grep --color=auto redis

223上：
## redis-server /data/cluster/8001/redis.conf 
## ps -ef |grep redis
root       4385      1  0 23:36 ?        00:00:00 redis-server 0.0.0.0:7001 [cluster]
root       4404      1  1 23:42 ?        00:00:00 redis-server 0.0.0.0:8001 [cluster]
root       4410   1356  0 23:42 pts/0    00:00:00 grep --color=auto redis

224上：
## redis-server /data/cluster/8002/redis.conf 
## ps -ef |grep redis
root       2298      1  0 23:36 ?        00:00:00 redis-server 0.0.0.0:7002 [cluster]
root       2311      1  0 23:42 ?        00:00:00 redis-server 0.0.0.0:8002 [cluster]
root       2317   1370  0 23:42 pts/0    00:00:00 grep --color=auto redis

(2).分别给3个主节点添加从库，在任何一节操作即可，下面以在128:7000的redis为例操作
别忘了主从的规划：
三主： 192.168.107.222:7000                     192.168.107.223:7001                       192.168.107.224:7002
三从： 192.168.107.222:8000(7002的从)      192.168.107.223:8001(7000的从)       192.168.107.224:8002(7001的从)
注意：上面设计是为了避免主从都在同一个节点，防止同一个节点挂了后，主从都挂掉，就没法进行主从切换，导致数据丢失

## redis-cli -a redispwd -p 7000 cluster nodes                                                       #查看集群的各个节点状态和master-id                
## redis-cli -a redispwd --cluster add-node --cluster-slave --cluster-master-id  7000的master-id  192.168.107.223:8001 192.168.107.222:7000
## redis-cli -a redispwd --cluster add-node --cluster-slave --cluster-master-id  7001的master-id  192.168.107.224:8002 192.168.107.223:7001
## redis-cli -a redispwd --cluster add-node --cluster-slave --cluster-master-id  7002的master-id  192.168.107.222:8000 192.168.107.224:7002

给3主分别加入从节点操作：
## redis-cli -a redispwd -p 7000 cluster nodes
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693044296068 2 connected 5461-10922
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693044297000 1 connected 0-5460
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693044298089 3 connected 10923-16383

222master-id:c4acfb2490f7557a5e1857118360bddfaa523c9f
223master-id:ff50bb210c08f3bd453201150be381bcb3b4f05f
224master-id:2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095
注意：下面命令中后面两个ip顺序不能颠倒，分别对应的一组主从，ip顺序为:  从redis的ip:从端口   主redis的ip:主端口

## redis-cli -a redispwd --cluster add-node --cluster-slave --cluster-master-id  c4acfb2490f7557a5e1857118360bddfaa523c9f  192.168.107.223:8001 192.168.107.222:7000      #注意:后面两个ip的redis的顺序是不能颠倒的,否则加入不成功 
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Adding node 192.168.107.223:8001 to cluster 192.168.107.222:7000
>>> Performing Cluster Check (using node 192.168.107.222:7000)
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
>>> Send CLUSTER MEET to node 192.168.107.223:8001 to make it join the cluster.
Waiting for the cluster to join

>>> Configure node as replica of 192.168.107.222:7000.
[OK] New node added correctly.


## redis-cli -a redispwd --cluster add-node --cluster-slave --cluster-master-id  ff50bb210c08f3bd453201150be381bcb3b4f05f  192.168.107.224:8002 192.168.107.223:7001    #注意:后面两个ip的redis的顺序是不能颠倒的,否则加入不成功 
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Adding node 192.168.107.224:8002 to cluster 192.168.107.223:7001
>>> Performing Cluster Check (using node 192.168.107.223:7001)
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
S: ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001
   slots: (0 slots) slave
   replicates c4acfb2490f7557a5e1857118360bddfaa523c9f
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
>>> Send CLUSTER MEET to node 192.168.107.224:8002 to make it join the cluster.
Waiting for the cluster to join

>>> Configure node as replica of 192.168.107.223:7001.
[OK] New node added correctly.


## redis-cli -a redispwd --cluster add-node --cluster-slave --cluster-master-id  2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095   192.168.107.222:8000 192.168.107.224:7002    #注意:后面两个ip的redis的顺序是不能颠倒的,否则加入不成功 
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Adding node 192.168.107.222:8000 to cluster 192.168.107.224:7002
>>> Performing Cluster Check (using node 192.168.107.224:7002)
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
S: 0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002
   slots: (0 slots) slave
   replicates ff50bb210c08f3bd453201150be381bcb3b4f05f
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
S: ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001
   slots: (0 slots) slave
   replicates c4acfb2490f7557a5e1857118360bddfaa523c9f
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
>>> Send CLUSTER MEET to node 192.168.107.222:8000 to make it join the cluster.
Waiting for the cluster to join

>>> Configure node as replica of 192.168.107.224:7002.
[OK] New node added correctly.

加入从节点后查看节点状态和各自角色：  (在任何一个节点操作即可，下面以222:7000redis为例)
## redis-cli -a redispwd -p 7000 cluster nodes
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693044780000 1 connected 0-5460
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693044781775 3 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693044780000 2 connected 5461-10922
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693044782785 2 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693044779756 3 connected 10923-16383
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693044781000 1 connected
```



#### e).验证cluster集群主从的高可用切换


```shell
在任何一节操作即可，下面以在222:7000的redis为例操作
停止其中222:7000的主库redis，查看223:8001的从库是否能提升为主库：
## ps -ef |grep redis
root      11692      1  0 17:49 ?        00:00:02 redis-server 0.0.0.0:7000 [cluster]
root      15244      1  0 18:04 ?        00:00:00 redis-server 0.0.0.0:8000 [cluster]
root      19270   6833  0 18:16 pts/0    00:00:00 grep --color=auto redis
## kill 11692
## ps -ef |grep redis
root      15244      1  0 18:04 ?        00:00:01 redis-server 0.0.0.0:8000 [cluster]
root      19452   6833  0 18:16 pts/0    00:00:00 grep --color=auto redis

以222:8000的redis作为入口，查看节点状态和角色信息，原主222:7000宕机，对应的原从223:8001提升为了新主
## redis-cli -a redispwd -p 8000 cluster nodes
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693045033000 1 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693045034748 3 connected 10923-16383
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 master,fail - 1693045017576 1693045013538 1 disconnected 0-5460
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 myself,slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693045032000 3 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693045032000 2 connected 5461-10922
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693045034000 2 connected


当原主222:7000redis恢复，自动作为从角色：
## redis-server /data/cluster/7000/redis.conf 
## ps -ef |grep redis
root       2301      1  0 Nov15 ?        00:00:04 redis-server 0.0.0.0:8000 [cluster]
root       2355      1  0 00:22 ?        00:00:00 redis-server 0.0.0.0:7000 [cluster]
root       2362   1362  0 00:22 pts/0    00:00:00 grep --color=auto redis

## redis-cli -a redispwd -p 7000 cluster nodes
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,slave ffb3bd0c4d3fade126022f2f90691a9cbde30f16 0 1693045436000 4 connected
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 master - 0 1693045434216 4 connected 0-5460
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693045435000 2 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693045437245 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693045436234 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693045435226 3 connected 10923-16383


如果还是习惯于让原来主库作为作为主库，可以用下面命令，手动提升为主库。
从库手动提升为主库的方法： CLUSTER FAILOVER
登录原主库现从库redis:  222:7000
## redis-cli -a redispwd -p 7000
127.0.0.1:7000> info Replication
## Replication
role:slave
master_host:192.168.107.223
master_port:8001
127.0.0.1:7000> CLUSTER FAILOVER
OK
127.0.0.1:7000> info Replication
## Replication
role:master
connected_slaves:1

再次查看节点
## redis-cli -a redispwd -p 7000 cluster nodes
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693045574000 5 connected 0-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693045573000 5 connected
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693045574492 2 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693045575500 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693045576509 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693045573481 3 connected 10923-16383
```



### 14.redis cluster集群添加和删除节点


### 环境准备


```plain
在前面的基础上
增加一个主节点：  192.168.107.222:7003   从节点 192.168.107.222:7004  （正常主从不能在一台机器，此处只是演示)
```



### 添加节点


```shell

查看3主3从节点状态：
## redis-cli -a redispwd -p 7000 cluster nodes
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693048229000 5 connected 0-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693048231000 5 connected
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693048231478 2 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693048232487 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693048230000 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693048232000 3 connected 10923-16383

mkdir /data/cluster/7003
mkdir /data/cluster/7004

2.新增节点主、从redis先启动
## redis-server -v
Redis server v=6.2.1 sha=00000000:0 malloc=jemalloc-5.1.0 bits=64 build=3bc8e110479b329d
## mkdir /data/cluster/7003 -p
## mkdir /data/cluster/7004 -p
## cp /data/cluster/7000/redis.conf /data/cluster/7003/redis.conf /data/cluster/7004/redis.conf
修改redis的配置文件：                 所有节点的redis配置都一样，只是下面两项：端口和路径不一样
## vi /data/cluster/7003/redis.conf          各自目录下创建配置文件: 7003  7004
cluster-enabled yes
port 7003
dir "/data/cluster/7003"
logfile "redis.log"
pidfile "redis.pid"
daemonize yes
bind 0.0.0.0
requirepass redispwd
masterauth redispwd
tcp-backlog 1024
tcp-keepalive 0
loglevel notice
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
save 900 1
save 300 10
save 60 10000
dbfilename "dump.rdb"
slave-serve-stale-data yes
slave-read-only yes
repl-diskless-sync no
repl-diskless-sync-delay 5
repl-disable-tcp-nodelay no
slave-priority 100
appendonly no
appendfilename "appendonly.aof"
appendfsync everysec
no-appendfsync-on-rewrite yes
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
aof-load-truncated yes
lua-time-limit 5000
slowlog-log-slower-than 10000
slowlog-max-len 128
latency-monitor-threshold 0
notify-keyspace-events ""
hash-max-ziplist-entries 512
hash-max-ziplist-value 64
list-max-ziplist-entries 512
list-max-ziplist-value 64
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
hll-sparse-max-bytes 3000
activerehashing yes
client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
hz 10
aof-rewrite-incremental-fsync yes

启动两个新增准备作为主从的redis：
## redis-server /data/cluster/7003/redis.conf 
## redis-server /data/cluster/7004/redis.conf 
## ps -ef |grep redis
root      15244      1  0 18:04 ?        00:00:06 redis-server 0.0.0.0:8000 [cluster]
root      21855      1  0 18:23 ?        00:00:05 redis-server 0.0.0.0:7000 [cluster]
root      46238      1  0 19:31 ?        00:00:00 redis-server 0.0.0.0:7003 [cluster]
root      46286      1  0 19:31 ?        00:00:00 redis-server 0.0.0.0:7004 [cluster]
root      46352   6833  0 19:32 pts/0    00:00:00 grep --color=auto redis



2.在redis集群中加入一个新的主节点（在任意一台集群的节点操作即可，此处在128:7000的节点操作)
## redis-cli -a redispwd --cluster add-node 新节点ip:新节点端口 集群任意主节点ip:集群任意主节点对应端口    
操作:
## redis-cli -a redispwd --cluster add-node 192.168.107.222:7003 192.168.107.222:7000          
#在128:7000节点操作，加入新主节点，131:7003
WWarning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Adding node 192.168.107.222:7003 to cluster 192.168.107.222:7000
>>> Performing Cluster Check (using node 192.168.107.222:7000)
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
S: ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001
   slots: (0 slots) slave
   replicates c4acfb2490f7557a5e1857118360bddfaa523c9f
S: 0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002
   slots: (0 slots) slave
   replicates ff50bb210c08f3bd453201150be381bcb3b4f05f
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
S: e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000
   slots: (0 slots) slave
   replicates 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
>>> Send CLUSTER MEET to node 192.168.107.222:7003 to make it join the cluster.
[OK] New node added correctly.

>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
>>> Send CLUSTER MEET to node 192.168.27.131:7003 to make it join the cluster.
[OK] New node added correctly.

查看集群节点信息：
## redis-cli -a redispwd -p 7000 cluster nodes
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693049633000 5 connected 0-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693049637676 5 connected
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693049636666 2 connected
c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 master - 0 1693049636000 0 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693049635000 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693049635000 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693049638684 3 connected 10923-16383


192.168.107.222:7003 master-id:c8f152ea7f6f436a96af0a3364e721ff108fb20b
2.在redis集群中加入一个新的从节点（在任意一台集群的节点操作即可，注意后面两个ip顺序即可，此处在128:7000节点机器操作)
注意：下面命令中后面两个ip顺序不能颠倒，分别对应的一组主从，ip顺序为:  从redis的ip:从端口   主redis的ip:主端口
## redis-cli -a redispwd --cluster add-node --cluster-slave --cluster-master-id  c8f152ea7f6f436a96af0a3364e721ff108fb20b  192.168.107.222:7004 192.168.107.222:7003        
#注意:后面两个ip的redis的顺序是不能颠倒的,否则加入不成功 
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Adding node 192.168.107.222:7004 to cluster 192.168.107.222:7003
>>> Performing Cluster Check (using node 192.168.107.222:7003)
M: c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003
   slots: (0 slots) master
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
S: 0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002
   slots: (0 slots) slave
   replicates ff50bb210c08f3bd453201150be381bcb3b4f05f
S: ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001
   slots: (0 slots) slave
   replicates c4acfb2490f7557a5e1857118360bddfaa523c9f
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
S: e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000
   slots: (0 slots) slave
   replicates 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
>>> Send CLUSTER MEET to node 192.168.107.222:7004 to make it join the cluster.
Waiting for the cluster to join

>>> Configure node as replica of 192.168.107.222:7003.
[OK] New node added correctly.


查看集群节点信息：发现新增加主从节点没有问题，原来主节点都分配了槽位，但新主节点没有分配槽位，所以也不会有数据
## redis-cli -a redispwd -p 7000 cluster nodes
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693049742000 5 connected 0-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693049745622 5 connected
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693049742000 2 connected
c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 master - 0 1693049743000 0 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693049743000 2 connected 5461-10922
61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 192.168.107.222:7004@17004 slave c8f152ea7f6f436a96af0a3364e721ff108fb20b 0 1693049743604 0 connected
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693049744613 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693049744000 3 connected 10923-16383



3.给新加主redis分配槽位 （在集群中任何一个节点操作即可，此处以222:7000节点上操作）
注意槽位分配，可以将某个节点槽位分到新节点，也可将所有主节点再做一个平均分配，此处是从128:7000主节点的槽位移动到新主节点一部分）
## redis-cli -a redispwd --cluster reshard 192.168.107.222:7000    #连接集群中任意一个节点的redis
## redis-cli -a redispwd --cluster reshard 192.168.107.222:7000 
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Performing Cluster Check (using node 192.168.107.222:7000)
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[0-5460] (5461 slots) master
   1 additional replica(s)
S: ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001
   slots: (0 slots) slave
   replicates c4acfb2490f7557a5e1857118360bddfaa523c9f
S: 0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002
   slots: (0 slots) slave
   replicates ff50bb210c08f3bd453201150be381bcb3b4f05f
M: c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003
   slots: (0 slots) master
   1 additional replica(s)
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
S: 61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 192.168.107.222:7004
   slots: (0 slots) slave
   replicates c8f152ea7f6f436a96af0a3364e721ff108fb20b
S: e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000
   slots: (0 slots) slave
   replicates 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
How many slots do you want to move (from 1 to 16384)? 2000   #要分配出去多少个槽位
What is the receiving node ID? c8f152ea7f6f436a96af0a3364e721ff108fb20b    #接收的redis的id的节点，222:7003
Please enter all the source node IDs.
  Type 'all' to use all the nodes as source nodes for the hash slots.
  Type 'done' once you entered all the source nodes IDs.
Source node #1: c4acfb2490f7557a5e1857118360bddfaa523c9f    #从哪个节点id移动过去,all是所有节点平均分,此处选从128:7000节点移过去
Source node #2: done                             #也可以选择从多个节点id移动过去,可输入多个节点id，此处选一个,如果选择节点完成就输入done
....
Do you want to proceed with the proposed reshard plan (yes/no)? yes    #输入yes，他就会帮我们移动
...

移动完槽位后，重新查看集群节点和槽位信息：（在任意一个节点操作，此处以222:7000节点操作)
## redis-cli -a redispwd -p 7000 cluster nodes      #发现槽位从222:7000节点分走了2000个槽位给222:7003节点
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693050081000 5 connected 2000-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693050083000 5 connected
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693050084594 2 connected
c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 master - 0 1693050083585 7 connected 0-1999
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693050085000 2 connected 5461-10922
61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 192.168.107.222:7004@17004 slave c8f152ea7f6f436a96af0a3364e721ff108fb20b 0 1693050085602 7 connected
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693050083000 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693050081565 3 connected 10923-16383


4.给新主从redis写入数据，验证能正常存放和获取数据 （在集群中任何一个节点操作即可，此处以222:7000节点上操作）
## redis-cli -a redispwd -h 192.168.107.222 -p 7003 -c
192.168.107.222:7003> set k1 v1
-> Redirected to slot [12706] located at 192.168.107.224:7002                     #存的key在主节点224:7002
OK
192.168.107.222:7003> set k2 v2
-> Redirected to slot [449] located at 192.168.107.222:7003                         #存的key在主节点222:7003   
OK
192.168.107.222:7003>  get k1
-> Redirected to slot [12706] located at 192.168.107.224:7002
"v1"

192.168.107.224:7002> get k2
-> Redirected to slot [449] located at 192.168.107.222:7003
"v2"


5.验证新主从redis的高可用切换（集群信息查看可在任意节点，停止新主redis在192.168.107.222上操作)
1).停掉新主redis服务，查看新从提升为主
## ps -ef |grep redis                     #在新主222:7003上操作
root      15244      1  0 18:04 ?        00:00:08 redis-server 0.0.0.0:8000 [cluster]
root      21855      1  0 18:23 ?        00:00:07 redis-server 0.0.0.0:7000 [cluster]
root      46238      1  0 19:31 ?        00:00:02 redis-server 0.0.0.0:7003 [cluster]
root      46286      1  0 19:31 ?        00:00:01 redis-server 0.0.0.0:7004 [cluster]
root      51697   6833  0 19:46 pts/0    00:00:00 grep --color=auto redis

## kill -9 46238                                   #停止新主131:7003节点
## ps -ef |grep redis
root      15244      1  0 18:04 ?        00:00:08 redis-server 0.0.0.0:8000 [cluster]
root      21855      1  0 18:23 ?        00:00:07 redis-server 0.0.0.0:7000 [cluster]
root      46286      1  0 19:31 ?        00:00:01 redis-server 0.0.0.0:7004 [cluster]
root      52095   6833  0 19:48 pts/0    00:00:00 grep --color=auto redis


## redis-cli -a redispwd -p 7004 cluster nodes     #查看集群节点信息，在新从后提升为主的222:7004上操作，发现新从222:7004提升为新主
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693050507360 2 connected 5461-10922
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693050508371 2 connected
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 master - 0 1693050504000 5 connected 2000-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693050507000 5 connected
61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 192.168.107.222:7004@17004 myself,master - 0 1693050507000 8 connected 0-1999
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693050506351 3 connected
#c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 master,fail - 1693050484145 1693050477078 7 disconnected 该主节点已经关闭
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693050509381 3 connected 10923-16383


6.新主恢复，自动转为从角色（在新主从131上操作)
## redis-server /data/cluster/7003/redis.conf                          #原新主222:7003节点恢复
## ps -ef |grep redis
root      15244      1  0 18:04 ?        00:00:08 redis-server 0.0.0.0:8000 [cluster]
root      21855      1  0 18:23 ?        00:00:08 redis-server 0.0.0.0:7000 [cluster]
root      46286      1  0 19:31 ?        00:00:01 redis-server 0.0.0.0:7004 [cluster]
root      52830      1  0 19:50 ?        00:00:00 redis-server 0.0.0.0:7003 [cluster]
root      52916   6833  0 19:50 pts/0    00:00:00 grep --color=auto redis


## redis-cli -a redispwd -p 7004 cluster nodes             #查看集群节点信息，发现原新主131:7003自动以从角色运行
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693050644000 2 connected 5461-10922
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693050643000 2 connected
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 master - 0 1693050645638 5 connected 2000-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693050643000 5 connected
#61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 192.168.107.222:7004@17004 myself,master - 0 1693050643000 8 connected 0-1999
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693050642614 3 connected
#c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 slave 61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 0 1693050644631 8 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693050643623 3 connected 10923-16383


7.为了习惯，将原新主的从角色还提升为新主角色（在新主从222上操作)
## redis-cli -a redispwd -p 7003
127.0.0.1:7003> info Replication
## Replication
role:slave
master_host:192.168.107.222
master_port:7004
master_link_status:up
master_last_io_seconds_ago:5
master_sync_in_progress:0
slave_read_repl_offset:1368
slave_repl_offset:1368
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:e376ee8f88183d53b2abc9ee67de7f401c10668b
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:1368
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1243
repl_backlog_histlen:126
127.0.0.1:7003> CLUSTER FAILOVER       #从库手动提升为主库的方法
127.0.0.1:7003> info Replication
## Replication
role:master
connected_slaves:1
slave0:ip=192.168.107.222,port=7004,state=online,offset=1410,lag=0
master_failover_state:no-failover
master_replid:9f7be49d29cac1d9041ac124325f3bf5144d70a4
master_replid2:e376ee8f88183d53b2abc9ee67de7f401c10668b
master_repl_offset:1410
second_repl_offset:1411
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1243
repl_backlog_histlen:168
## redis-cli -a redispwd -p 7003 cluster nodes           #查看集群节点信息
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 192.168.107.222:7004@17004 slave c8f152ea7f6f436a96af0a3364e721ff108fb20b 0 1693050759196 9 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693050760000 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693050760206 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693050758000 3 connected 10923-16383
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693050757181 5 connected
c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 myself,master - 0 1693050758000 9 connected 0-1999
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693050758189 2 connected
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 master - 0 1693050759000 5 connected 2000-5460
```



### 删除节点


```shell
删除主节点和从节点（删除新主节点和新从节点，集群相关操作可在任意节点操作，此处在新主从222上操作)
1).Redis集群移除从库:     
移除从库格式：
## redis-cli -a redispwd --cluster del-node 对应主库的ip:主端口 对应从库的id    
从库移除之前可以有数据，但移除从库后会关闭从库，清空数据

## redis-cli -a redispwd -p 7003 cluster nodes           #查看集群的节点信息和id
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
#61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 192.168.107.222:7004@17004 slave c8f152ea7f6f436a96af0a3364e721ff108fb20b 0 1693050759196 9 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693050760000 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693050760206 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693050758000 3 connected 10923-16383
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693050757181 5 connected
#c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 myself,master - 0 1693050758000 9 connected 0-1999
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693050758189 2 connected
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 master - 0 1693050759000 5 connected 2000-5460


## redis-cli -a redispwd --cluster del-node 192.168.107.222:7003 61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24   #移除从库222:7004 
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Removing node 61c1c9eb632203b3a9e021a5bf8eb1d5cee1ca24 from cluster 192.168.107.222:7003
>>> Sending CLUSTER FORGET messages to the cluster...
>>> Sending CLUSTER RESET SOFT to the deleted node.

## redis-cli -a redispwd -p 7003 cluster nodes                #查看只有主库131:7003
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693050884000 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693050882000 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693050881000 3 connected 10923-16383
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693050885294 5 connected
c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 myself,master - 0 1693050881000 9 connected 0-1999
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693050883277 2 connected
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 master - 0 1693050884284 5 connected 2000-5460



2).Redis集群移除主库:  
注意：主节点如果有数据，是删除不掉的，删除之前先进行主节点数据的迁移，此处将新主131:7003还迁移回主节点128:7000
集群移除主节点的格式：
## redis-cli -a redispwd --cluster del-node 随便一个其他主节点:主端口  要移除主节点的id

## redis-cli -a redispwd -p 7003 cluster nodes      #查看集群节点信息
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
69d305ad0b4ba25b7d1d84c7ea7cb86218a28a8c 192.168.27.128:7000@17000 master - 0 1668694034612 5 connected 2000-5460
01ab5c82622921138dd28d2b2fd2772e4ad65041 192.168.27.131:7003@17003 myself,master - 0 1668693596000 8 connected 0-1999
122bfd4294666e2d60502f0466010783a9af12bd 192.168.27.129:8001@18001 slave 69d305ad0b4ba25b7d1d84c7ea7cb86218a28a8c 0 1668694032570 5 connected
57c57905eea202b9fe1b47515cc4ea2851f608e6 192.168.27.130:8002@18002 slave 4301c9c511c84d99b4aa07fd53207c48da8e449e 0 1668694032368 2 connected
4301c9c511c84d99b4aa07fd53207c48da8e449e 192.168.27.129:7001@17001 master - 0 1668694033587 2 connected 5461-10922
781c3d1823c2efe8930eaabab7ff3c1e49b42f93 192.168.27.128:8000@18000 slave 390a2f7cb23d038982a42569f98c03cb13ff5a87 0 1668694035627 3 connected
390a2f7cb23d038982a42569f98c03cb13ff5a87 192.168.27.130:7002@17002 master - 0 1668694031552 3 connected 10923-16383

移除新主222:7003前先迁移数据：
## redis-cli -a redispwd --cluster reshard 192.168.107.222:7003  #任意一个节点连接集群即可,重新分配槽位,:7003的槽位移动到222:7000
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Performing Cluster Check (using node 192.168.107.222:7003)
M: c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003
   slots:[0-1999] (2000 slots) master
M: ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001
   slots:[5461-10922] (5462 slots) master
   1 additional replica(s)
S: e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000
   slots: (0 slots) slave
   replicates 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095
M: 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002
   slots:[10923-16383] (5461 slots) master
   1 additional replica(s)
S: ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001
   slots: (0 slots) slave
   replicates c4acfb2490f7557a5e1857118360bddfaa523c9f
S: 0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002
   slots: (0 slots) slave
   replicates ff50bb210c08f3bd453201150be381bcb3b4f05f
M: c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000
   slots:[2000-5460] (3461 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
How many slots do you want to move (from 1 to 16384)? 2000            #移动2000个槽位
What is the receiving node ID? c4acfb2490f7557a5e1857118360bddfaa523c9f     #接收的id，让222:7000接收
Source node #1: c8f152ea7f6f436a96af0a3364e721ff108fb20b            #把哪个节点的槽位移走，222:7003
Source node #2: done                    #选择完毕了，输入done，让其操作
...
Do you want to proceed with the proposed reshard plan (yes/no)? yes
...
## redis-cli -a redispwd -p 7003 cluster nodes      #查看集群节点信息,222:7003的槽位已经转移给222:7000
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693051157631 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693051156000 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693051158637 3 connected 10923-16383
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693051155000 10 connected
#c8f152ea7f6f436a96af0a3364e721ff108fb20b 192.168.107.222:7003@17003 myself,master - 0 1693051157000 9 connected
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693051156000 2 connected
#c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 master - 0 1693051156625 10 connected 0-5460



指定主222:7000,移除新主222:7003的id:  
## redis-cli -a redispwd --cluster del-node 192.168.107.222:7000 c8f152ea7f6f436a96af0a3364e721ff108fb20b  
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
>>> Removing node c8f152ea7f6f436a96af0a3364e721ff108fb20b from cluster 192.168.107.222:7000
>>> Sending CLUSTER FORGET messages to the cluster...
>>> Sending CLUSTER RESET SOFT to the deleted node.


上面将222上主从节点移除主从之前都可以使用集群操作命令，但主从都移除集群后，再执行查看集群等操作就需要在其他集群节点了
在222:7000节点查看现在集群状态：发现新主新从节点都已经移除出去：
## redis-cli -a redispwd -p 7000 cluster nodes
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
c4acfb2490f7557a5e1857118360bddfaa523c9f 192.168.107.222:7000@17000 myself,master - 0 1693051315000 10 connected 0-5460
ffb3bd0c4d3fade126022f2f90691a9cbde30f16 192.168.107.223:8001@18001 slave c4acfb2490f7557a5e1857118360bddfaa523c9f 0 1693051315528 10 connected
0a42290ad59f7ac2565bb1f3c6fe2ecbe45647ca 192.168.107.224:8002@18002 slave ff50bb210c08f3bd453201150be381bcb3b4f05f 0 1693051314518 2 connected
ff50bb210c08f3bd453201150be381bcb3b4f05f 192.168.107.223:7001@17001 master - 0 1693051314000 2 connected 5461-10922
e95d7e90e12b045e3f5bab0d27519770f46d42ae 192.168.107.222:8000@18000 slave 2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 0 1693051316535 3 connected
2611c9f0da19d1ee2b4d4f8c4b5f7fb617fdb095 192.168.107.224:7002@17002 master - 0 1693051315000 3 connected 10923-16383
```

