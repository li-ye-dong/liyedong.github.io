<font style="color:rgb(51, 51, 51);">SQLite</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);"> GLOB</font>**`<font style="color:rgb(51, 51, 51);">运算符用于使用通配符仅将文本值与模式匹配。如果搜索表达式可以与模式表达式匹配，则GLOB运算符将返回true，即为1。与LIKE运算符不同，GLOB区分大小写，并且它遵循UNIX的语法来指定THE以下通配符。</font>

+ <font style="color:rgb(51, 51, 51);">星号（*）</font>
+ <font style="color:rgb(51, 51, 51);">问号（？）</font>

<font style="color:rgb(51, 51, 51);">星号（*）表示零个或多个数字或字符。问号（？）代表单个数字或字符。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是基本语法</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">*</font>**`<font style="color:rgb(51, 51, 51);">和</font>`**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">?</font>**`<font style="color:rgb(51, 51, 51);">。</font>

```sql
SELECT FROM table_name WHERE column GLOB 'XXXX*'
or 
SELECT FROM table_name WHERE column GLOB '*XXXX*'
or  
SELECT FROM table_name WHERE column GLOB 'XXXX?'
or  
SELECT FROM table_name WHERE column GLOB '?XXXX'
or  
SELECT FROM table_name WHERE column GLOB '?XXXX?'
or  
SELECT FROM table_name WHERE column GLOB '????'
```

<font style="color:rgb(51, 51, 51);">您可以使用AND或OR运算符组合多个条件。在此，XXXX可以是任何数字或字符串值。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">下表列出了许多示例，这些示例显示WHERE部分的LIKE子句带有不同的'*'和'？' 运算符。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">声明与说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY GLOB '200*'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以200开头的任何值</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY GLOB '*200*'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找任何位置有200的值</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY GLOB '?00*'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找在第二和第三位置具有00的任何值</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY GLOB '2??'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以2开头且长度至少为3个字符的任何值</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY GLOB '*2'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以2结尾的任何值</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY GLOB '?2*3'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找第二个位置带有2并以3结尾的任何值</font> |
| <font style="color:rgb(51, 51, 51);">7</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY GLOB '2???3'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以2开头和3结束的五位数数字中的任何值</font> |


<font style="color:rgb(51, 51, 51);">让我们以一个真实的实例为例，考虑带有以下记录的COMPANY表-</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

<font style="color:rgb(51, 51, 51);">下面是一个示例，它将显示COMPANY表中的所有记录，其中AGE以2开头。</font>

sqlite> SELECT * FROM COMPANY WHERE AGE  GLOB '2*';

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

<font style="color:rgb(51, 51, 51);">以下是一个示例，它将显示COMPANY表中的所有记录，其中ADDRESS在文本内将带有连字符(-)-</font>

sqlite> SELECT * FROM COMPANY WHERE ADDRESS  GLOB '*-*';

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
4           Mark        25          Rich-Mond   65000.0
6           Kim         22          South-Hall  45000.0
```

