# 安装
## <font style="color:rgb(12, 60, 38);">安装 Apache 和</font><font style="color:rgb(12, 60, 38);"> </font>`**mod_wsgi**`[<font style="color:rgb(12, 60, 38);">¶</font>](https://docs.djangoproject.com/zh-hans/5.1/topics/install/#install-apache-and-mod-wsgi)
<font style="color:rgb(12, 60, 38);">如果您只是想试验 Django，请跳到下一部分；Django 包含一个可用于测试的轻量级 Web 服务器，因此在准备好在生产环境中部署 Django 之前，您不需要设置 Apache。</font>

<font style="color:rgb(12, 60, 38);">如果您想在生产站点上使用 Django，请使用</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">Apache</font>](https://httpd.apache.org/)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">与</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">mod_wsgi</font>](https://modwsgi.readthedocs.io/en/develop/)<font style="color:rgb(12, 60, 38);">。mod_wsgi 有两种模式：嵌入模式和守护模式。在嵌入模式下，mod_wsgi 类似于 mod_perl -- 它将 Python 嵌入到 Apache 中，并在服务器启动时将 Python 代码加载到内存中。代码在整个 Apache 进程的生命周期内保持在内存中，这会比其他服务器配置方式带来显著的性能提升。在守护模式下，mod_wsgi 会生成一个独立的守护进程来处理请求。守护进程可以以与 Web 服务器不同的用户身份运行，从而可能提高安全性。守护进程可以在不重新启动整个 Apache Web 服务器的情况下重新启动，从而可能使代码库的刷新更加无缝。请参考 mod_wsgi 文档以确定哪种模式适合您的设置。确保已安装 Apache 并启用了 mod_wsgi 模块。Django 将与支持 mod_wsgi 的任何版本的 Apache 配合使用。</font>

<font style="color:rgb(12, 60, 38);">若已安装 mod_wsgi 模块，请查看</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">Django 如何利用 mod_wsgi 工作</font>](https://docs.djangoproject.com/zh-hans/5.1/howto/deployment/wsgi/modwsgi/)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">了解如何配置。</font>

<font style="color:rgb(12, 60, 38);">如果由于某种原因你不能使用 mod_wsgi，请不要担心： Django 支持许多其他部署选项。一个是 </font>[<font style="color:rgb(12, 60, 38);">uWSGI</font>](https://docs.djangoproject.com/zh-hans/5.1/howto/deployment/wsgi/uwsgi/)<font style="color:rgb(12, 60, 38);"> ；它和 </font>[<font style="color:rgb(12, 60, 38);">nginx</font>](https://nginx.org/)<font style="color:rgb(12, 60, 38);"> 配合使用很好。此外，Django 遵循 WSGI 规范（ </font>[<font style="color:rgb(12, 60, 38);">PEP 3333</font>](https://peps.python.org/pep-3333/)<font style="color:rgb(12, 60, 38);"> ），允许它在各种服务器平台上运行。</font>

```python
pip install django
```

# 项目创建
```python
django-admin startproject 项目名
python manage.py startapp 应用名
python manage.py runserver
```

目录介绍

```python
polls/
__init__.py
admin.py
apps.py
migrations/
__init__.py
models.py
tests.py
views.py
```

## <font style="color:rgb(12, 60, 38);">使用模型</font>
<font style="color:rgb(12, 60, 38);">一旦你定义了你的模型，你需要告诉 Django 你准备</font><font style="color:rgb(12, 60, 38);"> </font>_<font style="color:rgb(12, 60, 38);">使用</font>_<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">这些模型。你需要修改设置文件中的</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">，在这个设置中添加包含</font><font style="color:rgb(12, 60, 38);"> </font>`**models.py**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">文件的模块名称。</font>

<font style="color:rgb(12, 60, 38);">例如，若模型位于项目中的</font><font style="color:rgb(12, 60, 38);"> </font>`**myapp.models**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">模块（ 此包结构由</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">manage.pystartapp</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-startapp)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">命令创建），</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">应设置如下：</font>

```python
INSTALLED_APPS = [
    # ...
    "myapp",
    # ...
]
```

