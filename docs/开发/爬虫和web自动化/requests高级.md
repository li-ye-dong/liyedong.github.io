### 上节作业
+ 简历数据爬取

```python
from lxml import etree
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url = 'https://sc.chinaz.com/jianli/free.html'
response = requests.get(url=url,headers=headers)
response.encoding = 'utf-8'
page_text = response.text
#数据解析:简历名称+详情页的url
tree = etree.HTML(page_text)
div_list = tree.xpath('//*[@id="container"]/div')
for div in div_list:
    title = div.xpath('./p/a/text()')[0]+'.rar'
    detail_url = 'https:'+div.xpath('./p/a/@href')[0]
    # print(title,detail_url)
    #对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url,headers=headers).text
    #数据解析：下载地址
    tree = etree.HTML(detail_page_text)
    download_url = tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
    #在下载请求建立模板
    data = requests.get(url=download_url,headers=headers).content
    with open(title,'wb') as fp:
        fp.write(data)
    print(title,'保存下载成功！')
```

+ 图片懒加载：
    - url：[https://sc.chinaz.com/tupian/meinvtupian.html](https://sc.chinaz.com/tupian/meinvtupian.html)
        * 爬取上述链接中所有的图片数据
    - 主要是应用在展示图片的网页中的一种技术，该技术是指当网页刷新后，先加载局部的几张图片数据即可，随着用户滑动滚轮，当图片被显示在浏览器的可视化区域范围的话，在动态将其图片请求加载出来即可。（图片数据是动态加载出来）。
    - 如何实现图片懒加载/动态加载？
        * 使用img标签的伪属性（指的是自定义的一种属性）。在网页中，为了防止图片马上加载出来，则在img标签中可以使用一种伪属性来存储图片的链接，而不是使用真正的src属性值来存储图片链接。（图片链接一旦给了src属性，则图片会被立即加载出来）。只有当图片被滑动到浏览器可视化区域范围的时候，在通过js将img的伪属性修改为真正的src属性，则图片就会被加载出来。
    - 如何爬取图片懒加载的图片数据？
        * 只需要在解析图片的时候，定位伪属性的属性值即可

```python
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url = 'https://sc.chinaz.com/tupian/meinvtupian.html'
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
div_list = tree.xpath('/html/body/div[3]/div[2]/div')
for div in div_list:
    src = 'https:'+div.xpath('./img/@data-original')[0]
    print(src)
```

### 防盗链
+ 现在很多网站启用了防盗链反爬，防止服务器上的资源被人恶意盗取。什么是防盗链呢？
    - 从HTTP协议说起，在HTTP协议中，有一个表头字段：referer，采用URL的格式来表示从哪一个链接跳转到当前网页的。通俗理解就是：客户端的请求具体从哪里来，服务器可以通过referer进行溯源。一旦检测来源不是网页所规定的，立即进行阻止或者返回指定的页面。
+ 案例：抓取微博图片，url：[http://blog.sina.com.cn/lm/pic/](http://blog.sina.com.cn/lm/pic/)，将页面中某一组系列详情页的图片进行抓取保存，比如三里屯时尚女郎：[http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1](http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1)
    - 注意：
        * 1.在解析图片地址的时候，定位src的属性值，返回的内容和开发工具Element中看到的不一样，通过network查看网页源码发现需要解析real_src的值。
        * 2.直接请求real_src请求到的图片不显示，加上Refere请求头即可
            + 哪里找Refere：抓包工具定位到某一张图片数据包，在其requests headers中获取

```python
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    "Referer": "http://blog.sina.com.cn/",

}
url = 'http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1'
page_text = requests.get(url,headers=headers).text
tree = etree.HTML(page_text)
img_src = tree.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img/@real_src')
for src in img_src:
    data = requests.get(src,headers=headers).content
    with open('./123.jpg','wb') as fp:
        fp.write(data)
    # break
```

### 视频数据爬取 
+ url：[https://www.51miz.com/shipin/](https://www.51miz.com/shipin/)
    - 爬取当前url页面中营销日期下的几个视频数据。
+ 找寻每个视频的播放地址：
    - 在video标签下面有一个source标签，其内部的src属性值正好就是视频的播放地址 (补充上https:即可) 。

```python
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Referer':'https://www.51miz.com/'
}
url = 'https://www.51miz.com/shipin/'
response = requests.get(url=url,headers=headers)
page_text = response.text

#数据解析
tree = etree.HTML(page_text)
div_list = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div')
for div in div_list:
    src_list = div.xpath('./a/div/div/div/video/source/@src')
    #要给视频地址进行补全
    for src in src_list:
        video_data = requests.get(url=src,headers=headers).content
        video_title = src.split('/')[-1]
        with open(video_title,'wb') as fp:
            fp.write(video_data)
        print(video_title,'爬取保存成功！')

    break
```

### Cookie（重点）
+ 什么是cookie？
    - cookie的本质就是一组数据（键值对的形式存在）
    - 是由服务器创建，返回给客户端，最终会保存在客户端浏览器中。
    - 如果客户端保存了cookie，则下次再次访问该服务器，就会携带cookie进行网络访问。
        * 典型的案例：网站的免密登录
+ 爬取雪球网中的咨询数据
    - url：[https://xueqiu.com/](https://xueqiu.com/)，需求就是爬取热帖内容
    - 经过分析发现帖子的内容是通过ajax动态加载出来的，因此通过抓包工具，定位到ajax请求的数据包，从数据包中提取：
        * url：[https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=311519&size=15](https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=311519&size=15)
        * 请求方式：get
        * 请求参数：拼接在了url后面

```python
import requests
import os
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
}
url = 'https://xueqiu.com/statuses/hot/listV2.json'
param = {
    "since_id": "-1",
    "max_id": "311519",
    "size": "15",
}
response = requests.get(url=url,headers=headers,params=param)
data = response.json()
print(data)
#发现没有拿到我们想要的数据
```

    - 分析why？
        * 切记：只要爬虫拿不到你想要的数据，唯一的原因是爬虫程序模拟浏览器的力度不够！一般来讲，模拟的力度重点放置在请求头中！
        * 上述案例，只需要在请求头headers中添加cookie即可！
    - 爬虫中cookie的处理方式（两种方式）：
        * 手动处理：将抓包工具中的cookie赋值到headers中即可
            + 缺点：
                - 编写麻烦
                - cookie通常都会存在有效时长
                - cookie中可能会存在实时变化的局部数据
        * 自动处理 (重点)
            + 爬虫的session会话对象：
                - 在爬虫里，session对象是一个非常常用的对象，这个对象代表一次用户会话（从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开）。session对象能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 cookie 。
            + 基于session对象实现自动处理cookie。
                - 1.创建一个空白的session对象。
                - 2.需要使用session对象发起请求，请求的目的是为了捕获cookie
                    * 注意：如果session对象在发请求的过程中，服务器端产生了cookie，则cookie会自动存储在session对象中。
                - 3.使用携带cookie的session对象，对目的网址发起请求，就可以实现携带cookie的请求发送，从而获取想要的数据。
            + 注意：session对象至少需要发起两次请求
                - 第一次请求的目的是为了捕获存储cookie到session对象
                - 后次的请求，就是携带cookie发起的请求了

```python
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}
param = {
    #如果遇到了动态变化的请求参数？必须经过测试才知道需不需要处理
    "since_id": "-1",
    "max_id": "553059", #动态变化的请求参数
    "size": "25"
}

url = 'https://xueqiu.com/statuses/hot/listV3.json?page=1&last_id='

#session对象会实时保存跟踪服务器端给客户端创建的cookie
#创建一个session对象
session = requests.Session() #空白的session对象

first_url = 'https://xueqiu.com/'
#使用session对象进行请求发送：如果该次请求时，服务器端给客户端创建cookie的话，则该cookie就会被保存seesion对象中
session.get(url=first_url,headers=headers)
#使用保存了cookie的session对象进行后续请求发送
ret = session.get(url=url,headers=headers).json()
print(ret)
```

### 模拟登录
+ [http://download.java1234.com/](http://download.java1234.com/)直接访问个人中心和登录后访问其个人中心

```python
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
session = requests.Session()
data = {
    "userName": "bb328410948",
    "password": "bb328410948"
}
session.post('http://download.java1234.com/user/login',data=data,headers=headers)

page_text = session.get('http://download.java1234.com/toUserCenterPage',headers=headers).text

with open('1.html','w') as fp:
    fp.write(page_text)
```

### 代理（重要）
+ 什么是代理
    - 代理服务器
+ 代理服务器的作用
    - 就是用来转发请求和响应

		

+ 在爬虫中为何需要使用代理？
    - 有些时候，需要对网站服务器发起高频的请求，网站的服务器会检测到这样的异常现象，则会讲请求对应机器的ip地址加入黑名单，则该ip再次发起的请求，网站服务器就不在受理，则我们就无法再次爬取该网站的数据。
    - 使用代理后，网站服务器接收到的请求，最终是由代理服务器发起，网站服务器通过请求获取的ip就是代理服务器的ip，并不是我们客户端本身的ip。
+ 代理的匿名度
    - 透明：网站的服务器知道你使用了代理，也知道你的真实ip
    - 匿名：网站服务器知道你使用了代理，但是无法获知你真实的ip
    - 高匿：网站服务器不知道你使用了代理，也不知道你的真实ip（推荐）
+ 代理的类型（重要）
    - http：该类型的代理服务器只可以转发http协议的请求
    - https：可以转发https协议的请求
+ 如何获取代理?
    - 芝麻代理：[https://jahttp.zhimaruanjian.com/](https://jahttp.zhimaruanjian.com/)（推荐，有新人福利）
+ 如何使用代理？
    - 测试：访问如下网址，返回自己本机ip

```python
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
}
url = 'http://www.cip.cc/'

page_text = requests.get(url,headers=headers).text
tree = etree.HTML(page_text)
text = tree.xpath('/html/body/div/div/div[3]/pre/text()')[0]
print(text.split('\n')[0])
```

    - 使用代理发起请求，查看是否可以返回代理服务器的ip

```python
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
}
url = 'http://www.cip.cc/'

page_text = requests.get(url,headers=headers,proxies={'http':'121.234.12.62:4246'}).text
tree = etree.HTML(page_text)
text = tree.xpath('/html/body/div/div/div[3]/pre/text()')[0]
print(text.split('\n')[0])
```

  


### 验证码
+ 图鉴平台：[http://www.ttshitu.com/](http://www.ttshitu.com/) （推荐）
+ <font style="color:rgb(51, 51, 51);">使用流程：</font>
    - <font style="color:rgb(51, 51, 51);">注册登录图鉴平台</font>
    - <font style="color:rgb(51, 51, 51);">登录后，点击开发文档，提取识别的源代码</font>
    - <font style="color:rgb(51, 51, 51);">模块(tujian.py)的封装：</font>

```python
import base64
import json
import requests
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""
```

    - <font style="color:rgb(51, 51, 51);">验证码图片识别操作</font>
        * <font style="color:rgb(51, 51, 51);">识别本地的滑动验证和坐标点击验证</font>

```python
import tujian
ret = tujian.base64_api('username','password','code_2.png',33)
print(ret)
```

```python

```

