<font style="color:rgb(51, 51, 51);">SQLite NULL是用来表示缺失值的术语。表中的空值是字段中看起来为空的值。</font>

<font style="color:rgb(51, 51, 51);">具有 NULL 值的字段是没有值的字段。理解 NULL 值与零值或包含空格的字段是不同的，这一点非常重要。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是</font>**<font style="color:rgb(51, 51, 51);">NULL</font>**<font style="color:rgb(51, 51, 51);">创建表时使用的基本语法。</font>

```sql
SQLite> CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL);
```

<font style="color:rgb(51, 51, 51);">在这里，</font>**<font style="color:rgb(51, 51, 51);">NOT NULL</font>**<font style="color:rgb(51, 51, 51);">表示该列应始终接受给定数据类型的显式值。有两列我们未使用NOT NULL，这意味着这些列可能为NULL。</font>

<font style="color:rgb(51, 51, 51);">具有NULL值的字段是在记录创建过程中留为空白的字段。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">NULL值在选择数据时可能会引起问题，因为将未知值与任何其他值进行比较时，结果始终是未知的，并且不包括在最终结果中。考虑具有以下记录的下表COMPANY-</font>

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

<font style="color:rgb(51, 51, 51);">让我们使用UPDATE语句将一些可为空的值设置为NULL，如下所示：</font>

sqlite> UPDATE COMPANY SET ADDRESS = NULL, SALARY = NULL where ID IN(6,7);

<font style="color:rgb(51, 51, 51);">现在，COMPANY表将具有以下记录。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22
7           James       24
```

<font style="color:rgb(51, 51, 51);">接下来，让我们看一下</font>**<font style="color:rgb(51, 51, 51);">IS NOT NULL</font>**<font style="color:rgb(51, 51, 51);">运算符的用法，以列出SALARY不为NULL的所有记录。</font>

```sql
sqlite> SELECT  ID, NAME, AGE, ADDRESS, SALARY
        FROM COMPANY
        WHERE SALARY IS NOT NULL;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite语句将产生以下结果-</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

<font style="color:rgb(51, 51, 51);">以下是</font>**<font style="color:rgb(51, 51, 51);">IS NULL</font>**<font style="color:rgb(51, 51, 51);">运算符的用法，该运算符将列出SALARY为NULL的所有记录。</font>

```sql
sqlite> SELECT  ID, NAME, AGE, ADDRESS, SALARY
        FROM COMPANY
        WHERE SALARY IS NULL;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite语句将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
6           Kim         22
7           James       24
```

