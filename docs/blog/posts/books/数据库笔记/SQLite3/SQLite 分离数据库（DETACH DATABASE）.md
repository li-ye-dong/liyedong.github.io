<font style="color:rgb(51, 51, 51);">SQLite DETACH DATABASE语句用于将命名数据库与以前使用ATTACH语句附加的数据库连接分离和取消关联。如果同一个数据库文件附加了多个别名，则DETACH命令将仅断开给定名称的连接，其余附件仍将继续。您不能分离</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">main</font>**`<font style="color:rgb(51, 51, 51);">或</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">temp</font>**`<font style="color:rgb(51, 51, 51);">数据库。  
</font>

<font style="color:rgb(51, 51, 51);">如果该数据库是内存数据库或临时数据库，则该数据库将被破坏并且内容将丢失。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是SQLite DETACH DATABASE 'Alias-Name' 语句的基本语法。</font>

```sql
DETACH DATABASE 'Alias-Name';
```

<font style="color:rgb(51, 51, 51);">在这里，“Alias-Name”是您使用ATTACH语句附加数据库时使用的别名。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">假设您有一个数据库，您在上一章中创建了该数据库，并在数据库中附加了“ test”和“ currentDB”，我们可以使用</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.database命令</font>**`<font style="color:rgb(51, 51, 51);">看到它。</font>

```plain
sqlite>.databases
seq  name             file
---  ---------------  ----------------------
0    main             /home/sqlite/testDB.db
2    test             /home/sqlite/testDB.db
3    currentDB        /home/sqlite/testDB.db
```

<font style="color:rgb(51, 51, 51);">让我们尝试使用以下命令从testDB.db分离“ currentDB”。</font>

```sql
sqlite> DETACH DATABASE 'currentDB';
```

<font style="color:rgb(51, 51, 51);">现在，如果您要检查当前附件，则会发现testDB.db仍与“ test”和“ main”连接。</font>

```plain
sqlite>.databases
seq  name             file
---  ---------------  ----------------------
0    main             /home/sqlite/testDB.db
2    test             /home/sqlite/testDB.db
```

