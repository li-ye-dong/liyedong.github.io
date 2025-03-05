<font style="color:rgb(51, 51, 51);">SQLite AUTOINCREMENT是用于自动递增表中字段值的关键字。我们可以使用AUTOINCREMENT关键字在创建具有特定列名的表时自动递增字段值。</font>

<font style="color:rgb(51, 51, 51);">关键字</font>**<font style="color:rgb(51, 51, 51);"> </font>****<font style="color:rgb(51, 51, 51);">AUTOINCREMENT</font>****<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">只能与INTEGER字段一起使用。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
**<font style="color:rgb(51, 51, 51);">AUTOINCREMENT</font>**<font style="color:rgb(51, 51, 51);">关键字的基本用法如下-</font>

```sql
CREATE TABLE table_name(
  column1 INTEGER AUTOINCREMENT,
  column2 datatype,
  column3 datatype,
  .....
  columnN datatype,
);
```

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">考虑如下创建的COMPANY表-</font>

```sql
sqlite> CREATE TABLE COMPANY(
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  NAME           TEXT      NOT NULL,
  AGE            INT       NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL
);
```

<font style="color:rgb(51, 51, 51);">现在，将以下记录插入表COMPANY-</font>

```sql
INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
VALUES ( 'Paul', 32, 'California', 20000.00 );

INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
VALUES ('Allen', 25, 'Texas', 15000.00 );

INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
VALUES ('Teddy', 23, 'Norway', 20000.00 );

INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
VALUES ( 'Mark', 25, 'Rich-Mond ', 65000.00 );

INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
VALUES ( 'David', 27, 'Texas', 85000.00 );

INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
VALUES ( 'Kim', 22, 'South-Hall', 45000.00 );

INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)
VALUES ( 'James', 24, 'Houston', 10000.00 );
```

<font style="color:rgb(51, 51, 51);">这将在表COMPANY中插入7个元组，并且COMPANY将具有以下记录-</font>

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

