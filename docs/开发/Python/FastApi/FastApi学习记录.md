## <font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">概述</font>
`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">fastapi</font>`<font style="color:rgb(51, 51, 51);">，一个用于构建 API 的现代、快速（高性能）的web框架。</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">fastapi</font>`<font style="color:rgb(51, 51, 51);">是建立在Starlette和Pydantic基础上的，Pydantic是一个基于Python类型提示来定义数据验证、序列化和文档的库。Starlette是一种轻量级的ASGI框架/工具包，是构建高性能Asyncio服务的理性选择。</font>

+ <font style="color:rgb(119, 119, 119);">快速：可与 NodeJS 和 Go 比肩的</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">极高性能</font>`<font style="color:rgb(119, 119, 119);">（归功于 </font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">Starlette</font>`<font style="color:rgb(119, 119, 119);"> 和 </font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">Pydantic</font>`<font style="color:rgb(119, 119, 119);">），是最快的 Python web 框架之一。</font>
+ <font style="color:rgb(119, 119, 119);">高效编码：提高功能开发速度约 200％ 至 300％。</font>
+ <font style="color:rgb(119, 119, 119);">更少bug：减少约 40％ 的人为（开发者）导致错误。</font>
+ <font style="color:rgb(119, 119, 119);">智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。</font>
+ <font style="color:rgb(119, 119, 119);">简单：设计的</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">易于使用和学习</font>`<font style="color:rgb(119, 119, 119);">，阅读文档的时间更短。</font>
+ <font style="color:rgb(119, 119, 119);">简短：使代码重复最小化。通过不同的参数声明实现丰富功能。</font>
+ <font style="color:rgb(119, 119, 119);">健壮：生产可用级别的代码。还有</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">自动生成的交互式文档</font>`<font style="color:rgb(119, 119, 119);">。</font>

<font style="color:rgb(51, 51, 51);">依赖：Python 3.6 及更高版本，FastAPI 站在以下巨人的肩膀之上</font>

