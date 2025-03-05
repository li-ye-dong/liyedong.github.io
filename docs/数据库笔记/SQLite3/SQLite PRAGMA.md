<font style="color:rgb(51, 51, 51);">SQLite PRAGMA命令是一个特殊的命令，用于控制SQLite环境中的各种环境变量和状态标志。PRAGMA值可以读取，也可以根据需要进行设置。</font>

### <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">要查询当前的PRAGMA值，只需提供编译指示的名称。</font>

```sql
PRAGMA pragma_name;
```

<font style="color:rgb(51, 51, 51);">要为PRAGMA设置新值，请使用以下语法。</font>

```sql
PRAGMA pragma_name = value;
```

<font style="color:rgb(51, 51, 51);">设置模式可以是名称，也可以是等效的整数，但是返回的值始终是整数。</font>

## <font style="color:rgb(51, 51, 51);">auto_vacuum PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">auto_vacuum</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置自动真空模式。以下是简单的语法。</font>

```plain
PRAGMA [database.]auto_vacuum;
PRAGMA [database.]auto_vacuum = mode;
```

<font style="color:rgb(51, 51, 51);">以下何处</font>**<font style="color:rgb(51, 51, 51);">mode</font>**<font style="color:rgb(51, 51, 51);">可以-</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">PRAGMA值和说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">0 or NONE</font>**<br/><font style="color:rgb(51, 51, 51);">Auto-vacuum已禁用。这是默认模式，这意味着除非使用VACUUM命令手动对其进行清理，否则数据库文件的大小永远不会缩小。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">1 or FULL</font>**<br/><font style="color:rgb(51, 51, 51);">启用了Auto-vacuum并且它是全自动的，当从数据库中删除数据时，它允许数据库文件缩小。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">2 or INCREMENTAL</font>**<br/><font style="color:rgb(51, 51, 51);">Auto-vacuum已启用，但必须手动激活。在这种模式下，将保留参考数据，但是将空闲页面简单地放在空闲列表中。这些页面可以随时使用</font>**<font style="color:rgb(51, 51, 51);">incremental_vacuum pragma</font>**<font style="color:rgb(51, 51, 51);">。</font> |


## <font style="color:rgb(51, 51, 51);">cache_size Pragma</font>
**<font style="color:rgb(51, 51, 51);">cache_size</font>**<font style="color:rgb(51, 51, 51);">编译可以得到或暂时设置在内存中的页面缓存的最大尺寸。以下是简单的语法。</font>

```plain
PRAGMA [database.]cache_size;
PRAGMA [database.]cache_size = pages;
```

**<font style="color:rgb(51, 51, 51);">pages</font>**<font style="color:rgb(51, 51, 51);">值表示高速缓存中的页面数。内置页面缓存的默认大小为2,000页，最小大小为10页。</font>

## <font style="color:rgb(51, 51, 51);">case_sensitive_like Pragma</font>
**<font style="color:rgb(51, 51, 51);">case_sensitive_like</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">pragma控制内置LIKE表达式的大小写敏感。默认情况下，此pragma为false，这意味着内置的LIKE运算符忽略字母大小写。下面是简单的语法。  
</font>

```sql
PRAGMA case_sensitive_like = [true|false];
```

<font style="color:rgb(51, 51, 51);">无法查询此编译指示的当前状态。</font>

## <font style="color:rgb(51, 51, 51);">count_changes Pragma</font>
**<font style="color:rgb(51, 51, 51);">count_changes</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">pragma获取或设置数据操作语句（例如INSERT，UPDATE和DELETE）的返回值。以下是简单的语法。</font>

```plain
PRAGMA count_changes;
PRAGMA count_changes = [true|false];
```

<font style="color:rgb(51, 51, 51);">默认情况下，此编译指示为false，并且这些语句不返回任何内容。如果设置为true，则每个提及的语句将返回一个单列单行表，该表由单个整数值组成，该整数值指示该操作所影响的行。</font>

## <font style="color:rgb(51, 51, 51);">database_list Pragma</font>
**<font style="color:rgb(51, 51, 51);">database_list</font>**<font style="color:rgb(51, 51, 51);">实用程序将用于列出所有附加数据库。以下是简单的语法。</font>

```sql
PRAGMA database_list;
```

<font style="color:rgb(51, 51, 51);">该实用程序将返回一个三列的表，每个打开或连接的数据库都有一行，给出数据库序列号，其名称和关联的文件。</font>

## <font style="color:rgb(51, 51, 51);">encoding Pragma</font>
**<font style="color:rgb(51, 51, 51);">encoding</font>****<font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">pragma控制字符串是如何编码，并存储在数据库中的文件。以下是简单的语法。</font>

```plain
PRAGMA encoding;
PRAGMA encoding = format;
```

