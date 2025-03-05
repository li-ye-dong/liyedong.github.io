<font style="color:rgb(51, 51, 51);">VACUUM 命令通过复制主数据库中的内容到一个临时数据库文件，然后清空主数据库，并从副本中重新载入原始的数据库文件。这消除了空闲页，把表中的数据排列为连续的，另外会清理数据库文件结构。</font>

<font style="color:rgb(51, 51, 51);">如果表中没有明确的整型主键（INTEGER PRIMARY KEY），VACUUM 命令可能会改变表中条目的行 ID(ROWID)。VACUUM 命令只适用于主数据库，附加的数据库文件是不可能使用 VACUUM 命令。</font>

<font style="color:rgb(51, 51, 51);">如果有一个活动的事务，VACUUM 命令就会失败。VACUUM 命令是一个用于内存数据库的任何操作。由于 VACUUM 命令从头开始重新创建数据库文件，所以 VACUUM 也可以用于修改许多数据库特定的配置参数。</font>

## <font style="color:rgb(51, 51, 51);">手动 Vacuum</font>
<font style="color:rgb(51, 51, 51);">以下是从命令提示符为整个数据库发出VACUUM命令的简单语法-</font>

```sql
$sqlite3 database_name "VACUUM;"
```

<font style="color:rgb(51, 51, 51);">您可以从SQLite提示符运行VACUUM，如下所示-</font>

```sql
sqlite> VACUUM;
```

<font style="color:rgb(51, 51, 51);">您还可以在特定表上运行VACUUM，如下所示-</font>

```sql
sqlite> VACUUM table_name;
```

## <font style="color:rgb(51, 51, 51);">自动 Vacuum(Auto-VACUUM)</font>
<font style="color:rgb(51, 51, 51);">SQLite 的 Auto-VACUUM 与 VACUUM 不大一样，它只是把空闲页移到数据库末尾，从而减小数据库大小。通过这样做，它可以明显地把数据库碎片化，而 VACUUM 则是反碎片化。所以 Auto-VACUUM 只会让数据库更小。</font>

<font style="color:rgb(51, 51, 51);">在 SQLite 提示符中，您可以通过下面的编译运行，启用/禁用 SQLite 的 Auto-VACUUM：</font>

```sql
sqlite> PRAGMA auto_vacuum = NONE; -- 0 means disable auto vacuum
sqlite> PRAGMA auto_vacuum = FULL; -- 1 means enable full auto vacuum
sqlite> PRAGMA auto_vacuum = INCREMENTAL; -- 2 means enable incremental vacuum
```

<font style="color:rgb(51, 51, 51);">您可以从命令提示符处运行以下命令以检查Vacuum设置-</font>

```sql
$sqlite3 database_name "PRAGMA auto_vacuum;"
```

<font style="color:rgb(133, 144, 166);background-color:rgb(251, 251, 251);">  
</font>

