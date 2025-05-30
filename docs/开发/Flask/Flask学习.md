# 概述
<font style="color:rgb(62, 67, 73);">欢迎阅读 Flask 的文档。推荐您先从《</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">安装</font>](https://dormousehole.readthedocs.io/en/2.3.2/installation.html)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">》入手，然后阅 读《</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">快速上手</font>](https://dormousehole.readthedocs.io/en/2.3.2/quickstart.html)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">》。更详细一些的《</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">教程</font>](https://dormousehole.readthedocs.io/en/2.3.2/tutorial/index.html)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">》介绍 了如何创建一个完整（尽管很小）的 Flask 应用。《</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">Flask 方案</font>](https://dormousehole.readthedocs.io/en/2.3.2/patterns/index.html)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">》 中介绍了一些常用的解决方案。其余的文档详细介绍了 Flask 的每一个组件。 《</font><font style="color:rgb(62, 67, 73);"> </font>[<font style="color:rgb(62, 67, 73);">API</font>](https://dormousehole.readthedocs.io/en/2.3.2/api.html)<font style="color:rgb(62, 67, 73);"> </font><font style="color:rgb(62, 67, 73);">》提供了最详细的参考。</font>

<font style="color:rgb(62, 67, 73);">Flask 依赖 </font>[<font style="color:rgb(62, 67, 73);">Werkzeug</font>](https://werkzeug.palletsprojects.com/)<font style="color:rgb(62, 67, 73);"> WSGI 套件、 </font>[<font style="color:rgb(62, 67, 73);">Jinja</font>](https://jinja.palletsprojects.com/)<font style="color:rgb(62, 67, 73);"> 模板引擎和 </font>[<font style="color:rgb(62, 67, 73);">Click</font>](https://click.palletsprojects.com/)<font style="color:rgb(62, 67, 73);"> CLI 套 件。查找信息时请不要忘了查阅它们的文档。</font>

<font style="color:rgb(62, 67, 73);">官网链接地址如下：</font>

[https://dormousehole.readthedocs.io/en/2.3.2/index.html](https://dormousehole.readthedocs.io/en/2.3.2/index.html)

# 安装
```python
poetry add Flask:2.3.2
```

# <font style="color:black;">用户指南</font>
<font style="color:rgb(62, 67, 73);">Flask 提供了配置和约定，以及合理的默认值，以开始使用。文档的这一部分 解释了 Flask 框架的不同部分以及如何使用、定制和扩展。除了 Flask 本身， 社区维护的扩展可以添加更多功能。</font>

+ [<font style="color:rgb(62, 67, 73);">安装</font>](https://dormousehole.readthedocs.io/en/latest/installation.html)
    - [<font style="color:rgb(62, 67, 73);">Python 版本</font>](https://dormousehole.readthedocs.io/en/latest/installation.html#python)
    - [<font style="color:rgb(62, 67, 73);">依赖</font>](https://dormousehole.readthedocs.io/en/latest/installation.html#id2)
    - [<font style="color:rgb(62, 67, 73);">虚拟环境</font>](https://dormousehole.readthedocs.io/en/latest/installation.html#id4)
    - [<font style="color:rgb(62, 67, 73);">安装 Flask</font>](https://dormousehole.readthedocs.io/en/latest/installation.html#flask)
+ [<font style="color:rgb(62, 67, 73);">快速上手</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html)
    - [<font style="color:rgb(62, 67, 73);">一个最小的应用</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id2)
    - [<font style="color:rgb(62, 67, 73);">调试模式</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id3)
    - [<font style="color:rgb(62, 67, 73);">HTML 转义</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#html)
    - [<font style="color:rgb(62, 67, 73);">路由</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id4)
    - [<font style="color:rgb(62, 67, 73);">静态文件</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id7)
    - [<font style="color:rgb(62, 67, 73);">渲染模板</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id8)
    - [<font style="color:rgb(62, 67, 73);">操作请求数据</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id12)
    - [<font style="color:rgb(62, 67, 73);">重定向和错误</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id16)
    - [<font style="color:rgb(62, 67, 73);">关于响应</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#about-responses)
    - [<font style="color:rgb(62, 67, 73);">会话</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#sessions)
    - [<font style="color:rgb(62, 67, 73);">消息闪现</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id19)
    - [<font style="color:rgb(62, 67, 73);">日志</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id20)
    - [<font style="color:rgb(62, 67, 73);">集成 WSGI 中间件</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#wsgi)
    - [<font style="color:rgb(62, 67, 73);">使用 Flask 扩展</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#flask)
    - [<font style="color:rgb(62, 67, 73);">部署到网络服务器</font>](https://dormousehole.readthedocs.io/en/latest/quickstart.html#id21)
+ [<font style="color:rgb(62, 67, 73);">教程</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/index.html)
    - [<font style="color:rgb(62, 67, 73);">项目布局</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/layout.html)
    - [<font style="color:rgb(62, 67, 73);">应用设置</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/factory.html)
    - [<font style="color:rgb(62, 67, 73);">定义和操作数据库</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/database.html)
    - [<font style="color:rgb(62, 67, 73);">蓝图和视图</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/views.html)
    - [<font style="color:rgb(62, 67, 73);">模板</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/templates.html)
    - [<font style="color:rgb(62, 67, 73);">静态文件</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/static.html)
    - [<font style="color:rgb(62, 67, 73);">博客蓝图</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/blog.html)
    - [<font style="color:rgb(62, 67, 73);">项目可安装化</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/install.html)
    - [<font style="color:rgb(62, 67, 73);">测试覆盖</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/tests.html)
    - [<font style="color:rgb(62, 67, 73);">部署产品</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/deploy.html)
    - [<font style="color:rgb(62, 67, 73);">继续开发！</font>](https://dormousehole.readthedocs.io/en/latest/tutorial/next.html)
+ [<font style="color:rgb(62, 67, 73);">模板</font>](https://dormousehole.readthedocs.io/en/latest/templating.html)
    - [<font style="color:rgb(62, 67, 73);">Jinja 设置</font>](https://dormousehole.readthedocs.io/en/latest/templating.html#jinja)
    - [<font style="color:rgb(62, 67, 73);">标准环境</font>](https://dormousehole.readthedocs.io/en/latest/templating.html#id2)
    - [<font style="color:rgb(62, 67, 73);">控制自动转义</font>](https://dormousehole.readthedocs.io/en/latest/templating.html#id3)
    - [<font style="color:rgb(62, 67, 73);">注册过滤器</font>](https://dormousehole.readthedocs.io/en/latest/templating.html#registering-filters)
    - [<font style="color:rgb(62, 67, 73);">环境处理器</font>](https://dormousehole.readthedocs.io/en/latest/templating.html#id5)
+ [<font style="color:rgb(62, 67, 73);">测试 Flask 应用</font>](https://dormousehole.readthedocs.io/en/latest/testing.html)
    - [<font style="color:rgb(62, 67, 73);">识别测试</font>](https://dormousehole.readthedocs.io/en/latest/testing.html#id1)
    - [<font style="color:rgb(62, 67, 73);">Fixtures</font>](https://dormousehole.readthedocs.io/en/latest/testing.html#fixtures)
    - [<font style="color:rgb(62, 67, 73);">用测试客户端发送请求</font>](https://dormousehole.readthedocs.io/en/latest/testing.html#id2)
    - [<font style="color:rgb(62, 67, 73);">追随重定向</font>](https://dormousehole.readthedocs.io/en/latest/testing.html#id4)
    - [<font style="color:rgb(62, 67, 73);">访问和修改会话</font>](https://dormousehole.readthedocs.io/en/latest/testing.html#id5)
    - [<font style="color:rgb(62, 67, 73);">使用 CLI 运行器运行命令</font>](https://dormousehole.readthedocs.io/en/latest/testing.html#cli)
    - [<font style="color:rgb(62, 67, 73);">依赖于活动状态情境的测试</font>](https://dormousehole.readthedocs.io/en/latest/testing.html#id6)
+ [<font style="color:rgb(62, 67, 73);">应用错误处理</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html)
    - [<font style="color:rgb(62, 67, 73);">错误日志工具</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html#error-logging-tools)
    - [<font style="color:rgb(62, 67, 73);">错误处理器</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html#id4)
    - [<font style="color:rgb(62, 67, 73);">自定义错误页面</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html#id9)
    - [<font style="color:rgb(62, 67, 73);">蓝印错误处理器</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html#id11)
    - [<font style="color:rgb(62, 67, 73);">将 API 错误作为 JSON 返回</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html#api-json)
    - [<font style="color:rgb(62, 67, 73);">日志</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html#id12)
    - [<font style="color:rgb(62, 67, 73);">调试</font>](https://dormousehole.readthedocs.io/en/latest/errorhandling.html#id13)
+ [<font style="color:rgb(62, 67, 73);">调试应用程序错误</font>](https://dormousehole.readthedocs.io/en/latest/debugging.html)
    - [<font style="color:rgb(62, 67, 73);">在生产环境中</font>](https://dormousehole.readthedocs.io/en/latest/debugging.html#id2)
    - [<font style="color:rgb(62, 67, 73);">内置调试器</font>](https://dormousehole.readthedocs.io/en/latest/debugging.html#id3)
    - [<font style="color:rgb(62, 67, 73);">外部调试器</font>](https://dormousehole.readthedocs.io/en/latest/debugging.html#id4)
+ [<font style="color:rgb(62, 67, 73);">日志</font>](https://dormousehole.readthedocs.io/en/latest/logging.html)
    - [<font style="color:rgb(62, 67, 73);">基本配置</font>](https://dormousehole.readthedocs.io/en/latest/logging.html#id2)
    - [<font style="color:rgb(62, 67, 73);">把出错信息通过电子邮件发送给管理者</font>](https://dormousehole.readthedocs.io/en/latest/logging.html#id5)
    - [<font style="color:rgb(62, 67, 73);">注入请求信息</font>](https://dormousehole.readthedocs.io/en/latest/logging.html#id6)
    - [<font style="color:rgb(62, 67, 73);">其他库</font>](https://dormousehole.readthedocs.io/en/latest/logging.html#id7)
+ [<font style="color:rgb(62, 67, 73);">配置管理</font>](https://dormousehole.readthedocs.io/en/latest/config.html)
    - [<font style="color:rgb(62, 67, 73);">配置入门</font>](https://dormousehole.readthedocs.io/en/latest/config.html#id2)
    - [<font style="color:rgb(62, 67, 73);">调试模式</font>](https://dormousehole.readthedocs.io/en/latest/config.html#id3)
    - [<font style="color:rgb(62, 67, 73);">内置配置变量</font>](https://dormousehole.readthedocs.io/en/latest/config.html#id4)
    - [<font style="color:rgb(62, 67, 73);">使用 Python 配置文件</font>](https://dormousehole.readthedocs.io/en/latest/config.html#python)
    - [<font style="color:rgb(62, 67, 73);">使用数据文件来配置</font>](https://dormousehole.readthedocs.io/en/latest/config.html#id5)
    - [<font style="color:rgb(62, 67, 73);">使用环境变量来配置</font>](https://dormousehole.readthedocs.io/en/latest/config.html#id6)
    - [<font style="color:rgb(62, 67, 73);">配置的最佳实践</font>](https://dormousehole.readthedocs.io/en/latest/config.html#id7)
    - [<font style="color:rgb(62, 67, 73);">开发/生产</font>](https://dormousehole.readthedocs.io/en/latest/config.html#config-dev-prod)
    - [<font style="color:rgb(62, 67, 73);">实例文件夹</font>](https://dormousehole.readthedocs.io/en/latest/config.html#instance-folders)
+ [<font style="color:rgb(62, 67, 73);">信号</font>](https://dormousehole.readthedocs.io/en/latest/signals.html)
    - [<font style="color:rgb(62, 67, 73);">核心信号</font>](https://dormousehole.readthedocs.io/en/latest/signals.html#id2)
    - [<font style="color:rgb(62, 67, 73);">订阅信号</font>](https://dormousehole.readthedocs.io/en/latest/signals.html#id3)
    - [<font style="color:rgb(62, 67, 73);">创建信号</font>](https://dormousehole.readthedocs.io/en/latest/signals.html#id4)
    - [<font style="color:rgb(62, 67, 73);">发送信号</font>](https://dormousehole.readthedocs.io/en/latest/signals.html#signals-sending)
    - [<font style="color:rgb(62, 67, 73);">信号与 Flask 的请求环境</font>](https://dormousehole.readthedocs.io/en/latest/signals.html#flask)
    - [<font style="color:rgb(62, 67, 73);">信号订阅装饰器</font>](https://dormousehole.readthedocs.io/en/latest/signals.html#id6)
+ [<font style="color:rgb(62, 67, 73);">基于类的视图</font>](https://dormousehole.readthedocs.io/en/latest/views.html)
    - [<font style="color:rgb(62, 67, 73);">基本可重用视图</font>](https://dormousehole.readthedocs.io/en/latest/views.html#id2)
    - [<font style="color:rgb(62, 67, 73);">URL变量</font>](https://dormousehole.readthedocs.io/en/latest/views.html#url)
    - [<font style="color:rgb(62, 67, 73);">视图的生命周期和self</font>](https://dormousehole.readthedocs.io/en/latest/views.html#self)
    - [<font style="color:rgb(62, 67, 73);">视图装饰器</font>](https://dormousehole.readthedocs.io/en/latest/views.html#id3)
    - [<font style="color:rgb(62, 67, 73);">方法提示</font>](https://dormousehole.readthedocs.io/en/latest/views.html#id4)
    - [<font style="color:rgb(62, 67, 73);">方法调度和 API</font>](https://dormousehole.readthedocs.io/en/latest/views.html#api)
+ [<font style="color:rgb(62, 67, 73);">应用程序结构和生命周期</font>](https://dormousehole.readthedocs.io/en/latest/lifecycle.html)
    - [<font style="color:rgb(62, 67, 73);">应用程序设置</font>](https://dormousehole.readthedocs.io/en/latest/lifecycle.html#id2)
    - [<font style="color:rgb(62, 67, 73);">为应用程序提供服务</font>](https://dormousehole.readthedocs.io/en/latest/lifecycle.html#id3)
    - [<font style="color:rgb(62, 67, 73);">如何处理请求</font>](https://dormousehole.readthedocs.io/en/latest/lifecycle.html#id5)
+ [<font style="color:rgb(62, 67, 73);">应用情境</font>](https://dormousehole.readthedocs.io/en/latest/appcontext.html)
    - [<font style="color:rgb(62, 67, 73);">情境的目的</font>](https://dormousehole.readthedocs.io/en/latest/appcontext.html#id2)
    - [<font style="color:rgb(62, 67, 73);">情境的生命周期</font>](https://dormousehole.readthedocs.io/en/latest/appcontext.html#id3)
    - [<font style="color:rgb(62, 67, 73);">手动推送情境</font>](https://dormousehole.readthedocs.io/en/latest/appcontext.html#id4)
    - [<font style="color:rgb(62, 67, 73);">存储数据</font>](https://dormousehole.readthedocs.io/en/latest/appcontext.html#id5)
    - [<font style="color:rgb(62, 67, 73);">事件和信号</font>](https://dormousehole.readthedocs.io/en/latest/appcontext.html#id6)
+ [<font style="color:rgb(62, 67, 73);">请求情境</font>](https://dormousehole.readthedocs.io/en/latest/reqcontext.html)
    - [<font style="color:rgb(62, 67, 73);">情境的用途</font>](https://dormousehole.readthedocs.io/en/latest/reqcontext.html#id2)
    - [<font style="color:rgb(62, 67, 73);">情境的生命周期</font>](https://dormousehole.readthedocs.io/en/latest/reqcontext.html#id3)
    - [<font style="color:rgb(62, 67, 73);">手动推送情境</font>](https://dormousehole.readthedocs.io/en/latest/reqcontext.html#id4)
    - [<font style="color:rgb(62, 67, 73);">情境如何工作</font>](https://dormousehole.readthedocs.io/en/latest/reqcontext.html#id5)
    - [<font style="color:rgb(62, 67, 73);">回调和错误</font>](https://dormousehole.readthedocs.io/en/latest/reqcontext.html#callbacks-and-errors)
    - [<font style="color:rgb(62, 67, 73);">关于代理的说明</font>](https://dormousehole.readthedocs.io/en/latest/reqcontext.html#notes-on-proxies)
+ [<font style="color:rgb(62, 67, 73);">使用蓝图进行应用模块化</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html)
    - [<font style="color:rgb(62, 67, 73);">为什么使用蓝图？</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#id2)
    - [<font style="color:rgb(62, 67, 73);">蓝图的概念</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#id3)
    - [<font style="color:rgb(62, 67, 73);">第一个蓝图</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#id4)
    - [<font style="color:rgb(62, 67, 73);">注册蓝图</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#id5)
    - [<font style="color:rgb(62, 67, 73);">嵌套蓝图</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#id6)
    - [<font style="color:rgb(62, 67, 73);">蓝图资源</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#id7)
    - [<font style="color:rgb(62, 67, 73);">创建 URL</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#url)
    - [<font style="color:rgb(62, 67, 73);">蓝图出错处理器</font>](https://dormousehole.readthedocs.io/en/latest/blueprints.html#id11)
+ [<font style="color:rgb(62, 67, 73);">扩展</font>](https://dormousehole.readthedocs.io/en/latest/extensions.html)
    - [<font style="color:rgb(62, 67, 73);">寻找扩展</font>](https://dormousehole.readthedocs.io/en/latest/extensions.html#id2)
    - [<font style="color:rgb(62, 67, 73);">使用扩展</font>](https://dormousehole.readthedocs.io/en/latest/extensions.html#id3)
    - [<font style="color:rgb(62, 67, 73);">创建扩展</font>](https://dormousehole.readthedocs.io/en/latest/extensions.html#id4)
+ [<font style="color:rgb(62, 67, 73);">命令行接口</font>](https://dormousehole.readthedocs.io/en/latest/cli.html)
    - [<font style="color:rgb(62, 67, 73);">探索应用</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#id2)
    - [<font style="color:rgb(62, 67, 73);">运行开发服务器</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#id3)
    - [<font style="color:rgb(62, 67, 73);">打开一个 Shell</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#shell)
    - [<font style="color:rgb(62, 67, 73);">通过 dotenv 设置环境变量</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#dotenv)
    - [<font style="color:rgb(62, 67, 73);">通过 virturalenv 设置环境变量</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#virturalenv)
    - [<font style="color:rgb(62, 67, 73);">自定义命令</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#id9)
    - [<font style="color:rgb(62, 67, 73);">插件</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#id12)
    - [<font style="color:rgb(62, 67, 73);">自定义脚本</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#custom-scripts)
    - [<font style="color:rgb(62, 67, 73);">PyCharm 集成</font>](https://dormousehole.readthedocs.io/en/latest/cli.html#pycharm)
+ [<font style="color:rgb(62, 67, 73);">开发服务器</font>](https://dormousehole.readthedocs.io/en/latest/server.html)
    - [<font style="color:rgb(62, 67, 73);">通过命令行使用开发服务器</font>](https://dormousehole.readthedocs.io/en/latest/server.html#id2)
    - [<font style="color:rgb(62, 67, 73);">通过代码使用开发服务器</font>](https://dormousehole.readthedocs.io/en/latest/server.html#id5)
+ [<font style="color:rgb(62, 67, 73);">在 Shell 中使用 Flask</font>](https://dormousehole.readthedocs.io/en/latest/shell.html)
    - [<font style="color:rgb(62, 67, 73);">命令行接口</font>](https://dormousehole.readthedocs.io/en/latest/shell.html#id1)
    - [<font style="color:rgb(62, 67, 73);">创建一个请求情境</font>](https://dormousehole.readthedocs.io/en/latest/shell.html#id2)
    - [<font style="color:rgb(62, 67, 73);">发送请求前/后动作</font>](https://dormousehole.readthedocs.io/en/latest/shell.html#id3)
    - [<font style="color:rgb(62, 67, 73);">在 Shell 中玩得更爽</font>](https://dormousehole.readthedocs.io/en/latest/shell.html#shell)
+ [<font style="color:rgb(62, 67, 73);">Flask 方案</font>](https://dormousehole.readthedocs.io/en/latest/patterns/index.html)
    - [<font style="color:rgb(62, 67, 73);">大型应用作为一个包</font>](https://dormousehole.readthedocs.io/en/latest/patterns/packages.html)
    - [<font style="color:rgb(62, 67, 73);">应用工厂</font>](https://dormousehole.readthedocs.io/en/latest/patterns/appfactories.html)
    - [<font style="color:rgb(62, 67, 73);">应用调度</font>](https://dormousehole.readthedocs.io/en/latest/patterns/appdispatch.html)
    - [<font style="color:rgb(62, 67, 73);">URL 处理器</font>](https://dormousehole.readthedocs.io/en/latest/patterns/urlprocessors.html)
    - [<font style="color:rgb(62, 67, 73);">使用 SQLite 3</font>](https://dormousehole.readthedocs.io/en/latest/patterns/sqlite3.html)
    - [<font style="color:rgb(62, 67, 73);">使用 SQLAlchemy</font>](https://dormousehole.readthedocs.io/en/latest/patterns/sqlalchemy.html)
    - [<font style="color:rgb(62, 67, 73);">上传文件</font>](https://dormousehole.readthedocs.io/en/latest/patterns/fileuploads.html)
    - [<font style="color:rgb(62, 67, 73);">缓存</font>](https://dormousehole.readthedocs.io/en/latest/patterns/caching.html)
    - [<font style="color:rgb(62, 67, 73);">视图装饰器</font>](https://dormousehole.readthedocs.io/en/latest/patterns/viewdecorators.html)
    - [<font style="color:rgb(62, 67, 73);">使用 WTForms 进行表单验证</font>](https://dormousehole.readthedocs.io/en/latest/patterns/wtforms.html)
    - [<font style="color:rgb(62, 67, 73);">模板继承</font>](https://dormousehole.readthedocs.io/en/latest/patterns/templateinheritance.html)
    - [<font style="color:rgb(62, 67, 73);">消息闪现</font>](https://dormousehole.readthedocs.io/en/latest/patterns/flashing.html)
    - [<font style="color:rgb(62, 67, 73);">JavaScript 、fetch和 JSON</font>](https://dormousehole.readthedocs.io/en/latest/patterns/javascript.html)
    - [<font style="color:rgb(62, 67, 73);">惰性载入视图</font>](https://dormousehole.readthedocs.io/en/latest/patterns/lazyloading.html)
    - [<font style="color:rgb(62, 67, 73);">通过 MongoEngine 使用 MongoDB</font>](https://dormousehole.readthedocs.io/en/latest/patterns/mongoengine.html)
    - [<font style="color:rgb(62, 67, 73);">添加一个页面图标</font>](https://dormousehole.readthedocs.io/en/latest/patterns/favicon.html)
    - [<font style="color:rgb(62, 67, 73);">流内容</font>](https://dormousehole.readthedocs.io/en/latest/patterns/streaming.html)
    - [<font style="color:rgb(62, 67, 73);">延迟的请求回调</font>](https://dormousehole.readthedocs.io/en/latest/patterns/deferredcallbacks.html)
    - [<font style="color:rgb(62, 67, 73);">添加 HTTP 方法重载</font>](https://dormousehole.readthedocs.io/en/latest/patterns/methodoverrides.html)
    - [<font style="color:rgb(62, 67, 73);">请求内容校验</font>](https://dormousehole.readthedocs.io/en/latest/patterns/requestchecksum.html)
    - [<font style="color:rgb(62, 67, 73);">使用 Celery 的后台任务</font>](https://dormousehole.readthedocs.io/en/latest/patterns/celery.html)
    - [<font style="color:rgb(62, 67, 73);">继承 Flask</font>](https://dormousehole.readthedocs.io/en/latest/patterns/subclassing.html)
    - [<font style="color:rgb(62, 67, 73);">单页应用</font>](https://dormousehole.readthedocs.io/en/latest/patterns/singlepageapplications.html)
+ [<font style="color:rgb(62, 67, 73);">安全注意事项</font>](https://dormousehole.readthedocs.io/en/latest/security.html)
    - [<font style="color:rgb(62, 67, 73);">跨站脚本攻击（ XSS ）</font>](https://dormousehole.readthedocs.io/en/latest/security.html#xss)
    - [<font style="color:rgb(62, 67, 73);">跨站请求伪造（ CSRF ）</font>](https://dormousehole.readthedocs.io/en/latest/security.html#csrf)
    - [<font style="color:rgb(62, 67, 73);">JSON 安全</font>](https://dormousehole.readthedocs.io/en/latest/security.html#json)
    - [<font style="color:rgb(62, 67, 73);">安全头部</font>](https://dormousehole.readthedocs.io/en/latest/security.html#id4)
    - [<font style="color:rgb(62, 67, 73);">复制/粘贴到终端</font>](https://dormousehole.readthedocs.io/en/latest/security.html#id5)
+ [<font style="color:rgb(62, 67, 73);">生产部署</font>](https://dormousehole.readthedocs.io/en/latest/deploying/index.html)
    - [<font style="color:rgb(62, 67, 73);">自主部署选项</font>](https://dormousehole.readthedocs.io/en/latest/deploying/index.html#id2)
    - [<font style="color:rgb(62, 67, 73);">托管平台</font>](https://dormousehole.readthedocs.io/en/latest/deploying/index.html#id3)
+ [<font style="color:rgb(62, 67, 73);">使用async和await</font>](https://dormousehole.readthedocs.io/en/latest/async-await.html)
    - [<font style="color:rgb(62, 67, 73);">性能</font>](https://dormousehole.readthedocs.io/en/latest/async-await.html#id2)
    - [<font style="color:rgb(62, 67, 73);">后台任务</font>](https://dormousehole.readthedocs.io/en/latest/async-await.html#id3)
    - [<font style="color:rgb(62, 67, 73);">何时使用 Quart 代替</font>](https://dormousehole.readthedocs.io/en/latest/async-await.html#quart)
    - [<font style="color:rgb(62, 67, 73);">扩展</font>](https://dormousehole.readthedocs.io/en/latest/async-await.html#id5)
    - [<font style="color:rgb(62, 67, 73);">其他事件循环</font>](https://dormousehole.readthedocs.io/en/latest/async-await.html#id6)

## <font style="color:black;">API 参考</font>
<font style="color:rgb(62, 67, 73);">这部分文档详细说明某个函数、类或方法。</font>

+ [<font style="color:rgb(62, 67, 73);">API</font>](https://dormousehole.readthedocs.io/en/latest/api.html)
    - [<font style="color:rgb(62, 67, 73);">Application Object</font>](https://dormousehole.readthedocs.io/en/latest/api.html#application-object)
    - [<font style="color:rgb(62, 67, 73);">Blueprint Objects</font>](https://dormousehole.readthedocs.io/en/latest/api.html#blueprint-objects)
    - [<font style="color:rgb(62, 67, 73);">Incoming Request Data</font>](https://dormousehole.readthedocs.io/en/latest/api.html#incoming-request-data)
    - [<font style="color:rgb(62, 67, 73);">Response Objects</font>](https://dormousehole.readthedocs.io/en/latest/api.html#response-objects)
    - [<font style="color:rgb(62, 67, 73);">Sessions</font>](https://dormousehole.readthedocs.io/en/latest/api.html#sessions)
    - [<font style="color:rgb(62, 67, 73);">Session Interface</font>](https://dormousehole.readthedocs.io/en/latest/api.html#session-interface)
    - [<font style="color:rgb(62, 67, 73);">Test Client</font>](https://dormousehole.readthedocs.io/en/latest/api.html#test-client)
    - [<font style="color:rgb(62, 67, 73);">Test CLI Runner</font>](https://dormousehole.readthedocs.io/en/latest/api.html#test-cli-runner)
    - [<font style="color:rgb(62, 67, 73);">Application Globals</font>](https://dormousehole.readthedocs.io/en/latest/api.html#application-globals)
    - [<font style="color:rgb(62, 67, 73);">Useful Functions and Classes</font>](https://dormousehole.readthedocs.io/en/latest/api.html#useful-functions-and-classes)
    - [<font style="color:rgb(62, 67, 73);">Message Flashing</font>](https://dormousehole.readthedocs.io/en/latest/api.html#message-flashing)
    - [<font style="color:rgb(62, 67, 73);">JSON Support</font>](https://dormousehole.readthedocs.io/en/latest/api.html#module-flask.json)
    - [<font style="color:rgb(62, 67, 73);">Template Rendering</font>](https://dormousehole.readthedocs.io/en/latest/api.html#template-rendering)
    - [<font style="color:rgb(62, 67, 73);">Configuration</font>](https://dormousehole.readthedocs.io/en/latest/api.html#configuration)
    - [<font style="color:rgb(62, 67, 73);">Stream Helpers</font>](https://dormousehole.readthedocs.io/en/latest/api.html#stream-helpers)
    - [<font style="color:rgb(62, 67, 73);">Useful Internals</font>](https://dormousehole.readthedocs.io/en/latest/api.html#useful-internals)
    - [<font style="color:rgb(62, 67, 73);">Signals</font>](https://dormousehole.readthedocs.io/en/latest/api.html#signals)
    - [<font style="color:rgb(62, 67, 73);">Class-Based Views</font>](https://dormousehole.readthedocs.io/en/latest/api.html#class-based-views)
    - [<font style="color:rgb(62, 67, 73);">URL Route Registrations</font>](https://dormousehole.readthedocs.io/en/latest/api.html#url-route-registrations)
    - [<font style="color:rgb(62, 67, 73);">View Function Options</font>](https://dormousehole.readthedocs.io/en/latest/api.html#view-function-options)
    - [<font style="color:rgb(62, 67, 73);">Command Line Interface</font>](https://dormousehole.readthedocs.io/en/latest/api.html#command-line-interface)

## <font style="color:black;">其他材料</font>
+ [<font style="color:rgb(62, 67, 73);">Flask 的设计思路</font>](https://dormousehole.readthedocs.io/en/latest/design.html)
    - [<font style="color:rgb(62, 67, 73);">显式的应用对象</font>](https://dormousehole.readthedocs.io/en/latest/design.html#id1)
    - [<font style="color:rgb(62, 67, 73);">路由系统</font>](https://dormousehole.readthedocs.io/en/latest/design.html#id2)
    - [<font style="color:rgb(62, 67, 73);">唯一模板引擎</font>](https://dormousehole.readthedocs.io/en/latest/design.html#id3)
    - [<font style="color:rgb(62, 67, 73);">“微”的含义</font>](https://dormousehole.readthedocs.io/en/latest/design.html#id4)
    - [<font style="color:rgb(62, 67, 73);">线程本地对象</font>](https://dormousehole.readthedocs.io/en/latest/design.html#id5)
    - [<font style="color:rgb(62, 67, 73);">Async/await 和 ASGI 支持</font>](https://dormousehole.readthedocs.io/en/latest/design.html#async-await-asgi)
    - [<font style="color:rgb(62, 67, 73);">Flask 是什么，不是什么</font>](https://dormousehole.readthedocs.io/en/latest/design.html#id6)
+ [<font style="color:rgb(62, 67, 73);">Flask 扩展开发</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html)
    - [<font style="color:rgb(62, 67, 73);">命名</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#id1)
    - [<font style="color:rgb(62, 67, 73);">扩展类和初始化</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#id2)
    - [<font style="color:rgb(62, 67, 73);">添加行为</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#id3)
    - [<font style="color:rgb(62, 67, 73);">配置技术</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#id4)
    - [<font style="color:rgb(62, 67, 73);">请求期间的数据</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#id5)
    - [<font style="color:rgb(62, 67, 73);">视图和模型</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#id6)
    - [<font style="color:rgb(62, 67, 73);">推荐的扩展指南</font>](https://dormousehole.readthedocs.io/en/latest/extensiondev.html#id7)
+ [<font style="color:rgb(62, 67, 73);">如何为 Flask 做出贡献</font>](https://dormousehole.readthedocs.io/en/latest/contributing.html)
    - [<font style="color:rgb(62, 67, 73);">问答支持</font>](https://dormousehole.readthedocs.io/en/latest/contributing.html#id1)
    - [<font style="color:rgb(62, 67, 73);">报告问题</font>](https://dormousehole.readthedocs.io/en/latest/contributing.html#id2)
    - [<font style="color:rgb(62, 67, 73);">提交补丁</font>](https://dormousehole.readthedocs.io/en/latest/contributing.html#id4)
+ [<font style="color:rgb(62, 67, 73);">BSD-3-Clause 许可证</font>](https://dormousehole.readthedocs.io/en/latest/license.html)
+ [<font style="color:rgb(62, 67, 73);">更新日志</font>](https://dormousehole.readthedocs.io/en/latest/changes.html)
    - [<font style="color:rgb(62, 67, 73);">Version 3.0.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-3-0-2)
    - [<font style="color:rgb(62, 67, 73);">Version 3.0.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-3-0-1)
    - [<font style="color:rgb(62, 67, 73);">Version 3.0.0</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-3-0-0)
    - [<font style="color:rgb(62, 67, 73);">Version 2.3.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-3-3)
    - [<font style="color:rgb(62, 67, 73);">Version 2.3.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-3-2)
    - [<font style="color:rgb(62, 67, 73);">Version 2.3.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-3-1)
    - [<font style="color:rgb(62, 67, 73);">Version 2.3.0</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-3-0)
    - [<font style="color:rgb(62, 67, 73);">Version 2.2.5</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-2-5)
    - [<font style="color:rgb(62, 67, 73);">Version 2.2.4</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-2-4)
    - [<font style="color:rgb(62, 67, 73);">Version 2.2.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-2-3)
    - [<font style="color:rgb(62, 67, 73);">Version 2.2.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-2-2)
    - [<font style="color:rgb(62, 67, 73);">Version 2.2.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-2-1)
    - [<font style="color:rgb(62, 67, 73);">Version 2.2.0</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-2-0)
    - [<font style="color:rgb(62, 67, 73);">Version 2.1.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-1-3)
    - [<font style="color:rgb(62, 67, 73);">Version 2.1.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-1-2)
    - [<font style="color:rgb(62, 67, 73);">Version 2.1.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-1-1)
    - [<font style="color:rgb(62, 67, 73);">Version 2.1.0</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-1-0)
    - [<font style="color:rgb(62, 67, 73);">Version 2.0.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-0-3)
    - [<font style="color:rgb(62, 67, 73);">Version 2.0.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-0-2)
    - [<font style="color:rgb(62, 67, 73);">Version 2.0.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-0-1)
    - [<font style="color:rgb(62, 67, 73);">Version 2.0.0</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-2-0-0)
    - [<font style="color:rgb(62, 67, 73);">Version 1.1.4</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-1-4)
    - [<font style="color:rgb(62, 67, 73);">Version 1.1.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-1-3)
    - [<font style="color:rgb(62, 67, 73);">Version 1.1.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-1-2)
    - [<font style="color:rgb(62, 67, 73);">Version 1.1.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-1-1)
    - [<font style="color:rgb(62, 67, 73);">Version 1.1.0</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-1-0)
    - [<font style="color:rgb(62, 67, 73);">Version 1.0.4</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-0-4)
    - [<font style="color:rgb(62, 67, 73);">Version 1.0.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-0-3)
    - [<font style="color:rgb(62, 67, 73);">Version 1.0.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-0-2)
    - [<font style="color:rgb(62, 67, 73);">Version 1.0.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-0-1)
    - [<font style="color:rgb(62, 67, 73);">Version 1.0</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-1-0)
    - [<font style="color:rgb(62, 67, 73);">Version 0.12.5</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-12-5)
    - [<font style="color:rgb(62, 67, 73);">Version 0.12.4</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-12-4)
    - [<font style="color:rgb(62, 67, 73);">Version 0.12.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-12-3)
    - [<font style="color:rgb(62, 67, 73);">Version 0.12.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-12-2)
    - [<font style="color:rgb(62, 67, 73);">Version 0.12.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-12-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.12</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-12)
    - [<font style="color:rgb(62, 67, 73);">Version 0.11.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-11-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.11</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-11)
    - [<font style="color:rgb(62, 67, 73);">Version 0.10.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-10-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.10</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-10)
    - [<font style="color:rgb(62, 67, 73);">Version 0.9</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-9)
    - [<font style="color:rgb(62, 67, 73);">Version 0.8.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-8-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.8</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-8)
    - [<font style="color:rgb(62, 67, 73);">Version 0.7.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-7-2)
    - [<font style="color:rgb(62, 67, 73);">Version 0.7.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-7-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.7</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-7)
    - [<font style="color:rgb(62, 67, 73);">Version 0.6.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-6-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.6</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-6)
    - [<font style="color:rgb(62, 67, 73);">Version 0.5.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-5-2)
    - [<font style="color:rgb(62, 67, 73);">Version 0.5.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-5-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.5</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-5)
    - [<font style="color:rgb(62, 67, 73);">Version 0.4</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-4)
    - [<font style="color:rgb(62, 67, 73);">Version 0.3.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-3-1)
    - [<font style="color:rgb(62, 67, 73);">Version 0.3</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-3)
    - [<font style="color:rgb(62, 67, 73);">Version 0.2</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-2)
    - [<font style="color:rgb(62, 67, 73);">Version 0.1</font>](https://dormousehole.readthedocs.io/en/latest/changes.html#version-0-1)

