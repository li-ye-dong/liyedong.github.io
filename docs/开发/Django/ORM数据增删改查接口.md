<font style="color:rgb(92, 89, 98);">Django的对象关系映射系统(Object-Relational Mapper, ORM)提供了丰富的数据查询接口, 让你无需使用原生SQL语句即可通过对模型的简单操作实现对数据库里的数据进行增删改查。查询得到的结果叫查询集(QuerySet), 所以这个接口被称为QuerySet API。今天我们就以博客blog为例，演示下Django是如何通过模型对数据库进行增删改查的。</font>

<font style="color:rgb(92, 89, 98);">我们用到的Article模型如下所示：</font>

```python
from django.db import models

class Article(models.Model):
    title = models.CharField('标题', max_length=200, unique=True)
    body = models.TextField('正文')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

## <font style="color:rgb(39, 38, 43);">增</font>
<font style="color:rgb(92, 89, 98);">对于新增数据，Django提供了两种方法，</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">save()</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">create()</font>`<font style="color:rgb(92, 89, 98);">方法。</font>

### <font style="color:rgb(39, 38, 43);">方法一：save方法</font>
```python
from .models import Article

article = Article(title="My first article", body="My first article body")
article.save()
```

<font style="color:rgb(92, 89, 98);">注意: 该方法如果不主动选择save(), 创建的对象实例只会存于内存之中，不会保存到数据库中去。正因为如此，Django还提供了更便捷的create方法。</font>

### <font style="color:rgb(39, 38, 43);">方法二：create方法</font>
```python
article = Article.objects.create(title="My first article", body="My first article body")
```

<font style="color:rgb(92, 89, 98);">为了避免重复创建数据表中已存在的条目，Django还提供了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">get_or_create</font>`<font style="color:rgb(92, 89, 98);">方法。它会返回查询到的或新建的模型对象实例，还会返回这个对象实例是否是刚刚创建的。</font>

```python
obj, created = Article.objects.get_or_create(title="My first article", body="My first article body")
```

<font style="color:rgb(92, 89, 98);">注意: 对Django自带auth模块中的User模型操作，比如创建新的用户时，请用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">create_user</font>`<font style="color:rgb(92, 89, 98);">方法。该方法会将密码自动加Hash存储到数据库中, 如下所示：</font>

```python
from django.contrib.auth.models import User
user = User.objects.create_user(username='john, email='john@gmail.com',password='somepwd')
```

### <font style="color:rgb(39, 38, 43);">方法三：bulk_create方法</font>
<font style="color:rgb(92, 89, 98);">在Django中向数据库中插入多条数据时，每使用save或create方法保存一条就会执行一次SQL。而Django提供的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">bulk_create</font>`<font style="color:rgb(92, 89, 98);">方法可以一次SQL添加多条数据，效率要高很多，如下所示：</font>

```python
# 内存生成多个对象实例
articles  = [Article(title="title1", body="body1"), Article(title="title2", body="body2"), Article(title="title3", body="body3")]

# 执行一次SQL插入数据
Article.objects.bulk_create(articles)
```

## <font style="color:rgb(39, 38, 43);">删</font>
<font style="color:rgb(92, 89, 98);">删即从数据表中删除一个已有条目。Django也允许同时删除一条或多条数据。</font>

### <font style="color:rgb(39, 38, 43);">删除单条数据</font>
```python
# 删除第5篇文章
Article.objects.get(pk=5).delete()
```

### <font style="color:rgb(39, 38, 43);">删除部分数据</font>
```python
# 删除标题含有python的文章
Article.objects.filter(title__icontains="python").delete()
```

### <font style="color:rgb(39, 38, 43);">删除所有数据</font>
```python
# 慎用
Article.objects.all().delete()
```

## <font style="color:rgb(39, 38, 43);">改</font>
<font style="color:rgb(92, 89, 98);">改既可以用save方法，也可以用update方法。其区别在于save方法不仅可以更新数据中现有对象数据，还可以创建新的对象。而update方法只能用于更新已有对象数据。一般来说，如果要同时更新多个对象数据，用update方法或bulk_update方法更合适。</font>

### <font style="color:rgb(39, 38, 43);">方法一： save方法</font>
```python
article = Article.objects.get(id=1)
article.title = "New article title"
article.save()
```

### <font style="color:rgb(39, 38, 43);">方法二：update方法更新单篇文章</font>
```python
article = Article.objects.get(id=1).update(title='new title')
```

### <font style="color:rgb(39, 38, 43);">方法三：update方法同时更新多篇文章</font>
```python
# 更新所有文章标题
article = Article.objects.filter(title__icontains='python').update(title='Django')
```