<font style="color:rgb(51, 51, 51);">格式值可以是</font>**<font style="color:rgb(51, 51, 51);">UTF-8, UTF-16le</font>**<font style="color:rgb(51, 51, 51);">或</font>**<font style="color:rgb(51, 51, 51);">UTF-16be</font>**<font style="color:rgb(51, 51, 51);">之一。</font>

## <font style="color:rgb(51, 51, 51);">freelist_count Pragma</font>
**<font style="color:rgb(51, 51, 51);">freelist_count</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">Pragma返回一个整数，表示许多数据库页当前如何标记为空闲和可用的。以下是简单的语法。</font>

```sql
PRAGMA [database.]freelist_count;
```

<font style="color:rgb(51, 51, 51);">格式值可以是</font>**<font style="color:rgb(51, 51, 51);">UTF-8, UTF-16le或</font>****<font style="color:rgb(51, 51, 51);">UTF-16be</font>**<font style="color:rgb(51, 51, 51);">之一。</font>

## <font style="color:rgb(51, 51, 51);">index_info Pragma</font>
**<font style="color:rgb(51, 51, 51);">index_info</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">Pragma返回有关数据库索引的信息。以下是简单的语法。</font>

```sql
PRAGMA [database.]index_info( index_name );
```

<font style="color:rgb(51, 51, 51);">结果集将为索引中包含的每一列包含一行，以给出列顺序，表中包含列索引和列名。</font>

## <font style="color:rgb(51, 51, 51);">index_list Pragma</font>
**<font style="color:rgb(51, 51, 51);">index_list</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">Pragma列出与表关联的所有索引。以下是简单的语法。</font>

```sql
PRAGMA [database.]index_list( table_name );
```

<font style="color:rgb(51, 51, 51);">结果集将为每个索引包含一行，从而提供索引序列，索引名称和指示索引是否唯一的标志。</font>

## <font style="color:rgb(51, 51, 51);">journal_mode Pragma</font>
**<font style="color:rgb(51, 51, 51);">journal_mode</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">Pragma获取或设置控制日志文件如何存储和处理的日志模式。以下是简单的语法。</font>

```plain
PRAGMA journal_mode;
PRAGMA journal_mode = mode;
PRAGMA database.journal_mode;
PRAGMA database.journal_mode = mode;
```

<font style="color:rgb(51, 51, 51);">下表列出了五种受支持的日记模式。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">Pragma 值和说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">DELETE</font>**<br/><font style="color:rgb(51, 51, 51);">这是默认模式。在交易结束时，日记文件被删除。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">TRUNCATE</font>**<br/><font style="color:rgb(51, 51, 51);">日志文件被截断为零字节的长度。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">PERSIST</font>**<br/><font style="color:rgb(51, 51, 51);">日记文件保留在原处，但是标题被覆盖以指示日记不再有效。</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | **<font style="color:rgb(51, 51, 51);">MEMORY</font>**<br/><font style="color:rgb(51, 51, 51);">日记记录保存在内存中，而不是磁盘上。</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | **<font style="color:rgb(51, 51, 51);">OFF</font>**<br/><font style="color:rgb(51, 51, 51);">不保留日记记录。</font> |


## <font style="color:rgb(51, 51, 51);">max_page_count PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">max_page_count</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置允许的最大页数为数据库。以下是简单的语法。</font>

```plain
PRAGMA [database.]max_page_count;
PRAGMA [database.]max_page_count = max_page;
```

<font style="color:rgb(51, 51, 51);">默认值为1,073,741,823，即一个千兆页，这意味着，如果默认为1 KB页面大小，则数据库可以增长到1 TB。</font>

## <font style="color:rgb(51, 51, 51);">page_count PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">page_count</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA返回的数据库的当前页数。以下是简单的语法-</font>

PRAGMA [database.]page_count;

<font style="color:rgb(51, 51, 51);">数据库文件的大小应为page_count * page_size。</font>

## <font style="color:rgb(51, 51, 51);">page_size PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">page_size</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置数据库页面的大小。以下是简单的语法。</font>

```plain
PRAGMA [database.]page_size;
PRAGMA [database.]page_size = bytes;
```

<font style="color:rgb(51, 51, 51);">默认情况下，允许的大小为512、1024、2048、4096、8192、16384和32768字节。更改现有数据库上页面大小的唯一方法是设置页面大小，然后立即对数据库进行VACUUM。</font>

## <font style="color:rgb(51, 51, 51);">parser_trace PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">parser_trace</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA指示控制打印调试状态，因为它解析SQL命令。以下是简单的语法。</font>

PRAGMA parser_trace = [true|false];

