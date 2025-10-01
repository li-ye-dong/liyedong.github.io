**<font style="color:rgb(59, 69, 73);">重建索引</font>**<font style="color:rgb(59, 69, 73);"> 会更改DataFrame的行标签和列标签。重新索引是指使数据与特定轴上的一组给定标签匹配。</font>

<font style="color:rgb(59, 69, 73);">通过索引可以完成多个操作，例如-</font>

<font style="color:rgb(51, 51, 51);">重新排序现有数据以匹配一组新标签。</font><font style="color:rgb(51, 51, 51);">在标签数据不存在的标签位置中插入缺失值(NA)标记。</font>

### <font style="color:rgb(51, 51, 51);">实例：</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 N=20
 df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
 })
 # DataFrame重建索引
 df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
 print(df_reindexed)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A    C     B
0  2016-01-01  Low   NaN
2  2016-01-03  High  NaN
5  2016-01-06  Low   NaN
```

## <font style="color:rgb(51, 51, 51);">重新索引以与其他对象对齐</font>
<font style="color:rgb(59, 69, 73);">您可能希望获取一个对象并为其轴重新索引，使其标记为与另一个对象相同。考虑以下示例以了解相同的内容。</font>

### <font style="color:rgb(51, 51, 51);">Example</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
 df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
 df1 = df1.reindex_like(df2)
 print(df1)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1         col2         col3
0    -2.467652    -1.211687    -0.391761
1    -0.287396     0.522350     0.562512
2    -0.255409    -0.483250     1.866258
3    -1.150467    -0.646493    -0.222462
4     0.152768    -2.056643     1.877233
5    -1.155997     1.528719    -1.343719
6    -1.015606    -1.245936    -0.295275
```

<font style="color:rgb(59, 69, 73);">在这里，df1 DataFrame像df2一样被更改和重新索引。列名称应匹配，否则将为整个列标签添加NAN。</font>

## <font style="color:rgb(51, 51, 51);">重新索引时填充</font>
**<font style="color:rgb(59, 69, 73);">reindex()</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">采用可选参数方法，这是一种填充方法，其值如下</font>

**<font style="color:rgb(59, 69, 73);">pad/ffill</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− 向前填充值</font>

**<font style="color:rgb(59, 69, 73);">bfill/backfill</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− 向后填充值</font>

**<font style="color:rgb(59, 69, 73);">nearest</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− 从最接近的索引值填充</font>

### <font style="color:rgb(51, 51, 51);">实例</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
 df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
 # 填充 NAN
 print df2.reindex_like(df1)
 # 现在用前面的值填充NAN
 print("带前向填充的数据帧:")
 print(df2.reindex_like(df1,method='ffill'))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1        col2       col3
0    1.311620   -0.707176   0.599863
1   -0.423455   -0.700265   1.133371
2         NaN         NaN        NaN
3         NaN         NaN        NaN
4         NaN         NaN        NaN
5         NaN         NaN        NaN

带前向填充的数据帧:
         col1        col2        col3
0    1.311620   -0.707176    0.599863
1   -0.423455   -0.700265    1.133371
2   -0.423455   -0.700265    1.133371
3   -0.423455   -0.700265    1.133371
4   -0.423455   -0.700265    1.133371
5   -0.423455   -0.700265    1.133371
```

<font style="color:rgb(59, 69, 73);">最后四行被填充。</font>

## <font style="color:rgb(51, 51, 51);">重新编制索引时的填充限制</font>
<font style="color:rgb(59, 69, 73);">limit参数为重新索引时的填充提供了额外的控制。限制指定连续匹配的最大数量。让我们考虑以下示例以了解相同的内容-</font>

### <font style="color:rgb(51, 51, 51);">实例</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
 df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
 # 填充 NAN
 print df2.reindex_like(df1)
 # 现在用前面的值填充NAN print("前向填充限制为1的数据帧:")
 print(df2.reindex_like(df1,method='ffill',limit=1))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1        col2        col3
0    0.247784    2.128727    0.702576
1   -0.055713   -0.021732   -0.174577
2         NaN         NaN         NaN
3         NaN         NaN         NaN
4         NaN         NaN         NaN
5         NaN         NaN         NaN

前向填充限制为1的数据帧:
         col1        col2        col3
0    0.247784    2.128727    0.702576
1   -0.055713   -0.021732   -0.174577
2   -0.055713   -0.021732   -0.174577
3         NaN         NaN         NaN
4         NaN         NaN         NaN
5         NaN         NaN         NaN
```

<font style="color:rgb(59, 69, 73);">请注意，前面的第六行仅填充了第七行。然后，各行保持原样。</font>

## <font style="color:rgb(51, 51, 51);">重命名</font>
<font style="color:rgb(59, 69, 73);">通过rename()方法，您可以基于某些映射（字典或系列）或任意函数来重新标记轴。    
</font><font style="color:rgb(59, 69, 73);">让我们考虑以下示例以了解这一点-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
 print df1
 print ("重命名行和列之后:")
 print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
 index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1        col2        col3
0    0.486791    0.105759    1.540122
1   -0.990237    1.007885   -0.217896
2   -0.483855   -1.645027   -1.194113
3   -0.122316    0.566277   -0.366028
4   -0.231524   -0.721172   -0.112007
5    0.438810    0.000225    0.435479

重命名行和列之后:
                c1          c2        col3
apple     0.486791    0.105759    1.540122
banana   -0.990237    1.007885   -0.217896
durian   -0.483855   -1.645027   -1.194113
3        -0.122316    0.566277   -0.366028
4        -0.231524   -0.721172   -0.112007
5         0.438810    0.000225    0.435479
```

