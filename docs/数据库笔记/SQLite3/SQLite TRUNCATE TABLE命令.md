<font style="color:rgb(51, 51, 51);">不幸的是，我们在SQLite中没有TRUNCATE TABLE命令，但是您可以使用SQLite DELETE命令从现有表中删除完整的数据，不过建议您使用DROP TABLE命令删除完整的表并重新创建它。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是DELETE命令的基本语法。</font>

```sql
sqlite> DELETE FROM table_name;
```

<font style="color:rgb(51, 51, 51);">以下是DROP TABLE的基本语法。</font>

```sql
sqlite> DROP TABLE table_name;
```

<font style="color:rgb(51, 51, 51);">如果使用DELETE TABLE命令删除所有记录，建议使用</font>**<font style="color:rgb(51, 51, 51);">VACUUM</font>**<font style="color:rgb(51, 51, 51);">命令清除未使用的空间。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
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

<font style="color:rgb(51, 51, 51);">以下是截断上表的示例-</font>

```sql
SQLite> DELETE FROM COMPANY;
SQLite> VACUUM;
```

<font style="color:rgb(51, 51, 51);">现在，COMPANY表被完全截断，并且SELECT语句的输出将为零。</font>

<font style="color:rgb(133, 144, 166);background-color:rgb(251, 251, 251);">  
</font>

