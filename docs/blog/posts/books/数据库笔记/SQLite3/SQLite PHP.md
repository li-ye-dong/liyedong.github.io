## <font style="color:rgb(51, 51, 51);">安装</font>
<font style="color:rgb(51, 51, 51);">自 PHP 5.3.0 起默认启用 SQLite3 扩展。可以在编译时使用</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">--without-sqlite3</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">禁用 SQLite3 扩展。</font>

<font style="color:rgb(51, 51, 51);">Windows 用户必须启用 php_sqlite3.dll 才能使用该扩展。自 PHP 5.3.0 起，这个 DLL 被包含在 PHP 的 Windows 分发版中。</font>

<font style="color:rgb(51, 51, 51);">如需了解详细的安装指导，建议查看我们的 PHP 教程和它的官方网站。</font>

## <font style="color:rgb(51, 51, 51);">PHP 接口 API</font>
<font style="color:rgb(51, 51, 51);">以下是重要的 PHP 程序，可以满足您在 PHP 程序中使用 SQLite 数据库的需求。如果您需要了解更多细节，请查看 PHP 官方文档。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">API & 描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">public void SQLite3::open ( filename, flags, encryption_key )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">打开一个 SQLite 3 数据库。如果构建包括加密，那么它将尝试使用的密钥。</font><br/><font style="color:rgb(51, 51, 51);">如果文件名</font><font style="color:rgb(51, 51, 51);"> </font>_<font style="color:rgb(51, 51, 51);">filename</font>_<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">赋值为</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">':memory:'</font>**<font style="color:rgb(51, 51, 51);">，那么 SQLite3::open() 将会在 RAM 中创建一个内存数据库，这只会在 session 的有效时间内持续。</font><br/><font style="color:rgb(51, 51, 51);">如果文件名 filename 为实际的设备文件名称，那么 SQLite3::open() 将使用这个参数值尝试打开数据库文件。如果该名称的文件不存在，那么将创建一个新的命名为该名称的数据库文件。</font><br/><font style="color:rgb(51, 51, 51);">可选的 flags 用于判断是否打开 SQLite 数据库。默认情况下，当使用 SQLITE3_OPEN_READWRITE | SQLITE3_OPEN_CREATE 时打开。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">public bool SQLite3::exec ( string $query )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">该例程提供了一个执行 SQL 命令的快捷方式，SQL 命令由 sql 参数提供，可以由多个 SQL 命令组成。该程序用于对给定的数据库执行一个无结果的查询。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">public SQLite3Result SQLite3::query ( string $query )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">该例程执行一个 SQL 查询，如果查询到返回结果则返回一个</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">SQLite3Result</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">对象。</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | **<font style="color:rgb(51, 51, 51);">public int SQLite3::lastErrorCode ( void )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">该例程返回最近一次失败的 SQLite 请求的数值结果代码。</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | **<font style="color:rgb(51, 51, 51);">public string SQLite3::lastErrorMsg ( void )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">该例程返回最近一次失败的 SQLite 请求的英语文本描述。</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | **<font style="color:rgb(51, 51, 51);">public int SQLite3::changes ( void )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">该例程返回最近一次的 SQL 语句更新或插入或删除的数据库行数。</font> |
| <font style="color:rgb(51, 51, 51);">7</font> | **<font style="color:rgb(51, 51, 51);">public bool SQLite3::close ( void )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">该例程关闭之前调用 SQLite3::open() 打开的数据库连接。</font> |
| <font style="color:rgb(51, 51, 51);">8</font> | **<font style="color:rgb(51, 51, 51);">public string SQLite3::escapeString ( string $value )</font>**<font style="color:rgb(51, 51, 51);">   </font><br/><font style="color:rgb(51, 51, 51);">该例程返回一个字符串，在 SQL 语句中，出于安全考虑，该字符串已被正确地转义。</font> |


## <font style="color:rgb(51, 51, 51);">连接数据库</font>
<font style="color:rgb(51, 51, 51);">下面的 PHP 代码显示了如何连接到一个现有的数据库。如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象。</font>

