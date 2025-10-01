## <font style="color:rgb(31, 35, 40);">FastAPI 最佳实践</font>
<font style="color:rgb(31, 35, 40);">我在创业公司中使用的最佳实践和惯例的主观列表。</font>

<font style="color:rgb(31, 35, 40);">在过去的几年里，我们一直在生产环境中做出一些好的和坏的决定，这些决定极大地影响了我们的开发者体验。其中一些值得分享。</font>

## <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">内容</font>
+ [项目结构](https://github.com/zhanymkanov/fastapi-best-practices#project-structure)
+ [异步路由](https://github.com/zhanymkanov/fastapi-best-practices#async-routes)
    - [I/O 密集型任务](https://github.com/zhanymkanov/fastapi-best-practices#io-intensive-tasks)
    - [CPU 密集型任务](https://github.com/zhanymkanov/fastapi-best-practices#cpu-intensive-tasks)
+ [依赖](https://github.com/zhanymkanov/fastapi-best-practices#pydantic)
    - [超越传统的依赖注入用途](https://github.com/zhanymkanov/fastapi-best-practices#excessively-use-pydantic)
    - [自定义基础模型](https://github.com/zhanymkanov/fastapi-best-practices#custom-base-model)
    - [解耦 Pydantic BaseSettings](https://github.com/zhanymkanov/fastapi-best-practices#decouple-pydantic-basesettings)
+ [依赖项](https://github.com/zhanymkanov/fastapi-best-practices#dependencies)
    - [超越依赖注入](https://github.com/zhanymkanov/fastapi-best-practices#beyond-dependency-injection)
    - [链式依赖](https://github.com/zhanymkanov/fastapi-best-practices#chain-dependencies)
    - [解耦并重用依赖项。依赖项调用会被缓存](https://github.com/zhanymkanov/fastapi-best-practices#decouple--reuse-dependencies-dependency-calls-are-cached)
    - [优先考虑async依赖](https://github.com/zhanymkanov/fastapi-best-practices#prefer-async-dependencies)
+ [各种各样的](https://github.com/zhanymkanov/fastapi-best-practices#miscellaneous)
    - [遵循 REST](https://github.com/zhanymkanov/fastapi-best-practices#follow-the-rest)
    - [FastAPI 响应序列化](https://github.com/zhanymkanov/fastapi-best-practices#fastapi-response-serialization)
    - [如果必须使用同步 SDK，则在线程池中运行它。](https://github.com/zhanymkanov/fastapi-best-practices#if-you-must-use-sync-sdk-then-run-it-in-a-thread-pool)
    - [ValueErrors 可能会变成 Pydantic ValidationError](https://github.com/zhanymkanov/fastapi-best-practices#valueerrors-might-become-pydantic-validationerror)
    - [文档](https://github.com/zhanymkanov/fastapi-best-practices#docs)
    - [设置数据库键命名约定](https://github.com/zhanymkanov/fastapi-best-practices#set-db-keys-naming-conventions)
    - [数据迁移](https://github.com/zhanymkanov/fastapi-best-practices#migrations-alembic)
    - [设置数据库命名约定](https://github.com/zhanymkanov/fastapi-best-practices#set-db-naming-conventions)
    - [SQL 优先，Pydantic 其次](https://github.com/zhanymkanov/fastapi-best-practices#sql-first-pydantic-second)
    - [从第 0 天开始设置测试客户端异步](https://github.com/zhanymkanov/fastapi-best-practices#set-tests-client-async-from-day-0)
    - [使用皱褶](https://github.com/zhanymkanov/fastapi-best-practices#use-ruff)
+ [奖金部分](https://github.com/zhanymkanov/fastapi-best-practices#bonus-section)

## <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">项目结构</font>
<font style="color:rgb(31, 35, 40);">构建项目的方法有很多种，但最好的结构是一致、直接、没有意外的结构。</font>

<font style="color:rgb(31, 35, 40);">许多示例项目和教程会根据文件类型（例如 CRUD、Router、Model）来划分项目，这对于微服务或范围较小的项目来说非常有效。然而，这种方法并不适合我们这个包含多个领域和模块的单体应用。</font>

<font style="color:rgb(31, 35, 40);">我发现在这些情况下更具可扩展性和可进化性的结构受到 Netflix 的</font><font style="color:rgb(31, 35, 40);"> </font>[Dispatch](https://github.com/Netflix/dispatch)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">的启发，并进行了一些细微的修改。</font>

```python
fastapi-project
├── alembic/
    ├── src
    │   ├── auth
    │   │   ├── router.py
    │   │   ├── schemas.py  # pydantic models
    │   │   ├── models.py  # db models
    │   │   ├── dependencies.py
    │   │   ├── config.py  # local configs
    │   │   ├── constants.py
    │   │   ├── exceptions.py
    │   │   ├── service.py
    │   │   └── utils.py
    │   ├── aws
    │   │   ├── client.py  # client model for external service communication
    │   │   ├── schemas.py
    │   │   ├── config.py
    │   │   ├── constants.py
    │   │   ├── exceptions.py
    │   │   └── utils.py
    │   └── posts
    │   │   ├── router.py
    │   │   ├── schemas.py
    │   │   ├── models.py
    │   │   ├── dependencies.py
    │   │   ├── constants.py
    │   │   ├── exceptions.py
    │   │   ├── service.py
    │   │   └── utils.py
    │   ├── config.py  # global configs
    │   ├── models.py  # global models
    │   ├── exceptions.py  # global exceptions
    │   ├── pagination.py  # global module e.g. pagination
    │   ├── database.py  # db connection related stuff
    │   └── main.py
    ├── tests/
    │   ├── auth
    │   ├── aws
    │   └── posts
    ├── templates/
    │   └── index.html
    ├── requirements
    │   ├── base.txt
    │   ├── dev.txt
│   └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini
```

1. <font style="color:rgb(31, 35, 40);">将所有域目录存储在</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">src</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">文件夹</font><font style="color:rgb(31, 35, 40);">中</font>
    1. `<font style="color:rgb(31, 35, 40);">src/</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">-应用程序的最高级别，包含通用模型、配置和常量等。</font>
    2. `<font style="color:rgb(31, 35, 40);">src/main.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 项目的根目录，用于初始化 FastAPI 应用程序</font>
2. <font style="color:rgb(31, 35, 40);">每个包都有自己的路由器、模式、模型等。</font>
    1. `<font style="color:rgb(31, 35, 40);">router.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 是每个模块的核心，包含所有端点</font>
    2. `<font style="color:rgb(31, 35, 40);">schemas.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 用于 pydantic 模型</font>
    3. `<font style="color:rgb(31, 35, 40);">models.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 用于数据库模型</font>
    4. `<font style="color:rgb(31, 35, 40);">service.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 模块特定的业务逻辑</font>
    5. `<font style="color:rgb(31, 35, 40);">dependencies.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 路由器依赖项</font>
    6. `<font style="color:rgb(31, 35, 40);">constants.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 模块特定的常量和错误代码</font>
    7. `<font style="color:rgb(31, 35, 40);">config.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 例如环境变量</font>
    8. `<font style="color:rgb(31, 35, 40);">utils.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 非业务逻辑功能，例如响应规范化、数据丰富等。</font>
    9. `<font style="color:rgb(31, 35, 40);">exceptions.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">- 模块特定异常，例如</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">PostNotFound</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">InvalidUserData</font>`
3. <font style="color:rgb(31, 35, 40);">当包需要来自其他包的服务、依赖项或常量时 - 使用明确的模块名称导入它们</font>

```python
from src.auth import constants as auth_constants
from src.notifications import service as notification_service
from src.posts.constants import ErrorCode as PostsErrorCode  # in case we have Standard ErrorCode in constants module of each package
```

## <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">异步路由</font>
<font style="color:rgb(31, 35, 40);">首先，FastAPI 是一个异步框架。它被设计用于处理异步 I/O 操作，这就是它如此快速的原因。</font>

<font style="color:rgb(31, 35, 40);">然而，FastAPI 并不限制你只能使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">async</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">路由，开发者也可以使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">sync</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">路由。这可能会让初学者误以为它们是相同的，但事实并非如此。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">I/O 密集型任务</font>
<font style="color:rgb(31, 35, 40);">在底层，FastAPI 可以</font>[有效地处理](https://fastapi.tiangolo.com/async/#path-operation-functions)<font style="color:rgb(31, 35, 40);">异步和同步 I/O 操作。</font>

+ <font style="color:rgb(31, 35, 40);">FastAPI 在</font>[线程池中](https://en.wikipedia.org/wiki/Thread_pool)<font style="color:rgb(31, 35, 40);">运行</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">sync</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">路由 阻塞 I/O 操作不会停止</font>[事件循环](https://docs.python.org/3/library/asyncio-eventloop.html)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">执行任务。</font>
+ <font style="color:rgb(31, 35, 40);">如果路由定义为</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">async</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，则通过</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">await</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">定期调用它 并且 FastAPI 相信您只执行非阻塞 I/O 操作。</font>

<font style="color:rgb(31, 35, 40);">需要注意的是，如果您违反该信任并在异步路由中执行阻塞操作，则事件循环将无法运行后续任务，直到阻塞操作完成。</font>

```python
import asyncio
import time

from fastapi import APIRouter


router = APIRouter()


@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, the whole process will be blocked

    return {"pong": True}

@router.get("/good-ping")
def good_ping():
    time.sleep(10) # I/O blocking operation for 10 seconds, but in a separate thread for the whole `good_ping` route

    return {"pong": True}

@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10) # non-blocking I/O operation

    return {"pong": True}
```

**<font style="color:rgb(31, 35, 40);">当我们调用时会发生什么：</font>**

1. `<font style="color:rgb(31, 35, 40);">GET /terrible-ping</font>`
    1. <font style="color:rgb(31, 35, 40);">FastAPI 服务器接收请求并开始处理</font>
    2. <font style="color:rgb(31, 35, 40);">服务器的事件循环和队列中的所有任务将等待，直到</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">time.sleep()</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">完成</font>
        1. <font style="color:rgb(31, 35, 40);">服务器认为</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">time.sleep()</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">不是 I/O 任务，因此它会等待直到它完成</font>
        2. <font style="color:rgb(31, 35, 40);">服务器在等待期间不会接受任何新请求</font>
    3. <font style="color:rgb(31, 35, 40);">服务器返回响应。</font>
        1. <font style="color:rgb(31, 35, 40);">响应后，服务器开始接受新的请求</font>
2. `<font style="color:rgb(31, 35, 40);">GET /good-ping</font>`
    1. <font style="color:rgb(31, 35, 40);">FastAPI 服务器接收请求并开始处理</font>
    2. <font style="color:rgb(31, 35, 40);">FastAPI 将整个路由</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">good_ping</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">发送到线程池，其中工作线程将运行该函数</font>
    3. <font style="color:rgb(31, 35, 40);">在</font><font style="color:rgb(31, 35, 40);">执行</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">good_ping</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">时，事件循环从队列中选择下一个任务并对其进行处理（例如接受新请求、调用数据库）</font>
        * <font style="color:rgb(31, 35, 40);">独立于主线程（即我们的 FastAPI 应用程序），工作线程将等待</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">time.sleep</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">完成。</font>
        * <font style="color:rgb(31, 35, 40);">同步操作仅阻塞侧线程，而不阻塞主线程。</font>
    4. <font style="color:rgb(31, 35, 40);">当</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">good_ping</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">完成工作后，服务器向客户端返回响应</font>
3. `<font style="color:rgb(31, 35, 40);">GET /perfect-ping</font>`
    1. <font style="color:rgb(31, 35, 40);">FastAPI 服务器接收请求并开始处理</font>
    2. <font style="color:rgb(31, 35, 40);">FastAPI 等待</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">asyncio.sleep(10)</font>`
    3. <font style="color:rgb(31, 35, 40);">事件循环从队列中选择下一个任务并对其进行处理（例如接受新请求、调用数据库）</font>
    4. <font style="color:rgb(31, 35, 40);">当</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">asyncio.sleep(10)</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">完成后，服务器完成路由的执行并向客户端返回响应</font>

警告

<font style="color:rgb(31, 35, 40);">关于线程池的注意事项：</font>

+ <font style="color:rgb(31, 35, 40);">线程比协程需要更多的资源，因此它们不像异步 I/O 操作那样便宜。</font>
+ <font style="color:rgb(31, 35, 40);">线程池的线程数量有限，也就是说，你的线程可能会耗尽，导致应用运行缓慢。</font>[阅读更多](https://github.com/Kludex/fastapi-tips?tab=readme-ov-file#2-be-careful-with-non-async-functions)<font style="color:rgb(31, 35, 40);">（外部链接）</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">CPU 密集型任务</font>
<font style="color:rgb(31, 35, 40);">第二个警告是，非阻塞等待操作或发送到线程池的操作必须是 I/O 密集型任务（例如打开文件、数据库调用、外部 API 调用）。</font>

+ <font style="color:rgb(31, 35, 40);">等待 CPU 密集型任务（例如繁重计算、数据处理、视频转码）是毫无价值的，因为 CPU 必须工作才能完成任务，而 I/O 操作是外部的，服务器在等待该操作完成时不执行任何操作，因此它可以转到下一个任务。</font>
+ <font style="color:rgb(31, 35, 40);">由于</font><font style="color:rgb(31, 35, 40);"> </font>[GIL](https://realpython.com/python-gil/)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">的存在，在其他线程中运行 CPU 密集型任务也是无效的。简而言之，GIL 一次只允许一个线程工作，这使得它对于 CPU 任务毫无用处。</font>
+ <font style="color:rgb(31, 35, 40);">如果您想优化 CPU 密集型任务，您应该将它们发送给另一个进程中的工作人员。</font>

**<font style="color:rgb(31, 35, 40);">困惑用户的相关 StackOverflow 问题</font>**

1. [https://stackoverflow.com/questions/62976648/architecture-flask-vs-fastapi/70309597#70309597](https://stackoverflow.com/questions/62976648/architecture-flask-vs-fastapi/70309597#70309597)
    - <font style="color:rgb(31, 35, 40);">您还可以在这里查看</font>[我的答案](https://stackoverflow.com/a/70309597/6927498)
2. [https://stackoverflow.com/questions/65342833/fastapi-uploadfile-is-slow-compared-to-flask](https://stackoverflow.com/questions/65342833/fastapi-uploadfile-is-slow-compared-to-flask)
3. [https://stackoverflow.com/questions/71516140/fastapi-runs-api-calls-in-serial-instead-of-parallel-fashion](https://stackoverflow.com/questions/71516140/fastapi-runs-api-calls-in-serial-instead-of-parallel-fashion)

## **依赖项**<font style="color:rgb(31, 35, 40);">  </font>
<font style="color:rgb(31, 35, 40);">—— FastAPI 的一个核心机制，可用于注入共享资源或逻辑</font>

### **超越传统的依赖注入用途**
<font style="color:rgb(31, 35, 40);">—— 不仅用于向路由函数传递服务对象，还可用于校验逻辑、访问数据库等。 </font>

<font style="color:rgb(31, 35, 40);">Pydantic 具有丰富的功能来验证和转换数据。</font>

<font style="color:rgb(31, 35, 40);">除了具有默认值的必填和非必填字段等常规功能外，Pydantic 还内置了全面的数据处理工具，如正则表达式、枚举、字符串操作、电子邮件验证等。</font>

```python
from enum import Enum
from pydantic import AnyUrl, BaseModel, EmailStr, Field


class MusicBand(str, Enum):
    AEROSMITH = "AEROSMITH"
    QUEEN = "QUEEN"
    ACDC = "AC/DC"


class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=128)
    username: str = Field(min_length=1, max_length=128, pattern="^[A-Za-z0-9-_]+$")
    email: EmailStr
    age: int = Field(ge=18, default=None)  # must be greater or equal to 18
    favorite_band: MusicBand | None = None  # only "AEROSMITH", "QUEEN", "AC/DC" values are allowed to be inputted
    website: AnyUrl | None = None
```

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">自定义基础模型</font>
<font style="color:rgb(31, 35, 40);">拥有一个可控的全局基础模型，使我们能够自定义应用内的所有模型。例如，我们可以强制使用标准的日期时间格式，或者为基础模型的所有子类引入一个通用方法。</font>

```python
from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, ConfigDict


def datetime_to_gmt_str(dt: datetime) -> str:
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))

    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")


class CustomModel(BaseModel):
    model_config = ConfigDict(
        json_encoders={datetime: datetime_to_gmt_str},
        populate_by_name=True,
    )

    def serializable_dict(self, **kwargs):
        """Return a dict which contains only serializable fields."""
        default_dict = self.model_dump()

        return jsonable_encoder(default_dict)
```

<font style="color:rgb(31, 35, 40);">在上面的例子中，我们决定创建一个全局基础模型：</font>

+ <font style="color:rgb(31, 35, 40);">将所有日期时间字段序列化为具有明确时区的标准格式</font>
+ <font style="color:rgb(31, 35, 40);">提供一种方法来返回仅具有可序列化字段的字典</font>

### <font style="color:rgb(31, 35, 40);">解耦 Pydantic BaseSettings</font>
<font style="color:rgb(31, 35, 40);">BaseSettings 是读取环境变量的一项重大创新，但整个应用使用单一的 BaseSettings 会随着时间的推移变得混乱。为了提高可维护性和组织性，我们将 BaseSettings 拆分到不同的模块和域中。</font>

```python
# src.auth.config
from datetime import timedelta

from pydantic_settings import BaseSettings


class AuthConfig(BaseSettings):
    JWT_ALG: str
    JWT_SECRET: str
    JWT_EXP: int = 5  # minutes

    REFRESH_TOKEN_KEY: str
    REFRESH_TOKEN_EXP: timedelta = timedelta(days=30)

    SECURE_COOKIES: bool = True


auth_settings = AuthConfig()


# src.config
from pydantic import PostgresDsn, RedisDsn, model_validator
from pydantic_settings import BaseSettings

from src.constants import Environment


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn
    REDIS_URL: RedisDsn

    SITE_DOMAIN: str = "myapp.com"

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None = None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None = None
    CORS_HEADERS: list[str]

    APP_VERSION: str = "1.0"


settings = Config()
```

## <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">依赖项</font>
### <font style="color:rgb(31, 35, 40);">超越依赖注入</font>
<font style="color:rgb(31, 35, 40);">Pydantic 是一个很棒的模式验证器，但对于涉及调用数据库或外部服务的复杂验证来说，它是不够的。</font>

<font style="color:rgb(31, 35, 40);">FastAPI 文档主要将依赖项作为端点的 DI 呈现，但它们也非常适合请求验证。</font>

<font style="color:rgb(31, 35, 40);">依赖关系可用于根据数据库约束验证数据（例如，检查电子邮件是否已经存在，确保找到用户等）。</font>

```python
# dependencies.py
async def valid_post_id(post_id: UUID4) -> dict[str, Any]:
    post = await service.get_by_id(post_id)
    if not post:
        raise PostNotFound()

    return post


# router.py
@router.get("/posts/{post_id}", response_model=PostResponse)
async def get_post_by_id(post: dict[str, Any] = Depends(valid_post_id)):
    return post


@router.put("/posts/{post_id}", response_model=PostResponse)
async def update_post(
    update_data: PostUpdate,  
    post: dict[str, Any] = Depends(valid_post_id), 
):
    updated_post = await service.update(id=post["id"], data=update_data)
    return updated_post


@router.get("/posts/{post_id}/reviews", response_model=list[ReviewsResponse])
async def get_post_reviews(post: dict[str, Any] = Depends(valid_post_id)):
    post_reviews = await reviews_service.get_by_post_id(post["id"])
    return post_reviews
```

<font style="color:rgb(31, 35, 40);">如果我们没有将数据验证置于依赖关系中，我们将必须验证每个端点的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">是否存在，并为每个端点编写相同的测试。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">链式依赖</font>
<font style="color:rgb(31, 35, 40);">依赖项可以使用其他依赖项并避免类似逻辑的代码重复。</font>

```python
# dependencies.py
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

async def valid_post_id(post_id: UUID4) -> dict[str, Any]:
    post = await service.get_by_id(post_id)
    if not post:
        raise PostNotFound()

    return post


async def parse_jwt_data(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/token"))
) -> dict[str, Any]:
    try:
        payload = jwt.decode(token, "JWT_SECRET", algorithms=["HS256"])
    except JWTError:
        raise InvalidCredentials()

    return {"user_id": payload["id"]}


async def valid_owned_post(
    post: dict[str, Any] = Depends(valid_post_id), 
    token_data: dict[str, Any] = Depends(parse_jwt_data),
) -> dict[str, Any]:
    if post["creator_id"] != token_data["user_id"]:
        raise UserNotOwner()

    return post

# router.py
@router.get("/users/{user_id}/posts/{post_id}", response_model=PostResponse)
async def get_user_post(post: dict[str, Any] = Depends(valid_owned_post)):
    return post
```

### <font style="color:rgb(31, 35, 40);">解耦并重用依赖项。依赖项调用会被缓存</font>
<font style="color:rgb(31, 35, 40);">依赖项可以重复使用多次，并且不会被重新计算 - FastAPI 默认在请求范围内缓存依赖项的结果，即如果</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">valid_post_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">在一条路由中被多次调用，则它只会被调用一次。</font>

<font style="color:rgb(31, 35, 40);">了解了这一点，我们可以将依赖项解耦到多个较小的函数中，这些函数在较小的域上运行，并且更易于在其他路由中重用。例如，在下面的代码中，我们使用了三次</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">parse_jwt_data</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">：</font>

1. `<font style="color:rgb(31, 35, 40);">valid_owned_post</font>`
2. `<font style="color:rgb(31, 35, 40);">valid_active_creator</font>`
3. `<font style="color:rgb(31, 35, 40);">get_user_post</font>`

<font style="color:rgb(31, 35, 40);">但</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">parse_jwt_data</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">只被调用一次，即在第一次调用中。</font>

```python
# dependencies.py
from fastapi import BackgroundTasks
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

async def valid_post_id(post_id: UUID4) -> Mapping:
    post = await service.get_by_id(post_id)
    if not post:
        raise PostNotFound()

    return post


async def parse_jwt_data(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="/auth/token"))
) -> dict:
    try:
        payload = jwt.decode(token, "JWT_SECRET", algorithms=["HS256"])
    except JWTError:
        raise InvalidCredentials()

    return {"user_id": payload["id"]}


async def valid_owned_post(
    post: Mapping = Depends(valid_post_id), 
    token_data: dict = Depends(parse_jwt_data),
) -> Mapping:
    if post["creator_id"] != token_data["user_id"]:
        raise UserNotOwner()

    return post


async def valid_active_creator(
    token_data: dict = Depends(parse_jwt_data),
):
    user = await users_service.get_by_id(token_data["user_id"])
    if not user["is_active"]:
        raise UserIsBanned()

    if not user["is_creator"]:
        raise UserNotCreator()

    return user


# router.py
@router.get("/users/{user_id}/posts/{post_id}", response_model=PostResponse)
async def get_user_post(
    worker: BackgroundTasks,
    post: Mapping = Depends(valid_owned_post),
    user: Mapping = Depends(valid_active_creator),
):
    """Get post that belong the active user."""
    worker.add_task(notifications_service.send_email, user["id"])
    return post
```

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">首选</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">async</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">依赖项</font>
<font style="color:rgb(31, 35, 40);">FastAPI 同时支持</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">sync</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">和</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">async</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">依赖项，当您不必等待任何事情时，可能会倾向于使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">sync</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">依赖项，但这可能不是最佳选择。</font>

<font style="color:rgb(31, 35, 40);">与路由一样，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">sync</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">依赖项在线程池中运行。这里的线程也有其代价和限制，如果你只是进行一些小型的非 I/O 操作，这些代价和限制是多余的。</font>

[查看更多](https://github.com/Kludex/fastapi-tips?tab=readme-ov-file#9-your-dependencies-may-be-running-on-threads)<font style="color:rgb(31, 35, 40);">（外部链接）</font>

## <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">各种各样的</font>
### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">遵循 REST</font>
<font style="color:rgb(31, 35, 40);">开发 RESTful API 可以更轻松地重用路由中的依赖项，如下所示：</font>

1. `<font style="color:rgb(31, 35, 40);">GET /courses/:course_id</font>`
2. `<font style="color:rgb(31, 35, 40);">GET /courses/:course_id/chapters/:chapter_id/lessons</font>`
3. `<font style="color:rgb(31, 35, 40);">GET /chapters/:chapter_id</font>`

<font style="color:rgb(31, 35, 40);">唯一需要注意的是必须在路径中使用相同的变量名：</font>

+ <font style="color:rgb(31, 35, 40);">如果您有两个端点</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">GET /profiles/:profile_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">和</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">GET /creators/:creator_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">两者都验证给定的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">profile_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">是否存在，但</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">GET /creators/:creator_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">还检查配置文件是否是创建者，那么最好将</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">creator_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">路径变量重命名为</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">profile_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">并链接这两个依赖关系。</font>

```python
# src.profiles.dependencies
async def valid_profile_id(profile_id: UUID4) -> Mapping:
    profile = await service.get_by_id(profile_id)
    if not profile:
        raise ProfileNotFound()

    return profile

# src.creators.dependencies
async def valid_creator_id(profile: Mapping = Depends(valid_profile_id)) -> Mapping:
    if not profile["is_creator"]:
        raise ProfileNotCreator()

    return profile

# src.profiles.router.py
@router.get("/profiles/{profile_id}", response_model=ProfileResponse)
async def get_user_profile_by_id(profile: Mapping = Depends(valid_profile_id)):
    """Get profile by id."""
    return profile

# src.creators.router.py
@router.get("/creators/{profile_id}", response_model=ProfileResponse)
async def get_user_profile_by_id(
    creator_profile: Mapping = Depends(valid_creator_id)
):
    """Get creator's profile by id."""
    return creator_profile
```

### <font style="color:rgb(31, 35, 40);">FastAPI 响应序列化</font>
<font style="color:rgb(31, 35, 40);">您可能认为您可以返回与您的路线的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">response_model</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">匹配的 Pydantic 对象来进行一些优化，但您错了。</font>

<font style="color:rgb(31, 35, 40);">FastAPI 首先使用其</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">jsonable_encoder</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">将 pydantic 对象转换为 dict，然后使用您的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">response_model</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">验证数据，然后才将您的对象序列化为 JSON。</font>

<font style="color:rgb(31, 35, 40);">这意味着您的 Pydantic 模型对象被创建了两次：</font>

+ <font style="color:rgb(31, 35, 40);">首先，当您明确创建它以从您的路线返回时。</font>
+ <font style="color:rgb(31, 35, 40);">其次，FastAPI 隐式地根据 response_model 验证响应数据。</font>

```python
from fastapi import FastAPI
from pydantic import BaseModel, root_validator

app = FastAPI()


class ProfileResponse(BaseModel):
    @model_validator(mode="after")
    def debug_usage(self):
        print("created pydantic model")

        return self


@app.get("/", response_model=ProfileResponse)
async def root():
    return ProfileResponse()
```

**<font style="color:rgb(31, 35, 40);"></font>****<font style="color:rgb(31, 35, 40);">日志输出：</font>**

```python
[INFO] [2022-08-28 12:00:00.000000] created pydantic model
[INFO] [2022-08-28 12:00:00.000020] created pydantic model
```

### <font style="color:rgb(31, 35, 40);">如果必须使用同步 SDK，则在线程池中运行它。</font>
<font style="color:rgb(31, 35, 40);">如果您必须使用库与外部服务交互，并且它不是</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">async</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，那么请在外部工作线程中进行 HTTP 调用。</font>

<font style="color:rgb(31, 35, 40);">我们可以使用 starlette 中著名的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">run_in_threadpool</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">。</font>

```python
from fastapi import FastAPI
from fastapi.concurrency import run_in_threadpool
from my_sync_library import SyncAPIClient 

app = FastAPI()


@app.get("/")
async def call_my_sync_library():
    my_data = await service.get_my_data()

    client = SyncAPIClient()
    await run_in_threadpool(client.make_request, data=my_data)
```

### <font style="color:rgb(31, 35, 40);">ValueErrors 可能会变成 Pydantic ValidationError</font>
<font style="color:rgb(31, 35, 40);">如果您在客户端直接面对的 Pydantic 模式中引发</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">ValueError</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，它将向用户返回详细的响应。</font>

```python
# src.profiles.schemas
from pydantic import BaseModel, field_validator

class ProfileCreate(BaseModel):
    username: str

    @field_validator("password", mode="after")
    @classmethod
    def valid_password(cls, password: str) -> str:
        if not re.match(STRONG_PASSWORD_PATTERN, password):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password


# src.profiles.routes
from fastapi import APIRouter

router = APIRouter()


@router.post("/profiles")
async def get_creator_posts(profile_data: ProfileCreate):
    pass
```

**<font style="color:rgb(31, 35, 40);"></font>****<font style="color:rgb(31, 35, 40);">响应示例：</font>**



### <font style="color:rgb(31, 35, 40);">文档</font>
1. <font style="color:rgb(31, 35, 40);">除非你的 API 是公开的，否则默认隐藏文档。仅在选定的环境中明确显示。</font>

```python
from fastapi import FastAPI
from starlette.config import Config

config = Config(".env")  # parse .env file for env variables

ENVIRONMENT = config("ENVIRONMENT")  # get current env name
SHOW_DOCS_ENVIRONMENT = ("local", "staging")  # explicit list of allowed envs

app_configs = {"title": "My Cool API"}
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs["openapi_url"] = None  # set url for docs as null

app = FastAPI(**app_configs)
```

1. <font style="color:rgb(31, 35, 40);">帮助 FastAPI 生成易于理解的文档</font>
    1. <font style="color:rgb(31, 35, 40);">Set</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">response_model</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">status_code</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">description</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">, etc.</font>
    2. <font style="color:rgb(31, 35, 40);">如果模型和状态不同，请使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">responses</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">路由属性为不同的响应添加文档</font>

```python
from fastapi import APIRouter, status

router = APIRouter()

@router.post(
    "/endpoints",
    response_model=DefaultResponseModel,  # default response pydantic model 
    status_code=status.HTTP_201_CREATED,  # default status code
    description="Description of the well documented endpoint",
    tags=["Endpoint Category"],
    summary="Summary of the Endpoint",
    responses={
        status.HTTP_200_OK: {
            "model": OkResponse, # custom pydantic model for 200 response
            "description": "Ok Response",
        },
        status.HTTP_201_CREATED: {
            "model": CreatedResponse,  # custom pydantic model for 201 response
            "description": "Creates something from user request ",
        },
        status.HTTP_202_ACCEPTED: {
            "model": AcceptedResponse,  # custom pydantic model for 202 response
            "description": "Accepts request and handles it later",
        },
    },
)
async def documented_route():
    pass
```

<font style="color:rgb(31, 35, 40);">将生成如下文档：</font>

### <font style="color:rgb(31, 35, 40);">设置数据库键命名约定</font>
<font style="color:rgb(31, 35, 40);">根据数据库的约定明确设置索引的命名比 sqlalchemy 的命名更可取。</font>

```python
from sqlalchemy import MetaData

POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}
metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
```

### <font style="color:rgb(31, 35, 40);">迁移。Alembic</font>
1. <font style="color:rgb(31, 35, 40);">迁移必须是静态且可恢复的。如果您的迁移依赖于动态生成的数据，请确保唯一动态的是数据本身，而不是其结构。</font>
2. <font style="color:rgb(31, 35, 40);">生成具有描述性名称和 slug 的迁移文件。slug 是必需的，并且应该能够解释迁移过程中发生的变更。</font>
3. <font style="color:rgb(31, 35, 40);">为新的迁移设置易于阅读的文件模板。我们使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">*date*_*slug*.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">格式，例如</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">2022-08-24_post_content_idx.py</font>`

```python
# alembic.ini
file_template = %%(year)d-%%(month).2d-%%(day).2d_%%(slug)s
```

### <font style="color:rgb(31, 35, 40);">设置数据库命名约定</font>
<font style="color:rgb(31, 35, 40);">名称保持一致很重要。我们遵循以下规则：</font>

1. <font style="color:rgb(31, 35, 40);">  </font><font style="color:rgb(31, 35, 40);">小写蛇形</font>
2. <font style="color:rgb(31, 35, 40);">单数形式（例如</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post_like</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">user_playlist</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">）</font>
3. <font style="color:rgb(31, 35, 40);">将相似的表用模块前缀分组，例如</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">payment_account</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">payment_bill</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post_like</font>`
4. <font style="color:rgb(31, 35, 40);">跨表保持一致，但具体命名也可以，例如</font>
    1. <font style="color:rgb(31, 35, 40);">在所有表中使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">profile_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，但如果其中一些只需要创建者的个人资料，则使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">creator_id</font>`
    2. <font style="color:rgb(31, 35, 40);">所有抽象表都使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，例如</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post_like</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">post_view</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，但在相关模块中使用具体命名，例如</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">chapters.course_id</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">中的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">course_id</font>`
5. `<font style="color:rgb(31, 35, 40);">_at</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">后缀表示日期时间</font>
6. `<font style="color:rgb(31, 35, 40);">_date</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">日期后缀</font>

### <font style="color:rgb(31, 35, 40);">SQL 优先，Pydantic 其次</font>
+ <font style="color:rgb(31, 35, 40);">通常，数据库处理数据比 CPython 更快、更干净。</font>
+ <font style="color:rgb(31, 35, 40);">最好使用 SQL 完成所有复杂的连接和简单的数据操作。</font>
+ <font style="color:rgb(31, 35, 40);">最好在数据库中聚合 JSON 以获得具有嵌套对象的响应。</font>

```python
# src.posts.service
from typing import Any

from pydantic import UUID4
from sqlalchemy import desc, func, select, text
from sqlalchemy.sql.functions import coalesce

from src.database import database, posts, profiles, post_review, products

async def get_posts(
    creator_id: UUID4, *, limit: int = 10, offset: int = 0
) -> list[dict[str, Any]]: 
    select_query = (
        select(
            (
                posts.c.id,
                posts.c.slug,
                posts.c.title,
                func.json_build_object(
                    text("'id', profiles.id"),
                    text("'first_name', profiles.first_name"),
                    text("'last_name', profiles.last_name"),
                    text("'username', profiles.username"),
                ).label("creator"),
            )
        )
        .select_from(posts.join(profiles, posts.c.owner_id == profiles.c.id))
        .where(posts.c.owner_id == creator_id)
        .limit(limit)
        .offset(offset)
        .group_by(
            posts.c.id,
            posts.c.type,
            posts.c.slug,
            posts.c.title,
            profiles.c.id,
            profiles.c.first_name,
            profiles.c.last_name,
            profiles.c.username,
            profiles.c.avatar,
        )
        .order_by(
            desc(coalesce(posts.c.updated_at, posts.c.published_at, posts.c.created_at))
        )
    )

    return await database.fetch_all(select_query)

# src.posts.schemas
from typing import Any

from pydantic import BaseModel, UUID4


class Creator(BaseModel):
    id: UUID4
    first_name: str
    last_name: str
    username: str


class Post(BaseModel):
    id: UUID4
    slug: str
    title: str
    creator: Creator


# src.posts.router
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/creators/{creator_id}/posts", response_model=list[Post])
async def get_creator_posts(creator: dict[str, Any] = Depends(valid_creator_id)):
    posts = await service.get_posts(creator["id"])

    return posts
```

### <font style="color:rgb(31, 35, 40);">从第 0 天开始设置测试客户端异步</font>
<font style="color:rgb(31, 35, 40);">使用 DB 编写集成测试很可能会导致将来出现混乱的事件循环错误。请立即设置异步测试客户端，例如</font><font style="color:rgb(31, 35, 40);"> </font>[httpx](https://github.com/encode/starlette/issues/652)

```python
import pytest
from async_asgi_testclient import TestClient

from src.main import app  # inited FastAPI app


@pytest.fixture
async def client() -> AsyncGenerator[TestClient, None]:
    host, port = "127.0.0.1", "9000"

    async with AsyncClient(transport=ASGITransport(app=app, client=(host, port)), base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_create_post(client: TestClient):
    resp = await client.post("/posts")

    assert resp.status_code == 201
```

<font style="color:rgb(31, 35, 40);">除非您有同步数据库连接（对不起？）或者不打算编写集成测试。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">使用皱褶</font>
<font style="color:rgb(31, 35, 40);">有了 linters，您可以忘记格式化代码并专注于编写业务逻辑。</font>

[Ruff](https://github.com/astral-sh/ruff)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">是一款“速度极快”的新型 linter，它取代了 black、autoflake、isort，并支持 600 多条 lint 规则。</font>

<font style="color:rgb(31, 35, 40);">使用预提交钩子是一种流行的良好做法，但对于我们来说，仅使用脚本就可以了。</font>

```python
#!/bin/sh -e
set -x

ruff check --fix src
ruff format src
```

## <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">奖金部分</font>
<font style="color:rgb(31, 35, 40);">一些非常友善的人分享了他们自己的经验和最佳实践，绝对值得一读。请在项目的</font>[议题](https://github.com/zhanymkanov/fastapi-best-practices/issues)<font style="color:rgb(31, 35, 40);">部分查看。</font>

<font style="color:rgb(31, 35, 40);">例如，</font><font style="color:rgb(31, 35, 40);"> </font>[lowercase00](https://github.com/zhanymkanov/fastapi-best-practices/issues/4)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">详细描述了他们在权限和授权、基于类的服务和视图方面的最佳实践， 任务队列、自定义响应序列化器、使用 dynaconf 的配置等。</font>

<font style="color:rgb(31, 35, 40);">如果您有任何使用 FastAPI 的经验想分享，无论好坏，都欢迎您创建新的 issue。我们很高兴阅读您的分享。</font>

