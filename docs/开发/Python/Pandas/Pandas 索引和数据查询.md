<font style="color:rgb(51, 51, 51);">Pandas 索引和数据查询的操作实例</font>

<font style="color:rgb(59, 69, 73);">在本章中，我们将讨论如何对日期进行切片和切块，并获得Pandas对象的子集。  
</font><font style="color:rgb(59, 69, 73);">Python和NumPy索引运算符“[]”和属性运算符“.”。可以在各种用例中快速轻松地访问Pandas数据结构。但是，由于事先不知道要访问的数据类型，因此直接使用标准运算符存在一些优化限制。对于生产代码，我们建议您利用本章中介绍的优化的熊猫数据访问方法。  
</font><font style="color:rgb(59, 69, 73);">Pandas现在支持三种类型的多轴索引：下表中提到了三种类型-</font>

| <font style="color:rgb(51, 51, 51);">索引</font> | <font style="color:rgb(51, 51, 51);">说明</font> |
| --- | --- |
| **<font style="color:rgb(51, 51, 51);">.loc()</font>** | <font style="color:rgb(51, 51, 51);">基于标签</font> |
| **<font style="color:rgb(51, 51, 51);">.iloc()</font>** | <font style="color:rgb(51, 51, 51);">基于整数</font> |
| **<font style="color:rgb(51, 51, 51);">.ix()</font>** | <font style="color:rgb(51, 51, 51);">基于标签和整数</font> |


## <font style="color:rgb(51, 51, 51);">.loc()</font>
<font style="color:rgb(59, 69, 73);">Pandas 提供了多种方法来具有纯粹基于标签的索引。切片时，还包括起始边界。整数是有效的标签，但它们引用的是标签而不是位置。</font>

**<font style="color:rgb(59, 69, 73);">.loc()</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">具有多种访问方法，例如：</font>

<font style="color:rgb(51, 51, 51);">一个标量标签</font><font style="color:rgb(51, 51, 51);">标签列表</font><font style="color:rgb(51, 51, 51);">切片对象</font><font style="color:rgb(51, 51, 51);">布尔数组</font>

**<font style="color:rgb(59, 69, 73);">loc</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">需要两个单/列表/范围运算符，以“，”分隔。第一个指示行，第二个指示列。</font>

### <font style="color:rgb(51, 51, 51);">案例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 导入pandas库并起别名pd
 import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4),
 index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
 # 选择特定列的所有行
 print(df.loc[:,'A'])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
a   0.391548
b  -0.070649
c  -0.317212
d  -2.162406
e   2.202797
f   0.613709
g   1.050559
h   1.122680
Name: A, dtype: float64
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4),
 index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
 # 为多个列选择所有行，比如list[]
 print(df.loc[:,['A','C']])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A           C
a    0.391548    0.745623
b   -0.070649    1.620406
c   -0.317212    1.448365
d   -2.162406   -0.873557
e    2.202797    0.528067
f    0.613709    0.286414
g    1.050559    0.216526
h    1.122680   -1.621420
```

### <font style="color:rgb(51, 51, 51);">实例 3</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 导入pandas库并起别名pd
 import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4),
 index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
 # 为多个列选择几行，比如list[]
 print(df.loc[['a','b','f','h'],['A','C']])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A          C
a   0.391548   0.745623
b  -0.070649   1.620406
f   0.613709   0.286414
h   1.122680  -1.621420
```

### <font style="color:rgb(51, 51, 51);">实例 4</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 导入pandas库并起别名pd
 import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4),
 index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
 # 为所有列选择行范围
 print(df.loc['a':'h'])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A           B          C          D
a    0.391548   -0.224297   0.745623   0.054301
b   -0.070649   -0.880130   1.620406   1.419743
c   -0.317212   -1.929698   1.448365   0.616899
d   -2.162406    0.614256  -0.873557   1.093958
e    2.202797   -2.315915   0.528067   0.612482
f    0.613709   -0.157674   0.286414  -0.500517
g    1.050559   -2.272099   0.216526   0.928449
h    1.122680    0.324368  -1.621420  -0.741470
```

### <font style="color:rgb(51, 51, 51);">实例 5</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 导入pandas库并起别名pd
 import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4),
 index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])
 # 用于使用布尔数组获取值
 print(df.loc['a']>0)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A  False
 B  True
 C  False
 D  False
 Name: a, dtype: bool
```

## <font style="color:rgb(51, 51, 51);">.iloc()</font>
<font style="color:rgb(59, 69, 73);">Pandas 提供了多种方法来获得纯粹基于整数的索引。像python和numpy一样，它们都是基于0的索引。  
</font><font style="color:rgb(59, 69, 73);">各种访问方法如下：</font>

<font style="color:rgb(51, 51, 51);">整数</font><font style="color:rgb(51, 51, 51);">整数列表</font><font style="color:rgb(51, 51, 51);">值范围</font>

### <font style="color:rgb(51, 51, 51);">实例1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 导入pandas库并起别名pd
 import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 # 选择特定列的所有行
 print(df.iloc[:4])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A          B           C           D
