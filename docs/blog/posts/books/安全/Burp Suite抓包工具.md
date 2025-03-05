# 安装<font style="color:rgb(79, 79, 79);">JDK</font>
**<font style="color:rgb(77, 77, 77);">1，我们先把工具放到win10主机上，准备好（可以安装到win10虚拟机，也可以安装到物理机上）</font>**

![](../../images/1729265377461-a9fbfb62-16b6-4b0f-a32b-16c43d1b0911.png)

![](../../images/1729265390268-8733cae2-bbd4-4cb6-aba1-c0ea43b81d47.png)

![](../../images/1729265402518-7c53721e-d68c-4368-be73-9ae54592907b.png)

![](../../images/1729265420783-0126af98-4f42-40e5-a10d-e5c28da065de.png)

![](../../images/1729265429188-069cb69c-0e48-4784-a97e-0800d6f61c97.png)

# 安装Burp Suite
![](../../images/1729265442616-727d7c48-82b7-4b04-a3d5-f6da77777d01.png)

# <font style="color:rgb(79, 79, 79);">激活Burp Suite</font>
**<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">首先，打开中文版bp程序， CN-JRE Burp.bat 是启动中文版BP的， EN-JRE Brup.bat 是启动英文版BP 的，其他的文件看 当前目录注意事项.txt 文档，有说明。</font>**![](../../images/1729265495237-c52e6c7a-f3c4-4fe5-9355-8fa54cb8a386.png)

**<font style="color:rgb(77, 77, 77);">点击 CN-JRE Burp.bat，如下，会有一个黑色的CMD窗口自动跟着打开了，这个窗口之后都不要关闭，除非我们要关闭BP。</font>**

![](../../images/1729265504345-9876e5fc-a1b4-49f0-a92f-03b0da6f7e80.png)

**<font style="color:rgb(77, 77, 77);">取消勾选，点击接受</font>**

![](../../images/1729265514429-d6d6c395-a582-40ff-8cc9-1f490102d18c.png)

**<font style="color:rgb(77, 77, 77);">弹出如下窗口</font>**

![](../../images/1729265523528-c8876101-1ad0-4db6-80c6-8b6acac4b980.png)

**<font style="color:rgb(77, 77, 77);">生成许可证密钥数据，打开bp目录中的如下目录</font>**

![](../../images/1729265540345-bc24d302-cb53-4469-92d5-c575f646f7e0.png)

**<font style="color:rgb(77, 77, 77);">如下，添加密钥，然后点击下一步：</font>**

![](../../images/1729265548400-6126e95f-9716-4c11-8198-2d0f1775e979.png)

**<font style="color:rgb(77, 77, 77);">选择手动激活</font>**

![](../../images/1729265555685-462d3b9c-bb2f-4658-8247-e6eebb878f87.png)

**<font style="color:rgb(77, 77, 77);">按照如下步骤进行操作</font>**

![](../../images/1729265567211-fcfe2d90-53b6-4312-9d0a-e42b6b3891d7.png)

**<font style="color:rgb(77, 77, 77);">成功安装并激活完成了</font>**

![](../../images/1729265576798-54a72bb5-238e-48a9-8bae-62e19f4dbf7f.png)

**<font style="color:rgb(77, 77, 77);">看到如下窗口，表示BP安装并激活成功了。</font>**<font style="color:rgb(77, 77, 77);"> </font>**<font style="color:rgb(77, 77, 77);">下一步</font>**

![](../../images/1729265585838-981ad38c-70b1-4866-8a55-9dbfb4b16266.png)

**<font style="color:rgb(77, 77, 77);">启动burp</font>**

![](../../images/1729265619041-467334c8-ff16-4485-b4dd-6d7f821240e7.png)

**<font style="color:rgb(77, 77, 77);">这就是他的面板了</font>**

![](../../images/1729265629251-2af35f12-ad89-4805-85d9-9b36896d94dc.png)

**<font style="color:rgb(77, 77, 77);">快捷方式 CN-JRE Burp.bat就是它的启动文件，可以放到桌面上</font>**

![](../../images/1729265638744-f913d61f-714d-4601-bcf6-04bd531fd81d.png)

# **<font style="color:rgb(79, 79, 79);">设置 Burp Suite 代理</font>**
![](../../images/1729265647066-22fde58b-e108-410f-be28-fdb440fe2369.png)

