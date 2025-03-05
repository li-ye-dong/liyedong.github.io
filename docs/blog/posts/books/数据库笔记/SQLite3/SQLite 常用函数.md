<font style="color:rgb(51, 51, 51);">SQLite具有许多内置函数，可以对字符串或数字数据进行处理。以下是一些有用的SQLite内置函数的列表，所有这些函数都不区分大小写，这意味着您可以以小写形式，大写形式或混合形式使用这些函数。有关更多详细信息，您可以查看SQLite的官方文档。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">函数说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">SQLite COUNT 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite COUNT聚合函数用于计算数据库表中的行数。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">SQLite MAX</font>****<font style="color:rgb(51, 51, 51);"> </font>****<font style="color:rgb(51, 51, 51);">函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite MAX聚合函数使我们能够为特定列选择最高（最大值）值。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">SQLite MIN 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite MIN聚合函数允许我们为特定列选择最低（最小值）值。</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | **<font style="color:rgb(51, 51, 51);">SQLite AVG 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite AVG聚合函数选择某些表列的平均值。</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | **<font style="color:rgb(51, 51, 51);">SQLite SUM 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite SUM聚合函数允许为数字列选择总计。</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | **<font style="color:rgb(51, 51, 51);">SQLite RANDOM 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite RANDOM函数返回-9223372036854775808和+9223372036854775807之间的伪随机整数。</font> |
| <font style="color:rgb(51, 51, 51);">7</font> | **<font style="color:rgb(51, 51, 51);">SQLite ABS 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite ABS函数返回数字参数的绝对值。</font> |
| <font style="color:rgb(51, 51, 51);">8</font> | **<font style="color:rgb(51, 51, 51);">SQLite UPPER 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite UPPER函数将字符串转换为大写字母。</font> |
| <font style="color:rgb(51, 51, 51);">9</font> | **<font style="color:rgb(51, 51, 51);">SQLite LOWER 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite LOWER函数将字符串转换为小写字母。</font> |
| <font style="color:rgb(51, 51, 51);">10</font> | **<font style="color:rgb(51, 51, 51);">SQLite LENGTH 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite LENGTH函数返回字符串的长度。</font> |
| <font style="color:rgb(51, 51, 51);">11</font> | **<font style="color:rgb(51, 51, 51);">SQLite sqlite_version 函数</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite sqlite_version函数返回SQLite库的版本。</font> |


<font style="color:rgb(51, 51, 51);">在开始提供上述功能的示例之前，请考虑带有以下记录的COMPANY表。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

## <font style="color:rgb(51, 51, 51);">SQLite COUNT函数</font>
<font style="color:rgb(51, 51, 51);">SQLite COUNT聚合函数用于计算数据库表中的行数。以下是一个实例-</font>

```sql
sqlite> SELECT count(*) FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
count(*)
----------
7
```

## <font style="color:rgb(51, 51, 51);">SQLite MAX函数</font>
<font style="color:rgb(51, 51, 51);">SQLite MAX聚合函数使我们能够为特定列选择最高（最大值）值。以下是一个实例-</font>

```sql
sqlite> SELECT max(salary) FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
max(salary)
-----------
85000.0
```

## <font style="color:rgb(51, 51, 51);">SQLite MIN函数</font>
<font style="color:rgb(51, 51, 51);">SQLite MIN聚合函数允许我们为特定列选择最低（最小值）值。以下是一个实例-</font>

```sql
sqlite> SELECT min(salary) FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
min(salary)
-----------
10000.0
```

## <font style="color:rgb(51, 51, 51);">SQLite AVG函数</font>
<font style="color:rgb(51, 51, 51);">SQLite AVG聚合函数选择某个表列的平均值。以下是一个实例-</font>

sqlite> SELECT avg(salary) FROM COMPANY;

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
avg(salary)
----------------
37142.8571428572
```

## <font style="color:rgb(51, 51, 51);">SQLite SUM函数</font>
<font style="color:rgb(51, 51, 51);">SQLite SUM聚合函数允许为数字列选择总计。以下是一个实例-</font>

```sql
sqlite> SELECT sum(salary) FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
sum(salary)
-----------
260000.0
```

## <font style="color:rgb(51, 51, 51);">SQLite RANDOM函数</font>
<font style="color:rgb(51, 51, 51);">SQLite RANDOM函数返回-9223372036854775808和+9223372036854775807之间的伪随机整数。以下是一个实例-</font>

```sql
sqlite> SELECT random() AS Random;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
Random
-------------------
5876796417670984050
```

## <font style="color:rgb(51, 51, 51);">SQLite ABS 函数  
</font>
<font style="color:rgb(51, 51, 51);">SQLite ABS函数返回数字参数的绝对值。以下是一个实例-</font>

```sql
sqlite> SELECT abs(5), abs(-15), abs(NULL), abs(0), abs("ABC");
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
abs(5)      abs(-15)    abs(NULL)   abs(0)      abs("ABC")
----------  ----------  ----------  ----------  ----------
5           15                      0           0.0
```

## <font style="color:rgb(51, 51, 51);">SQLite UPPER函数</font>
<font style="color:rgb(51, 51, 51);">SQLite UPPER函数将字符串转换为大写字母。以下是一个实例-</font>

```sql
sqlite> SELECT upper(name) FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
upper(name)
-----------
PAULALLENTEDDYMARKDAVIDKIMJAMES
```

## <font style="color:rgb(51, 51, 51);">SQLite LOWER函数</font>
<font style="color:rgb(51, 51, 51);">SQLite LOWER函数将字符串转换为小写字母。以下是一个实例-</font>

```sql
sqlite> SELECT lower(name) FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
lower(name)
-----------
paulallenteddymarkdavidkimjames
```

## <font style="color:rgb(51, 51, 51);">SQLite LENGTH函数</font>
<font style="color:rgb(51, 51, 51);">SQLite LENGTH函数返回字符串的长度。以下是一个实例-</font>

```sql
sqlite> SELECT name, length(name) FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
NAME        length(name)
----------  ------------
Paul        4
Allen       5
Teddy       5
Mark        4
David       5
Kim         3
James       5
```

## <font style="color:rgb(51, 51, 51);">SQLite sqlite_version 函数</font>
<font style="color:rgb(51, 51, 51);">SQLite sqlite_version函数返回SQLite库的版本。以下是一个实例-</font>

```sql
sqlite> SELECT sqlite_version() AS 'SQLite Version';
```

<font style="color:rgb(51, 51, 51);">上面的SQLite SQL语句将产生以下内容。</font>

```sql
SQLite Version--------------3.6.20
```

