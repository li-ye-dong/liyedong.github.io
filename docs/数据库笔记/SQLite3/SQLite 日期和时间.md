<font style="color:rgb(51, 51, 51);">SQLite 支持以下五个日期和时间函数：</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">函数</font> | <font style="color:rgb(254, 254, 254);">实例</font> |
| --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | <font style="color:rgb(51, 51, 51);">date(timestring, modifier, modifier, ...)</font> | <font style="color:rgb(51, 51, 51);">以 YYYY-MM-DD 格式返回日期。</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | <font style="color:rgb(51, 51, 51);">time(timestring, modifier, modifier, ...)</font> | <font style="color:rgb(51, 51, 51);">以 HH:MM:SS 格式返回时间。</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | <font style="color:rgb(51, 51, 51);">datetime(timestring, modifier, modifier, ...)</font> | <font style="color:rgb(51, 51, 51);">以 YYYY-MM-DD HH:MM:SS 格式返回。</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | <font style="color:rgb(51, 51, 51);">julianday(timestring, modifier, modifier, ...)</font> | <font style="color:rgb(51, 51, 51);">这将返回从格林尼治时间的公元前 4714 年 11 月 24 日正午算起的天数。</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | <font style="color:rgb(51, 51, 51);">strftime(format, timestring, modifier, modifier, ...)</font> | <font style="color:rgb(51, 51, 51);">这将根据第一个参数指定的格式字符串返回格式化的日期。具体格式见下边讲解。</font> |


<font style="color:rgb(51, 51, 51);">上述五个日期和时间函数把时间字符串作为参数。时间字符串后跟零个或多个 modifier 修饰符。strftime() 函数也可以把格式字符串 format 作为其第一个参数。下面将为您详细讲解不同类型的时间字符串和修饰符。</font>

## <font style="color:rgb(51, 51, 51);">时间字符串</font>
<font style="color:rgb(51, 51, 51);">一个时间字符串可以采用下面任何一种格式：</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">时间字符串</font> | <font style="color:rgb(254, 254, 254);">实例</font> |
| --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | <font style="color:rgb(51, 51, 51);">YYYY-MM-DD</font> | <font style="color:rgb(51, 51, 51);">2010-12-30</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | <font style="color:rgb(51, 51, 51);">YYYY-MM-DD HH:MM</font> | <font style="color:rgb(51, 51, 51);">2010-12-30 12:10</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | <font style="color:rgb(51, 51, 51);">YYYY-MM-DD HH:MM:SS.SSS</font> | <font style="color:rgb(51, 51, 51);">2010-12-30 12:10:04.100</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | <font style="color:rgb(51, 51, 51);">MM-DD-YYYY HH:MM</font> | <font style="color:rgb(51, 51, 51);">30-12-2010 12:10</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | <font style="color:rgb(51, 51, 51);">HH:MM</font> | <font style="color:rgb(51, 51, 51);">12:10</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | <font style="color:rgb(51, 51, 51);">YYYY-MM-DD</font>**<font style="color:rgb(51, 51, 51);">T</font>**<font style="color:rgb(51, 51, 51);">HH:MM</font> | <font style="color:rgb(51, 51, 51);">2010-12-30 12:10</font> |
| <font style="color:rgb(51, 51, 51);">7</font> | <font style="color:rgb(51, 51, 51);">HH:MM:SS</font> | <font style="color:rgb(51, 51, 51);">12:10:01</font> |
| <font style="color:rgb(51, 51, 51);">8</font> | <font style="color:rgb(51, 51, 51);">YYYYMMDD HHMMSS</font> | <font style="color:rgb(51, 51, 51);">20101230 121001</font> |
| <font style="color:rgb(51, 51, 51);">9</font> | <font style="color:rgb(51, 51, 51);">now</font> | <font style="color:rgb(51, 51, 51);">2013-05-07</font> |


<font style="color:rgb(51, 51, 51);">您可以使用 "T" 作为分隔日期和时间的文字字符。</font>

## <font style="color:rgb(51, 51, 51);">修饰符(Modifier)</font>
<font style="color:rgb(51, 51, 51);">时间字符串后边可跟着零个或多个的修饰符，这将改变有上述五个函数返回的日期和/或时间。任何上述五大功能返回时间。修饰符应从左到右使用，下面列出了可在 SQLite 中使用的修饰符：</font>

+ <font style="color:rgb(51, 51, 51);">NNN days</font>
+ <font style="color:rgb(51, 51, 51);">NNN hours</font>
+ <font style="color:rgb(51, 51, 51);">NNN minutes</font>
+ <font style="color:rgb(51, 51, 51);">NNN.NNNN seconds</font>
+ <font style="color:rgb(51, 51, 51);">NNN months</font>
+ <font style="color:rgb(51, 51, 51);">NNN years</font>
+ <font style="color:rgb(51, 51, 51);">start of month</font>
+ <font style="color:rgb(51, 51, 51);">start of year</font>
+ <font style="color:rgb(51, 51, 51);">start of day</font>
+ <font style="color:rgb(51, 51, 51);">weekday N</font>
+ <font style="color:rgb(51, 51, 51);">unixepoch</font>
+ <font style="color:rgb(51, 51, 51);">localtime</font>
+ <font style="color:rgb(51, 51, 51);">utc</font>