**<font style="color:rgb(77, 77, 77);">设置代理有多种形式，我们先说两种最常用的</font>**

#### **<font style="color:rgb(79, 79, 79);">5-1 系统设置代理转发到****BP</font>**
**<font style="color:rgb(77, 77, 77);">首先，打开我们的BP，看一下BP的代理功能设置</font>**

![](../../images/1729265664973-445521e0-55c4-4f5e-99b1-950bf325bac7.png)

**<font style="color:rgb(77, 77, 77);">注意上面的IP和端口，我们称之为BP代理服务器的IP和端口。 它监听本机8080端口，并对过8080端口的数据包进行拦截，修改等操作，所以我们还需要设置系统代理，让流量转发到8080端口</font>**

**<font style="color:rgb(77, 77, 77);">win10：</font>**

**<font style="color:rgb(77, 77, 77);">打开系统设置</font>**

![](../../images/1729265681831-ba94c06b-4fc9-4824-8795-f0d769092861.png)

**<font style="color:rgb(77, 77, 77);">搜索代理，然后是代理服务器设置</font>**

![](../../images/1729265689982-d31f5117-4925-443b-9ce9-1f9e7ba2b183.png)

![](../../images/1729265698183-5539f860-f949-4fee-b881-7d759022b21e.png)

**<font style="color:rgb(85, 86, 102);">代理服务器的IP和端口设置，要和BP代理服务器的IP和端口一致，这样就能将我们主机上的HTTP数据包 转发到BP上了。</font>**

**<font style="color:rgb(85, 86, 102);">win11设置代理如下，其他和win10是一样的，不做累述了：</font>**

**<font style="color:rgb(85, 86, 102);">打开系统设置 – 搜索代理 – 打开代理服务器设置 – 找到手动代理中的使用代理服务器 – 点击设置</font>**

![](../../images/1729265708144-80dac518-1e2d-4c5a-9353-6bf23eda7af5.png)

#### <font style="color:rgb(79, 79, 79);">5-2</font><font style="color:rgb(79, 79, 79);"> </font>**<font style="color:rgb(79, 79, 79);">系统代理开启之后</font>****<font style="color:rgb(79, 79, 79);">BP</font>****<font style="color:rgb(79, 79, 79);">抓包</font>**
**<font style="color:rgb(77, 77, 77);">打开谷歌浏览器（如果没有安装的话工具里面给了，自行安装，安装很简单的）</font>**

**<font style="color:rgb(77, 77, 77);">浏览了一个 hebei.com.cn的网站，现在看看是否有历史记录</font>**

![](../../images/1729265716583-cb706228-4a92-4b89-93a0-643eb04e9934.png)

**<font style="color:rgb(77, 77, 77);">可以看到在代理 ---- http历史记录里看到许多记录</font>**

![](../../images/1729265724656-c6d2f86b-e907-4f0c-be6c-1574fb900db9.png)

**<font style="color:rgb(77, 77, 77);">如何拦截数据包？</font>**

**<font style="color:rgb(77, 77, 77);">代理 — 拦截 ----打开拦截</font>**

![](../../images/1729265732682-62168302-192c-43d1-8d6d-3d4706bf7d04.png)

**<font style="color:rgb(77, 77, 77);">回到浏览器刷新页面，发现页面一直在刷新，回来看看burp Suite</font>**

![](../../images/1729265743624-4cca1f5e-4894-4399-8934-872ce6b48f01.png)

**<font style="color:rgb(77, 77, 77);">修改完成以后可以点击‘放行’ 来放包，也可以让数据包丢弃，不让他到后端，就相当于丢失了</font>**

![](../../images/1729265755221-1100fd7c-cfc2-45cf-a23c-ac67b12bf1c3.png)

**<font style="color:rgb(77, 77, 77);">有时候我们需要对一个数据包进行反复修改，发到后端，这时候可以把包放到重放器里面</font>**

**<font style="color:rgb(77, 77, 77);">右击 ---- 发动到repeater</font>**

![](../../images/1729265767147-e3e11605-53c8-4b97-9b10-4d637121ef56.png)

**<font style="color:rgb(77, 77, 77);">打开重放器就可以看到数据包，可以进行反复修改</font>**

![](../../images/1729265774778-5ba3fcb2-4d0c-421a-9248-247f065401ce.png)

