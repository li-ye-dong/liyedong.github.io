<font style="color:rgb(92, 89, 98);">在本篇文章中我们将以博客为例，使用DRF提供的序列化器(Serializers类)开发两个API接口并测试。</font>

<font style="color:rgb(92, 89, 98);">这两个API端点的简单描述如下所示 (注意：规范的API文档需要更多信息)。</font>

```python
# 接口描述：文章列表资源。GET请求获取文章列表资源, POST请求提交新文章
# 接口地址: http://127.0.0.1:8000/api/v1/articles
# 请求方式：GET, POST
# 返回参数：JSON格式文章列表和状态码


# 接口描述：单篇文章资源。GET获取文章详情, PUT修改，DELETE删除
# 接口地址: http://127.0.0.1:8000/api/v1/articles/{id}
# 请求方式：GET, PUT, DELETE
# 返回参数: GET和PUT(JSON格式文章详情和状态码), DELETE(状态码)
```

## <font style="color:rgb(39, 38, 43);">准备工作</font>
<font style="color:rgb(92, 89, 98);">在正式开始前，我们先要用virtualenv创建一个新的Python虚拟环境。如果你使用PyCharm创建Django项目，它会自动为你创建好一个虚拟环境。</font>

```python
virtualenv env
source env/bin/activate
```

<font style="color:rgb(92, 89, 98);">虚拟环境激活后，我们就可以安装我们需要的包了。</font>

```python
pip install django
pip install djangorestframework
```

<font style="color:rgb(92, 89, 98);">接下来我们使用如下命令创建一个名为</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">apiproject</font>`<font style="color:rgb(92, 89, 98);">的项目，另外创建一个名为</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog</font>`<font style="color:rgb(92, 89, 98);">的app。</font>

```python
django-admin.py startproject apiproject # 创建项目
cd apiproject # 进入项目目录
python manage.py startapp blog # 创建应用
```

