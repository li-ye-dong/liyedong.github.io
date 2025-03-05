<font style="color:rgb(51, 51, 51);">事务是针对数据库执行的工作单元。事务是以逻辑顺序完成的单位或工作顺序，无论是由用户手动完成还是由某种数据库程序自动完成。</font>

<font style="color:rgb(51, 51, 51);">事务是将一个或多个更改传播到数据库。例如，如果您要在表中创建，更新或删除记录，那么您将在表上执行事务。控制事务以确保数据完整性和处理数据库错误很重要。</font>

<font style="color:rgb(51, 51, 51);">实际上，您会将许多SQLite查询组成一个组，并将它们作为事务的一部分一起执行。</font>

## <font style="color:rgb(51, 51, 51);">事务属性</font>
<font style="color:rgb(51, 51, 51);">事务具有以下四个标准属性，通常由首字母缩写ACID指代。</font>

+ **<font style="color:rgb(51, 51, 51);">原子性(Atomicity)：</font>**<font style="color:rgb(51, 51, 51);">确保工作单位内的所有操作都成功完成，否则，事务会在出现故障时终止，之前的操作也会回滚到以前的状态。</font>
+ **<font style="color:rgb(51, 51, 51);">一致性（Consistency)：</font>**<font style="color:rgb(51, 51, 51);">确保数据库在成功提交的事务上正确地改变状态。</font>
+ **<font style="color:rgb(51, 51, 51);">隔离性(Isolation)：</font>**<font style="color:rgb(51, 51, 51);">使事务操作相互独立和透明。</font>
+ **<font style="color:rgb(51, 51, 51);">持久性(Durability)：</font>**<font style="color:rgb(51, 51, 51);">确保已提交事务的结果或效果在系统发生故障的情况下仍然存在。</font>

## <font style="color:rgb(51, 51, 51);">事务控制</font>
<font style="color:rgb(51, 51, 51);">以下是用于控制事务的以下命令：</font>

+ **<font style="color:rgb(51, 51, 51);">BEGIN TRANSACTION</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−开始事务。</font>
+ **<font style="color:rgb(51, 51, 51);">COMMIT</font>**<font style="color:rgb(51, 51, 51);">−要保存更改，也可以使用</font>**<font style="color:rgb(51, 51, 51);">END TRANSACTION</font>**<font style="color:rgb(51, 51, 51);">命令。</font>
+ **<font style="color:rgb(51, 51, 51);">ROLLBACK</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−回滚更改。</font>

<font style="color:rgb(51, 51, 51);">事务控制命令只与 DML 命令 INSERT、UPDATE 和 DELETE 一起使用。他们不能在创建表或删除表时使用，因为这些操作在数据库中是自动提交的。</font>

### <font style="color:rgb(51, 51, 51);">BEGIN TRANSACTION 命令</font>
<font style="color:rgb(51, 51, 51);">可以使用BEGIN TRANSACTION或简单地使用BEGIN命令来启动事务。这样的事务通常会持续到遇到下一个COMMIT或ROLLBACK命令为止。但是，如果数据库关闭或发生错误，则事务也将回滚。以下是启动事务的简单语法。</font>

```sql
BEGIN;
or 
BEGIN TRANSACTION;
```

### <font style="color:rgb(51, 51, 51);">COMMIT 命令</font>
<font style="color:rgb(51, 51, 51);">COMMIT命令是用于将事务调用的更改保存到数据库的事务性命令。</font>

<font style="color:rgb(51, 51, 51);">自上一个COMMIT或ROLLBACK命令以来，COMMIT命令将所有事务保存到数据库中。</font>

<font style="color:rgb(51, 51, 51);">以下是COMMIT命令的语法。</font>

```sql
COMMIT;
or
END TRANSACTION;
```

### <font style="color:rgb(51, 51, 51);">ROLLBACK 命令</font>
<font style="color:rgb(51, 51, 51);">ROLLBACK命令是用于撤消尚未保存到数据库的事务的事务性命令。</font>

<font style="color:rgb(51, 51, 51);">自上次发出COMMIT或ROLLBACK命令以来，ROLLBACK命令只能用于撤消事务。</font>

<font style="color:rgb(51, 51, 51);">以下是ROLLBACK命令的语法。</font>

ROLLBACK;

**<font style="color:rgb(51, 51, 51);">在线示例</font>**

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

<font style="color:rgb(51, 51, 51);">现在，让我们开始一个事务并从age = 25的表中删除记录。然后，使用ROLLBACK命令撤消所有更改。</font>

```sql
sqlite> BEGIN;
sqlite> DELETE FROM COMPANY WHERE AGE = 25;
sqlite> ROLLBACK;
```

<font style="color:rgb(51, 51, 51);">现在，如果您检查COMPANY表，它仍然具有以下记录-</font>

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

<font style="color:rgb(51, 51, 51);">让我们开始另一个事务，并从AGE= 25的表中删除记录，最后我们使用COMMIT命令来提交所有更改。</font>

```sql
sqlite> BEGIN;
sqlite> DELETE FROM COMPANY WHERE AGE = 25;
sqlite> COMMIT;
```

<font style="color:rgb(51, 51, 51);">如果现在检查COMPANY表仍然具有以下记录-</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
3           Teddy       23          Norway      20000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

