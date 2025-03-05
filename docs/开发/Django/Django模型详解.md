<font style="color:rgb(92, 89, 98);">Model (模型) 简而言之即数据模型，是一个Django应用的核心。模型不是数据本身（比如数据表里的数据), 而是抽象的描述数据的构成和逻辑关系。</font>

<font style="color:rgb(92, 89, 98);">每个Django的模型(model)实际上是个类，继承了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">models.Model</font>`<font style="color:rgb(92, 89, 98);">。每个Model应该包括属性(字段)，关系（比如单对单，单对多和多对多)和方法。当你定义好Model模型后，Django的接口会自动帮你在数据库生成相应的数据表(table)。这样你就不用自己用SQL语言创建表格或在数据库里操作创建表格了，是不是很省心？</font>

## <font style="color:rgb(39, 38, 43);">模型定义小案例</font>
<font style="color:rgb(92, 89, 98);">假设你要开发一个名叫</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">bookstore</font>`<font style="color:rgb(92, 89, 98);">的应用，专门来管理书店里的书籍。我们首先要为书本和出版社创建模型。出版社有名字和地址。书有名字，描述和添加日期。我们还需要利用ForeignKey定义了出版社与书本之间单对多的关系，因为一个出版社可以出版很多书，每本书都有对应的出版社。我们定义了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Publisher</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Book</font>`<font style="color:rgb(92, 89, 98);">模型，它们都继承了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">models.Model</font>`<font style="color:rgb(92, 89, 98);">。你能看出代码有什么问题吗?</font>

```python
# models.py
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    publisher = ForeignKey(Publisher)
    add_date = models.DateField()

    def __str__(self):
        return self.name
```

<font style="color:rgb(92, 89, 98);">模型创建好后，当你运行</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">python manage.py migrate</font>`<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">命令创建数据表的时候你会遇到错误，错误原因如下：</font>

+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">CharField</font>`<font style="color:rgb(92, 89, 98);">里的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">max_length</font>`<font style="color:rgb(92, 89, 98);">选项没有定义</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ForeignKey(Publisher)</font>`<font style="color:rgb(92, 89, 98);">里的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete</font>`<font style="color:rgb(92, 89, 98);">选项有没有定义</font>

<font style="color:rgb(92, 89, 98);">所以当你定义Django模型Model的时候，你一定要十分清楚2件事:</font>

+ <font style="color:rgb(92, 89, 98);">这个Field是否有必选项, 比如</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">CharField</font>`<font style="color:rgb(92, 89, 98);">的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">max_length</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ForeignKey</font>`<font style="color:rgb(92, 89, 98);">的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete</font>`<font style="color:rgb(92, 89, 98);">选项是必须要设置的。</font>
+ <font style="color:rgb(92, 89, 98);">这个Field是否必需(blank = True or False)，是否可以为空 (null = True or False)。这关系到数据的完整性。</font>

<font style="color:rgb(92, 89, 98);">下面是订正错误后的Django模型：</font>

```python
# models.py
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    publisher = ForeignKey(Publisher,on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
```

<font style="color:rgb(92, 89, 98);">修改模型后，你需要连续运行</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">python manage.py makemigrations</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">python manage.py migrate</font>`<font style="color:rgb(92, 89, 98);">这两个命令，前者检查模型有无变化，后者将变化迁移至数据表。如果一切顺利，Django会在数据库(默认sqlite)中生成或变更由</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">appname_modelname</font>`<font style="color:rgb(92, 89, 98);">组成的数据表，本例两张数据表分别为</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">bookstore_publisher</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">bookstore_book</font>`<font style="color:rgb(92, 89, 98);">。</font>

## <font style="color:rgb(39, 38, 43);">模型的组成</font>
<font style="color:rgb(92, 89, 98);">一个标准的Django模型分别由模型字段、META选项和方法三部分组成。我们接下来对各部分进行详细介绍。Django官方编码规范建议按如下方式排列：</font>

+ <font style="color:rgb(92, 89, 98);">定义的模型字段：包括基础字段和关系字段</font>
+ <font style="color:rgb(92, 89, 98);">自定义的Manager方法：改变模型</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">class Meta选项</font>`<font style="color:rgb(92, 89, 98);">: 包括排序、索引等等(可选)。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">def __str__()</font>`<font style="color:rgb(92, 89, 98);">：定义单个模型实例对象的名字(可选)。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">def save()</font>`<font style="color:rgb(92, 89, 98);">：重写save方法(可选)。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">def get_absolute_url()</font>`<font style="color:rgb(92, 89, 98);">：为单个模型实例对象生成独一无二的url(可选)</font>
+ <font style="color:rgb(92, 89, 98);">其它自定义的方法。</font>

