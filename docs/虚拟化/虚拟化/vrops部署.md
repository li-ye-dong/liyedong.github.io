# <font style="color:rgb(100, 100, 109);">兼容列表查询</font>
[<font style="color:rgb(100, 100, 109);">https://interopmatrix.vmware.com/Interoperability?col=116,&row=1363,</font>](https://interopmatrix.vmware.com/Interoperability?col=116,&row=1363,)

![](../../images/1711518863212-401dd11a-8206-4644-9f17-c6079d0c1c00.png)

# 部署安装
<font style="color:rgb(100, 100, 109);">导入OVF</font>![](../../images/1711518891242-c2fdeb94-79fe-4174-8b15-2e35b4fc4575.png)

<font style="color:rgb(100, 100, 109);">查看详细信息</font>![](../../images/1711518902024-c554de47-e922-4bea-bb07-981d67339ef3.png)

<font style="color:rgb(100, 100, 109);">选择部署配置</font>![](../../images/1711518915199-b6a14fe8-b3e8-45af-9e66-cc801c003473.png)

<font style="color:rgb(100, 100, 109);">选择部署的存储位置，磁盘格式建议选择精简置备</font>![](../../images/1711518926629-2d60efbb-6fed-4d46-8d95-1f639eaf8ae9.png)

<font style="color:rgb(100, 100, 109);">选择网络，注意目标网络通信正常</font>![](../../images/1711518935578-002230d7-b887-42a9-9fe1-3a2ebd0f414d.png)

<font style="color:rgb(100, 100, 109);">填写时区，网关，IP，掩码,dns</font>

![](../../images/1712646973868-eb3c17d4-2f7e-4f7b-99bd-a0b0b508660b.png)![](../../images/1711518944883-dd238d4b-5399-4a3c-9bf1-2ebfa641f98d.png)<font style="color:rgb(100, 100, 109);">点击FINISH</font>![](../../images/1711518964278-86f17d7a-2f65-4207-bcec-a8295d373cf4.png)

<font style="color:rgb(100, 100, 109);">设置时区，按照数字提示选亚洲，中国，北京时间，保存。</font>![](../../images/1711518973035-461e0e87-a244-45a3-9950-4d058519a6f6.png)

<font style="color:rgb(100, 100, 109);">继续选择快速安装</font>![](../../images/1711518984571-cf352131-6643-4d3d-86f7-499c09167268.png)

<font style="color:rgb(100, 100, 109);">设置管理员密码</font>

![](../../images/1711518995808-62ea0d86-e28d-4d0a-ad7a-943505847071.png)



![](../../images/1711519011892-f98ab4fd-734d-4fd5-92e2-03b67728b753.png)

<font style="color:rgb(100, 100, 109);">暂时使用评估，后续可以再导入License</font>![](../../images/1711519024903-051181a5-168c-4374-a59a-d914675be872.png)

<font style="color:rgb(100, 100, 109);">添加云账户</font>![](../../images/1711519033507-038b2590-f3d1-42b2-a343-4e50a67f1e21.png)

<font style="color:rgb(100, 100, 109);">账户类型选择vCenter</font>![](../../images/1711519042071-45336344-981c-4a80-8b8c-d5f9299e5dd9.png)

<font style="color:rgb(100, 100, 109);">按照提示添加vCenter相关IP，账户和密码，验证连接。</font>![](../../images/1711519054270-3f7c92c9-7cd4-4e8c-b48b-7b13fadfef25.png)

<font style="color:rgb(100, 100, 109);">已经添加完成。</font>![](../../images/1711519062389-928366a9-7d20-4c7b-9d25-d0dea4ed5bdb.png)

# 设置root密码
选择1

![](../../images/1711519425566-21e8b899-4fc0-4079-ae72-d8c71314ea78.png)

进入登录页

```shell
#进入虚拟机
#输入root
root
#输入新密码
Ops#123456
#再次输入新密码
Ops#123456
```

# DNS配置
```shell
#进入root用户
vi /etc/resolv.conf 
nameserver DNS_Server_1
nameserver DNS_Server_2
search searchpath
#搜索路径和第二个 DNS 服务器都是可选项，可以跳过。
#运行如下命令确认 DNS 已更改：
resolvectl status
重启会失效
vi /etc/sysconfig/network-scripts/ifup-eth
# 在这里设置 DNS 服务器
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf
systemctl restart network
```

虚拟机选项中的vapp选项的属性进行编辑

## ![](../../images/1712647352474-2a2f7fff-c96d-4aee-9e11-389a62ca5b20.png)
