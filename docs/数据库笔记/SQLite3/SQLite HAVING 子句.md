<font style="color:rgb(51, 51, 51);">HAVING子句使您可以指定条件，以过滤哪些组结果出现在最终结果中。</font>

<font style="color:rgb(51, 51, 51);">WHERE子句在所选列上放置条件，而HAVING子句在GROUP BY子句创建的组上放置条件。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是HAVING子句在SELECT查询中的位置。</font>

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

<font style="color:rgb(51, 51, 51);">HAVING子句必须在查询中的GROUP BY子句之后，并且如果使用，还必须在ORDER BY子句之前。以下是SELECT语句的语法，包括HAVING子句。</font>

```sql
SELECT column1, column2
FROM table1, table2
WHERE [ conditions ]
GROUP BY column1, column2
HAVING [ conditions ]
ORDER BY column1, column2
```

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
8           Paul        24          Houston     20000.0
9           James       44          Norway      5000.0
10          James       45          Texas       5000.0
```

<font style="color:rgb(51, 51, 51);">以下是示例，它将显示名称计数小于2的记录。</font>

```python
sqlite > SELECT * FROM COMPANY GROUP BY name HAVING count(name) < 2;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000
5           David       27          Texas       85000
6           Kim         22          South-Hall  45000
4           Mark        25          Rich-Mond   65000
3           Teddy       23          Norway      20000
```

<font style="color:rgb(51, 51, 51);">下面是示例，它将显示名称计数大于2的记录。</font>

```python
sqlite > SELECT * FROM COMPANY GROUP BY name HAVING count(name) > 2;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
10          James       45          Texas       5000
```

