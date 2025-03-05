<font style="color:rgb(51, 51, 51);">SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> INSERT INTO</font>**`<font style="color:rgb(51, 51, 51);">语句用于将新的数据行添加到数据库的表中。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是INSERT INTO语句的两种基本语法。</font>

INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  VALUES (value1, value2, value3,...valueN);

<font style="color:rgb(51, 51, 51);">在这里，column1，column2，... columnN是表中要向其中插入数据的列的名称。</font>

<font style="color:rgb(51, 51, 51);">如果要为表中的所有列添加值，则可能不需要在 SQLite 查询中指定列名。但是，请确保值的顺序与表中的列的顺序相同。SQLite INSERT INTO 语法如下-所示</font>

INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">考虑您已经在testDB.db中创建了COMPANY表，如下所示：</font>

```plain
sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

<font style="color:rgb(51, 51, 51);">现在，以下语句将在COMPANY表中创建六个记录。</font>

```plain
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (1, 'Paul', 32, 'California', 20000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (2, 'Allen', 25, 'Texas', 15000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (5, 'David', 27, 'Texas', 85000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (6, 'Kim', 22, 'South-Hall', 45000.00 );
```

<font style="color:rgb(51, 51, 51);">您可以使用第二种语法在COMPANY表中创建记录，如下所示：</font>

```python
INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );
```

<font style="color:rgb(51, 51, 51);">以上所有语句将在COMPANY表中创建以下记录。在下一章中，您将学习如何从表中显示所有这些记录。</font>

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

## <font style="color:rgb(51, 51, 51);">使用另一个表填充一个表</font>
<font style="color:rgb(51, 51, 51);">您可以通过另一个表上的select语句将数据填充到表中，前提是另一个表具有一组字段，这些字段是填充第一个表所必需的。这是语法-</font>

```plain
INSERT INTO first_table_name [(column1, column2, ... columnN)] 
   SELECT column1, column2, ...columnN 
   FROM second_table_name
   [WHERE condition];
```

<font style="color:rgb(51, 51, 51);">现在，您可以跳过上述声明。首先，让我们学习SELECT和WHERE子句，这些子句将在后续章节中介绍。</font>

