### <font style="color:rgb(51, 51, 51);">介绍</font>
<font style="color:rgb(51, 51, 51);">Playwright 是一个用于自动化浏览器操作的开源工具，由 Microsoft 开发和维护。它支持多种浏览器（包括 Chromium、Firefox 和 WebKit）和多种编程语言（如 Python、JavaScript 和 C#），可以用于测试、爬虫、自动化任务等场景。 </font>

**<font style="color:rgb(51, 51, 51);">与 Selenium 和 pyppeteer 相比，Playwright 具有以下几个区别和优势：</font>**

1. <font style="color:rgb(51, 51, 51);">多浏览器支持：支持所有主流浏览器。这使得开发人员可以根据需求选择最适合的浏览器进行自动化操作。（Playwright不支持旧版Microsoft Edge或IE11）</font>
2. <font style="color:rgb(51, 51, 51);">更快的执行速度：Playwright 通过使用浏览器的底层调试协议来进行操作，相比于 Selenium 和 pyppeteer，它具有更快的执行速度和更低的资源消耗。</font>
3. <font style="color:rgb(51, 51, 51);">可靠性和稳定性：Playwright 提供了更可靠和稳定的浏览器自动化操作，通过使用浏览器的原生 API 来模拟用户行为，避免了一些传统自动化工具的一些限制和不稳定性。</font>
4. <font style="color:rgb(51, 51, 51);">支持跨浏览器和跨平台：Playwright 可以在不同浏览器和不同操作系统上运行，这使得开发人员可以更方便地进行跨浏览器和跨平台的测试和自动化操作。</font>
5. <font style="color:rgb(51, 51, 51);">支持屏幕录制功能：根据屏幕录制指定生成相关操作代码。</font>

**<font style="color:rgb(51, 51, 51);">在爬虫中使用 Playwright 的好处包括：</font>**

1. <font style="color:rgb(51, 51, 51);">动态网页爬取：Playwright 可以模拟用户在浏览器中的操作，包括渲染 JavaScript、点击按钮、填写表单等，从而可以爬取包含动态内容的网页。</font>
2. <font style="color:rgb(51, 51, 51);">多浏览器支持：Playwright 支持多种浏览器，可以根据需求选择最适合的浏览器进行爬取，以确保爬取结果的准确性和一致性。</font>
3. <font style="color:rgb(51, 51, 51);">更高的稳定性和可靠性：Playwright 使用浏览器的原生 API 进行操作，避免了一些传统爬虫工具的一些限制和不稳定性，提供了更可靠和稳定的爬取能力。</font>

<font style="color:rgb(51, 51, 51);">总之，Playwright 是一个功能强大、跨浏览器、跨平台的浏览器自动化工具，相比于 Selenium 和 pyppeteer，它具有更快的执行速度、更高的稳定性和更广泛的浏览器支持，适用于多种自动化操作和爬虫场景。</font>

