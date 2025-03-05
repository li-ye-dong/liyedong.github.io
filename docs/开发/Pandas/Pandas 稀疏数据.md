# <font style="color:rgb(51, 51, 51);">Pandas 稀疏数据</font>
<font style="color:rgb(51, 51, 51);">Pandas 稀疏数据操作实例</font>

<font style="color:rgb(59, 69, 73);">当省略与特定值（NaN /缺失值，尽管可以选择任何值）匹配的任何数据时，稀疏对象将被“压缩”。一个特殊的SparseIndex对象跟踪数据被“分散”的位置。在一个示例中，这将更加有意义。所有标准的Pandas数据结构都应用to_sparse方法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 ts = pd.Series(np.random.randn(10))
 ts[2:-2] = np.nan
 sts = ts.to_sparse()
 print sts
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0 -0.810497
 1 -1.419954
 2 NaN
 3 NaN
 4 NaN
 5 NaN
 6 NaN
 7 NaN
 8 0.439240
 9 -1.095910
 dtype: float64
 BlockIndex
 Block locations: array([0, 8], dtype=int32)
 Block lengths: array([2, 2], dtype=int32)
```

<font style="color:rgb(59, 69, 73);">出于内存效率的原因，存在稀疏对象。 </font><font style="color:rgb(59, 69, 73);">现在让我们假设您有一个很大的NA DataFrame并执行以下代码-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(10000, 4))
 df.ix[:9998] = np.nan
 sdf = df.to_sparse()
 print sdf.density
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```python
   0.0001
```

<font style="color:rgb(59, 69, 73);">可以通过调用to_dense将任何稀疏对象转换回标准密集形式</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 ts = pd.Series(np.random.randn(10))
 ts[2:-2] = np.nan
 sts = ts.to_sparse()
 print sts.to_dense()
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0 -0.810497
 1 -1.419954
 2 NaN
 3 NaN
 4 NaN
 5 NaN
 6 NaN
 7 NaN
 8 0.439240
 9 -1.095910
 dtype: float64
```

## <font style="color:rgb(51, 51, 51);">稀疏数据类型</font>
<font style="color:rgb(59, 69, 73);">稀疏数据应具有与其密集表示相同的dtype。当前，支持float64，int64和booldtypes。取决于原始dtype，fill_value默认更改-</font>

**<font style="color:rgb(59, 69, 73);">float64</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− np.nan</font>

**<font style="color:rgb(59, 69, 73);">int64</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− 0</font>

**<font style="color:rgb(59, 69, 73);">bool</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− False</font>

<font style="color:rgb(59, 69, 73);">下面我们执行以下代码来了解它们：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series([1, np.nan, np.nan])
 print s
 s.to_sparse()
 print s
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0 1.0
 1 NaN
 2 NaN
 dtype: float64
 0 1.0
 1 NaN
 2 NaN
 dtype: float64
```

# 