[<font style="color:rgb(119, 119, 119);">Starlette</font>](https://www.starlette.io/)<font style="color:rgb(119, 119, 119);"> 负责 web 部分(Asyncio)</font>

[<font style="color:rgb(119, 119, 119);">Pydantic</font>](https://pydantic-docs.helpmanual.io/)<font style="color:rgb(119, 119, 119);"> 负责数据部分(类型提示)</font>

<font style="color:rgb(51, 51, 51);">FastApi是站在前人肩膀上，集成了多种框架的优点的新秀框架。它出现的比较晚，2018年底才发布在github上。广泛应用于当前各种前后端分离的项目开发，测试运维自动化以及微服务的场景中。</font>

## <font style="color:rgb(51, 51, 51);">quick start</font>
### <font style="color:rgb(51, 51, 51);">简单案例</font>
**<font style="color:rgb(51, 51, 51);">安装</font>**

```python
pip install fastapi
```

<font style="color:rgb(51, 51, 51);">你还会需要一个 ASGI 服务器，生产环境可以使用 </font>[<font style="color:rgb(51, 51, 51);">Uvicorn</font>](https://www.uvicorn.org/)

```python
pip install uvicorn
```

**<font style="color:rgb(51, 51, 51);">代码</font>**

```python
from fastapi import FastAPI  # FastAPI 是一个为你的 API 提供了所有功能的 Python 类。

app = FastAPI()  # 这个实例将是创建你所有 API 的主要交互对象。这个 app 同样在如下命令中被 uvicorn 所引用

@app.get("/")
async def root():
    return {"message": "Hello yuan"}
```

<font style="color:rgb(51, 51, 51);">通过以下命令运行服务器：</font>

<font style="color:rgb(51, 51, 51);">uvicorn main:app --reload</font>

```python
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [73408]
INFO:     Started server process [73408]
INFO:     Waiting for application startup
INFO:     Application startup complete
```

<font style="color:rgb(51, 51, 51);">也可以直接运行：</font>

```python
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8080, debug=True, reload=True)
```

<font style="color:rgb(119, 119, 119);">（1）导入 FastAPI。（2）创建一个 app 实例。（3）编写一个路径操作装饰器（如 @app.get("/")）。（4）编写一个路径操作函数（如上面的 def root(): ...）（5）定义返回值（6）运行开发服务器（如 uvicorn main:app --reload）</font>

<font style="color:rgb(51, 51, 51);">此外，fastapi有着</font>**<font style="color:rgb(51, 51, 51);">非常棒的交互式 API 文档</font>**<font style="color:rgb(51, 51, 51);">，这一点很吸引人。</font>

<font style="color:rgb(51, 51, 51);">跳转到 </font>[<font style="color:rgb(51, 51, 51);">http://127.0.0.1:8080/docs</font>](http://127.0.0.1:8080/docs)<font style="color:rgb(51, 51, 51);">。你将会看到</font>**<font style="color:rgb(51, 51, 51);">自动生成</font>**<font style="color:rgb(51, 51, 51);">的交互式 API 文档。</font>

## <font style="color:rgb(51, 51, 51);">路径操作</font>
### <font style="color:rgb(51, 51, 51);">路径操作装饰器</font>
<font style="color:rgb(51, 51, 51);">fastapi支持各种请求方式：</font>

```python
@app.get()
@app.post()
@app.put()
@app.patch()
@app.delete()
@app.options()
@app.head()
@app.trace()
```

| FastAPI 装饰器 | HTTP 方法 | 操作类型 | 常见用途 | 是否幂等 |
| --- | --- | --- | --- | --- |
| `@app.get()` | GET | 读取资源 | 查询数据、获取列表或详情 | ✅ 是 |
| `@app.post()` | POST | 创建资源 | 新增数据、提交表单、上传文件 | ❌ 否 |
| `@app.put()` | PUT | 更新资源（整体） | 替换对象所有字段 | ✅ 是 |
| `@app.patch()` | PATCH | 更新资源（部分） | 局部修改对象字段 | ❌/✅ 视实现而定 |
| `@app.delete()` | DELETE | 删除资源 | 删除记录、注销账号等 | ✅ 是 |
| `@app.options()` | OPTIONS | 获取通信选项 | 查看允许的方法（CORS 请求预检） | ✅ 是 |
| `@app.head()` | HEAD | 类似 GET，但无响应体 | 用于检查资源是否存在 | ✅ 是 |
| `@app.trace()` | TRACE | 回显请求内容 | 调试用途（不常用） | ✅ 是 |


```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/get")
def get_test():
    return {"method": "get方法"}


@app.post("/post")
def post_test():
    return {"method": "post方法"}


@app.put("/put")
def put_test():
    return {"method": "put方法"}


@app.delete("/delete")
def delete_test():
    return {"method": "delete方法"}
```

![](../../../images/1721480552012-92ce2005-e3c1-43fe-9dfd-64ff2639e308.png)

<font style="color:rgb(51, 51, 51);">路径操作装饰器参数：</font>

```python
@app.post(
    "/items/{item_id}",
    response_model=Item,
    status_code=status.HTTP_200_OK,
    tags=["AAA"],
    summary="this is summary",
    description="this is description",
    response_description= "this is response_description",
    deprecated=False,
)
```

### <font style="color:rgb(51, 51, 51);">include_router</font>
<font style="color:rgb(51, 51, 51);">main.py</font>

```python
from typing import Union

from fastapi import FastAPI
import uvicorn

from apps import app01, app02

app = FastAPI()

app.include_router(app01, prefix="/app01", tags=["第一章节：商城接口", ])
app.include_router(app02, prefix="/app02", tags=["第二章节：用户中心接口", ])

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, debug=True, reload=True)
```

<font style="color:rgb(51, 51, 51);">与main.py同级目录apps：</font>![](../../../images/1721480539015-94eda5aa-d243-48b0-9d52-487e1859d160.png)

```python
# __init__.py
from .app01 import app01
from .app02 import app02
```

```python
from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/shop/food")
def shop_food():
    return {"shop": "food"}


@app01.get("/shop/bed")
def shop_food():
    return {"shop": "bed"}
```

```python
from fastapi import APIRouter

app02 = APIRouter()


@app02.post("/user/login")
def user_login():
    return {"user": "login"}


@app02.post("/user/reg")
def user_reg():
    return {"user": "reg"}
```

  
 ![](../../../images/1721480570631-48b71f7e-0f45-4d38-bfb9-b2b1cb2e8de0.png)

## <font style="color:rgb(51, 51, 51);">请求与响应</font>
### <font style="color:rgb(51, 51, 51);">4.1、路径参数</font>
#### <font style="color:rgb(51, 51, 51);">（1）基本用法</font>
<font style="color:rgb(51, 51, 51);">以使用与 Python 格式化字符串相同的语法来声明路径"参数"或"变量"：</font>

```python
@app.get("/user/{user_id}")
def get_user(user_id):
    print(user_id, type(user_id))
    return {"user_id": user_id}
```

<font style="color:rgb(51, 51, 51);">路径参数 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">user_id</font>`<font style="color:rgb(51, 51, 51);"> 的值将作为参数 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">user_id</font>`<font style="color:rgb(51, 51, 51);"> 传递给你的函数。</font>

#### <font style="color:rgb(51, 51, 51);">（2）有类型的路径参数</font>
<font style="color:rgb(51, 51, 51);">你可以使用标准的 Python 类型标注为函数中的路径参数声明类型。</font>

```python
@app.get("/user/{user_id}")
def get_user(user_id: int):
    print(user_id, type(user_id))
    return {"user_id": user_id}
```

<font style="color:rgb(51, 51, 51);">在这个例子中，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">user_id</font>`<font style="color:rgb(51, 51, 51);"> 被声明为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">int</font>`<font style="color:rgb(51, 51, 51);"> 类型。</font>

<font style="color:rgb(119, 119, 119);">这将为你的函数提供编辑器支持，包括错误检查、代码补全等等。</font>

#### <font style="color:rgb(51, 51, 51);">（3）注意顺序</font>
<font style="color:rgb(51, 51, 51);">在创建</font>_<font style="color:rgb(51, 51, 51);">路径操作</font>_<font style="color:rgb(51, 51, 51);">时，你会发现有些情况下路径是固定的。</font>

<font style="color:rgb(51, 51, 51);">比如 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/users/me</font>`<font style="color:rgb(51, 51, 51);">，我们假设它用来获取关于当前用户的数据.</font>

<font style="color:rgb(51, 51, 51);">然后，你还可以使用路径 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/user/{username}</font>`<font style="color:rgb(51, 51, 51);"> 来通过用户名 获取关于特定用户的数据。</font>

<font style="color:rgb(51, 51, 51);">由于</font>_<font style="color:rgb(51, 51, 51);">路径操作</font>_<font style="color:rgb(51, 51, 51);">是按顺序依次运行的，你需要确保路径 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/user/me</font>`<font style="color:rgb(51, 51, 51);"> 声明在路径 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/user/{username}</font>`<font style="color:rgb(51, 51, 51);">之前：</font>

```python
@app.get("/user/me")
async def read_user_me():
    return {"username": "the current user"}

@app.get("/user/{username}")
async def read_user(username: str):
    return {"username": username}
```

<font style="color:rgb(51, 51, 51);">否则，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/user/{username}</font>`<font style="color:rgb(51, 51, 51);"> 的路径还将与 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/user/me</font>`<font style="color:rgb(51, 51, 51);"> 相匹配，"认为"自己正在接收一个值为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">"me"</font>`<font style="color:rgb(51, 51, 51);"> 的 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">username</font>`<font style="color:rgb(51, 51, 51);"> 参数。</font>

### <font style="color:rgb(51, 51, 51);">4.2、查询参数（请求参数）</font>
<font style="color:rgb(51, 51, 51);">路径函数中声明不属于路径参数的其他函数参数时，它们将被自动解释为"查询字符串"参数，就是 url? 之后用</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">&</font>`<font style="color:rgb(51, 51, 51);">分割的 key-value 键值对。</font>

```python
@app.get("/jobs/{kd}")
async def search_jobs(kd: str, city: Union[str, None] = None, xl: Union[str, None] = None):  # 有默认值即可选，否则必选
    if city or xl:
        return {"kd": kd, "city": city, "xl": xl}
    return {"kd": kd}
```

  
 ![](../../../images/1721480586637-cb58f6aa-7016-4b10-9e3a-7ea56057004d.png)

<font style="color:rgb(51, 51, 51);">在这个例子中，函数参数 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">city</font>`<font style="color:rgb(51, 51, 51);">和</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">xl</font>`<font style="color:rgb(51, 51, 51);"> 是可选的，并且默认值为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">None</font>`<font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">自python3.5开始，PEP484为python引入了类型注解(type hints)，typing的主要作用有：</font>

1. <font style="color:rgb(119, 119, 119);">类型检查，防止运行时出现参数、返回值类型不符。</font>
2. <font style="color:rgb(119, 119, 119);">作为开发文档附加说明，方便使用者调用时传入和返回参数类型。</font>
3. <font style="color:rgb(119, 119, 119);">模块加入不会影响程序的运行不会报正式的错误，pycharm支持typing检查错误时会出现黄色警告。</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">type hints</font>`<font style="color:rgb(51, 51, 51);">主要是要指示函数的输入和输出的数据类型，数据类型在typing 包中，基本类型有str list dict等等，</font>

<font style="color:rgb(51, 51, 51);">Union 是当有多种可能的数据类型时使用，比如函数有可能根据不同情况有时返回str或返回list，那么就可以写成Union[list, str]Optional 是Union的一个简化， 当 数据类型中有可能是None时，比如有可能是str也有可能是None，则Optional[str], 相当于Union[str, None]</font>

### <font style="color:rgb(51, 51, 51);">4.3、请求体数据</font>
<font style="color:rgb(51, 51, 51);">当你需要将数据从客户端（例如浏览器）发送给 API 时，你将其作为「请求体」发送。</font>**<font style="color:rgb(51, 51, 51);">请求</font>**<font style="color:rgb(51, 51, 51);">体是客户端发送给 API 的数据。</font>**<font style="color:rgb(51, 51, 51);">响应</font>**<font style="color:rgb(51, 51, 51);">体是 API 发送给客户端的数据。</font>

<font style="color:rgb(51, 51, 51);">FastAPI 基于 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">Pydantic</font>`<font style="color:rgb(51, 51, 51);"> ，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">Pydantic</font>`<font style="color:rgb(51, 51, 51);"> 主要用来做类型强制检查（校验数据）。不符合类型要求就会抛出异常。</font>

<font style="color:rgb(51, 51, 51);">对于 API 服务，支持类型检查非常有用，会让服务更加健壮，也会加快开发速度，因为开发者再也不用自己写一行一行的做类型检查。</font>

<font style="color:rgb(51, 51, 51);">安装上手</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">pip install pydantic</font>`

```python
from typing import Union, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field, ValidationError, validator
import uvicorn
from datetime import date


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    name = 'root'
    age: int = Field(default=0, lt=100, gt=0)
    birth: Optional[date] = None
    friends: List[int] = []
    description: Union[str, None] = None

    # addr: Union[Addr, None] = None  # 类型嵌套

    @validator('name')
    def name_must_alpha(cls, v):
        assert v.isalpha(), 'name must be alpha'
        return v


class Data(BaseModel):  # 类型嵌套
    users: List[User]


app = FastAPI()


@app.post("/data/")
async def create_data(data: Data):
    # 添加数据库
    return data


if __name__ == '__main__':
    try:
        User(name="",...)
    except ValidationError as e:
        print(e.json())
```

<font style="color:rgb(51, 51, 51);">测试：</font>

```python
{
  "name": "rain",
  "age": 32,
  "birth": "2022-09-29",
  "friends": [],
  "description": "最帅的讲fastapi的老师"
}
```

<font style="color:rgb(51, 51, 51);">和声明查询参数时一样，当一个模型属性具有默认值时，它不是必需的。否则它是一个必需属性。将默认值设为 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">None</font>`<font style="color:rgb(51, 51, 51);"> 可使其成为可选属性。</font>

<font style="color:rgb(51, 51, 51);">FastAPI 会自动将定义的模型类转化为</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">JSON Schema</font>`<font style="color:rgb(51, 51, 51);">，Schema 成为 OpenAPI 生成模式的一部分，并显示在 API 交互文档中，查看 API 交互文档如下，该接口将接收</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">application/json</font>`<font style="color:rgb(51, 51, 51);">类型的参数。</font>

<font style="color:rgb(51, 51, 51);">FastAPI 支持同时定义 Path 参数、Query 参数和请求体参数，FastAPI 将会正确识别并获取数据。</font>

<font style="color:rgb(119, 119, 119);">参数在 url 中也声明了，它将被解释为 path 参数</font>

<font style="color:rgb(119, 119, 119);">参数是单一类型（例如int、float、str、bool等），它将被解释为 query 参数</font>

<font style="color:rgb(119, 119, 119);">参数类型为继承 Pydantic 模块的</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">BaseModel</font>`<font style="color:rgb(119, 119, 119);">类的数据模型类，则它将被解释为请求体参数</font>

### <font style="color:rgb(51, 51, 51);">4.4、form表单数据</font>
<font style="color:rgb(51, 51, 51);">在 OAuth2 规范的一种使用方式（密码流）中，需要将用户名、密码作为表单字段发送，而不是 JSON。</font>

<font style="color:rgb(51, 51, 51);">FastAPI 可以使用</font>**<font style="color:rgb(51, 51, 51);">Form</font>**<font style="color:rgb(51, 51, 51);">组件来接收表单数据，需要先使用</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">pip install python-multipart</font>`<font style="color:rgb(51, 51, 51);">命令进行安装。</font>

<font style="color:rgb(119, 119, 119);">pip install python-multipart</font>

```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/regin")
def regin(username: str = Form(..., max_length=16, min_length=8, regex='[a-zA-Z]'),
          password: str = Form(..., max_length=16, min_length=8, regex='[0-9]')):
    print(f"username:{username},password:{password}")
    return {"username": username}
```

<font style="color:rgb(51, 51, 51);">  
</font><font style="color:rgb(51, 51, 51);"> </font>![](../../../images/1721480613252-14282974-544b-454d-865d-88634b609122.png)

### <font style="color:rgb(51, 51, 51);">4.5、文件上传</font>
```python
from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()

# file: bytes = File()：适合小文件上传
@app.post("/files/")
async def create_file(file: bytes = File()):
    print("file:", file)
    return {"file_size": len(file)}


@app.post("/multiFiles/")
async def create_files(files: List[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


# file: UploadFile：适合大文件上传

@app.post("/uploadFile/")
async def create_upload_file(file: UploadFile):
    with open(f"{file.filename}", 'wb') as f:
        for chunk in iter(lambda: file.file.read(1024), b''):
            f.write(chunk)

    return {"filename": file.filename}


@app.post("/multiUploadFiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}
```

### <font style="color:rgb(51, 51, 51);">4.6、Reqeust对象</font>
<font style="color:rgb(51, 51, 51);">有些情况下我们希望能直接访问</font>_<font style="color:rgb(51, 51, 51);">Request</font>_<font style="color:rgb(51, 51, 51);">对象。例如我们在路径操作函数中想获取客户端的IP地址，需要在函数中声明</font>**<font style="color:rgb(51, 51, 51);">Request</font>**<font style="color:rgb(51, 51, 51);">类型的参数，FastAPI 就会自动传递 Request 对象给这个参数，我们就可以获取到 Request 对象及其属性信息，例如 header、url、cookie、session 等。</font>

```python
from fastapi import Request


@app.get("/items")
async def items(request: Request):
    return {
        "请求URL：": request.url,
        "请求ip：": request.client.host,
        "请求宿主：": request.headers.get("user-agent"),
        "cookies": request.cookies,
    }
```

### <font style="color:rgb(51, 51, 51);">4.7、请求静态文件</font>
<font style="color:rgb(51, 51, 51);">在 Web 开发中，需要请求很多静态资源文件（不是由服务器生成的文件），如 css/js 和图片文件等。</font>

```python
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"))
```

### <font style="color:rgb(51, 51, 51);">4.8、响应模型相关参数</font>
#### <font style="color:rgb(51, 51, 51);">（1）response_model</font>
<font style="color:rgb(51, 51, 51);">前面写的这么多路径函数最终 return 的都是自定义结构的字典，FastAPI 提供了 response_model 参数，声明 return 响应体的模型</font>

```python
# 路径操作
@app.post("/items/", response_model=Item)
# 路径函数
async def create_item(item: Item):
    ...
```

<font style="color:rgb(119, 119, 119);">response_model 是路径操作的参数，并不是路径函数的参数哦</font>

<font style="color:rgb(51, 51, 51);">FastAPI将使用</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">response_model</font>`<font style="color:rgb(51, 51, 51);">进行以下操作：</font>

+ <font style="color:rgb(51, 51, 51);">将输出数据转换为response_model中声明的数据类型。</font>
+ <font style="color:rgb(51, 51, 51);">验证数据结构和类型</font>
+ <font style="color:rgb(51, 51, 51);">将输出数据限制为该model定义的</font>
+ <font style="color:rgb(51, 51, 51);">添加到OpenAPI中</font>
+ <font style="color:rgb(51, 51, 51);">在自动文档系统中使用。</font>

<font style="color:rgb(51, 51, 51);">你可以在任意的路径操作中使用 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">response_model</font>`<font style="color:rgb(51, 51, 51);"> 参数来声明用于响应的模型</font>

<font style="color:rgb(51, 51, 51);">案例：</font>

+ <font style="color:rgb(51, 51, 51);">注册功能</font>
+ <font style="color:rgb(51, 51, 51);">输入账号、密码、昵称、邮箱，注册成功后返回个人信息</font>

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user
```

  
 ![](../../../images/1721480653624-0d6afe24-4dcc-41b3-8f3d-f20b34c9b713.png)

#### <font style="color:rgb(51, 51, 51);">（2）response_model_exclude_unset</font>
<font style="color:rgb(51, 51, 51);">通过上面的例子，我们学到了如何用response_model控制响应体结构，但是如果它们实际上没有存储，则可能要从结果中忽略它们。例如，如果model在NoSQL数据库中具有很多可选属性，但是不想发送很长的JSON响应，其中包含默认值。</font>

<font style="color:rgb(51, 51, 51);">案例：</font>

```python
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
```

<font style="color:rgb(51, 51, 51);">请求：</font>[<font style="color:rgb(51, 51, 51);">http://127.0.0.1:8080/items/foo</font>](http://127.0.0.1:8080/items/foo)

<font style="color:rgb(51, 51, 51);">不设置unset参数：</font>

```python
{
    "name": "Foo",
    "description": null,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
}
```

<font style="color:rgb(51, 51, 51);">设置unset参数：</font>

```python
{
    "name": "Foo",
    "price": 50.2
}
```

<font style="color:rgb(51, 51, 51);">使用路径操作装饰器的 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">response_model</font>`<font style="color:rgb(51, 51, 51);"> 参数来定义响应模型，特别是确保私有数据被过滤掉。使用 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">response_model_exclude_unset</font>`<font style="color:rgb(51, 51, 51);"> 来仅返回显式设定的值。</font><font style="color:rgb(51, 51, 51);">除了</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">response_model_exclude_unset</font>`<font style="color:rgb(51, 51, 51);">以外，还有</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">response_model_exclude_defaults</font>`<font style="color:rgb(51, 51, 51);">和</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">response_model_exclude_none</font>`<font style="color:rgb(51, 51, 51);">，我们可以很直观的了解到他们的意思，不返回是默认值的字段和不返回是None的字段。</font>

#### <font style="color:rgb(51, 51, 51);">（3）INCLUDE和EXCLUDE</font>
```python
# response_model_exclude
@app.get("/items/{item_id}", response_model=Item, response_model_exclude={"description"}, )
async def read_item(item_id: str):
    return items[item_id]

# response_model_include  
@app.get("/items/{item_id}", response_model=Item, response_model_include={"name", "price"}, )
async def read_item(item_id: str):
    return items[item_id]
```

## <font style="color:rgb(51, 51, 51);">jinja2模板</font>
<font style="color:rgb(51, 51, 51);">要了解jinja2，那么需要先理解模板的概念。模板在Python的web开发中⼴泛使⽤，它能够有效的将业务逻辑和页⾯逻辑分开，使代码可读性增强、并且更加容易理解和维护。</font><font style="color:rgb(51, 51, 51);">模板简单来说就是⼀个其中包涵占位变量表⽰动态的部分的⽂件，模板⽂件在经过动态赋值后，返回给⽤户。</font>

<font style="color:rgb(51, 51, 51);">jinja2是Flask作者开发的⼀个模板系统，起初是仿django模板的⼀个模板引擎，为Flask提供模板⽀持，由于其灵活，快速和安全等优点被⼴泛使⽤。</font>

<font style="color:rgb(51, 51, 51);">在jinja2中，存在三种语法：</font>

1. <font style="color:rgb(119, 119, 119);">变量取值 {{ }}</font>
2. <font style="color:rgb(119, 119, 119);">控制结构 {% %}</font>

### <font style="color:rgb(51, 51, 51);">5.1、jinja2 的变量</font>
`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">Main.py</font>`

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()  # 实例化 FastAPI对象
templates = Jinja2Templates(directory="templates")  # 实例化Jinja2对象，并将文件夹路径设置为以templates命令的文件夹


@app.get('/')
def hello(request: Request):
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,  # 注意，返回模板响应时，必须有request键值对，且值为Request请求对象
            'user': 'yuan',
            "books": ["金瓶梅", "聊斋", "剪灯新话", "国色天香"],
            "booksDict": {
                "金瓶梅": {"price": 100, "publish": "苹果出版社"},
                "聊斋": {"price": 200, "publish": "橘子出版社"},
            }
        }
    )
if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, debug=True, reload=True)
```

```python
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
<title>Title</title>
</head>
<body>


<h1>{{ user}}</h1>

<p>{{ books.0 }}</p>
<p>{{ books.1 }}</p>
<p>{{ books.2 }}</p>
<p>{{ books.3 }}</p>

<p>{{ booksDict.金瓶梅.price }}</p>


</body>
</html>
```

### <font style="color:rgb(51, 51, 51);">5.2、jinja2 的过滤器</font>
<font style="color:rgb(51, 51, 51);">变量可以通过“过滤器”进⾏修改，过滤器可以理解为是jinja2⾥⾯的内置函数和字符串处理函数。常⽤的过滤器有：</font>

| **<font style="color:rgb(51, 51, 51);">过滤器名称</font>** | **<font style="color:rgb(51, 51, 51);">说明</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">capitialize</font> | <font style="color:rgb(51, 51, 51);">把值的⾸字母转换成⼤写，其他⼦母转换为⼩写</font> |
| <font style="color:rgb(51, 51, 51);">lower</font> | <font style="color:rgb(51, 51, 51);">把值转换成⼩写形式</font> |
| <font style="color:rgb(51, 51, 51);">title</font> | <font style="color:rgb(51, 51, 51);">把值中每个单词的⾸字母都转换成⼤写</font> |
| <font style="color:rgb(51, 51, 51);">trim</font> | <font style="color:rgb(51, 51, 51);">把值的⾸尾空格去掉</font> |
| <font style="color:rgb(51, 51, 51);">striptags</font> | <font style="color:rgb(51, 51, 51);">渲染之前把值中所有的HTML标签都删掉</font> |
| <font style="color:rgb(51, 51, 51);">join</font> | <font style="color:rgb(51, 51, 51);">拼接多个值为字符串</font> |
| <font style="color:rgb(51, 51, 51);">round</font> | <font style="color:rgb(51, 51, 51);">默认对数字进⾏四舍五⼊，也可以⽤参数进⾏控制</font> |
| <font style="color:rgb(51, 51, 51);">safe</font> | <font style="color:rgb(51, 51, 51);">渲染时值不转义</font> |


<font style="color:rgb(51, 51, 51);">那么如何使⽤这些过滤器呢？只需要在变量后⾯使⽤管道(|)分割，多个过滤器可以链式调⽤，前⼀个过滤器的输出会作为后⼀个过滤</font><font style="color:rgb(51, 51, 51);">器的输⼊。</font>

```python
{{ 'abc'| captialize  }}  # Abc

{{ 'abc'| upper  }} # ABC

{{ 'hello world'| title  }} # Hello World

{{ "hello world"| replace('world','yuan') | upper }} # HELLO YUAN

{{ 18.18 | round | int }} # 18
```

### <font style="color:rgb(51, 51, 51);">5.3、jinja2 的控制结构</font>
#### <font style="color:rgb(51, 51, 51);">5.3.1、分支控制</font>
<font style="color:rgb(51, 51, 51);">jinja2中的if语句类似与Python的if语句，它也具有单分⽀，多分⽀等多种结构，不同的是，条件语句不需要使⽤冒号结尾，⽽结束控制语句，需要使⽤endif关键字</font>

```python
{% if age > 18 %}

<p>成年区</p>

{% else %}

<p>未成年区</p>

{% endif %}
```

#### <font style="color:rgb(51, 51, 51);">5.3.2、循环控制</font>
<font style="color:rgb(51, 51, 51);">jinja2中的for循环⽤于迭代Python的数据类型，包括列表，元组和字典。在jinja2中不存在while循环。</font>

```python
{% for book in books %}
<p>{{ book }}</p>
{% endfor %}
```

## <font style="color:rgb(51, 51, 51);">ORM操作</font>
<font style="color:rgb(51, 51, 51);">在大型的web开发中，我们肯定会用到数据库操作，那么FastAPI也支持数据库的开发，你可以用 PostgreSQL、MySQL、 SQLite Oracle 等。本文用SQLite为例。我们看下在fastapi是如何操作设计数据库的。</font>

<font style="color:rgb(51, 51, 51);">fastapi是一个很优秀的框架，但是缺少一个合适的orm，官方代码里面使用的是sqlalchemy，Tortoise ORM 是受 Django 启发的易于使用的异步 ORM （对象关系映射器）。</font>![](../../../images/1721480672618-57d98553-6b41-40c4-a1de-815998d4b291.png)

[<font style="color:rgb(51, 51, 51);">Tortoise ORM文档</font>](https://tortoise-orm.readthedocs.io/en/latest/index.html)

<font style="color:rgb(119, 119, 119);">Tortoise ORM 目前支持以下</font>[<font style="color:rgb(119, 119, 119);">数据库</font>](https://tortoise-orm.readthedocs.io/en/latest/databases.html#databases)<font style="color:rgb(119, 119, 119);">：</font>

+ <font style="color:rgb(119, 119, 119);">PostgreSQL >= 9.4（使用</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">asyncpg</font>`<font style="color:rgb(119, 119, 119);">）</font>
+ <font style="color:rgb(119, 119, 119);">SQLite（使用</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">aiosqlite</font>`<font style="color:rgb(119, 119, 119);">）</font>
+ <font style="color:rgb(119, 119, 119);">MySQL/MariaDB（使用</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">aiomysql</font>`<font style="color:rgb(119, 119, 119);">或使用</font>[<font style="color:rgb(119, 119, 119);">asyncmy</font>](https://github.com/long2ice/asyncmy)<font style="color:rgb(119, 119, 119);">）</font>

```python
安装
首先你必须像这样安装Tortoise ORM：
pip install tortoise-orm
你也可以使用你的db驱动程序来安装（aiosqlite是内置的）：
pip install tortoise-orm[asyncpg]
For MySQL:对于MySQL：
pip install tortoise-orm[asyncmy]
```

### <font style="color:rgb(51, 51, 51);">6.1、创建模型</font>
<font style="color:rgb(51, 51, 51);">以选课系统为例：</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">models.py</font>`

```python
from tortoise.models import Model
from tortoise import fields


class Clas(Model):
    name = fields.CharField(max_length=255, description='班级名称')


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='姓名')
    tno = fields.IntField(description='账号')
    pwd = fields.CharField(max_length=255, description='密码')


class Student(Model):
    id = fields.IntField(pk=True)
    sno = fields.IntField(description='学号')
    pwd = fields.CharField(max_length=255, description='密码')
    name = fields.CharField(max_length=255, description='姓名')
    # 一对多
    clas = fields.ForeignKeyField('models.Clas', related_name='students')
    # 多对多
    courses = fields.ManyToManyField('models.Course', related_name='students',description='学生选课表')


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='课程名')
    teacher = fields.ForeignKeyField('models.Teacher', related_name='courses', description='课程讲师')
```

### <font style="color:rgb(51, 51, 51);">6.2、aerich迁移工具</font>
`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">main.py</font>`

```python
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM


app = FastAPI()

# 该方法会在fastapi启动时触发，内部通过传递进去的app对象，监听服务启动和终止事件
# 当检测到启动事件时，会初始化Tortoise对象，如果generate_schemas为True则还会进行数据库迁移
# 当检测到终止事件时，会关闭连接
register_tortoise(
    app,
    config=TORTOISE_ORM,
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True,
                debug=True, workers=1)
```

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">settings.py</font>`

```python
TORTOISE_ORM = {
    'connections': {
        'default': {
            # 'engine': 'tortoise.backends.asyncpg',  PostgreSQL
            'engine': 'tortoise.backends.mysql',  # MySQL or Mariadb
            'credentials': {
                'host': '127.0.0.1',
                'port': '3306',
                'user': 'root',
                'password': 'yuan0316',
                'database': 'fastapi',
                'minsize': 1,
                'maxsize': 5,
                'charset': 'utf8mb4',
                "echo": True
            }
        },
    },
    'apps': {
        'models': {
            'models': ['models', "aerich.models"],
            'default_connection': 'default',

        }
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}
```

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">aerich</font>`<font style="color:rgb(51, 51, 51);">是一种</font>[<font style="color:rgb(51, 51, 51);">ORM</font>](https://so.csdn.net/so/search?q=ORM&spm=1001.2101.3001.7020)<font style="color:rgb(51, 51, 51);">迁移工具，需要结合</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">tortoise</font>`<font style="color:rgb(51, 51, 51);">异步orm框架使用。安装</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">aerich</font>`

```python
pip install aerich
```

#### <font style="color:rgb(51, 51, 51);">1. 初始化配置，只需要使用一次</font>
```python
aerich init -t settings.TORTOISE_ORM  # TORTOISE_ORM配置的位置)
```

<font style="color:rgb(119, 119, 119);">初始化完会在当前目录生成一个文件：pyproject.toml和一个文件夹：migrations</font>

+ `<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">pyproject.toml</font>`<font style="color:rgb(119, 119, 119);">：保存配置文件路径，低版本可能是</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">aerich.ini</font>`
+ `<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">migrations</font>`<font style="color:rgb(119, 119, 119);">：存放迁移文件</font>
+ ![](../../../images/1721480694981-4a90beb0-9650-4086-9e8f-3037a49f10e8.png)

#### <font style="color:rgb(51, 51, 51);">2. 初始化数据库，一般情况下只用一次</font>
```python
> aerich init-db
Success create app migrate location migrations\models
Success generate schema for app "models"
```

1. <font style="color:rgb(119, 119, 119);">此时数据库中就有相应的表格</font>
2. <font style="color:rgb(119, 119, 119);">如果</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">TORTOISE_ORM</font>`<font style="color:rgb(119, 119, 119);">配置文件中的</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">models</font>`<font style="color:rgb(119, 119, 119);">改了名，则执行这条命令时需要增加</font>`<font style="color:rgb(119, 119, 119);background-color:rgb(243, 244, 244);">--app</font>`<font style="color:rgb(119, 119, 119);">参数，来指定你修改的名字</font>

![](../../../images/1721480735145-9bfe9eaf-38e1-4090-94f7-f824ac70869a.png)

#### <font style="color:rgb(51, 51, 51);">3. 更新模型并进行迁移</font>
<font style="color:rgb(51, 51, 51);">修改model类，重新生成迁移文件,比如添加一个字段</font>

```python
class Admin(Model):
    ...
    xxx = fields.CharField(max_length=255)
```

```python
aerich migrate [--name] (标记修改操作) #  aerich migrate --name add_column
```

<font style="color:rgb(119, 119, 119);">迁移文件名的格式为 {version_num}</font>_<font style="color:rgb(119, 119, 119);">{datetime}</font>_<font style="color:rgb(119, 119, 119);">{name|update}.json。</font>![](../../../images/1721480751687-0e378d0c-b8ee-4818-b722-0d07a1c83816.png)<font style="color:rgb(51, 51, 51);">注意，此时sql并没有执行，数据库中admin表中没有xxx字段</font>![](../../../images/1721480762908-ef361211-a140-4a02-8cba-58b43a3fa421.png)

#### <font style="color:rgb(51, 51, 51);">4. 重新执行迁移，写入数据库</font>
```python
aerich upgrade
```

![](../../../images/1721480782388-2c2ff148-b2e1-4c66-8495-761908678a93.png)

#### <font style="color:rgb(51, 51, 51);">5. 回到上一个版本</font>
```python
aerich downgrade
 
```

#### <font style="color:rgb(51, 51, 51);">6. 查看历史迁移记录</font>
```python
aerich history
```

![](../../../images/1721480813944-f4f537bf-28e4-4588-9c67-e969a8e538c3.png)

### <font style="color:rgb(51, 51, 51);">6.3、api接口与restful规范</font>
#### <font style="color:rgb(51, 51, 51);">api接口</font>
<font style="color:rgb(51, 51, 51);">应用程序编程接口（Application Programming Interface，API接口），就是应用程序对外提供了一个操作数据的入口，这个入口可以是一个函数或类方法，也可以是一个url地址或者一个网络地址。当客户端调用这个入口，应用程序则会执行对应代码操作，给客户端完成相对应的功能。</font>

![](../../../images/1721480825093-1a52f0b5-29b6-450b-adb2-41ea56e2d64b.png)

<font style="color:rgb(51, 51, 51);">当然，api接口在工作中是比较常见的开发内容，有时候，我们会调用其他人编写的api接口，有时候，我们也需要提供api接口给其他人操作。由此就会带来一个问题，api接口往往都是一个函数、类方法、或者url或其他网络地址，不断是哪一种，当api接口编写过程中，我们都要考虑一个问题就是这个接口应该怎么编写？接口怎么写的更加容易维护和清晰，这就需要大家在调用或者编写api接口的时候要有一个明确的编写规范！！！</font>

#### <font style="color:rgb(51, 51, 51);">restful规范</font>
<font style="color:rgb(51, 51, 51);">为了在团队内部形成共识、防止个人习惯差异引起的混乱，我们都需要找到一种大家都觉得很好的接口实现规范，而且这种规范能够让后端写的接口，用途一目了然，减少客户端和服务端双方之间的合作成本。</font>

<font style="color:rgb(51, 51, 51);">目前市面上大部分公司开发人员使用的接口实现规范主要有：restful、RPC。</font>

<font style="color:rgb(51, 51, 51);">REST与技术无关，代表的是一种软件架构风格，REST是Representational State Transfer的简称，中文翻译为“表征状态转移”或“表现层状态转化”。</font>

<font style="color:rgb(51, 51, 51);">简单来说，REST的含义就是客户端与Web服务器之间进行交互的时候，使用HTTP协议中的4个请求方法代表不同的动作。</font>

<font style="color:rgb(119, 119, 119);">GET用来获取资源</font>

<font style="color:rgb(119, 119, 119);">POST用来新建资源 </font>

<font style="color:rgb(119, 119, 119);">PUT用来更新资源</font>

<font style="color:rgb(119, 119, 119);">DELETE用来删除资源。</font>

<font style="color:rgb(51, 51, 51);">只要API程序遵循了REST风格，那就可以称其为RESTful API。目前在前后端分离的架构中，前后端基本都是通过RESTful API来进行交互。</font>

<font style="color:rgb(51, 51, 51);">例如，我们现在要编写一个选课系统的接口，我们可以查询对一个学生进行查询、创建、更新和删除等操作，我们在编写程序的时候就要设计客户端浏览器与我们Web服务端交互的方式和路径。</font>

<font style="color:rgb(51, 51, 51);">而对于数据资源分别使用POST、DELETE、GET、UPDATE等请求动作来表达对数据的增删查改。</font>

| **<font style="color:rgb(51, 51, 51);">GET</font>** | **<font style="color:rgb(51, 51, 51);">/students</font>** | **<font style="color:rgb(51, 51, 51);">获取所有学生</font>** |
| :--- | :--- | :--- |
| <font style="color:rgb(51, 51, 51);">请求方法</font> | <font style="color:rgb(51, 51, 51);">请求地址</font> | <font style="color:rgb(51, 51, 51);">后端操作</font> |
| <font style="color:rgb(51, 51, 51);">GET</font> | <font style="color:rgb(51, 51, 51);">/students</font> | <font style="color:rgb(51, 51, 51);">获取所有学生</font> |
| <font style="color:rgb(51, 51, 51);">POST</font> | <font style="color:rgb(51, 51, 51);">/students</font> | <font style="color:rgb(51, 51, 51);">增加学生</font> |
| <font style="color:rgb(51, 51, 51);">GET</font> | <font style="color:rgb(51, 51, 51);">/students/1</font> | <font style="color:rgb(51, 51, 51);">获取编号为1的学生</font> |
| <font style="color:rgb(51, 51, 51);">PUT</font> | <font style="color:rgb(51, 51, 51);">/students/1</font> | <font style="color:rgb(51, 51, 51);">修改编号为1的学生</font> |
| <font style="color:rgb(51, 51, 51);">DELETE</font> | <font style="color:rgb(51, 51, 51);">/students/1</font> | <font style="color:rgb(51, 51, 51);">删除编号为1的学生</font> |


### <font style="color:rgb(51, 51, 51);">6.4、选课系统接口开发</font>
`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">api/student.py</font>`

```python
from fastapi import APIRouter
from models import *
from pydantic import BaseModel, validator
from typing import List, Union
from fastapi.templating import Jinja2Templates
from fastapi import Request

from fastapi.exceptions import HTTPException

student_api = APIRouter()


@student_api.get("/")
async def getAllStudent():
    # (1) 查询所有 all方法
    students = await Student.all()  # Queryset: [Student(),Student(),Student()]
    # print("students", students)
    #
    # for stu in students:
    #     print(stu.name, stu.sno)
    # print(students[0].name)
    # (2) 过滤查询 filter
    # students = await Student.filter(name="rain")  # Queryset: [Student(),Student(),Student()]
    # students = await Student.filter(clas_id=14)  # Queryset: [Student(),Student(),Student()]
    # print("students", students)

    # (3) 过滤查询 get方法：返回模型类型对象

    # stu = await Student.filter(id=6)  # [Student(),]
    # print(stu[0].name)
    # stu = await Student.get(id=6)  # Student()
    # print(stu.name)

    # (4) 模糊查询
    # stus = await Student.filter(sno__gt=2001)
    # stus = await Student.filter(sno__range=[1, 10000])
    # stus = await Student.filter(sno__in=[2001, 2002])
    # print(stus)  # [<Student: 7>, <Student: 8>]

    # (5) values查询
    # stus = await Student.filter(sno__range=[1, 10000])  # [Student(),Student(),Student(),...]
    # stus = await Student.all().values("name", "sno")  # [{},{},{},...]
    # print(stus)

    # (6) 一对多查询 多对多查询
    alvin = await Student.get(name="alvin")
    print(alvin.name)
    print(alvin.sno)
    print(await alvin.clas.values("name"))  # {'name': '计算机科学与技术2班'}
    students = await Student.all().values("name", "clas__name")
    print(await alvin.courses.all().values("name", "teacher__name"))
    students = await Student.all().values("name", "clas__name", "courses__name")

    return students


@student_api.get("/index.html")
async def getAllStudent(request: Request):
    templates = Jinja2Templates(directory="templates")
    students = await Student.all()  # [Student(),Student(),...]

    return templates.TemplateResponse(
        "index.html", {
            "request": request,
            "students": students
        }
    )


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    courses: List[int] = []

    @validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must be alpha'
        return value

    @validator("sno")
    def sno_validate(cls, value):
        assert 1000 < value < 10000, '学号要在2000-10000的范围内'
        return value


@student_api.post("/")
async def addStudent(student_in: StudentIn):
    # 插入到数据库
    # 方式1
    # student = Student(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno, clas_id=student_in.clas_id)
    # await student.save() # 插入到数据库student表
    # 方式2
    student = await Student.create(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno,
                                   clas_id=student_in.clas_id)

    # 多对多的关系绑定
    choose_courses = await Course.filter(id__in=student_in.courses)
    await student.courses.add(*choose_courses)

    return student


@student_api.get("/{student_id}")
async def getOneStudent(student_id: int):
    student = await Student.get(id=student_id)

    return student


@student_api.put("/{student_id}")
async def updateStudent(student_id: int, student_in: StudentIn):
    data = student_in.dict()
    print("data", data)
    courses = data.pop("courses")

    await Student.filter(id=student_id).update(**data)

    #  设置多对多的选修课
    edit_stu = await Student.get(id=student_id)
    choose_courses = await Course.filter(id__in=courses)
    await edit_stu.courses.clear()
    await edit_stu.courses.add(*choose_courses)

    return edit_stu


@student_api.delete("/{student_id}")
async def deleteStudent(student_id: int):
    deleteCount = await Student.filter(id=student_id).delete()
    if not deleteCount:
        raise HTTPException(status_code=404, detail=f"主键为{student_id}的学生不存在")

    return {}

```

## <font style="color:rgb(51, 51, 51);">中间件与CORS跨域</font>
### <font style="color:rgb(51, 51, 51);">中间件</font>
<font style="color:rgb(51, 51, 51);">你可以向 </font>**<font style="color:rgb(51, 51, 51);">FastAPI</font>**<font style="color:rgb(51, 51, 51);"> 应用添加中间件.</font>

<font style="color:rgb(51, 51, 51);">"中间件"是一个函数,它在每个</font>**<font style="color:rgb(51, 51, 51);">请求</font>**<font style="color:rgb(51, 51, 51);">被特定的路径操作处理之前,以及在每个</font>**<font style="color:rgb(51, 51, 51);">响应</font>**<font style="color:rgb(51, 51, 51);">之后工作.</font>

![](../../../images/1721480837774-70eb043b-b1a6-494e-acb8-9408f979e7a2.png)

> 如果你使用了 `yield` 关键字依赖, 依赖中的退出代码将在执行中间件_后_执行.
>
> 如果有任何后台任务(稍后记录), 它们将在执行中间件_后_运行.
>

要创建中间件你可以在函数的顶部使用装饰器 `@app.middleware("http")`.

中间件参数接收如下参数：

> + `request`.
> + 一个函数`call_next`，它将接收request，作为参数.
>     - 这个函数将 `request` 传递给相应的 _路径操作_.
>     - 然后它将返回由相应的_路径操作_生成的 `response`.
> + 然后你可以在返回 `response` 前进一步修改它.
>

```python
import uvicorn
from fastapi import FastAPI

from fastapi import Request
from fastapi.responses import Response
import time

app = FastAPI()


@app.middleware("http")
async def m2(request: Request, call_next):
    # 请求代码块
    print("m2 request")
    response = await call_next(request)
    # 响应代码块
    response.headers["author"] = "yuan"
    print("m2 response")
    return response


@app.middleware("http")
async def m1(request: Request, call_next):
    # 请求代码块
    print("m1 request")
    # if request.client.host in ["127.0.0.1", ]:  # 黑名单
    #     return Response(content="visit forbidden")

    # if request.url.path in ["/user"]:
    #     return Response(content="visit forbidden")

    start = time.time()

    response = await call_next(request)
    # 响应代码块
    print("m1 response")
    end = time.time()
    response.headers["ProcessTimer"] = str(end - start)
    return response


@app.get("/user")
def get_user():
    time.sleep(3)
    print("get_user函数执行")
    return {
        "user": "current user"
    }


@app.get("/item/{item_id}")
def get_item(item_id: int):
    time.sleep(2)
    print("get_item函数执行")
    return {
        "item_id": item_id
    }


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8030, reload=True,
                debug=True, workers=1)

```

### <font style="color:rgb(51, 51, 51);">CORS跨域</font>
```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.js"></script>
</head>
<body>

<p>click</p>

<script>
  
    $("p").click(function () {
        $.ajax({
            url: "http://127.0.0.1:8080/",
            success: function (res) {
                $("p").html(res.message)
            },
        })
    })

</script>
</body>
</html>
```

```python
@app.middleware("http")
async def CORSMiddleware(request: Request, call_next):
    response = await call_next(request)
    print(response.headers)
    return response
```

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:63342"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # *：代表所有客户端
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8080, debug=True, reload=True)
```

## 全局异常处理
```python
#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from starlette.responses import JSONResponse

