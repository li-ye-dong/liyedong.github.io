<font style="color:rgb(62, 67, 73);">喜欢 Python 的原因之一是交互式的 shell ，它可以让你实时运行 Python 命令， 并且立即得到结果。 Flask 本身不带交互 shell ，因为它不需要特定的前期设置， 只要在 shell 中导入你的应用就可以开始使用了。</font>

<font style="color:rgb(62, 67, 73);">有些辅助工具可以让你在 shell 中更舒服。在交互终端中最大的问题是你不会像浏 览器一样触发一个请求，这就意味着无法使用</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">g</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.g)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">和</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">request</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.request)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">等对象。那么如何在 shell 中测试依赖这些对象的代码呢？</font>

<font style="color:rgb(62, 67, 73);">这里有一些有用的辅助函数。请记住，这些辅助函数不仅仅只能用于 shell ，还可 以用于单元测试和其他需要假冒请求情境的情况下。</font>

<font style="color:rgb(62, 67, 73);">在读下去之前最好你已经读过</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">请求情境</font>](https://dormousehole.readthedocs.io/en/2.3.2/reqcontext.html)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">。</font>

## <font style="color:black;">命令行接口</font>
<font style="color:rgb(62, 67, 73);">自 Flask 0.11 版开始，推荐在 shell 中使用</font><font style="color:rgb(62, 67, 73);"> </font>`<font style="color:rgb(34, 34, 34);background-color:rgb(232, 239, 240);">flask</font><font style="color:rgb(34, 34, 34);background-color:rgb(232, 239, 240);"> </font><font style="color:rgb(34, 34, 34);background-color:rgb(232, 239, 240);">shell</font>`<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">命令，它可以为你 做许多自动化工作。比如在 shell 中自动初始化应用情境。</font>

<font style="color:rgb(62, 67, 73);">更多信息参见</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">命令行接口</font>](https://dormousehole.readthedocs.io/en/2.3.2/cli.html)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">。</font>

## <font style="color:black;">创建一个请求情境</font>
<font style="color:rgb(62, 67, 73);">在 shell 中创建一个正确的请求情境的最简便的方法是使用</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">test_request_context</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.Flask.test_request_context)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">方法。这个方法会创建一个</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">RequestContext</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.ctx.RequestContext)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">：</font>

```python
>>> ctx = app.test_request_context()
```

<font style="color:rgb(62, 67, 73);">通常你会使用</font><font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">with</font><font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">语句来激活请求对象，但是在 shell 中，可以简便地手动使用</font><font style="color:rgb(62, 67, 73);"> </font>`**<font style="color:rgb(34, 34, 34);">push()</font>**`<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">和</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">pop()</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.ctx.RequestContext.pop)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">方法：</font>

```python
>>> ctx.push()
```

<font style="color:rgb(62, 67, 73);">从这里开始，直到调用</font><font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">pop</font><font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">之前，你可以使用请求对象：</font>

```python
>>> ctx.pop()
```

## <font style="color:black;">发送请求前/后动作</font>
<font style="color:rgb(62, 67, 73);">仅仅创建一个请求情境还是不够的，需要在请求前运行的代码还是没有运行。比如， 在请求前可以会需要转接数据库，或者把用户信息储存在</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">g</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.g)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">对象中。</font>

<font style="color:rgb(62, 67, 73);">使用</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">preprocess_request()</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.Flask.preprocess_request)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">可以方便地模拟请求前/后动作：</font>

```python
>>> ctx = app.test_request_context()
>>> ctx.push()
>>> app.preprocess_request()
```

<font style="color:rgb(62, 67, 73);">请记住，</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">preprocess_request()</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.Flask.preprocess_request)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">函数可以会返回一个响应对 象。如果返回的话请忽略它。</font>

<font style="color:rgb(62, 67, 73);">如果要关闭一个请求，那么你需要在请求后函数（由</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">process_response()</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.Flask.process_response)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">触发）作用于响应对象前关闭：</font>

```python
>>> app.process_response(app.response_class())
<Response 0 bytes [200 OK]>
>>> ctx.pop()
```

[<font style="color:rgb(62, 67, 73);">teardown_request()</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html#flask.Flask.teardown_request)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">函数会在环境弹出后自动执行。我们可以 使用这些函数来销毁请求情境所需要使用的资源（如数据库连接）。</font>

## <font style="color:black;">在 Shell 中玩得更爽</font>
<font style="color:rgb(62, 67, 73);">如果你喜欢在 shell 中的感觉，那么你可以创建一个导入有关东西的模块，在模块 中还可以定义一些辅助方法，如初始化数据库或者删除表等等。假设这个模块名为</font><font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">shelltools</font><font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">，那么在开始时你可以：</font>

<font style="color:rgb(62, 67, 73);background-color:rgb(248, 248, 248);">>>> from shelltools import *</font>