<font style="color:rgb(12, 60, 38);">当你向 </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> 添加新的应用的时候，请务必运行 </font>[<font style="color:rgb(12, 60, 38);">manage.pymigrate</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-migrate)<font style="color:rgb(12, 60, 38);">，此外你也可以先使用以下命令进行迁移 </font>[<font style="color:rgb(12, 60, 38);">manage.pymakemigrations</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-makemigrations)<font style="color:rgb(12, 60, 38);">。</font>



# 数据库配置
## <font style="color:rgb(12, 60, 38);">数据库配置</font>
<font style="color:rgb(12, 60, 38);">现在，打开</font><font style="color:rgb(12, 60, 38);"> </font>`**mysite/settings.py**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">。这是个包含了 Django 项目设置的 Python 模块。</font>

<font style="color:rgb(12, 60, 38);">By default, the</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">DATABASES</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-DATABASES)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">configuration uses SQLite. If you're new to databases, or you're just interested in trying Django, this is the easiest choice. SQLite is included in Python, so you won't need to install anything else to support your database. When starting your first real project, however, you may want to use a more scalable database like PostgreSQL, to avoid database-switching headaches down the road.</font>

<font style="color:rgb(12, 60, 38);">If you wish to use another database, see</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">details to customize and get your database running</font>](https://docs.djangoproject.com/zh-hans/5.1/topics/install/#database-installation)<font style="color:rgb(12, 60, 38);">.</font>

<font style="color:rgb(12, 60, 38);">编辑</font><font style="color:rgb(12, 60, 38);"> </font>`**mysite/settings.py**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">文件前，先设置</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">TIME_ZONE</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-TIME_ZONE)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">为你自己时区。</font>

<font style="color:rgb(12, 60, 38);">此外，关注一下文件头部的</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">设置项。这里包括了会在你项目中启用的所有 Django 应用。应用能在多个项目中使用，你也可以打包并且发布应用，让别人使用它们。</font>

<font style="color:rgb(12, 60, 38);">通常，</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">默认包括了以下 Django 的自带应用：</font>