async def exception_not_found(request, exc):
    return JSONResponse({
        "code": exc.status_code,
        "error": "没有定义这个请求地址"},
                        status_code=exc.status_code)

exception_handlers = {
    404: exception_not_found,
}

app = FastAPI(exception_handlers=exception_handlers)


if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)

```

## 字典json和对象的转换
```python
#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from typing import Union, Optional, List

from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    # 基础类型
    name: str  # 字符串类型
    password: str  # 字符串类型
    age: int  # 整形类型
    enable: bool = True  # 布尔类型



if __name__ == '__main__':
    try:
        user = Person(name='xiaozhong', password='123456', age=15)
    except ValidationError as e:
        print(e.errors())
        print(e.json())
    else:
        # print(user.dict())
        print(user.dict(exclude_unset=True))
        # print(user.dict(exclude={'password'}))
        print(user.json(exclude={'password'},models_as_dict=False))
        # # 进行拷贝==================
        # new_user = user.copy()
        # print("userID", user, id(user))
        # print("new_userID", new_user, id(new_user))
        # # 仅仅包含密码输出===========
        new_user = user.copy(include={'password'})
        # print("new_user", new_user)
        print("new_userID", new_user, id(new_user))

```

## 生命周期管理
```python
#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# 弃用
# from fastapi import FastAPI
# from starlette.background import BackgroundTasks
# import time
#
# app = FastAPI()
#
# # 生命周期异步上下文管理器处理程序代替单独的启动和关闭处理程序
# @app.on_event("startup")
# async def startup_event_async():
#     print("服务进程启动成功-async函数")
#
# @app.on_event("startup")
# def startup_event_sync():
#     print("服务进程启动成功-sync函数")
#
# @app.on_event("shutdown")
# async def shutdown_event_async():
#     print("服务进程已关闭-async函数")
#
#
# @app.on_event("shutdown")
# def shutdown_event_sync():
#     print("服务进程已关闭-sync函数")
#





