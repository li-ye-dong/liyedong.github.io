<font style="color:rgb(51, 51, 51);">SQLite </font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">UPDATE</font>**`<font style="color:rgb(51, 51, 51);">查询用于修改表中的现有记录。您可以将WHERE子句与UPDATE查询一起使用来更新选定的行，否则所有行都将被更新。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是带有WHERE子句的UPDATE查询的基本语法。</font>

```python
UPDATE table_nameSET column1 = value1, column2 = value2...., columnN = valueNWHERE [condition];
```

<font style="color:rgb(51, 51, 51);">可以使用 AND 或 OR 运算符组合 n 个条件。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">请看带有以下记录的COMPANY表-</font>

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

<font style="color:rgb(51, 51, 51);">下面是一个示例，它将为ID为6的客户更新ADDRESS。</font>

sqlite> UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;

<font style="color:rgb(51, 51, 51);">现在，COMPANY表将具有以下记录。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          Texas       45000.0
7           James       24          Houston     10000.0
```

<font style="color:rgb(51, 51, 51);">如果要修改COMPANY表中的所有ADDRESS和SALARY列值，则无需使用WHERE子句，UPDATE查询将如下所示-</font>

sqlite> UPDATE COMPANY SET ADDRESS = 'Texas', SALARY = 20000.00;

<font style="color:rgb(51, 51, 51);">现在，COMPANY表将具有以下记录-</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          Texas       20000.0
2           Allen       25          Texas       20000.0
3           Teddy       23          Texas       20000.0
4           Mark        25          Texas       20000.0
5           David       27          Texas       20000.0
6           Kim         22          Texas       20000.0
7           James       24          Texas       20000.0
```

