<font style="color:rgb(51, 51, 51);">SQLite数据类型是一个属性，用于指定任何对象的数据类型。每个列，变量和表达式在SQLite中都有相关的数据类型。</font>

<font style="color:rgb(51, 51, 51);">您将在创建表时使用这些数据类型。SQLite使用更通用的动态类型系统。在SQLite中，值的数据类型与值本身相关联，而不是与其容器相关联。</font>

## <font style="color:rgb(51, 51, 51);">SQLite存储类</font>
<font style="color:rgb(51, 51, 51);">存储在SQLite数据库中的每个值都具有以下存储类别之一-</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">储存类别和说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">NULL</font>**`<br/><font style="color:rgb(51, 51, 51);">该值为NULL值。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">INTEGER</font>**`<br/><font style="color:rgb(51, 51, 51);">该值是一个有符号整数，根据值的大小存储在1、2、3、4、6或8个字节中。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">REAL</font>**`<br/><font style="color:rgb(51, 51, 51);">该值是一个浮点值，存储为8字节IEEE浮点数。</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">TEXT</font>**`<br/><font style="color:rgb(51, 51, 51);">该值是一个文本字符串，使用数据库编码（UTF-8，UTF-16BE或UTF-16LE）存储</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">BLOB</font>**`<br/><font style="color:rgb(51, 51, 51);">该值是数据的一滴，完全按输入存储。</font> |


<font style="color:rgb(51, 51, 51);">SQLite存储类比数据类型更通用。例如，INTEGER存储类包括6种不同长度的不同整数数据类型。</font>

## <font style="color:rgb(51, 51, 51);">SQLite关联类型</font>
<font style="color:rgb(51, 51, 51);">SQLite支持列上的类型相似性的概念。 任何列仍然可以存储任何类型的数据，但是列的首选存储类称为亲和力。  SQLite3数据库中的每个表列都分配了以下类型关联性之一-</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">亲和力和描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">TEXT</font>**`<br/><font style="color:rgb(51, 51, 51);">该列使用存储类NULL，TEXT或BLOB存储所有数据。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">NUMERIC</font>**`<br/><font style="color:rgb(51, 51, 51);">该列可能包含使用所有五个存储类的值。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">INTEGER</font>**`<br/><font style="color:rgb(51, 51, 51);">行为与具有NUMERIC相关性的列相同，但CAST表达式除外。</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">REAL</font>**`<br/><font style="color:rgb(51, 51, 51);">行为类似于具有NUMERIC关联性的列，不同之处在于它强制将整数值转换为浮点表示形式。</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">NONE</font>**`<br/><font style="color:rgb(51, 51, 51);">亲和性为NONE的列不喜欢一个存储类别而不是另一个存储类别，也没有尝试将数据从一个存储类别强制转换为另一个存储类别。</font> |


## <font style="color:rgb(51, 51, 51);">SQLite关联性和类型名称</font>
<font style="color:rgb(51, 51, 51);">下表列出了各种数据类型名称，这些名称可以在创建具有相应应用相似性的SQLite3表时使用。</font>

| <font style="color:rgb(254, 254, 254);">数据类型</font> | <font style="color:rgb(254, 254, 254);">亲和力</font> |
| --- | --- |
| + <font style="color:rgb(51, 51, 51);">INT</font><br/>+ <font style="color:rgb(51, 51, 51);">INTEGER</font><br/>+ <font style="color:rgb(51, 51, 51);">TINYINT</font><br/>+ <font style="color:rgb(51, 51, 51);">SMALLINT</font><br/>+ <font style="color:rgb(51, 51, 51);">MEDIUMINT</font><br/>+ <font style="color:rgb(51, 51, 51);">BIGINT</font><br/>+ <font style="color:rgb(51, 51, 51);">UNSIGNED BIG INT</font><br/>+ <font style="color:rgb(51, 51, 51);">INT2</font><br/>+ <font style="color:rgb(51, 51, 51);">INT8</font> | <font style="color:rgb(51, 51, 51);">INTEGER</font> |
| + <font style="color:rgb(51, 51, 51);">CHARACTER(20)</font><br/>+ <font style="color:rgb(51, 51, 51);">VARCHAR(255)</font><br/>+ <font style="color:rgb(51, 51, 51);">VARYING CHARACTER(255)</font><br/>+ <font style="color:rgb(51, 51, 51);">NCHAR(55)</font><br/>+ <font style="color:rgb(51, 51, 51);">NATIVE CHARACTER(70)</font><br/>+ <font style="color:rgb(51, 51, 51);">NVARCHAR(100)</font><br/>+ <font style="color:rgb(51, 51, 51);">TEXT</font><br/>+ <font style="color:rgb(51, 51, 51);">CLOB</font> | <font style="color:rgb(51, 51, 51);">TEXT</font> |
| + <font style="color:rgb(51, 51, 51);">BLOB</font><br/>+ <font style="color:rgb(51, 51, 51);">未指定数据类型</font> | <font style="color:rgb(51, 51, 51);">NONE</font> |
| + <font style="color:rgb(51, 51, 51);">REAL</font><br/>+ <font style="color:rgb(51, 51, 51);">DOUBLE</font><br/>+ <font style="color:rgb(51, 51, 51);">DOUBLE PRECISION</font><br/>+ <font style="color:rgb(51, 51, 51);">FLOAT</font> | <font style="color:rgb(51, 51, 51);">REAL</font> |
| + <font style="color:rgb(51, 51, 51);">NUMERIC</font><br/>+ <font style="color:rgb(51, 51, 51);">DECIMAL(10,5)</font><br/>+ <font style="color:rgb(51, 51, 51);">BOOLEAN</font><br/>+ <font style="color:rgb(51, 51, 51);">DATE</font><br/>+ <font style="color:rgb(51, 51, 51);">DATETIME</font> | <font style="color:rgb(51, 51, 51);">NUMERIC</font> |


## <font style="color:rgb(51, 51, 51);">布尔数据类型</font>
<font style="color:rgb(51, 51, 51);">SQLite没有单独的布尔存储类。而是将布尔值存储为整数0(false)和1(true)。</font>

## <font style="color:rgb(51, 51, 51);">日期和时间数据类型</font>
<font style="color:rgb(51, 51, 51);">SQLite没有用于存储日期和/或时间的单独存储类，但是SQLite能够将日期和时间存储为TEXT，REAL或INTEGER值。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">存储类别和日期格式</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">TEXT</font>**`<br/><font style="color:rgb(51, 51, 51);">日期格式为“ YYYY-MM-DD HH：MM：SS.SSS”</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">REAL</font>**`<br/><font style="color:rgb(51, 51, 51);">公元前4714年11月24日格林威治正午以来的天数。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">INTEGER</font>**`<br/><font style="color:rgb(51, 51, 51);">自1970-01-01 00:00:00 UTC以来的秒数</font> |


<font style="color:rgb(51, 51, 51);">您可以选择以这些格式存储日期和时间，并使用内置的日期和时间函数在格式之间自由转换。</font>

