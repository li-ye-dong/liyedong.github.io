# <font style="color:rgb(51, 51, 51);">Pandas 注意事项</font>
<font style="color:rgb(51, 51, 51);">Pandas 注意事项和陷阱</font>

## <font style="color:rgb(51, 51, 51);">在Pandas中使用If/Truth语句</font>
<font style="color:rgb(59, 69, 73);">当您使用布尔运算符if或when，or或or not，尝试将某些内容转换为bool时，有时会引发一个错误。错误是怎么发生的目前尚不清楚。Pandas提出了一个ValueError异常。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 if pd.Series([False, True, False]):
    print 'I am True'
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
ValueError: The truth value of a Series is ambiguous. 
 Use a.empty, a.bool() a.item(),a.any() or a.all().
```

<font style="color:rgb(59, 69, 73);">在这种情况下，不清楚该怎么处理。这个错误暗示了是使用None或是其中任何一个。.</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 if pd.Series([False, True, False]).any():
    print("I am any")
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

I am any

<font style="color:rgb(59, 69, 73);">要在布尔上下文中评估单元素Pandas对象，请使用.bool()方法-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print pd.Series([True]).bool()
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

True

### <font style="color:rgb(51, 51, 51);">位布尔值</font>
<font style="color:rgb(59, 69, 73);">像==和!之类的按位布尔运算符=将返回一个布尔序列，这几乎总是需要的。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(range(5))
 print s==4
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0 False
 1 False
 2 False
 3 False
 4 True
 dtype: bool
```

### <font style="color:rgb(51, 51, 51);">isin操作</font>
<font style="color:rgb(59, 69, 73);">这将返回一个布尔系列，显示布尔值中的每个元素是否完全包含在传递的值序列中。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(list('abc'))
 s = s.isin(['a', 'c', 'e'])
 print s
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0 True
 1 False
 2 True
 dtype: bool
```

### <font style="color:rgb(51, 51, 51);">重建索引 vs ix索引</font>
<font style="color:rgb(59, 69, 73);">许多用户会发现自己使用ix索引功能作为从Pandas对象中选择数据的一种简洁方法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
 'four'],index=list('abcdef'))
 print df
 print df.ix[['b', 'c', 'e']]
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one        two      three       four
a   -1.582025   1.335773   0.961417  -1.272084
b    1.461512   0.111372  -0.072225   0.553058
c   -1.240671   0.762185   1.511936  -0.630920
d   -2.380648  -0.029981   0.196489   0.531714
e    1.846746   0.148149   0.275398  -0.244559
f   -1.842662  -0.933195   2.303949   0.677641

          one        two      three       four
b    1.461512   0.111372  -0.072225   0.553058
c   -1.240671   0.762185   1.511936  -0.630920
e    1.846746   0.148149   0.275398  -0.244559
```

<font style="color:rgb(59, 69, 73);">当然，在这种情况下，这完全等同于使用reindex方法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
 'four'],index=list('abcdef'))
 print df
 print df.reindex(['b', 'c', 'e'])
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one        two      three       four
a    1.639081   1.369838   0.261287  -1.662003
b   -0.173359   0.242447  -0.494384   0.346882
c   -0.106411   0.623568   0.282401  -0.916361
d   -1.078791  -0.612607  -0.897289  -1.146893
e    0.465215   1.552873  -1.841959   0.329404
f    0.966022  -0.190077   1.324247   0.678064

          one        two      three       four
b   -0.173359   0.242447  -0.494384   0.346882
c   -0.106411   0.623568   0.282401  -0.916361
e    0.465215   1.552873  -1.841959   0.329404
```

<font style="color:rgb(59, 69, 73);">有人可能会得出结论，ix和reindex基于此是100％等效的。除了整数索引的情况外，都是如此。例如，上述操作可以代替地表示为：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randn(6, 4), columns=['one', 'two', 'three',
 'four'],index=list('abcdef'))
 print df
 print df.ix[[1, 2, 4]]
 print df.reindex([1, 2, 4])
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
one        two      three       four
a   -1.015695  -0.553847   1.106235  -0.784460
b   -0.527398  -0.518198  -0.710546  -0.512036
c   -0.842803  -1.050374   0.787146   0.205147
d   -1.238016  -0.749554  -0.547470  -0.029045
e   -0.056788   1.063999  -0.767220   0.212476
f    1.139714   0.036159   0.201912   0.710119

          one        two      three       four
b   -0.527398  -0.518198  -0.710546  -0.512036
c   -0.842803  -1.050374   0.787146   0.205147
e   -0.056788   1.063999  -0.767220   0.212476

    one  two  three  four
1   NaN  NaN    NaN   NaN
2   NaN  NaN    NaN   NaN
4   NaN  NaN    NaN   NaN
```

<font style="color:rgb(59, 69, 73);">重要的是要记住，重新索引仅是严格的标签索引。在索引包含例如整数和字符串的出错情况下，这可能导致某些可能令人意想不到的结果。</font>