<font style="color:rgb(51, 51, 51);">默认情况下，它设置为false，但是当通过将其设置为true启用时，SQL解析器将在解析SQL命令时打印其状态。</font>

## <font style="color:rgb(51, 51, 51);">recursive_triggers PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">recursive_triggers</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置递归触发功能。如果未启用递归触发器，则触发器操作将不会触发另一个触发器。以下是简单的语法。</font>

```plain
PRAGMA recursive_triggers;
PRAGMA recursive_triggers = [true|false];
```

## <font style="color:rgb(51, 51, 51);">schema_version PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">schema_version</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置存储在数据库头架构版本值。以下是简单的语法。</font>

```plain
PRAGMA [database.]schema_version;
PRAGMA [database.]schema_version = number;
```

<font style="color:rgb(51, 51, 51);">这是一个32位带符号整数值，用于跟踪架构更改。每当执行更改模式的命令（例如CREATE ...或DROP ...）时，此值都会增加。</font>

## <font style="color:rgb(51, 51, 51);">secure_delete PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">secure_delete</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA用于控制如何将内容从数据库中删除。以下是简单的语法。</font>

```plain
PRAGMA secure_delete;
PRAGMA secure_delete = [true|false];
PRAGMA database.secure_delete;
PRAGMA database.secure_delete = [true|false];
```

<font style="color:rgb(51, 51, 51);">安全删除标志的默认值通常为off，但是可以使用SQLITE_SECURE_DELETE构建选项更改该默认值。</font>

## <font style="color:rgb(51, 51, 51);">sql_trace PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">sql_trace</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA用于转储SQL跟踪结果到屏幕上。以下是简单的语法。</font>

```plain
PRAGMA sql_trace;
PRAGMA sql_trace = [true|false];
```

<font style="color:rgb(51, 51, 51);">必须使用SQLITE_DEBUG指令编译SQLite，才能包含此编译指示。</font>

## <font style="color:rgb(51, 51, 51);">synchronous PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">synchronous</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置当前磁盘同步模式，控制如何积极的SQLite将一路写数据到物理存储。以下是简单的语法。</font>

```plain
PRAGMA [database.]synchronous;
PRAGMA [database.]synchronous = mode;
```

<font style="color:rgb(51, 51, 51);">SQLite支持下表中列出的以下同步模式。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">Pragma 值和说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">0 or OFF</font>**<br/><font style="color:rgb(51, 51, 51);">完全没有同步</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">1 or NORMAL</font>**<br/><font style="color:rgb(51, 51, 51);">在每个关键磁盘操作序列之后进行同步</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">2 or FULL</font>**<br/><font style="color:rgb(51, 51, 51);">每次关键磁盘操作后同步</font> |


## <font style="color:rgb(51, 51, 51);">temp_store PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">temp_store</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置临时数据库文件所使用的存储模式。以下是简单的语法。</font>

```plain
PRAGMA temp_store;
PRAGMA temp_store = mode;
```

<font style="color:rgb(51, 51, 51);">SQLite支持以下存储模式。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">Pragma 值和说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">0 or DEFAULT</font>**<br/><font style="color:rgb(51, 51, 51);">使用编译时默认值。通常是FILE。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">1 or FILE</font>**<br/><font style="color:rgb(51, 51, 51);">使用基于文件的存储。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">2 or MEMORY</font>**<br/><font style="color:rgb(51, 51, 51);">使用基于内存的存储。</font> |


## <font style="color:rgb(51, 51, 51);">temp_store_directory PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">temp_store_directory</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">PRAGMA获取或设置用于临时数据库文件的位置。以下是简单的语法。</font>

```plain
PRAGMA temp_store_directory;
PRAGMA temp_store_directory = 'directory_path';
```

## <font style="color:rgb(51, 51, 51);">user_version PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">user_version</font>**<font style="color:rgb(51, 51, 51);">编译指示获取或设置存储在数据库头中的用户定义的版本值。以下是简单的语法。</font>

```plain
PRAGMA [database.]user_version;
PRAGMA [database.]user_version = number;
```

<font style="color:rgb(51, 51, 51);">这是一个32位带符号整数值，开发人员可以出于版本跟踪目的设置该值。</font>

## <font style="color:rgb(51, 51, 51);">writable_schema PRAGMA</font>
**<font style="color:rgb(51, 51, 51);">writable_schema</font>**<font style="color:rgb(51, 51, 51);">编译获取或设置修改系统表的能力。以下是简单的语法。</font>

```plain
PRAGMA writable_schema;
PRAGMA writable_schema = [true|false];
```

<font style="color:rgb(51, 51, 51);">如果设置了此编译指示，则可以创建和修改以sqlite_开头的表，包括sqlite_master表。使用编译指示时请小心，因为它可能导致数据库完全损坏。</font>

