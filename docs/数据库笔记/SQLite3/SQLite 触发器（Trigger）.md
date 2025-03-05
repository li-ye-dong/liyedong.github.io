<font style="color:rgb(51, 51, 51);">SQLite触发器是数据库回调函数，当发生指定的数据库事件时，将自动执行/调用这些函数。 以下是有关SQLite触发器的要点-</font>

+ <font style="color:rgb(51, 51, 51);">SQLite 的触发器(Trigger)可以指定在特定的数据库表发生 DELETE、INSERT 或 UPDATE 时触发，或在一个或多个指定表的列发生更新时触发。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite 只支持 FOR EACH ROW 触发器(Trigger)，没有 FOR EACH STATEMENT 触发器(Trigger)。因此，明确指定 FOR EACH ROW 是可选的。</font>
+ <font style="color:rgb(51, 51, 51);">WHEN 子句和触发器(Trigger)动作可能访问使用表单</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">NEW.column-name</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">OLD.column-name</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">的引用插入、删除或更新的行元素，其中 column-name 是从与触发器关联的表的列的名称。</font>
+ <font style="color:rgb(51, 51, 51);">如果提供 WHEN 子句，则只针对 WHEN 子句为真的指定行执行 SQL 语句。如果没有提供 WHEN 子句，则针对所有行执行 SQL 语句。</font>
+ <font style="color:rgb(51, 51, 51);">BEFORE 或 AFTER 关键字决定何时执行触发器动作，决定是在关联行的插入、修改或删除之前或者之后执行触发器动作。</font>
+ <font style="color:rgb(51, 51, 51);">当触发器相关联的表删除时，自动删除触发器(Trigger)。</font>
+ <font style="color:rgb(51, 51, 51);">要修改的表必须存在于同一数据库中，作为触发器被附加的表或视图，且必须只使用</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">tablename</font>**<font style="color:rgb(51, 51, 51);">，而不是</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">database.tablename</font>**<font style="color:rgb(51, 51, 51);">。</font>
+ <font style="color:rgb(51, 51, 51);">一个特殊的 SQL 函数 RAISE() 可用于触发器程序内抛出异常。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是创建trigger的基本语法。</font>

```plain
CREATE  TRIGGER trigger_name [BEFORE|AFTER] event_name 
ON table_name
BEGIN
 -- 触发器逻辑....
END;
```

<font style="color:rgb(51, 51, 51);">在这里，</font>**<font style="color:rgb(51, 51, 51);">event_name</font>**<font style="color:rgb(51, 51, 51);">可以是对上述表的</font>_<font style="color:rgb(51, 51, 51);">INSERT，DELETE</font>_<font style="color:rgb(51, 51, 51);">和</font>_<font style="color:rgb(51, 51, 51);">UPDATE</font>_<font style="color:rgb(51, 51, 51);">数据库操作</font>**<font style="color:rgb(51, 51, 51);">table_name</font>**<font style="color:rgb(51, 51, 51);">。您可以选择在表名称后指定FOR EACH ROW。</font>

<font style="color:rgb(51, 51, 51);">以下是在表的一个或多个指定列上的UPDATE操作上创建触发器的语法。</font>

```plain
CREATE TRIGGER trigger_name [BEFORE|AFTER] UPDATE OF column_name 
ON table_name

BEGIN
   -- 触发逻辑在这里....
END;
```

### <font style="color:rgb(51, 51, 51);">示例</font>
<font style="color:rgb(51, 51, 51);">让我们考虑一种情况，我们希望对插入到COMPANY表中的每条记录进行审计试用，这是我们新创建的，如下所示（如果已经有了，则删除COMPANY表）。</font>

```plain
sqlite> CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

<font style="color:rgb(51, 51, 51);">为了保持审计试用状态，只要在COMPANY表中有新记录的条目，我们将创建一个名为AUDIT的新表，在该表中将插入日志消息。</font>

```plain
sqlite> CREATE TABLE AUDIT(
   EMP_ID INT NOT NULL,
   ENTRY_DATE TEXT NOT NULL
);
```

<font style="color:rgb(51, 51, 51);">在这里，ID是AUDIT记录ID，EMP_ID是来自COMPANY表的ID，DATE将在COMPANY表中创建记录时保留时间戳。现在让我们在COMPANY表上创建触发器，如下所示：</font>

```plain
sqlite> CREATE TRIGGER audit_log AFTER INSERT 
ON COMPANY
BEGIN
   INSERT INTO AUDIT(EMP_ID, ENTRY_DATE) VALUES (new.ID, datetime('now'));
END;
```

<font style="color:rgb(51, 51, 51);">现在，我们将开始实际的工作，让我们开始在COMPANY表中插入记录，这将导致在AUDIT表中创建审核日志记录。在COMPANY表中创建一条记录，如下所示-</font>

```plain
sqlite> INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (1, 'Paul', 32, 'California', 20000.00 );
```

<font style="color:rgb(51, 51, 51);">这将在COMPANY表中创建一条记录，如下所示-</font>

```plain
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
```

<font style="color:rgb(51, 51, 51);">同时，将在AUDIT表中创建一条记录。该记录是触发器的结果，该触发器是我们在COMPANY表中的INSERT操作上创建的。同样，您可以根据需要在UPDATE和DELETE操作上创建触发器。</font>

```plain
EMP_ID      ENTRY_DATE
----------  -------------------
1           2013-04-05 06:26:00
```

## <font style="color:rgb(51, 51, 51);">列出触发器</font>
<font style="color:rgb(51, 51, 51);">您可以从</font>**<font style="color:rgb(51, 51, 51);">sqlite_master</font>**<font style="color:rgb(51, 51, 51);">表中列出所有触发器，如下所示：</font>

```plain
sqlite> SELECT name FROM sqlite_master
WHERE type = 'trigger';
```

<font style="color:rgb(51, 51, 51);">上面的SQLite语句将仅列出一个条目，如下所示-</font>

```plain
name
----------
audit_log
```

<font style="color:rgb(51, 51, 51);">如果要列出特定表上的触发器，请使用AND子句和表名，如下所示：</font>

```plain
sqlite> SELECT name FROM sqlite_master
WHERE type = 'trigger' AND tbl_name = 'COMPANY';
```

<font style="color:rgb(51, 51, 51);">上面的SQLite语句还将仅列出一个条目，如下所示-</font>

```plain
name
----------
audit_log
```

## <font style="color:rgb(51, 51, 51);">删除触发器</font>
<font style="color:rgb(51, 51, 51);">以下是DROP命令，可用于删除现有触发器。</font>

sqlite> DROP TRIGGER trigger_name;

