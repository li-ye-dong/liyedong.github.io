<font style="color:rgb(51, 51, 51);">Pandas 基本方法实例</font>

<font style="color:rgb(59, 69, 73);">到目前为止，我们了解了三个Pandas DataStructures以及如何创建它们。由于它在实时数据处理中的重要性，因此我们将主要关注DataFrame对象，并讨论其他一些DataStructures。</font>

| <font style="color:rgb(51, 51, 51);">方法</font> | <font style="color:rgb(51, 51, 51);">描述</font> |
| --- | --- |
| **<font style="color:rgb(51, 51, 51);">axes</font>** | <font style="color:rgb(51, 51, 51);">返回行轴标签的列表</font> |
| **<font style="color:rgb(51, 51, 51);">dtype</font>** | <font style="color:rgb(51, 51, 51);">返回对象的dtype。</font> |
| **<font style="color:rgb(51, 51, 51);">empty</font>** | <font style="color:rgb(51, 51, 51);">如果Series为空，则返回True。</font> |
| **<font style="color:rgb(51, 51, 51);">ndim</font>** | <font style="color:rgb(51, 51, 51);">根据定义返回基础数据的维数。</font> |
| **<font style="color:rgb(51, 51, 51);">size</font>** | <font style="color:rgb(51, 51, 51);">返回基础数据中的元素数。</font> |
| **<font style="color:rgb(51, 51, 51);">values</font>** | <font style="color:rgb(51, 51, 51);">将Series返回为ndarray。</font> |
| **<font style="color:rgb(51, 51, 51);">head()</font>** | <font style="color:rgb(51, 51, 51);">返回前n行。</font> |
| **<font style="color:rgb(51, 51, 51);">tail()</font>** | <font style="color:rgb(51, 51, 51);">返回最后n行。</font> |


<font style="color:rgb(51, 51, 51);">接下来我们创建一个Series，并看看上所有列表的属性操作。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用100随机数创建一个Series
 s = pd.Series(np.random.randn(4))
 print(s)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0   0.967853
1  -0.148368
2  -1.395906
3  -1.758394
dtype: float64
```

### axes
<font style="color:rgb(59, 69, 73);">返回Series标签的列表</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用100随机数创建一个Series
 s = pd.Series(np.random.randn(4))
 print ("The axes are:")
 print(s.axes)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
The axes are:
 [RangeIndex(start=0, stop=4, step=1)]
```

<font style="color:rgb(59, 69, 73);">以上结果是0到5（即[0,1,2,3,4]）。</font>

### empty
<font style="color:rgb(59, 69, 73);">返回布尔值，说明对象是否为空。True表示对象为空</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用100随机数创建一个Series
 s = pd.Series(np.random.randn(4))
 print ("Is the Object empty?")
 print(s.empty)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Is the Object empty?
False
```

### ndim
<font style="color:rgb(51, 51, 51);">返回对象的维数。根据定义，Series 是一个1D 数据结构，所以它返回</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用4个随机数创建一个Series
 s = pd.Series(np.random.randn(4))
 print s
 print ("The dimensions of the object:")
 print(s.ndim)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0   0.175898
1   0.166197
2  -0.609712
3  -1.377000
dtype: float64

The dimensions of the object:
1
```

### size
<font style="color:rgb(59, 69, 73);">返回Series的大小（长度）.</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用4个随机数创建一个Series
 s = pd.Series(np.random.randn(2))
 print s
 print ("The size of the object:")
 print(s.size)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0   3.078058
1  -1.207803
dtype: float64

The size of the object:
2
```

### values
<font style="color:rgb(59, 69, 73);">以数组形式返回Series数据</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用4个随机数创建一个Series
 s = pd.Series(np.random.randn(4))
 print s
 print ("The actual data series is:")
 print(s.values)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0   1.787373
1  -0.605159
2   0.180477
3  -0.140922
dtype: float64

The actual data series is:
[ 1.78737302 -0.60515881 0.18047664 -0.1409218 ]
```

