<font style="color:rgb(51, 51, 51);">本章将带您了解SQLite程序员使用的简单且有用的命令。这些命令称为SQLite点命令，但这些命令的例外是它们不应以分号（;）终止。</font>

<font style="color:rgb(51, 51, 51);">让我们从</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">sqlite3</font>**`<font style="color:rgb(51, 51, 51);">在命令提示符处键入一个简单命令开始，它将为您提供SQLite命令提示符，您将在其中发出各种SQLite命令。</font>

```plain
$sqlite3
SQLite version 3.3.6
Enter ".help" for instructions
sqlite>
```

<font style="color:rgb(51, 51, 51);">有关可用的点命令的列表，您可以随时输入“ .help”。例如-</font>

sqlite>.help

<font style="color:rgb(51, 51, 51);">上面的命令将显示各种重要的SQLite点命令的列表，下表中列出了这些命令。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">命令与说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.backup ?DB? FILE</font>**`<br/><font style="color:rgb(51, 51, 51);">备份数据库（默认为“主”）到FILE</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.bail ON|OFF</font>**`<br/><font style="color:rgb(51, 51, 51);">遇到错误后停止。默认关闭</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.databases</font>**`<br/><font style="color:rgb(51, 51, 51);">列出附加数据库的名称和文件</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.dump ?TABLE?</font>**`<br/><font style="color:rgb(51, 51, 51);">以SQL文本格式转储数据库。如果指定了TABLE，则仅转储与LIKE模式TABLE相匹配的表</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.echo ON|OFF</font>**`<br/><font style="color:rgb(51, 51, 51);">打开或关闭命令回显</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.exit</font>**`<br/><font style="color:rgb(51, 51, 51);">退出SQLite提示</font> |
| <font style="color:rgb(51, 51, 51);">7</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.explain ON|OFF</font>**`<br/><font style="color:rgb(51, 51, 51);">打开或关闭适合EXPLAIN的输出模式。没有参数，它将打开EXPLAIN</font> |
| <font style="color:rgb(51, 51, 51);">8</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.</font>**``**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">header(s)</font>**``**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> </font>****<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">ON|OFF</font>**`<br/><font style="color:rgb(51, 51, 51);">打开或关闭页眉显示</font> |
| <font style="color:rgb(51, 51, 51);">9</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.help</font>**`<br/><font style="color:rgb(51, 51, 51);">显示此消息</font> |
| <font style="color:rgb(51, 51, 51);">10</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.import FILE TABLE</font>**`<br/><font style="color:rgb(51, 51, 51);">将数据从FILE导入TABLE</font> |
| <font style="color:rgb(51, 51, 51);">11</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.indices ?TABLE?</font>**`<br/><font style="color:rgb(51, 51, 51);">显示所有索引的名称。如果指定了TABLE，则仅显示与LIKE模式TABLE匹配的表的索引</font> |
| <font style="color:rgb(51, 51, 51);">12</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.load FILE ?ENTRY?</font>**`<br/><font style="color:rgb(51, 51, 51);">加载扩展库</font> |
| <font style="color:rgb(51, 51, 51);">13</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.log FILE|off</font>**`<br/><font style="color:rgb(51, 51, 51);">打开或关闭登录。FILE可以是stderr / stdout</font> |
| <font style="color:rgb(51, 51, 51);">14</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.mode MODE</font>**`<br/><font style="color:rgb(51, 51, 51);">设置MODE为以下之一的输出模式-</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">csv</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−逗号分隔的值</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">column</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−左对齐的列。</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">html</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− HTML <table>代码</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">insert</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− TABLE的SQL插入语句</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">line</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−每行一个值</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">list</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">−以.separator字符串分隔的值</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">tabs</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">-制表符分隔的值</font><br/>+ `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">tcl</font>**`<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− TCL列表元素</font> |
| <font style="color:rgb(51, 51, 51);">15</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.nullvalue STRING</font>**`<br/><font style="color:rgb(51, 51, 51);">打印STRING代替NULL值</font> |
| <font style="color:rgb(51, 51, 51);">16</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.output FILENAME</font>**`<br/><font style="color:rgb(51, 51, 51);">将输出发送到FILENAME</font> |
| <font style="color:rgb(51, 51, 51);">17</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.output stdout</font>**`<br/><font style="color:rgb(51, 51, 51);">将输出发送到屏幕</font> |
| <font style="color:rgb(51, 51, 51);">18岁</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.print STRING...</font>**`<br/><font style="color:rgb(51, 51, 51);">打印文字STRING</font> |
| <font style="color:rgb(51, 51, 51);">19</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.prompt MAIN CONTINUE</font>**`<br/><font style="color:rgb(51, 51, 51);">替换标准提示</font> |
| <font style="color:rgb(51, 51, 51);">20</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.quit</font>**`<br/><font style="color:rgb(51, 51, 51);">退出SQLite提示</font> |
| <font style="color:rgb(51, 51, 51);">21</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.read FILENAME</font>**`<br/><font style="color:rgb(51, 51, 51);">在FILENAME中执行SQL</font> |
| <font style="color:rgb(51, 51, 51);">22</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.schema ?TABLE?</font>**`<br/><font style="color:rgb(51, 51, 51);">显示CREATE语句。如果指定了TABLE，则仅显示与LIKE模式TABLE匹配的表</font> |
| <font style="color:rgb(51, 51, 51);">23</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.separator STRING</font>**`<br/><font style="color:rgb(51, 51, 51);">更改输出模式和.import使用的分隔符</font> |
| <font style="color:rgb(51, 51, 51);">24</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.show</font>**`<br/><font style="color:rgb(51, 51, 51);">显示各种设置的当前值</font> |
| <font style="color:rgb(51, 51, 51);">25</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.stats ON|OFF</font>**`<br/><font style="color:rgb(51, 51, 51);">开启或关闭统计</font> |
| <font style="color:rgb(51, 51, 51);">26</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.tables ?PATTERN?</font>**`<br/><font style="color:rgb(51, 51, 51);">列出与LIKE模式匹配的表的名称</font> |
| <font style="color:rgb(51, 51, 51);">27</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.timeout MS</font>**`<br/><font style="color:rgb(51, 51, 51);">尝试打开锁定的表，以毫秒为单位</font> |
| <font style="color:rgb(51, 51, 51);">28</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.width NUM NUM</font>**`<br/><font style="color:rgb(51, 51, 51);">设置“列”模式的列宽</font> |
| <font style="color:rgb(51, 51, 51);">29</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.timer ON|OFF</font>**`<br/><font style="color:rgb(51, 51, 51);">打开或关闭CPU计时器测量</font> |


