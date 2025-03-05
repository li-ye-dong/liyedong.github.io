<font style="color:rgb(51, 51, 51);">索引是特殊的查找表，数据库搜索引擎可以使用索引来加速数据检索。简而言之，an</font>**<font style="color:rgb(51, 51, 51);">index</font>**<font style="color:rgb(51, 51, 51);">是指向表中数据的指针。数据库中的索引与书后的索引非常相似。</font>

<font style="color:rgb(51, 51, 51);">例如，如果要引用一本书中讨论某个主题的所有页面，则首先要参考索引，该索引按字母顺序列出所有主题，然后引用一个或多个特定的页码。</font>

<font style="color:rgb(51, 51, 51);">索引有助于加快SELECT查询和WHERE子句的速度，但它会通过UPDATE和INSERT语句减慢数据输入速度。可以创建或删除索引，而不会影响数据。</font>

<font style="color:rgb(51, 51, 51);">创建索引涉及CREATE INDEX语句，该语句使您可以命名索引，指定表以及要索引的列或列，并指示索引是升序还是降序。</font>

<font style="color:rgb(51, 51, 51);">索引也可以是唯一的，类似于UNIQUE约束，因为索引可以防止存在索引的列或列组合中的重复条目。</font>

## <font style="color:rgb(51, 51, 51);">CREATE INDEX命令</font>
<font style="color:rgb(51, 51, 51);">以下是的基本语法</font>**<font style="color:rgb(51, 51, 51);">CREATE INDEX</font>**<font style="color:rgb(51, 51, 51);">。</font>

```sql
CREATE INDEX index_name ON table_name;
```

### <font style="color:rgb(51, 51, 51);">单列索引</font>
<font style="color:rgb(51, 51, 51);">单列索引是仅基于一个表列创建的索引。基本语法如下-</font>

```sql
CREATE INDEX index_nameON table_name (column_name);
```

### <font style="color:rgb(51, 51, 51);">唯一索引</font>
<font style="color:rgb(51, 51, 51);">唯一索引不仅用于提高性能，而且还用于数据完整性。唯一索引不允许将任何重复的值插入表中。基本语法如下-</font>

```sql
CREATE UNIQUE INDEX index_nameon table_name (column_name);
```

### <font style="color:rgb(51, 51, 51);">复合索引</font>
<font style="color:rgb(51, 51, 51);">复合索引是表的两个或多个列上的索引。基本语法如下-</font>

```sql
CREATE INDEX index_nameon table_name (column1, column2);
```

<font style="color:rgb(51, 51, 51);">无论是创建单列索引还是复合索引，都要考虑column(s)到您可能在查询的WHERE子句中非常频繁地使用它作为过滤条件。</font>

<font style="color:rgb(51, 51, 51);">如果只使用一列，则应选择单列索引。如果WHERE子句中经常使用两个或更多列作为过滤器，则复合索引将是最佳选择。</font>

### <font style="color:rgb(51, 51, 51);">隐式索引</font>
<font style="color:rgb(51, 51, 51);">隐式索引是创建对象时由数据库服务器自动创建的索引。自动为主键约束和唯一约束创建索引。</font>

**<font style="color:rgb(51, 51, 51);">Example</font>**

<font style="color:rgb(51, 51, 51);">以下是一个示例，我们将在COMPANY表中为薪水列创建索引-</font>

```sql
sqlite> CREATE INDEX salary_index ON COMPANY (salary);
```

<font style="color:rgb(51, 51, 51);">现在，让我们使用以下</font>**<font style="color:rgb(51, 51, 51);">.indices</font>**<font style="color:rgb(51, 51, 51);">命令列出COMPANY表中所有可用的索引：</font>

```sql
sqlite> .indices COMPANY
```

<font style="color:rgb(51, 51, 51);">这将产生以下结果，其中</font>_<font style="color:rgb(51, 51, 51);">sqlite_autoindex_COMPANY_1</font>_<font style="color:rgb(51, 51, 51);">是隐式索引，</font>_<font style="color:rgb(51, 51, 51);">该隐</font>_<font style="color:rgb(51, 51, 51);">式索引是在创建表本身时创建的。</font>

```sql
salary_indexsqlite_autoindex_COMPANY_1
```

<font style="color:rgb(51, 51, 51);">您可以列出所有索引数据库范围，如下所示：</font>

```sql
sqlite> SELECT * FROM sqlite_master WHERE type = 'index';
```

## <font style="color:rgb(51, 51, 51);">DROP INDEX命令</font>
<font style="color:rgb(51, 51, 51);">可以使用SQLite</font>**<font style="color:rgb(51, 51, 51);"> </font>****<font style="color:rgb(51, 51, 51);">DROP</font>**<font style="color:rgb(51, 51, 51);">命令删除索引。删除索引时应小心，因为性能可能会减慢或提高。</font>

<font style="color:rgb(51, 51, 51);">以下是基本语法如下-</font>

```sql
DROP INDEX index_name;
```

<font style="color:rgb(51, 51, 51);">您可以使用以下语句删除以前创建的索引。</font>

```sql
sqlite> DROP INDEX salary_index;
```

### <font style="color:rgb(51, 51, 51);">什么时候应该避免索引？</font>
<font style="color:rgb(51, 51, 51);">尽管索引旨在提高数据库的性能，但有时应避免使用它们。以下准则指示何时应重新考虑使用索引。</font>

<font style="color:rgb(51, 51, 51);">索引不得用于-</font>

+ <font style="color:rgb(51, 51, 51);">小表。</font>
+ <font style="color:rgb(51, 51, 51);">具有频繁，大量批处理更新或插入操作的表。</font>
+ <font style="color:rgb(51, 51, 51);">包含大量NULL值的列。</font>
+ <font style="color:rgb(51, 51, 51);">经常操作的列。</font>