### Head 和 Tail
<font style="color:rgb(59, 69, 73);">要查看Series或DataFrame对象的头尾数据，请使用head() 和tail() 方法。</font>

**<font style="color:rgb(59, 69, 73);">head()</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">返回前n行（观察索引值）。默认显示的元素数是5，但是您可以传递自定义数字。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用4个随机数创建一个Series
 s = pd.Series(np.random.randn(4))
 print ("最初的系列是:")
 print s
 print ("数据系列的前两行:")
 print(s.head(2))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
最初的系列是:
0   0.720876
1  -0.765898
2   0.479221
3  -0.139547
dtype: float64

数据系列的前两行:
0   0.720876
1  -0.765898
dtype: float64
```

**<font style="color:rgb(59, 69, 73);">tail()</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">返回最后n行（观察索引值）。默认显示的元素数是5，但是您可以传递自定义数字。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 用4个随机数创建一个Series
 s = pd.Series(np.random.randn(4))
 print("最初的系列是:")
 print(s)
 print("数据序列的最后两行:")
 print(s)tail(2)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
最初的系列是:
0 -0.655091
1 -0.881407
2 -0.608592
3 -2.341413
dtype: float64

数据序列的最后两行:
2 -0.608592
3 -2.341413
dtype: float64
```

## DataFrame 基本功能
<font style="color:rgb(59, 69, 73);">现在让我们了解什么是DataFrame基本功能。下表列出了有助于DataFrame基本功能的重要属性或方法。</font>

| <font style="color:rgb(51, 51, 51);">属性/方法</font> | <font style="color:rgb(51, 51, 51);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">T</font> | <font style="color:rgb(51, 51, 51);">行和列互相转换</font> |
| <font style="color:rgb(51, 51, 51);">axes</font> | <font style="color:rgb(51, 51, 51);">返回以行轴标签和列轴标签为唯一成员的列表。</font> |
| **<font style="color:rgb(51, 51, 51);">dtypes</font>** | <font style="color:rgb(51, 51, 51);">返回此对象中的dtypes。</font> |
| **<font style="color:rgb(51, 51, 51);">empty</font>** | <font style="color:rgb(51, 51, 51);">如果NDFrame完全为空[没有项目]，则为true；否则为false。如果任何轴的长度为0。</font> |
| **<font style="color:rgb(51, 51, 51);">ndim</font>** | <font style="color:rgb(51, 51, 51);">轴数/数组尺寸。</font> |
| **<font style="color:rgb(51, 51, 51);">shape</font>** | <font style="color:rgb(51, 51, 51);">返回表示DataFrame维度的元组。</font> |
| **<font style="color:rgb(51, 51, 51);">size</font>** | <font style="color:rgb(51, 51, 51);">NDFrame中的元素数。</font> |
| **<font style="color:rgb(51, 51, 51);">values</font>** | <font style="color:rgb(51, 51, 51);">NDFrame的数字表示。</font> |
| **<font style="color:rgb(51, 51, 51);">head()</font>** | <font style="color:rgb(51, 51, 51);">返回前n行。</font> |
| **<font style="color:rgb(51, 51, 51);">tail()</font>** | <font style="color:rgb(51, 51, 51);">返回最后n行。</font> |


<font style="color:rgb(59, 69, 73);">下面我们下创建一个DataFrame并查看上述属性的所有操作方式。</font>