```php
<?php
  class MyDB extends SQLite3
  {
  function __construct()
  {
    $this->open('test.db');
  }
  }
  $db = new MyDB();
if(!$db){
  echo $db->lastErrorMsg();
} else {
  echo "Opened database successfully\n";
}
?>
```

<font style="color:rgb(51, 51, 51);">现在，让我们来运行上面的程序，在当前目录中创建我们的数据库</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">test.db</font>**<font style="color:rgb(51, 51, 51);">。您可以根据需要改变路径。如果数据库成功创建，那么会显示下面所示的消息：</font>

```php
Open database successfully
```

## <font style="color:rgb(51, 51, 51);">创建表</font>
<font style="color:rgb(51, 51, 51);">下面的 PHP 代码段将用于在先前创建的数据库中创建一个表：</font>

```php
<?php
  class MyDB extends SQLite3
  {
  function __construct()
  {
    $this->open('test.db');
  }
  }
  $db = new MyDB();
if(!$db){
  echo $db->lastErrorMsg();
} else {
  echo "Opened database successfully\n";
}
$sql =<<<EOF
  CREATE TABLE COMPANY
  (ID INT PRIMARY KEY     NOT NULL,
  NAME           TEXT    NOT NULL,
  AGE            INT     NOT NULL,
  ADDRESS        CHAR(50),
  SALARY         REAL);
  EOF;
$ret = $db->exec($sql);
if(!$ret){
  echo $db->lastErrorMsg();
} else {
  echo "Table created successfully\n";
}
$db->close();
?>
```

<font style="color:rgb(51, 51, 51);">上述程序执行时，它会在</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">test.db</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">中创建 COMPANY 表，并显示下面所示的消息：</font>

```php
Opened database successfully
  Table created successfully
```

## <font style="color:rgb(51, 51, 51);">INSERT 操作</font>
<font style="color:rgb(51, 51, 51);">下面的 PHP 程序显示了如何在上面创建的 COMPANY 表中创建记录：</font>

```php
<?php
  class MyDB extends SQLite3
  {
  function __construct()
  {
    $this->open('test.db');
  }
  }
  $db = new MyDB();
if(!$db){
  echo $db->lastErrorMsg();
} else {
  echo "Opened database successfully\n";
}
$sql =<<<EOF
  INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
  VALUES (1, 'Paul', 32, 'California', 20000.00 );
  INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
  VALUES (2, 'Allen', 25, 'Texas', 15000.00 );
  INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
  VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );
  INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
  VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );
  EOF;
$ret = $db->exec($sql);
if(!$ret){
  echo $db->lastErrorMsg();
} else {
  echo "Records created successfully\n";
}
$db->close();
?>
```

<font style="color:rgb(51, 51, 51);">上述程序执行时，它会在 COMPANY 表中创建给定记录，并会显示以下两行：</font>

```php
Opened database successfully
  Records created successfully
```

## <font style="color:rgb(51, 51, 51);">SELECT 操作</font>
<font style="color:rgb(51, 51, 51);">下面的 PHP 程序显示了如何从前面创建的 COMPANY 表中获取并显示记录：</font>

```php
<?php
  class MyDB extends SQLite3
  {
  function __construct()
  {
    $this->open('test.db');
  }
  }
  $db = new MyDB();
if(!$db){
  echo $db->lastErrorMsg();
} else {
  echo "Opened database successfully\n";
}
$sql =<<<EOF
  SELECT * from COMPANY;
  EOF;
$ret = $db->query($sql);
while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
  echo "ID = ". $row['ID'] . "\n";
  echo "NAME = ". $row['NAME'] ."\n";
  echo "ADDRESS = ". $row['ADDRESS'] ."\n";
  echo "SALARY =  ".$row['SALARY'] ."\n\n";
}
echo "Operation done successfully\n";
$db->close();
?>
```

<font style="color:rgb(51, 51, 51);">上述程序执行时，它会产生以下结果：</font>

