<font style="color:rgb(51, 51, 51);">SQLite</font>**<font style="color:rgb(51, 51, 51);"> GROUP BY </font>**<font style="color:rgb(51, 51, 51);">子句与SELECT语句配合使用，以将相同的数据分组。</font>

<font style="color:rgb(51, 51, 51);">GROUP BY子句在SELECT语句中的WHERE子句之后，并在ORDER BY子句之前。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是GROUP BY子句的基本语法。GROUP BY子句必须遵循WHERE子句中的条件，并且如果使用ORDER BY子句，则必须在ORDER BY子句之前。</font>

```sql
SELECT column-list
FROM table_name
WHERE [ conditions ]
GROUP BY column1, column2....columnN
ORDER BY column1, column2....columnN
```

<font style="color:rgb(51, 51, 51);">您可以在GROUP BY子句中使用多个列。确保要用于分组的任何列，该列都应该在column-list中可用。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">考虑带有以下记录的COMPANY表。</font>

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

<font style="color:rgb(51, 51, 51);">如果您想知道每个客户的工资总额，那么GROUP BY查询将如下所示-</font>

```sql
sqlite> SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME;
```

<font style="color:rgb(51, 51, 51);">输出结果：</font>

```sql
NAME        SUM(SALARY)
----------  -----------
Allen       15000.0
David       85000.0
James       10000.0
Kim         45000.0
Mark        65000.0
Paul        20000.0
Teddy       20000.0
```

<font style="color:rgb(51, 51, 51);">现在，让我们使用以下INSERT语句在COMPANY表中再创建三个记录。  
</font>

```sql
INSERT INTO COMPANY VALUES (8, 'Paul', 24, 'Houston', 20000.00 );
INSERT INTO COMPANY VALUES (9, 'James', 44, 'Norway', 5000.00 );
INSERT INTO COMPANY VALUES (10, 'James', 45, 'Texas', 5000.00 );
```

<font style="color:rgb(51, 51, 51);">现在，我们的表具有以下重复名称的记录。</font>

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
8           Paul        24          Houston     20000.0
9           James       44          Norway      5000.0
10          James       45          Texas       5000.0
```

<font style="color:rgb(51, 51, 51);">再次，让我们使用相同的语句使用NAME列对所有记录进行分组，如下所示：</font>

```sql
sqlite> SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME ORDER BY NAME;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
NAME        SUM(SALARY)
----------  -----------
Allen       15000
David       85000
James       20000
Kim         45000
Mark        65000
Paul        40000
Teddy       20000
```

<font style="color:rgb(51, 51, 51);">让我们如下使用ORDER BY子句和GROUP BY子句-</font>

```sql
sqlite>  SELECT NAME, SUM(SALARY) 
   FROM COMPANY GROUP BY NAME ORDER BY NAME DESC;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
NAME        SUM(SALARY)
----------  -----------
Teddy       20000
Paul        40000
Mark        65000
Kim         45000
James       20000
David       85000
Allen       15000
```

