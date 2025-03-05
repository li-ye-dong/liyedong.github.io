<font style="color:rgb(51, 51, 51);">SQLite</font>**<font style="color:rgb(51, 51, 51);"> DISTINCT</font>**<font style="color:rgb(51, 51, 51);">关键字与SELECT语句结合使用，以消除所有重复记录并仅获取唯一记录。</font>

<font style="color:rgb(51, 51, 51);">当表中有多个重复记录时，可能会出现这种情况。在获取此类记录时，仅获取唯一记录而不是获取重复记录更为有意义。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是DISTINCT关键字消除重复记录的基本语法。</font>

```sql
SELECT DISTINCT column1, column2,.....columnN FROM table_name
WHERE [condition]
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

<font style="color:rgb(51, 51, 51);">首先，让我们看看下面的SELECT查询如何返回重复的薪水记录。</font>

```python
sqlite> SELECT name FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
NAME
----------
Paul
Allen
Teddy
Mark
David
Kim
James
Paul
James
James
```

<font style="color:rgb(51, 51, 51);">现在，让我们</font>**<font style="color:rgb(51, 51, 51);">DISTINCT</font>**<font style="color:rgb(51, 51, 51);">在上面的SELECT查询中使用关键字并查看结果。</font>

```python
sqlite> SELECT DISTINCT name FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果，其中没有重复的条目。</font>

```sql
NAME
----------
Paul
Allen
Teddy
Mark
David
Kim
James
```

