### Django用户模型类
```python
from django.contrib.auth.models import User
```

Django的Auth认证系统中提供了用户模型类User保存用户的数据，默认的User包含以下常见的基本字段：

| 字段名 | 字段描述 |
| --- | --- |
| `username` | 必选。150个字符以内。 用户名可能包含字母数字，`_`，`@`，`+` `.` 和`-`个字符。 |
| `first_name` | 可选（`blank=True`）。 少于等于30个字符。 |
| `last_name` | 可选（`blank=True`）。 少于等于30个字符。 |
| `email` | 可选（`blank=True`）。 邮箱地址。 |
| `password` | 必选。 密码的哈希加密串。 （Django 不保存原始密码）。 原始密码可以无限长而且可以包含任意字符。 |
| `groups` | 与`Group` 之间的多对多关系。对接权限功能的。 |
| `user_permissions` | 与`Permission` 之间的多对多关系。对接权限功能的。 |
| `is_staff` | 布尔值。 设置用户是否可以访问Admin 站点。 |
| `is_active` | 布尔值。 指示用户的账号是否激活。 它不是用来控制用户是否能够登录，而是描述一种帐号的使用状态。值为False的时候，是无法登录的。 |
| `is_superuser` | 是否是超级用户。超级用户具有所有权限。 |
| `last_login` | 用户最后一次登录的时间。 |
| `date_joined` | 账户创建的时间。 当账号创建时，默认设置为当前的date/time。 |


##### 模型提供的常用方法：
模型常用方法可以通过`user实例对象.方法名`来进行调用。

+ `set_password`(_raw_password_)设置用户的密码为给定的原始字符串，并负责密码的。 不会保存`User` 对象。当`None`为`raw_password` 时，密码将设置为一个不可用的密码。
+ `check_password`(_raw_password_)如果给定的raw_password是用户的真实密码，则返回True，可以在校验用户密码时使用。

##### 管理器的常用方法：
管理器方法可以通过`User.objects.` 进行调用。

+ `create_user`(_username_, _email=None_, _password=None_, **_extra_fields_)创建、保存并返回一个`User`对象。
+ `create_superuser`(_username_, _email_, _password_, **_extra_fields_)与`create_user()` 相同，但是设置`is_staff` 和`is_superuser` 为`True`。

虽然上面的User模型看起来很多的属性和方法了，但是我们当前要实现的项目是一个在线教育商城，所以我们还需要记录用户的手机号，或者头像等等一系列信息。所以我们需要在原有模型的基础上对这个模型进行改造。

所以我们需要自定义一个新的users子应用并在django原有功能的基础上，完善用户的登录注册功能。

### 创建用户模块的子应用
```shell
cd luffycityapi/apps/
python ../../manage.py startapp users
```

在settings/dev.py文件中注册子应用。

```python
INSTALLED_APPS = [
    ...
      'users',
]
```

创建users/urls.py子路由并在总路由中进行注册。

users/urls.py，代码：

```python
from django.urls import path
from . import views
urlpatterns = [

]
```

luffycityapi/urls.py，总路由，代码：

```python
from django.contrib import admin
from django.urls import path,re_path,include

from django.conf import settings
from django.views.static import serve # 静态文件代理访问模块

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'uploads/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    path("", include("home.urls")),
    path("users/", include("users.urls")),
]
```

### 创建自定义的用户模型类
Django认证系统中提供的用户模型类及方法很方便，我们可以使用这个模型类，但是字段有些无法满足项目需求，如本项目中需要保存用户的手机号，需要给模型类添加额外的字段。

Django提供了`django.contrib.auth.models.AbstractUser`用户抽象模型类允许我们继承，扩展字段来使用Django认证系统的用户模型类。

**我们可以在apps中创建Django应用users，并在配置文件中注册users应用。**

在创建好的应用models.py中定义用户的用户模型类。

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True, verbose_name='手机号')
    money = models.DecimalField(max_digits=9, default=0.0, decimal_places=2, verbose_name="钱包余额")
    credit = models.IntegerField(default=0, verbose_name="积分")
    avatar = models.ImageField(upload_to="avatar/%Y", null=True, default="", verbose_name="个人头像")
    nickname = models.CharField(max_length=50, default="", null=True, verbose_name="用户昵称")

    class Meta:
        db_table = 'lf_users'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
```

我们自定义的用户模型类还不能直接被Django的认证系统所识别，需要在配置文件中告知Django认证系统使用我们自定义的模型类。

在settings/dev.py配置文件中进行设置

```python
AUTH_USER_MODEL = 'users.User'
```

`AUTH_USER_MODEL` 参数的设置以`点.`来分隔，表示`应用名.模型类名`。

**注意：Django建议我们对于AUTH_USER_MODEL参数的设置一定要在第一次数据库迁移之前就设置好，否则后续使用可能出现未知错误。**

这是表示有一个叫admin的子应用使用了原来的废弃的auth.User模型，但是目前数据库已经设置了默认的子应用为`users`的模型了，所以产生了冲突。那么这种冲突，我们需要重置下原来的auth模块的迁移操作，再次迁移就可以解决了。

```plain
解决步骤：
1. 备份数据库[如果刚开始开发，无需备份。]
   cd /home/moluo/Desktop/luffycity/docs
   mysqldump -uroot -p123 luffycity > 03_20_luffycity.sql

2. 注释掉users.User代码以及AUTH_USER_MODEL配置项，然后执行数据迁移回滚操作，把冲突的所有表迁移记录全部归零
   cd ~/Desktop/luffycity/luffycityapi
   # python manage.py migrate <子应用目录> zero
   python manage.py migrate auth zero

3. 恢复users.User代码以及AUTH_USER_MODEL配置项，执行数据迁移。
   python manage.py makemigrations
   python manage.py migrate
4. 创建管理员查看auth功能是否能正常使用。
   python manage.py createsuperuser
```