<font style="color:rgb(51, 51, 51);">让我们尝试使用</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">.show</font>**`<font style="color:rgb(51, 51, 51);">命令查看SQLite命令提示符的默认设置。</font>

```plain
sqlite>.show
     echo: off
  explain: off
  headers: off
     mode: column
nullvalue: ""
   output: stdout
separator: "|"
    width:
sqlite>
```

<font style="color:rgb(51, 51, 51);">确保在sqlite>提示符和dot命令之间没有空格，否则它将无法正常工作。</font>

## <font style="color:rgb(51, 51, 51);">格式化输出</font>
<font style="color:rgb(51, 51, 51);">您可以使用以下点命令序列来格式化输出。</font>

```plain
sqlite>.header on
sqlite>.mode column
sqlite>.timer on
sqlite>
```

<font style="color:rgb(51, 51, 51);">上面的设置将产生以下格式的输出。</font>

```plain
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
CPU Time: user 0.000000 sys 0.000000
```

上述配置只是临时生效，需要长期配置，需要使用配置文件

### 创建 SQLite 配置脚本
如果你希望每次启动 `sqlite3` 都自动应用这些设置，可以编写一个 `.sqliterc` 文件（SQLite 的启动配置文件），并将其放在用户主目录下（例如，Linux 和 macOS 系统中的 `~/.sqliterc` 或 Windows 系统中的 `C:\Users\YourUsername\.sqliterc`）。

在 `.sqliterc` 文件中，添加以下内容：

```plain
sql


复制代码
.header on
.mode column
.timer on
```

SQLite 每次启动时会自动读取这个文件，并应用这些配置。

## <font style="color:rgb(51, 51, 51);">sqlite_master表</font>
<font style="color:rgb(51, 51, 51);">主表保存有关数据库表的关键信息，该表称为</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">sqlite_master</font>**`<font style="color:rgb(51, 51, 51);">。您可以看到其架构，如下所示：</font>

sqlite>.schema sqlite_master

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```plain
CREATE TABLE sqlite_master (
   type text,
   name text,
   tbl_name text,
   rootpage integer,
   sql text);
```