<font style="color:rgb(92, 89, 98);">我们需要将新建的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog</font>`<font style="color:rgb(92, 89, 98);">app和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">rest_framework</font>`<font style="color:rgb(92, 89, 98);">添加到</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">INSTALLED_APPS</font>`<font style="color:rgb(92, 89, 98);">。现在可以编辑</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">apiproject/settings.py</font>`<font style="color:rgb(92, 89, 98);">文件, 如下所示：</font>

```python
INSTALLED_APPS =(
    ...
    'rest_framework',
'blog',
)
```

<font style="color:rgb(92, 89, 98);">注意: 如果你使用的Django版本很低或希望避免自己的app名与第三方库的app名冲突，你需要使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog.apps.BlogConfig</font>`<font style="color:rgb(92, 89, 98);">替换</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog</font>`<font style="color:rgb(92, 89, 98);">。</font>

### <font style="color:rgb(39, 38, 43);">创建模型 (models)</font>
<font style="color:rgb(92, 89, 98);">编辑</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog/models.py</font>`<font style="color:rgb(92, 89, 98);">文件, 创建</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Article</font>`<font style="color:rgb(92, 89, 98);">模型，用于存储我们博客的文章数据。用户(User)与文章(Article)是单对多的关系(ForeinKey)，因为一个用户可以发表多篇文章。为了方便，用户模型我们使用了Django自带的用户模型。</font>

```python
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    """Article Model"""
    STATUS_CHOICES = (
        ('p', _('Published')),
        ('d', _('Draft')),
    )

    title = models.CharField(verbose_name=_('Title (*)'), max_length=90, db_index=True)
    body = models.TextField(verbose_name=_('Body'), blank=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE, related_name='articles')
    status = models.CharField(_('Status (*)'), max_length=1, choices=STATUS_CHOICES, default='s', null=True, blank=True)
    create_date = models.DateTimeField(verbose_name=_('Create Date'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
```

<font style="color:rgb(92, 89, 98);">模型创建好后，执行如下命令同步数据库并创建超级用户, Django会自动根据模型字段生成数据表。</font>

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

<font style="color:rgb(92, 89, 98);">之所以我们要创建超级用户是因为我们要通过Django自带的后台admin添加文章和用户信息, 以便测试我们的API接口能否正常工作。</font>

### <font style="color:rgb(39, 38, 43);">配置Django后台(admin)</font>
<font style="color:rgb(92, 89, 98);">编辑</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog/admin.py</font>`<font style="color:rgb(92, 89, 98);">文件, 添加如下代码：</font>

```python
from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'create_date')

    '''filter options'''
    list_filter = ('status', )

    '''10 items per page'''
    list_per_page = 10

admin.site.register(Article, ArticleAdmin)
```

<font style="color:rgb(92, 89, 98);">现在可以启动Django自带的测试服务器，进入admin后台添加些文章和用户(这里就不详细演示了)，接下来就可以开始我们的序列化工作了。</font>

```python
python manage.py runserver
```

## <font style="color:rgb(39, 38, 43);">自定义序列化器(serializers)</font>
<font style="color:rgb(92, 89, 98);">利用DRF开发Web API的第一步总是自定义序列化器(serializers)。序列化器的作用是将模型实例(比如用户、文章)序列化和反序列化为诸如</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">json</font>`<font style="color:rgb(92, 89, 98);">之类的表示形式。一个模型实例可能有许多字段属性，但一般情况下你不需要把所有字段信息以JSON格式数据返回给用户。</font>**<font style="color:rgb(92, 89, 98);">序列化器定义了需要对一个模型实例的哪些字段进行序列化/反序列化, 并可对客户端发送过来的数据进行验证和存储</font>**<font style="color:rgb(92, 89, 98);">。</font>

<font style="color:rgb(92, 89, 98);">就像Django提供了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Form</font>`<font style="color:rgb(92, 89, 98);">类和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ModelForm</font>`<font style="color:rgb(92, 89, 98);">类两种方式自定义表单一样，REST framework提供了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Serializer</font>`<font style="color:rgb(92, 89, 98);">类和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ModelSerializer</font>`<font style="color:rgb(92, 89, 98);">类两种方式供你自定义序列化器。前者需手动指定需要序列化和反序列化的字段，后者根据模型(model)生成需要序列化和反序列化的字段，可以使代码更简洁。</font>

<font style="color:rgb(92, 89, 98);">下面我们将分别展示如何使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Serializer</font>`<font style="color:rgb(92, 89, 98);">类和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ModelSerializer</font>`<font style="color:rgb(92, 89, 98);">类自定义序列化器。</font>

### <font style="color:rgb(39, 38, 43);">使用Serializer类</font>
<font style="color:rgb(92, 89, 98);">在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog</font>`<font style="color:rgb(92, 89, 98);">的目录下创建一个名为</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">serializers.py</font>`<font style="color:rgb(92, 89, 98);">文件，并添加以下内容。</font>

```python
from rest_framework import serializers
from .models import Article
from django.contrib.auth import get_user_model

User = get_user_model()

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=90)
    body = serializers.CharField(required=False, allow_blank=True)
    author = serializers.ReadOnlyField(source="author.id")
    status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')
    create_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create a new "article" instance
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Use validated data to return an existing `Article`instance。"""
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
```

<font style="color:rgb(92, 89, 98);">序列化器类的第一部分定义了序列化/反序列化的字段。</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">create()</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">update()</font>`<font style="color:rgb(92, 89, 98);">方法定义了在调用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">serializer.save()</font>`<font style="color:rgb(92, 89, 98);">时如何创建和修改完整的实例。</font>

<font style="color:rgb(92, 89, 98);">序列化器类与Django</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Form</font>`<font style="color:rgb(92, 89, 98);">类非常相似，并在各种字段中设置各种验证，例如</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">required</font>`<font style="color:rgb(92, 89, 98);">，</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">max_length</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">default</font>`<font style="color:rgb(92, 89, 98);">。</font>

**<font style="color:rgb(92, 89, 98);">注意</font>**<font style="color:rgb(92, 89, 98);">：定义序列化器时一定要注明哪些是仅可读字段(</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">read-only fields</font>`<font style="color:rgb(92, 89, 98);">)，哪些是普通字段。对于read-only fields，客户端是不需要也不能够通过POST或PUT请求提交相关数据进行反序列化的。</font>

<font style="color:rgb(92, 89, 98);">本例中ID和create_date都是由模型自动生成，每个article的author我们也希望在视图中与request.user绑定，而不是由用户通过POST或PUT自行修改，所以这些字段都是read-only。相反title，body和status是用户可以添加或修改的字段，所以未设成read-only。</font>

### <font style="color:rgb(39, 38, 43);">使用ModelSerializer类</font>
<font style="color:rgb(92, 89, 98);">我们的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ArticleSerializer</font>`<font style="color:rgb(92, 89, 98);">类中重复了很多包含在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Article</font>`<font style="color:rgb(92, 89, 98);">模型（model）中的字段信息。使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ModelSerializer</font>`<font style="color:rgb(92, 89, 98);">类可以重构我们的序列化器类，使整体代码更简洁。</font>

<font style="color:rgb(92, 89, 98);">再次打开</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog/serializers.py</font>`<font style="color:rgb(92, 89, 98);">文件，并将</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ArticleSerializer</font>`<font style="color:rgb(92, 89, 98);">类替换为以下内容。两者作用是一样的。</font>

```python
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')
```

<font style="color:rgb(92, 89, 98);">如果你希望author不可见并让DRF根据request.user自动补全这个字段，可以按如下修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ArticleSerializer</font>`

```python
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id','create_date')
```

## <font style="color:rgb(39, 38, 43);">编写API视图(views.py)</font>
<font style="color:rgb(92, 89, 98);">接下来我们要使用自定义的序列化器来编写API视图，处理客户端的请求，并给出响应。与Django一样，DRF也支持使用基于函数的视图(Functional Based View, FBV)和基于类的视图(Class Based View, CBV)来编写视图(views)。</font>

<font style="color:rgb(92, 89, 98);">在本篇教程中，我们将编写两个基于函数的视图：</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">article_list</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">article_detail</font>`<font style="color:rgb(92, 89, 98);">。关于基于类的视图，我们会在下篇文章中介绍。</font>

<font style="color:rgb(92, 89, 98);">编辑</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog/views.py</font>`<font style="color:rgb(92, 89, 98);">文件，并且添加以下内容。</font>

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    """
    List all articles, or create a new article.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            # Very important. Associate request.user with author
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**<font style="color:rgb(92, 89, 98);">注意</font>**<font style="color:rgb(92, 89, 98);">：由于序列化器中author是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">read-only</font>`<font style="color:rgb(92, 89, 98);">字段，用户是无法通过POST提交来修改的，我们在创建Article实例时需手动将author和request.user绑定，如下所示：</font>

```python
serializer.save(author=request.user)
```

<font style="color:rgb(92, 89, 98);">以下是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">views.py</font>`<font style="color:rgb(92, 89, 98);">模块中单个</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">article_detail</font>`<font style="color:rgb(92, 89, 98);">的视图。</font>

```python
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    """
    Retrieve，update or delete an article instance。"""
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

<font style="color:rgb(92, 89, 98);">这两个函数视图看似和Django普通函数视图非常类似，但其作用大不相同。这里我们使用了DRF提供的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">@api_view</font>`<font style="color:rgb(92, 89, 98);">这个非常重要的装饰器，实现了以下几大功能：</font>

+ <font style="color:rgb(92, 89, 98);">与Django传统函数视图相区分，强调这是API视图，并限定了可以接受的请求方法。</font>
+ <font style="color:rgb(92, 89, 98);">拓展了django原来的request对象。新的request对象不仅仅支持request.POST提交的数据，还支持其它请求方式如PUT或PATCH等方式提交的数据，所有的数据都在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request.data</font>`<font style="color:rgb(92, 89, 98);">字典里。这对开发Web API非常有用。</font>

```python
request.POST  # 只处理表单数据, 只适用于'POST'方法
request.data  # 处理任意数据, 适用于'POST'，'PUT'和'PATCH'方法
```

**<font style="color:rgb(92, 89, 98);">注意</font>**<font style="color:rgb(92, 89, 98);">: 我们不再显式地将请求或响应绑定到特定的内容类型比如HttpResponse和JSONResponse，我们统一使用Response方法返回响应，该方法支持内容协商，可根据客户端请求的内容类型返回不同的响应数据。</font>

## <font style="color:rgb(39, 38, 43);">给URLs添加可选的格式后缀</font>
<font style="color:rgb(92, 89, 98);">为了充分利用我们的响应不再与单一内容类型连接，我们可以为API路径添加对格式后缀(.json或.api)的支持。使用格式后缀给我们明确指定了给定格式的URL，能让我们的API将能够处理诸如</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">http://example.com/api/items/4.json</font>`<font style="color:rgb(92, 89, 98);">之类的URL。</font>

<font style="color:rgb(92, 89, 98);">首先要给视图函数添加一个</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">format=None</font>`<font style="color:rgb(92, 89, 98);">关键字参数。</font>

```python
def article_list(request, format=None):
    def article_detail(request, pk, format=None):
```

<font style="color:rgb(92, 89, 98);">接着更新</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">blog/urls.py</font>`<font style="color:rgb(92, 89, 98);">文件，给现有的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">urlpatterns</font>`<font style="color:rgb(92, 89, 98);">加上</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">format_suffix_patterns</font>`<font style="color:rgb(92, 89, 98);">。</font>

```python
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    re_path(r'^articles/$', views.article_list),
    re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),]

urlpatterns = format_suffix_patterns(urlpatterns)
```

<font style="color:rgb(92, 89, 98);">最后我们还需要把app的urls加入到项目URL配置</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">apiproject/urls.py</font>`<font style="color:rgb(92, 89, 98);">文件中，如下所示：</font>

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('blog.urls')),
]
```

## <font style="color:rgb(39, 38, 43);">API测试</font>
<font style="color:rgb(92, 89, 98);">启动Django服务器后，就可以开始测试我们的API是否工作正常了。测试工具有很多，比如简便的curl命令和强大的postman，我们这里使用DRF自带的图形化测试界面。</font>

### <font style="color:rgb(39, 38, 43);">GET请求</font>
```python
[GET] http://127.0.0.1:8000/v1/articles
```

<font style="color:rgb(92, 89, 98);">发送GET请求到/v1/articles, 我们可以看HTTP=200 OK的字样和json格式的文章列表数据。</font>

<font style="color:rgb(92, 89, 98);">注意：DRF默认是以可浏览的api形式展示返回响应结果的(</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">articles.api</font>`<font style="color:rgb(92, 89, 98);">)，如果你只需要返回最简单的json格式的数据，只需要在访问地址后面加上</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">.json</font>`<font style="color:rgb(92, 89, 98);">后缀即可(articles.json)</font>

```python
[GET] http://127.0.0.1:8000/v1/articles/3
```

### <font style="color:rgb(39, 38, 43);">POST请求</font>
```python
[POST] http://127.0.0.1:8000/v1/articles
```

<font style="color:rgb(92, 89, 98);">发送POST请求到/v1/articles。在GET页面下方下拉框选择json格式数据或者表单，新增文章数据，点击POST提交后即可看到新的文章已经添加。</font>

### <font style="color:rgb(39, 38, 43);">PUT请求</font>
```python
[PUT] http://127.0.0.1:8000/v1/articles/3
```

<font style="color:rgb(92, 89, 98);">发送PUT请求到/v1/articles。在GET页面下方下拉框下选择json格式数据，数据为由序列化器中定义的非read-only字段组成的json对象，点击PUT提交后即可看到第3篇文章标题及状态已经由draft变成published。</font>

### <font style="color:rgb(39, 38, 43);">其它请求</font>
<font style="color:rgb(92, 89, 98);">DELETE请求非常简单，点击页面上DELETE按钮即可，这里就不展示了。HEAD和OPTIONS请求很少用，这里也不展示了。</font>

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本文介绍了DRF的两个序列化器类(Serializer类和ModelSerializer类), 并以博客为例使用基于函数的视图开发了两个简单的API端点并进行了测试。需要值得注意的有以下几点：</font>

1. <font style="color:rgb(92, 89, 98);">定义序列化器时一定要注意区分read-only字段和常规字段，read-only字段仅可读，用户不能通过POST或PUT方法对其进行修改。</font>
2. <font style="color:rgb(92, 89, 98);">DRF中使用函数视图开发API千万别忘了使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">@api_view</font>`<font style="color:rgb(92, 89, 98);">这个重要的装饰器。</font>

<font style="color:rgb(92, 89, 98);">在下篇文章中，我们将介绍关于DRF的基于类的视图，比如APIView类, GenericAPIView类和GenericViewSet类，并用它们重写本例中的API视图。</font>

