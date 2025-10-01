#### <font style="color:rgb(51, 51, 51);">查询数据</font>
##### <font style="color:rgb(51, 51, 51);">单表查询</font>
+ <font style="color:rgb(51, 51, 51);">准备数据</font>

```python
#创建员工表，字段为：
#id自增，员工名不能为空，性别只可以为male或者female且不能为空，默认值为male
#age不能为空，默认值28，入职日期只显示年月日，职位名称，工资保留两位小数，办公室门牌号，部门id
create table emp (
    id int PRIMARY KEY auto_increment,
name char(20) not null,
gender enum('male','female') default 'male',
age int not null default 28,
hire_date date,
job_title varchar(30),
salary float(10,2),
office_num int,
dep_id int
)

数据
insert into emp (name,gender,age,hire_date,job_title,salary,office_num,dep_id)values
('weiwei','male',78,'20150302','teacher',1000000.31,401,1),
('lala','male',81,'20130305','teacher',8300,401,1),
('zhangsan','male',73,'20140701','teacher',3500,401,1),
('liulaogen','male',28,'20121101','teacher',2100,401,1),
('aal','female',18,'20110211','teacher',9000,401,1),
('zhugelang','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),
('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35,402,2),
('丁丁','female',18,'20110312','sale',1000.37,402,2),
('星星','female',18,'20160513','sale',3000.29,402,2),
('格格','female',28,'20170127','sale',4000.33,402,2),
('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000,403,3),
('程咬银','female',18,'20130311','operation',19000,403,3),
('程咬铜','male',18,'20150411','operation',18000,403,3),
('程咬铁','female',18,'20140512','operation',17000,403,3)
```

+ <font style="color:rgb(51, 51, 51);">条件查询where语句</font>
    - <font style="color:rgb(51, 51, 51);">单条件查询</font>

```python
#查询销售员工的姓名和薪资
select name,salary from emp where job_title = 'sale'
```

    - <font style="color:rgb(51, 51, 51);">多条件查询1：结合and</font>

```python
#查询薪资大于1w的老师对应的名字和薪资
select name,salary from emp where job_title = 'teacher' and salary > 10000
```

    - <font style="color:rgb(51, 51, 51);">多条件查询2：结合or</font>

```python
#查询薪资为3，3.5，4，9k的员工名字和具体薪资
select name,salary from emp where salary = 3000 or salary = 3500 or salary = 4000 or salary = 9000
```

    - <font style="color:rgb(51, 51, 51);">多条件查询3：结合between...and</font>

```python
#查询薪资范围在1000-5000之间的员工名字和具体薪资
select name,salary from emp where salary between 1000 and 5000
```

    - <font style="color:rgb(51, 51, 51);">多条件查询4:结合in</font>

```python
#查询薪资为3，3.5，4，9k的员工名字和具体薪资
select name,salary from emp where salary in (3000,3500,4000,9000)
```

    - <font style="color:rgb(51, 51, 51);">多条件查询5:结合not in</font>
    - <font style="color:rgb(51, 51, 51);">select name,salary from emp where salary not in (3000,3500,4000,9000)</font>
    - <font style="color:rgb(51, 51, 51);">模糊查询like</font>
        * <font style="color:rgb(51, 51, 51);">通配符%:表示多个字符</font>
            + <font style="color:rgb(51, 51, 51);">select * from emp where name like 'a%'</font>
        * <font style="color:rgb(51, 51, 51);">通配符_:表示一个字符</font>
            + <font style="color:rgb(51, 51, 51);">select * from emp where name like 'zhang___'</font>
+ <font style="color:rgb(51, 51, 51);">排序：order by</font>
    - <font style="color:rgb(51, 51, 51);">升序： order by 字段 asc(默认升序,可以不写)</font>
    - <font style="color:rgb(51, 51, 51);">降序： order by 字段 desc</font>
    - <font style="color:rgb(51, 51, 51);">单列排序：</font>
    - <font style="color:rgb(51, 51, 51);">select * from emp order by salary</font>
