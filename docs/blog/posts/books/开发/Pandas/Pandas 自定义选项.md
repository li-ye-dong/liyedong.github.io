<font style="color:rgb(51, 51, 51);">Pandas 自定义选项操作实例</font>

<font style="color:rgb(59, 69, 73);">Pandas因为提供了API来自定义行为，所以被广泛使用。  
</font><font style="color:rgb(59, 69, 73);">自定义API中有五个相关功如下：</font>

<font style="color:rgb(51, 51, 51);">get_option()</font><font style="color:rgb(51, 51, 51);">set_option()</font><font style="color:rgb(51, 51, 51);">reset_option()</font><font style="color:rgb(51, 51, 51);">describe_option()</font><font style="color:rgb(51, 51, 51);">option_context()</font>

<font style="color:rgb(59, 69, 73);">下面我们一起了解下这些方法。</font>

## <font style="color:rgb(51, 51, 51);">get_option(param)</font>
<font style="color:rgb(59, 69, 73);">get_option接受一个参数并输出以下值：</font>

### <font style="color:rgb(51, 51, 51);">display.max_rows</font>
<font style="color:rgb(59, 69, 73);">显示默认值的数量。解释器读取该值，并以该值作为显示上限显示行。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 print(pd.get_option("display.max_rows"))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

    60

### <font style="color:rgb(51, 51, 51);">display.max_columns</font>
<font style="color:rgb(59, 69, 73);">显示默认值的数量。解释器读取该值，并以该值作为显示上限显示行。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 print(pd.get_option("display.max_columns"))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

    20

<font style="color:rgb(59, 69, 73);">此处，60和20是默认配置参数值。</font>

## <font style="color:rgb(51, 51, 51);">set_option(param,value)</font>
<font style="color:rgb(59, 69, 73);">set_option接受两个参数并将值设置为参数，如下所示：</font>

### <font style="color:rgb(51, 51, 51);">display.max_rows</font>
<font style="color:rgb(59, 69, 73);">使用set_option()，我们可以更改要显示的默认行数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 pd.set_option("display.max_rows",80)
 print(pd.get_option("display.max_rows"))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

    80

### <font style="color:rgb(51, 51, 51);">display.max_columns</font>
<font style="color:rgb(59, 69, 73);">使用set_option()，我们可以更改要显示的默认行数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 pd.set_option("display.max_columns",30)
 print(pd.get_option("display.max_columns"))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

    30

## <font style="color:rgb(51, 51, 51);">reset_option(param)</font>
**<font style="color:rgb(59, 69, 73);">reset_option</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">接受一个参数并将其设置回默认值。</font>

### <font style="color:rgb(51, 51, 51);">display.max_rows</font>
<font style="color:rgb(59, 69, 73);">使用reset_option()，我们可以将值更改回要显示的默认行数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 pd.reset_option("display.max_rows")
 print(pd.get_option("display.max_rows"))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

    60

## <font style="color:rgb(51, 51, 51);">describe_option(param)</font>
**<font style="color:rgb(59, 69, 73);">describe_option</font>**<font style="color:rgb(59, 69, 73);"> </font><font style="color:rgb(59, 69, 73);">打印参数的描述</font>

### <font style="color:rgb(51, 51, 51);">display.max_rows</font>
<font style="color:rgb(59, 69, 73);">使用reset_option()，我们可以将值更改回要显示的默认行数。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 pd.describe_option("display.max_rows")
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
display.max_rows : int
    if max_rows is exceeded, switch to truncate view. Depending on
    'large_repr', objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.
    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print(a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 60] [currently: 60]
```

## <font style="color:rgb(51, 51, 51);">option_context()</font>
<font style="color:rgb(59, 69, 73);">option_context上下文管理器用于临时设置with语句中的选项。当您退出with块时，选项值会自动恢复。</font>

### <font style="color:rgb(51, 51, 51);">display.max_rows</font>
<font style="color:rgb(59, 69, 73);">使用option_context()，我们可以临时设置值。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 with pd.option_context("display.max_rows",10):
    print(pd.get_option("display.max_rows"))
    print(pd.get_option("display.max_rows"))
```

<font style="color:rgb(59, 69, 73);">运行结果：</font>

```plain
10
 10
```

<font style="color:rgb(59, 69, 73);">请参阅第一个和第二个打印语句之间的差异。第一条语句打印由option_context()设置的值，该值在with上下文本身中是临时的。在with上下文之后，第二个print语句打印配置的值。</font>

### <font style="color:rgb(51, 51, 51);">Frequently used 参数</font>
| <font style="color:rgb(51, 51, 51);">参数</font> | <font style="color:rgb(51, 51, 51);">说明</font> |
| --- | --- |
| **<font style="color:rgb(51, 51, 51);">display.max_rows</font>** | <font style="color:rgb(51, 51, 51);">显示要显示的最大行数</font> |
| **<font style="color:rgb(51, 51, 51);">display.max_columns</font>**<font style="color:rgb(51, 51, 51);"><</font> | <font style="color:rgb(51, 51, 51);">显示要显示的最大列数</font> |
| **<font style="color:rgb(51, 51, 51);">display.expand_frame_repr</font>** | <font style="color:rgb(51, 51, 51);">显示数据框以拉伸页面</font> |
| **<font style="color:rgb(51, 51, 51);">display.max_colwidth</font>** | <font style="color:rgb(51, 51, 51);">显示最大列宽</font> |
| **<font style="color:rgb(51, 51, 51);">display.precision</font>** | <font style="color:rgb(51, 51, 51);">显示十进制数字的精度</font> |


