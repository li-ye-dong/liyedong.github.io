<font style="color:rgb(51, 51, 51);">您可以通过提供另一个名称(ALIAS)来临时重命名表或列。 表别名的使用意味着在特定的SQLite语句中重命名表。 重命名是一个临时更改，数据库中的实际表名不会更改。</font>

<font style="color:rgb(51, 51, 51);">列别名用于重命名表的列，以用于特定的SQLite查询。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是</font>**<font style="color:rgb(51, 51, 51);">table</font>**<font style="color:rgb(51, 51, 51);">别名的基本语法。</font>

```sql
SELECT column1, column2....
FROM table_name AS alias_name
WHERE [condition];
```

<font style="color:rgb(51, 51, 51);">以下是</font>**<font style="color:rgb(51, 51, 51);">column</font>**<font style="color:rgb(51, 51, 51);">别名的基本语法。</font>

```sql
SELECT column_name AS alias_name
FROM table_name
WHERE [condition];
```

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">考虑以下两个表，(a)COMPANY表如下-</font>

```sql
sqlite> select * from COMPANY;
ID          NAME                  AGE         ADDRESS     SALARY
----------  --------------------  ----------  ----------  ----------
1           Paul                  32          California  20000.0
2           Allen                 25          Texas       15000.0
3           Teddy                 23          Norway      20000.0
4           Mark                  25          Rich-Mond   65000.0
5           David                 27          Texas       85000.0
6           Kim                   22          South-Hall  45000.0
7           James                 24          Houston     10000.0
```

<font style="color:rgb(51, 51, 51);">(b)另一个表格是部门--</font>

```sql
ID          DEPT                  EMP_ID
----------  --------------------  ----------
1           IT Billing            1
2           Engineering           2
3           Finance               7
4           Engineering           3
5           Finance               4
6           Engineering           5
7           Finance               6
```

<font style="color:rgb(51, 51, 51);">现在，下面是</font>**<font style="color:rgb(51, 51, 51);">TABLE ALIAS</font>**<font style="color:rgb(51, 51, 51);">我们分别使用C和D作为COMPANY和DEPARTMENT表的别名的用法-</font>

```sql
sqlite> SELECT C.ID, C.NAME, C.AGE, D.DEPT
        FROM COMPANY AS C, DEPARTMENT AS D
        WHERE  C.ID = D.EMP_ID;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite语句将产生以下结果-</font>

```sql
ID          NAME        AGE         DEPT
----------  ----------  ----------  ----------
1           Paul        32          IT Billing
2           Allen       25          Engineering
3           Teddy       23          Engineering
4           Mark        25          Finance
5           David       27          Engineering
6           Kim         22          Finance
7           James       24          Finance
```

<font style="color:rgb(51, 51, 51);">考虑一个使用示例，</font>**<font style="color:rgb(51, 51, 51);">COLUMN ALIAS</font>**<font style="color:rgb(51, 51, 51);">其中COMPANY_ID是ID列的别名，而COMPANY_NAME是name列的别名。  
</font>

```sql
sqlite> SELECT C.ID AS COMPANY_ID, C.NAME AS COMPANY_NAME, C.AGE, D.DEPT
        FROM COMPANY AS C, DEPARTMENT AS D
        WHERE  C.ID = D.EMP_ID;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite语句将产生以下结果-</font>

```sql
COMPANY_ID  COMPANY_NAME  AGE         DEPT
----------  ------------  ----------  ----------
1           Paul          32          IT Billing
2           Allen         25          Engineering
3           Teddy         23          Engineering
4           Mark          25          Finance
5           David         27          Engineering
6           Kim           22          Finance
7           James         24          Finance
```

