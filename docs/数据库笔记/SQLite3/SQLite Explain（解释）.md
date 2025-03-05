<font style="color:rgb(51, 51, 51);">SQLite语句前面可以加关键字“EXPLAIN”或短语“EXPLAIN QUERY PLAN”，用于描述表的详细信息。</font>

<font style="color:rgb(51, 51, 51);">这两种修改都会导致 SQLite 语句表现为一个查询，并返回关于如果省略了 EXPLAIN 关键字或短语 SQLite 语句将如何运行的信息。</font>

+ <font style="color:rgb(51, 51, 51);">EXPLAIN和EXPLAIN QUERY PLAN的输出仅用于交互式分析和故障排除。</font>
+ <font style="color:rgb(51, 51, 51);">输出格式的详细信息可能会从一个版本的SQLite更改为下一个版本。</font>
+ <font style="color:rgb(51, 51, 51);">应用程序不应该使用 EXPLAIN 或 EXPLAIN QUERY PLAN，因为其确切的行为是可变的且只有部分会被记录。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
**<font style="color:rgb(51, 51, 51);">EXPLAIN</font>**<font style="color:rgb(51, 51, 51);">的语法如下:</font>

```sql
EXPLAIN [SQLite Query]
```

**<font style="color:rgb(51, 51, 51);">EXPLAIN QUERY PLAN</font>**<font style="color:rgb(51, 51, 51);">的语法如下:</font>

```sql
EXPLAIN  QUERY PLAN [SQLite Query]
```

## <font style="color:rgb(51, 51, 51);">在线示例</font>
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

<font style="color:rgb(51, 51, 51);">现在，让我们使用SELECT语句检查以下子查询-</font>

```sql
sqlite> EXPLAIN SELECT * FROM COMPANY WHERE Salary >= 20000;
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
addr        opcode      p1          p2          p3
----------  ----------  ----------  ----------  ----------
0           Goto        0           19
1           Integer     0           0
2           OpenRead    0           8
3           SetNumColu  0           5
4           Rewind      0           17
5           Column      0           4
6           RealAffini  0           0
7           Integer     20000       0
8           Lt          357         16          collseq(BI
                                                        9           Rowid       0           0
                                                        10          Column      0           1
                                                        11          Column      0           2
                                                        12          Column      0           3
                                                        13          Column      0           4
                                                        14          RealAffini  0           0
                                                        15          Callback    5           0
                                                        16          Next        0           5
                                                        17          Close       0           0
                                                        18          Halt        0           0
                                                        19          Transactio  0           0
                                                        20          VerifyCook  0           38
                                                        21          Goto        0           1
                                                        22          Noop        0           0
```

<font style="color:rgb(51, 51, 51);">现在，让我们检查 SELECT 语句中的 Explain Query Plan 使用：</font>

```sql
SQLite> EXPLAIN QUERY PLAN SELECT * FROM COMPANY WHERE Salary >= 20000;

order       from        detail
----------  ----------  -------------
0           0           TABLE COMPANY
```

