<font style="color:rgb(51, 51, 51);">Pandas SQL操作的具体实例</font>

<font style="color:rgb(59, 69, 73);">由于许多潜在的Pandas用户都对SQL有所了解，因此本页面旨在提供一些示例说明如何使用Pandas执行各种SQL操作。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 url = 'https://raw.github.com/pandasdev/
 pandas/master/pandas/tests/data/tips.csv'
 tips=pd.read_csv(url)
 print tips.head()
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
total_bill   tip      sex  smoker  day     time  size
0        16.99  1.01   Female      No  Sun  Dinner      2
1        10.34  1.66     Male      No  Sun  Dinner      3
2        21.01  3.50     Male      No  Sun  Dinner      3
3        23.68  3.31     Male      No  Sun  Dinner      2
4        24.59  3.61   Female      No  Sun  Dinner      4
```

## <font style="color:rgb(51, 51, 51);">查询</font>
<font style="color:rgb(59, 69, 73);">在SQL中，选择是使用您选择的列的逗号分隔列表（或使用*来选择所有列）来完成的：</font>

```plain
SELECT total_bill, tip, smoker, time
 from tips
 LIMIT 5;
```

<font style="color:rgb(59, 69, 73);">使用Pandas，通过将列名称列表传递到DataFrame来完成列选择：</font>

 tips[['total_bill', 'tip', 'smoker', 'time']].head(5)

<font style="color:rgb(59, 69, 73);">让我们看一个完整的实例：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 url = 'https://raw.github.com/pandasdev/
 pandas/master/pandas/tests/data/tips.csv'
  
 tips=pd.read_csv(url)
 print tips[['total_bill', 'tip', 'smoker', 'time']].head(5)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
total_bill   tip  smoker     time
0       16.99  1.01      No   Dinner
1       10.34  1.66      No   Dinner
2       21.01  3.50      No   Dinner
3       23.68  3.31      No   Dinner
4       24.59  3.61      No   Dinner
```

<font style="color:rgb(59, 69, 73);">调用不带列名列表的DataFrame将显示所有列（类似于SQL的*）。</font>

## <font style="color:rgb(51, 51, 51);">WHERE条件查询</font>
<font style="color:rgb(59, 69, 73);">通过WHERE子句在SQL中进行过滤。</font>

 SELECT * from tips WHERE time = 'Dinner' LIMIT 5;

<font style="color:rgb(59, 69, 73);">DataFrame可以通过多种方式进行过滤。最直观的方法是使用布尔索引。</font>

 tips[tips['time'] == 'Dinner'].head(5)

<font style="color:rgb(59, 69, 73);">我们来看一个完整的实例</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 url = 'https://raw.github.com/pandasdev/
 pandas/master/pandas/tests/data/tips.csv'
 tips=pd.read_csv(url)
 print tips[tips['time'] == 'Dinner'].head(5)
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
total_bill   tip      sex  smoker  day    time  size
0       16.99  1.01   Female     No   Sun  Dinner    2
1       10.34  1.66     Male     No   Sun  Dinner    3
2       21.01  3.50     Male     No   Sun  Dinner    3
3       23.68  3.31     Male     No   Sun  Dinner    2
4       24.59  3.61   Female     No   Sun  Dinner    4
```

<font style="color:rgb(59, 69, 73);">上面的语句将一系列True / False对象传递给DataFrame，并返回所有带有True的行。</font>

## <font style="color:rgb(51, 51, 51);">GroupBy分组</font>
<font style="color:rgb(59, 69, 73);">此操作获取整个数据集中每个组中的记录数。例如查询性别分组和数量：</font>

```plain
SELECT sex, count(*)
 from tips
 GROUP BY sex;
```

<font style="color:rgb(59, 69, 73);">在Pandas是如下操作：</font>

 tips.groupby('sex').size()

<font style="color:rgb(59, 69, 73);">我们来看一个完整的实例</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 url = 'https://raw.github.com/pandasdev/
 pandas/master/pandas/tests/data/tips.csv'
 tips=pd.read_csv(url)
 print tips.groupby('sex').size()
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
sex
 Female 87
 Male 157
 dtype: int64
```

## <font style="color:rgb(51, 51, 51);">查询N行数量</font>
<font style="color:rgb(59, 69, 73);">SQL 使用LIMIT返回N行：</font>

```plain
SELECT * from tips
 LIMIT 5 ;
```

<font style="color:rgb(59, 69, 73);">在Pandas中操作如下：</font>

 tips.head(5)

<font style="color:rgb(59, 69, 73);">我们来看一个完整的实例</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv'
 tips=pd.read_csv(url)
 tips = tips[['smoker', 'day', 'time']].head(5)
 print tips
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
smoker   day     time
0      No   Sun   Dinner
1      No   Sun   Dinner
2      No   Sun   Dinner
3      No   Sun   Dinner
4      No   Sun   Dinner
```

