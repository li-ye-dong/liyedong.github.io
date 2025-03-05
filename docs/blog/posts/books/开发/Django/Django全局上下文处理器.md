<font style="color:rgb(92, 89, 98);">Django的全局上下文处理器(Context Processors)的作用就是向模板传递需要全局使用的变量。今天小编就来带大家一起来看看这把利器，并教你如何自定义全局上下文处理器(Context Processors)。</font>

## <font style="color:rgb(39, 38, 43);">全局上下文处理器(Context Processors)应用场景</font>
<font style="color:rgb(92, 89, 98);">当你需要向所有模板传递一个可以被全局使用的变量时。在编写Django视图函数时，我们一般会在视图函数中以Python字典(dict)形式向模板中传递需要被调用或使用的变量并指定渲染模板。通常情况下，我们向模板的传递的字典变量与模板是一一对应的关系。有时我们还需要向模板传递全局变量，即每个模板都需要使用到的变量(比如站点名称, 博客的最新文章列表)。</font>

<font style="color:rgb(92, 89, 98);">如果每个视图函数分别去查询数据库，然后向每个模板传递这些变量，不仅造成代码冗余，而且会造成对数据库的重复查询。一个更好的解决方案就是使用自定义的上下文处理器(Context Processors)给模板传递全局变量，一次查询全局使用，完美解决了这些问题。</font>

## <font style="color:rgb(39, 38, 43);">Django内置的全局上下文处理器</font>
<font style="color:rgb(92, 89, 98);">你或许没有自定义过自己的全局上下文处理器(Context Processors)，但你一定使用过Django内置的全局上下文处理器(Context Processors)。举个例子，虽然你没有向某个模板中传递过权限perms对象，你却可以在所有模板中随时调用它（如下所示)。同样可以在模板中全局使用的变量还有request和user对象。</font>

<font style="color:rgb(92, 89, 98);">为什么？因为Django的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">里已经包含了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">django.template.context_processors.request</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">django.contrib.auth.context_processors.auth</font>`<font style="color:rgb(92, 89, 98);">这两个全局上下文处理器。如果你把他们移除， 看看还能不能在模板中调用</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">user</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">perms</font>`<font style="color:rgb(92, 89, 98);">?</font>

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ # 以下包含了4个默认的全局上下文处理器
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myapp.custom_context_processors.xxx',  # 自定义全局上下文处理器
            ],
        },
    },
]
```

<font style="color:rgb(92, 89, 98);">Django一般包含了上述4个默认全局上下文处理器，它们作用如下所示：</font>

+ <font style="color:rgb(92, 89, 98);">django.template.context_processors.debug：在模板里面可以直接使用settings的DEBUG参数以及强大的sql_queries:它本身是一个字典，其中包括当前页面执行SQL查询所需的时间</font>
+ <font style="color:rgb(92, 89, 98);">django.template.context_processors.request：在模板中可以直接使用request对象</font>
+ <font style="color:rgb(92, 89, 98);">django.contrib.auth.context_processors.auth：在模板里面可以直接使用user，perms对象。</font>
+ <font style="color:rgb(92, 89, 98);">django.contrib.messages.context_processors.messages：在模板里面可以直接使用message对象。</font>

<font style="color:rgb(92, 89, 98);">另外Django还提供了几个全局上下文处理器：</font>

+ <font style="color:rgb(92, 89, 98);">django.template.context_processors.i18n：在模板里面可以直接使用settings的LANGUAGES和LANGUAGE_CODE</font>
+ <font style="color:rgb(92, 89, 98);">django.template.context_processors.media：可以在模板里面使用settings的MEDIA_URL参数</font>
+ <font style="color:rgb(92, 89, 98);">django.template.context_processors.csrf : 给模板标签 csrf_token提供值</font>
+ <font style="color:rgb(92, 89, 98);">django.template.context_processors.tz: 可以在模板里面使用 TIME_ZONE参数。</font>

## <font style="color:rgb(39, 38, 43);">如何自定义全局上下文处理器</font>
<font style="color:rgb(92, 89, 98);">自定义的全局上下文处理器本质上是个函数，使用它必须满足3个条件：</font>

1. <font style="color:rgb(92, 89, 98);">传入参数必须有</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">request</font>`<font style="color:rgb(92, 89, 98);">对象</font>
2. <font style="color:rgb(92, 89, 98);">返回值必须是个字典</font>
3. <font style="color:rgb(92, 89, 98);">使用前需要在settings的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">context_processors</font>`<font style="color:rgb(92, 89, 98);">里申明。</font>

<font style="color:rgb(92, 89, 98);">我们通常会把自定义的上下文处理器函数放在单独命名的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">context_processors.py</font>`<font style="color:rgb(92, 89, 98);">里，这个python文件可以放在project目录下，也可以放在某个app的目录下。</font>

<font style="color:rgb(92, 89, 98);">接下来我们来看一个具体例子。我们需要向所有模板传递一个叫</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">site_name</font>`<font style="color:rgb(92, 89, 98);">的全局变量以便在所有模板中直接使用</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">site_name</font>`<font style="color:rgb(92, 89, 98);">输出站点名称，我们可以在blog(应用名)的目录下新建</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">context_processors.py</font>`<font style="color:rgb(92, 89, 98);">，新增如下代码：</font>

```python
# blog/context_processors.py

from django.conf import settings
def global_site_name(request):
    return {'site_name': settings.SITE_NAME,}
```

<font style="color:rgb(92, 89, 98);">然后可以在settings.py里声明：</font>

```python
'context_processors': [ # 以下包含了4个默认的全局上下文处理器
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'blog.context_processors.global_site_name',  # 自定义全局上下文处理器
]
```

## <font style="color:rgb(39, 38, 43);">全局变量与本地变量的优先级</font>
<font style="color:rgb(92, 89, 98);">全局上下文处理器提供的变量优先级高于单个视图函数给单个模板传递的变量。这意味着全局上下文处理器提供的变量可能会覆盖你视图函数中自定义的本地变量，因此请注意避免本地变量名与全局上下文处理器提供的变量名称重复。这些变量名包括perms, user和debug等等。</font>

<font style="color:rgb(92, 89, 98);">如果你希望单个视图函数定义的变量名覆盖全局变量，请使用以下强制模式：</font>

```python
from django.template import RequestContext

high_priority_context = RequestContext(request)
high_priority_context.push({"my_name": "Adrian"})
```

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">本文总结了什么是Django的全局上下文处理器(Context Processors)，它的应用场景及如何自定义使用自己的全局上下文处理器，希望大家喜欢。</font>

