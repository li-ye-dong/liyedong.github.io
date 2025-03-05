<font style="color:rgb(92, 89, 98);">Django 框架包含了一个信号机制，它允许若干个发送者（sender）通知一组接收者（receiver）某些特定操作或事件(events)已经发生了， 接收者收到指令信号(signals)后再去执行特定的操作。本文主要讲解Django信号(signals)的工作机制、应用场景，如何在项目中使用信号以及如何自定义信号。</font>

## <font style="color:rgb(39, 38, 43);">信号的工作机制</font>
<font style="color:rgb(92, 89, 98);">Django 中的信号工作机制依赖如下三个主要要素：</font>

+ <font style="color:rgb(92, 89, 98);">发送者（sender）：信号的发出方，可以是模型，也可以是视图。当某个操作发生时，发送者会发出信号。</font>
+ <font style="color:rgb(92, 89, 98);">信号（signal）：发送的信号本身。Django内置了许多信号，比如模型保存后发出的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_save</font>`<font style="color:rgb(92, 89, 98);">信号。</font>
+ <font style="color:rgb(92, 89, 98);">接收者（receiver）：信号的接收者，其本质是一个简单的回调函数。将这个函数注册到信号上，当特定的事件发生时，发送者发送信号，回调函数就会被执行。</font>

## <font style="color:rgb(39, 38, 43);">信号的应用场景</font>
<font style="color:rgb(92, 89, 98);">信号主要用于Django项目内不同事件的联动，实现程序的解耦。比如当模型A有变动时，模型B与模型C收到发出的信号后同步更新。又或当一个数据表数据有所改变时，监听这个信号的函数可以及时清除已失效的缓存。另外通知也是一个信号常用的场景，比如有人刚刚回复了你的贴子，可以通过信号进行推送。</font>

**<font style="color:rgb(92, 89, 98);">注意</font>**<font style="color:rgb(92, 89, 98);">：Django中信号监听函数不是异步执行，而是同步执行，所以需要异步执行耗时的任务时(比如发送邮件或写入文件)，不建议使用Django自带的信号。</font>

## <font style="color:rgb(39, 38, 43);">两个简单例子</font>
<font style="color:rgb(92, 89, 98);">假如我们有一个Profile模型，与User模型是一对一的关系。我们希望创建User对象实例时自动创建Profile对象实例，而更新User对象实例时不创建新的Profile对象实例。这时我们就可以自定义</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">create_user_profile</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">save_user_profile</font>`<font style="color:rgb(92, 89, 98);">两个监听函数，同时监听sender (User模型)发出的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_save</font>`<font style="color:rgb(92, 89, 98);">信号。由于</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_save</font>`<font style="color:rgb(92, 89, 98);">可同时用于模型的创建和更新，我们用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">if created</font>`<font style="color:rgb(92, 89, 98);">这个判断来加以区别。</font>

```plain
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

# 监听User模型创建    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
   if created:
       Profile.objects.create(user=instance)

# 监听User模型更新  
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```

<font style="color:rgb(92, 89, 98);">我们再来看一个使用信号清除缓存的例子。当模型A被更新或被删除时，会分别发出</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_save</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_delete</font>`<font style="color:rgb(92, 89, 98);">的信号，监听这两个信号的receivers函数会自动清除缓存里的A对象列表。</font>

```plain
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

@receiver(post_save, sender=ModelA)
def cache_post_save_handler(sender, **kwargs):
    cache.delete('cached_a_objects')
    
@receiver(post_delete, sender=ModelA)
def cache_post_delete_handler(sender, **kwargs):
     cache.delete('cached_a_objects')
```

<font style="color:rgb(92, 89, 98);">注意：有时为了防止信号多次发送，可以通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">dispatch_uid</font>`<font style="color:rgb(92, 89, 98);">给receiver函数提供唯一标识符。</font>

```plain
@receiver(post_delete, sender=ModelA, dispatch_uid = "unique_identifier")
```

## <font style="color:rgb(39, 38, 43);">Django常用内置信号</font>
<font style="color:rgb(92, 89, 98);">前面例子我们仅仅使用了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_save</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_delete</font>`<font style="color:rgb(92, 89, 98);">信号。Django还内置了其它常用信号：</font>

+ <font style="color:rgb(92, 89, 98);">pre_save & post_save: 在模型调用 save()方法之前或之后发送。</font>
+ <font style="color:rgb(92, 89, 98);">pre_init& post_init: 在模型调用_init_方法之前或之后发送。</font>
+ <font style="color:rgb(92, 89, 98);">pre_delete & post_delete: 在模型调用delete()方法或查询集调用delete() 方法之前或之后发送。</font>
+ <font style="color:rgb(92, 89, 98);">m2m_changed: 在模型多对多关系改变后发送。</font>
+ <font style="color:rgb(92, 89, 98);">request_started & request_finished: Django建立或关闭HTTP 请求时发送。</font>

<font style="color:rgb(92, 89, 98);">这些信号都非常有用。举个例子：使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">pre_save</font>`<font style="color:rgb(92, 89, 98);">信号可以在将用户的评论存入数据库前对其进行过滤，或则检测一个模型对象的字段是否发生了变更。</font>

