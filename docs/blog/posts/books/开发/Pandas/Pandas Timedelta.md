# Pandas Timedelta
<font style="color:rgb(51, 51, 51);">Pandas Timedelta的操作实例</font>

<font style="color:rgb(59, 69, 73);">时间增量是时间差异，以差异单位表示，例如，天，小时，分钟，秒。它们可以是正面的也可以是负面的。</font>

<font style="color:rgb(59, 69, 73);">通过传递字符串文字，我们可以创建一个timedelta对象。</font>

## <font style="color:rgb(51, 51, 51);">字符串</font>
<font style="color:rgb(59, 69, 73);">我们可以使用各种参数创建Timedelta对象，如下所示-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

 2 days 02:15:30

## <font style="color:rgb(51, 51, 51);">整数</font>
<font style="color:rgb(59, 69, 73);">通过为单位传递整数值，参数将创建一个Timedelta对象。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.Timedelta(6,unit='h'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

 0 days 06:00:00

## <font style="color:rgb(51, 51, 51);">数据偏移</font>
<font style="color:rgb(59, 69, 73);">数据偏移量（例如-周，天，小时，分钟，秒，毫秒，微秒，纳秒）也可以在构造中使用。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.Timedelta(days=2))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

2 days 00:00:00

## <font style="color:rgb(51, 51, 51);">to_timedelta()</font>
<font style="color:rgb(59, 69, 73);">使用pd.to_timedelta，您可以将标量，数组，列表或序列从公认的timedelta格式/值转换为Timedelta类型。如果输入为Series，则将构造Series；如果输入为标量，则将构造标量；否则，将输出TimedeltaIndex。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.Timedelta(days=2))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

2 days 00:00:00

## <font style="color:rgb(51, 51, 51);">具体操作</font>
<font style="color:rgb(59, 69, 73);">您可以对Series / DataFrame进行操作，并通过对datetime64 [ns] Series或Timestamps 进行减法运算来构造timedelta64 [ns] Series 。 </font><font style="color:rgb(59, 69, 73);">现在让我们创建一个带有Timedelta和datetime对象的DataFrame并对其执行一些算术运算-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
 td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
 df = pd.DataFrame(dict(A = s, B = td))
 print(df)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
A      B
0  2012-01-01 0 days
1  2012-01-02 1 days
2  2012-01-03 2 days
```

## <font style="color:rgb(51, 51, 51);">加法运算</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
 td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
 df = pd.DataFrame(dict(A = s, B = td))
 df['C']=df['A']+df['B']
 print(df)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
A      B          C
0 2012-01-01 0 days 2012-01-01
1 2012-01-02 1 days 2012-01-03
2 2012-01-03 2 days 2012-01-05
```

## <font style="color:rgb(51, 51, 51);">减法运算</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
 td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
 df = pd.DataFrame(dict(A = s, B = td))
 df['C']=df['A']+df['B']
 df['D']=df['C']+df['B']
 print(df)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
A      B          C          D
0 2012-01-01 0 days 2012-01-01 2012-01-01
1 2012-01-02 1 days 2012-01-03 2012-01-04
2 2012-01-03 2 days 2012-01-05 2012-01-07
```

# 
