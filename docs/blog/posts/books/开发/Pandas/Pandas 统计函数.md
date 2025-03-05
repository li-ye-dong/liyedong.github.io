<font style="color:rgb(51, 51, 51);">Pandas 统计函数的操作实例</font>

<font style="color:rgb(59, 69, 73);">统计方法有助于理解和分析数据的行为。现在，我们将学习一些统计函数，可以将它们应用于Pandas对象。</font>

## <font style="color:rgb(51, 51, 51);">百分比变化</font>
<font style="color:rgb(59, 69, 73);">Series，DatFrames和Panel都具有功能pct_change()。此函数将每个元素与其先前的元素进行比较，并计算更改百分比。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series([1,2,3,4,5,4])
 print(s.pct_change()
 df = pd.DataFrame(np.random.randn(5, 2))
 print(df.pct_change())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0        NaN
1   1.000000
2   0.500000
3   0.333333
4   0.250000
5  -0.200000
dtype: float64

          0          1
0         NaN        NaN
1  -15.151902   0.174730
2  -0.746374   -1.449088
3  -3.582229   -3.165836
4   15.601150  -1.860434
```

<font style="color:rgb(59, 69, 73);">默认情况下，pct_change()对列进行操作；如果要明智地应用同一行，请使用axis = 1()参数。</font>

## <font style="color:rgb(51, 51, 51);">协方差</font>
<font style="color:rgb(59, 69, 73);">协方差应用于序列数据。系列对象具有方法cov来计算系列对象之间的协方差。NA将被自动排除。</font>

### <font style="color:rgb(51, 51, 51);">Cov Series</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s1 = pd.Series(np.random.randn(10))
 s2 = pd.Series(np.random.randn(10))
 print(s1.cov(s2))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

   -0.12978405324

<font style="color:rgb(59, 69, 73);">将协方差方法应用于DataFrame时，将计算所有列之间的cov。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
 print(frame['a'].cov(frame['b']))
 print(frame.cov())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
-0.58312921152741437

           a           b           c           d            e
a   1.780628   -0.583129   -0.185575    0.003679    -0.136558
b  -0.583129    1.297011    0.136530   -0.523719     0.251064
c  -0.185575    0.136530    0.915227   -0.053881    -0.058926
d   0.003679   -0.523719   -0.053881    1.521426    -0.487694
e  -0.136558    0.251064   -0.058926   -0.487694     0.960761
```

<font style="color:rgb(59, 69, 73);">观察第一条语句中a和b列之间的cov值，这与cov在DataFrame上返回的值相同。</font>

## <font style="color:rgb(51, 51, 51);">相关性</font>
<font style="color:rgb(59, 69, 73);">相关性显示任意两个值数组（序列）之间的线性关系。有多种计算相关性的方法，例如pearson（默认），spearman和kendall。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
 print(frame['a'].corr(frame['b']))
 print(frame.corr())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
-0.383712785514

           a          b          c          d           e
a   1.000000  -0.383713  -0.145368   0.002235   -0.104405
b  -0.383713   1.000000   0.125311  -0.372821    0.224908
c  -0.145368   0.125311   1.000000  -0.045661   -0.062840
d   0.002235  -0.372821  -0.045661   1.000000   -0.403380
e  -0.104405   0.224908  -0.062840  -0.403380    1.000000
```

<font style="color:rgb(59, 69, 73);">如果DataFrame中存在任何非数字列，则会自动将其排除。</font>

## <font style="color:rgb(51, 51, 51);">数据排名</font>
<font style="color:rgb(59, 69, 73);">数据排名对元素数组中的每个元素进行排名。如果是平局，则分配平均排名。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))
 s['d'] = s['b'] # so there's a tie
 print(s.rank())
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
a  1.0
b  3.5
c  2.0
d  3.5
e  5.0
dtype: float64
```

<font style="color:rgb(59, 69, 73);">Rank可以选择将参数升序，默认情况下为true；如果为false，则对数据进行反向排名，将较大的值分配为较小的排名。</font>

<font style="color:rgb(59, 69, 73);">Rank支持使用method参数：</font>

**<font style="color:rgb(51, 51, 51);">average</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 并列组的平均等级。</font>**<font style="color:rgb(51, 51, 51);">min</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 组中最低的排名。</font>**<font style="color:rgb(51, 51, 51);">max</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 组中最高等级。</font>**<font style="color:rgb(51, 51, 51);">first</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 行列分配在它们出现的数组中的顺序。</font>

<font style="color:rgb(133, 144, 166);background-color:rgb(251, 251, 251);">  
</font>

