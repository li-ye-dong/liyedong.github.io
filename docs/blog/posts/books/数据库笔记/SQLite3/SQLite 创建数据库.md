<font style="color:rgb(51, 51, 51);">在SQLite中，</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">sqlite3</font>**`<font style="color:rgb(51, 51, 51);">命令用于创建新的SQLite数据库。您无需具有任何特殊特权即可创建数据库。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是sqlite3命令创建数据库的基本语法：-</font>

```python
$sqlite3 DatabaseName.db
```

<font style="color:rgb(51, 51, 51);">始终，数据库名称在RDBMS中应该是唯一的。</font>

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">如果要创建新数据库<testDB.db>，则SQLITE3语句如下-</font>

```plain
$sqlite3 testDB.db
SQLite version 3.7.15.2 2013-01-09 11:53:05
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

<font style="color:rgb(51, 51, 51);">上面的命令将</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">testDB.db</font>**`<font style="color:rgb(51, 51, 51);">在当前目录中创建一个文件。该文件将被SQLite引擎用作数据库。如果在创建数据库时注意到了，sqlite3命令将</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">sqlite></font>**`<font style="color:rgb(51, 51, 51);">在成功创建数据库文件后提供提示。</font>

<font style="color:rgb(51, 51, 51);">创建数据库后，您可以使用以下SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.databases</font>****<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> </font>**`<font style="color:rgb(51, 51, 51);">命令在数据库列表中对其进行验证。</font>

```plain
sqlite>.databases
seq  name             file
---  ---------------  ----------------------
0    main             /home/sqlite/testDB.db
```

<font style="color:rgb(51, 51, 51);">您将使用SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.quit</font>**`<font style="color:rgb(51, 51, 51);">命令从sqlite提示符出来，如下所示-</font>

```python
sqlite>.quit$
```

## <font style="color:rgb(51, 51, 51);">.dump命令</font>
<font style="color:rgb(51, 51, 51);">可以使用.dump dot命令在命令提示符下使用以下SQLite命令将完整的数据库导出到文本文件中。</font>

```python
$sqlite3 testDB.db .dump > testDB.sql
```

<font style="color:rgb(51, 51, 51);">上面的命令会将</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">testDB.db</font>**`<font style="color:rgb(51, 51, 51);">数据库的全部内容转换为SQLite语句，并将其转储为ASCII文本文件</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">testDB.sql</font>**`<font style="color:rgb(51, 51, 51);">。您可以通过以下简单方式从生成的testDB.sql执行恢复-</font>

```python
$sqlite3 testDB.db < testDB.sql
```

<font style="color:rgb(51, 51, 51);">目前您的数据库为空，因此一旦数据库中的表和数据很少，您可以尝试上述两个过程。现在，让我们继续下一章。</font>

