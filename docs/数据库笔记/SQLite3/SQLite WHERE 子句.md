<font style="color:rgb(51, 51, 51);">SQLite</font>**<font style="color:rgb(51, 51, 51);"> WHERE</font>**<font style="color:rgb(51, 51, 51);">子句用于指定从一个或多个表中获取数据时的条件。</font>

<font style="color:rgb(51, 51, 51);">如果满足给定条件，即为true，那么它将从表中返回特定值。您将必须使用WHERE子句来过滤记录并仅提取必要的记录。</font>

<font style="color:rgb(51, 51, 51);">WHERE子句不仅在SELECT语句中使用，而且在UPDATE，DELETE语句等中使用，这将在后续章节中介绍。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是带有WHERE子句的SQLite SELECT语句的基本语法。</font>

```python
SELECT column1, column2, columnN FROM table_nameWHERE [condition]
```

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">您可以使用</font>[<font style="color:rgb(51, 51, 51);">比较运算符或逻辑运算符（</font>](https://www.cainiaoplus.com/sqlite/sqlite-operators.html)<font style="color:rgb(51, 51, 51);">例如>，<，=，LIKE，NOT等）指定条件。请看带有以下记录的COMPANY表-</font>

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

<font style="color:rgb(51, 51, 51);">以下是显示SQLite逻辑运算符用法的简单示例。以下SELECT语句列出AGE(年龄)大于或等于25 和 SALARY (薪水)大于或等于65000.00的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE >= 25 AND SALARY >= 65000;

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

<font style="color:rgb(51, 51, 51);">以下SELECT语句列出AGE(年龄)大于或等于25</font>**<font style="color:rgb(51, 51, 51);"> </font>****<font style="color:rgb(51, 51, 51);">或</font>****<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">SALARY (薪水)大于或等于65000.00的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE >= 25 OR SALARY >= 65000;

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

<font style="color:rgb(51, 51, 51);">紧接着SELECT语句列出了AGE(年龄)不为NULL的所有记录，这意味着将显示所有记录，因为没有记录的AGE的值等于NULL。</font>

```sql
sqlite>  SELECT * FROM COMPANY WHERE AGE IS NOT NULL;

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

<font style="color:rgb(51, 51, 51);">以下SELECT语句列出了NAME以'Ki'开头的所有记录，而与'Ki'之后的任意记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE NAME LIKE 'Ki%';

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
6           Kim         22          South-Hall  45000.0
```

<font style="color:rgb(51, 51, 51);">以下SELECT语句列出了NAME以'Ki'开头的所有记录，与'Ki'之后的记录无关。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE NAME GLOB 'Ki*';

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
6           Kim         22          South-Hall  45000.0
```

<font style="color:rgb(51, 51, 51);">在SELECT语句之后，列出了AGE(年龄)值为25或27的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE IN ( 25, 27 );

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

<font style="color:rgb(51, 51, 51);">以下SELECT语句列出了AGE(年龄)值既不是25也不是27的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE NOT IN ( 25, 27 );

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
3           Teddy       23          Norway      20000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

<font style="color:rgb(51, 51, 51);">在SELECT语句之后，列出了AGE(年龄)值在25和27之间的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE BETWEEN 25 AND 27;

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

<font style="color:rgb(51, 51, 51);">以下SELECT语句使用SQL子查询，其中子查询查找AGE(年龄)字段的SALARY> 65000的所有记录，随后WHERE子句与EXISTS运算符一起使用，以列出外部查询存在AGE的所有记录在子查询返回的结果中-</font>

```sql
sqlite> SELECT AGE FROM COMPANY 
   WHERE EXISTS (SELECT AGE FROM COMPANY WHERE SALARY > 65000);

AGE
----------
32
25
23
25
27
22
24
```

<font style="color:rgb(51, 51, 51);">以下SELECT语句使用SQL子查询，其中子查询查找AGE字段的SALARY> 65000的所有记录，以及与 > 运算符一起使用的where子句列出外部查询的AGE大于子查询返回的结果中的AGE的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY 
   WHERE AGE > (SELECT AGE FROM COMPANY WHERE SALARY > 65000);

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
```