**<font style="color:rgb(77, 77, 77);">功能差不多就讲到这里，我会出一期视频会详细讲解burpSuite的常用功能</font>**

**<font style="color:rgb(77, 77, 77);">但是你可以抓一下，百度，或者京东的包，发现如下情况</font>**

![](../../images/1729265784167-01289255-9993-4645-950a-9e4e8897e3ea.png)

**<font style="color:rgb(77, 77, 77);">点击高级，然后继续访问此页面，看到如下样式乱了的页面</font>**

![](../../images/1729265792437-186677bf-2365-4ecb-a978-22264ac168c3.png)

**<font style="color:rgb(85, 86, 102);">这是为什么呢？提示不安全？并且看到网址栏中有了个红色的https，并且画了个横线，然后我们点击高级，点击继续访问，就看到了页面，但是有些数据却显示不正常，页面也乱套了，为什么呢？</font>**

**<font style="color:rgb(85, 86, 102);">这就不得不说HTTPS协议了，这是个网络传输的安全协议，由于我们做代理配置和抓包时，没有做 HTTPS协议的相关处理，导致了问题的出现，提示不安全的同时，导致有些数据都没有办法正常传输， 有些数据甚至都抓不到包</font>**

**<font style="color:rgb(77, 77, 77);">想解决如上问题，想抓到HTTPS的数据包就需要在浏览器上安装上Bp导出的证书</font>**

#### <font style="color:rgb(79, 79, 79);">5-3 浏览器安装Burp Suite安全证书</font>
![](../../images/1729265827075-a597f5fe-4563-47b5-8412-6acfddd6f3a4.png)

**<font style="color:rgb(77, 77, 77);">选择 DER格式的证书，然后下一步</font>**

![](../../images/1729265835044-1843807d-a2c5-43f8-b757-7624dea709bb.png)

**<font style="color:rgb(77, 77, 77);">自己选择个文件，文件名可以随便写，但是.cer后缀</font>**

  
 ![](../../images/1729265843162-668bde16-3f3d-4fb2-9dd1-d814c305dc66.png)

![](../../images/1729265866681-79318007-1a67-4ed4-9408-fad545dd954c.png)



##### **<font style="color:rgb(79, 79, 79);">5-3-2 浏览器安装证书</font>**
**<font style="color:rgb(77, 77, 77);">打开谷歌浏览器的设置</font>**

![](../../images/1729265875585-e6edced1-0357-45ee-aa7f-2169c26911ce.png)

**<font style="color:rgb(77, 77, 77);">搜索证书，然后选择安全</font>**

![](../../images/1729265891262-18333766-9c0e-4ee5-ace1-4cbbd539258c.png)

**<font style="color:rgb(77, 77, 77);">管理证书</font>**

![](../../images/1729265899587-1f50a8af-a7a3-4f21-b971-a890009f3c08.png)

**<font style="color:rgb(77, 77, 77);">选择导入</font>**

![](../../images/1729265906888-d07bf659-d496-4de6-8b2b-248a1ef56d0b.png)

**<font style="color:rgb(77, 77, 77);">下一步</font>**

![](../../images/1729265915080-370d9267-1bc1-457d-90a5-df04e7b9c4ab.png)

**<font style="color:rgb(77, 77, 77);">选择刚才导出的证书，然后就下一步即可</font>**

![](../../images/1729265923126-ff2b106e-56b0-4352-afc0-1dd7dc6cdf4c.png)

**<font style="color:rgb(77, 77, 77);">下一步</font>**

![](../../images/1729265930751-639bbabe-166c-4dd5-b346-7f7ea7a04428.png)

**<font style="color:rgb(77, 77, 77);">完成</font>**

![](../../images/1729265948173-2565c9a6-6d5a-40c9-ae82-4de84c11e9c8.png)

**<font style="color:rgb(77, 77, 77);">同样的导入方式继续导入证书</font>**

**<font style="color:rgb(77, 77, 77);">（注意，未受信任的发布者不用导入，导入了就抓不到包了）</font>**

![](../../images/1729265967597-c5372b00-1e7e-4dd1-9ec5-f27b624ac361.png)

**<font style="color:rgb(77, 77, 77);">安装受信任的根证书颁发机构的时候会有以下提示，点击是即可</font>**

![](../../images/1729265978850-8b8be7bd-3fe6-4e47-be43-a5d797fb0527.png)

