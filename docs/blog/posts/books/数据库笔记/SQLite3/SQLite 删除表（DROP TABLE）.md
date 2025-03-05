<font style="color:rgb(51, 51, 51);">SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> DROP TABLE</font>**`<font style="color:rgb(51, 51, 51);">语句用于删除表定义以及该表的所有关联数据，索引，触发器，约束和权限规范。</font>

<font style="color:rgb(51, 51, 51);">使用此命令时必须小心，因为一旦删除了表，那么表中所有可用的信息也将永远丢失。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是DROP TABLE语句的基本语法。您可以选择指定数据库名称以及表名称，如下所示：</font>

DROP TABLE database_name.table_name;

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">让我们首先验证COMPANY表，然后将其从数据库中删除。</font>

```sql
sqlite>.tables
COMPANY       test.COMPANY
```

<font style="color:rgb(51, 51, 51);">这意味着COMPANY表在数据库中可用，因此让我们如下删除它-</font>

```sql
sqlite>DROP TABLE COMPANY;
sqlite>
```

<font style="color:rgb(51, 51, 51);">现在，如果您尝试使用.TABLES命令，那么您将不再找到COMPANY表。</font>

```sql
sqlite>.tables
sqlite>
```

<font style="color:rgb(51, 51, 51);">它什么也没有显示，这意味着已成功删除数据库中的表。</font>

