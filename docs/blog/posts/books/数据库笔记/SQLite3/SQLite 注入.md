<font style="color:rgb(51, 51, 51);">如果您的站点允许用户通过网页输入，并将输入内容插入到 SQLite 数据库中，这个时候您就面临着一个被称为 SQL 注入的安全问题。本章节将向您讲解如何防止这种情况的发生，确保脚本和 SQLite 语句的安全。</font>

<font style="color:rgb(51, 51, 51);">注入通常在请求用户输入时发生，比如需要用户输入姓名，但用户却输入了一个 SQLite 语句，而这语句就会在不知不觉中在数据库上运行。</font>

<font style="color:rgb(51, 51, 51);">永远不要相信用户提供的数据，所以只处理通过验证的数据，这项规则是通过模式匹配来完成的。在下面的实例中，用户名 username 被限制为字母数字字符或者下划线，长度必须在 8 到 20 个字符之间 - 请根据需要修改这些规则。</font>

```sql
if (preg_match("/^\w{8,20}$/", $_GET['username'], $matches)){
   $db = new SQLiteDatabase('filename');
   $result = @$db->query("SELECT * FROM users WHERE username = $matches[0]");} else {
   echo "username not accepted";}
```

<font style="color:rgb(51, 51, 51);">为了演示问题，请看以下摘录-</font>

```sql
$name = "Qadir'; 
DELETE FROM users;";@$db->query("SELECT * FROM users WHERE username = '{$name}'");
```

<font style="color:rgb(51, 51, 51);">函数调用是为了从用户表中检索 name 列与用户指定的名称相匹配的记录。正常情况下，</font>**<font style="color:rgb(51, 51, 51);">$name</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">只包含字母数字字符或者空格，比如字符串 ilia。但在这里，向 $name 追加了一个全新的查询，这个对数据库的调用将会造成灾难性的问题：注入的 DELETE 查询会删除 users 的所有记录。</font>

<font style="color:rgb(51, 51, 51);">虽然已经存在有不允许查询堆叠或在单个函数调用中执行多个查询的数据库接口，如果尝试堆叠查询，则会调用失败，但 SQLite 和 PostgreSQL 里仍进行堆叠查询，即执行在一个字符串中提供的所有查询，这会导致严重的安全问题。</font>

## <font style="color:rgb(51, 51, 51);">防止SQL注入</font>
<font style="color:rgb(51, 51, 51);">在脚本语言中，比如 PERL 和 PHP，您可以巧妙地处理所有的转义字符。编程语言 PHP 提供了字符串函数</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">SQLite3::escapeString($string)</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">sqlite_escape_string()</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">来转义对于 SQLite 来说比较特殊的输入字符。</font>

<font style="color:rgb(51, 51, 51);">注意：使用函数</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">sqlite_escape_string()</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">的 PHP 版本要求为</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">PHP 5 < 5.4.0</font>**<font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">更高版本 PHP 5 >= 5.3.0, PHP 7 使用以上函数:</font>

```sql
if (get_magic_quotes_gpc()) {
   $name = sqlite_escape_string($name);
}
$result = @$db->query("SELECT * FROM users WHERE username = '{$name}'");
```

<font style="color:rgb(51, 51, 51);">尽管编码使得插入数据变得安全，但是它会呈现简单的文本比较，在查询中，对于包含二进制数据的列，</font>**<font style="color:rgb(51, 51, 51);">LIKE</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">子句是不可用的。</font>

<font style="color:rgb(51, 51, 51);">请注意，addslashes() 不应该被用在 SQLite 查询中引用字符串，它会在检索数据时导致奇怪的结果。  
</font>

<font style="color:rgb(133, 144, 166);background-color:rgb(251, 251, 251);">  
</font>

