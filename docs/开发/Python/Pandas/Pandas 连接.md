# Pandas 连接
<font style="color:rgb(51, 51, 51);">Pandas 连接的操作实例</font>

<font style="color:rgb(59, 69, 73);">Pandas具有与SQL等关系数据库非常相似的功能齐全的高性能内存中连接操作。 </font><font style="color:rgb(59, 69, 73);">Pandas提供单个功能merge作为DataFrame对象之间所有标准数据库联接操作的入口点</font>

```plain
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
 left_index=False, right_index=False, sort=True)
```

<font style="color:rgb(59, 69, 73);">在这里，我们使用了以下参数：</font>

**<font style="color:rgb(51, 51, 51);">left</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 一个DataFrame对象。</font>**<font style="color:rgb(51, 51, 51);">right</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 另一个DataFrame对象。</font>**<font style="color:rgb(51, 51, 51);">on</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 列（名）加入上。必须在左右DataFrame对象中都找到。</font>**<font style="color:rgb(51, 51, 51);">left_on</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 左侧DataFrame中的列用作键。可以是列名，也可以是长度等于DataFrame长度的数组。</font>**<font style="color:rgb(51, 51, 51);">right_on</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 右侧DataFrame中的列用作键。可以是列名，也可以是长度等于DataFrame长度的数组。</font>**<font style="color:rgb(51, 51, 51);">left_index</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 如果为True，则使用左侧DataFrame的索引（行标签）作为其连接键。如果DataFrame具有MultiIndex（分层），则级别数必须与右侧DataFrame中的连接键数匹配。</font>**<font style="color:rgb(51, 51, 51);">right_index</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 相同的使用作为left_index为正确的数据帧。</font>**<font style="color:rgb(51, 51, 51);">how</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− “左”，“右”，“外”，“内”之一。默认为内部。每种方法已在下面描述。</font>**<font style="color:rgb(51, 51, 51);">sort</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 排序的结果数据框中加入字典顺序按键。默认情况下为True，在许多情况下，设置为False将大大提高性能。</font>

<font style="color:rgb(59, 69, 73);">现在让我们创建两个不同的DataFrame并对其执行合并操作。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
 right = pd.DataFrame(
    {'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']}))
 print(left
 print(right)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Name  id   subject_id
0   Alex   1         sub1
1    Amy   2         sub2
2  Allen   3         sub4
3  Alice   4         sub6
4  Ayoung  5         sub5

    Name  id   subject_id
0  Billy   1         sub2
1  Brian   2         sub4
2  Bran    3         sub3
3  Bryce   4         sub6
4  Betty   5         sub5
```

### <font style="color:rgb(51, 51, 51);">在一个键上合并两个数据框</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
 right = pd.DataFrame({
 'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
 print(pd.merge(left,right,on='id'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Name_x   id  subject_id_x   Name_y   subject_id_y
0  Alex      1          sub1    Billy           sub2
1  Amy       2          sub2    Brian           sub4
2  Allen     3          sub4     Bran           sub3
3  Alice     4          sub6    Bryce           sub6
4  Ayoung    5          sub5    Betty           sub5
```

### <font style="color:rgb(51, 51, 51);">在多个键上合并两个数据框</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
 right = pd.DataFrame({
 'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
 print(pd.merge(left,right,on=['id','subject_id']))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Name_x   id   subject_id   Name_y
0    Alice    4         sub6    Bryce
1   Ayoung    5         sub5    Betty
```

## <font style="color:rgb(51, 51, 51);">合并使用“how”参数</font>
<font style="color:rgb(59, 69, 73);">合并的how参数指定如何确定要在结果表中包括哪些键。如果左侧或右侧表中均未出现组合键，则联接表中的值为NA。</font>

<font style="color:rgb(59, 69, 73);">这里的一个总结如何选择和他们的SQL等价的名字:</font>

| 合并方法 | SQL等效 | 描述 |
| --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">left</font> | <font style="color:rgb(51, 51, 51);">LEFT OUTER JOIN</font> | <font style="color:rgb(51, 51, 51);">使用左侧对象的key</font> |
| <font style="color:rgb(51, 51, 51);">right</font> | <font style="color:rgb(51, 51, 51);">RIGHT OUTER JOIN</font> | <font style="color:rgb(51, 51, 51);">使用正确对象的key</font> |
| <font style="color:rgb(51, 51, 51);">outer</font> | <font style="color:rgb(51, 51, 51);">FULL OUTER JOIN</font> | <font style="color:rgb(51, 51, 51);">使用联合key</font> |
| <font style="color:rgb(51, 51, 51);">inner</font> | <font style="color:rgb(51, 51, 51);">INNER JOIN</font> | <font style="color:rgb(51, 51, 51);">使用key的交集</font> |


### <font style="color:rgb(51, 51, 51);">左连接</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
 right = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
 print(pd.merge(left, right, on='subject_id', how='left'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Name_x   id_x   subject_id   Name_y   id_y
0     Alex      1         sub1      NaN    NaN
1      Amy      2         sub2    Billy    1.0
2    Allen      3         sub4    Brian    2.0
3    Alice      4         sub6    Bryce    4.0
4   Ayoung      5         sub5    Betty    5.0
```

### <font style="color:rgb(51, 51, 51);">右连接</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
 right = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
 print(pd.merge(left, right, on='subject_id', how='right'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Name_x  id_x   subject_id   Name_y   id_y
0      Amy   2.0         sub2    Billy      1
1    Allen   3.0         sub4    Brian      2
2    Alice   4.0         sub6    Bryce      4
3   Ayoung   5.0         sub5    Betty      5
4      NaN   NaN         sub3     Bran      3
```

### <font style="color:rgb(51, 51, 51);">外连接</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
 right = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
 print(pd.merge(left, right, how='outer', on='subject_id'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Name_x  id_x   subject_id   Name_y   id_y
0     Alex   1.0         sub1      NaN    NaN
1      Amy   2.0         sub2    Billy    1.0
2    Allen   3.0         sub4    Brian    2.0
3    Alice   4.0         sub6    Bryce    4.0
4   Ayoung   5.0         sub5    Betty    5.0
5      NaN   NaN         sub3     Bran    3.0
```

### <font style="color:rgb(51, 51, 51);">内连接</font>
<font style="color:rgb(59, 69, 73);">连接将在索引上执行。联接操作接受调用它的对象。因此，a.join(b)不等于b.join(a)。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5']})
 right = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5']})
 print(pd.merge(left, right, on='subject_id', how='inner'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Name_x   id_x   subject_id   Name_y   id_y
0      Amy      2         sub2    Billy      1
1    Allen      3         sub4    Brian      2
2    Alice      4         sub6    Bryce      4
3   Ayoung      5         sub5    Betty      5
```

# 
