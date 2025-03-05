<font style="color:rgb(51, 51, 51);">SQLite </font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">LIMIT</font>**`<font style="color:rgb(51, 51, 51);">子句用于限制SELECT语句返回的数据量。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是带有LIMIT子句的SELECT语句的基本语法。</font>

```sql
SELECT column1, column2, columnN FROM table_nameLIMIT [no of rows]
```

<font style="color:rgb(51, 51, 51);">以下是LIMIT子句与OFFSET子句一起使用时的语法。</font>

```sql
SELECT column1, column2, columnN FROM table_name LIMIT [no of rows] OFFSET [row num]
```

<font style="color:rgb(51, 51, 51);">SQLite引擎将返回从下一行开始到给定OFFSET的行，如上一个示例所示。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">考虑带有以下记录的COMPANY表-</font>

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

<font style="color:rgb(51, 51, 51);">下面是一个示例，该示例根据要从表中获取的行数来限制表中的行。</font>

```sql
sqlite> SELECT * FROM COMPANY LIMIT 6;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
```

<font style="color:rgb(51, 51, 51);">然而，在某些情况下，您可能需要从特定的偏移量获取一组记录。下面是一个实例，它从第三个位置开始获取3条记录。</font>

```sql
sqlite> SELECT * FROM COMPANY LIMIT 3 OFFSET 2;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