## <font style="color:rgb(39, 38, 43);">模型的字段</font>
`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">models.Model</font>`<font style="color:rgb(92, 89, 98);">提供的常用模型字段包括基础字段和关系字段。</font>

### <font style="color:rgb(39, 38, 43);">基础字段</font>
<font style="color:rgb(92, 89, 98);">**CharField() **</font>

<font style="color:rgb(92, 89, 98);">一般需要通过max_length = xxx 设置最大字符长度。如不是必填项，可设置blank = True和default = ‘‘。如果用于username, 想使其唯一，可以设置</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">unique = True</font>`<font style="color:rgb(92, 89, 98);">。如果有choice选项，可以设置 choices = XXX_CHOICES</font>

<font style="color:rgb(92, 89, 98);">**TextField() **</font>

<font style="color:rgb(92, 89, 98);">适合大量文本，max_length = xxx选项可选。</font>

<font style="color:rgb(92, 89, 98);">**DateField() 和DateTimeField() **</font>

<font style="color:rgb(92, 89, 98);">可通过default=xx选项设置默认日期和时间。</font>

+ <font style="color:rgb(92, 89, 98);">对于DateTimeField: default=timezone.now - 先要</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">from django.utils import timezone</font>`
+ <font style="color:rgb(92, 89, 98);">如果希望自动记录一次修改日期(modified)，可以设置:</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">auto_now=True</font>`
+ <font style="color:rgb(92, 89, 98);">如果希望自动记录创建日期(created),可以设置</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">auto_now_add=True</font>`

<font style="color:rgb(92, 89, 98);">**EmailField() **</font>

<font style="color:rgb(92, 89, 98);">如不是必填项，可设置blank = True和default = ‘。一般Email用于用户名应该是唯一的，建议设置unique = True</font>

**<font style="color:rgb(92, 89, 98);">IntegerField(), SlugField(), URLField()，BooleanField()</font>**

<font style="color:rgb(92, 89, 98);">可以设置blank = True or null = True。对于BooleanField一般建议设置</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">defaut = True or False</font>`

<font style="color:rgb(92, 89, 98);">**FileField(upload_to=None, max_length=100) - 文件字段 **</font>

+ <font style="color:rgb(92, 89, 98);">upload_to = “/some folder/”：上传文件夹路径</font>
+ <font style="color:rgb(92, 89, 98);">max_length = xxxx：文件最大长度</font>

<font style="color:rgb(92, 89, 98);">**ImageField (upload_to=None, max_length=100,)- 图片字段 **</font>

+ <font style="color:rgb(92, 89, 98);">upload_to = “/some folder/”: 指定上传图片路径</font>

### <font style="color:rgb(39, 38, 43);">关系字段</font>
**<font style="color:rgb(92, 89, 98);">OneToOneField(to, on_delete=xxx, options) - 单对单关系</font>**

+ <font style="color:rgb(92, 89, 98);">to必需指向其他模型，比如 Book or ‘self’ .</font>
+ <font style="color:rgb(92, 89, 98);">必需指定</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete</font>`<font style="color:rgb(92, 89, 98);">选项(删除选项): i.e, “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete = models.CASCADE</font>`<font style="color:rgb(92, 89, 98);">” or “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete = models.SET_NULL</font>`<font style="color:rgb(92, 89, 98);">” .</font>
+ <font style="color:rgb(92, 89, 98);">可以设置 “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name = xxx</font>`<font style="color:rgb(92, 89, 98);">” 便于反向查询。</font>

**<font style="color:rgb(92, 89, 98);">ForeignKey(to, on_delete=xxx, options) - 单对多关系</font>**

