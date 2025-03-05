<font style="color:rgb(59, 69, 73);">Pandas 有三种常用的数据结构</font>

<font style="color:rgb(51, 51, 51);">Series</font><font style="color:rgb(51, 51, 51);">DataFrame</font><font style="color:rgb(51, 51, 51);">Panel</font>

<font style="color:rgb(59, 69, 73);">这些数据结构建立在Numpy数组之上，这意味着它们运行速度都非常快。</font>

## <font style="color:rgb(51, 51, 51);">Python、Numpy和Pandas对比</font>
**<font style="color:rgb(51, 51, 51);">Python</font>**

<font style="color:rgb(51, 51, 51);">list：Python自带数据类型，主要用一维，功能简单，效率低</font><font style="color:rgb(51, 51, 51);">Dict：Python自带数据类型，多维键值对，效率低</font>

**<font style="color:rgb(51, 51, 51);">Numpy</font>**

<font style="color:rgb(51, 51, 51);">ndarray：Numpy基础数据类型，单一数据类型</font><font style="color:rgb(51, 51, 51);">关注数据结构/运算/维度（数据间关系）</font>

**<font style="color:rgb(51, 51, 51);">Pandas</font>**

<font style="color:rgb(51, 51, 51);">Series：1维，类似带索引的1维ndarray</font><font style="color:rgb(51, 51, 51);">DataFrame：2维，表格型数据类型，类似带行／列索引的2维ndarray 关注数据与索引的关系（数据实际应用）</font>

**<font style="color:rgb(59, 69, 73);">从实用性、功能强弱和和可操作性比较：list < ndarray < Series/DataFrame</font>**

**<font style="color:rgb(59, 69, 73);">数据规整和分析工作中，ndarry数组作为必要补充，大部分数据尽量使用Pandas数据类型</font>**

<font style="color:rgb(59, 69, 73);">考虑这些数据结构的最佳方法是高维数据结构是其低维数据结构的容器。例如，DataFrame是Series的容器，Panel是DataFrame的容器。</font>

| <font style="color:rgb(51, 51, 51);">数据结构</font> | <font style="color:rgb(51, 51, 51);">维度</font> | <font style="color:rgb(51, 51, 51);">说明</font> |
| --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">Series</font> | <font style="color:rgb(51, 51, 51);">1</font> | <font style="color:rgb(51, 51, 51);">用于存储一个序列的一维数据</font> |
| <font style="color:rgb(51, 51, 51);">Data Frames</font> | <font style="color:rgb(51, 51, 51);">2</font> | <font style="color:rgb(51, 51, 51);">DataFrame作为更复杂的数据结构，则用于存储多维数据</font> |
| <font style="color:rgb(51, 51, 51);">Panel</font> | <font style="color:rgb(51, 51, 51);">3</font> | <font style="color:rgb(51, 51, 51);">通用的3D标签，大小可变的数组。</font> |


<font style="color:rgb(59, 69, 73);">建立和处理二维数组是一项繁琐的工作，在编写函数时，要由用户来考虑数据集的方向。但是使用Pandas数据结构可以减少用户的精力。  
</font><font style="color:rgb(59, 69, 73);">例如，对于表格数据(DataFrame)，在语义上考虑索引（行）和列比在轴0和轴1上更有帮助。</font>

## <font style="color:rgb(51, 51, 51);">变异性</font>
<font style="color:rgb(59, 69, 73);">所有Pandas数据结构都是值可变的（可以更改），除了Series以外，其他大小都是可变的。系列是大小不变的。</font>

<font style="color:rgb(59, 69, 73);">注 -DataFrame被广泛使用，是最重要的数据结构之一。面板使用少得多。</font>

## <font style="color:rgb(51, 51, 51);">Series</font>
<font style="color:rgb(59, 69, 73);">Series是具有均匀数据的一维数组状结构。例如，以下系列是整数10、23、56的集合...</font>

