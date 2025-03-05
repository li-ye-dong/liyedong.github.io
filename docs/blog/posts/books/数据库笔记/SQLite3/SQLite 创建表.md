<font style="color:rgb(51, 51, 51);">SQLite CREATE TABLE语句用于在任何给定数据库中创建新表。创建基本表包括命名表、定义其列和每列的数据类型。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是CREATE TABLE语句的基本语法。</font>

```sql
CREATE TABLE database_name.table_name(
  column1 datatype PRIMARY KEY(one or more columns),
  column2 datatype,
  column3 datatype,
  .....
  columnN datatype);
```

<font style="color:rgb(51, 51, 51);">CREATE TABLE是告诉数据库系统创建新表的关键字。该表的唯一名称或标识符位于CREATE TABLE语句之后。（可选）您可以指定</font>_<font style="color:rgb(51, 51, 51);">database_name</font>_<font style="color:rgb(51, 51, 51);">和</font>_<font style="color:rgb(51, 51, 51);">table_name</font>_<font style="color:rgb(51, 51, 51);">。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">下面是一个示例，该示例创建一个ID为主键的COMPANY表，而NOT NULL是约束条件，表明在此表中创建记录时这些字段不能为NULL。</font>

```sql
sqlite> CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL
);
```

<font style="color:rgb(51, 51, 51);">让我们再创建一个表，在以后的章节中的练习中将使用该表。</font>

```sql
sqlite> CREATE TABLE DEPARTMENT(
  ID INT PRIMARY KEY      NOT NULL,
  DEPT           CHAR(50) NOT NULL,
  EMP_ID         INT      NOT NULL
);
```

<font style="color:rgb(51, 51, 51);">您可以使用SQLite命令</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.tables</font>**`<font style="color:rgb(51, 51, 51);">命令验证是否已成功创建表，该命令将用于列出附加数据库中的所有表。</font>

```sql
sqlite>.tables
COMPANY     DEPARTMENT
```

<font style="color:rgb(51, 51, 51);">在这里，您可以看到COMPANY表两次，因为它显示了为主数据库的COMPANY表和为您的testDB.db创建的“ test”别名的test.COMPANY表。您可以使用以下SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.schema</font>**`<font style="color:rgb(51, 51, 51);">命令获取有关表的完整信息。</font>

```sql
sqlite>.schema COMPANY
CREATE TABLE COMPANY(
  ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL
);
```

