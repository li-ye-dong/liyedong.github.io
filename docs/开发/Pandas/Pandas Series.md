<font style="color:rgb(51, 51, 51);">Pandas Series基本操作</font>

## <font style="color:rgb(51, 51, 51);">pandas.Series</font>
<font style="color:rgb(59, 69, 73);">Series结构如下：</font>

pandas.Series( data, index, dtype, copy)

<font style="color:rgb(59, 69, 73);">构造函数的参数如下-</font>

<font style="color:rgb(51, 51, 51);">data:数据采用各种形式，例如ndarray，list，常量</font><font style="color:rgb(51, 51, 51);">index:索引值必须是唯一且可哈希的，且长度与数据相同。如果未传递索引，则默认为np.arrange(n)。</font><font style="color:rgb(51, 51, 51);">dtype:dtype用于数据类型。如果为None，则将推断数据类型</font><font style="color:rgb(51, 51, 51);">copy:复制数据。默认为假</font>

<font style="color:rgb(59, 69, 73);">可以使用各种输入来创建Series，例如</font>

<font style="color:rgb(51, 51, 51);">Array</font><font style="color:rgb(51, 51, 51);">Dict</font><font style="color:rgb(51, 51, 51);">标量值或常数</font>

## <font style="color:rgb(51, 51, 51);">创建一个空Series</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
>>> # 导入pandas依赖包并起别名
 >>> import pandas as pd
 >>> s = pd.Series()
 >>> print(s)
 Series([], dtype: float64)
```

## <font style="color:rgb(51, 51, 51);">从ndarray创建Series</font>
<font style="color:rgb(59, 69, 73);">如果数据是ndarray，则传递的索引必须具有相同的长度。如果没有传递索引，则默认情况下索引将是range(n)，其中n是数组长度，即[0,1,2,3…。范围（len(array)）-1]。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 import numpy as np
 data = np.array(['a','b','c','d'])
 s = pd.Series(data)
 print(s)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 a
 1 b
 2 c
 3 d
 dtype: object
```

<font style="color:rgb(59, 69, 73);">我们没有传递任何索引，因此默认情况下，它分配的索引范围为0到len(data)-1，即0到3。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 import numpy as np
 data = np.array(['a','b','c','d'])
 s = pd.Series(data,index=[100,101,102,103])
 print(s)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
100 a
 101 b
 102 c
 103 d
 dtype: object
```

<font style="color:rgb(59, 69, 73);">我们在这里传递了索引值。现在，我们可以在输出中看到自定义的索引值。</font>

## <font style="color:rgb(51, 51, 51);">从字典创建Series</font>
<font style="color:rgb(59, 69, 73);">字典可以作为输入被传递，如果未指定索引，则该字典键都采取了在排序顺序来构建的索引。如果指数通过，在对应于索引标签数据的值将被拉出。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 import numpy as np
 data = {'a' : 0., 'b' : 1., 'c' : 2.}
 s = pd.Series(data)
 print(s)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
a 0.0
 b 1.0
 c 2.0
 dtype: float64
```

<font style="color:rgb(59, 69, 73);">字典键用于构造索引。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 import numpy as np
 data = {
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
b 1.0
 c 2.0
 d NaN
 a 0.0
 dtype: float64
```

<font style="color:rgb(59, 69, 73);">索引顺序保持不变，丢失的元素用NaN（非数字）填充。</font>

## <font style="color:rgb(51, 51, 51);">从标量创建Series</font>
<font style="color:rgb(59, 69, 73);">如果数据是标量值，则必须提供索引。该值将重复以匹配索引的长度</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 import numpy as np
 s = pd.Series(5, index=[0, 1, 2, 3])
 print(s)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 5
 1 5
 2 5
 3 5
 dtype: int64
```

## <font style="color:rgb(51, 51, 51);">从具有位置Series的访问数据</font>
<font style="color:rgb(59, 69, 73);">可以像访问ndarray一样访问Series中的数据。  
</font><font style="color:rgb(59, 69, 73);">检索第一个元素。众所周知，数组的计数从零开始，这意味着第一个元素存储在第零个位置，依此类推。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
 # 检索第一个数据
 print s[0]
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

1

<font style="color:rgb(59, 69, 73);">检索Series中的前三个元素。如果在其前面插入，则将从该索引开始的所有项目都将被提取。如果使用两个参数（它们之间带有：），则两个索引之间的项目（不包括停止索引）</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
 # 检索前3个元素
 print s[:3]
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
a 1
 b 2
 c 3
 dtype: int64
```

<font style="color:rgb(59, 69, 73);">检索最后三个元素。</font>

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
 # 检索最后三个元素
 print s[-3:]
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
c 3
 d 4
 e 5
 dtype: int64
```

## <font style="color:rgb(51, 51, 51);">使用标签（索引）检索数据</font>
<font style="color:rgb(59, 69, 73);">Series就像固定大小的字典一样，可以通过索引标签获取和设置值。  
</font><font style="color:rgb(59, 69, 73);">使用索引标签值检索单个元素。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 s = pd.Series([1,2,3,4,5],index = [
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

 1

<font style="color:rgb(59, 69, 73);">使用索引标签值列表检索多个元素。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 s = pd.Series([1,2,3,4,5],index = [
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
a 1
 c 3
 d 4
 dtype: int64
```

<font style="color:rgb(59, 69, 73);">如果不包含标签，则会引发异常。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# Filename : pandas.py
 # author by : www.cainiaoplus.com 
 # 导入pandas依赖包并起别名
 import pandas as pd
 s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
 # 检索多个元素
 print(s['f'])
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
…
 KeyError: 'f'
```

