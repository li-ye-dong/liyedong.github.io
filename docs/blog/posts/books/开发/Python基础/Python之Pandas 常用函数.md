## <font style="color:rgb(51, 51, 51);">读取数据</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">pd.read_csv(filename)</font> | <font style="color:rgb(51, 51, 51);">读取 CSV 文件；</font> |
| <font style="color:rgb(51, 51, 51);">pd.read_excel(filename)</font> | <font style="color:rgb(51, 51, 51);">读取 Excel 文件；</font> |
| <font style="color:rgb(51, 51, 51);">pd.read_sql(query, connection_object)</font> | <font style="color:rgb(51, 51, 51);">从 SQL 数据库读取数据；</font> |
| <font style="color:rgb(51, 51, 51);">pd.read_json(json_string)</font> | <font style="color:rgb(51, 51, 51);">从 JSON 字符串中读取数据；</font> |
| <font style="color:rgb(51, 51, 51);">pd.read_html(url)</font> | <font style="color:rgb(51, 51, 51);">从 HTML 页面中读取数据。</font> |


## <font style="color:rgb(51, 51, 51);">实例</font>
```python
import pandas as pd

# 从 CSV 文件中读取数据
df = pd.read_csv('data.csv')

# 从 Excel 文件中读取数据
df = pd.read_excel('data.xlsx')

# 从 SQL 数据库中读取数据
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql('SELECT * FROM table_name', conn)

# 从 JSON 字符串中读取数据
json_string = '{"name": "John", "age": 30, "city": "New York"}'
df = pd.read_json(json_string)

# 从 HTML 页面中读取数据
url = 'https://www.runoob.com'
dfs = pd.read_html(url)
df = dfs[0] # 选择第一个数据框
```

---

## <font style="color:rgb(51, 51, 51);">查看数据</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">df.head(n)</font> | <font style="color:rgb(51, 51, 51);">显示前 n 行数据；</font> |
| <font style="color:rgb(51, 51, 51);">df.tail(n)</font> | <font style="color:rgb(51, 51, 51);">显示后 n 行数据；</font> |
| <font style="color:rgb(51, 51, 51);">df.info()</font> | <font style="color:rgb(51, 51, 51);">显示数据的信息，包括列名、数据类型、缺失值等；</font> |
| <font style="color:rgb(51, 51, 51);">df.describe()</font> | <font style="color:rgb(51, 51, 51);">显示数据的基本统计信息，包括均值、方差、最大值、最小值等；</font> |
| <font style="color:rgb(51, 51, 51);">df.shape</font> | <font style="color:rgb(51, 51, 51);">显示数据的行数和列数。</font> |


## <font style="color:rgb(51, 51, 51);">实例</font>
```python
# 显示前五行数据
df.head()

# 显示后五行数据
df.tail()

# 显示数据信息
df.info()

# 显示基本统计信息
df.describe()

# 显示数据的行数和列数
df.shape
```

## <font style="color:rgb(51, 51, 51);">实例</font>
```python
import pandas as pd

data = [
    {"name": "Google", "likes": 25, "url": "https://www.google.com"},
    {"name": "Runoob", "likes": 30, "url": "https://www.runoob.com"},
    {"name": "Taobao", "likes": 35, "url": "https://www.taobao.com"}
]

df = pd.DataFrame(data)
# 显示前两行数据
print(df.head(2))
# 显示前最后一行数据
print(df.tail(1))
```

<font style="color:rgb(51, 51, 51);">以上实例输出结果为：</font>

```python
name  likes                     url
0  Google     25  https://www.google.com
1  Runoob     30  https://www.runoob.com
name  likes                     url
2  Taobao     35  https://www.taobao.com
```

---

## <font style="color:rgb(51, 51, 51);">数据清洗</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">df.dropna()</font> | <font style="color:rgb(51, 51, 51);">删除包含缺失值的行或列；</font> |
| <font style="color:rgb(51, 51, 51);">df.fillna(value)</font> | <font style="color:rgb(51, 51, 51);">将缺失值替换为指定的值；</font> |
| <font style="color:rgb(51, 51, 51);">df.replace(old_value, new_value)</font> | <font style="color:rgb(51, 51, 51);">将指定值替换为新值；</font> |
| <font style="color:rgb(51, 51, 51);">df.duplicated()</font> | <font style="color:rgb(51, 51, 51);">检查是否有重复的数据；</font> |
| <font style="color:rgb(51, 51, 51);">df.drop_duplicates()</font> | <font style="color:rgb(51, 51, 51);">删除重复的数据。</font> |


