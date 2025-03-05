<font style="color:rgb(51, 51, 51);">表达式是一个或多个值，运算符以及对一个值求值的SQL函数的组合。</font>

<font style="color:rgb(51, 51, 51);">SQL表达式类似于公式，它们以查询语言编写。您还可以用于在数据库中查询一组特定的数据。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">看SELECT语句的基本语法，如下所示：</font>

```python
SELECT column1, column2, columnN FROM table_name WHERE [CONDITION | EXPRESSION];
```

<font style="color:rgb(51, 51, 51);">以下是不同类型的SQLite表达式。</font>

## <font style="color:rgb(51, 51, 51);">SQLite-布尔表达式</font>
<font style="color:rgb(51, 51, 51);">SQLite布尔表达式基于匹配的单个值获取数据。以下是语法-</font>

```python
SELECT column1, column2, columnN FROM table_name WHERE SINGLE VALUE MATCHTING EXPRESSION;
```

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

<font style="color:rgb(51, 51, 51);">以下是显示SQLite布尔表达式用法的简单示例-</font>

```sql
sqlite> SELECT * FROM COMPANY WHERE SALARY = 10000;

ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
4           James        24          Houston   10000.0
```

## <font style="color:rgb(51, 51, 51);">SQLite-数值表达式</font>
<font style="color:rgb(51, 51, 51);">这些表达式用于在任何查询中执行任何数学运算。以下是语法-</font>

SELECT numerical_expression as OPERATION_NAME[FROM table_name WHERE CONDITION] ;

<font style="color:rgb(51, 51, 51);">此处，numeric_expression用于数学表达式或任何公式。下面是一个简单的示例，显示了SQLite数值表达式的用法。</font>

```sql
sqlite> SELECT (15 + 6) AS ADDITION
ADDITION = 21
```

<font style="color:rgb(51, 51, 51);">有几个内置函数，如avg()、sum()、count()等，用于对表或特定表列执行所谓的聚合数据计算。</font>

```sql
sqlite> SELECT COUNT(*) AS "RECORDS" FROM COMPANY; 
RECORDS = 7
```

## <font style="color:rgb(51, 51, 51);">SQLite-日期表达式</font>
<font style="color:rgb(51, 51, 51);">日期表达式返回当前系统日期和时间值。这些表达式用于各种数据操作中。</font>

```sql
sqlite> SELECT CURRENT_TIMESTAMP;
CURRENT_TIMESTAMP = 2013-03-17 10:43:35
```

