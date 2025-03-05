<font style="color:rgb(92, 89, 98);">缓存(Cache)对于创建一个高性能的网站和提升用户体验来说是至关重要。本章将介绍缓存Cache应用场景及工作原理，并详细介绍如何在Django中设置缓存Cache并使用它们。</font>

## <font style="color:rgb(39, 38, 43);">什么是缓存Cache?</font>
<font style="color:rgb(92, 89, 98);">缓存是一类可以更快的读取数据的介质统称，也指其它可以加快数据读取的存储方式。一般用来存储临时数据，常用介质的是读取速度很快的内存。一般来说从数据库多次把所需要的数据提取出来，要比从内存或者硬盘等一次读出来付出的成本大很多。对于中大型网站而言，使用缓存减少对数据库的访问次数是提升网站性能的关键之一。</font>

## <font style="color:rgb(39, 38, 43);">为什么要使用缓存Cache?</font>
<font style="color:rgb(92, 89, 98);">当用户请求到达Django的视图后，视图会先从数据库读取数据传递给模板进行渲染，返回给用户看到的网页。如果用户每次请求都从数据库读取数据并渲染，将极大降低性能，不仅服务器压力大，而且客户端也无法即时获得响应。如果能将</font>**<font style="color:rgb(92, 89, 98);">数据库中读取的数据</font>**<font style="color:rgb(92, 89, 98);">或</font>**<font style="color:rgb(92, 89, 98);">动态生成的网页</font>**<font style="color:rgb(92, 89, 98);">放到速度更快的缓存中，每次有请求过来，先检查缓存中是否有对应的资源，如果有，直接从缓存中取出来返回响应，节省读取数据和渲染的时间，不仅能大大提高系统性能，还能提高用户体验。</font>

<font style="color:rgb(92, 89, 98);">我们来看一个实际的博客例子。每当我们访问首页/index/时，下面视图就会从数据库中读取文章列表，并与模板结合动态地生成网页。大多数情况下，我们的博客不会更新得那么频繁，所以文章列表和首页都是不变的。这样用户在一定时间内多次访问首页时每次都从数据库重新读取同样的数据再进行渲染是一种很大的浪费。</font>

```python
from django.shortcuts import render
from .models import Article

def index(request):
    # 读取数据库等并渲染到网页
    article_list = Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})
```

<font style="color:rgb(92, 89, 98);">服务器端使用缓存Cache就可以帮我们解决这个问题。当第一个用户首次访问博客首页时，我们将从数据库中读取的数据或动态生成的网页存储到缓存里(常用的是内存，这取决于你的设置)。当这个用户或其它更多用户在一定时间内多次请求访问首页时, Django先检查缓存里用户请求的数据或网页是否已经存在，如果存在，直接从缓存中读取相关内容，展示给用户。如果数据不存在或缓存已过期，则重新读取数据建立缓存。这就是</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">cache_page</font>`<font style="color:rgb(92, 89, 98);">这个装饰器的作用，如下所示：</font>

```python
from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # 这里指缓存 15 分钟
def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', {'article_list': article_list})
```

## <font style="color:rgb(39, 38, 43);">缓存Cache的应用场景</font>
<font style="color:rgb(92, 89, 98);">缓存主要适用于对页面实时性要求不高的页面。存放在缓存的数据，通常是频繁访问而又不会经常修改的数据。我们来举几个应用例子:</font>

+ <font style="color:rgb(92, 89, 98);">个人博客：假设用户平均一天更新一篇文章，那么可以设置1天的全站缓存，一天后会刷新。</font>
+ <font style="color:rgb(92, 89, 98);">购物网站：商品的描述信息几乎不会变化，而商品的购买数量需要根据用户情况实时更新。我们可以只选择缓存商品描述信息。</font>
+ <font style="color:rgb(92, 89, 98);">缓存网页片段：比如缓存网页导航菜单和脚部(Footer)。</font>
+ <font style="color:rgb(92, 89, 98);">热点信息： 比如短时间内新闻点击排行，这些热点数据不需要存入到关系型数据库里，放到缓存里即可。</font>