+ <font style="color:rgb(92, 89, 98);">to必需指向其他模型，比如 Book or ‘self’ .</font>
+ <font style="color:rgb(92, 89, 98);">必需指定</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete</font>`<font style="color:rgb(92, 89, 98);">选项(删除选项): i.e, “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete = models.CASCADE</font>`<font style="color:rgb(92, 89, 98);">” or “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete = models.SET_NULL</font>`<font style="color:rgb(92, 89, 98);">” .</font>
+ <font style="color:rgb(92, 89, 98);">可以设置”default = xxx” or “null = True” ;</font>
+ <font style="color:rgb(92, 89, 98);">如果有必要，可以设置 “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">limit_choices_to =</font>`<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">“,</font>
+ <font style="color:rgb(92, 89, 98);">可以设置 “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name = xxx</font>`<font style="color:rgb(92, 89, 98);">” 便于反向查询。</font>

**<font style="color:rgb(92, 89, 98);">ManyToManyField(to, options) - 多对多关系</font>**

+ <font style="color:rgb(92, 89, 98);">to 必需指向其他模型，比如 User or ‘self’ .</font>
+ <font style="color:rgb(92, 89, 98);">设置 “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">symmetrical = False</font>`<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">“ 表示多对多关系不是对称的，比如A关注B不代表B关注A</font>
+ <font style="color:rgb(92, 89, 98);">设置 “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">through = 'intermediary model'</font>`<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">“ 如果需要建立中间模型来搜集更多信息。</font>
+ <font style="color:rgb(92, 89, 98);">可以设置 “</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name = xxx</font>`<font style="color:rgb(92, 89, 98);">” 便于反向查询。</font>

<font style="color:rgb(92, 89, 98);">示例：一个人加入多个组，一个组包含多个人，我们需要额外的中间模型记录加入日期和理由。</font>

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```

<font style="color:rgb(92, 89, 98);">对于</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">OneToOneField</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ForeignKey</font>`<font style="color:rgb(92, 89, 98);">,</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">on_delete</font>`<font style="color:rgb(92, 89, 98);">选项和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name</font>`<font style="color:rgb(92, 89, 98);">是两个非常重要的设置，前者决定了了关联外键删除方式，后者决定了模型反向查询的名字。</font>

### <font style="color:rgb(39, 38, 43);">on_delete删除选项</font>
<font style="color:rgb(92, 89, 98);">Django提供了如下几种关联外键删除选项, 可以根据实际需求使用。</font>

+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">CASCADE</font>`<font style="color:rgb(92, 89, 98);">：级联删除。当你删除publisher记录时，与之关联的所有 book 都会被删除。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">PROTECT</font>`<font style="color:rgb(92, 89, 98);">: 保护模式。如果有外键关联，就不允许删除，删除的时候会抛出ProtectedError错误，除非先把关联了外键的记录删除掉。例如想要删除publisher，那你要把所有关联了该publisher的book全部删除才可能删publisher。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">SET_NULL</font>`<font style="color:rgb(92, 89, 98);">: 置空模式。删除的时候，外键字段会被设置为空。删除publisher后，book 记录里面的publisher_id 就置为null了。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">SET_DEFAULT</font>`<font style="color:rgb(92, 89, 98);">: 置默认值，删除的时候，外键字段设置为默认值。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">SET()</font>`<font style="color:rgb(92, 89, 98);">: 自定义一个值。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">DO_NOTHING</font>`<font style="color:rgb(92, 89, 98);">：什么也不做。删除不报任何错，外键值依然保留，但是无法用这个外键去做查询。</font>

### <font style="color:rgb(39, 38, 43);">related_name选项</font>
`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name</font>`<font style="color:rgb(92, 89, 98);">用于设置模型反向查询的名字，非常有用。在文初的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Publisher</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Book</font>`<font style="color:rgb(92, 89, 98);">模型里，我们可以通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">book.publisher</font>`<font style="color:rgb(92, 89, 98);">获取每本书的出版商信息，这是因为</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Book</font>`<font style="color:rgb(92, 89, 98);">模型里有</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">publisher</font>`<font style="color:rgb(92, 89, 98);">这个字段。但是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Publisher</font>`<font style="color:rgb(92, 89, 98);">模型里并没有</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">book</font>`<font style="color:rgb(92, 89, 98);">这个字段，那么我们如何通过出版商反查其出版的所有书籍信息呢？</font>

<font style="color:rgb(92, 89, 98);">Django对于关联字段默认使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">模型名_set</font>`<font style="color:rgb(92, 89, 98);">进行反查，即通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">publisher.book_set.all</font>`<font style="color:rgb(92, 89, 98);">查询。但是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">book_set</font>`<font style="color:rgb(92, 89, 98);">并不是一个很友好的名字，我们更希望通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">publisher.books</font>`<font style="color:rgb(92, 89, 98);">获取一个出版社已出版的所有书籍信息，这时我们就要修改我们的模型了，将</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name</font>`<font style="color:rgb(92, 89, 98);">设为</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">books</font>`<font style="color:rgb(92, 89, 98);">, 如下所示：</font>

```python
# models.py
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name