## <font style="color:rgb(51, 51, 51);">格式化</font>
<font style="color:rgb(51, 51, 51);">SQLite 提供了非常方便的函数</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">strftime()</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">来格式化任何日期和时间。您可以使用以下的替换来格式化日期和时间：</font>

| <font style="color:rgb(254, 254, 254);">替换</font> | <font style="color:rgb(254, 254, 254);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">%d</font> | <font style="color:rgb(51, 51, 51);">一月中的第几天，01-31</font> |
| <font style="color:rgb(51, 51, 51);">%f</font> | <font style="color:rgb(51, 51, 51);">带小数部分的秒，SS.SSS</font> |
| <font style="color:rgb(51, 51, 51);">%H</font> | <font style="color:rgb(51, 51, 51);">小时，00-23</font> |
| <font style="color:rgb(51, 51, 51);">%j</font> | <font style="color:rgb(51, 51, 51);">一年中的第几天，001-366</font> |
| <font style="color:rgb(51, 51, 51);">%J</font> | <font style="color:rgb(51, 51, 51);">儒略日数，DDDD.DDDD</font> |
| <font style="color:rgb(51, 51, 51);">%m</font> | <font style="color:rgb(51, 51, 51);">月，00-12</font> |
| <font style="color:rgb(51, 51, 51);">%M</font> | <font style="color:rgb(51, 51, 51);">分，00-59</font> |
| <font style="color:rgb(51, 51, 51);">%s</font> | <font style="color:rgb(51, 51, 51);">从 1970-01-01 算起的秒数</font> |
| <font style="color:rgb(51, 51, 51);">%S</font> | <font style="color:rgb(51, 51, 51);">秒，00-59</font> |
| <font style="color:rgb(51, 51, 51);">%w</font> | <font style="color:rgb(51, 51, 51);">一周中的第几天，0-6 (0 is Sunday)</font> |
| <font style="color:rgb(51, 51, 51);">%W</font> | <font style="color:rgb(51, 51, 51);">一年中的第几周，01-53</font> |
| <font style="color:rgb(51, 51, 51);">%Y</font> | <font style="color:rgb(51, 51, 51);">年，YYYY</font> |
| <font style="color:rgb(51, 51, 51);">%%</font> | <font style="color:rgb(51, 51, 51);">% symbol</font> |


### <font style="color:rgb(51, 51, 51);">实例</font>
<font style="color:rgb(51, 51, 51);">现在让我们使用SQLite提示符尝试各种示例。以下命令计算当前日期。</font>

```sql
sqlite> SELECT date('now');
2013-05-07
```

<font style="color:rgb(51, 51, 51);">以下命令计算当前月份的最后一天。</font>

```sql
sqlite> SELECT date('now','start of month','+1 month','-1 day');
2013-05-31
```

<font style="color:rgb(51, 51, 51);">以下命令计算给定UNIX时间戳1092941466的日期和时间。</font>

```sql
sqlite> SELECT datetime(1092941466, 'unixepoch');
2004-08-19 18:51:06
```

<font style="color:rgb(51, 51, 51);">以下命令计算给定UNIX时间戳1092941466的日期和时间，并补偿您的本地时区。</font>

```sql
sqlite> SELECT datetime(1092941466, 'unixepoch', 'localtime');
2004-08-19 13:51:06
```

<font style="color:rgb(51, 51, 51);">以下命令计算当前的UNIX时间戳。</font>

```sql
sqlite> SELECT strftime('%s','now');
1393348134
```

<font style="color:rgb(51, 51, 51);">以下命令计算自美国独立宣言签署以来的天数。</font>

```sql
sqlite> SELECT julianday('now') - julianday('1776-07-04');
86798.7094695023
```

<font style="color:rgb(51, 51, 51);">以下命令计算自2004年某个特定时刻以来的秒数。</font>

```sql
sqlite> SELECT strftime('%s','now') - strftime('%s','2004-01-01 02:34:56');
295001572
```

<font style="color:rgb(51, 51, 51);">以下命令计算当年10月的第一个星期二的日期。</font>

```sql
sqlite> SELECT date('now','start of year','+9 months','weekday 2');
2013-10-01
```

<font style="color:rgb(51, 51, 51);">以下命令以秒为单位计算自UNIX时代以来的时间（类似于strftime（'％s'，'now'），但包括小数部分）。</font>

```sql
sqlite> SELECT (julianday('now') - 2440587.5)*86400.0;
1367926077.12598
```

<font style="color:rgb(51, 51, 51);">要在格式化日期时在UTC和本地时间值之间进行转换，请使用utc或localtime修饰符，如下所示：</font>

```sql
sqlite> SELECT time('12:00', 'localtime');
05:00:00
```

```sql
sqlite> SELECT time('12:00', 'utc');
19:00:00
```