from fastapi import FastAPI
from contextlib import asynccontextmanager
import time

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("服务进程启动成功-async lifespan")
    yield
    print("服务进程已关闭-async lifespan")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"msg": "Hello"}


if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True,port=10000)
```

## swagger文档
### 配置
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from contextlib import asynccontextmanager
import socket

HOST = "127.0.0.1"
PORT = 10000

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("✅ 服务启动中...")

    # 打印 Swagger 文档地址
    print_docs_urls(app, host=HOST, port=PORT)

    yield

    print("🛑 服务正在关闭...")

def print_docs_urls(app: FastAPI, host: str, port: int):
    ip = socket.gethostbyname(socket.gethostname())
    base_url = f"http://{host}:{port}"

    print(f"🔗 Swagger Docs: {base_url}{app.docs_url}")
    print(f"📘 ReDoc Docs  : {base_url}{app.redoc_url}")
    print(f"📄 OpenAPI JSON: {base_url}{app.openapi_url}")

app = FastAPI(
    title="文档的标题",
    description="关于该API文档的一些描述信息补充说明",
    version="v1.0.0",

    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi/openapi_json.json",

    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth=None,

    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  # 默认不展开 Models
        "docExpansion": "none",          # 默认折叠接口列表
        "displayRequestDuration": True,  # 显示请求时长
    },

    terms_of_service="https://terms/团队的官网网站/",
    deprecated=False,

    contact={
        "name": "API 负责人",
        "url": "https://xxx.cc",
        "email": "308711822@qq.com",
    },
    license_info={
        "name": "版权信息说明 License v3.0",
        "url": "https://xxxxxxx.com",
    },
    openapi_tags=[
        {
            "name": "通用接口",
            "description": "对外通用基础接口",
        },
        {
            "name": "测试分组",
            "description": "用于演示和测试功能接口",
        }
    ],
    servers=[
        {"url": "/", "description": "本地调试环境"},
        {"url": "https://xx.xx.com", "description": "线上测试环境"},
        {"url": "https://xx2.xx2.com", "description": "线上生产环境"},
    ],
    lifespan=lifespan
)

@app.get(path="/index", tags=["通用接口"])
async def index():
    return {"message": "Hello from /index"}

@app.post("/echo", tags=["测试分组"])
async def echo_data(payload: dict):
    return {"you_sent": payload}

if __name__ == "__main__":
    import uvicorn
    import os

    module_name = os.path.basename(__file__).replace(".py", "")
    print(f"🚀 启动模块：{module_name}")
    uvicorn.run(f"{module_name}:app", host=HOST, port=PORT, reload=True)

```