+ <font style="color:rgb(51, 51, 51);">limit</font>
    - <font style="color:rgb(51, 51, 51);">显示前三条数据</font>
    - <font style="color:rgb(51, 51, 51);">select * from emp limit 3</font>
    - <font style="color:rgb(51, 51, 51);">从0开始,先查出第一条,然后包含这条再往后查5条</font>
    - <font style="color:rgb(51, 51, 51);">select * from emp limit 0,5</font>
    - <font style="color:rgb(51, 51, 51);">从第3开始,即先查出第4条,然后包含这条再往后查7条</font>
    - <font style="color:rgb(51, 51, 51);">select * from emp limit 3,7</font>

### <font style="color:rgb(51, 51, 51);">分组查询：</font>
+ <font style="color:rgb(51, 51, 51);">简单的分组查询</font>
    - <font style="color:rgb(51, 51, 51);">注意：使用group by的查询字段必须是分组字段，否则会出错，想要获取其他字段信息,可以借助于聚合函数</font>
+ <font style="color:rgb(51, 51, 51);">select job_title from emp group by job_title</font>
+ <font style="color:rgb(51, 51, 51);">分组聚合</font>

```python
#查看每一个岗位的人数
#count(1)每组的行数
select job_title, count(1)from emp group by job_title

#计算男女员工的平均年龄
select gender,avg(age) from emp group by gender

#计算不同岗位员工的平均薪资
select job_title,avg(salary) from emp group by job_title

#查看男女员工的最大,最小年级和整体年龄
select gender,max(age),min(age),sum(age) from emp group by gender
```

+ <font style="color:rgb(51, 51, 51);">having子句</font>
    - <font style="color:rgb(51, 51, 51);">where 与 having的区别：</font><font style="color:rgb(51, 51, 51);">	</font>
        * <font style="color:rgb(51, 51, 51);">where 是针对分组之前的字段内容进行过滤,而having是针对分组后的</font>
    - <font style="color:rgb(51, 51, 51);">注意：having后面的条件字段只可以是分组后结果中存在的字段名，否则会报错！</font>

```python
#查看销售岗位的平均薪资
select job_title,avg(salary) from emp GROUP BY job_title having job_title = 'sale'
```

### <font style="color:rgb(51, 51, 51);">条件判断</font>
#### <font style="color:rgb(51, 51, 51);">case when语句</font>
<font style="color:rgb(51, 51, 51);">语法格式</font>

<font style="color:rgb(51, 51, 51);">case when [expr] then [result1]...else [default] end</font>

<font style="color:rgb(51, 51, 51);">如果expr条件成立则返回result1，否则返回default，并且最后以end结束条件判断。</font>

```python
#建表  
CREATE TABLE t_demo (
    id int(32) NOT NULL,
name varchar(255) DEFAULT NULL,
age int(2) DEFAULT NULL,
num int(3) DEFAULT NULL,
PRIMARY KEY (`id`)
);

#插入数据
INSERT INTO t_demo VALUES ('1', '张三', '21', '69');
INSERT INTO t_demo VALUES ('2', '李四', '12', '98');
INSERT INTO t_demo VALUES ('3', '王五', '20', '54');
INSERT INTO t_demo VALUES ('4', '赵甜', '17', '80');

#给t_demo添加一列level，表示学生的得分等级
select * ,
case 
when t.num >= 85 then '优秀'
when t.num < 85 and t.num >= 60 then '一般'
else '不及格'
end as level
from t_demo as t;
```

#### <font style="color:rgb(51, 51, 51);">if判断</font>
<font style="color:rgb(51, 51, 51);">用法1：if(expr1,ret1,ret2)</font>

<font style="color:rgb(51, 51, 51);">如果expr1条件为真，则返回ret1否则返回ret2</font>

```python
#添加一列表示学生是否成年
select *,
if(t.age >= 18,'成人','未成年') as 是否成年
from t_demo as t;
```

### <font style="color:rgb(51, 51, 51);">python连接数据库（重点）</font>
+ <font style="color:rgb(51, 51, 51);">环境安装：pip install pymysql</font>
+ <font style="color:rgb(51, 51, 51);">操作流程：</font>

