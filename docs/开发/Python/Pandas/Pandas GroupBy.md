# <font style="color:rgb(51, 51, 51);">Pandas GroupBy</font>
<font style="color:rgb(51, 51, 51);">Pandas GroupBy的操作实例</font>

<font style="color:rgb(59, 69, 73);">任何groupby操作都会对原始对象进行以下操作：</font>

<font style="color:rgb(51, 51, 51);">拆分对象</font><font style="color:rgb(51, 51, 51);">应用函数</font><font style="color:rgb(51, 51, 51);">合并结果</font>

<font style="color:rgb(59, 69, 73);">在许多情况下，我们将数据分成几组，然后在每个子集上应用一些功能。在Apply功能中，我们可以执行以下操作-</font>

**<font style="color:rgb(51, 51, 51);">聚合</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 计算汇总统计</font>**<font style="color:rgb(51, 51, 51);">转换</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 分组操作</font>**<font style="color:rgb(51, 51, 51);">过滤</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 在某些条件下过滤数据</font>

<font style="color:rgb(59, 69, 73);">现在我们创建一个DataFrame对象并对其执行所有操作。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
#import the pandas library
 import pandas as pd
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 print(df)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Points   Rank     Team   Year
0      876      1   Riders   2014
1      789      2   Riders   2015
2      863      2   Devils   2014
3      673      3   Devils   2015
4      741      3    Kings   2014
5      812      4    kings   2015
6      756      1    Kings   2016
7      788      1    Kings   2017
8      694      2   Riders   2016
9      701      4   Royals   2014
10     804      1   Royals   2015
11     690      2   Riders   2017
```

## <font style="color:rgb(51, 51, 51);">将数据分成组</font>
<font style="color:rgb(59, 69, 73);">象可以拆分为任何对象。有多种分割对象的方法，例如：</font>

<font style="color:rgb(51, 51, 51);">obj.groupby('key')</font><font style="color:rgb(51, 51, 51);">obj.groupby(['key1','key2'])</font><font style="color:rgb(51, 51, 51);">obj.groupby(key,axis=1)</font>

<font style="color:rgb(59, 69, 73);">现在我们看看如何将分组对象应用于DataFrame对象</font>

### <font style="color:rgb(51, 51, 51);">实例</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 print(df.groupby('Team'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain

```

## <font style="color:rgb(51, 51, 51);">查看组</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 print(df.groupby('Team').groups)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
{'Kings': Int64Index([4, 6, 7], dtype='int64'),
 'Devils': Int64Index([2, 3], dtype='int64'),
 'Riders': Int64Index([0, 1, 8, 11], dtype='int64'),
 'Royals': Int64Index([9, 10], dtype='int64'),
 'kings' : Int64Index([5], dtype='int64')}
```

### <font style="color:rgb(51, 51, 51);">实例</font>
<font style="color:rgb(59, 69, 73);">用多列分组</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 print(df.groupby(['Team','Year']).groups)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
{('Kings', 2014): Int64Index([4], dtype='int64'),
  ('Royals', 2014): Int64Index([9], dtype='int64'),
  ('Riders', 2014): Int64Index([0], dtype='int64'),
  ('Riders', 2015): Int64Index([1], dtype='int64'),
  ('Kings', 2016): Int64Index([6], dtype='int64'),
  ('Riders', 2016): Int64Index([8], dtype='int64'),
  ('Riders', 2017): Int64Index([11], dtype='int64'),
  ('Devils', 2014): Int64Index([2], dtype='int64'),
  ('Devils', 2015): Int64Index([3], dtype='int64'),
  ('kings', 2015): Int64Index([5], dtype='int64'),
  ('Royals', 2015): Int64Index([10], dtype='int64'),
  ('Kings', 2017): Int64Index([7], dtype='int64')}
```

## <font style="color:rgb(51, 51, 51);">遍历组</font>
<font style="color:rgb(59, 69, 73);">有了groupby对象，我们可以类似于itertools.obj遍历该对象。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 grouped = df.groupby('Year')
 for name,group in grouped:
    print(name)
    print(group)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
2014
   Points  Rank     Team   Year
0     876     1   Riders   2014
2     863     2   Devils   2014
4     741     3   Kings    2014
9     701     4   Royals   2014