### 关闭
```python
#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
app = FastAPI(
    docs_url=None,
    redoc_url=None,
    # 或者直接设置openapi_url=None
    openapi_url=None,
)
if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)

```

## .env配置详解
.env

```python
DEBUG=true
TITLE="FastAPI"
DESCRIPTION="FastAPI文档明细描述"
vERSION="v1.0.0"
```

main.py

```python
#!/usr/bin/evn python
# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import Optional
from fastapi import FastAPI
from pydantic import validator, field_validator

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    title: str
    description: str
    version: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

    #@validator("version", pre=True)  v1弃用
    @field_validator("version", mode="before")
    def version_len_check(cls, v: str) -> Optional[str]:
        if v and len(v) == 0:
            return None
        return v

@lru_cache()
def get_settings():
    return Settings()

settings = Settings()
print(settings.debug)
print(settings.title)
print(settings.description)
print(settings.version)

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
app = FastAPI(
    debug=settings.debug,
    title=settings.title,
    description=settings.description,
    version=settings.version,
)


if __name__ == "__main__":
    import uvicorn
    import os
    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True,port=12345)

```

## 后台任务tasks
```python
#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from starlette.background import BackgroundTasks
import time
app = FastAPI(routes=None)
import asyncio
def send_mail(n):
    time.sleep(n)

@app.api_route(path="/index", methods=["GET", "POST"])
async def index(tasks: BackgroundTasks):
    tasks.add_task(send_mail, 10)
    print(id(asyncio.get_event_loop()))
    return {"index": "index"}

if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)

```

## 请求参数校验规则定义
```python
from fastapi import FastAPI
from pydantic import BaseModel, root_validator, Field, model_validator

app = FastAPI()


class User(BaseModel):
    username: str = Field(..., title='姓名', description='姓名字段需要长度大于6且小于等于12', max_length=12, min_length=6, example="Foo")
    age: int = Field(..., title='年龄', description='年龄需要大于18岁', ge=18, example=12)
    password_old: str = Field(..., title='旧密码', description='密码需要长度大于6', gl=6, example=6)
    password_new: str = Field(..., title='新密码', description='密码需要长度大于6', gl=6, example=6)

    # @root_validator  弃用
    # def check_passwords(cls, values):
    #     password_old, password_new = values.get('password_old'), values.get('password_new')
    #     # 新旧号码的确认匹配处理
    #     if password_old and password_new and password_old != password_new:
    #         raise ValueError('passwords do not match')
    #     return values
    @model_validator(mode="after")
    def check_passwords(self):
        if self.password_old != self.password_new:
            raise ValueError("passwords do not match")
        return self

@app.post("/user")
def read_user(user: User):
    return {
        'username': user.username,
        'password_old': user.password_old,
        'password_new': user.password_new,
    }


if __name__ == "__main__":
    import uvicorn
    import os

    app_modeel_name = os.path.basename(__file__).replace(".py", "")
    print(app_modeel_name)
    uvicorn.run(f"{app_modeel_name}:app", host='127.0.0.1', reload=True)

```

##  依赖注入`Depends`
###  实现一个简单的用户验证机制  
```python
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional

app = FastAPI()

# 模拟数据库中的 token 对应的用户
fake_users_db = {
    "token123": {"username": "alice"},
    "token456": {"username": "bob"},
}

# 依赖函数：用于从请求中获取 token 并验证用户身份
def get_current_user(token: Optional[str] = None):
    if token not in fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的令牌",
        )
    return fake_users_db[token]  # 返回用户信息

# 使用 Depends 注入 get_current_user 函数
@app.get("/profile")
def read_profile(user: dict = Depends(get_current_user)):
    # user 是 get_current_user 返回的字典
    return {"message": f"你好，{user['username']}！"}

```

###  数据库连接依赖（以 SQLAlchemy 为例）  
```python
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 模拟一个用户表
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# 创建表
Base.metadata.create_all(bind=engine)

# 依赖：获取数据库 session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db  # 使用 yield 是为了支持 with 自动关闭
    finally:
        db.close()

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user or {"error": "用户不存在"}

```

###  权限控制（角色权限依赖）  
```python
from fastapi import Depends, HTTPException, status, Request

# 模拟用户身份
def get_current_user(token: str = ""):
    users = {
        "admin-token": {"username": "admin", "role": "admin"},
        "user-token": {"username": "user", "role": "user"},
    }
    user = users.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="未认证")
    return user

# 权限控制依赖（只允许管理员访问）
def admin_required(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="权限不足")
    return user

@app.get("/admin")
def admin_panel(current_user: dict = Depends(admin_required)):
    return {"message": f"欢迎管理员 {current_user['username']}！"}

```