| <font style="color:rgb(51, 51, 51);">10</font> | <font style="color:rgb(51, 51, 51);">23</font> | <font style="color:rgb(51, 51, 51);">56</font> | <font style="color:rgb(51, 51, 51);">17</font> | <font style="color:rgb(51, 51, 51);">52</font> | <font style="color:rgb(51, 51, 51);">61</font> | <font style="color:rgb(51, 51, 51);">73</font> | <font style="color:rgb(51, 51, 51);">90</font> | <font style="color:rgb(51, 51, 51);">26</font> | <font style="color:rgb(51, 51, 51);">72</font> |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


<font style="color:rgb(59, 69, 73);">Series是具有均匀数据的一维数组状结构。例如，以下系列是整数10、23、56的集合...</font>

**<font style="color:rgb(51, 51, 51);">关键点</font>**

<font style="color:rgb(51, 51, 51);">同类数据</font><font style="color:rgb(51, 51, 51);">大小不变</font><font style="color:rgb(51, 51, 51);">数据可变值</font>

## <font style="color:rgb(51, 51, 51);">Data Frames</font>
<font style="color:rgb(59, 69, 73);">DataFrame是具有异构数据的二维数组。例如，</font>

| <font style="color:rgb(51, 51, 51);">Name</font> | <font style="color:rgb(51, 51, 51);">Age</font> | <font style="color:rgb(51, 51, 51);">Gender</font> | <font style="color:rgb(51, 51, 51);">Rating</font> |
| --- | --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">Steve</font> | <font style="color:rgb(51, 51, 51);">32</font> | <font style="color:rgb(51, 51, 51);">Male</font> | <font style="color:rgb(51, 51, 51);">3.45</font> |
| <font style="color:rgb(51, 51, 51);">Lia</font> | <font style="color:rgb(51, 51, 51);">28</font> | <font style="color:rgb(51, 51, 51);">Female</font> | <font style="color:rgb(51, 51, 51);">4.6</font> |
| <font style="color:rgb(51, 51, 51);">Vin</font> | <font style="color:rgb(51, 51, 51);">45</font> | <font style="color:rgb(51, 51, 51);">Male</font> | <font style="color:rgb(51, 51, 51);">3.9</font> |
| <font style="color:rgb(51, 51, 51);">Katie</font> | <font style="color:rgb(51, 51, 51);">38</font> | <font style="color:rgb(51, 51, 51);">Female</font> | <font style="color:rgb(51, 51, 51);">2.78</font> |


<font style="color:rgb(59, 69, 73);">上表代表组织的销售团队的数据及其总体绩效等级，数据以行和列表示，每列代表一个属性，每行代表一个人。</font>

**<font style="color:rgb(51, 51, 51);">列的数据类型</font>**

| <font style="color:rgb(51, 51, 51);">Column</font> | <font style="color:rgb(51, 51, 51);">Type</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">Name</font> | <font style="color:rgb(51, 51, 51);">String</font> |
| <font style="color:rgb(51, 51, 51);">Age</font> | <font style="color:rgb(51, 51, 51);">Integer</font> |
| <font style="color:rgb(51, 51, 51);">Gender</font> | <font style="color:rgb(51, 51, 51);">String</font> |
| <font style="color:rgb(51, 51, 51);">Rating</font> | <font style="color:rgb(51, 51, 51);">Float</font> |


**<font style="color:rgb(51, 51, 51);">关键点</font>**

<font style="color:rgb(51, 51, 51);">异构数据</font><font style="color:rgb(51, 51, 51);">大小不变</font><font style="color:rgb(51, 51, 51);">数据可变</font>

## <font style="color:rgb(51, 51, 51);">Panel</font>
<font style="color:rgb(59, 69, 73);">Panel是具有异构数据的三维数据结构。很难用图形表示面板。但是面板可以说明为DataFrame的容器。</font>

**<font style="color:rgb(51, 51, 51);">关键点</font>**

<font style="color:rgb(51, 51, 51);">异构数据大小可变数据可变</font>