## <font style="color:rgb(39, 38, 43);">Django缓存设置</font>
<font style="color:rgb(92, 89, 98);">Django中提供了多种缓存方式，如果要使用缓存，需要先在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">中进行配置，然后应用。根据缓存介质的不同，你需要设置不同的缓存后台Backend。在生产环境中最常用的缓存是Memcached和Redis。在开发环境中可以使用本地内存缓存进行测试。</font>

### <font style="color:rgb(39, 38, 43);">Memcached缓存</font>
<font style="color:rgb(92, 89, 98);">Memcached是一个高性能的分布式内存对象缓存系统，是Django原生支持的最快最有效的缓存系统。Memcached的优点是速度快，属于分布式缓存，支持同时在多台服务器上运行 (Django会把它们当成一个大缓存)，缺点是不支持数据持久化，服务器重启后缓存数据就没了。</font>

**<font style="color:rgb(92, 89, 98);">第一步：安装Memcached</font>**

+ <font style="color:rgb(92, 89, 98);">windows系统：官网下载，解压安装即可。</font>
+ <font style="color:rgb(92, 89, 98);">Linux系统：Ubuntu系统需要使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">sudo apt-get install libevent ibevent-dev</font>`<font style="color:rgb(92, 89, 98);">安装Memcached依赖环境，再使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">sudo apt-get install memcached</font>`<font style="color:rgb(92, 89, 98);">安装memcached。</font>

<font style="color:rgb(92, 89, 98);">如何安装参考菜鸟网教程：https://www.runoob.com/memcached/memcached-tutorial.html</font>

<font style="color:rgb(92, 89, 98);">**第二步：启动Memcached **</font>

```python
# Linux系统-前台启动
/usr/local/memcached/bin/memcached -p 11211 -m 64m -vv
# Linux系统-作为后台服务启动
/usr/local/memcached/bin/memcached -p 11211 -m 64m -d
```

**<font style="color:rgb(92, 89, 98);">第三步：pip安装python-memcached</font>**

<font style="color:rgb(92, 89, 98);">Python操作memcached数据库需要安装</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">python-memcached</font>`<font style="color:rgb(92, 89, 98);">或</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">pylibmc</font>`<font style="color:rgb(92, 89, 98);">, 推荐前者。</font>

```python
pip install pyhon-memcached
```

**<font style="color:rgb(92, 89, 98);">第四步：将memcached设为Django缓存后台</font>**

```python
# 本地缓存，使用localhost
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# 使用unix soket通信
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
    }
}   

# 分布式缓存，多台服务器，支持配置权重。
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '172.19.26.240:11211',
            '172.19.26.242:11211',
        ]
        # 我们也可以给缓存机器加权重，权重高的承担更多的请求，如下：
        'LOCATION': [
            ('172.19.26.240:11211',5),
            ('172.19.26.242:11211',1),
        ]
    }
}
```

### <font style="color:rgb(39, 38, 43);">Redis缓存</font>
<font style="color:rgb(92, 89, 98);">Redis 是当今速度最快的内存型非关系型（NoSQL）型数据库。Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等多种数据结构的存储。与memcached相比，Redis不仅支持支持缓存数据在硬盘上的持久化，还支持master-slave模式的数据备份，有明显的优点。</font>

**<font style="color:rgb(92, 89, 98);">第一步：安装Redis</font>**

+ <font style="color:rgb(92, 89, 98);">windows系统：官网下载，解压安装即可, 记得勾上加入环境变量。</font>
+ <font style="color:rgb(92, 89, 98);">Linux系统：Ubuntu系统可使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">sudo apt-get install redis-server</font>`<font style="color:rgb(92, 89, 98);">安装。</font>

**<font style="color:rgb(92, 89, 98);">第二步：启动Redis服务</font>**

