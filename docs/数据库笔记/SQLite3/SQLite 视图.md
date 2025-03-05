<font style="color:rgb(51, 51, 51);">视图只不过是数据库中存储的带有相关名称的 SQLite 语句。它实际上是一个预定义 SQLite 查询形式的表的组合。</font>

<font style="color:rgb(51, 51, 51);">一个视图可以包含一个表的所有行或一个或多个表中的选定行。可以从一个或多个表创建视图，这取决于编写的SQLite查询来创建视图。</font>

<font style="color:rgb(51, 51, 51);">作为虚拟表的视图允许用户-</font>

+ <font style="color:rgb(51, 51, 51);">以用户或用户类别自然或直观的方式来构造数据。</font>
+ <font style="color:rgb(51, 51, 51);">限制对数据的访问，以便用户只能看到有限的数据，而不是完整的表。</font>
+ <font style="color:rgb(51, 51, 51);">汇总各种表中的数据，这些数据可用于生成报告。</font>

<font style="color:rgb(51, 51, 51);">SQLite视图是只读的，因此您可能无法在视图上执行DELETE，INSERT或UPDATE语句。但是，您可以在视图上创建触发器，该触发器将在尝试删除，插入或更新视图时触发，并在触发器主体中执行所需的操作。</font>

## <font style="color:rgb(51, 51, 51);">创建视图</font>
<font style="color:rgb(51, 51, 51);">使用</font>**<font style="color:rgb(51, 51, 51);">CREATE VIEW</font>**<font style="color:rgb(51, 51, 51);">语句创建SQLite视图。可以从一个表，多个表或另一个视图创建SQLite视图。</font>

<font style="color:rgb(51, 51, 51);">以下是基本的CREATE VIEW语法。</font>

```sql
CREATE [TEMP | TEMPORARY] VIEW view_name ASSELECT column1, column2.....FROM table_nameWHERE [condition];
```

<font style="color:rgb(51, 51, 51);">您可以像在普通SQL SELECT查询中使用多个表一样，在SELECT语句中包括多个表。如果存在可选的TEMP或TEMPORARY关键字，则将在temp数据库中创建该视图。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">带有以下记录的COMPANY表-</font>

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

<font style="color:rgb(51, 51, 51);">以下是从COMPANY表创建视图的示例。该视图将仅用于COMPANY表中的几列。</font>

```sql
sqlite> CREATE VIEW COMPANY_VIEW AS
SELECT ID, NAME, AGE
FROM  COMPANY;
```

<font style="color:rgb(51, 51, 51);">现在，您可以通过查询实际表的类似方式查询COMPANY_VIEW。以下是一个实例-</font>

```sql
sqlite> SELECT * FROM COMPANY_VIEW;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE
----------  ----------  ----------
1           Paul        32
2           Allen       25
3           Teddy       23
4           Mark        25
5           David       27
6           Kim         22
7           James       24
```

## <font style="color:rgb(51, 51, 51);">删除视图</font>
<font style="color:rgb(51, 51, 51);">要删除视图，只需将DROP VIEW语句与一起使用</font>**<font style="color:rgb(51, 51, 51);">view_name</font>**<font style="color:rgb(51, 51, 51);">。基本的DROP VIEW语法如下-</font>

```sql
sqlite> DROP VIEW view_name;
```

<font style="color:rgb(51, 51, 51);">以下命令将删除我们在上一节中创建的COMPANY_VIEW视图。</font>

```sql
sqlite> DROP VIEW COMPANY_VIEW;
```

