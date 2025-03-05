<font style="color:rgb(51, 51, 51);">Pandas 文本处理操作实例</font>

<font style="color:rgb(59, 69, 73);">在本章中，我们将使用基本的Series / Index讨论字符串操作。在随后的章节中，我们将学习如何在DataFrame上应用这些字符串函数。</font>

<font style="color:rgb(59, 69, 73);">Pandas提供了一组字符串函数，可以轻松地对字符串数据进行操作。最重要的是，这些函数忽略（或排除）缺少的/ NaN值。</font>

<font style="color:rgb(59, 69, 73);">几乎所有这些方法都可用于Python字符串函数（请参阅：</font><font style="color:rgb(59, 69, 73);"> </font>[<font style="color:rgb(59, 69, 73);">https://docs.python.org/3/library/stdtypes.html#string-methods</font>](https://docs.python.org/3/library/stdtypes.html#string-methods)<font style="color:rgb(59, 69, 73);">)。因此，将Series对象转换为String对象，然后执行该操作。</font>

<font style="color:rgb(59, 69, 73);">我们看看每个操作如何执行。</font>

| <font style="color:rgb(51, 51, 51);">方法</font> | <font style="color:rgb(51, 51, 51);">说明</font> |
| --- | --- |
| **<font style="color:rgb(51, 51, 51);">lower()</font>** | <font style="color:rgb(51, 51, 51);">将系列/索引中的字符串转换为小写。</font> |
| **<font style="color:rgb(51, 51, 51);">upper()</font>** | <font style="color:rgb(51, 51, 51);">将系列/索引中的字符串转换为大写。</font> |
| **<font style="color:rgb(51, 51, 51);">len()</font>** | <font style="color:rgb(51, 51, 51);">计算字符串length()。</font> |
| **<font style="color:rgb(51, 51, 51);">strip()</font>** | <font style="color:rgb(51, 51, 51);">帮助从两侧从系列/索引中的每个字符串中去除空格（包括换行符）。</font> |
| **<font style="color:rgb(51, 51, 51);">split(' ')</font>** | <font style="color:rgb(51, 51, 51);">用给定的模式分割每个字符串。</font> |
| **<font style="color:rgb(51, 51, 51);">cat(sep=' ')</font>**<font style="color:rgb(51, 51, 51);">/td></font> | <font style="color:rgb(51, 51, 51);">用给定的分隔符连接系列/索引元素。</font> |
| **<font style="color:rgb(51, 51, 51);">get_dummies()</font>** | <font style="color:rgb(51, 51, 51);">返回具有一键编码值的DataFrame。</font> |
| **<font style="color:rgb(51, 51, 51);">contains(pattern)</font>** | <font style="color:rgb(51, 51, 51);">如果子字符串包含在元素中，则为每个元素返回一个布尔值True，否则返回False。</font> |
| **<font style="color:rgb(51, 51, 51);">replace(a,b)</font>** | <font style="color:rgb(51, 51, 51);">a值替换成b。</font> |
| **<font style="color:rgb(51, 51, 51);">repeat(value)</font>** | <font style="color:rgb(51, 51, 51);">以指定的次数重复每个元素。</font> |
| **<font style="color:rgb(51, 51, 51);">count(pattern)</font>** | <font style="color:rgb(51, 51, 51);">返回每个元素中模式出现的次数。</font> |
| **<font style="color:rgb(51, 51, 51);">startswith(pattern)</font>** | <font style="color:rgb(51, 51, 51);">如果系列/索引中的元素以模式开头，则返回true。</font> |
| **<font style="color:rgb(51, 51, 51);">endswith(pattern)</font>** | <font style="color:rgb(51, 51, 51);">如果系列/索引中的元素以模式结尾，则返回true。</font> |
| **<font style="color:rgb(51, 51, 51);">find(pattern)</font>** | <font style="color:rgb(51, 51, 51);">返回模式首次出现的第一个位置。</font> |
| **<font style="color:rgb(51, 51, 51);">findall(pattern)</font>** | <font style="color:rgb(51, 51, 51);">返回所有出现的模式的列表。</font> |
| **<font style="color:rgb(51, 51, 51);">swapcase</font>** | <font style="color:rgb(51, 51, 51);">大小写互换</font> |
| **<font style="color:rgb(51, 51, 51);">islower()</font>**<font style="color:rgb(51, 51, 51);"><</font> | <font style="color:rgb(51, 51, 51);">检查“系列/索引”中每个字符串中的所有字符是否都小写。返回布尔值</font> |
| **<font style="color:rgb(51, 51, 51);">isupper()</font>** | <font style="color:rgb(51, 51, 51);">检查“系列/索引”中每个字符串中的所有字符是否都大写。返回布尔值。</font> |
| **<font style="color:rgb(51, 51, 51);">isnumeric()</font>** | <font style="color:rgb(51, 51, 51);">检查“系列/索引”中每个字符串中的所有字符是否都是数字。返回布尔值。</font> |


<font style="color:rgb(59, 69, 73);">我们来创建一个Series，看看以上所有功能如何工作。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
 print s
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 Tom
 1 William Rick
 2 John
 3 Alber@t
 4 NaN
 5 1234
 6 Steve Smith
 dtype: object
```

### <font style="color:rgb(51, 51, 51);">lower()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
 print s.str.lower()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 tom
 1 william rick
 2 john
 3 alber@t
 4 NaN
 5 1234
 6 steve smith
 dtype: object
```

### <font style="color:rgb(51, 51, 51);">upper()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
 print s.str.upper()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 TOM
 1 WILLIAM RICK
 2 JOHN
 3 ALBER@T
 4 NaN
 5 1234
 6 STEVE SMITH
 dtype: object
```

### <font style="color:rgb(51, 51, 51);">len()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveSmith'])
 print s.str.len()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 3.0
 1 12.0
 2 4.0
 3 7.0
 4 NaN
 5 4.0
 6 10.0
 dtype: float64
```

### <font style="color:rgb(51, 51, 51);">strip()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s
 print ("After Stripping:")
 print s.str.strip()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 Tom
 1 William Rick
 2 John
 3 Alber@t
 dtype: object
 After Stripping:
 0 Tom
 1 William Rick
 2 John
 3 Alber@t
 dtype: object
```

### <font style="color:rgb(51, 51, 51);">split(pattern)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s
 print ("Split Pattern:")
 print s.str.split(' ')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 Tom
 1 William Rick
 2 John
 3 Alber@t
 dtype: object
 Split Pattern:
 0 [Tom, , , , , , , , , , ]
 1 [, , , , , William, Rick]
 2 [John]
 3 [Alber@t]
 dtype: object
```

### <font style="color:rgb(51, 51, 51);">cat(sep=pattern)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s.str.cat(sep='_')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

   Tom _ William Rick_John_Alber@t

### <font style="color:rgb(51, 51, 51);">get_dummies()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 import numpy as np
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s.str.get_dummies()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
William Rick   Alber@t   John   Tom
0             0         0      0     1
1             1         0      0     0
2             0         0      1     0
3             0         1      0     0
```

### <font style="color:rgb(51, 51, 51);">contains ()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s.str.contains(' ')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0  True
 1  True
 2  False
 3  False
 dtype: bool
```

### <font style="color:rgb(51, 51, 51);">replace(a,b)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s
 print ("After replacing @ with $:")
 print s.str.replace('@',')
 )
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 Tom
 1 William Rick
 2 John
 3 Alber@t
 dtype: object
 After replacing @ with $:
 0 Tom
 1 William Rick
 2 John
 3 Alber$t
 dtype: object
```

### <font style="color:rgb(51, 51, 51);">repeat(value)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s.str.repeat(2)
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0   Tom            Tom
1   William Rick   William Rick
2                  JohnJohn
3                  Alber@tAlber@t
dtype: object
```

### <font style="color:rgb(51, 51, 51);">count(pattern)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
  
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print ("每个字符串中的“ m”数:")
 print s.str.count('m')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
每个字符串中的“ m”数:
 0 1
 1 1
 2 0
 3 0
```

### <font style="color:rgb(51, 51, 51);">startswith(pattern)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print ("Strings that start with 'T':")
 print s.str. startswith ('T')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0  True
 1  False
 2  False
 3  False
 dtype: bool
```

### <font style="color:rgb(51, 51, 51);">endswith(pattern)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print ("Strings that end with 't':")
 print s.str.endswith('t')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
Strings that end with 't':
 0  False
 1  False
 2  False
 3  True
 dtype: bool
```

### <font style="color:rgb(51, 51, 51);">find(pattern)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s.str.find('e')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 -1
 1 -1
 2 -1
 3 3
 dtype: int64
```

<font style="color:rgb(59, 69, 73);">“ -1”表示元素中没有匹配到。</font>

### <font style="color:rgb(51, 51, 51);">findall(pattern)</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
 print s.str.findall('e')
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 []
 1 []
 2 []
 3 [e]
 dtype: object
```

<font style="color:rgb(59, 69, 73);">空列表（[]）表示元素中没有匹配到</font>

### <font style="color:rgb(51, 51, 51);">swapcase()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
 print s.str.swapcase()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0 tOM
 1 wILLIAM rICK
 2 jOHN
 3 aLBER@T
 dtype: object
```

### <font style="color:rgb(51, 51, 51);">islower()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
 print s.str.islower()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0  False
 1  False
 2  False
 3  False
 dtype: bool
```

### <font style="color:rgb(51, 51, 51);">isupper()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
 print s.str.isupper()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0  False
 1  False
 2  False
 3  False
 dtype: bool
```

### <font style="color:rgb(51, 51, 51);">isnumeric()</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
 print s.str.isnumeric()
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
0  False
 1  False
 2  False
 3  False
 dtype: bool
```

