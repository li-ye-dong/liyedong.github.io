# Pandas 串联
<font style="color:rgb(51, 51, 51);">Pandas 连接的操作实例</font>

<font style="color:rgb(59, 69, 73);">Pandas提供了各种功能，可以轻松地将Series，DataFrame和Panel对象组合在一起。</font>

```plain
pd.concat(objs,axis=0,join='outer',join_axes=None,
 ignore_index=False)
```

**<font style="color:rgb(51, 51, 51);">objs</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 这是Series的序列或映射，DataFrame或Panel对象。</font>**<font style="color:rgb(51, 51, 51);">axis</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− {0，1，...}，默认为0。这是要串联的轴。</font>**<font style="color:rgb(51, 51, 51);">join</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− {'inner'，'outer'}，默认为'outer'。如何处理其他轴上的索引。外部为联合，内部为交叉。</font>**<font style="color:rgb(51, 51, 51);">ignore_index</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 布尔值，默认为False。如果为True，则不要在串联轴上使用索引值。结果轴将标记为0，...，n-1。</font>**<font style="color:rgb(51, 51, 51);">join_axes</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 这是索引对象的列表。用于其他(n-1)轴的特定索引，而不是执行内部/外部设置逻辑。</font>

## <font style="color:rgb(51, 51, 51);">连接对象</font>
<font style="color:rgb(59, 69, 73);">该CONCAT函数执行所有沿轴线进行联接操作的重任。让我们创建不同的对象并进行串联。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'Marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])
 two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'Marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])
 print(pd.concat([one,two])))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Marks_scored     Name   subject_id
1             98     Alex         sub1
2             90      Amy         sub2
3             87    Allen         sub4
4             69    Alice         sub6
5             78   Ayoung         sub5
1             89    Billy         sub2
2             80    Brian         sub4
3             79     Bran         sub3
4             97    Bryce         sub6
5             88    Betty         sub5
```

<font style="color:rgb(59, 69, 73);">假设我们想将特定的键与切碎的DataFrame的每个片段相关联。我们可以通过使用keys参数来做到这一点-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'Marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])
 two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'Marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])
 print(pd.concat([one,two],keys=['x','y']))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
x  1  98    Alex    sub1
   2  90    Amy     sub2
   3  87    Allen   sub4
   4  69    Alice   sub6
   5  78    Ayoung  sub5
y  1  89    Billy   sub2
   2  80    Brian   sub4
   3  79    Bran    sub3
   4  97    Bryce   sub6
   5  88    Betty   sub5
```

<font style="color:rgb(59, 69, 73);">结果的索引是重复的；每个索引重复。</font>

<font style="color:rgb(59, 69, 73);">如果结果对象必须遵循其自己的索引，则将ignore_index设置为True。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'Marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])
 two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'Marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])
 print(pd.concat([one,two],keys=['x','y'],ignore_index=True))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Marks_scored     Name    subject_id
0             98     Alex          sub1
1             90      Amy          sub2
2             87    Allen          sub4
3             69    Alice          sub6
4             78   Ayoung          sub5
5             89    Billy          sub2
6             80    Brian          sub4
7             79     Bran          sub3
8             97    Bryce          sub6
9             88    Betty          sub5
```

<font style="color:rgb(59, 69, 73);">注意，索引完全更改，并且键也被覆盖。</font>

<font style="color:rgb(59, 69, 73);">如果需要沿axis = 1添加两个对象，则将添加新列。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'Marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])
 two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'Marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])
 print(pd.concat([one,two],axis=1))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Marks_scored    Name  subject_id   Marks_scored    Name   subject_id
1           98      Alex      sub1         89         Billy         sub2
2           90       Amy      sub2         80         Brian         sub4
3           87     Allen      sub4         79          Bran         sub3
4           69     Alice      sub6         97         Bryce         sub6
5           78    Ayoung      sub5         88         Betty         sub5
```

### <font style="color:rgb(51, 51, 51);">使用append串联</font>
<font style="color:rgb(59, 69, 73);">Concat有用的快捷方式是Series和DataFrame上的append实例方法。这些方法实际上早于concat。它们沿着轴= 0连接，即索引-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'Marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])
 two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'Marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])
 print(one.append(two))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Marks_scored    Name  subject_id