+ [<font style="color:rgb(12, 60, 38);">django.contrib.admin</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/contrib/admin/#module-django.contrib.admin)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">-- 管理员站点， 你很快就会使用它。</font>
+ [<font style="color:rgb(12, 60, 38);">django.contrib.auth</font>](https://docs.djangoproject.com/zh-hans/5.1/topics/auth/#module-django.contrib.auth)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">-- 认证授权系统。</font>
+ [<font style="color:rgb(12, 60, 38);">django.contrib.contenttypes</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/contrib/contenttypes/#module-django.contrib.contenttypes)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">-- 内容类型框架。</font>
+ [<font style="color:rgb(12, 60, 38);">django.contrib.sessions</font>](https://docs.djangoproject.com/zh-hans/5.1/topics/http/sessions/#module-django.contrib.sessions)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">-- 会话框架。</font>
+ [<font style="color:rgb(12, 60, 38);">django.contrib.messages</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/contrib/messages/#module-django.contrib.messages)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">-- 消息框架。</font>
+ [<font style="color:rgb(12, 60, 38);">django.contrib.staticfiles</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/contrib/staticfiles/#module-django.contrib.staticfiles)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">-- 管理静态文件的框架。</font>

<font style="color:rgb(12, 60, 38);">这些应用被默认启用是为了给常规项目提供方便。</font>

<font style="color:rgb(12, 60, 38);">默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下命令：</font>

/<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(187, 187, 187);"></font>

```python
python manage.py migrate
```

<font style="color:rgb(12, 60, 38);">这个</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">migrate</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-migrate)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">命令查看</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">配置，并根据</font><font style="color:rgb(12, 60, 38);"> </font>`**mysite/settings.py**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">文件中的数据库配置和随应用提供的数据库迁移文件（我们将在后面介绍这些），创建任何必要的数据库表。你会看到它应用的每一个迁移都有一个消息。如果你有兴趣，运行你的数据库的命令行客户端，输入</font><font style="color:rgb(12, 60, 38);"> </font>`**\dt**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">（PostgreSQL），</font><font style="color:rgb(12, 60, 38);"> </font>`**SHOW**** ****TABLES;**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">（MariaDB，MySQL），</font><font style="color:rgb(12, 60, 38);"> </font>`**.tables**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">（SQLite）或</font><font style="color:rgb(12, 60, 38);"> </font>`**SELECT**** ****TABLE_NAME**** ****FROM**** ****USER_TABLES;**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">（Oracle）来显示 Django 创建的表。</font>

**<font style="color:rgb(12, 60, 38);">写给极简主义者</font>**

<font style="color:rgb(12, 60, 38);">就像之前说的，为了方便大多数项目，我们默认激活了一些应用，但并不是每个人都需要它们。如果你不需要某个或某些应用，你可以在运行 </font>[<font style="color:rgb(12, 60, 38);">migrate</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-migrate)<font style="color:rgb(12, 60, 38);"> 前毫无顾虑地从 </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> 里注释或者删除掉它们。 </font>[<font style="color:rgb(12, 60, 38);">migrate</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-migrate)<font style="color:rgb(12, 60, 38);"> 命令只会为在 </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> 里声明了的应用进行数据库迁移。</font>

<font style="color:rgb(12, 60, 38);">新建以下模型</font>

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

## <font style="color:rgb(12, 60, 38);">激活模型</font>
<font style="color:rgb(12, 60, 38);">上面的一小段用于创建模型的代码给了 Django 很多信息，通过这些信息，Django 可以：</font>

+ <font style="color:rgb(12, 60, 38);">为这个应用创建数据库 schema（生成</font><font style="color:rgb(12, 60, 38);"> </font>`**CREATE**** ****TABLE**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">语句）。</font>
+ <font style="color:rgb(12, 60, 38);">创建可以与</font><font style="color:rgb(12, 60, 38);"> </font>`**Question**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">和</font><font style="color:rgb(12, 60, 38);"> </font>`**Choice**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">对象进行交互的 Python 数据库 API。</font>

<font style="color:rgb(12, 60, 38);">但是首先得把</font><font style="color:rgb(12, 60, 38);"> </font>`**polls**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">应用安装到我们的项目里。</font>

**<font style="color:rgb(12, 60, 38);">设计哲学</font>**

<font style="color:rgb(12, 60, 38);">Django 应用是“可插拔”的。你可以在多个项目中使用同一个应用。除此之外，你还可以发布自己的应用，因为它们并不会被绑定到当前安装的 Django 上。</font>

<font style="color:rgb(12, 60, 38);">为了在我们的工程中包含这个应用，我们需要在配置类 </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> 中添加设置。因为 </font>`**PollsConfig**`<font style="color:rgb(12, 60, 38);"> 类写在文件 </font>`**polls/apps.py**`<font style="color:rgb(12, 60, 38);"> 中，所以它的点式路径是 </font>`**'polls.apps.PollsConfig'**`<font style="color:rgb(12, 60, 38);">。在文件 </font>`**mysite/settings.py**`<font style="color:rgb(12, 60, 38);"> 中 </font>[<font style="color:rgb(12, 60, 38);">INSTALLED_APPS</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/settings/#std-setting-INSTALLED_APPS)<font style="color:rgb(12, 60, 38);"> 子项添加点式路径后，它看起来像这样：</font>

```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

<font style="color:rgb(12, 60, 38);">现在你的 Django 项目会包含</font><font style="color:rgb(12, 60, 38);"> </font>`**polls**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">应用。接着运行下面的命令：</font>

/<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(187, 187, 187);"></font>

```python
$ python manage.py makemigrations polls
    Migrations for 'polls':
      polls/migrations/0001_initial.py
        + Create model Question
        + Create model Choice
$  python manage.py check 
$ python manage.py sqlmigrate polls 0001
```

+ <font style="color:rgb(12, 60, 38);">编辑</font><font style="color:rgb(12, 60, 38);"> </font>`**models.py**`<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">文件，改变模型。</font>
+ <font style="color:rgb(12, 60, 38);">运行</font><font style="color:rgb(12, 60, 38);"> </font>[<font style="color:rgb(12, 60, 38);">python manage.py makemigrations</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-makemigrations)<font style="color:rgb(12, 60, 38);"> </font><font style="color:rgb(12, 60, 38);">为模型的改变生成迁移文件。</font>
+ <font style="color:rgb(12, 60, 38);">运行 </font>[<font style="color:rgb(12, 60, 38);">python manage.py migrate</font>](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-migrate)<font style="color:rgb(12, 60, 38);"> 来应用数据库迁移。</font>
+ <font style="color:rgb(12, 60, 38);">通过阅读文档 </font>[Django 后台文档](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/)<font style="color:rgb(12, 60, 38);"> ，你可以获得关于 </font>`**manage.py**`<font style="color:rgb(12, 60, 38);"> 工具的更多信息</font>

增删改查

```python
from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    """
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
        """

    def test_save(self):
        question = Question(question_text="Test question", pub_date=timezone.now())
        question.save()
        question = Question.objects.get(question_text="Test question")
        self.assertEqual(question.question_text, "Test question")

    def test_update(self):
        question = Question(question_text="Test question", pub_date=timezone.now())
        question.save()
        question = Question.objects.get(question_text="Test question")
        question.question_text = "liyedong"
        question.save()
        # question.question_text="Updated question"
        # question.save()
        restult = Question.objects.get(question_text="liyedong")
        self.assertEqual(restult.question_text, "liyedong")

    def test_select(self):
        question = Question(question_text="Test question", pub_date=timezone.now())
        question.save()
        question = Question.objects.get(question_text="Test question")
        self.assertEqual(question.question_text, "Test question")
        questions = Question.objects.all()
        self.assertIs(questions.count() > 0, True)

    def test_delete(self):
        question = Question(question_text="Test question", pub_date=timezone.now())
        question.save()
        question_delete = Question.objects.get(question_text="Test question")
        self.assertEqual(question_delete.question_text, "Test question")
        count, question_dict = question.delete()
        self.assertIs(count == 1, True)
        self.assertEqual(question_dict["polls.Question"], 1)

    def test_add_choice(self):
        question = Question(question_text="Test question", pub_date=timezone.now())
        question.save()
        choice_list = question.choice_set.all()
        self.assertEqual(choice_list.count(), 0)
        question.choice_set.create(choice_text="choice1", votes=0)
        question.choice_set.create(choice_text="choice2", votes=0)
        question.choice_set.create(choice_text="choice2", votes=0)
        question=Question.objects.get(question_text="Test question")
        choice_list = question.choice_set.all()
        self.assertEqual(choice_list.count(), 3)
    def test_select_choice(self):
        question = Question(question_text="Test question", pub_date=timezone.now())
        question.save()
        choice_list = question.choice_set.all()
        self.assertEqual(choice_list.count(), 0)
        question.choice_set.create(choice_text="choice1", votes=0)
        question.choice_set.create(choice_text="choice2", votes=0)
        question.choice_set.create(choice_text="choice2", votes=0)
        choices= Choice.objects.filter(question__question_text="Test question")
        self.assertEqual(choices.count(), 3)

```

## 运行这些测试
```python
python manage.py test polls
```

# 命名空间
```python
app_name = "xxx"
```

## <font style="color:rgb(39, 38, 43);"></font>
# <font style="color:rgb(39, 38, 43);">Django SimpleUI</font>
```python
poetry add django-simpleui
```

<font style="color:rgb(92, 89, 98);">修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 将</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">simpleui</font>`<font style="color:rgb(92, 89, 98);">加入到</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">INSTALLED_APPS</font>`<font style="color:rgb(92, 89, 98);">里去，放在第一行，也就是django自带admin的前面。</font>

```python
INSTALLED_APPS = [
    'simpleui', # 注意这里
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ...     
]
```

## <font style="color:rgb(39, 38, 43);">常用配置</font>
### <font style="color:rgb(39, 38, 43);">设置语言, 去Logo和管理后台名字</font>
<font style="color:rgb(92, 89, 98);">当你看到以上界面时，首先你想改动的一定是语言，去掉SimpleUI的默认logo，并把</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Django administration</font>`<font style="color:rgb(92, 89, 98);">改成比如某某管理后台的名字。</font>

<font style="color:rgb(92, 89, 98);">修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">， 添加如下代码：</font>

```python
# 更改默认语言为中文
LANGUAGE_CODE = 'zh-hans'

# 去掉默认Logo或换成自己Logo链接
SIMPLEUI_LOGO = 'https://th.bing.com/th/id/R2411a2b340731d67dfa0d84503e915e3?rik=zmYce%2fLys72JVQ&pid=ImgRaw'
```

<font style="color:rgb(92, 89, 98);">修改管理后台的名称和标题要稍微复杂些，因为你不能在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">里进行配置。在任何一个app的目录下新建一个</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">admin.py</font>`<font style="color:rgb(92, 89, 98);">, 添加如下代码即可修改(本例app名为tasks)。这个设置属于Django的设置，不属于SimpleUI的设置。</font>

```python
# tasks/admin.py
from django.contrib import admin

admin.site.site_header = '大江狗管理后台'  # 设置header
admin.site.site_title = '大江狗管理后台'   # 设置title
admin.site.index_title = '大江狗管理后台'

from .models import Task
admin.site.register(Task)
```

<font style="color:rgb(92, 89, 98);">现在你可以看到语言、Logo和管理后台名字都已经改过来了。但是你会发现两个问题，左侧菜单的tasks显示的依然是英文，我们需要将其设置成中文。另外，右侧有simpleui的广告链接，页面背后有js文件跟踪simpleui的使用，这些都需要关闭。我们接下来教你如何解决这两个问题。</font>

### <font style="color:rgb(39, 38, 43);">自定义或第三方APP名和模型名修改成中文</font>
<font style="color:rgb(92, 89, 98);">修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">tasks/app.py</font>`<font style="color:rgb(92, 89, 98);">, 通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">verbose_name</font>`<font style="color:rgb(92, 89, 98);">可以将app名改为中文，这里将</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">tasks</font>`<font style="color:rgb(92, 89, 98);"> </font><font style="color:rgb(92, 89, 98);">改成了</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">任务管理</font>`<font style="color:rgb(92, 89, 98);">。</font>

```python
from django.apps import AppConfig

class TasksConfig(AppConfig):
    name = 'tasks'

    verbose_name = '任务管理'
```

<font style="color:rgb(92, 89, 98);">接着修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">tasks/models.py</font>`<font style="color:rgb(92, 89, 98);">, 设置模型的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">verbose_name</font>`<font style="color:rgb(92, 89, 98);">, 如下所示：</font>

```python
from django.db import models

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"

    def __str__(self):
        return self.name
```

<font style="color:rgb(92, 89, 98);">现在刷新页面，你将看到tasks英文都变成中文了。</font>

<font style="color:rgb(92, 89, 98);">实际Django开发中，我们还会用到第三方应用app和第三方app提供的模型，我们也可以通过打补丁的方式更改第三方app或模型以及模型字段的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">verbose_name</font>`<font style="color:rgb(92, 89, 98);">或者</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">label</font>`<font style="color:rgb(92, 89, 98);">，将其修改成中文，如下所示：</font>

```python
from third_package.models import ModelA

ModelA._meta.verbose_name = ''
ModelA._meta.verbose_name_plural = ''
ModelA._meta.get_field('first_name').verbose_name = '名字'
```

### <font style="color:rgb(39, 38, 43);">关闭右侧广告链接和使用分析</font>
<font style="color:rgb(92, 89, 98);">修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 添加如下两行代码：</font>

```python
# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False 
SIMPLEUI_ANALYSIS = False
```

<font style="color:rgb(92, 89, 98);">现在查看效果，是不是清爽多了?</font>

<font style="color:rgb(92, 89, 98);">实际上首页的快捷操作和最近动作也可以关闭，在自定义首页部分我们会讲到。</font>

### <font style="color:rgb(39, 38, 43);">设置默认主题</font>
<font style="color:rgb(92, 89, 98);">SimpleUI默认主题(default)是深蓝色的，它支持的主题有</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Element-ui</font>`<font style="color:rgb(92, 89, 98);">,</font><font style="color:rgb(92, 89, 98);"> </font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Admin Lte</font>`<font style="color:rgb(92, 89, 98);">和</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">Layui</font>`<font style="color:rgb(92, 89, 98);">等多种风格。你可以通过右上角下拉菜单改变主题，也可以在</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">中设置默认主题，如下所示：</font>

```python
# 设置默认主题，指向主题css文件名。Admin Lte风格
SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'

# 设置默认主题，指向主题css文件名。Element-ui风格
SIMPLEUI_DEFAULT_THEME = 'element.css'

# 设置默认主题，指向主题css文件名。layui风格
SIMPLEUI_DEFAULT_THEME = 'layui.css'

# 设置默认主题，指向主题css文件名。紫色风格
SIMPLEUI_DEFAULT_THEME = 'purple.css'
```

### <font style="color:rgb(39, 38, 43);">自定义菜单</font>
<font style="color:rgb(92, 89, 98);">左侧可折叠菜单是Simple UI系统默认菜单，根据已注册的应用和模型自动生成，其中父级菜单是App名，子菜单一般是所属App的各个模型名。SimpleUI甚至会自动为你分配默认图标，比如本例的tasks的应用使用了font-awsome的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">fa fa-tasks</font>`<font style="color:rgb(92, 89, 98);">。在大多数情况下，Simple UI系统默认菜单不能满足需求，这时你就需要自定义菜单了，比如添加新的选项或给菜单选项分配新的图标。</font>

<font style="color:rgb(92, 89, 98);">修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 添加如下代码：</font>

```python
SIMPLEUI_CONFIG = {
    # 是否使用系统默认菜单。
    'system_keep': False,

    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。 空列表[] 为全部不显示.
    'menu_display': ['任务管理', '权限认证'],

    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时刷新展示菜单内容。
    # 一般建议关闭。
    'dynamic': False,
    'menus': [
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户列表',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
                {
                    'name': '用户组',
                    'icon': 'fa fa-th-list',
                    'url': 'auth/group/'
                }
            ]
        },

        {
            'name': '任务管理',
            'icon': 'fa fa-th-list',
            'models': [
                {
                    'name': '任务列表',
                    # 注意url按'/admin/应用名小写/模型名小写/'命名。  
                    'url': '/admin/tasks/task/',
                    'icon': 'fa fa-tasks'
                },
            ]
        },
    ]
}
```

<font style="color:rgb(92, 89, 98);">自定义菜单效果如下所示。我们更改了SimpleUI默认分配的图标。你还可以随意增减菜单选项并对其进行排序。</font>

<font style="color:rgb(92, 89, 98);">当然使用SimpleUI系统菜单也有优点，比如用户拥有什么模型的权限就显示什么菜单。自定义menus中输出的菜单不会受权限控制。如果你想要在后台使用基于RBAC控制的菜单，就不要通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">SIMPLEUI_CONFIG</font>`<font style="color:rgb(92, 89, 98);">自定义菜单。如果你不喜欢，系统默认的菜单图标，只需要通过</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">SIMPLEUI_ICON</font>`<font style="color:rgb(92, 89, 98);">定义即可，如下所示：</font>

```python
# 注意key名为菜单上实际显示的名字，不是模型或App名。
SIMPLEUI_ICON = {
    '任务管理': 'fas fa-tasks',
    '任务': 'fas fa-th-list',
}
```

### <font style="color:rgb(39, 38, 43);">自定义首页</font>
<font style="color:rgb(92, 89, 98);">SimpleUI默认首页由快捷链接和最近动作组成，我们可以将其隐藏，并将其链接到其它url。</font>

<font style="color:rgb(92, 89, 98);">继续修改</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 添加如下代码：</font>

```python
# 隐藏首页的快捷操作和最近动作
SIMPLEUI_HOME_QUICK = False 
SIMPLEUI_HOME_ACTION = False

# 修改左侧菜单首页设置
SIMPLEUI_HOME_PAGE = 'https://www.baidu.com'  # 指向页面
SIMPLEUI_HOME_TITLE = '百度欢迎你!' # 首页标题
SIMPLEUI_HOME_ICON = 'fa fa-code' # 首页图标

# 设置右上角Home图标跳转链接，会以另外一个窗口打开
SIMPLEUI_INDEX = 'https://www.baidu.com'
```

<font style="color:rgb(92, 89, 98);">实际应用中后台首页通常是控制面板，需要用图表形式展示各种关键数据，这时就需要重写首页了。这里主要有两种实现方法。第一种是重写simpleui自带的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">home.html</font>`<font style="color:rgb(92, 89, 98);">, 另一种自己编写一个控制面板的页面，然后设置首页指向它, 个人倾向于第二种, 因为它完全不涉及改动simpleui的源码。</font>

<font style="color:rgb(92, 89, 98);">我们现在开始使用Django编写一个用于显示控制面板的页面，用于在首页显示注册用户数量及任务数量。URL路由及对应的视图函数如下所示：</font>

```python
# tasks/urls.py
urlpatterns = [
    path('tasks/dashboard/', views.dashboard, name='dashboard'),
]

# tasks/views.py
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Task

def dashboard(request):
    user_count = User.objects.count()
    task_count = Task.objects.count()

    context = { 'user_count': user_count, 'task_count': task_count }
    return render(request, 'tasks/dashboard.html',context)
```

<font style="color:rgb(92, 89, 98);">我们的模板也很简单，使用了boostrap4的admin lte风格的卡片展示用户总数和任务总数。</font>

```python
<!DOCTYPE html>
 <html>
  <head>
  <meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>控制面板</title>
<!-- Tell the browser to be responsive to screen width -->
<meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Theme style -->
    <link rel="stylesheet" href="https://adminlte.io/themes/AdminLTE/bower_components/bootstrap/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://adminlte.io/themes/AdminLTE/dist/css/AdminLTE.min.css">
</head>

<body>
<div class="wrapper">
 <!-- Main content -->
    <section class="content">
      <div class="container-fluid">
        <!-- Small boxes (Stat box) -->
        <div class="row">
          <div class="col-sm-3">
            <!-- small box -->
            <div class="small-box bg-info">
              <div class="inner">
                <h3>{{ user_count }}</h3>

                <p>用户总数</p>
              </div>
              <div class="icon">
                <i class="ion ion-bag"></i>
              </div>
              <a href="#" class="small-box-footer">更多信息 <i class="fas fa-arrow-circle-right"></i></a>
            </div>
          </div>
          <!-- ./col -->
          <div class="col-sm-3">
            <!-- small box -->
            <div class="small-box bg-success">
              <div class="inner">
                <h3>{{ task_count }}</h3>
                <p>任务总数</p>
              </div>
              <div class="icon">
                <i class="ion ion-stats-bars"></i>
              </div>
              <a href="#" class="small-box-footer">更多信息 <i class="fas fa-arrow-circle-right"></i></a>
            </div>
          </div>
          <!-- ./col -->
             <div class="col-sm-3">
            <!-- small box -->
            <div class="small-box bg-info">
              <div class="inner">
                <h3>{{ user_count }}</h3>

                <p>用户总数</p>
              </div>
              <div class="icon">
                <i class="ion ion-bag"></i>
              </div>
              <a href="#" class="small-box-footer">更多信息 <i class="fas fa-arrow-circle-right"></i></a>
            </div>
          </div>
          <!-- ./col -->
          <div class="col-sm-3">
            <!-- small box -->
            <div class="small-box bg-success">
              <div class="inner">
                <h3>{{ task_count }}</h3>

                <p>任务总数</p>
              </div>
              <div class="icon">
                <i class="ion ion-stats-bars"></i>
              </div>
              <a href="#" class="small-box-footer">更多信息 <i class="fas fa-arrow-circle-right"></i></a>
            </div>
          </div>
          <!-- ./col -->

        </div>
      </div>
    </section>
  </div>
</body>
```

<font style="color:rgb(92, 89, 98);">现在修改我们的</font>`<font style="color:rgb(92, 89, 98);background-color:rgb(245, 246, 250);">settings.py</font>`<font style="color:rgb(92, 89, 98);">, 将首页指向这个新创建的控制面板。</font>

```python
# 修改首页设置, 指向新创建的控制面板
SIMPLEUI_HOME_PAGE = '/tasks/dashboard/'
SIMPLEUI_HOME_TITLE = '控制面板!' 
SIMPLEUI_HOME_ICON = 'fa fa-eye'
```

<font style="color:rgb(92, 89, 98);">刷新浏览器，你就会发现我们的首页已经修改了，是不是很酷?</font>

### <font style="color:rgb(39, 38, 43);">其它常见配置</font>
```python
# 离线模式。不填该项或者为False的时候，默认从第三方的cdn获取
SIMPLEUI_STATIC_OFFLINE = False
# 关闭Loading遮罩层
SIMPLEUI_LOADING = False
# 关闭登录界面粒子动画
SIMPLEUI_LOGIN_PARTICLES = False
```

# <font style="color:rgb(39, 38, 43);"></font>
