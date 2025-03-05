<font style="color:rgb(51, 51, 51);">SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> SELECT</font>**`<font style="color:rgb(51, 51, 51);">语句用于从SQLite数据库表中获取数据，该表以结果表的形式返回数据。这些结果表也称为</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">result sets</font>**`<font style="color:rgb(51, 51, 51);">。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是SQLite SELECT语句的基本语法。</font>

```python
SELECT column1, column2, columnN FROM table_name;
```

<font style="color:rgb(51, 51, 51);">在这里，column1，column2 ...是表的字段，您要获取其值。如果要获取该字段中所有可用的字段，则可以使用以下语法-</font>

```python
SELECT * FROM table_name;
```

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">考虑带有以下记录的COMPANY表-</font>

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

<font style="color:rgb(51, 51, 51);">以下是使用SELECT语句获取并显示所有这些记录的示例。在这里，前三个命令已用于设置正确格式的输出。</font>

```sql
sqlite>.header on
sqlite>.mode column
sqlite> SELECT * FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">最后，您将获得以下结果。</font>

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

<font style="color:rgb(51, 51, 51);">如果您只想获取COMPANY表的选定字段，则使用以下查询-</font>

```python
sqlite> SELECT ID, NAME, SALARY FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的查询将产生以下结果。</font>

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

## <font style="color:rgb(51, 51, 51);">设置输出列宽</font>
<font style="color:rgb(51, 51, 51);">有时，</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.mode column</font>**`<font style="color:rgb(51, 51, 51);">由于要显示的列的默认宽度，您会遇到与截断输出有关的问题。您可以做的是，可以使用以下</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.width num, num....</font>**`<font style="color:rgb(51, 51, 51);">命令设置列可显示的列宽：</font>

```sql
sqlite>.width 10, 20, 10
sqlite>SELECT * FROM COMPANY;
```

<font style="color:rgb(51, 51, 51);">上面的</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.width</font>**`<font style="color:rgb(51, 51, 51);">命令将第一列的宽度设置为10，第二列的宽度设置为20，第三列的宽度设置为10。最后，上面的SELECT语句将给出以下结果。</font>

```sql
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

## <font style="color:rgb(51, 51, 51);">模式信息</font>
<font style="color:rgb(51, 51, 51);">由于所有的 dot 命令都可以在 SQLite 提示符下使用，因此在使用 SQLite 编程时，您将使用下面的 SELECT 语句和 SQLite 主表列出在数据库中创建的所有表。</font>

```python
sqlite> SELECT tbl_name FROM sqlite_master WHERE type = 'table';
```

<font style="color:rgb(51, 51, 51);">假设您的testDB.db中只有COMPANY表，这将产生以下结果。</font>

```python
tbl_name----------COMPANY
```

<font style="color:rgb(51, 51, 51);">您可以列出有关COMPANY表的完整信息，如下所示：</font>

```python
sqlite> SELECT sql FROM sqlite_master WHERE type = 'table' AND tbl_name = 'COMPANY';
```

<font style="color:rgb(51, 51, 51);">假设您的testDB.db中只有COMPANY表，这将产生以下结果。</font>

```sql
CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL)
```