1           98      Alex      sub1
2           90       Amy      sub2
3           87     Allen      sub4
4           69     Alice      sub6
5           78    Ayoung      sub5
1           89     Billy      sub2
2           80     Brian      sub4
3           79      Bran      sub3
4           97     Bryce      sub6
5           88     Betty      sub5
```

<font style="color:rgb(59, 69, 73);">该附加功能可以采取多个对象，以及-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 one = pd.DataFrame({
    'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1','sub2','sub4','sub6','sub5'],
    'Marks_scored':[98,90,87,69,78]},
    index=[1,2,3,4,5])
 two = pd.DataFrame({
    'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2','sub4','sub3','sub6','sub5'],
    'Marks_scored':[89,80,79,97,88]},
    index=[1,2,3,4,5])
 print(one.append([two,one,two]))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Marks_scored   Name    subject_id
1           98     Alex          sub1
2           90      Amy          sub2
3           87    Allen          sub4
4           69    Alice          sub6
5           78   Ayoung          sub5
1           89    Billy          sub2
2           80    Brian          sub4
3           79     Bran          sub3
4           97    Bryce          sub6
5           88    Betty          sub5
1           98     Alex          sub1
2           90      Amy          sub2
3           87    Allen          sub4
4           69    Alice          sub6
5           78   Ayoung          sub5
1           89    Billy          sub2
2           80    Brian          sub4
3           79     Bran          sub3
4           97    Bryce          sub6
5           88    Betty          sub5
```

## <font style="color:rgb(51, 51, 51);">时间序列</font>
<font style="color:rgb(59, 69, 73);">Pandas 提供了一个强大的工具来处理时间序列数据，特别是在金融领域。在处理时间序列数据时，我们经常遇到以下情况：</font>

<font style="color:rgb(51, 51, 51);">产生时间顺序</font><font style="color:rgb(51, 51, 51);">将时间序列转换为不同的频率</font>

<font style="color:rgb(59, 69, 73);">提供了一套相对紧凑且独立的工具来执行上述任务。</font>

### <font style="color:rgb(51, 51, 51);">获取当前时间</font>
**<font style="color:rgb(59, 69, 73);">datetime.now()</font>**<font style="color:rgb(59, 69, 73);">为您提供当前日期和时间。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 print(pd.datetime.now())
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

2017-05-11 06:10:13.393147

### <font style="color:rgb(51, 51, 51);">创建一个时间戳</font>
<font style="color:rgb(59, 69, 73);">时间戳数据是将值与时间点相关联的时间序列数据的最基本类型。对于熊猫对象，这意味着使用时间点。让我们举个实例-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.Timestamp('2017-03-01'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

2017-03-01 00:00:00

<font style="color:rgb(59, 69, 73);">也可以转换整数或浮点时间。这些的默认单位是纳秒（因为这是时间戳的存储方式）。但是，通常将纪元存储在可以指定的另一个单元中。再举一个实例</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.Timestamp(1587687255,unit='s'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

 2020-04-24 00:14:15

### <font style="color:rgb(51, 51, 51);">创建时间范围</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.date_range("11:00", "13:30", freq="30min").time)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
[datetime.time(11, 0) datetime.time(11, 30) datetime.time(12, 0)
 datetime.time(12, 30) datetime.time(13, 0) datetime.time(13, 30)]
```

### <font style="color:rgb(51, 51, 51);">更改时间频率</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.date_range("11:00", "13:30", freq="H").time)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

[datetime.time(11, 0) datetime.time(12, 0) datetime.time(13, 0)]

### <font style="color:rgb(51, 51, 51);">转换为时间戳</font>
<font style="color:rgb(59, 69, 73);">若要将类似日期的对象的系列或类似列表的对象（例如字符串，历元或混合）转换，可以使用to_datetime函数。传递时，将返回一个Series（具有相同的索引），而类似列表的列表将转换为DatetimeIndex。看下面的实例-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0 2009-07-31
 1 2010-01-10
 2 NaT
 dtype: datetime64[ns]
```

<font style="color:rgb(59, 69, 73);">NaT表示不是时间（相当于NaN）</font>

<font style="color:rgb(59, 69, 73);">让我们再举一个实例。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.to_datetime(['2005/11/23', '2010.12.31', None]))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```python
DatetimeIndex(['2005-11-23', '2010-12-31', 'NaT'], dtype='datetime64[ns]', freq=None)
```

# 