### 使用依赖
```python
# url注入
@app.get("/secure-data", dependencies=[Depends(verify_token), Depends(verify_key)])
def secure_data(
    user: dict = Depends(admin_required),  #要求执行admin_required的依赖
    db: Session = Depends(get_db)     #要求注入admin_required的依赖
):

# global注入
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


# yield注入
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
```

## <font style="color:rgba(0, 0, 0, 0.87);">返回自定义 </font>`Response`
```python
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")
```

## 日志配置
使用python库的logging， log_config.py  

```python
import logging
from logging.handlers import TimedRotatingFileHandler
import os

# 日志目录和文件
LOG_DIR = "logs"
LOG_FILE = "app.log"
os.makedirs(LOG_DIR, exist_ok=True)

# 创建 logger 实例
logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)  # 可设为 DEBUG、WARNING、ERROR 等

# 设置日志格式
log_format = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 控制台日志 handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)

# 文件日志 handler（按天轮转，保留7天）
file_handler = TimedRotatingFileHandler(
    filename=os.path.join(LOG_DIR, LOG_FILE),
    when="midnight",       # 每天轮转一次
    backupCount=7,         # 最多保留7个旧日志文件
    encoding="utf-8"
)
#或者使用文件大小轮转
# from logging.handlers import RotatingFileHandler

# file_handler = RotatingFileHandler(
#     filename=os.path.join(LOG_DIR, LOG_FILE),
#     maxBytes=5 * 1024 * 1024,  # 每个文件最大5MB
#     backupCount=5,             # 最多保留5个旧文件
#     encoding="utf-8"
# )

file_handler.setFormatter(log_format)

# 添加 handler
logger.addHandler(console_handler)
logger.addHandler(file_handler)


```

main.py，自定义中间件

```python
import time
import json
from fastapi import FastAPI, Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware
from log_config import logger

app = FastAPI()

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 记录请求信息
        request_time = time.time()
        try:
            request_body = await request.body()
            request_body = request_body.decode('utf-8')
        except Exception:
            request_body = "<无法解析的请求体>"

        logger.info(f"请求开始: {request.method} {request.url}")
        logger.info(f"请求头: {dict(request.headers)}")
        logger.info(f"请求体: {request_body}")

        # 处理请求
        response = await call_next(request)

        # 记录响应信息
        response_time = time.time()
        duration = response_time - request_time
        logger.info(f"响应状态: {response.status_code}")
        logger.info(f"处理耗时: {duration:.4f} 秒")

        return response

# 添加中间件
app.add_middleware(LoggingMiddleware)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}

```

## <font style="color:#080808;background-color:#ffffff;">redis异步操作集成</font>
[https://github.com/redis-developer/fastapi-redis-tutorial](https://github.com/redis-developer/fastapi-redis-tutorial)

### 📦 安装依赖
首先，确保安装了必要的依赖项：

```bash
pip install redis fastapi uvicorn pydantic async-timeout
```

### 🔧 `main.py`：
```python
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import redis.asyncio as redis
import asyncio
import async_timeout
from pydantic import BaseModel

class MessageEvent(BaseModel):
    username: str
    message: dict

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 创建 Redis 异步客户端，连接到本地 Redis 实例
    # decode_responses=True 表示返回的数据会自动解码为字符串，而不是字节
    redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

    # 创建 PubSub 对象，用于发布订阅功能
    pubsub = redis_client.pubsub()

    # 订阅 Redis 中的两个频道："channel:1" 和 "channel:2"
    await pubsub.subscribe("channel:1", "channel:2")

    # 将 Redis 客户端和 pubsub 对象挂载到 FastAPI 的应用状态中
    # 这样可以在其他地方通过 request.app.state.redis 获取
    app.state.redis = redis_client
    app.state.pubsub = pubsub

    # 启动订阅任务      
    async def reader(channel):
        while True:
            try:
                async with async_timeout.timeout(1):
                    msg = await channel.get_message(ignore_subscribe_messages=True)
                    if msg:
                        event = MessageEvent.parse_raw(msg["data"])
                        print("收到消息：", event)
                    await asyncio.sleep(0.01)
            except asyncio.TimeoutError:
                pass

    asyncio.create_task(reader(pubsub))

    # 发布一条测试消息 
    await redis_client.publish("channel:1", MessageEvent(username="start", message={"info": "应用启动"}).json())

    yield  # 应用运行期间
    # ========== 应用关闭时清理资源 ==========

    # 取消订阅频道，避免资源泄漏
    await pubsub.unsubscribe("channel:1", "channel:2")

    # 关闭 pubsub 对象（停止监听）
    await pubsub.close()

    # 关闭 Redis 客户端连接
    await redis_client.close()

app = FastAPI(lifespan=lifespan)

@app.get("/index")
async def index(req: Request):
    event = MessageEvent(username="api", message={"info": "来自接口的消息"})
    await req.app.state.redis.publish("channel:1", event.json())
    return {"msg": "消息已发布"}


from redis.asyncio.lock import Lock

@app.get("/lock-test")
async def lock_test(req: Request):
    redis_client = req.app.state.redis
    lock: Lock = redis_client.lock("test:lock", timeout=10)  # 超时10秒

    # 非阻塞尝试获取锁
    if await lock.acquire(blocking=False):
        try:
            print("成功获取锁，正在执行业务逻辑...")
            await asyncio.sleep(5)  # 模拟耗时任务
            return {"msg": "任务执行完成，锁释放"}
        finally:
            await lock.release()
    else:
        return {"msg": "资源繁忙，请稍后重试"}


```

## 集成celery
###  💠配置tasks
---

#### 🧰 安装依赖
首先安装必要依赖：

```bash
pip install fastapi celery redis uvicorn
```

---

#### 📦 项目结构
```plain
project/
├── main.py          # FastAPI 应用
├── celery_worker.py # Celery worker 启动入口
└── tasks.py         # 异步任务定义
```

---

#### 🔧 tasks.py：定义异步任务
```python
from celery import Celery

# 创建 Celery 实例，指定 Broker 使用 Redis
celery_app = Celery("worker", broker="redis://localhost:6379/0")

# 定义一个简单的异步任务
@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def slow_task(n):
    import time
    time.sleep(n)
    return f"任务耗时 {n} 秒执行完毕"
```

#### 🚀 main.py：FastAPI 接口触发任务
```python
from fastapi import FastAPI
from tasks import add, slow_task

app = FastAPI()

@app.get("/add")
def trigger_add(x: int, y: int):
    # 发送异步任务给 celery worker
    result = add.delay(x, y)
    return {"task_id": result.id}

@app.get("/slow")
def trigger_slow(n: int):
    result = slow_task.delay(n)
    return {"task_id": result.id}
```

---

#### 🛠 celery_worker.py：启动 worker 使用的脚本
```python
from tasks import celery_app

# 使用 celery -A celery_worker worker 启动即可
# 这个文件只为了暴露 celery_app 实例
```

---

#### ▶ 启动服务
##### **1️⃣**** 启动 Redis**
确保 Redis 已经运行在 `localhost:6379`

##### **2️⃣**** 启动 Celery worker**
```bash
celery -A celery_worker worker --loglevel=info
```

##### **3️⃣**** 启动 FastAPI 应用**
```bash
uvicorn main:app --reload
```

---

好的，我们继续为 FastAPI + Celery 集成添加以下高级功能：

---

### 🌸 集成 Flower 可视化监控
#### 🔧 安装 Flower
```bash
pip install flower
```

#### 🚀 启动 Flower 监控
```bash
celery -A celery_worker flower --port=5555
```

#### 📌 访问监控页面
浏览器访问 [http://localhost:5555](http://localhost:5555/)，可以实时查看：

+ 任务列表
+ 状态统计
+ 执行日志
+ 每个 worker 的资源信息等

---

### ✅ 配置任务结果存储（`result_backend`）
编辑 `tasks.py`，添加 Redis 作为任务结果后端：

```python
celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",  # 使用另一个 Redis DB 存结果
)
```

#### 🎯 在 FastAPI 中获取任务结果（可选）
```python
@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = add.AsyncResult(task_id)
    return {
        "status": result.status,
        "result": result.result if result.ready() else None
    }
```

---

### 🐳 Docker 化部署（示例）
#### 📁 创建 Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi celery redis uvicorn flower

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 📁 docker-compose.yml 示例
```yaml
version: '3.9'

services:
  redis:
    image: redis:6.2
    ports:
      - "6379:6379"

  backend:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - redis

  celery_worker:
    build: .
    command: celery -A celery_worker worker --loglevel=info
    depends_on:
      - redis

  flower:
    build: .
    command: celery -A celery_worker flower --port=5555
    ports:
      - "5555:5555"
    depends_on:
      - redis
```

---

### 🔁 任务重试机制与超时设置
在 `tasks.py` 中配置任务参数：

```python
@celery_app.task(
    bind=True,
    max_retries=3,            # 最多重试3次
    default_retry_delay=5,    # 每次重试间隔5秒
    time_limit=10             # 最长执行时间10秒，超时将被杀死
)
def fragile_task(self, x):
    try:
        # 假设某些业务可能抛异常
        if x < 0:
            raise ValueError("不能为负数")
        return x * 10
    except Exception as e:
        raise self.retry(exc=e)  # 调用 retry() 自动进入重试机制
```

## 集成Mongodb
### 集成motor异步client
```python
pip install motor
```

 database.py  

```python
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "mydb"

client: AsyncIOMotorClient = None
db = None

# 推荐使用 lifespan 生命周期管理连接
async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]

async def close_mongo_connection():
    client.close()

```

 models.py  

```python
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

# 自定义 ObjectId 的字段转换
class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("无效的 ObjectId")
        return ObjectId(v)

class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    name: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

```

 main.py  

```python
from fastapi import FastAPI, HTTPException
from database import connect_to_mongo, close_mongo_connection, db
from models import User
from bson import ObjectId

app = FastAPI(lifespan=lambda app: _lifespan(app))

# 异步 lifespan 管理连接
from contextlib import asynccontextmanager
@asynccontextmanager
async def _lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()

@app.post("/users")
async def create_user(user: User):
    user_dict = user.dict(by_alias=True, exclude_unset=True)
    result = await db["users"].insert_one(user_dict)
    user_dict["_id"] = result.inserted_id
    return user_dict

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="用户未找到")
    return user

```

### 集成Beanie odm框架
以下是一个完整的 FastAPI 集成 MongoDB 的最佳实践方案，涵盖 ✅ 使用 ODM 框架、✅ 自动建索引、✅ 认证配置、✅ Docker Compose 集成：

```bash
pip install beanie motor pydantic[dotenv]
```

```plain
project/
├── main.py             # FastAPI 应用入口
├── database.py         # MongoDB 初始化
├── models/user.py      # 用户模型，Beanie 文档类
├── .env                # Mongo 配置
├── docker-compose.yml  # 一键部署 Mongo
```

 `.env`（环境变量）

```plain
MONGO_URI=mongodb://root:example@mongo:27017/mydb?authSource=admin
DB_NAME=mydb
```

`models/user.py`

```python
from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(Document):
    name: str
    email: Indexed(EmailStr, unique=True)  # ✅ 自动建唯一索引

    class Settings:
        name = "users"  # Mongo 集合名

    class Config:
        schema_extra = {
            "example": {
                "name": "Tom",
                "email": "tom@example.com"
            }
        }
```

 `database.py`

```python
import motor.motor_asyncio
from beanie import init_beanie
from models.user import User
from os import getenv
from dotenv import load_dotenv

load_dotenv()

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(getenv("MONGO_URI"))
    await init_beanie(database=client[getenv("DB_NAME")], document_models=[User])
```

`main.py`

```python
from fastapi import FastAPI, HTTPException
from models.user import User
from database import init_db
from pydantic import BaseModel, EmailStr
from contextlib import asynccontextmanager

class UserIn(BaseModel):
    name: str
    email: EmailStr

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/users")
async def create_user(user_in: UserIn):
    if await User.find_one(User.email == user_in.email):
        raise HTTPException(status_code=409, detail="邮箱已存在")
    user = User(**user_in.dict())
    await user.insert()
    return user

@app.get("/users")
async def list_users():
    return await User.find_all().to_list()
```

---

`docker-compose.yml`

```yaml
version: "3.8"
services:
  mongo:
    image: mongo:6.0
    container_name: mongo
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

---

###  ODM复杂嵌套模型（如用户档案、地址信息）  
🗂️ 示例模型结构：`models/user.py`

```python

from beanie import Document, Indexed
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# 嵌套地址信息
class Address(BaseModel):
    street: str
    city: str
    zipcode: str
    country: str

# 用户档案
class Profile(BaseModel):
    bio: Optional[str] = None
    age: Optional[int] = None
    addresses: List[Address] = []

# 用户主模型
class User(Document):
    name: str
    email: Indexed(EmailStr, unique=True)
    profile: Optional[Profile] = None

    class Settings:
        name = "users"
```

🧪 示例数据提交 JSON：

```json

{
  "name": "小中同学",
  "email": "xiaozhong@example.com",
  "profile": {
    "bio": "全栈开发者",
    "age": 30,
    "addresses": [
      {
        "street": "天安门大街 1 号",
        "city": "北京",
        "zipcode": "100000",
        "country": "中国"
      }
    ]
  }
}
```

###  MongoDB 副本集 / 集群认证配置  
🔐 修改 `.env` 中连接 URI

Mongo URI 语法支持集群或副本集，例如：

```python

MONGO_URI=mongodb://root:example@mongo1:27017,mongo2:27017,mongo3:27017/mydb?replicaSet=rs0&authSource=admin
```

+ `mongo1,mongo2,mongo3`: 指定多个 Mongo 节点。
+ `replicaSet=rs0`: 副本集名称，需与集群设置一致。
+ `authSource=admin`: 认证数据库。

🐳 Docker Compose 支持副本集（示意）

副本集需要容器互通、时间同步，以下是最小可运行配置之一（简化版）：

```yaml
version: '3.8'
services:
  mongo1:
    image: mongo:6.0
    container_name: mongo1
    command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

  mongo2:
    image: mongo:6.0
    container_name: mongo2
    command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]

  mongo3:
    image: mongo:6.0
    container_name: mongo3
    command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]