```python
#数据的增删改
import pymysql
#1.创建一个链接对象:决定了要去访问链接哪一个数据库服务器下的哪一个数据仓库
conn = pymysql.Connect(
    host='127.0.0.1',#数据库服务器的ip地址
    port=3306,#mysql的端口
    user='root',#mysql用户名
    password='boboadmin',#mysql的密码
    db='new_spider',#数据库的名字
    charset='utf8'#中文编码
)
#2.创建一个游标对象：可以让python执行sql语句
cursor = conn.cursor()
#3.使用游标对象执行sql语句(增删改)
# sql = 'delete from new_dep where id = 5'
# sql = 'insert into new_dep values (66,"haha","xxx")'
sql = 'update new_dep set dep_name="销售" where id = 66'
cursor.execute(sql)
#4.提交事务:让游标执行的sql语句完全的映射到数据库中
conn.commit()
#5.关闭资源
cursor.close()
conn.close()
```

```python
#数据查询操作
import pymysql
#1.创建一个链接对象:决定了要去访问链接哪一个数据库服务器下的哪一个数据仓库
conn = pymysql.Connect(
    host='127.0.0.1',#数据库服务器的ip地址
    port=3306,#mysql的端口
    user='root',#mysql用户名
    password='boboadmin',#mysql的密码
    db='new_spider',#数据库的名字
    charset='utf8'#中文编码
)
#2.创建一个游标对象：可以让python执行sql语句
cursor = conn.cursor()
#3.使用游标对象执行sql语句(查询)
# sql = 'select * from new_dep where id = 66'
sql = 'select * from new_dep'
cursor.execute(sql)
#4.获取查询结果
ret = cursor.fetchall()
print(ret)
#5.关闭资源
cursor.close()
conn.close()
```

+ <font style="color:rgb(51, 51, 51);">爬取豆瓣电影数据，存储到数据库中</font>

```python
import requests
import pymysql
#创建一个mysql的链接对象
conn = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='boboadmin',
    db='spider',
    charset='utf8'
)
#创建游标对象
cursor = conn.cursor()

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "20",
    "limit": "20"
}
movie_data = requests.get(url=url,headers=headers,params=params).json()
#电影名字，评分，导演，上映时间
for dic in movie_data:
    title = dic['title']
    score = dic['score']
    actors = dic['actors']
    actors = ','.join(actors)
    year = dic['release_date']

    sql = 'insert into movie_tb(title,score,actors,year) values ("%s","%s","%s","%s")'%(title,score,actors,year)
    cursor.execute(sql)
    conn.commit()
    print(title,'：电影数据爬取存储成功！')

cursor.close()
conn.close()
```

### <font style="color:rgb(51, 51, 51);">pandas数据表格（重点）</font>
+ <font style="color:rgb(51, 51, 51);">环境安装：</font>

```python
pip install openpyxl
pip install pandas
```

+ <font style="color:rgb(51, 51, 51);">基础操作</font>

```python
import pandas as pd
#pandas会帮我们创建一个数据表格，可以对数据表格进行相关操作，最后将该数据表格同步到excel

#1.手动的创建一个pandas的数据表格
table = pd.DataFrame(columns=['name','salary','job_title'])
#2.给数据表格插入数据
table.loc[0] = ['Jay',40000,'singer']
table.loc[1] = ['Tom',10000,'sale']
print(table)
#3.将数据表格转换成excel
table.to_excel('test.xlsx',sheet_name='haha')
```

+ <font style="color:rgb(51, 51, 51);">爬取数据存储到excel</font>

```python
import requests
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "20",
    "limit": "20"
}
movie_data = requests.get(url=url, headers=headers, params=params).json()
# 电影名字，评分，导演，上映时间
table = pd.DataFrame(columns=['title','score','actors','year'])
index = 0 #初始的行索引
for dic in movie_data:
    title = dic['title']
    score = dic['score']
    actors = dic['actors']
    actors = ','.join(actors)
    year = dic['release_date']

    table.loc[index] = [title,score,actors,year]

    index += 1
    print(title,':爬取保存成功！')

table.to_excel('movie_data.xlsx',sheet_name='movie')
```

### <font style="color:rgb(51, 51, 51);">将mysql的数据转存到Excel中</font>
```python
#python-mysql   python-excel    mysql-excel

#将数据库中的数据读取到Excel文件中
import pandas as pd
import pymysql

#创建一个mysql的链接对象
conn = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='boboadmin',
    db='spider',
    charset='utf8'
)
table = pd.read_sql('select * from emp',conn)
table.to_excel('emp.xlsx')
```

  
 

