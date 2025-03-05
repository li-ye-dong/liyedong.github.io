<font style="color:rgb(51, 51, 51);">SQLite ALTER TABLE命令可修改现有表，而无需执行数据的完整转储和重新加载。 您可以使用ALTER TABLE语句重命名表，并可以使用ALTER TABLE语句在现有表中添加其他列。</font>

<font style="color:rgb(51, 51, 51);">除了重命名表和在现有表中添加列之外，SQLite中的ALTER TABLE命令不支持其他操作。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是</font>**<font style="color:rgb(51, 51, 51);">ALTER TABLE</font>**<font style="color:rgb(51, 51, 51);">重命名现有表的基本语法。</font>

```sql
ALTER TABLE database_name.table_name RENAME TO new_table_name;
```

<font style="color:rgb(51, 51, 51);">以下是</font>**<font style="color:rgb(51, 51, 51);">ALTER TABLE</font>**<font style="color:rgb(51, 51, 51);">在现有表中添加新列的基本语法。</font>

```sql
ALTER TABLE database_name.table_name ADD COLUMN column_def...;
```

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">带有以下记录的COMPANY表-</font>

```plain
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

<font style="color:rgb(51, 51, 51);">现在，让我们尝试使用ALTER TABLE语句重命名该表，如下所示：</font>

```sql
sqlite> ALTER TABLE COMPANY RENAME TO OLD_COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的SQLite语句会将COMPANY表重命名为OLD_COMPANY。现在，让我们尝试在OLD_COMPANY表中添加新列，如下所示：</font>

```sql
sqlite> ALTER TABLE OLD_COMPANY ADD COLUMN SEX char(1);
```

<font style="color:rgb(51, 51, 51);">COMPANY表现在已更改，以下将是SELECT语句的输出。</font>

```plain
ID          NAME        AGE         ADDRESS     SALARY      SEX
----------  ----------  ----------  ----------  ----------  ---
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

<font style="color:rgb(51, 51, 51);">应当注意，新添加的列填充有NULL值。</font>