# 将related_name设置为books
class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    publisher = ForeignKey(Publisher,on_delete=models.CASCADE, related_name='books')
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
```

<font style="color:rgb(92, 89, 98);">我们再来对比一下如何通过publisher查询其出版的所有书籍，你觉得哪个更好呢?</font>

1. <font style="color:rgb(92, 89, 98);">设置</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name</font>`<font style="color:rgb(92, 89, 98);">前：</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">publisher.book_set.all</font>`
2. <font style="color:rgb(92, 89, 98);">设置</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">related_name</font>`<font style="color:rgb(92, 89, 98);">后：</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">publisher.books.all</font>`

## <font style="color:rgb(39, 38, 43);">模型的META选项</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">abstract=True</font>`<font style="color:rgb(92, 89, 98);">: 指定该模型为抽象模型</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">proxy=True</font>`<font style="color:rgb(92, 89, 98);">: 指定该模型为代理模型</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">verbose_name=xxx</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">verbose_name_plural=xxx</font>`<font style="color:rgb(92, 89, 98);">: 为模型设置便于人类阅读的别名</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">db_table= xxx</font>`<font style="color:rgb(92, 89, 98);">: 自定义数据表名</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">odering=['-pub-date']</font>`<font style="color:rgb(92, 89, 98);">: 自定义按哪个字段排序，</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">-</font>`<font style="color:rgb(92, 89, 98);">代表逆序</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">permissions=[]</font>`<font style="color:rgb(92, 89, 98);">: 为模型自定义权限</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">managed=False</font>`<font style="color:rgb(92, 89, 98);">: 默认为True，如果为False，Django不会为这个模型生成数据表</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">indexes=[]</font>`<font style="color:rgb(92, 89, 98);">: 为数据表设置索引，对于频繁查询的字段，建议设置索引</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">constraints=</font>`<font style="color:rgb(92, 89, 98);">: 给数据库中的数据表增加约束。</font>

## <font style="color:rgb(39, 38, 43);">模型的方法</font>
### <font style="color:rgb(39, 38, 43);">标准方法</font>
<font style="color:rgb(92, 89, 98);">以下三个方法是Django模型自带的三个标准方法：</font>

+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">def __str__()</font>`<font style="color:rgb(92, 89, 98);">：给单个模型对象实例设置人为可读的名字(可选)。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">def save()</font>`<font style="color:rgb(92, 89, 98);">：重写save方法(可选)。</font>
+ `<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">def get_absolute_url()</font>`<font style="color:rgb(92, 89, 98);">：为单个模型实例对象生成独一无二的url(可选)</font>

<font style="color:rgb(92, 89, 98);">除此以外，我们经常自定义方法或Manager方法</font>

### <font style="color:rgb(39, 38, 43);">示例一：自定义方法</font>
```python
# 为每篇文章生成独一无二的url
def get_absolute_url(self):
    return reverse('blog:article_detail', args=[str(self.id)])

# 计数器
def viewed(self):
    self.views += 1
    self.save(update_fields=['views'])
```

### <font style="color:rgb(39, 38, 43);">示例二：自定义Manager方法</font>
```python
# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Roald Dahl')

# Then hook it into the Book model explicitly.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    objects = models.Manager() # The default manager.
    dahl_objects = DahlBookManager() # The Dahl-specific manager.
```

## <font style="color:rgb(39, 38, 43);">完美的高级Django模型示例</font>
<font style="color:rgb(92, 89, 98);">一个完美的django高级模型结构如下所示，可以满足绝大部分应用场景，希望对你有所帮助。</font>

```python
from django.db import models
from django.urls import reverse

# 自定义Manager方法
class HighRatingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(rating=1)

# CHOICES选项
class Rating(models.IntegerChoices):
    VERYGOOD = 1, 'Very Good'
    GOOD = 2, 'Good'
    BAD = 3, 'Bad'

class Product(models.Model):
    # 数据表字段
    name = models.CharField('name', max_length=30)
    rating = models.IntegerField(max_length=1, choices=Rating.choices)

    # MANAGERS方法
    objects = models.Manager()
    high_rating_products =HighRatingManager()

    # META类选项
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    # __str__方法
    def __str__(self):
        return self.name

    # 重写save方法
    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs) 
        do_something_else()

    # 定义单个对象绝对路径
    def get_absolute_url(self):
        return reverse('product_details', kwargs={'pk': self.id})

    # 其它自定义方法
    def do_something(self):
```

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本章我们介绍了Django模型的组成: 字段(基础字段和关系字段), META选项和方法。我还没有介绍模型的继承及模型特殊字段(比如Choices枚举类型)，这些我们将放在Django进阶教程的模型进阶部分。查询下章我们将重点介绍如何使用这些API语句操作我们的模型，对数据表里的数据进行增删查改。</font>

