```python
pip install celery
```

**<font style="color:rgb(28, 30, 31);">这里还是拿django来举例，目录结构调整如下：</font>**

```plain
luffycityapi/           # 服务端项目根目录
└── luffycityapi/       # 主应用目录
    ├── apps/           # 子应用存储目录  
    ├   └── users/            # django的子应用
    ├       └── tasks.py      # [新增]分散在各个子应用下的异步任务模块
    ├── settings/     # [修改]django的配置文件存储目录[celery的配置信息填写在django配置中即可]
    ├── __init__.py   # [修改]设置当前包目录下允许外界调用celery应用实例对象
    └── celery.py     # [新增]celery入口程序，相当于上一种用法的main.py
```

**<font style="color:rgb(28, 30, 31);">luffycityapi/celery.py，主应用目录下创建cerley入口程序，创建celery对象并加载配置和异步任务，代码：</font>**

```python
import logging
import os
from celery import Celery

# 必须在实例化celery应用对象之前执行
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffycityapi.settings.dev')

# 实例化celery应用对象
app = Celery('luffycityapi')
# 指定任务的队列名称
app.conf.task_default_queue = 'Celery'

# 也可以把配置写在django的项目配置中
app.config_from_object('django.conf:settings', namespace='CELERY') # 设置django中配置信息以 "CELERY_"开头为celery的配置信息
# 自动根据配置查找django的所有子应用下的tasks任务文件
app.autodiscover_tasks()


```

**<font style="color:rgb(28, 30, 31);">settings/dev.py，django配置中新增celery相关配置信息，代码：</font>**  
 

```python
# Celery异步任务队列框架的配置项[注意：django的配置项必须大写，所以这里的所有配置项必须全部大写]
# 任务队列
# 有些情况防止死锁
CELERYD_FORCE_EXECV = True
# 任务失败允许重试
#CELERY_ACKS_LATE = True  废弃   6.0以后使用以下
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
# 验证任务确认机制
CELERY_TASK_ACKS_LATE=True
#线程池模式，windows下使用最佳，因为进程池模式运行会出现权限等问题，导致任务无法确认，无法进入队列被消费
CELERY_WORKER_POOL = 'threads'  # 使用线程池
#CELERY_WORKER_POOL = 'prefork'  # 使用进程池
# Worker并发数量，一般默认CPU核数，可以不设置
CELERY_WORKER_CONCURRENCY = 4  # CELERYD_CONCURRENCY = 4
# 每个worker最多执行的任务数，超过这个就将worker进行销毁，防止内存泄漏，默认无限
CELERYD_MAX_TASKS_PER_CHILD = 100
# 单个任务运行的最大时间，超过这个时间，task就会被kill
CELERY_TASK_TIME_LIMIT = 1 * 1
# 过期时间,默认一天
CELERY_RESULT_EXPIRES = 30 * 60

# 任务限流
# CELERY_TASK_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
# 指定 Broker 使用 Redis，Broker 负责任务的分发和调度
CELERY_BROKER_URL = 'redis://:123456@127.0.0.1:6379/11'
# 指定结果存储 Backend 使用 Redis，Backend 负责存储任务执行结果
CELERY_RESULT_BACKEND = 'redis://:123456@127.0.0.1:6379/12'
# Celery的日志配置
# 禁用 Celery 自己的日志系统，使用 Django 配置的日志
CELERY_TASK_LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s',
CELERY_RESULT_LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s',
CELERY_WORKER_HIJACK_ROOT_LOGGER = False  # 防止 Celery 劫持根日志记录器
# 定时任务
# CELERYBEAT_SCHEDULE = {
#     'task1': {
#         'task': 'upload-task',  # 指定任务名称
#         'schedule': datetime.timedelta(seconds=5),  # 任务执行时间，每5秒执行一次
#         'options': {
#             'queue': 'beat_tasks' # 指定队列
#         }
#     }
# }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR.parent / "logs/luffycity.log",  # 确保logs文件夹已经存在
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose',
        },
        # Celery的日志文件处理
        'celery_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR.parent / "logs/celery.log",  # Celery日志的文件路径
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        # 为celery配置日志
        'celery': {
            'handlers': ['console', 'celery_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

**<font style="color:rgb(28, 30, 31);">users/tasks.py，代码：</font>**

```python
from celery import shared_task
# from ronglianyunapi import send_sms as sms
# 记录日志：
import logging
from send_email import EmailUtil

logger = logging.getLogger('celery')


# @shared_task(name="send_sms")
# def send_sms(tid, mobile, datas):
#     """异步发送短信"""
#     try:
#         return sms(tid, mobile, datas)
#     except Exception as e:
#         logger.error(f"手机号：{mobile}，发送短信失败错误: {e}")
@shared_task(name="send_email",queue='Celery')
def send_email(recipient, datas):
    """发送邮件"""
    logger.info(f"发送邮件到：{recipient}")
    return EmailUtil.send_code_email(recipient=recipient, code=datas)

@shared_task(name="send_sms")
def send_sms(tid, mobile, datas):
    """异步发送短信"""
    try:
        return sms(tid, mobile, datas)
    except Exception as e:
        logger.error(f"手机号：{mobile}，发送短信失败错误: {e}")

@shared_task(name="send_sms1")
def send_sms1():
    print("send_sms1执行了！！！")

```

  
 **<font style="color:rgb(28, 30, 31);">users/views，视图中调用异步发送短信的任务，代码：</font>**

```python
from .tasks import send_sms
send_sms.delay(settings.RONGLIANYUN.get("reg_tid"),mobile, datas=(code, time // 60))
```

  
 

