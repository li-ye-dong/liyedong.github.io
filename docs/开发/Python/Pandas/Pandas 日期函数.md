# Pandas 日期函数
<font style="color:rgb(51, 51, 51);">Pandas 日期函数操作实例</font>

<font style="color:rgb(59, 69, 73);">扩展时间序列，日期功能在财务数据分析中起着重要作用。使用日期数据时，我们经常会遇到以下情况-</font>

<font style="color:rgb(51, 51, 51);">生成日期序列</font><font style="color:rgb(51, 51, 51);">将日期序列转换为不同的频率</font>

## <font style="color:rgb(51, 51, 51);">创建日期范围</font>
<font style="color:rgb(59, 69, 73);">通过指定日期和频率使用date.range()函数，我们可以创建日期序列。默认情况下，范围的频率为天。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.date_range('1/1/2011', periods=5))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-05'],dtype='datetime64[ns]', freq='D')

## <font style="color:rgb(51, 51, 51);">更改日期频率</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.date_range('1/1/2011', periods=5,freq='M'))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

 DatetimeIndex(['2011-01-31', '2011-02-28', '2011-03-31', '2011-04-30', '2011-05-31'],dtype='datetime64[ns]', freq='M')

## <font style="color:rgb(51, 51, 51);">bdate_range</font>
<font style="color:rgb(59, 69, 73);">bdate_range()代表营业日期范围。与date_range()不同，它不包括星期六和星期日。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
print(pd.date_range('1/1/2011', periods=5))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-05'],
    dtype='datetime64[ns]', freq='D')
```

<font style="color:rgb(59, 69, 73);">请注意，3月3日之后，日期跳至3月6日（不包括4日和5日）。只需检查日历中的日期即可。 </font><font style="color:rgb(59, 69, 73);">诸如date_range和bdate_range之类的便利功能利用了多种频率别名。date_range的默认频率是日历日，而bdate_range的默认频率是工作日。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
import pandas as pd
 start = pd.datetime(2011, 1, 1)
 end = pd.datetime(2011, 1, 5)
 print(pd.date_range(start, end))
```

<font style="color:rgb(59, 69, 73);">运行结果如下：</font>

```plain
DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04', '2011-01-05'],
    dtype='datetime64[ns]', freq='D')
```

## <font style="color:rgb(51, 51, 51);">偏移别名</font>
<font style="color:rgb(59, 69, 73);">为有用的通用时间序列频率提供了许多字符串别名。我们将这些别名称为偏移别名。</font>

| 别名 | 描述 | 别名 | 描述 |
| --- | --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">B</font> | <font style="color:rgb(51, 51, 51);">工作日频率</font> | <font style="color:rgb(51, 51, 51);">BQS</font> | <font style="color:rgb(51, 51, 51);">业务季度开始频率</font> |
| <font style="color:rgb(51, 51, 51);">D</font> | <font style="color:rgb(51, 51, 51);">日历日频率</font> | <font style="color:rgb(51, 51, 51);">A</font> | <font style="color:rgb(51, 51, 51);">年度（年）结束频率</font> |
| <font style="color:rgb(51, 51, 51);">W</font> | <font style="color:rgb(51, 51, 51);">每周频率</font> | <font style="color:rgb(51, 51, 51);">BA</font> | <font style="color:rgb(51, 51, 51);">营业年度结束频率</font> |
| <font style="color:rgb(51, 51, 51);">M</font> | <font style="color:rgb(51, 51, 51);">月末频率</font> | <font style="color:rgb(51, 51, 51);">BAS</font> | <font style="color:rgb(51, 51, 51);">营业年度开始频率</font> |
| <font style="color:rgb(51, 51, 51);">SM</font> | <font style="color:rgb(51, 51, 51);">半月结束频率</font> | <font style="color:rgb(51, 51, 51);">BH</font> | <font style="color:rgb(51, 51, 51);">营业时间频率</font> |
| <font style="color:rgb(51, 51, 51);">BM</font> | <font style="color:rgb(51, 51, 51);">营业月结束频率</font> | <font style="color:rgb(51, 51, 51);">H</font> | <font style="color:rgb(51, 51, 51);">每小时频率</font> |
| <font style="color:rgb(51, 51, 51);">MS</font> | <font style="color:rgb(51, 51, 51);">月开始频率</font> | <font style="color:rgb(51, 51, 51);">T, min</font> | <font style="color:rgb(51, 51, 51);">分钟频率</font> |
| <font style="color:rgb(51, 51, 51);">SMS</font> | <font style="color:rgb(51, 51, 51);">信息半个月开始频率</font> | <font style="color:rgb(51, 51, 51);">S</font> | <font style="color:rgb(51, 51, 51);">其次频率</font> |
| <font style="color:rgb(51, 51, 51);">BMS</font> | <font style="color:rgb(51, 51, 51);">工作月开始频率</font> | <font style="color:rgb(51, 51, 51);">L, ms</font> | <font style="color:rgb(51, 51, 51);">毫秒</font> |
| <font style="color:rgb(51, 51, 51);">Q</font> | <font style="color:rgb(51, 51, 51);">四分之一结束频率</font> | <font style="color:rgb(51, 51, 51);">U, us</font> | <font style="color:rgb(51, 51, 51);">微秒</font> |
| <font style="color:rgb(51, 51, 51);">BQ</font> | <font style="color:rgb(51, 51, 51);">业务季度结束频率</font> | <font style="color:rgb(51, 51, 51);">N</font> | <font style="color:rgb(51, 51, 51);">纳秒</font> |
| <font style="color:rgb(51, 51, 51);">QS</font> | <font style="color:rgb(51, 51, 51);">季度开始频率</font> | <font style="color:rgb(51, 51, 51);">   </font> | <font style="color:rgb(51, 51, 51);">   </font> |


