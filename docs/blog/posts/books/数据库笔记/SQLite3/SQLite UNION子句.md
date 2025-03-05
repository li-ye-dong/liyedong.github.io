<font style="color:rgb(51, 51, 51);">SQLite </font>**<font style="color:rgb(51, 51, 51);">UNION</font>**<font style="color:rgb(51, 51, 51);">子句/运算符用于合并两个或多个SELECT语句的结果，而不返回任何重复的行。</font>

<font style="color:rgb(51, 51, 51);">要使用UNION，每个SELECT必须具有相同数量的选定列，相同数量的列表达式，相同数据类型，并且具有相同的顺序，但是它们的长度不必相同。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是</font>**<font style="color:rgb(51, 51, 51);">UNION</font>**<font style="color:rgb(51, 51, 51);">的基本语法。</font>

```sql
SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition]

UNION

SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition]
```

<font style="color:rgb(51, 51, 51);">在此，给定条件可以是根据您的要求的任何给定表达式。  
</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">考虑以下两个表，(a)COMPANY表如下：</font>

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

<font style="color:rgb(51, 51, 51);">(b)另一个表是部门(DEPARTMENT)--</font>

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

<font style="color:rgb(51, 51, 51);">现在，让我们使用SELECT语句和UNION子句将这两个表连接起来，如下所示：</font>

```sql
sqlite>  SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT
         ON COMPANY.ID = DEPARTMENT.EMP_ID
         
         UNION
         
         SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT
         ON COMPANY.ID = DEPARTMENT.EMP_ID;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
EMP_ID      NAME                  DEPT
----------  --------------------  ----------
1           Paul                  IT Billing
2           Allen                 Engineering
3           Teddy                 Engineering
4           Mark                  Finance
5           David                 Engineering
6           Kim                   Finance
7           James                 Finance
```

## <font style="color:rgb(51, 51, 51);">UNION ALL子句</font>
<font style="color:rgb(51, 51, 51);">UNION ALL运算符用于合并两个SELECT语句的结果，包括重复的行。</font>

<font style="color:rgb(51, 51, 51);">适用于UNION的相同规则也适用于UNION ALL运算符。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是的基本语法</font>**<font style="color:rgb(51, 51, 51);">UNION ALL</font>**<font style="color:rgb(51, 51, 51);">。</font>

```sql
SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition]

UNION ALL

SELECT column1 [, column2 ]
FROM table1 [, table2 ]
[WHERE condition]
```

<font style="color:rgb(51, 51, 51);">在此，给定条件可以是根据您的要求的任何给定表达式。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">现在，让我们在SELECT语句中将上述两个表连接如下：</font>

```sql
sqlite>  SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT
         ON COMPANY.ID = DEPARTMENT.EMP_ID
         
         UNION ALL

         SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT
         ON COMPANY.ID = DEPARTMENT.EMP_ID;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
EMP_ID      NAME                  DEPT
----------  --------------------  ----------
1           Paul                  IT Billing
2           Allen                 Engineering
3           Teddy                 Engineering
4           Mark                  Finance
5           David                 Engineering
6           Kim                   Finance
7           James                 Finance
1           Paul                  IT Billing
2           Allen                 Engineering
3           Teddy                 Engineering
4           Mark                  Finance
5           David                 Engineering
6           Kim                   Finance
7           James                 Finance
```

