<font style="color:rgb(51, 51, 51);">子查询或内部查询或嵌套查询是另一个SQLite查询中的查询，并嵌入在WHERE子句中。</font>

<font style="color:rgb(51, 51, 51);">子查询用于返回将在主查询中使用的数据，作为进一步限制要检索的数据的条件。</font>

<font style="color:rgb(51, 51, 51);">子查询可以与SELECT，INSERT，UPDATE和DELETE语句以及=，<，>，> =，<=，IN，BETWEEN等运算符一起使用。</font>

<font style="color:rgb(51, 51, 51);">有一些子查询必须遵循的规则-</font>

+ <font style="color:rgb(51, 51, 51);">子查询必须放在括号内。</font>
+ <font style="color:rgb(51, 51, 51);">子查询在SELECT子句中只能有一个列，除非主查询中有多个列供子查询比较其选定的列。</font>
+ <font style="color:rgb(51, 51, 51);">尽管主查询可以使用ORDER BY，但是不能在子查询中使用ORDER BY。GROUP BY可用于执行与子查询中的ORDER BY相同的功能。</font>
+ <font style="color:rgb(51, 51, 51);">返回多行的子查询只能与多个值运算符（例如IN运算符）一起使用。</font>
+ <font style="color:rgb(51, 51, 51);">BETWEEN运算符不能与子查询一起使用；但是，可以在子查询中使用BETWEEN。</font>

## <font style="color:rgb(51, 51, 51);">带有SELECT语句的子查询</font>
<font style="color:rgb(51, 51, 51);">子查询最常与SELECT语句一起使用。基本语法如下-</font>

```sql
SELECT column_name [, column_name ]
FROM table1 [, table2 ]
WHERE column_name OPERATOR
   (SELECT column_name [, column_name ]
    FROM table1 [, table2 ]
    [WHERE])
```

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">带有以下记录的COMPANY表。</font>

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

<font style="color:rgb(51, 51, 51);">现在，让我们使用SELECT语句检查以下子查询。</font>

```sql
sqlite> SELECT * 
   FROM COMPANY 
   WHERE ID IN (SELECT ID 
                FROM COMPANY 
                WHERE SALARY > 45000) ;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

## <font style="color:rgb(51, 51, 51);">带有INSERT语句的子查询</font>
<font style="color:rgb(51, 51, 51);">子查询也可以与INSERT语句一起使用。INSERT语句使用从子查询返回的数据插入另一个表。可以使用任何字符，日期或数字功能修改子查询中的选定数据。</font>

<font style="color:rgb(51, 51, 51);">以下是基本语法如下-</font>

```sql
INSERT INTO table_name [ (column1 [, column2 ]) ]
   SELECT [ *|column1 [, column2 ]
           FROM table1 [, table2 ]
           [ WHERE VALUE OPERATOR ]
```

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">考虑一个表COMPANY_BKP，其结构与COMPANY表相似，并且可以使用COMPANY_BKP作为表名使用相同的CREATE TABLE创建。要将完整的COMPANY表复制到COMPANY_BKP，请使用以下语法-</font>

```sql
sqlite> INSERT INTO COMPANY_BKP
   SELECT * FROM COMPANY 
   WHERE ID IN (SELECT ID 
                FROM COMPANY) ;
```

## <font style="color:rgb(51, 51, 51);">带有UPDATE语句的子查询</font>
<font style="color:rgb(51, 51, 51);">子查询可以与UPDATE语句结合使用。使用带有UPDATE语句的子查询时，可以更新表中的单列或多列。</font>

<font style="color:rgb(51, 51, 51);">以下是基本语法如下-</font>

```sql
UPDATE tableSET column_name = new_value[ WHERE OPERATOR [ VALUE ]
                                        (SELECT COLUMN_NAME
    FROM TABLE_NAME)
                                        [ WHERE) ]
```

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">假设我们有COMPANY_BKP表可用，它是COMPANY表的备份。</font>

<font style="color:rgb(51, 51, 51);">以下示例将COMPANY表中年龄大于或等于27岁的所有客户的薪资更新0.50倍。</font>

```sql
sqlite> UPDATE COMPANY
   SET SALARY = SALARY * 0.50
   WHERE AGE IN (SELECT AGE FROM COMPANY_BKP
                 WHERE AGE >= 27 );
```

<font style="color:rgb(51, 51, 51);">这将影响两行，最后COMPANY表将具有以下记录-</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  10000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       42500.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

## <font style="color:rgb(51, 51, 51);">带有DELETE语句的子查询</font>
<font style="color:rgb(51, 51, 51);">子查询可以与DELETE语句一起使用，就像上面提到的任何其他语句一样。</font>

<font style="color:rgb(51, 51, 51);">以下是基本语法如下-</font>

```sql
DELETE FROM TABLE_NAME[ WHERE OPERATOR [ VALUE ]
                       (SELECT COLUMN_NAME
    FROM TABLE_NAME)
                       [ WHERE) ]
```

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">假设我们有COMPANY_BKP表可用，它是COMPANY表的备份。</font>

<font style="color:rgb(51, 51, 51);">下面的示例从COMPANY表中删除年龄大于或等于27的所有客户的记录。</font>

```sql
sqlite> DELETE FROM COMPANY
   WHERE AGE IN (SELECT AGE FROM COMPANY_BKP
                 WHERE AGE > 27 );
```

<font style="color:rgb(51, 51, 51);">这将影响两行，最后COMPANY表将具有以下记录-</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       42500.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

