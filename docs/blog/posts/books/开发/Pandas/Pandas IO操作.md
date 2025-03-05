# <font style="color:rgb(51, 51, 51);">Pandas IO操作</font>
<font style="color:rgb(51, 51, 51);">Pandas IO操作实例</font>

<font style="color:rgb(59, 69, 73);">读取文本文件的两个主要功能是read_csv()和read_table()。他们都使用相同的解析代码将表格数据智能地转换为DataFrame对象：</font>

```plain
pandas.read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer',
 names=None, index_col=None, usecols=None
```

```plain
pandas.read_csv(filepath_or_buffer, sep='\t', delimiter=None, header='infer',
 names=None, index_col=None, usecols=None
```

<font style="color:rgb(59, 69, 73);">将此数据另存为temp.csv并对其进行操作。</font>

```plain
S.No,Name,Age,City,Salary
 1,Tom,28,Toronto,20000
 2,Lee,32,HongKong,3000
 3,Steven,43,Bay Area,8300
 4,Ram,38,Hyderabad,3900
```

## <font style="color:rgb(51, 51, 51);">read.csv</font>
<font style="color:rgb(59, 69, 73);">read.csv从csv文件读取数据并创建一个DataFrame对象。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 df=pd.read_csv("temp.csv")
 print df
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
S.No     Name   Age       City   Salary
0     1      Tom    28    Toronto    20000
1     2      Lee    32   HongKong     3000
2     3   Steven    43   Bay Area     8300
3     4      Ram    38  Hyderabad     3900
```

### <font style="color:rgb(51, 51, 51);">自定义索引</font>
<font style="color:rgb(59, 69, 73);">这将在csv文件中指定一列，以使用index_col自定义索引。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 df=pd.read_csv("temp.csv",index_col=['S.No'])
 print df
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
S.No   Name   Age       City   Salary
1       Tom    28    Toronto    20000
2       Lee    32   HongKong     3000
3    Steven    43   Bay Area     8300
4       Ram    38  Hyderabad     3900
```

### <font style="color:rgb(51, 51, 51);">转换器</font>
<font style="color:rgb(59, 69, 73);">列的dtype可以作为dict传递。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
 print df.dtypes
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
S.No       int64
Name      object
Age        int64
City      object
Salary   float64
dtype: object
```

<font style="color:rgb(59, 69, 73);">默认情况下，Salary列的dtype为int，但结果将其显示为float，因为我们已明确转换了类型。因此，数据看起来像float。</font>

<font style="color:rgb(59, 69, 73);">Thus, the data looks like float −</font>

```plain
S.No   Name   Age      City    Salary
0   1     Tom   28    Toronto   20000.0
1   2     Lee   32   HongKong    3000.0
2   3  Steven   43   Bay Area    8300.0
3   4     Ram   38  Hyderabad    3900.0
```

### <font style="color:rgb(51, 51, 51);">标题名称</font>
<font style="color:rgb(59, 69, 73);">使用names参数指定标题的名称。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
  
 df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e'])
 print df
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
a        b    c           d        e
0   S.No     Name   Age       City   Salary
1      1      Tom   28     Toronto    20000
2      2      Lee   32    HongKong     3000
3      3   Steven   43    Bay Area     8300
4      4      Ram   38   Hyderabad     3900
```

<font style="color:rgb(59, 69, 73);">请注意，标头名称后附加了自定义名称，但是文件中的标头尚未消除。现在，我们使用header参数将其删除。</font>

<font style="color:rgb(59, 69, 73);">如果标题不在第一行中，则将行号传递给标题。这将跳过前面的行。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd 
 df=pd.read_csv("temp.csv",names=['a','b','c','d','e'],header=0)
 print df
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
a        b    c           d        e
0  S.No     Name   Age       City   Salary
1     1      Tom   28     Toronto    20000
2     2      Lee   32    HongKong     3000
3     3   Steven   43    Bay Area     8300
4     4      Ram   38   Hyderabad     3900
```

### <font style="color:rgb(51, 51, 51);">skiprows</font>
<font style="color:rgb(59, 69, 73);">skiprows跳过指定的行数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 df=pd.read_csv("temp.csv", skiprows=2)
 print df
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
2      Lee   32    HongKong   3000
0   3   Steven   43    Bay Area   8300
1   4      Ram   38   Hyderabad   3900
```

# 
