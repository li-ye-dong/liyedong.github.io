<font style="color:rgb(51, 51, 51);">本章可帮助您了解什么是SQLite，它与SQL有何不同，为什么需要它以及它处理应用程序数据库的方式。</font>

<font style="color:rgb(51, 51, 51);">SQLite是一个软件库，它实现了一个自包含、无服务器、零配置、事务性SQL数据库引擎。SQLite是目前增长最快的数据库引擎之一，但这是受欢迎程度的增长，与它的规模无关。SQLite的源代码在公共域中。</font>

## <font style="color:rgb(51, 51, 51);">什么是SQLite？</font>
<font style="color:rgb(51, 51, 51);">SQLite是一个进程内库，可实现自包含的，无服务器的，零配置的事务型SQL数据库引擎。它是一个零配置的数据库，这意味着像其他数据库一样，您无需在系统中对其进行配置。</font>

<font style="color:rgb(51, 51, 51);">SQLite引擎不是一个独立于其他数据库的独立进程，您可以根据需要将其静态或动态链接到应用程序。SQLite直接访问其存储文件。</font>

## <font style="color:rgb(51, 51, 51);">为什么选择SQLite？</font>
+ <font style="color:rgb(51, 51, 51);">SQLite不需要单独的服务器进程或系统即可运行（无服务器）。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite带有零配置，这意味着不需要设置或管理。</font>
+ <font style="color:rgb(51, 51, 51);">完整的SQLite数据库存储在单个跨平台磁盘文件中。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite非常小且重量轻，完全配置的内存小于400KiB，而省略的可选功能则小于250KiB。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite是独立的，这意味着没有外部依赖关系。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite事务完全符合ACID，从而允许从多个进程或线程进行安全访问。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite支持SQL92(SQL2)标准中的大多数查询语言功能。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite用ANSI-C编写，提供简单易用的API。</font>
+ <font style="color:rgb(51, 51, 51);">SQLite在UNIX（Linux，Mac OS-X，Android，iOS）和Windows(Win32,WinCE,WinRT)上可用。</font>

## <font style="color:rgb(51, 51, 51);">SQLite简史</font>
+ <font style="color:rgb(51, 51, 51);">2000年-D.理查德·希普（R. Richard Hipp）设计SQLite的目的是无需管理程序即可运行程序。</font>
+ <font style="color:rgb(51, 51, 51);">2000年-8月，SQLite 1.0与GNU数据库管理器一起发布。</font>
+ <font style="color:rgb(51, 51, 51);">2011年-Hipp宣布将UNQl接口添加到SQLite DB并开发UNQLite（面向文档的数据库）。</font>

## <font style="color:rgb(51, 51, 51);">SQLite局限性</font>
<font style="color:rgb(51, 51, 51);">下表列出了 SQLite 中几个不受支持的 SQL92特性。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">功能与说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">RIGHT OUTER JOIN</font>**<br/><font style="color:rgb(51, 51, 51);">仅实现了LEFT OUTER JOIN。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">FULL OUTER JOIN</font>**<br/><font style="color:rgb(51, 51, 51);">仅实现了LEFT OUTER JOIN。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">ALTER TABLE</font>**<br/><font style="color:rgb(51, 51, 51);">支持ALTER TABLE命令的RENAME TABLE和ADD COLUMN变体。不支持DROP COLUMN，ALTER COLUMN，ADD CONSTRAINT。</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | **<font style="color:rgb(51, 51, 51);">Trigger support</font>**<br/><font style="color:rgb(51, 51, 51);">支持FOR EACH ROW触发器，但不支持FOR EACH STATEMENT触发器。</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | **<font style="color:rgb(51, 51, 51);">VIEWs</font>**<br/><font style="color:rgb(51, 51, 51);">SQLite中的VIEW是只读的。您可能无法在视图上执行DELETE，INSERT或UPDATE语句。</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | **<font style="color:rgb(51, 51, 51);">GRANT and REVOKE</font>**<br/><font style="color:rgb(51, 51, 51);">唯一可以应用的访问权限是基础操作系统的普通文件访问权限。</font> |


## <font style="color:rgb(51, 51, 51);">SQLite命令</font>
<font style="color:rgb(51, 51, 51);">与关系数据库进行交互的标准SQLite命令类似于SQL。它们是CREATE，SELECT，INSERT，UPDATE，DELETE和DROP。这些命令可以根据其操作性质分为几类-</font>

## <font style="color:rgb(51, 51, 51);">DDL-数据定义语言</font>
| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">命令与说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">CREATE</font>**<br/><font style="color:rgb(51, 51, 51);">在数据库中创建新表，表视图或其他对象。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">ALTER</font>**<br/><font style="color:rgb(51, 51, 51);">修改现有的数据库对象，例如表。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">DROP</font>**<br/><font style="color:rgb(51, 51, 51);">删除整个表，数据库表的视图或其他对象。</font> |


## <font style="color:rgb(51, 51, 51);">DML-数据处理语言</font>
| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">命令与说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">INSERT</font>**<br/><font style="color:rgb(51, 51, 51);">创建一条记录</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | **<font style="color:rgb(51, 51, 51);">UPDATE</font>**<br/><font style="color:rgb(51, 51, 51);">修改记录</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | **<font style="color:rgb(51, 51, 51);">DELETE</font>**<br/><font style="color:rgb(51, 51, 51);">删除记录</font> |


## <font style="color:rgb(51, 51, 51);">DQL-数据查询语言</font>
| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">命令与说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | **<font style="color:rgb(51, 51, 51);">SELECT</font>**<br/><font style="color:rgb(51, 51, 51);">从一个或多个表中检索某些记录</font> |


