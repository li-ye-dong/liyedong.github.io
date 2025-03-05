<font style="color:rgb(51, 51, 51);">Pandas 描述性统计操作实例</font>

<font style="color:rgb(59, 69, 73);">DataFrame用在大量的计算描述性信息统计和其他相关操作。其中大多数是聚合，例如sum()，mean()，但其中一些聚合（例如sumsum()）会产生相同大小的对象。一般而言，这些方法采用轴参数，就像ndarray。{sum，std，...}一样，但是可以通过名称或整数指定轴</font><font style="color:rgb(51, 51, 51);">DataFrame − 索引 (axis=0, default), 列 (axis=1)</font>

<font style="color:rgb(51, 51, 51);">我们来创建一个DataFrame并在本章中使用此对象进行所有操作。</font>

### 实例
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建一个series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
 # 创建一个DataFrame
 df = pd.DataFrame(d)
 print(df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Age  Name   Rating
0   25   Tom     4.23
1   26   James   3.24
2   25   Ricky   3.98
3   23   Vin     2.56
4   30   Steve   3.20
5   29   Smith   4.60
6   23   Jack    3.80
7   34   Lee     3.78
8   40   David   2.98
9   30   Gasper  4.80
10  51   Betina  4.10
11  46   Andres  3.65
```

### sum()
<font style="color:rgb(59, 69, 73);">返回所请求轴的值之和。默认情况下，轴为索引（轴=0）</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 #创建一个Series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
 #创建一个DataFrame
 df = pd.DataFrame(d)
 print(df.sum())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Age                                                    382
Name     TomJamesRickyVinSteveSmithJackLeeDavidGasperBe...
Rating                                               44.92
dtype: object
```

<font style="color:rgb(59, 69, 73);">每个单独的列都添加了字符串</font>

### axis=1
<font style="color:rgb(59, 69, 73);">此语法将输出以下内容。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 # 创建一个series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
  
 #创建一个DataFrame
 df = pd.DataFrame(d)
 print(df.sum(1))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0    29.23
1    29.24
2    28.98
3    25.56
4    33.20
5    33.60
6    26.80
7    37.78
8    42.98
9    34.80
10   55.10
11   49.65
dtype: float64
```

### mean()
<font style="color:rgb(59, 69, 73);">返回平均值</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建一个series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
 #创建一个DataFrame
 df = pd.DataFrame(d)
 print(df.mean())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Age       31.833333
Rating     3.743333
dtype: float64
```

### std()
<font style="color:rgb(59, 69, 73);">返回数值列的Bressel标准偏差。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建一个series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
 #创建一个DataFrame
 df = pd.DataFrame(d)
 print(df.std())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Age       9.232682
Rating    0.661628
dtype: float64
```

## Functions & Description
<font style="color:rgb(59, 69, 73);">现在我们来了解Python Pandas中描述性统计信息下的功能。下表列出了重要功能：</font>

| <font style="color:rgb(51, 51, 51);">编号</font> | <font style="color:rgb(51, 51, 51);">方法</font> | <font style="color:rgb(51, 51, 51);">描述</font> |
| --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">1</font> | <font style="color:rgb(51, 51, 51);">count()</font> | <font style="color:rgb(51, 51, 51);">非空数</font> |
| <font style="color:rgb(51, 51, 51);">2</font> | <font style="color:rgb(51, 51, 51);">sum()</font> | <font style="color:rgb(51, 51, 51);">总数</font> |
| <font style="color:rgb(51, 51, 51);">3</font> | <font style="color:rgb(51, 51, 51);">mean()</font> | <font style="color:rgb(51, 51, 51);">平均数</font> |
| <font style="color:rgb(51, 51, 51);">4</font> | <font style="color:rgb(51, 51, 51);">median()</font> | <font style="color:rgb(51, 51, 51);">中位数</font> |
| <font style="color:rgb(51, 51, 51);">5</font> | <font style="color:rgb(51, 51, 51);">mode()</font> | <font style="color:rgb(51, 51, 51);">模式</font> |
| <font style="color:rgb(51, 51, 51);">6</font> | <font style="color:rgb(51, 51, 51);">std()</font> | <font style="color:rgb(51, 51, 51);">标准差</font> |
| <font style="color:rgb(51, 51, 51);">7</font> | <font style="color:rgb(51, 51, 51);">min()</font> | <font style="color:rgb(51, 51, 51);">最低值</font> |
| <font style="color:rgb(51, 51, 51);">8</font> | <font style="color:rgb(51, 51, 51);">max()</font> | <font style="color:rgb(51, 51, 51);">最大值</font> |
| <font style="color:rgb(51, 51, 51);">9</font> | <font style="color:rgb(51, 51, 51);">abs()</font> | <font style="color:rgb(51, 51, 51);">绝对值</font> |
| <font style="color:rgb(51, 51, 51);">10</font> | <font style="color:rgb(51, 51, 51);">prod()</font> | <font style="color:rgb(51, 51, 51);">乘积</font> |
| <font style="color:rgb(51, 51, 51);">11</font> | <font style="color:rgb(51, 51, 51);">cumsum()</font> | <font style="color:rgb(51, 51, 51);">累加</font> |
| <font style="color:rgb(51, 51, 51);">12</font> | <font style="color:rgb(51, 51, 51);">cumprod()</font> | <font style="color:rgb(51, 51, 51);">累乘</font> |


<font style="color:rgb(51, 51, 51);">注意：</font><font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 由于DataFrame是异构数据结构。泛型运算并不适用于所有功能。</font>

<font style="color:rgb(51, 51, 51);">诸如sum()，cumsum()之类的函数可用于数字和字符（或）字符串数据元素，而不会出现任何错误。虽然字符集合从不普遍使用，但不会抛出任何异常。</font><font style="color:rgb(51, 51, 51);">当DataFrame包含字符或字符串数据时，诸如abs()，cumprod()之类的函数将引发异常，因为此类操作无法执行。</font>

## 汇总数据
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建一个series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
 #创建一个DataFrame
 df = pd.DataFrame(d)
 print(df.describe())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Age         Rating
count    12.000000      12.000000
mean     31.833333       3.743333
std       9.232682       0.661628
min      23.000000       2.560000
25%      25.000000       3.230000
50%      29.500000       3.790000
75%      35.500000       4.132500
max      51.000000       4.800000
```

<font style="color:rgb(59, 69, 73);">此函数提供平均值，std和IQR值。并且，函数不包括字符列和有关数字列的给定摘要。“ include”是用于传递有关汇总时需要考虑哪些列的必要信息的参数。取值列表；默认情况下为“数字”。</font>

**<font style="color:rgb(51, 51, 51);">object</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 汇总字符串列</font>**<font style="color:rgb(51, 51, 51);">number</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 汇总数字列</font>**<font style="color:rgb(51, 51, 51);">all</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 总结所有列在一起（不应该把它作为一个列表值）</font>

<font style="color:rgb(59, 69, 73);">下面我们在程序中使用以下语句并执行并输出：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建一个series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
 #创建一个DataFrame
 df = pd.DataFrame(d)
 print(df.describe(include=['object']))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Name
count       12
unique      12
top      Ricky
freq         1
```

<font style="color:rgb(59, 69, 73);">下面我们在程序中使用以下语句并执行并输出：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 创建一个series字典
 d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
    'Lee','David','Gasper','Betina','Andres']),
    'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
 }
 #创建一个DataFrame
 df = pd.DataFrame(d)
 print(df. describe(include='all'))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Age          Name       Rating
count   12.000000        12    12.000000
unique        NaN        12          NaN
top           NaN     Ricky          NaN
freq          NaN         1          NaN
mean    31.833333       NaN     3.743333
std      9.232682       NaN     0.661628
min     23.000000       NaN     2.560000
25%     25.000000       NaN     3.230000
50%     29.500000       NaN     3.790000
75%     35.500000       NaN     4.132500
max     51.000000       NaN     4.800000
```

