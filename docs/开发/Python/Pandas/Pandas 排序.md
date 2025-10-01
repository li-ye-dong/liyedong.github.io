<font style="color:rgb(59, 69, 73);">Pandas的排序方式有两种：</font>

<font style="color:rgb(51, 51, 51);">按 标签</font><font style="color:rgb(51, 51, 51);">按实际值</font>

<font style="color:rgb(59, 69, 73);">我们看一个下面的示例。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
 mns=['col2','col1'])
 print(unsorted_df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col2       col1
1  -2.063177   0.537527
4   0.142932  -0.684884
6   0.012667  -0.389340
2  -0.548797   1.848743
3  -1.044160   0.837381
5   0.385605   1.300185
9   1.031425  -1.002967
8  -0.407374  -0.435142
0   2.237453  -1.067139
7  -1.445831  -1.701035
```

<font style="color:rgb(59, 69, 73);">在unsorted_df中，标签和值未排序。让我们看看如何对它们进行排序。</font>

## <font style="color:rgb(51, 51, 51);">按标签排序</font>
<font style="color:rgb(59, 69, 73);">使用sort_index()方法，通过传递轴参数和排序顺序，可以对DataFrame进行排序。默认情况下，按升序对行标签进行排序。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
    mns = ['col2','col1'])
 sorted_df=unsorted_df.sort_index()
 print(sorted_df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col2        col1
9    0.825697    0.374463
8   -1.699509    0.510373
7   -0.581378    0.622958
6   -0.202951    0.954300
5   -1.289321   -1.551250
4    1.302561    0.851385
3   -0.157915   -0.388659
2   -1.222295    0.166609
1    0.584890   -0.291048
0    0.668444   -0.061294
```

### <font style="color:rgb(51, 51, 51);">排序的顺序</font>
<font style="color:rgb(59, 69, 73);">通过将布尔值传递给升序参数，可以控制排序的顺序。让我们考虑以下示例以了解相同的情况。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
    mns = ['col2','col1'])
 sorted_df = unsorted_df.sort_index(ascending=False)
 print(sorted_df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col2        col1
9    0.825697    0.374463
8   -1.699509    0.510373
7   -0.581378    0.622958
6   -0.202951    0.954300
5   -1.289321   -1.551250
4    1.302561    0.851385
3   -0.157915   -0.388659
2   -1.222295    0.166609
1    0.584890   -0.291048
0    0.668444   -0.061294
```

### <font style="color:rgb(51, 51, 51);">按行排序</font>
<font style="color:rgb(59, 69, 73);">通过将轴参数传递给值0或1，可以在列标签上进行排序。默认情况下，axis = 0 按行排序。让我们考虑以下示例以了解相同的情况。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
  
 unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
    mns = ['col2','col1'])
  
 sorted_df=unsorted_df.sort_index(axis=1)
 print(sorted_df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1        col2
1   -0.291048    0.584890
4    0.851385    1.302561
6    0.954300   -0.202951
2    0.166609   -1.222295
3   -0.388659   -0.157915
5   -1.551250   -1.289321
9    0.374463    0.825697
8    0.510373   -1.699509
0   -0.061294    0.668444
7    0.622958   -0.581378
```

### <font style="color:rgb(51, 51, 51);">按值排序</font>
<font style="color:rgb(59, 69, 73);">与索引排序类似，sort_values()是按值排序的方法。它接受一个“ by”参数，该参数将使用要对值进行排序的DataFrame的列名。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
    sorted_df = unsorted_df.sort_values(by='col1')
 print(sorted_df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1  col2
1    1    3
2    1    2
3    1    4
0    2    1
```

<font style="color:rgb(59, 69, 73);">注意，col1值已排序，并且相应的col2值和行索引将与col1一起更改。因此，它们看起来没有分类。</font>

**<font style="color:rgb(59, 69, 73);">'by'</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">参数采用列值列表。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
    sorted_df = unsorted_df.sort_values(by=['col1','col2'])
 print(sorted_df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 col2
2   1   2
1   1   3
3   1   4
0   2   1
```

## <font style="color:rgb(51, 51, 51);">排序算法</font>
**<font style="color:rgb(59, 69, 73);">sort_values()</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">提供了从mergesort，heapsort和quicksort中选择算法的指定。Mergesort是唯一稳定的算法。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
 sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')
 print(sorted_df)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 col2
1    1    3
2    1    2
3    1    4
0    2    1
```

