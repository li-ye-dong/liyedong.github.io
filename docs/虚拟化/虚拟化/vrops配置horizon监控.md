# 上载pak文件
首先上传pak文件

![](../../images/1711518118769-75538238-5770-4b59-92ab-9d381054c11b.png)

<font style="color:rgb(100, 100, 109);">按照提示下一步，同意协议，直到提示安装成功。</font>

<font style="color:rgb(100, 100, 109);">单击 vRealize Operations Management Pack for Horizon 图标上的添加帐户。</font>![](../../images/1711518141452-1f70c2c6-dc5f-4e6e-9661-f9763b64ab60.png)

<font style="color:rgb(100, 100, 109);">按照提示，输入连接服务器的FQDN，凭据信息（vdi管理员用户名和密码，域信息）</font>![](../../images/1711518155158-b1175707-413e-4781-a188-d01ef874747c.png)

<font style="color:rgb(100, 100, 109);">验证连接后，提示成功后保存。</font>

<font style="color:rgb(100, 100, 109);">Tips：由于在安装vRealize Operations的时候没有配置DNS，导致提示无法连接，参考下面DNS配置添加DNS后即正常。</font>

![](../../images/1711518167766-f0b9761a-1dd5-48f2-9ea6-4952ab50a20b.png)

<font style="color:rgb(100, 100, 109);">多了一个Horizon目录，慢慢体验吧……</font>

# <font style="color:rgb(100, 100, 109);">升级pak文件</font>
<font style="color:rgb(100, 100, 109);">升级：以2.2升级到2.5.1为例。</font>

![](../../images/1711518179623-31fafa1c-ef56-4813-95f0-c67a9efb047b.png)

<font style="color:rgb(100, 100, 109);">集成，存储库，找到Horizon包，升级。</font>![](../../images/1711518190643-f173c4f8-bd85-42d7-bc7f-d58e5e9bdf56.png)

<font style="color:rgb(100, 100, 109);">浏览，上传最新的Horizon包，上载；</font>![](../../images/1711518199541-46375413-99a3-422c-bff3-cdaaaa98d8f9.png)

<font style="color:rgb(100, 100, 109);">完成，版本已经升级成功。</font>![](../../images/1711518207841-e6afb60d-70c0-454d-9051-01446e9afd2c.png)

# 关于horizon的连接配置问题
因为高版本的horizon中，如果没有dns解析，将无法正常连接horizon，所以需要配置dns

## dns配置教程
```shell
#进入虚拟机
#输入root
root
#输入新密码
Ops#123456
#再次输入新密码
Ops#123456
#进入root用户
vi /etc/resolv.conf 
nameserver DNS_Server_1
nameserver DNS_Server_2
search searchpath
#搜索路径和第二个 DNS 服务器都是可选项，可以跳过。
#运行如下命令确认 DNS 已更改：
resolvectl status
```

## horizon配置数据源后失败
确认dns，FQDN是否正确，如果都正确，则开始进行配置用户，与horizon控制台登录一致即可

![](../../images/1711518693133-14902761-97c1-49dd-9611-85760821350e.png)