**<font style="color:rgb(77, 77, 77);">当除了未受信任的发布者不要安装以外，其余的安装好以后可以退出</font>**

**<font style="color:rgb(77, 77, 77);">现在抓https的包试一试，发现正常能访问了，爆破也能看到浏览记录</font>**  
 

#### **<font style="color:rgb(79, 79, 79);">5-4 应用程序设置代理转发到****BP</font>**
---

**<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">刚才的系统代理开启然后BP抓包的方式太粗暴了，会抓取我们计算机上所有的HTTP请求请求数据包， 这样导致一个问题就是，会抓到好多我们不想看到的其他应用程序的数据包，比如我们只想抓取火狐浏览器firefox的数据包，但是如果你电脑上运行着一些其他应用程序，这些应用程序的HTTP数据包也会被抓到，很容易对我们分析数据包的时候产生混淆。</font>**

**<font style="color:rgb(85, 86, 102);background-color:rgb(238, 240, 244);">那么我们就可以给某个应用程序单独设置代理，那么BP就只抓这个应用程序的数据，但是有个问题就是，并不是所有的应用程序都支持单独设置代理，比如chrome浏览器就不行，火狐浏览器就可以，那么不能单独设置代理的程序如何来抓呢，就可以用上面的系统代理的形式来抓，还有一些可能不是http协议数据传输的，那么还可以用到其他的抓包工具，比如wireshark、进程抓包工具、全局代理工具等来实现抓包，这些后面我们再一一细说，先看火狐浏览器是如何单独设置代理的。</font>**

##### <font style="color:rgb(79, 79, 79);">5-4-1 火狐浏览器设置代理</font>
**<font style="color:rgb(77, 77, 77);">（火狐浏览器自行安装一下，安装包也给你们了，工具里面有）</font>**

**<font style="color:rgb(77, 77, 77);">1、先关闭我们的系统代理</font>**

**<font style="color:rgb(77, 77, 77);">关掉刚才开的系统代理</font>**

![](../../images/1729266056532-492e8093-bc0d-4f53-854f-9e44d66ef477.png)

**<font style="color:rgb(77, 77, 77);">2、打开火狐浏览器的代理设置</font>**

![](../../images/1729266064249-d6cd9dea-af1a-4385-9384-8fbf0e05823d.png)

**<font style="color:rgb(77, 77, 77);">搜索代理，然后点击设置</font>**

![](../../images/1729266073713-3b638d73-4904-4836-9fbb-fe33f20bd244.png)

**<font style="color:rgb(77, 77, 77);">填写代理地址，端口，将下面的将此代理由于HTTPS√勾上，然后确定即可</font>**

  
 ![](../../images/1729266085949-988fa1a4-c999-48f6-ae8f-bf525ca61573.png)

##### <font style="color:rgb(79, 79, 79);">5-4-2 火狐浏览器安装证书</font>
**<font style="color:rgb(77, 77, 77);">同样为了解决HTTPS协议的抓包问题，也需要安装证书</font>**

  
 ![](../../images/1729266102939-6bb1a5b8-18e2-4c94-bee9-0cc4e0580afc.png)

**<font style="color:rgb(77, 77, 77);">选择导入（证书颁发机构，服务器，个人，认证决策，你的证书，凡是能安装证书的地方都安装上）</font>**

![](../../images/1729266114456-c66538cf-14a0-427c-a42c-bbe9fffa1365.png)



**<font style="color:rgb(77, 77, 77);">选择导入以后，选择bp导出的证书，然后可能会有如下弹框，两个√都勾上，然后确定即可</font>**

![](../../images/1729266146036-2bf15b79-1120-4b9c-80c8-a74d6dbdef0c.png)

**<font style="color:rgb(77, 77, 77);">好像只需要在证书办法机构和个人两个地方导入即可，最后点击确认即可。</font>**

**<font style="color:rgb(77, 77, 77);">设置完成以后浏览器重启一下</font>**

![](../../images/1729266159711-bf1b95d8-39fb-46fc-ad43-f7bad64d3c88.png)

**<font style="color:rgb(77, 77, 77);">发现Burp Suite开启拦截以后也能正常抓https的包</font>**

![](../../images/1729266239718-f305439b-d071-4358-a276-9f250d5c44a1.png)  
 