```python
# Windows系统：cmd进入redis安装目录，启动redis服务
redis-server.exe redis.windows.conf

# Linux系统：进入redis安装目录启动redis服务
redis-server /etc/redis/redis.conf 

# 打开redis交互命令行，用于测试(可选)
redis-cli.exe -h 127.0.0.1 -p 6379 # windows系统下另打开一个窗口
redis-cli # linux系统
```

<font style="color:rgb(92, 89, 98);">注意：默认情况下，访问Redis服务器是不需要密码的，为了让其他服务器使用同增加安全性我们建议设置Redis服务器的访问密码。</font>

<font style="color:rgb(92, 89, 98);">由于redis默认绑定本机的，所以第一步取消该设置：</font>

```python
#编辑配置文件
sudo vim /etc/redis/redis.conf
```

<font style="color:rgb(92, 89, 98);">用vim打开该配置文件后，注释掉下面这行：</font>

```python
# bind 127.0.0.1
```

<font style="color:rgb(92, 89, 98);">然后设置登录密码。由于配置文件较长，命令模式下输入</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">/requirepass foobared</font>`<font style="color:rgb(92, 89, 98);">快速搜索该配置项：</font>

```python
#找到下面这一行并去除注释，未修改之前：
#requirepass foobared

#修改成：
requirepass your_pwd #设置新的密码
```

<font style="color:rgb(92, 89, 98);">修改后使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">redis-server restart</font>`<font style="color:rgb(92, 89, 98);">重启服务器使配置生效。以后从其它服务器访问redis时携带你设置的密码即可：</font>

```python
redis-cli -a your_pwd -h hostip
```

**<font style="color:rgb(92, 89, 98);">第三步：pip安装django-redis</font>**

<font style="color:rgb(92, 89, 98);">Redis安装好并且启动后，你还需要通过pip安装</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">django-redis</font>`<font style="color:rgb(92, 89, 98);">才能在Django中操作redis数据库。</font>

```python
pip install django-redis
```

**<font style="color:rgb(92, 89, 98);">第四步：将Redis设为Django缓存后台</font>**

```python
CACHES = {

    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://your_host_ip:6379', # redis所在服务器或容器ip地址
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "your_pwd", # 你设置的密码
        },
    },
}
```

<font style="color:rgb(92, 89, 98);">你还可以在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">设置缓存默认过期时间（非必须)。</font>

```python
REDIS_TIMEOUT=24*60*60
CUBES_REDIS_TIMEOUT=60*30
NEVER_REDIS_TIMEOUT=365*24*60*60
```

### <font style="color:rgb(39, 38, 43);">数据库缓存</font>
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
```

<font style="color:rgb(92, 89, 98);">使用数据库缓存前需要先使用如下命令创建缓存数据表：</font>

```python
python manage.py createcachetable
```

### <font style="color:rgb(39, 38, 43);">文件系统缓存</font>
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',#这个是文件夹的路径
        #'LOCATION': 'c:\foo\bar',# windows下的示例
    }
}
```

### <font style="color:rgb(39, 38, 43);">本地内存缓存</font>
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake' # 名字随便定
    }
}
```

### <font style="color:rgb(39, 38, 43);">Dummy缓存</font>
<font style="color:rgb(92, 89, 98);">不做任何实际缓存，仅用于测试目的。</font>

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
```

## <font style="color:rgb(39, 38, 43);">测试缓存是否设置成功</font>
<font style="color:rgb(92, 89, 98);">在你修改完</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">中关于缓存的配置后，你一定想知道Django缓存是否设置成功。你可以输入下面命令打开Python的命令交互窗口：</font>

```python
python manage.py shell
```

<font style="color:rgb(92, 89, 98);">然后逐条输入以下命令进行测试。如果无任何报错，说明你缓存设置成功。</font>

```python
from django.core.cache import cache  #引入缓存模块

cache.set('k1', '555', 60*1)   #写入key为k1，值为555的缓存，有效期1分钟
cache.has_key('k1')#判断key为k1是否存在
cache.get('k1')   #获取key为k1的缓存结果
```