### Example
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("Our data series is:")
 print(df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Our data series is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Smith   4.60
6   23    Jack    3.80
```

### T (Transpose)
<font style="color:rgb(59, 69, 73);">返回DataFrame的转置。行和列将互换。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("数据序列的转置是:")
 print(df.T)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
数据序列的转置是:
         0     1       2      3      4      5       6
Age      25    26      25     23     30     29      23
Name     Tom   James   Ricky  Vin    Steve  Smith   Jack
Rating   4.23  3.24    3.98   2.56   3.2    4.6     3.8
```

### axes
<font style="color:rgb(59, 69, 73);">返回行轴标签和列轴标签的列表。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("行轴标签和列轴标签是:")
 print(df.axes)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
行轴标签和列轴标签是:
 [RangeIndex(start=0, stop=7, step=1), Index([u'Age', u'Name', u'Rating'],
 dtype='object')]
```

### dtypes
<font style="color:rgb(59, 69, 73);">返回每一列的数据类型。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("每列的数据类型如下:")
 print(df.dtypes)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
每列的数据类型如下:
Age     int64
Name    object
Rating  float64
dtype: object
```

### empty
<font style="color:rgb(59, 69, 73);">返回布尔值，说明对象是否为空；True表示对象为空。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
  
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("Is the object empty?")
 print(df.empty)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Is the object empty?
 False
```

### ndim
<font style="color:rgb(59, 69, 73);">返回对象的数量。根据定义，DataFrame是2D对象。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("Our object is:")
 print df
 print ("The dimension of the object is:")
 print(df.ndim)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Our object is:
      Age    Name     Rating
0     25     Tom      4.23
1     26     James    3.24
2     25     Ricky    3.98
3     23     Vin      2.56
4     30     Steve    3.20
5     29     Smith    4.60
6     23     Jack     3.80

The dimension of the object is:
2
```

### shape
<font style="color:rgb(59, 69, 73);">返回表示DataFrame维度的元组。元组(a,b)，其中a表示行数，b表示列数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
  
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("Our object is:")
 print df
 print ("The shape of the object is:")
 print(df.shape)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Our object is:
   Age   Name    Rating
0  25    Tom     4.23
1  26    James   3.24
2  25    Ricky   3.98
3  23    Vin     2.56
4  30    Steve   3.20
5  29    Smith   4.60
6  23    Jack    3.80

The shape of the object is:
(7, 3)
```

### size
<font style="color:rgb(59, 69, 73);">返回DataFrame中的元素数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
  
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("Our object is:")
 print df
 print ("The total number of elements in our object is:")
 print(df.size)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Our object is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Smith   4.60
6   23    Jack    3.80

The total number of elements in our object is:
21
```

### values
<font style="color:rgb(59, 69, 73);">以NDarray的形式返回DataFrame中的实际数据。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
  
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("Our object is:")
 print df
 print ("The actual data in our data frame is:")
 print(df.values)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Our object is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Smith   4.60
6   23    Jack    3.80
The actual data in our data frame is:
[[25 'Tom' 4.23]
[26 'James' 3.24]
[25 'Ricky' 3.98]
[23 'Vin' 2.56]
[30 'Steve' 3.2]
[29 'Smith' 4.6]
[23 'Jack' 3.8]]
```

### Head & Tail
<font style="color:rgb(59, 69, 73);">要查看DataFrame对象的头尾数据，请使用head()和tail()方法。head() 返回前n行（观察索引值）。默认显示的元素数是5，但是您可以传递自定义数字。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("Our data frame is:")
 print df
 print ("The first two rows of the data frame is:")
 print(df.head(2))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Our data frame is:
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Smith   4.60
6   23    Jack    3.80

The first two rows of the data frame is:
   Age   Name   Rating
0  25    Tom    4.23
1  26    James  3.24
```

**<font style="color:rgb(59, 69, 73);">tail()</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">返回最后n行（观察索引值）。默认显示的元素数是5，但是您可以传递自定义数字。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
    'Age':pd.Series([25,26,25,23,30,29,23]), 
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
  
 # 创建一个 DataFrame
 df = pd.DataFrame(d)
 print ("我们的数据帧是:")
 print df
 print ("数据帧的最后两行是:")
 print(df.tail(2))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
我们的数据帧是：
    Age   Name    Rating
0   25    Tom     4.23
1   26    James   3.24
2   25    Ricky   3.98
3   23    Vin     2.56
4   30    Steve   3.20
5   29    Smith   4.60
6   23    Jack    3.80

数据帧的最后两行是:
    Age   Name    Rating
5   29    Smith    4.6
6   23    Jack     3.8
```