0   0.699435   0.256239   -1.270702   -0.645195
1  -0.685354   0.890791   -0.813012    0.631615
2  -0.783192  -0.531378    0.025070    0.230806
3   0.539042  -1.284314    0.826977   -0.026251
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 # 整数切片
 print(df.iloc[:4]
 print(df.iloc[1:5, 2:4])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A          B           C           D
0   0.699435   0.256239   -1.270702   -0.645195
1  -0.685354   0.890791   -0.813012    0.631615
2  -0.783192  -0.531378    0.025070    0.230806
3   0.539042  -1.284314    0.826977   -0.026251

           C          D
1  -0.813012   0.631615
2   0.025070   0.230806
3   0.826977  -0.026251
4   1.423332   1.130568
```

### <font style="color:rgb(51, 51, 51);">实例 3</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 # 对值列表进行切片
 print(df.iloc[[1, 3, 5], [1, 3]]
 print(df.iloc[1:3, :])
 print(df.iloc[:,1:3])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
B           D
1   0.890791    0.631615
3  -1.284314   -0.026251
5  -0.512888   -0.518930

           A           B           C           D
1  -0.685354    0.890791   -0.813012    0.631615
2  -0.783192   -0.531378    0.025070    0.230806

           B           C
0   0.256239   -1.270702
1   0.890791   -0.813012
2  -0.531378    0.025070
3  -1.284314    0.826977
4  -0.460729    1.423332
5  -0.512888    0.581409
6  -1.204853    0.098060
7  -0.947857    0.641358
```

## <font style="color:rgb(51, 51, 51);">.ix()</font>
<font style="color:rgb(59, 69, 73);">除了基于纯标签和基于整数的方法外，Pandas还提供了一种混合方法，用于使用.ix()运算符选择和子集对象。</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 # 整数切片
 print(df.ix[:4])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A          B           C           D
0   0.699435   0.256239   -1.270702   -0.645195
1  -0.685354   0.890791   -0.813012    0.631615
2  -0.783192  -0.531378    0.025070    0.230806
3   0.539042  -1.284314    0.826977   -0.026251
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 # 索引切片
 print(df.ix[:,'A'])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0   0.699435
1  -0.685354
2  -0.783192
3   0.539042
4  -1.044209
5  -1.415411
6   1.062095
7   0.994204
Name: A, dtype: float64
```

## <font style="color:rgb(51, 51, 51);">符号的使用</font>
<font style="color:rgb(59, 69, 73);">通过多轴索引从Pandas对象获取值使用以下符号：</font>

| <font style="color:rgb(51, 51, 51);">对象</font> | <font style="color:rgb(51, 51, 51);">索引器</font> | <font style="color:rgb(51, 51, 51);">返回类型</font> |
| --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">Series</font> | <font style="color:rgb(51, 51, 51);">s.loc[indexer]</font> | <font style="color:rgb(51, 51, 51);">标量值</font> |
| <font style="color:rgb(51, 51, 51);">DataFrame</font> | <font style="color:rgb(51, 51, 51);">df.loc[row_index,col_index]</font> | <font style="color:rgb(51, 51, 51);">Series 对象</font> |
| <font style="color:rgb(51, 51, 51);">Panel</font> | <font style="color:rgb(51, 51, 51);">p.loc[item_index,major_index, minor_index]</font> | <font style="color:rgb(51, 51, 51);">p.loc[item_index,major_index, minor_index]</font> |


<font style="color:rgb(59, 69, 73);">.iloc()和.ix()应用相同的索引选项和返回值。</font>

<font style="color:rgb(59, 69, 73);">我们看看如何对DataFrame对象执行每个操作。我们将使用基本索引运算符'[]'-</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 print(df['A'])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0  -0.478893
1   0.391931
2   0.336825
3  -1.055102
4  -0.165218
5  -0.328641
6   0.567721
7  -0.759399
Name: A, dtype: float64
```

<font style="color:rgb(59, 69, 73);">我们可以将值列表传递给[]以选择那些列</font>

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 print(df[['A','B']])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
A           B
0  -0.478893   -0.606311
1   0.391931   -0.949025
2   0.336825    0.093717
3  -1.055102   -0.012944
4  -0.165218    1.550310
5  -0.328641   -0.226363
6   0.567721   -0.312585
7  -0.759399   -0.372696
```

### <font style="color:rgb(51, 51, 51);">实例 3</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 print(df[2:2])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Columns: [A, B, C, D]
 Index: []
```

### <font style="color:rgb(51, 51, 51);">属性访问</font>
<font style="color:rgb(59, 69, 73);">可以使用属性运算符“。”选择列。</font>

### <font style="color:rgb(51, 51, 51);">实例</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
 print(df.A)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0   -0.478893
1    0.391931
2    0.336825
3   -1.055102
4   -0.165218
5   -0.328641
6    0.567721
7   -0.759399
Name: A, dtype: float64
```