## <font style="color:rgb(39, 38, 43);">Django项目中使用缓存</font>
<font style="color:rgb(92, 89, 98);">当你做好有关缓存(Cache)的设置后，在Django项目中你可以有四种方式使用Cache。</font>

+ <font style="color:rgb(92, 89, 98);">全站缓存</font>
+ <font style="color:rgb(92, 89, 98);">在视图View中使用</font>
+ <font style="color:rgb(92, 89, 98);">在路由URLConf中使用</font>
+ <font style="color:rgb(92, 89, 98);">在模板中使用</font>

<font style="color:rgb(92, 89, 98);">### 全站缓存</font>

<font style="color:rgb(92, 89, 98);">全站缓存(per-site)是依赖中间件实现的，也是Django项目中使用缓存最简单的方式。这种缓存方式仅适用于静态网站或动态内容很少的网站。</font>

```python
# 缓存中间件，添加顺序很重要
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',     # 新增
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',  # 新增
]

# 其它设置
CACHE_MIDDLEWARE_ALIAS = 'default'  # 缓存别名
CACHE_MIDDLEWARE_SECONDS = '600'    # 缓存时间
CACHE_MIDDLEWARE_KEY_PREFIX = ''    # 缓存别名前缀
```

### <font style="color:rgb(39, 38, 43);">在视图View中使用</font>
<font style="color:rgb(92, 89, 98);">此种缓存方式依赖</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">@cache_page</font>`<font style="color:rgb(92, 89, 98);">这个装饰器，仅适合内容不怎么变化的单个视图页面。</font>

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def my_view(request):
    ...
```

### <font style="color:rgb(39, 38, 43);">路由URLConf中使用</font>
<font style="color:rgb(92, 89, 98);">同样</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">@cache_page</font>`<font style="color:rgb(92, 89, 98);">这个装饰器，只不过在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">urls.py</font>`<font style="color:rgb(92, 89, 98);">中使用。</font>

```python
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('articles/<int:id>/', cache_page(60 * 15)(my_view)),
]
```

### <font style="color:rgb(39, 38, 43);">模板中使用缓存</font>
<font style="color:rgb(92, 89, 98);">与</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">@cache_page</font>`<font style="color:rgb(92, 89, 98);">缓存整个页面不同，模板缓存的颗粒度更细，可以用来缓存内容不怎么变化的 HTML 片段。具体的使用方式如下，首先加载</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);"> </font><font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">cache</font>`<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">过滤器，然后使用模板标签语法把需要缓存的片段包围起来即可。</font>

```python
{% load cache %}
{% cache 500 sidebar request.user.username %}
.. sidebar for logged in user ..
{% endcache %}
```

## <font style="color:rgb(39, 38, 43);">自定义缓存和清除缓存</font>
<font style="color:rgb(92, 89, 98);">实际缓存应用中，Django提供的缓存中间件、装饰器或者模板cache标签的颗粒度还是不够细，有时候你需要在视图中自定义数据缓存，如下所示：</font>

```python
from django.core.cache import cache

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    objects = cache.get('cached_objects')

    if objects is None:
        objects = MyModel.objects.all()
        cache.set('cached_objects', objects)

    context['objects'] = objects

    return context
```

<font style="color:rgb(92, 89, 98);">当你的模型有所变化(比如删除或更新)时，你还需及时地清除老的缓存，这个可以通过Django的信号机制实现。</font>

```python
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

@receiver(post_delete, sender=MyModel)
def cache_post_delete_handler(sender, **kwargs):
    cache.delete('cached_objects')

@receiver(post_save, sender=MyModel)
def cache_post_save_handler(sender, **kwargs):
    cache.delete('cached_objects')
```

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本章总结了Django项目中如何设置缓存后台以及如何在视图和模板中使用缓存，提高网站性能和用户体验。</font>

