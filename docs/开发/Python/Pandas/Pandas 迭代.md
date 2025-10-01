<font style="color:rgb(59, 69, 73);">在Pandas对象上进行基本迭代的行为取决于类型。在Series上进行迭代时，它等同于数组。其他数据结构（例如DataFrame和Panel）遵循类似dict的语法，即在对象的键上进行迭代。</font>

<font style="color:rgb(59, 69, 73);">In short, basic iteration (for</font><font style="color:rgb(59, 69, 73);"> </font>**<font style="color:rgb(59, 69, 73);">i</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">in object) produces −</font>

**<font style="color:rgb(51, 51, 51);">Series</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 值</font>**<font style="color:rgb(51, 51, 51);">DataFrame</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 列标签</font>**<font style="color:rgb(51, 51, 51);">Panel</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− item 标签</font>

## <font style="color:rgb(51, 51, 51);">DataFrame迭代</font>
<font style="color:rgb(59, 69, 73);">迭代DataFrame会给出列名。我们看看以下示例。</font>

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
 for col in df:
    print col
```

<font style="color:rgb(59, 69, 73);">其输出如下</font>

```plain
A
 C
 D
 x
 y
```

<font style="color:rgb(59, 69, 73);">要遍历DataFrame的行，我们可以使用以下函数-</font>

**<font style="color:rgb(51, 51, 51);">iteritems()</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 迭代（键，值）对</font>**<font style="color:rgb(51, 51, 51);">iterrows()</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 以(index,series)对的形式遍历行</font>**<font style="color:rgb(51, 51, 51);">itertuples()</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">− 以namedtuples的形式遍历行</font>

## <font style="color:rgb(51, 51, 51);">iteritems()</font>
<font style="color:rgb(59, 69, 73);">遍历每列作为键，将带有标签的值对作为键，将列值作为Series对象。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
  import numpy as np
  
  
  
 df = pd.
  DataFrame(np.
  random.randn(4,3),columns=[
  'col1',
  'col2',
  'col3'])
  
 
  for key,value
   in df.
  iteritems():
  
    print key,value
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 0    0.802390
1    0.324060
2    0.256811
3    0.839186
Name: col1, dtype: float64

col2 0    1.624313
1   -1.033582
2    1.796663
3    1.856277
Name: col2, dtype: float64

col3 0   -0.022142
1   -0.230820
2    1.160691
3   -0.830279
Name: col3, dtype: float64
```

<font style="color:rgb(59, 69, 73);">可以看出每一列作为系列中的键值对分别进行迭代。</font>

## <font style="color:rgb(51, 51, 51);">iterrows()</font>
<font style="color:rgb(59, 69, 73);">iterrows() 返回产生每个索引值以及包含每一行数据的序列的迭代器。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
 for row_index,row in df.iterrows():
    print row_index,row
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0  col1    1.529759
   col2    0.762811
   col3   -0.634691
Name: 0, dtype: float64

1  col1   -0.944087
   col2    1.420919
   col3   -0.507895
Name: 1, dtype: float64
 
2  col1   -0.077287
   col2   -0.858556
   col3   -0.663385
Name: 2, dtype: float64
3  col1    -1.638578
   col2     0.059866
   col3     0.493482
Name: 3, dtype: float64
```

<font style="color:rgb(59, 69, 73);">由于iterrows()遍历行，因此不会保留行中的数据类型。0,1,2是行索引，col1，col2，col3是列索引。</font>

## <font style="color:rgb(51, 51, 51);">itertuples()</font>
<font style="color:rgb(59, 69, 73);">itertuples()方法将返回一个迭代器，为DataFrame中的每一行生成一个命名的元组。元组的第一个元素将是行的相应索引值，而其余值是行值。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
 for row in df.itertuples():
     print row
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Pandas(Index=0, col1=1.5297586201375899, col2=0.76281127433814944, col3=-
0.6346908238310438)

Pandas(Index=1, col1=-0.94408735763808649, col2=1.4209186418359423, col3=-
0.50789517967096232)

Pandas(Index=2, col1=-0.07728664756791935, col2=-0.85855574139699076, col3=-
0.6633852507207626)

Pandas(Index=3, col1=0.65734942534106289, col2=-0.95057710432604969,
col3=0.80344487462316527)
```

<font style="color:rgb(51, 51, 51);">注意：</font><font style="color:rgb(51, 51, 51);">请勿在迭代时尝试修改任何对象。迭代用于读取，迭代器返回原始对象（视图）的副本，因此更改不会反映在原始对象上。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
 for index, row in df.iterrows():
    row['a'] = 10
 print df
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1       col2       col3
0  -1.739815   0.735595  -0.295589
1   0.635485   0.106803   1.527922
2  -0.939064   0.547095   0.038585
3  -1.016509  -0.116580  -0.523158
```

<font style="color:rgb(51, 51, 51);">观察，没有反映出任何变化。</font>