```php
Opened database successfully
  ID = 1
  NAME = Paul
    ADDRESS = California
      SALARY =  20000
      ID = 2
        NAME = Allen
        ADDRESS = Texas
        SALARY =  15000
        ID = 3
        NAME = Teddy
          ADDRESS = Norway
            SALARY =  20000
            ID = 4
              NAME = Mark
              ADDRESS = Rich-Mond
              SALARY =  65000
              Operation done successfully
```

## <font style="color:rgb(51, 51, 51);">UPDATE 操作</font>
<font style="color:rgb(51, 51, 51);">下面的 PHP 代码显示了如何使用 UPDATE 语句来更新任何记录，然后从 COMPANY 表中获取并显示更新的记录：</font>

```php
<?php
  class MyDB extends SQLite3
  {
  function __construct()
  {
    $this->open('test.db');
  }
  }
  $db = new MyDB();
if(!$db){
  echo $db->lastErrorMsg();
} else {
  echo "Opened database successfully\n";
}
$sql =<<<EOF
  UPDATE COMPANY set SALARY = 25000.00 where ID=1;
  EOF;
$ret = $db->exec($sql);
if(!$ret){
  echo $db->lastErrorMsg();
} else {
  echo $db->changes(), " Record updated successfully\n";
}
$sql =<<<EOF
  SELECT * from COMPANY;
  EOF;
$ret = $db->query($sql);
while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
  echo "ID = ". $row['ID'] . "\n";
  echo "NAME = ". $row['NAME'] ."\n";
  echo "ADDRESS = ". $row['ADDRESS'] ."\n";
  echo "SALARY =  ".$row['SALARY'] ."\n\n";
}
echo "Operation done successfully\n";
$db->close();
?>
```

<font style="color:rgb(51, 51, 51);">上述程序执行时，它会产生以下结果：</font>

```php
Opened database successfully
  1 Record updated successfully
    ID = 1
    NAME = Paul
      ADDRESS = California
        SALARY =  25000
        ID = 2
          NAME = Allen
          ADDRESS = Texas
          SALARY =  15000
          ID = 3
          NAME = Teddy
            ADDRESS = Norway
              SALARY =  20000
                ID = 4
                NAME = Mark
                  ADDRESS = Rich-Mond
                    SALARY =  65000
                    Operation done successfully
```

## <font style="color:rgb(51, 51, 51);">DELETE 操作</font>
<font style="color:rgb(51, 51, 51);">下面的 PHP 代码显示了如何使用 DELETE 语句删除任何记录，然后从 COMPANY 表中获取并显示剩余的记录：</font>

```php
<?php
  class MyDB extends SQLite3
  {
  function __construct()
  {
    $this->open('test.db');
  }
  }
  $db = new MyDB();
if(!$db){
  echo $db->lastErrorMsg();
} else {
  echo "Opened database successfully\n";
}
$sql =<<<EOF
  DELETE from COMPANY where ID=2;
  EOF;
$ret = $db->exec($sql);
if(!$ret){
  echo $db->lastErrorMsg();
} else {
  echo $db->changes(), " Record deleted successfully\n";
}
$sql =<<<EOF
  SELECT * from COMPANY;
  EOF;
$ret = $db->query($sql);
while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
  echo "ID = ". $row['ID'] . "\n";
  echo "NAME = ". $row['NAME'] ."\n";
  echo "ADDRESS = ". $row['ADDRESS'] ."\n";
  echo "SALARY =  ".$row['SALARY'] ."\n\n";
}
echo "Operation done successfully\n";
$db->close();
?>
```

<font style="color:rgb(51, 51, 51);">上述程序执行时，它会产生以下结果：</font>

```php
Opened database successfully
  1 Record deleted successfully
    ID = 1
    NAME = Paul
      ADDRESS = California
        SALARY =  25000
        ID = 3
          NAME = Teddy
          ADDRESS = Norway
          SALARY =  20000
          ID = 4
          NAME = Mark
            ADDRESS = Rich-Mond
              SALARY =  65000
              Operation done successfully
```

