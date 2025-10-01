<font style="color:rgb(51, 51, 51);">Pandas 重建索引操作实例</font>

<font style="color:rgb(59, 69, 73);">要将您自己或其他库的函数应用于Pandas对象，您应该了解三个重要的方法。方法如下所述。要使用的适当方法取决于您的函数是希望对整个数据帧进行操作，还是行操作还是按列操作，还是按元素操作。</font>

<font style="color:rgb(51, 51, 51);">表函数应用程序：pipe()</font><font style="color:rgb(51, 51, 51);">行或列函数应用程序：apply()</font><font style="color:rgb(51, 51, 51);">元素级函数应用程序：applymap()</font>

## <font style="color:rgb(51, 51, 51);">表函数应用程序</font>
<font style="color:rgb(59, 69, 73);">可以通过传递函数和适当数量的参数作为管道参数来执行对DataFrame自定义操作</font>

### <font style="color:rgb(51, 51, 51);">加法器函数</font>
<font style="color:rgb(59, 69, 73);">例如，将2个值添加到DataFrame中。加法器功能将两个数字值相加并返回总和。</font>

```plain
def adder(ele1,ele2):
    return ele1+ele2
```

<font style="color:rgb(59, 69, 73);">我们使用自定义函数对DataFrame进行操作.</font>

```plain
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
 df.pipe(adder,2)
```

<font style="color:rgb(59, 69, 73);">我们看下完整的程序：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 def adder(ele1,ele2):
    return ele1+ele2
 df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
 df.pipe(adder,2)
 print(df.apply(np.mean))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 col2 col3
 0 2.176704 2.219691 1.509360
 1 2.222378 2.422167 3.953921
 2 2.241096 1.135424 2.696432
 3 2.355763 0.376672 1.182570
 4 2.308743 2.714767 2.130288
```

## <font style="color:rgb(51, 51, 51);">行或列函数应用程序</font>
<font style="color:rgb(59, 69, 73);">可以使用apply()方法沿DataFrame或Panel的轴应用任意函数，该方法与描述性统计方法一样，采用可选的axis参数。默认情况下，该操作按列执行，将每一列视为类似数组的形式。</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
 df.apply(np.mean)
 print(df.apply(np.mean))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 -0.288022
 col2 1.044839
 col3 -0.187009
 dtype: float64
```

<font style="color:rgb(59, 69, 73);">通过传递 axis 参数，可以逐行执行操作。</font>

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
 df.apply(np.mean,axis=1)
 print(df.apply(np.mean))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 0.034093
 col2 -0.152672
 col3 -0.229728
 dtype: float64
```

### <font style="color:rgb(51, 51, 51);">实例 3</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
 df.apply(lambda x: x.max() - x.min())
 print(df.apply(np.mean))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 -0.167413
 col2 -0.370495
 col3 -0.707631
 dtype: float64
```

## <font style="color:rgb(51, 51, 51);">元素级函数应用程序</font>
<font style="color:rgb(59, 69, 73);">并非所有函数都可以向量化（NumPy数组既不返回另一个数组，也不返回任何值），DataFrame上的applymap() 方法和Series上的map() 类似地接受任何采用单个值并返回单个值的Python函数。</font>

### <font style="color:rgb(51, 51, 51);">实例 1</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
 # 自定义函数
 df['col1'].map(lambda x:x*100)
 print(df.apply(np.mean))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 0.480742
 col2 0.454185
 col3 0.266563
 dtype: float64
```

### <font style="color:rgb(51, 51, 51);">实例 2</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 # 自定义函数
 df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
 df.applymap(lambda x:x*100)
 print(df.apply(np.mean))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
col1 0.395263
 col2 0.204418
 col3 -0.795188
 dtype: float64
```