### <font style="color:rgb(39, 38, 43);">方法四： bulk_update方法</font>
<font style="color:rgb(92, 89, 98);">与</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">bulk_create</font>`<font style="color:rgb(92, 89, 98);">方法类似，Django还提供了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">bulk_update</font>`<font style="color:rgb(92, 89, 98);">方法可以对数据库里的数据进行批量更新。</font>

## <font style="color:rgb(39, 38, 43);">查</font>
<font style="color:rgb(92, 89, 98);">查主要使用get, filter及exclude方法，而且这些方法是可以联用的。</font>

### <font style="color:rgb(39, 38, 43);">查询所有数据</font>
```python
# QuerySet类型，实例对象列表
Article.objects.all() 
# 字典列表
Article.objects.all().values() 
# 只获取title-字典形式
Article.objects.all().values('title') 
# 只获取title列表- 元组形式，只有value，没有key
Article.objects.all().values_list('title')
# 只获取title列表，只有value
Article.objects.all().values_list('title', flat=True)
```

### <font style="color:rgb(39, 38, 43);">查询单条数据</font>
```python
article = Article.objects.get(id=11)
```

<font style="color:rgb(92, 89, 98);">当上述查询有个问题，如果id不存在，会抛出错误。还有一种方式是使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">filter</font>`<font style="color:rgb(92, 89, 98);">方法, 这样即使id不存在也不会报错。</font>

```python
article = Article.objects.filter(id=1).first()
```

<font style="color:rgb(92, 89, 98);">一个更好的方式是使用Django提供的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">get_object_or_404</font>`<font style="color:rgb(92, 89, 98);">方法，如下所示：</font>

```python
from django.shortcuts import get_object_or_404 
article = get_object_or_404(Article, pk=1)
```

### <font style="color:rgb(39, 38, 43);">查询多条数据</font>
#### <font style="color:rgb(39, 38, 43);">按大于、小于及不等于查询</font>
```python
# gte：大于等于，lte：小于等于
articles = Article.objects.filter(id__gte=2).filter(id__lte=11)
# 不等于
articles = Article.objects.exclude(id=10)
```

#### <font style="color:rgb(39, 38, 43);">按范围查询</font>
```python
# 按范围查询，in或者range
articles = Article.objects.filter(id__range=[2, 11])
articles = Article.objects.filter(id__in=[3, 6,9])
```

#### <font style="color:rgb(39, 38, 43);">字符串模糊查询</font>
```python
#标题包含python，若忽略大小写使用icontains
articles = Article.objects.filter(title__contains='python')

#标题以python开头，若忽略大小写使用istartswith
articles = Article.objects.filter(title__startswith='python')

#标题是python结尾的，若忽略大小写使用__iendswith
articles = Article.objects.filter(title__endswith='python')
```

#### <font style="color:rgb(39, 38, 43);">按日期时间查询</font>
```python
# 查询2021年发表的文章
Article.objects.filter(created__year=2021)

# 查询2021年3月19日发表的文章
import datetime
Article.objects.filter(created__date=datetime.date(2021,3,19))

# 查询2021年1月1日以后发表的文章
Article.objects.filter(created__gt=datetime.date(2021, 1, 1))

# 与当前时间相比，查询即将发表的文章
from django.utils import timezone
Article.objects.filter(created__gt=timezone.now())

# 按绝对时间范围查询，查询2021年1月1日到6月30日发表文章
article = Aritlce.objects.filter(created__gte=datetime.date(2021, 1, 1),
                                 pub_date__lte=datetime.date(2021, 6, 30))

# 按相对时间范围查询，用range查询3月1日以后30天内发表文章
startdate = datetime.date(2021, 3, 1)
enddate = startdate + datetime.timedelta(days=30)
Article.objects.filter(pub_date__range=[startdate, enddate])
```

### <font style="color:rgb(39, 38, 43);">切片、排序、去重</font>
```python
# 切片
articles = Article.objects.filter(created__year=2021)[:5]

# 排序：created正序，-表示逆序
articles = Article.objects.all().order_by('-created')

# 去重
Article.objects.filter(title__icontains='python').distinct()
```

## <font style="color:rgb(39, 38, 43);">高级Q和F方法</font>
### <font style="color:rgb(39, 38, 43);">Q方法</font>
<font style="color:rgb(92, 89, 98);">有时候我们需要执行or逻辑的条件查询，这时使用Q方法就可以了，它可以连接多个查询条件。Q对象前面加~可以表示否定。</font>

```python
from django.models import Q
# 查询标题含有python或Django的文章
article = Article.objects.filter(Q(title__icontains='python')|Q(title__icontains='django'))
# 查询标题含有python，不含有Django的文章
article = Article.objects.filter(Q(title__icontains='python')|~Q(title__icontains='django'))
```

### <font style="color:rgb(39, 38, 43);">F方法</font>
<font style="color:rgb(92, 89, 98);">使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">F()</font>`<font style="color:rgb(92, 89, 98);">方法可以实现基于自身字段值来过滤一组对象，它还支持加、减、乘、除、取模和幂运算等算术操作。</font>

```python
from django.db.models import F
Article.objects.filter(n_commnets__gt=F('n_pingbacks'))
Article.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
```

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本章我们介绍了Django中常用的模型查询API，并以博客为例介绍了如何使用基本语句对数据库里的数据进行增删改查。我们还没有介绍更高级的跨表聚合查询，比如</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">annotate</font>`<font style="color:rgb(92, 89, 98);">，</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">aggregate</font>`<font style="color:rgb(92, 89, 98);">,</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);"> select_related</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">prefech_related</font>`<font style="color:rgb(92, 89, 98);">方法，这些会放在Django进阶教程部分的数据查询篇，请欢迎关注。</font>

