## <font style="color:rgb(31, 35, 40);">概念描述</font>
<font style="color:rgb(31, 35, 40);">Flet 是一个框架，让您能够使用自己喜欢的语言轻松构建实时 Web、移动和桌面应用程序，并安全地与您的团队共享。无需任何前端经验。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">几分钟内从创意到应用</font>
<font style="color:rgb(31, 35, 40);">作为您团队的内部工具或仪表板、周末项目、数据输入表单、信息亭应用程序或高保真原型 - Flet 是一个理想的框架，可以快速破解外观精美的交互式应用程序以服务于一组用户。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);"> 简单的架构</font>
<font style="color:rgb(31, 35, 40);">不再需要具有 JavaScript 前端、REST API 后端、数据库、缓存等的复杂架构。使用 Flet，您只需用 Python 编写一个整体状态应用程序，即可获得多用户、实时的单页应用程序 (SPA)。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);">含电池</font>
<font style="color:rgb(31, 35, 40);">要使用 Flet 进行开发，您只需要一个您喜欢的 IDE 或文本编辑器。无需 SDK、无需成千上万的依赖项、无需复杂的工具 - Flet 内置了 Web 服务器，包含资源托管和桌面客户端。</font>

### <font style="color:rgb(31, 35, 40);">由 Flutter 提供支持</font>
<font style="color:rgb(31, 35, 40);">Flet UI 基于</font><font style="color:rgb(31, 35, 40);"> </font>[Flutter](https://flutter.dev/)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">构建，因此您的应用外观专业，并且可以交付到任何平台。Flet 通过使用命令式编程模型，将较小的“Widget”与即用型“控件”相结合，简化了 Flutter 模型。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);"> 讲你的语言</font>
<font style="color:rgb(31, 35, 40);">Flet 与语言无关，因此团队中的任何人都可以使用自己喜欢的语言开发 Flet 应用。目前已支持</font><font style="color:rgb(31, 35, 40);"> </font>[Python](https://flet.dev/docs/guides/python/getting-started)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">，Go、C# 和其他语言</font>[即将推出](https://flet.dev/roadmap)<font style="color:rgb(31, 35, 40);">。</font>

### <font style="color:rgb(31, 35, 40);"></font><font style="color:rgb(31, 35, 40);"> 递送至任何设备</font>
<font style="color:rgb(31, 35, 40);">将 Flet 应用部署为 Web 应用并在浏览器中查看。将其打包为适用于 Windows、macOS 和 Linux 的独立桌面应用。将其作为</font><font style="color:rgb(31, 35, 40);"> </font>[PWA](https://web.dev/what-are-pwas/)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">安装到移动设备上，或通过适用于 iOS 和 Android 的 Flet 应用查看。</font>

## <font style="color:rgb(31, 35, 40);">Flet 应用程序示例</font>
<font style="color:rgb(31, 35, 40);">目前，您可以使用 Python 编写 Flet 应用程序，并且很快将添加其他语言。</font>

<font style="color:rgb(31, 35, 40);">这是一个示例“计数器”应用程序：</font>

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.alignment.center,
        )
    )

ft.app(main)
```

<font style="color:rgb(31, 35, 40);">要运行应用程序安装</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">flet</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">模块：</font>

```python
pip install flet
```

<font style="color:rgb(31, 35, 40);">并运行程序：</font>

```python
python counter.py
```

<font style="color:rgb(31, 35, 40);">该应用程序将在本机操作系统窗口中启动 - 这是 Electron 的一个不错的替代品！</font>

<font style="color:rgb(31, 35, 40);">现在，如果您想将该应用程序作为 Web 应用程序运行，只需将最后一行替换为：</font>

```python
flet.app(target=main, view=flet.AppView.WEB_BROWSER)
```

<font style="color:rgb(31, 35, 40);">再次运行，现在您立即获得一个 Web 应用程序：</font>

## <font style="color:rgb(31, 35, 40);">入门</font>
+ [使用 Python 创建 Flet 应用程序](https://flet.dev/docs/guides/python/getting-started)
+ [控件参考](https://flet.dev/docs/controls)

## <font style="color:rgb(31, 35, 40);">Python 中的示例应用程序</font>
+ [迎宾员](https://github.com/flet-dev/examples/blob/main/python/apps/greeter/greeter.py)<font style="color:rgb(31, 35, 40);">（</font>[在线演示](https://gallery.flet.dev/greeter/)<font style="color:rgb(31, 35, 40);">）</font>
+ [计数器](https://github.com/flet-dev/examples/blob/main/python/apps/counter/counter.py)<font style="color:rgb(31, 35, 40);">（</font>[在线演示](https://gallery.flet.dev/counter/)<font style="color:rgb(31, 35, 40);">）</font>
+ [待办事项](https://github.com/flet-dev/examples/blob/main/python/apps/todo/todo.py)<font style="color:rgb(31, 35, 40);">（</font>[在线演示](https://gallery.flet.dev/todo/)<font style="color:rgb(31, 35, 40);">）</font>
+ [图标浏览器](https://github.com/flet-dev/examples/blob/main/python/apps/icons-browser/main.py)<font style="color:rgb(31, 35, 40);">（</font>[在线演示](https://gallery.flet.dev/icons-browser/)<font style="color:rgb(31, 35, 40);">）</font>

<font style="color:rgb(31, 35, 40);">更多演示应用程序可以在</font>[图库](https://flet.dev/gallery/)<font style="color:rgb(31, 35, 40);">中找到。</font>

## 资源
[https://github.com/flet-dev/awesome-flet](https://github.com/flet-dev/awesome-flet)