## <font style="color:rgb(51, 51, 51);">实例</font>
```python
import pandas as pd

data = [
    {"name": "Google", "likes": 25, "url": "https://www.google.com"},
    {"name": "Runoob", "likes": 30, "url": "https://www.runoob.com"},
    {"name": "Taobao", "likes": 35, "url": "https://www.taobao.com"}
]

df = pd.DataFrame(data)
# 显示前两行数据
print(df.head(2))
# 显示前最后一行数据
print(df.tail(1))
```

---

## <font style="color:rgb(51, 51, 51);">数据选择和切片</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">df[column_name]</font> | <font style="color:rgb(51, 51, 51);">选择指定的列；</font> |
| <font style="color:rgb(51, 51, 51);">df.loc[row_index, column_name]</font> | <font style="color:rgb(51, 51, 51);">通过标签选择数据；</font> |
| <font style="color:rgb(51, 51, 51);">df.iloc[row_index, column_index]</font> | <font style="color:rgb(51, 51, 51);">通过位置选择数据；</font> |
| <font style="color:rgb(51, 51, 51);">df.ix[row_index, column_name]</font> | <font style="color:rgb(51, 51, 51);">通过标签或位置选择数据；</font> |
| <font style="color:rgb(51, 51, 51);">df.filter(items=[column_name1, column_name2])</font> | <font style="color:rgb(51, 51, 51);">选择指定的列；</font> |
| <font style="color:rgb(51, 51, 51);">df.filter(regex='regex')</font> | <font style="color:rgb(51, 51, 51);">选择列名匹配正则表达式的列；</font> |
| <font style="color:rgb(51, 51, 51);">df.sample(n)</font> | <font style="color:rgb(51, 51, 51);">随机选择 n 行数据。</font> |


## <font style="color:rgb(51, 51, 51);">实例</font>
```python
# 选择指定的列
df['column_name']

# 通过标签选择数据
df.loc[row_index, column_name]

# 通过位置选择数据
df.iloc[row_index, column_index]

# 通过标签或位置选择数据
df.ix[row_index, column_name]

# 选择指定的列
df.filter(items=['column_name1', 'column_name2'])

# 选择列名匹配正则表达式的列
df.filter(regex='regex')

# 随机选择 n 行数据
df.sample(n=5)
```

---

## <font style="color:rgb(51, 51, 51);">数据排序</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">df.sort_values(column_name)</font> | <font style="color:rgb(51, 51, 51);">按照指定列的值排序；</font> |
| <font style="color:rgb(51, 51, 51);">df.sort_values([column_name1, column_name2], ascending=[True, False])</font> | <font style="color:rgb(51, 51, 51);">按照多个列的值排序；</font> |
| <font style="color:rgb(51, 51, 51);">df.sort_index()</font> | <font style="color:rgb(51, 51, 51);">按照索引排序。</font> |


## <font style="color:rgb(51, 51, 51);">实例</font>
```python
# 按照指定列的值排序
df.sort_values('column_name')

# 按照多个列的值排序
df.sort_values(['column_name1', 'column_name2'], ascending=[True, False])

# 按照索引排序
df.sort_index()
```

---

## <font style="color:rgb(51, 51, 51);">数据分组和聚合</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">df.groupby(column_name)</font> | <font style="color:rgb(51, 51, 51);">按照指定列进行分组；</font> |
| <font style="color:rgb(51, 51, 51);">df.aggregate(function_name)</font> | <font style="color:rgb(51, 51, 51);">对分组后的数据进行聚合操作；</font> |
| <font style="color:rgb(51, 51, 51);">df.pivot_table(values, index, columns, aggfunc)</font> | <font style="color:rgb(51, 51, 51);">生成透视表。</font> |


## <font style="color:rgb(51, 51, 51);">实例</font>
```python
# 按照指定列进行分组
df.groupby('column_name')

# 对分组后的数据进行聚合操作
df.aggregate('function_name')

# 生成透视表
df.pivot_table(values='value', index='index_column', columns='column_name', aggfunc='function_name')
```

---

## <font style="color:rgb(51, 51, 51);">数据合并</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">pd.concat([df1, df2])</font> | <font style="color:rgb(51, 51, 51);">将多个数据框按照行或列进行合并；</font> |
| <font style="color:rgb(51, 51, 51);">pd.merge(df1, df2, on=column_name)</font> | <font style="color:rgb(51, 51, 51);">按照指定列将两个数据框进行合并。</font> |