volumes:
  mongo-data:
```

初始化副本集：

```bash
docker exec -it mongo1 mongosh
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" }
  ]
})
```

### curd和分页+模糊搜索
✅ 1. 用户模型（支持分页 + 模糊搜索）

```python
# models/user.py
from beanie import Document, Indexed
from pydantic import EmailStr
from typing import Optional

class User(Document):
    name: str
    email: Indexed(EmailStr, unique=True)
    age: Optional[int]

    class Settings:
        name = "users"
```

---

✅ 2. 创建用户、查询、分页、模糊搜索、导出接口

```python
# main.py
from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from models.user import User
from pydantic import BaseModel
import beanie, motor.motor_asyncio
import csv, io
from fastapi.responses import StreamingResponse

app = FastAPI()

# 初始化数据库连接
@app.on_event("startup")
async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    await beanie.init_beanie(database=client.mydb, document_models=[User])


# 创建用户
class UserIn(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    user_doc = User(**user.dict())
    await user_doc.insert()
    return user_doc


# 查询 + 分页 + 模糊匹配
@app.get("/users/", response_model=List[User])
async def list_users(
    keyword: Optional[str] = Query(None, description="按姓名模糊匹配"),
    skip: int = 0,
    limit: int = 10
):
    query = {}
    if keyword:
        query["name"] = {"$regex": keyword, "$options": "i"}
    users = await User.find(query).skip(skip).limit(limit).to_list()
    return users


# 导出为 CSV
@app.get("/users/export/csv")
async def export_users_csv():
    users = await User.find_all().to_list()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["name", "email", "age"])
    for u in users:
        writer.writerow([u.name, u.email, u.age or ""])
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=users.csv"
    })
```

---

✅ 3. 导出为 Excel（可选）

如果需要支持导出为 `.xlsx`，可用 `openpyxl`：

```bash
pip install openpyxl
```

```python
# 导出 Excel
from openpyxl import Workbook

@app.get("/users/export/excel")
async def export_users_excel():
    users = await User.find_all().to_list()
    wb = Workbook()
    ws = wb.active
    ws.append(["name", "email", "age"])
    for u in users: 
        ws.append([u.name, u.email, u.age or ""])
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    return StreamingResponse(output, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={
        "Content-Disposition": "attachment; filename=users.xlsx"
    })
```

---

## 集成OAuth2安全鉴权
```python
pip install python-multipart pyjwt passlib[bcrypt] fastapi uvicorn
# 如果您打算使用类似 RSA 或 ECDSA 的数字签名算法，您应该安装加密库依赖项 pyjwt[crypto]
# 这是因为 OAuth2 使用表单数据发送 username 与 password。
# Passlib 是处理密码哈希的 Python 包
```

<font style="color:rgba(0, 0, 0, 0.87);">OAuth2的</font>作用域和jwt使用

```python
from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta

# 密钥配置
SECRET_KEY = "super-secret"  # 用于对 JWT 令牌进行加密和解密的密钥，必须保密，建议设置为环境变量
ALGORITHM = "HS256"          # 使用的加密算法，这里使用 HMAC-SHA256，FastAPI + JWT 默认推荐该算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 设置访问令牌（access token）的有效期为 30 分钟，过期后需重新登录

# OAuth2 定义多个 scopes
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"read": "读取权限", "write": "写入权限", "admin": "管理员权限"},
)

# 模拟用户数据
fake_users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": "$2b$12$7qA1xbsMTLtH3W6rsH33QOnfpxn1qP1B9xuJzW2GH77j3tZddLaZu",  # password
        "scopes": ["read"],
    },
    "bob": {
        "username": "bob",
        "hashed_password": "$2b$12$7qA1xbsMTLtH3W6rsH33QOnfpxn1qP1B9xuJzW2GH77j3tZddLaZu",  # password
        "scopes": ["read", "write", "admin"],
    }
}

class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []

class User(BaseModel):
    username: str
    scopes: List[str] = []

# 创建 token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 获取用户
def get_user(username: str) -> Optional[User]:
    user = fake_users_db.get(username)
    if user:
        return User(username=user["username"], scopes=user["scopes"])

# 获取当前用户并验证 scope
async def get_current_user(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="权限不足或认证失败",
        headers={"WWW-Authenticate": f'Bearer scope="{security_scopes.scope_str}"'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        token_scopes = payload.get("scopes", [])
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username, scopes=token_scopes)
    except JWTError:
        raise credentials_exception

    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="权限不足",
                headers={"WWW-Authenticate": f'Bearer scope="{security_scopes.scope_str}"'},
            )

    return user


app = FastAPI()


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict or form_data.password != "password":
        raise HTTPException(status_code=400, detail="登录失败")
    token = create_access_token(
        data={"sub": form_data.username, "scopes": user_dict["scopes"]}
    )
    return {"access_token": token, "token_type": "bearer"}


@app.get("/read", dependencies=[Security(get_current_user, scopes=["read"])])
async def read_data():
    return {"data": "这是只读数据"}

@app.post("/write", dependencies=[Security(get_current_user, scopes=["write"])])
async def write_data():
    return {"status": "写入成功"}

@app.delete("/admin", dependencies=[Security(get_current_user, scopes=["admin"])])
async def admin_delete():
    return {"status": "管理员删除成功"}

```

##  HTTP Basic 认证示例  
FastAPI 提供了对 HTTP 基本认证（HTTP Basic Auth）的内置支持，适用于简单的身份验证场景。以下是一个完整的示例，展示如何使用 FastAPI 实现 HTTP Basic 认证，并验证用户名和密码  

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

app = FastAPI()
security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "alice")
    correct_password = secrets.compare_digest(credentials.password, "wonderland")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}

```

测试

+ 当您在浏览器中访问受保护的端点（例如 `/users/me`）时，浏览器会弹出一个对话框，提示您输入用户名和密码。
+ 输入正确的凭据后，浏览器会自动将其编码为 Base64，并添加到请求的 `Authorization` 头部中。

使用curl工具进行测试

```bash
curl -u alice:wonderland http://localhost:8000/users/me
```

 使用 FastAPI 的 `TestClient` 进行自动化测试  

```bash
pip install httpx
```

```python
from fastapi.testclient import TestClient
from myapp import app  # 替换为您的 FastAPI 应用实例

client = TestClient(app)

def test_read_current_user():
    response = client.get("/users/me", auth=("alice", "wonderland"))
    assert response.status_code == 200
    assert response.json() == {"username": "alice"}

def test_read_current_user_invalid_credentials():
    response = client.get("/users/me", auth=("alice", "wrongpassword"))
    assert response.status_code == 401

```

## WebSocket聊天室
顺便学习下uv管理

<font style="color:#080808;background-color:#ffffff;">pyproject.toml</font>

```toml
# pyproject.toml
[project]
name = "fastapi_websockets"
version = "0.1.0"
description = "Project description"
requires-python = ">=3.11"
dependencies = [
    "anyio>=4.9.0",
    "fastapi>=0.115.12",
    "httpx>=0.28.1",
    "pytest>=8.3.5",
    "trio>=0.30.0",
    "uvicorn>=0.34.2",
    "websockets>=15.0.1",
]

[project.optional-dependencies]
dev = [

]
# 下载源配置 uv sync
[[tool.uv.index]]
#[[index]]这个也可以
# 默认源
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = true
#使用uv pip时配置
[tool.uv.pip]
index-url = "https://mirrors.aliyun.com/pypi/simple/"
```

```toml
uv init #创建配置文件初始化
uv venv --python 3.11
./venv/scripts/activate
uv add xxx
uv remove xxx
uv sync #类似npm install，安装所有依赖，并且生成uv.lock
uv sync --upgrade #更新软件包
```

main.py

```python
# backend/main.py
import json

from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect  # ✅ 正确导入方式

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 添加 CORS 中间件，允许前端地址访问（开发阶段使用 *）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议替换为具体地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

# 存储 WebSocket 连接的列表
active_connections = {}
online_users = []


@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # 通过 WebSocket 连接的客户端保持一个字典映射: 用户名 -> WebSocket
    username = None

    try:
        while True:
            # 接受客户端发送的消息
            data = await websocket.receive_text()
            message_data = json.loads(data)  # 解析收到的 JSON 数据
            username = message_data.get("uAsername")
            text = message_data.get("text")

            # 如果用户名尚未注册，则注册该用户
            if username and username not in online_users:
                online_users.append(username)

            # 记录该连接
            active_connections[username] = websocket

            # 广播消息给其他用户
            for connection in active_connections.values():
                await connection.send_text(json.dumps({
                    "username": username,
                    "text": text,
                }))

            # 广播更新在线用户列表
            for connection in active_connections.values():
                await connection.send_text(json.dumps({
                    "type": "user_list",
                    "users": online_users,
                }))

    except WebSocketDisconnect:
        # 用户断开连接时移除该用户
        if username in online_users:
            online_users.remove(username)
        active_connections.pop(username, None)

        # 广播更新在线用户列表
        for connection in active_connections.values():
            await connection.send_text(json.dumps({
                "type": "user_list",
                "users": online_users,
            }))

if __name__ == '__main__':
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    print(app_model_name)
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True)

```

