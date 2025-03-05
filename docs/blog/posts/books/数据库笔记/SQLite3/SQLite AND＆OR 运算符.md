<font style="color:rgb(51, 51, 51);">SQLite </font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">AND</font>**`<font style="color:rgb(51, 51, 51);">＆</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">OR</font>**`<font style="color:rgb(51, 51, 51);">运算符用于编译多个条件，以缩小SQLite语句中选定数据的范围。这两个运算符称为合取运算符。</font>

<font style="color:rgb(51, 51, 51);">这些运算符提供了一种在同一SQLite语句中与不同运算符进行多次比较的方法。</font>

## <font style="color:rgb(51, 51, 51);">AND运算符</font>
`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">AND</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">运算符允许多个条件在SQLite的声明中存在的WHERE子句。使用AND运算符时，当所有条件都为真时，将假定完全条件为真。例如，仅当condition1和condition2均为true时，[condition1] AND [condition2]才为true。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是带有WHERE子句的AND运算符的基本语法。</font>

SELECT column1, column2, columnN FROM table_nameWHERE [condition1] AND [condition2]...AND [conditionN];

<font style="color:rgb(51, 51, 51);">您可以使用AND运算符组合N个条件。 对于要由SQLite语句执行的操作（无论是事务还是查询），用AND分隔的所有条件必须为TRUE。</font>

### <font style="color:rgb(51, 51, 51);">例</font>
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

<font style="color:rgb(51, 51, 51);">以下SELECT语句列出AGE大于或等于25</font><font style="color:rgb(51, 51, 51);"> </font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">AND</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">薪水(SALARY)大于或等于65000.00的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE >= 25 AND SALARY >= 65000;

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

## <font style="color:rgb(51, 51, 51);">OR 运算符</font>
<font style="color:rgb(51, 51, 51);">OR运算符还用于在SQLite语句的WHERE子句中组合多个条件。使用OR运算符时，如果至少有一个条件为true，则将假定完全条件为true。例如，如果condition1或condition2为true，则[condition1]或[condition2]将为true。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是带有WHERE子句的OR运算符的基本语法。</font>

SELECT column1, column2, columnN FROM table_nameWHERE [condition1] OR [condition2]...OR [conditionN]

<font style="color:rgb(51, 51, 51);">可以使用OR运算符组合N个条件。对于SQLite语句要执行的操作，无论是事务还是查询，只有由or分隔的条件中的任何一个必须为TRUE。</font>

### <font style="color:rgb(51, 51, 51);">例</font>
<font style="color:rgb(51, 51, 51);">请看带有以下记录的COMPANY表。</font>

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

<font style="color:rgb(51, 51, 51);">以下SELECT语句列出AGE大于或等于25</font><font style="color:rgb(51, 51, 51);"> </font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">OR</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">薪水大于或等于65000.00的所有记录。</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE >= 25 OR SALARY >= 65000;

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

