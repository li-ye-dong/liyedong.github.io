<font style="color:rgb(51, 51, 51);">考虑一种情况，当您有多个可用数据库并且想一次使用其中任何一个数据库时。SQLite </font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">ATTACH DATABASE</font>**`<font style="color:rgb(51, 51, 51);">语句用于选择特定的数据库，执行此命令后，所有SQLite语句将在附加数据库下执行。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是SQLite ATTACH DATABASE语句的基本语法。</font>

```sql
ATTACH DATABASE 'DatabaseName' As 'Alias-Name';
```

<font style="color:rgb(51, 51, 51);">如果尚未创建数据库，上述命令还将创建一个数据库，否则它将仅将数据库文件名附加到逻辑数据库“别名”。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">如果要附加现有数据库</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">testDB.db</font>**`<font style="color:rgb(51, 51, 51);">，则ATTACH DATABASE语句如下-</font>

```python
sqlite> ATTACH DATABASE 'testDB.db' as 'TEST';
```

<font style="color:rgb(51, 51, 51);">使用SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.database</font>**`<font style="color:rgb(51, 51, 51);">命令显示附加的数据库。</font>

```plain
sqlite> .database
seq  name             file
---  ---------------  ----------------------
0    main             /home/sqlite/testDB.db
2    test             /home/sqlite/testDB.db
```

<font style="color:rgb(51, 51, 51);">数据库名称main和temp是为主数据库和保留临时表和其他临时数据对象的数据库保留的。 这两个数据库名称对于每个数据库连接都存在，并且不应用于附件，否则您将收到以下警告消息。</font>

```plain
sqlite> ATTACH DATABASE 'testDB.db' as 'TEMP';
Error: database TEMP is already in use
sqlite> ATTACH DATABASE 'testDB.db' as 'main';
Error: database TEMP is already in use
```

