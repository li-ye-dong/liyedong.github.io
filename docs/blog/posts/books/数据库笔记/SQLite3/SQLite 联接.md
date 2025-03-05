<font style="color:rgb(51, 51, 51);">SQLite</font>**<font style="color:rgb(51, 51, 51);"> Joins</font>**<font style="color:rgb(51, 51, 51);">子句用于合并数据库中两个或多个表中的记录。JOIN是一种通过使用每个表的公用值来组合两个表中的字段的方法。</font>

<font style="color:rgb(51, 51, 51);">SQL定义了三种主要的联接类型-</font>

+ <font style="color:rgb(51, 51, 51);">交叉联接</font>
+ <font style="color:rgb(51, 51, 51);">内部联接</font>
+ <font style="color:rgb(51, 51, 51);">外联接</font>

<font style="color:rgb(51, 51, 51);">在继续之前，让我们考虑两个表COMPANY和DEPARTMENT。我们已经看到了INSERT语句来填充COMPANY表。所以让我们假设COMPANY表中可用的记录列表-</font>

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

<font style="color:rgb(51, 51, 51);">另一个表是DEPARTMENT，具有以下定义-</font>

```sql
CREATE TABLE DEPARTMENT(
  ID INT PRIMARY KEY      NOT NULL,
  DEPT           CHAR(50) NOT NULL,
  EMP_ID         INT      NOT NULL
);
```

<font style="color:rgb(51, 51, 51);">这是用于填充DEPARTMENT表的INSERT语句的列表-</font>

```sql
INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (1, 'IT Billing', 1 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (2, 'Engineering', 2 );

INSERT INTO DEPARTMENT (ID, DEPT, EMP_ID)
VALUES (3, 'Finance', 7 );
```

<font style="color:rgb(51, 51, 51);">最后，我们在DEPARTMENT表中有以下可用的记录列表-</font>

```sql
ID          DEPT        EMP_ID
----------  ----------  ----------
1           IT Billing  1
2           Engineering 2
3           Finance     7
```

## <font style="color:rgb(51, 51, 51);">CROSS JOIN - 交叉联接</font>
<font style="color:rgb(51, 51, 51);">CROSS JOIN将第一个表的每一行与第二个表的每一行匹配。如果输入表分别具有x和y行，则结果表将具有x * y行。由于CROSS JOINs可能会生成极大的表，因此必须注意仅在适当的时候使用它们。</font>

<font style="color:rgb(51, 51, 51);">以下是CROSS JOIN的语法-</font>

SELECT ... FROM table1 CROSS JOIN table2 ...

<font style="color:rgb(51, 51, 51);">根据上表，您可以编写CROSS JOIN，如下所示</font>

```sql
sqlite> SELECT EMP_ID, NAME, DEPT FROM COMPANY CROSS JOIN DEPARTMENT;
```

<font style="color:rgb(51, 51, 51);">上面的查询将产生以下结果-</font>

```sql
EMP_ID      NAME        DEPT
----------  ----------  ----------
1           Paul        IT Billing
2           Paul        Engineering
7           Paul        Finance
1           Allen       IT Billing
2           Allen       Engineering
7           Allen       Finance
1           Teddy       IT Billing
2           Teddy       Engineering
7           Teddy       Finance
1           Mark        IT Billing
2           Mark        Engineering
7           Mark        Finance
1           David       IT Billing
2           David       Engineering
7           David       Finance
1           Kim         IT Billing
2           Kim         Engineering
7           Kim         Finance
1           James       IT Billing
2           James       Engineering
7           James       Finance
```

## <font style="color:rgb(51, 51, 51);">INNER JOIN - 内部联接</font>
<font style="color:rgb(51, 51, 51);">INNER JOIN通过基于连接谓词组合两个表（table1和table2）的列值来创建新的结果表。该查询将table1的每一行与table2的每一行进行比较，以找到满足join谓词的所有行对。当满足连接谓词时，A和B的每个匹配行对的列值将合并为结果行。</font>

<font style="color:rgb(51, 51, 51);">INNER JOIN是最常见的默认连接类型。您可以选择使用INNER关键字。</font>

<font style="color:rgb(51, 51, 51);">以下是INNER JOIN的语法-</font>

SELECT ... FROM table1 [INNER] JOIN table2 ON conditional_expression ...

<font style="color:rgb(51, 51, 51);">为了避免冗余并缩短短语，可以使用</font>**<font style="color:rgb(51, 51, 51);">USING</font>**<font style="color:rgb(51, 51, 51);">表达式声明INNER JOIN条件。此表达式指定一个或多个列的列表。</font>

SELECT ... FROM table1 JOIN table2 USING ( column1 ,... ) ...

<font style="color:rgb(51, 51, 51);">NATURAL JOIN与</font>**<font style="color:rgb(51, 51, 51);">JOIN...USING</font>**<font style="color:rgb(51, 51, 51);">自然相似，只是它自动测试两个表中每个列的值之间是否相等-</font>

SELECT ... FROM table1 NATURAL JOIN table2...

<font style="color:rgb(51, 51, 51);">根据上面的表格，您可以编写一个INNER JOIN，如下所示：</font>

```sql
sqlite> SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT
   ON COMPANY.ID = DEPARTMENT.EMP_ID;
```

<font style="color:rgb(51, 51, 51);">上面的查询将产生以下结果-</font>

```sql
EMP_ID      NAME        DEPT
----------  ----------  ----------
1           Paul        IT Billing
2           Allen       Engineering
7           James       Finance
```

## <font style="color:rgb(51, 51, 51);">OUTER JOIN - 外联接</font>
<font style="color:rgb(51, 51, 51);">OUTER JOIN是INNER JOIN的扩展。尽管SQL标准定义了三种外部联接类型：LEFT，RIGHT和FULL，但是SQLite仅支持</font>**<font style="color:rgb(51, 51, 51);">LEFT OUTER JOIN</font>**<font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">外部联接的条件与内部联接的条件相同，使用ON，USING或NATURAL关键字表示。初始结果表的计算方法相同。一旦计算了主JOIN，OUTER JOIN将从一个或两个表中获取所有未连接的行，将它们填充为NULL，然后将它们附加到结果表中。</font>

<font style="color:rgb(51, 51, 51);">以下是LEFT OUTER JOIN的语法-</font>

```sql
SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...
```

<font style="color:rgb(51, 51, 51);">为了避免冗余并缩短短语，可以使用USING表达式声明OUTER JOIN条件。此表达式指定一个或多个列的列表。</font>

SELECT ... FROM table1 LEFT OUTER JOIN table2 USING ( column1 ,... ) ...

<font style="color:rgb(51, 51, 51);">基于上面的表，您可以编写内部联接，如下所示：</font>

```sql
sqlite> SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT
   ON COMPANY.ID = DEPARTMENT.EMP_ID;
```

<font style="color:rgb(51, 51, 51);">上面的查询将产生以下结果-</font>

```sql
EMP_ID      NAME        DEPT
----------  ----------  ----------
1           Paul        IT Billing
2           Allen       Engineering
            Teddy
            Mark
            David
            Kim
7           James       Finance
```

