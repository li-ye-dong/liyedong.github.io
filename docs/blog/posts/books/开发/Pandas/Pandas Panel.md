<font style="color:rgb(51, 51, 51);">Pandas Panel基本操作</font>

<font style="color:rgb(59, 69, 73);">Panel数据3D容器. 术语</font><font style="color:rgb(59, 69, 73);"> </font>**<font style="color:rgb(59, 69, 73);">Panel data</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">源自计量经济学，名称来之于pandas −</font><font style="color:rgb(59, 69, 73);"> </font>**<font style="color:rgb(59, 69, 73);">pan(el)-da(ta)</font>**<font style="color:rgb(59, 69, 73);">-s.</font>

<font style="color:rgb(59, 69, 73);">3个轴的名称描述如下- −</font>

**<font style="color:rgb(59, 69, 73);">items</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− 轴0，每个items都对应一个包含在其中的DataFrame。</font>

**<font style="color:rgb(59, 69, 73);">major_axis</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− 轴1，它是每个DataFrame的索引（行）。</font>

**<font style="color:rgb(59, 69, 73);">minor_axis</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">− 轴2，它是每个DataFrame的列。</font>

## <font style="color:rgb(51, 51, 51);">pandas.Panel()</font>
<font style="color:rgb(59, 69, 73);">面板可以使用以下构造函数创建- −</font>

 pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)

<font style="color:rgb(59, 69, 73);">构造函数的参数如下：</font>

| <font style="color:rgb(51, 51, 51);">参数</font> | <font style="color:rgb(51, 51, 51);">描述</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">data</font> | <font style="color:rgb(51, 51, 51);">数据采用各种形式，例如ndarray，series，map，list，dict，常量以及DataFrame</font> |
| <font style="color:rgb(51, 51, 51);">items</font> | <font style="color:rgb(51, 51, 51);">axis=0</font> |
| <font style="color:rgb(51, 51, 51);">major_axis</font> | <font style="color:rgb(51, 51, 51);">axis=1</font> |
| <font style="color:rgb(51, 51, 51);">minor_axis</font> | <font style="color:rgb(51, 51, 51);">axis=2</font> |
| <font style="color:rgb(51, 51, 51);">dtype</font> | <font style="color:rgb(51, 51, 51);">每列的数据类型</font> |
| <font style="color:rgb(51, 51, 51);">copy</font> | <font style="color:rgb(51, 51, 51);">复制数据。默认</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">false</font>** |


## <font style="color:rgb(51, 51, 51);">创建 Panel</font>
<font style="color:rgb(59, 69, 73);">面板可以使用多种方式创建，例如：</font>

<font style="color:rgb(51, 51, 51);">从 ndarrays 创建</font><font style="color:rgb(51, 51, 51);">从 DataFrame的字典创建</font>

### <font style="color:rgb(51, 51, 51);">从ndarrays创建</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 创建一个空panel
 import pandas as pd
 import numpy as np
 data = np.random.rand(2,4,5)
 p = pd.Panel(data)
 print(p)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
<class 'pandas.core.panel.Panel'>
 Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
 Items axis: 0 to 1
 Major_axis axis: 0 to 3
 Minor_axis axis: 0 to 4
```

### <font style="color:rgb(51, 51, 51);">从 DataFrame的字典创建</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 创建一个空panel
 
  import pandas
   as pd  
 
  import numpy
   as np  
 data = {
  'Item1' : pd.
  DataFrame(np.
  random.randn(4, 3)), 
  
    
  'Item2' : pd.
  DataFrame(np.
  random.randn(4, 2))}  
 p = pd.
  Panel(data)  
 print(p)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
 Items axis: Item1 to Item2
 Major_axis axis: 0 to 3
 Minor_axis axis: 0 to 2
```

### <font style="color:rgb(51, 51, 51);">创建一个空Panel</font>
<font style="color:rgb(59, 69, 73);">可以使用Panel构造函数创建一个空面板，如下所示：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 创建一个空panel
 import pandas as pd
 p = pd.Panel()
 print(p)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
<class 'pandas.core.panel.Panel'>
 Dimensions: 0 (items) x 0 (major_axis) x 0 (minor_axis)
 Items axis: None
 Major_axis axis: None
 Minor_axis axis: None
```

## <font style="color:rgb(51, 51, 51);">从Panel中查询数据</font>
<font style="color:rgb(59, 69, 73);">可以用以下三项从panel中查询数据：</font>

<font style="color:rgb(51, 51, 51);">Items</font><font style="color:rgb(51, 51, 51);">Major_axis</font><font style="color:rgb(51, 51, 51);">Minor_axis</font>

### <font style="color:rgb(51, 51, 51);">用 Items查询</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 创建一个空panel
 import pandas as pd
 import numpy as np
 data = {
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0         1        2
 0 0.488224 -0.128637 0.930817
 1 0.417497 0.896681 0.576657
 2 -2.775266 0.571668 0.290082
 3 -0.400538 -0.144234 1.110535
```

<font style="color:rgb(59, 69, 73);">从两个item中查询item1，输出的结果是一个具有4行3列的DataFrame，分别是Major_axis和Minor_axis。</font>

### <font style="color:rgb(51, 51, 51);">用major_axis查询</font>
<font style="color:rgb(59, 69, 73);">可以使用panel.major_axis(index)方法访问数据.</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 创建一个空panel
 import pandas as pd
 import numpy as np
 data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
    'Item2' : pd.DataFrame(np.random.randn(4, 2))}
 p = pd.Panel(data)
 print(p.major_xs(1))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Item1 Item2
 0 0.417497 0.748412
 1 0.896681 -0.557322
 2 0.576657 NaN
```

### <font style="color:rgb(51, 51, 51);">用 minor_axis查询</font>
<font style="color:rgb(59, 69, 73);">可以使用panel.minor_axis(index)方法访问数据。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
# 创建一个空panel
 import pandas as pd
 import numpy as np
 data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
    'Item2' : pd.DataFrame(np.random.randn(4, 2))}
 p = pd.Panel(data)
 print(p.minor_xs(1))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Item1 Item2
 0 -0.128637 -1.047032
 1 0.896681 -0.557322
 2 0.571668 0.431953
 3 -0.144234 1.302466
```