## <font style="color:rgb(51, 51, 51);">实例</font>
```python
# 将多个数据框按照行或列进行合并
df = pd.concat([df1, df2])

# 按照指定列将两个数据框进行合并
df = pd.merge(df1, df2, on='column_name')
```

---

## <font style="color:rgb(51, 51, 51);">数据选择和过滤</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">df.loc[row_indexer, column_indexer]</font> | <font style="color:rgb(51, 51, 51);">按标签选择行和列。</font> |
| <font style="color:rgb(51, 51, 51);">df.iloc[row_indexer, column_indexer]</font> | <font style="color:rgb(51, 51, 51);">按位置选择行和列。</font> |
| <font style="color:rgb(51, 51, 51);">df[df['column_name'] > value]</font> | <font style="color:rgb(51, 51, 51);">选择列中满足条件的行。</font> |
| <font style="color:rgb(51, 51, 51);">df.query('column_name > value')</font> | <font style="color:rgb(51, 51, 51);">使用字符串表达式选择列中满足条件的行。</font> |


---

## <font style="color:rgb(51, 51, 51);">数据统计和描述</font>
| **<font style="color:rgb(51, 51, 51);">函数</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">df.describe()</font> | <font style="color:rgb(51, 51, 51);">计算基本统计信息，如均值、标准差、最小值、最大值等。</font> |
| <font style="color:rgb(51, 51, 51);">df.mean()</font> | <font style="color:rgb(51, 51, 51);">计算每列的平均值。</font> |
| <font style="color:rgb(51, 51, 51);">df.median()</font> | <font style="color:rgb(51, 51, 51);">计算每列的中位数。</font> |
| <font style="color:rgb(51, 51, 51);">df.mode()</font> | <font style="color:rgb(51, 51, 51);">计算每列的众数。</font> |
| <font style="color:rgb(51, 51, 51);">df.count()</font> | <font style="color:rgb(51, 51, 51);">计算每列非缺失值的数量。</font> |


---

## <font style="color:rgb(51, 51, 51);">实例</font>
<font style="color:rgb(51, 51, 51);">假设我们有如下的 JSON 数据，数据保存到 </font>**<font style="color:rgb(51, 51, 51);">data.json</font>**<font style="color:rgb(51, 51, 51);"> 文件：</font>

## <font style="color:rgb(51, 51, 51);">data.json 文件</font>
```python
[
    {
        "name": "Alice",
        "age": 25,
        "gender": "female",
        "score": 80
    },
    {
        "name": "Bob",
        "age": **null**,
        "gender": "male",
        "score": 90
    },
    {
        "name": "Charlie",
        "age": 30,
        "gender": "male",
        "score": **null**
    },
    {
        "name": "David",
        "age": 35,
        "gender": "male",
        "score": 70
    }
]
```

<font style="color:rgb(51, 51, 51);">我们可以使用 Pandas 读取 JSON 数据，并进行数据清洗和处理、数据选择和过滤、数据统计和描述等操作，具体如下：</font>

## <font style="color:rgb(51, 51, 51);">实例</font>
```python
import pandas as pd

# 读取 JSON 数据
df = pd.read_json('data.json')

# 删除缺失值
df = df.dropna()

# 用指定的值填充缺失值
df = df.fillna({'age': 0, 'score': 0})

# 重命名列名
df = df.rename(columns={'name': '姓名', 'age': '年龄', 'gender': '性别', 'score': '成绩'})

# 按成绩排序
df = df.sort_values(by='成绩', ascending=False)

# 按性别分组并计算平均年龄和成绩
grouped = df.groupby('性别').agg({'年龄': 'mean', '成绩': 'mean'})

# 选择成绩大于等于90的行，并只保留姓名和成绩两列
df = df.loc[df['成绩'] >= 90, ['姓名', '成绩']]

# 计算每列的基本统计信息
stats = df.describe()

# 计算每列的平均值
mean = df.mean()

# 计算每列的中位数
median = df.median()

# 计算每列的众数
mode = df.mode()

# 计算每列非缺失值的数量
count = df.count()
```

<font style="color:rgb(51, 51, 51);">输出结果如下：</font>

```python
# df
姓名  年龄 性别  成绩
1  Bob   0  male  90

# grouped
年龄  成绩
性别                
female  25.000000  80
male    27.500000  80

# stats
成绩
count   1.0
mean   90.0
std     NaN
min    90.0
25%    90.0
50%    90.0
75%    90.0
max    90.0

# mean
成绩    90.0
dtype: float64

# median
成绩    90.0
dtype: float64

# mode
姓名    成绩
0  Bob  90.0

# count
姓名    1
成绩    1
dtype: int64
```