**<font style="color:rgb(92, 89, 98);">注意</font>**<font style="color:rgb(92, 89, 98);">：监听</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">pre_save</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_save</font>`<font style="color:rgb(92, 89, 98);">信号的回调函数不能再调用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">save()</font>`<font style="color:rgb(92, 89, 98);">方法，否则回出现死循环。另外Django的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">update</font>`<font style="color:rgb(92, 89, 98);">方法不会发出</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">pre_save</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">post_save</font>`<font style="color:rgb(92, 89, 98);">的信号。</font>

## <font style="color:rgb(39, 38, 43);">如何放置信号监听函数代码</font>
<font style="color:rgb(92, 89, 98);">在之前案例中，我们将Django信号的监听函数写在了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">models.py</font>`<font style="color:rgb(92, 89, 98);">文件里。当一个app的与信号相关的自定义监听函数很多时，此时models.py代码将变得非常臃肿。一个更好的方式把所以自定义的信号监听函数集中放在app对应文件夹下的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">signals.py</font>`<font style="color:rgb(92, 89, 98);">文件里，便于后期集中维护。</font>

<font style="color:rgb(92, 89, 98);">假如我们有个</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">account</font>`<font style="color:rgb(92, 89, 98);">的app，包含了User和Profile模型，我们首先需要在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">account</font>`<font style="color:rgb(92, 89, 98);">文件夹下新建</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">signals.py</font>`<font style="color:rgb(92, 89, 98);">，如下所示：</font>

```plain
# account/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
      Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
```

<font style="color:rgb(92, 89, 98);">接下来我们需要修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">account</font>`<font style="color:rgb(92, 89, 98);">文件下</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">apps.py</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">__init__.py</font>`<font style="color:rgb(92, 89, 98);">，以导入创建的信号监听函数。</font>

```plain
# apps.py
from django.apps import AppConfig
 
class AccountConfig(AppConfig):
    name = 'account'
 
    def ready(self):
        import account.signals
        
# account/__init__.py中增加如下代码：
default_app_config = 'account.apps.AccountConfig'
```

## <font style="color:rgb(39, 38, 43);">自定义信号</font>
<font style="color:rgb(92, 89, 98);">Django的内置信号在大多数情况下能满足我们的项目需求，但有时我们还需要使用自定义的信号。在Django项目中使用自定义信号也比较简单，分三步即可完成。</font>

### <font style="color:rgb(39, 38, 43);">第一步：自定义信号</font>
<font style="color:rgb(92, 89, 98);">每个自定义的信号，都是Signal类的实例。这里我们首先在app目录下新建一个</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">signals.py</font>`<font style="color:rgb(92, 89, 98);">文件，创建一个名为</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">my_signal</font>`<font style="color:rgb(92, 89, 98);">的信号，它包含有</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">msg</font>`<font style="color:rgb(92, 89, 98);">这个参数，这个参数在信号触发的时候需要传递。当监听函数收到这个信号时，会得到</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">msg</font>`<font style="color:rgb(92, 89, 98);">参数的值。</font>

```plain
from django.dispatch import Signal

my_signal = Signal(providing_args=['msg'])
```

### <font style="color:rgb(39, 38, 43);">第二步：触发信号</font>
<font style="color:rgb(92, 89, 98);">视图中进行某个操作时可以使用</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">send</font>`<font style="color:rgb(92, 89, 98);">方法触发自定义的信号，并设定</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">msg</font>`<font style="color:rgb(92, 89, 98);">的值。</font>

```plain
from . import signals
# Create your views here.

def index(request):
    signals.my_signal.send(sender=None, msg='Hello world')
    return render(request, template_name='index.html')
```

### <font style="color:rgb(39, 38, 43);">第三步：将监听函数与信号相关联</font>
```plain
from django.dispatch import Signal, Receiver

my_signal = Signal(providing_args=['msg'])

@receiver(my_signal)
def my_signal_callback(sender, **kwargs):
    print(kwargs['msg']) # 打印Hello world!
```

<font style="color:rgb(92, 89, 98);">这样每当用户访问/index/视图时，Django都会发出</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">my_signal</font>`<font style="color:rgb(92, 89, 98);">的信号(包含msg这个参数)。回调函数收到这个信号后就会打印出msg的值来。</font>

## <font style="color:rgb(39, 38, 43);">小结</font>
<font style="color:rgb(92, 89, 98);">在本文里我们总结了Django信号(signals)的工作机制及应用场景，介绍了如何在Django项目中使用信号实现事件的联动。最后我们还总结了Django常用内置信号以及如何自定义信号。Django信号还有非常多的应用场景等着你去发现。</font>

