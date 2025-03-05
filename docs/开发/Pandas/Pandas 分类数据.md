# Pandas 分类数据
<font style="color:rgb(51, 51, 51);">Pandas 分类数据的操作实例</font>

<font style="color:rgb(59, 69, 73);">数据通常实时包含重复的文本列。性别，国家/地区和代码等功能始终是重复的。这些是分类数据的示例。 </font><font style="color:rgb(59, 69, 73);">分类变量只能采用有限的且通常是固定数量的可能值。除固定长度外，分类数据可能还具有顺序，但不能执行数字运算。分类是Pandas数据类型。</font>

<font style="color:rgb(59, 69, 73);">分类数据类型在以下情况下很有用</font>

<font style="color:rgb(59, 69, 73);">一个仅包含几个不同值的字符串变量。将这样的字符串变量转换为分类变量将节省一些内存。</font>

<font style="color:rgb(59, 69, 73);">变量的词汇顺序与逻辑顺序（“一个”，“两个”，“三个”）不同。通过转换为类别并在类别上指定顺序，排序和最小/最大将使用逻辑顺序而不是词汇顺序。</font>

<font style="color:rgb(59, 69, 73);">作为其他Python库的信号，此列应视为分类变量（例如，使用适当的统计方法或绘图类型）。</font>

## <font style="color:rgb(51, 51, 51);">对象创建</font>
<font style="color:rgb(59, 69, 73);">分类对象可以通过多种方式创建。下面描述了不同的方式：</font>

### <font style="color:rgb(51, 51, 51);">类别</font>
<font style="color:rgb(59, 69, 73);">通过在熊猫对象创建中将dtype指定为“ category”。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(["a","b","c","a"], dtype="category")
 print(s)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0 a
 1 b
 2 c
 3 a
 dtype: category
 Categories (3, object): [a, b, c]
```

<font style="color:rgb(59, 69, 73);">传递给series对象的元素数为4，但是类别仅为3。在输出类别中观察相同。</font>

### <font style="color:rgb(51, 51, 51);">pd.Categorical</font>
<font style="color:rgb(59, 69, 73);">使用标准的熊猫分类构造器，我们可以创建一个类别对象。</font>

pandas.Categorical(values, categories, ordered)

<font style="color:rgb(59, 69, 73);">我们看一个实例-</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
 print(cat)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
[a, b, c, a, b, c]
 Categories (3, object): [a, b, c]
```

<font style="color:rgb(59, 69, 73);">让我们再看一个实例</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
 print(cat)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
[a, b, c, a, b, c, NaN]
 Categories (3, object): [c, b, a]
```

<font style="color:rgb(59, 69, 73);">在这里，第二个参数表示类别。因此，类别中不存在的任何值都将被视为NaN。 </font><font style="color:rgb(59, 69, 73);">现在，看看以下示例：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
 print(cat)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
[a, b, c, a, b, c, NaN]
 Categories (3, object): [c < b < a]
```

<font style="color:rgb(59, 69, 73);">从逻辑上讲，该顺序意味着a大于b且b大于c。</font>

### <font style="color:rgb(51, 51, 51);">描述</font>
<font style="color:rgb(59, 69, 73);">使用.describe()的分类数据的命令，我们得到相似的输出到一个系列或数据框的的类型的字符串。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
 df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})
 print(df.describe())
 print(df["cat"].describe())
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
cat s
count    3 3
unique   2 2
top      c c
freq     2 2
count     3
unique    2
top       c
freq      2
Name: cat, dtype: object
```

### <font style="color:rgb(51, 51, 51);">获取分类的属性</font>
<font style="color:rgb(59, 69, 73);">obj.cat.categories命令用于获取对象的类别。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
 print(s.categories)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

  Index([u'b', u'a', u'c'], dtype='object')

<font style="color:rgb(59, 69, 73);">obj.ordered命令用于获取对象的顺序。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
 print(cat.ordered)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

   False

<font style="color:rgb(59, 69, 73);">该函数返回false，因为我们未指定任何顺序。</font>

### <font style="color:rgb(51, 51, 51);">重命名分类</font>
<font style="color:rgb(59, 69, 73);">重命名类别是通过向series.cat.categories series.cat.categories属性分配新值来完成的。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(["a","b","c","a"], dtype="category")
 s.cat.categories = ["Group %s" % g for g in s.cat.categories]
 print(s.cat.categories)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

Index([u'Group a', u'Group b', u'Group c'], dtype='object')

<font style="color:rgb(59, 69, 73);">初始类别[a，b，c]由对象的s.cat.categories属性更新。</font>

### <font style="color:rgb(51, 51, 51);">追加新类别</font>
<font style="color:rgb(59, 69, 73);">使用Categorical.add.categories()方法，可以追加新类别。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(["a","b","c","a"], dtype="category")
 s = s.cat.add_categories([4])
 print(s.cat.categories)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

Index([u'a', u'b', u'c', 4], dtype='object')

### <font style="color:rgb(51, 51, 51);">删除类别</font>
<font style="color:rgb(59, 69, 73);">使用Categorical.remove_categories()方法，可以删除不需要的类别。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(["a","b","c","a"], dtype="category")
 print(("Original object:"))
 print(s)
 print(("After removal:"))
 print(s.cat.remove_categories("a"))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
Original object:
 0 a
 1 b
 2 c
 3 a
 dtype: category
 Categories (3, object): [a, b, c]
 After removal:
 0 NaN
 1 b
 2 c
 3 NaN
 dtype: category
 Categories (2, object): [b, c]
```

### <font style="color:rgb(51, 51, 51);">分类数据比较</font>
<font style="color:rgb(59, 69, 73);">在三种情况下可以将分类数据与其他对象进行比较：</font>

<font style="color:rgb(59, 69, 73);">将等于（==和！=）与长度与分类数据相同的类似列表的对象（列表，序列，数组，...）进行比较。</font>

<font style="color:rgb(59, 69, 73);">当排序== True并且类别相同时，将类别数据与另一个类别系列的所有比较（==，！=，>，> =，  <和<=）。< div>    </font>

<font style="color:rgb(51, 51, 51);">分类数据与标量的所有比较。</font>

<font style="color:rgb(59, 69, 73);">看下面的实例：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 cat = pd.Series([1,2,3]).astype("category", categories=[1,2,3], ordered=True)
 cat1 = pd.Series([2,2,2]).astype("category", categories=[1,2,3], ordered=True)
 print(cat>cat1)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
0  False
 1  False
 2  True
 dtype: bool
```

# 