2015
   Points  Rank     Team   Year
1     789     2   Riders   2015
3     673     3   Devils   2015
5     812     4    kings   2015
10    804     1   Royals   2015

2016
   Points  Rank     Team   Year
6     756     1    Kings   2016
8     694     2   Riders   2016

2017
   Points  Rank    Team   Year
7     788     1   Kings   2017
11    690     2  Riders   2017
```

<font style="color:rgb(59, 69, 73);">默认情况下，groupby对象的标签名称与组名称相同。</font>

## <font style="color:rgb(51, 51, 51);">选择组p</font>
<font style="color:rgb(59, 69, 73);">使用get_group()方法，我们可以选择一个组。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 grouped = df.groupby('Year')
 print(grouped.get_group(2014))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Points  Rank     Team    Year
0     876     1   Riders    2014
2     863     2   Devils    2014
4     741     3   Kings     2014
9     701     4   Royals    2014
```

## <font style="color:rgb(51, 51, 51);">集合体</font>
<font style="color:rgb(59, 69, 73);">聚合函数为每个组返回一个聚合值。一旦通过组对象被创建，几个聚合操作可以在分组的数据来执行。</font>

<font style="color:rgb(59, 69, 73);">一个明显的方法是通过合计或等效的agg方法进行合计。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 import numpy as np
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 grouped = df.groupby('Year')
 print(grouped['Points'].agg(np.mean))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Year
2014   795.25
2015   769.50
2016   725.00
2017   739.00
Name: Points, dtype: float64
```

<font style="color:rgb(59, 69, 73);">查看每个组的大小的另一种方法是通过应用size()函数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 Attribute Access in Python Pandas
 grouped = df.groupby('Team')
 print(grouped.agg(np.size))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Points   Rank   Year
Team
Devils        2      2      2
Kings         3      3      3
Riders        4      4      4
Royals        2      2      2
kings         1      1      1
```

### <font style="color:rgb(51, 51, 51);">一次应用多个聚合功能</font>
<font style="color:rgb(59, 69, 73);">借助分组的Series，您还可以传递函数的列表或字典来进行聚合，并生成DataFrame作为输出-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 import numpy as np
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 grouped = df.groupby('Team')
 print(grouped['Points'].agg([np.sum, np.mean, np.std]))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Team      sum      mean          std
Devils   1536   768.000000   134.350288
Kings    2285   761.666667    24.006943
Riders   3049   762.250000    88.567771
Royals   1505   752.500000    72.831998
kings     812   812.000000          NaN
```

## <font style="color:rgb(51, 51, 51);">转换</font>
<font style="color:rgb(59, 69, 73);">在组或列上进行转换将返回一个索引，该索引的大小与正在分组的对象的大小相同。因此，转换应返回与组块大小相同的结果。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# import the pandas library
 import pandas as pd
 import numpy as np
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 grouped = df.groupby('Team')
 score = lambda x: (x - x.mean()) / x.std()*10
 print(grouped.transform(score))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Points        Rank        Year
0   12.843272  -15.000000  -11.618950
1   3.020286     5.000000   -3.872983
2   7.071068    -7.071068   -7.071068
3  -7.071068     7.071068    7.071068
4  -8.608621    11.547005  -10.910895
5        NaN          NaN         NaN
6  -2.360428    -5.773503    2.182179
7  10.969049    -5.773503    8.728716
8  -7.705963     5.000000    3.872983
9  -7.071068     7.071068   -7.071068
10  7.071068    -7.071068    7.071068
11 -8.157595     5.000000   11.618950
```

## <font style="color:rgb(51, 51, 51);">过滤</font>
<font style="color:rgb(59, 69, 73);">过滤根据定义的条件过滤数据并返回数据的子集。所述过滤器()函数是用来筛选数据。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
    'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
    'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
    'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
    'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
 df = pd.DataFrame(ipl_data)
 print(df.groupby('Team').filter(lambda x: len(x) >= 3))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Points  Rank     Team   Year
0      876     1   Riders   2014
1      789     2   Riders   2015
4      741     3   Kings    2014
6      756     1   Kings    2016
7      788     1   Kings    2017
8      694     2   Riders   2016
11     690     2   Riders   2017
```

# 