**<font style="color:rgb(51, 51, 51);">python版本的Playwright官网文档：</font>**[<font style="color:rgb(51, 51, 51);">https://playwright.dev/python/docs/intro</font>](https://playwright.dev/python/docs/intro)

### <font style="color:rgb(51, 51, 51);">环境安装</font>
+ <font style="color:rgb(51, 51, 51);">系统要求：</font>
    - <font style="color:rgb(51, 51, 51);">Python 3.8 或更高版本。</font>
    - <font style="color:rgb(51, 51, 51);">Windows 10+、Windows Server 2016+ 或适用于 Linux 的 Windows 子系统 （WSL）。</font>
    - <font style="color:rgb(51, 51, 51);">MacOS 12 Monterey 或 MacOS 13 Ventura。</font>
    - <font style="color:rgb(51, 51, 51);">Debian 11、Debian 12、Ubuntu 20.04 或 Ubuntu 22.04。</font>
+ <font style="color:rgb(51, 51, 51);">安装playwright的python版本</font>
    - <font style="color:rgb(51, 51, 51);">pip install playwright</font>
+ <font style="color:rgb(51, 51, 51);">安装Playwright所需的所有工具插件和所支持的浏览器</font>
    - <font style="color:rgb(51, 51, 51);">playwright install</font>
    - <font style="color:rgb(51, 51, 51);">该步骤耗时较长</font>

#### <font style="color:rgb(51, 51, 51);">屏幕录制</font>
+ <font style="color:rgb(51, 51, 51);">创建一个py文件，比如：main.py</font>
+ <font style="color:rgb(51, 51, 51);">在终端中，执行如下指令：</font>
    - **<font style="color:rgb(51, 51, 51);">playwright codegen -o main.py </font>**
        * <font style="color:rgb(51, 51, 51);">将屏幕录制生成的代码保存到main.py文件中</font>
        * <font style="color:rgb(51, 51, 51);">可以通过如下设置，生成同步还是异步的代码：</font>
    - **<font style="color:rgb(51, 51, 51);">playwright codegen --viewport-size=800,600 </font>**[**<font style="color:rgb(51, 51, 51);">www.baidu.com</font>**](https://www.baidu.com)**<font style="color:rgb(51, 51, 51);"> -o main.py </font>**
        * <font style="color:rgb(51, 51, 51);">访问指定网址，并且设置浏览器窗口大小</font>

**<font style="color:rgb(51, 51, 51);">playwright codegen --device="iPhone 13" -o main.py</font>**

        * <font style="color:rgb(51, 51, 51);">模拟手机设备进行网络请求（只支持手机模拟器，无需单独安装）</font>
        * <font style="color:rgb(51, 51, 51);">支持的移动端设备如下：目前对安卓设备的覆盖率不高</font>
    - <font style="color:rgb(51, 51, 51);">"Blackberry PlayBook",  "Blackberry PlayBook landscape",  "BlackBerry Z30",  "BlackBerry Z30 landscape",  "Galaxy Note 3",  "Galaxy Note 3 landscape",  "Galaxy Note II",  "Galaxy Note II landscape",  "Galaxy S III",  "Galaxy S III landscape",  "Galaxy S5",  "Galaxy S5 landscape",  "Galaxy S8",  "Galaxy S8 landscape",  "Galaxy S9+",  "Galaxy S9+ landscape",  "Galaxy Tab S4",  "Galaxy Tab S4 landscape",  "iPad (gen 5)",  "iPad (gen 5) landscape",  "iPad (gen 6)",  "iPad (gen 6) landscape",  "iPad (gen 7)",  "iPad (gen 7) landscape",  "iPad Mini",  "iPad Mini landscape",  "iPad Pro 11",  "iPad Pro 11 landscape",  "iPhone 6",  "iPhone 6 landscape",  "iPhone 6 Plus",  "iPhone 6 Plus landscape",  "iPhone 7",  "iPhone 7 landscape",  "iPhone 7 Plus",  "iPhone 7 Plus landscape",  "iPhone 8",  "iPhone 8 landscape",  "iPhone 8 Plus",  "iPhone 8 Plus landscape",  "iPhone SE",  "iPhone SE landscape",  "iPhone X",  "iPhone X landscape",  "iPhone XR",  "iPhone XR landscape",  "iPhone 11",  "iPhone 11 landscape",  "iPhone 11 Pro",  "iPhone 11 Pro landscape",  "iPhone 11 Pro Max",  "iPhone 11 Pro Max landscape",  "iPhone 12",  "iPhone 12 landscape",  "iPhone 12 Pro",  "iPhone 12 Pro landscape",  "iPhone 12 Pro Max",  "iPhone 12 Pro Max landscape",  "iPhone 12 Mini",  "iPhone 12 Mini landscape",  "iPhone 13",  "iPhone 13 landscape",  "iPhone 13 Pro",  "iPhone 13 Pro landscape",  "iPhone 13 Pro Max",  "iPhone 13 Pro Max landscape",  "iPhone 13 Mini",  "iPhone 13 Mini landscape",  "iPhone 14",  "iPhone 14 landscape",  "iPhone 14 Plus",  "iPhone 14 Plus landscape",  "iPhone 14 Pro",  "iPhone 14 Pro landscape",  "iPhone 14 Pro Max",  "iPhone 14 Pro Max landscape",  "Kindle Fire HDX",  "Kindle Fire HDX landscape",  "LG Optimus L70",  "LG Optimus L70 landscape",  "Microsoft Lumia 550",  "Microsoft Lumia 550 landscape",  "Microsoft Lumia 950",  "Microsoft Lumia 950 landscape",  "Nexus 10",  "Nexus 10 landscape",  "Nexus 4",  "Nexus 4 landscape",  "Nexus 5",  "Nexus 5 landscape",  "Nexus 5X",  "Nexus 5X landscape",  "Nexus 6",  "Nexus 6 landscape",  "Nexus 6P",  "Nexus 6P landscape",  "Nexus 7",  "Nexus 7 landscape",  "Nokia Lumia 520",  "Nokia Lumia 520 landscape",  "Nokia N9",  "Nokia N9 landscape",  "Pixel 2",  "Pixel 2 landscape",  "Pixel 2 XL",  "Pixel 2 XL landscape",  "Pixel 3",  "Pixel 3 landscape",  "Pixel 4",  "Pixel 4 landscape",  "Pixel 4a (5G)",  "Pixel 4a (5G) landscape",  "Pixel 5",  "Pixel 5 landscape",  "Pixel 7",  "Pixel 7 landscape",  "Moto G4",  "Moto G4 landscape"</font>

### <font style="color:rgb(51, 51, 51);">保留记录cookie信息(重要)</font>
+ **<font style="color:rgb(51, 51, 51);">playwright codegen --save-storage=auth.json </font>**[**<font style="color:rgb(51, 51, 51);">http://download.java1234.com/</font>**](http://download.java1234.com/)
    - <font style="color:rgb(51, 51, 51);">在屏幕录制时，进行登录操作，登录后，cookie信息会被保存到auth.json文件中</font>
+ **<font style="color:rgb(51, 51, 51);">playwright codegen --load-storage=auth.json </font>**[**<font style="color:rgb(51, 51, 51);">http://download.java1234.com/</font>**](http://download.java1234.com/)**<font style="color:rgb(51, 51, 51);"> -o main.py </font>**
    - <font style="color:rgb(51, 51, 51);">基于auth.json进行屏幕录制，会自动进入到登录成功后的页面中</font>

### <font style="color:rgb(51, 51, 51);">第一个Playwright脚本</font>
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:#创建Playwright管理器
    bro = p.chromium.launch(headless=False)
    page = bro.new_page()
    page.goto('https://www.baidu.com')
    #自行设置等待时长，注意：不可使用time.sleep
    page.wait_for_timeout(1000)
    title = page.title()
    content = page.content()
    print(title,content)
    page.close()
    bro.close()
```

### <font style="color:rgb(51, 51, 51);">元素定位（重点）</font>
#### <font style="color:rgb(51, 51, 51);">CSS选择器定位</font>
+ <font style="color:rgb(51, 51, 51);">语法结构：page.locator()</font>
    - <font style="color:rgb(51, 51, 51);">参数：标签/id/层级/class 选择器</font>
+ <font style="color:rgb(51, 51, 51);">交互操作：</font>
    - <font style="color:rgb(51, 51, 51);">点击元素， </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">click()</font>`<font style="color:rgb(51, 51, 51);"> 方法</font>
    - <font style="color:rgb(51, 51, 51);">元素内输入文本， </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">fill()</font>`<font style="color:rgb(51, 51, 51);"> 方法</font>

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    bro = p.chromium.launch(headless=False,slow_mo=2000)
    page = bro.new_page()
    page.goto('https://www.baidu.com')

    #定位到输入框，进行文本录入
    page.locator('#kw').fill('Python教程') #id定位
    # 定位搜索按钮，进行点击操作
    page.locator('#su').click()
    #后退操作
    page.go_back()

    page.locator('.s_ipt').fill('爬虫')  # class定位
    page.locator('#su').click()
    page.go_back()

    page.locator('input#kw').fill('人工智能')  # 标签+属性定位
    page.locator('#su').click()
    page.go_back()

    page.locator('#form > span > input#kw').fill('数据分析') #层级定位
    page.locator('#su').click()

    page.close()
    bro.close()
```

+ <font style="color:rgb(51, 51, 51);">设置内容输入的时间间隔</font>

```python
from playwright.sync_api import sync_playwright
import random
with sync_playwright() as p:
    bro = p.chromium.launch(headless=False)
    page = bro.new_page()
    page.goto('https://www.baidu.com')

    #定位到输入框，进行文本录入
    tag = page.locator('#kw') #id定位

    #设置内容的输入的时间间隔
    tag.focus() #聚焦于当前标签
    input_text = 'Hello, World!'
    for char in input_text:
        page.keyboard.type(char, delay=random.randint(300,600))

    # 定位搜索按钮，进行点击操作
    page.locator('#su').click()

    page.close()
    bro.close()
```

+ <font style="color:rgb(51, 51, 51);">更多操作</font>
    - <font style="color:rgb(51, 51, 51);">locator.count()</font>
    - <font style="color:rgb(51, 51, 51);">locator.nth(index)</font>
    - <font style="color:rgb(51, 51, 51);">inner_text()</font>
    - <font style="color:rgb(51, 51, 51);">get_by_text(xxx)</font>
    - <font style="color:rgb(51, 51, 51);">get_attribute(attrName)</font>
+ <font style="color:rgb(51, 51, 51);">taobao在不登录情况下无法进行商品搜索，因此需要手动登录，保留Cookie信息</font>
    - <font style="color:rgb(51, 51, 51);">playwright codegen --save-storage=taobao.json </font>[<font style="color:rgb(51, 51, 51);">https://www.taobao.com</font>](https://www.taobao.com)
+ <font style="color:rgb(51, 51, 51);">携带Cookie信息进行操作：</font>
    - <font style="color:rgb(51, 51, 51);">context = browser.new_context(storage_state="taobao.json")</font>

```python
from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p:
    #slow_mo=2000每个操作等待两秒
    browser = p.chromium.launch(headless=False,slow_mo=2000)
    context = browser.new_context(storage_state="taobao.json")
    page = context.new_page()
    page.goto("https://www.taobao.com/")

    page.locator('#q').fill('mac pro')
    # class属性值为btn-search tb-bg，在定位的时候选择空格左右两侧任意一个属性值即可
    page.locator('.btn-search').click()
    page.wait_for_timeout(1000)

    # 根据文本定位
    page.get_by_text('发货地').click()
    page.wait_for_timeout(1000)

    # 定位到满足要求所有的标签(商品列表最外层的a标签)
    locator = page.locator('.Content--contentInner--QVTcU0M > div > a')
    all_eles = locator.all()

    # 查看定位到满足要求标签的数量
    count = locator.count()
    print(count)
# 定位到第10个a标签,nth下标从0开始
a_10 = locator.nth(9)
print(a_10.get_attribute('href'), a_10.inner_text())
print('---------------------------------------------------------------------------')
# 获得每一个a标签中的文本内容和href属性值
for index in range(count):
    ele = locator.nth(index)
    text = ele.inner_text()
    href = ele.get_attribute('href')
    print(text, href)

    page.close()
context.close()
browser.close()
```

#### <font style="color:rgb(51, 51, 51);">xpath定位</font>
<font style="color:rgb(51, 51, 51);">page.locator(xpath表达式)</font>

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    bro = p.chromium.launch(headless=False,slow_mo=2000)
    page = bro.new_page()
    page.goto('https://www.bilibili.com/')

    #xpath定位
    page.locator('//*[@id="nav-searchform"]/div[1]/input').fill('Python教程')
    page.locator('//*[@id="nav-searchform"]/div[2]').click()

    page.close()
    bro.close()
```

  
 

