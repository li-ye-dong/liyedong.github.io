<font style="color:rgb(51, 51, 51);">SQLite LIKE 操作符用于使用通配符将文本值与模式匹配。如果搜索表达式可以与模式表达式匹配，LIKE 运算符将返回 true，即1。有两个通配符与 LIKE 操作符-一起使用</font>

+ <font style="color:rgb(51, 51, 51);">百分号（％）</font>
+ <font style="color:rgb(51, 51, 51);">下划线(_)</font>

<font style="color:rgb(51, 51, 51);">百分号代表零个，一个或多个数字或字符。下划线表示单个数字或字符。这些符号可以组合使用。</font>

## <font style="color:rgb(51, 51, 51);">语法</font>
<font style="color:rgb(51, 51, 51);">以下是 ％ 和 _ 的基本语法。</font>

```sql
SELECT FROM table_name  WHERE column LIKE 'XXXX%'
or 
SELECT FROM table_name  WHERE column LIKE '%XXXX%'
or 
SELECT FROM table_name WHERE column LIKE 'XXXX_'
or
SELECT FROM table_name WHERE column LIKE '_XXXX'
or
SELECT FROM table_nameWHERE column LIKE '_XXXX_'
```

<font style="color:rgb(51, 51, 51);">可以使用 AND 或 OR 运算符组合 n 个条件。这里，XXXX 可以是任何数值或字符串值。</font>

## <font style="color:rgb(51, 51, 51);">在线示例</font>
<font style="color:rgb(51, 51, 51);">下表列出了许多示例，这些示例显示WHERE部分具有不同的LIKE子句，且带有'％'和'_'运算符。</font>

| <font style="color:rgb(254, 254, 254);">序号</font> | <font style="color:rgb(254, 254, 254);">声明与说明</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY LIKE '200%'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以200开头的任何值</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY LIKE '%200%'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找任何位置有200的值</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY LIKE '_00%'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找在第二和第三位置具有00的任何值</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY LIKE '2_%_%'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以2开头且长度至少为3个字符的任何值</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY LIKE '%2'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以2结尾的任何值</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY LIKE '_2%3'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找第二个位置带有2并以3结尾的任何值</font> |
| <font style="color:rgb(51, 51, 51);">7</font> | `**<font style="color:rgb(199, 37, 78);background-color:rgb(249, 242, 244);">WHERE SALARY LIKE '2___3'</font>**`<br/><font style="color:rgb(51, 51, 51);">查找以2开头和3结束的五位数数字中的任何值</font> |


<font style="color:rgb(51, 51, 51);">让我们举一个真实的实例，考虑带有以下记录的COMPANY表。</font>

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

<font style="color:rgb(51, 51, 51);">下面是一个示例，它将显示COMPANY表中AGE以2开头的所有记录。</font>

sqlite> SELECT * FROM COMPANY WHERE AGE LIKE '2%';

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

<font style="color:rgb(51, 51, 51);">下面是一个示例，它将显示COMPANY表中的所有记录，其中ADDRESS在文本内将带有连字符(-)。</font>

sqlite> SELECT * FROM COMPANY WHERE ADDRESS  LIKE '%-%';

<font style="color:rgb(51, 51, 51);">这将产生以下结果。</font>

```sql
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
4           Mark        25          Rich-Mond   65000.0
6           Kim         22          South-Hall  45000.0
```

