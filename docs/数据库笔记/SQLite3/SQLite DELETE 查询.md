<font style="color:rgb(51, 51, 51);">SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> DELETE</font>**`<font style="color:rgb(51, 51, 51);">查询用于从表中删除现有记录。您可以将WHERE子句与DELETE查询一起使用以删除所选的行，否则所有记录将被删除。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是带有WHERE子句的DELETE查询的基本语法。</font>

DELETE FROM table_nameWHERE [condition];

<font style="color:rgb(51, 51, 51);">可以使用 AND 或 OR 运算符组合 n 个条件。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
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

<font style="color:rgb(51, 51, 51);">下面是一个示例，它将删除ID为7的客户。</font>

sqlite> DELETE FROM COMPANY WHERE ID = 7;

<font style="color:rgb(51, 51, 51);">现在COMPANY表将具有以下记录。</font>

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

<font style="color:rgb(51, 51, 51);">如果要删除COMPANY表中的所有记录，则无需将WHERE子句与DELETE查询一起使用，如下所示-</font>

sqlite> DELETE FROM COMPANY;

<font style="color:rgb(51, 51, 51);">现在，COMPANY表没有任何记录，因为所有记录已被DELETE语句删除。</font>

