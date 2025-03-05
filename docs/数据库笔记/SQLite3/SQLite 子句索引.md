<font style="color:rgb(51, 51, 51);">“ INDEXED BY index-name”子句指定必须使用命名索引才能在上表中查找值。</font>

<font style="color:rgb(51, 51, 51);">如果index-name不存在或不能用于查询，则SQLite语句的准备失败。</font>

<font style="color:rgb(51, 51, 51);">“ NOT INDEXED”子句指定访问上表时不使用索引，包括由UNIQUE和PRIMARY KEY约束创建的隐式索引。</font>

<font style="color:rgb(51, 51, 51);">但是，即使指定了“ NOT INDEXED”，仍可以使用INTEGER PRIMARY KEY查找条目。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是INDEXED BY子句的语法，可以与DELETE，UPDATE或SELECT语句一起使用。</font>

```sql
SELECT|DELETE|UPDATE column1, column2...INDEXED BY (index_name)table_nameWHERE (CONDITION);
```

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">在表COMPANY我们将创建一个索引并将其用于执行INDEXED BY操作。</font>

```plain
sqlite> CREATE INDEX salary_index ON COMPANY(salary);
sqlite>
```

<font style="color:rgb(51, 51, 51);">现在从表COMPANY中选择数据，您可以使用INDEXED BY子句，如下所示：</font>

```sql
sqlite> SELECT * FROM COMPANY INDEXED BY salary_index WHERE salary > 5000;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```plain
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
7           James       24          Houston     10000.0
2           Allen       25          Texas       15000.0
1           Paul        32          California  20000.0
3           Teddy       23          Norway      20000.0
6           Kim         22          South-Hall  45000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
```

