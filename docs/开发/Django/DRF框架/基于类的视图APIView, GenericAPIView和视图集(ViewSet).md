## <font style="color:rgb(39, 38, 43);">使用基础APIView类</font>
<font style="color:rgb(92, 89, 98);">DRF的APIView类继承了Django自带的View类, 一样可以按请求方法调用不同的处理函数，比如get方法处理GET请求，post方法处理POST请求。不过DRF的APIView要强大得多。它不仅支持更多请求方法，而且对Django的request对象进行了封装，可以使用request.data获取用户通过POST, PUT和PATCH方法发过来的数据，而且支持插拔式地配置认证、权限和限流类。</font>

<font style="color:rgb(92, 89, 98);">现在我们可以使用APIView类重写我们之前的函数视图了。</font>

```python
# blog/views.py
# 使用基础APIView类

from rest_framework.views import APIView
from django.http import Http404
from .models import Article
from .serializers import ArticleSerializer

class ArticleList(APIView):
    """
    List all articles, or create a new article.
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

<font style="color:rgb(92, 89, 98);">或许你已经注意到，这段代码跟之前基于函数的视图差别并不大。最大不同的是我们不需要在对用户的请求方法进行判断。该视图可以自动将不同请求转发到相应处理方法，逻辑上也更清晰。</font>

<font style="color:rgb(92, 89, 98);">现在我们还需要修改应用的url配置, 让其指向新的基于类的视图。注意：类视图需要调用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">as_view()</font>`<font style="color:rgb(92, 89, 98);">的方法才能在视图中实现查找指定方法, 比如GET请求执行get方法。</font>

  
 

## <font style="color:rgb(39, 38, 43);">使用通用视图Generics.*类</font>
<font style="color:rgb(92, 89, 98);">将Mixin类和GenericAPI类混配，已经帮助我们减少了一些代码，但我们还可以做得更好，比如将get请求与mixin提供的list方法进行绑定感觉有些多余。幸好DRF还提供了一套常用的将 Mixin 类与 GenericAPI类已经组合好了的视图，开箱即用，可以进一步简化我们的代码，如下所示：</font>

```python
# generic class-based views
from rest_framework import generics

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # 将request.user与author绑定
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class =ArticleSerializer
```

<font style="color:rgb(92, 89, 98);">顾名思义，</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">generics.ListCreateAPIView</font>`<font style="color:rgb(92, 89, 98);">类支持List、Create两种视图功能，分别对应GET和POST请求。</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">generics.RetrieveUpdateDestroyAPIView</font>`<font style="color:rgb(92, 89, 98);">支持Retrieve、Update、Destroy操作，其对应方法分别是GET、PUT和DELETE。</font>

<font style="color:rgb(92, 89, 98);">寥寥几行，实现了我们所有想要的功能，神不神奇?</font>

<font style="color:rgb(92, 89, 98);">其它常用generics类视图还包括</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ListAPIView</font>`<font style="color:rgb(92, 89, 98);">,</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">RetrieveAPIView</font>`<font style="color:rgb(92, 89, 98);">,</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">RetrieveUpdateAPIView</font>`<font style="color:rgb(92, 89, 98);">等等。你可以根据实际需求使用，为你的API写视图时只需要定义</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">queryset</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">serializer_class</font>`<font style="color:rgb(92, 89, 98);">即可。</font>

## <font style="color:rgb(39, 38, 43);">使用视图集ViewSet</font>
<font style="color:rgb(92, 89, 98);">使用通用视图generics类后视图代码已经大大简化，但是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ArticleList</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ArticleDetail</font>`<font style="color:rgb(92, 89, 98);">两个类中</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">queryset</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">serializer_class</font>`<font style="color:rgb(92, 89, 98);">属性依然存在代码重复。使用视图集可以将两个类视图进一步合并，一次性提供List、Create、Retrieve、Update、Destroy这5种常见操作，这样</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">queryset</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">seralizer_class</font>`<font style="color:rgb(92, 89, 98);">属性也只需定义一次就好, 这就变成了视图集(viewset)。</font>

<font style="color:rgb(92, 89, 98);">如下所示：</font>

```python
# blog/views.py
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    # 用一个视图集替代ArticleList和ArticleDetail两个视图
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # 自行添加，将request.user与author绑定
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

<font style="color:rgb(92, 89, 98);">使用视图集后，我们需要使用DRF提供的路由router来分发urls，因为一个视图集现在对应多个urls，而不像之前的一个url对应一个视图函数或一个视图类。</font>

```python
# blog/urls.py
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', viewset=views.ArticleViewSet)

urlpatterns = [
    # re_path(r'^articles/$', views.ArticleList.as_view()),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
```

<font style="color:rgb(92, 89, 98);">你或许又要问了，一个视图集对应List、Create、Retrieve、Update、Destroy这5种操作。有时候我只需要其中的一种或几种操作，该如何实现呢？答案是在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">urls.py</font>`<font style="color:rgb(92, 89, 98);">中指定方法映射即可，如下所示：</font>

```python
# blog/urls.py

from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'articles', viewset=views.ArticleViewSet)

article_list = views.ArticleViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    })

article_detail = views.ArticleViewSet.as_view({
    'get': 'retrieve', # 只处理get请求，获取单个记录
})


urlpatterns = [
    re_path(r'^articles/$', article_list),
    re_path(r'^articles/(?P<pk>[0-9]+)$', article_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

<font style="color:rgb(92, 89, 98);">另外DRF还提供了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">ReadOnlyModelViewSet</font>`<font style="color:rgb(92, 89, 98);">这个类，它仅支持list和retrive这两个可读的操作，如下所示：</font>

```python
from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ReadOnlyModelViewSet仅提供list和detail可读动作
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

<font style="color:rgb(92, 89, 98);">Django视图集viewset代码最少，但这是以牺牲了代码的可读性为代价的，因为它对代码进行了高度地抽象化。另外urls由router生成，不如自己手动配置的清楚。</font>

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本文使用了DRF提供的多种基于类的API视图的重写了文章资源API。那么这几种方式到底哪种更好呢? 答案是各有利弊。小编个人认为大家只需掌握以下三种方式即可：</font>

+ <font style="color:rgb(92, 89, 98);">基础的API类：可读性最高、代码最多、灵活性最高。当你需要对的API行为进行个性化定制时，建议使用这种方式。</font>
+ <font style="color:rgb(92, 89, 98);">通用generics类：可读性好、代码适中、灵活性较高。当你需要对一个模型进行标准的增删查改全部或部分操作时建议使用这种方式。</font>
+ <font style="color:rgb(92, 89, 98);">使用视图集viewset: 可读性较低、代码最少、灵活性最低。当你需要对一个模型进行标准的增删查改的全部操作且不需定制API行为时建议使用这种方式。</font>

