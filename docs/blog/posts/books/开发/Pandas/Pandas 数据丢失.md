# <font style="color:rgb(51, 51, 51);">Pandas 数据丢失</font>
<font style="color:rgb(51, 51, 51);">Pandas 数据丢失的操作实例</font>

<font style="color:rgb(59, 69, 73);">在现实生活中，数据丢失始终是一个问题。机器学习和数据挖掘等领域在模型预测的准确性方面面临严重问题，因为缺少值会导致数据质量较差。在这些领域中，缺失值处理是使模型更准确和有效的主要重点。</font>

## <font style="color:rgb(51, 51, 51);">什么时候以及为什么会丢失数据？</font>
<font style="color:rgb(59, 69, 73);">让我们考虑一项产品的在线调查。很多时候，人们不会共享与他们有关的所有信息。很少有人会分享他们的经验，但是不会分享他们使用该产品有多长时间；很少有人分享他们使用该产品的时间，他们的经历而不是他们的联系信息。因此，以某种方式或其他方式总是会丢失一部分数据，这在实时情况下非常普遍。 </font><font style="color:rgb(59, 69, 73);">现在让我们看看如何使用熊猫处理缺失值（例如NA或NaN）。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one        two     three
a  -0.576991  -0.741695  0.553172
b        NaN        NaN       NaN
c   0.744328  -1.735166  1.749580

NaN replaced with '0':
         one        two     three
a  -0.576991  -0.741695  0.553172
b   0.000000   0.000000  0.000000
c   0.744328  -1.735166  1.749580
```

<font style="color:rgb(59, 69, 73);">使用重新索引，我们创建了一个缺少值的DataFrame。在输出中，NaN表示不是数字。</font>

### <font style="color:rgb(51, 51, 51);">检查缺失值</font>
<font style="color:rgb(59, 69, 73);">为了使检测的缺失值更容易（和不同阵列dtypes），熊猫提供ISNULL()和NOTNULL()功能，这也是对系列和数据帧的对象的方法-</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df['one'].isnull())
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
a  False
 b  True
 c  False
 d  True
 e  False
 f  False
 g  True
 h  False
 Name: one, dtype: bool
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df['one'].notnull())
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
a  True
 b  False
 c  True
 d  False
 e  True
 f  True
 g  False
 h  True
 Name: one, dtype: bool
```

### <font style="color:rgb(51, 51, 51);">缺少数据的计算</font>
<font style="color:rgb(51, 51, 51);">汇总数据时，NA将被视为零</font><font style="color:rgb(51, 51, 51);">如果数据均为不适用，则结果为不适用</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df['one'].sum())
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

   2.02357685917

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
 print(df['one'].sum()
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

   nan

## <font style="color:rgb(51, 51, 51);">清理/填充丢失的数据</font>
<font style="color:rgb(59, 69, 73);">Pandas 提供了多种清除缺失值的方法。fillna函数可以通过以下几种方法用非空数据“填充” NA值。</font>

## <font style="color:rgb(51, 51, 51);">用标量值替换NaN</font>
<font style="color:rgb(59, 69, 73);">以下程序显示了如何将“ NaN”替换为“ 0”。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one',
 'two', 'three'])
 df = df.reindex(['a', 'b', 'c']))
 print(df)
 print(("NaN replaced with '0':"))
 print(df.fillna(0))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one        two     three
a  -0.576991  -0.741695  0.553172
b        NaN        NaN       NaN
c   0.744328  -1.735166  1.749580

NaN replaced with '0':
         one        two     three
a  -0.576991  -0.741695  0.553172
b   0.000000   0.000000  0.000000
c   0.744328  -1.735166  1.749580
```

<font style="color:rgb(59, 69, 73);">在这里，我们填充零值；相反，我们还可以填充其他任何值。</font>

## <font style="color:rgb(51, 51, 51);">向前和向后填充NA</font>
<font style="color:rgb(59, 69, 73);">使用“重新索引”一章中讨论的填充概念，我们将填充缺少的值。</font>

| 方法 | 操作 |
| --- | --- |
| **<font style="color:rgb(51, 51, 51);">pad/fill</font>** | <font style="color:rgb(51, 51, 51);">向前填充<</font> |
| **<font style="color:rgb(51, 51, 51);">bfill/backfill</font>** | <font style="color:rgb(51, 51, 51);">向后填充</font> |


### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df.fillna(method='pad'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one        two      three
a   0.077988   0.476149   0.965836
b   0.077988   0.476149   0.965836
c  -0.390208  -0.551605  -2.301950
d  -0.390208  -0.551605  -2.301950
e  -2.000303  -0.788201   1.510072
f  -0.930230  -0.670473   1.146615
g  -0.930230  -0.670473   1.146615
h   0.085100   0.532791   0.887415
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df.fillna(method='backfill'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one        two      three
a   0.077988   0.476149   0.965836
b  -0.390208  -0.551605  -2.301950
c  -0.390208  -0.551605  -2.301950
d  -2.000303  -0.788201   1.510072
e  -2.000303  -0.788201   1.510072
f  -0.930230  -0.670473   1.146615
g   0.085100   0.532791   0.887415
h   0.085100   0.532791   0.887415
```

## <font style="color:rgb(51, 51, 51);">删除缺失值</font>
<font style="color:rgb(59, 69, 73);">如果只想排除丢失的值，则将dropna函数与axis参数一起使用。默认情况下，axis = 0，即沿着行，这意味着如果一行中的任何值为NA，那么将排除整行。</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df.dropna())
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one two three a 0.077988 0.476149 0.965836 c -0.390208 -0.551605 -2.301950 e -2.000303 -0.788201 1.510072 f -0.930230 -0.670473 1.146615 h 0.085100 0.532791 0.887415
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
 'h'],columns=['one', 'two', 'three'])
 df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
 print(df.dropna(axis=1))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Empty DataFrame
 Columns: [ ]
 Index: [a, b, c, d, e, f, g, h]
```

## <font style="color:rgb(51, 51, 51);">替换缺失的（或）通用值</font>
<font style="color:rgb(59, 69, 73);">很多时候，我们必须用某个特定值替换一个通用值。我们可以通过应用replace方法来实现。 </font><font style="color:rgb(59, 69, 73);">用标量值替换NA是fillna()函数的等效行为。</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
 print(df.replace({1000:10,2000:60}))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one two
 0 10 10
 1 20 0
 2 30 30
 3 40 40
 4 50 50
 5 60 60
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
 print(df.replace({1000:10,2000:60})
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one two
 0 10 10
 1 20 0
 2 30 30
 3 40 40
 4 50 50
 5 60 60
```

# 