单元测试test_ws.py

```python
# backend/test_ws.py

import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.websockets import WebSocketDisconnect
from main import app  # 导入你项目的 FastAPI 实例


@pytest.mark.anyio
async def test_websocket_chat():
    client = TestClient(app)

    with client.websocket_connect("/ws/chat") as websocket1:
        with client.websocket_connect("/ws/chat") as websocket2:
            # 客户端1发送消息
            websocket1.send_text("你好，客户端2")
            # 客户端2接收消息
            data = websocket2.receive_text()
            assert data == "你好，客户端2"

```

初始化前端项目react

```python
npm create vite@latest frontend -- --template react
cd frontend
pnpm install
pnpm run dev
```

```javascript
// frontend/src/App.js

import React from "react";
import Chat from "./Chat";

function App() {
  return (
    <div className="App">
    <Chat />
    </div>
  );
}

export default App;
```

```javascript
// frontend/src/Chat.js

import React, { useState, useEffect, useRef } from "react";

const Chat = () => {
  const [message, setMessage] = useState("");  // 输入框中的消息
  const [messages, setMessages] = useState([]);  // 存储聊天记录
  const [username, setUsername] = useState("");  // 用户名
  const [onlineUsers, setOnlineUsers] = useState([]);  // 在线用户列表
  const ws = useRef(null);  // WebSocket 实例

  // 组件挂载时创建 WebSocket 连接
  useEffect(() => {
    if (username === "") {
      alert("请先设置用户名！");
      return;
    }

    // 连接到后端的 WebSocket
    ws.current = new WebSocket("ws://localhost:8000/ws/chat");

    // 连接成功日志
    ws.current.onopen = () => {
      console.log("WebSocket连接已建立");
    };

    // 监听收到的消息
    ws.current.onmessage = (event) => {
      const receivedMessage = JSON.parse(event.data);  // 假设后端返回JSON格式
      console.log("收到消息:", receivedMessage);

      if (receivedMessage.type === "user_list") {
        setOnlineUsers(receivedMessage.users);  // 更新在线用户列表
      } else {
        setMessages((prevMessages) => [
          ...prevMessages,
          receivedMessage,
        ]);
      }
    };

    // 监听 WebSocket 错误
    ws.current.onerror = (error) => {
      console.error("WebSocket 发生错误:", error);
    };

    // 清理函数，在组件卸载时关闭 WebSocket 连接
    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, [username]);

  // 发送消息
  const sendMessage = () => {
    if (message.trim() !== "") {
      const messageData = {
        username: username,
        text: message,
      };
      ws.current.send(JSON.stringify(messageData));  // 发送消息时带上用户名
      setMessage("");  // 清空输入框
    }
  };

  return (
    <div>
    <h1>聊天室</h1>
    <div>
    {!username && (
      <div>
      <input
      type="text"
  placeholder="请输入用户名"
  value={username}
  onChange={(e) => setUsername(e.target.value)}
    />
    </div>
  )}
  <div style={{ display: "flex" }}>
  <div style={{ width: "300px", marginRight: "20px" }}>
  <h2>在线用户</h2>
  <ul>
  {onlineUsers.map((user, index) => (
    <li key={index}>{user}</li>
                  ))}
</ul>
  </div>
  <div style={{ flex: 1 }}>
  <div
style={{
  height: "300px",
  overflowY: "scroll",
  border: "1px solid #ccc",
  marginBottom: "10px",
  padding: "10px",
}}
>
{messages.map((msg, index) => (
  <div
              key={index}
 style={{
   display: "flex",
   alignItems: "center",
   marginBottom: "10px",
 }}
>
  <img
src={`https://avatars.dicebear.com/api/initials/${msg.username}.svg`}
alt={msg.username}
style={{
  width: "30px",
  height: "30px",
  borderRadius: "50%",
                      marginRight: "10px",
                    }}
                  />
                  <div
                    style={{
                      padding: "10px",
                      borderRadius: "8px",
                      backgroundColor: msg.username === username ? "#cce5ff" : "#f1f1f1",
                      color: "#333",
                      maxWidth: "60%",
                    }}
                  >
                    <strong>{msg.username}</strong>: {msg.text}
                  </div>
                </div>
              ))}
            </div>
            <div>
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="请输入消息"
                style={{ width: "300px", marginRight: "10px" }}
              />
              <button onClick={sendMessage}>发送</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Chat;
```

初始化vue项目

```javascript
pnpm create vite@latest vite-vue-chat --template vue
cd vite-vue-chat
pnpm install
pnpm dev
pnpm install pinia # 状态管理（推荐）
pnpm install uuid  # 生成临时用户 ID（可选）
```

`src/main.js`

```javascript
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

 src/App.vue  

```javascript
<template>
  <div class="app">
  <h1>Vue 聊天室</h1>
  <div v-if="!username">
  <input v-model="tempName" placeholder="输入用户名" @keyup.enter="setUsername" />
  <button @click="setUsername">进入聊天室</button>
  </div>
  <div v-else>
  <p>你好，{{ username }}！</p>
  <UserList :users="users" />
  <ChatWindow :username="username" :socket="socket" :messages="messages" />
  </div>
  </div>
  </template>

  <script setup>
  import { ref } from 'vue'
import ChatWindow from './components/ChatWindow.vue'
import UserList from './components/UserList.vue'

const username = ref('')
const tempName = ref('')
const messages = ref([])
const users = ref([])
const socket = ref(null)

function setUsername() {
  if (!tempName.value.trim()) return
  username.value = tempName.value
  socket.value = new WebSocket('ws://localhost:8000/ws/chat')

  socket.value.onopen = () => {
    console.log('连接成功')
  }

  socket.value.onmessage = (event) => {
    const data = JSON.parse(event.data)
    if (data.type === 'user_list') {
      users.value = data.users
    } else {
      messages.value.push(data)
    }
  }

  socket.value.onerror = (e) => {
    console.error('WebSocket 错误', e)
  }

  socket.value.onclose = () => {
    console.warn('连接已关闭')
  }
}
</script>

  <style>
  .app {
  max-width: 600px;
  margin: 0 auto;
  font-family: sans-serif;
}
</style>

```

 src/components/ChatWindow.vue  

```javascript
<template>
  <div class="chat">
    <div class="messages">
      <div v-for="(msg, i) in messages" :key="i">
        <strong>{{ msg.username }}:</strong> {{ msg.text }}
      </div>
    </div>
    <input v-model="input" @keyup.enter="sendMessage" placeholder="输入消息..." />
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
const props = defineProps(['username', 'socket', 'messages'])

const input = ref('')

function sendMessage() {
  if (!input.value.trim()) return
  props.socket.send(
    JSON.stringify({
      username: props.username,
      text: input.value,
    })
  )
  input.value = ''
}
</script>

<style>
.chat {
  border: 1px solid #ccc;
  padding: 10px;
}
.messages {
  height: 200px;
  overflow-y: auto;
  margin-bottom: 10px;
}
</style>

```

`src/components/UserList.vue`

```javascript
<template>
  <div class="users">
  <h3>在线用户</h3>
  <ul>
  <li v-for="user in users" :key="user">{{ user }}</li>
  </ul>
  </div>
  </template>

  <script setup>
  defineProps(['users'])
  </script>

  <style>
  .users {
  margin-top: 10px;
}
</style>

```

## OpenAPI 回调
```toml
uv add fastapi>=0.115.12  #亲测版本需要是这个，否则回调函数无法适配文档自动生成
```

```javascript
from typing import Union
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, HttpUrl

app = FastAPI()
invoices_callback_router = APIRouter()

# 定义发票模型
class Invoice(BaseModel):
    id: str
    customer: str
    total: float

# 定义回调通知的请求体模型
class InvoiceEvent(BaseModel):
    description: str
    paid: bool

# 定义回调通知的响应体模型
class InvoiceEventReceived(BaseModel):
    received: bool

# 定义回调路径和请求体
@invoices_callback_router.post(
    "{$callback_url}/invoices/{$request.body.id}",
    response_model=InvoiceEventReceived,
)
def invoice_notification(body: InvoiceEvent):
    """
    回调通知接口的定义，用于文档展示。
    实际不会被本服务调用，由外部服务实现。
    """
    pass

# 创建发票的主接口，包含回调定义
@app.post("/invoices/", callbacks=invoices_callback_router.routes)
def create_invoice(invoice: Invoice, callback_url: Union[HttpUrl, None] = None):
    """
    创建发票的接口。

    参数:
    - invoice: 发票信息
    - callback_url: 用户提供的回调地址

    流程:
    1. 接收发票信息
    2. 处理发票（例如，发送给客户、收款等）
    3. 向用户提供的回调地址发送通知
    """
    # 实际处理逻辑省略
    return {"message": "Invoice created successfully"}



if __name__ == '__main__':
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    print(app_model_name)
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True,port=12345)
```

## <font style="color:rgba(0, 0, 0, 0.87);">Webhook</font>
### <font style="color:rgba(0, 0, 0, 0.87);">Webhook</font>是什么
+ **直观比喻**  
把 Webhook 想象成“事件的邮递员”：当 A 系统发生某件事（比如用户下单、文件上传、支付成功）时，就会把相关信息「主动」推送（POST）给你预先留好的网址（callback URL）。
+ **与轮询的区别**
    - 轮询（Polling）：你不停地去问 A 系统 “现在有新事件没？”。
    - Webhook：A 系统自己会“敲门”通知你，不需要你去打听，省时省资源。

### 使用场景
1. **支付通知**
    - 支付平台（如 Stripe、PayPal）在用户完成付款后，向商户系统的 Webhook URL 发通知，告知支付结果。
2. **持续集成/部署（CI/CD）**
    - GitHub、GitLab 在有新提交或合并请求时，通过 Webhook 通知 Jenkins、GitHub Actions 等自动跑测试、部署。
3. **聊天机器人**
    - 当 Slack、钉钉中有人@机器人时，它会把消息发到你的 Webhook，你再根据内容做智能回复。
4. **第三方服务通知**
    - 如订单系统、新用户注册、监控告警等，把事件第一时间推送给你的后台或消息中心，触发后续处理。

### 参考代码
比如支付时，需要提供给在微信或者支付宝配置的webhook，根据返回才知道支付的成功和失败，并且需要检验签名，以此来判断webhook的回调是否合法。

```python
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import hmac
import hashlib

app = FastAPI()

# 用于验证Webhook签名的密钥
WEBHOOK_SECRET = "your-webhook-secret"

# 定义支付事件的数据模型
class PaymentEvent(BaseModel):
    payment_id: str
    status: str
    amount: float
    currency: str

# Webhook端点，接收支付通知
@app.post("/webhooks/payment")
async def payment_webhook(request: Request, event: PaymentEvent):
    """
    接收并处理来自支付平台的支付通知。
    """
    # 从请求头中提取签名
    signature = request.headers.get("X-Signature")
    if not signature:
        raise HTTPException(status_code=400, detail="缺少签名")

    # 使用HMAC-SHA256验证签名
    body = await request.body()
    expected_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, expected_signature):
        raise HTTPException(status_code=403, detail="签名无效")

    # 处理支付事件
    if event.status == "completed":
        print(f"支付 {event.payment_id} 完成: {event.amount} {event.currency}")
    elif event.status == "failed":
        print(f"支付 {event.payment_id} 失败")
    else:
        print(f"未知的支付状态: {event.status}")

    return {"status": "received"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

