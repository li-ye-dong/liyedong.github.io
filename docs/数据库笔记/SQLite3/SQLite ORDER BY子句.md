<font style="color:rgb(51, 51, 51);">SQLite</font>**<font style="color:rgb(51, 51, 51);"> ORDER BY</font>**<font style="color:rgb(51, 51, 51);">子句用于根据一个或多个列以升序或降序对数据进行排序。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是ORDER BY子句的基本语法。</font>

```python
SELECT column-list FROM table_name [WHERE condition] [ORDER BY column1, column2, .. columnN] [ASC | DESC];
```

<font style="color:rgb(51, 51, 51);">您可以在ORDER BY子句中使用多个列。确保要用于排序的任何列，该列都应在column-list中可用。</font>

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

<font style="color:rgb(51, 51, 51);">下面是一个示例，它将按SALARY降序对结果进行排序。</font>

```python
sqlite> SELECT * FROM COMPANY ORDER BY SALARY ASC;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
7           James       24          Houston     10000.0
2           Allen       25          Texas       15000.0
1           Paul        32          California  20000.0
3           Teddy       23          Norway      20000.0
6           Kim         22          South-Hall  45000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

<font style="color:rgb(51, 51, 51);">下面是一个示例，它将按NAME和SALARY的降序对结果进行排序。</font>

```python
sqlite> SELECT * FROM COMPANY ORDER BY NAME, SALARY ASC;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000.0
5           David       27          Texas       85000.0
7           James       24          Houston     10000.0
6           Kim         22          South-Hall  45000.0
4           Mark        25          Rich-Mond   65000.0
1           Paul        32          California  20000.0
3           Teddy       23          Norway      20000.0
```

<font style="color:rgb(51, 51, 51);">以下是一个示例，它将按照NAME的降序对结果进行排序。</font>

```python
sqlite> SELECT * FROM COMPANY ORDER BY NAME DESC;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
3           Teddy       23          Norway      20000.0
1           Paul        32          California  20000.0
4           Mark        25          Rich-Mond   65000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
5           David       27          Texas       85000.0
2           Allen       25          Texas       15000.0
```

