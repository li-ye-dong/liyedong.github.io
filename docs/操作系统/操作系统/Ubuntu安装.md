## 安装
1、选择 Install Ubuntu Server

![](../../images/1700457590820-a4d0b768-c1f2-4364-a5c9-664cdcffe54a.png)<font style="color:rgb(51, 51, 51);">2、 语言选择，默认英语</font>![](../../images/1700457604892-536af1fa-7fd9-49bf-bb8e-fe7771213a76.png)

<font style="color:rgb(51, 51, 51);">3、键盘布局，可不用修改</font>![](../../images/1700457617514-72d5531e-747a-43d7-83f5-39f738927995.png)

<font style="color:rgb(51, 51, 51);">4、选择第二项最小化安装（如果对系统不是熟的可以选择第一项）</font>

  
 ![](../../images/1700457628237-c6e44531-ad98-4a8e-a140-d236e1e00da8.png)

<font style="color:rgb(51, 51, 51);"> 5、网络配置，使用 DHCP 或者 静态IP（建议这里设置好静态IP，如果选择DHCP，则在此界面直接选择 Done 后回车即可)。</font>

![](../../images/1700457641361-5dd1fc9f-fceb-4954-a014-5bcacbb83923.png)

![](../../images/1700457649870-5144ecd3-0347-4fff-afc7-dc8cccd52b19.png)![](../../images/1700457663751-06205fe4-71ea-4dcc-95fe-872ac93625e0.png)![](../../images/1700457671442-66161089-5e0b-46b0-80d3-800239545f46.png)

<font style="color:rgb(51, 51, 51);">6、Configure proxy配置页面的Proxy address无需配置</font>

![](../../images/1700457685175-c1217862-4811-447a-b7eb-3bb0c1baca7b.png)

<font style="color:rgb(51, 51, 51);">7、设置镜像源地址，这个可以配置阿里云(</font>[http://mirrors.aliyun.com/ubuntu/](http://mirrors.aliyun.com/ubuntu/)<font style="color:rgb(51, 51, 51);">)，下载加速</font>![](../../images/1700457697216-30af8933-3b28-4efe-a2a1-34cb6a5327d1.png)

<font style="color:rgb(51, 51, 51);"> 8、选择安装磁盘，直接回车默认自动分配，需要手动分区的话选择 [custom storage layout]</font>![](../../images/1700457708941-bb83200a-d46d-4133-bf35-b3407119fbf3.png)

<font style="color:rgb(51, 51, 51);"> 检查磁盘分区是否符合你的要求，回车继续</font>

![](../../images/1700457719434-e7156a6d-a12e-4dad-ae14-0779079e7d3e.png)

<font style="color:rgb(51, 51, 51);">再次确认 Continue 继续 </font>

![](../../images/1700457732495-1553e4b5-0922-4f8b-b05e-8f3e1d8fd1b7.png)

<font style="color:rgb(51, 51, 51);">9、设置计算机名、用户名及密码</font>

![](../../images/1700457745971-0dfdbb67-5465-434a-9200-5e594b990806.png)

<font style="color:rgb(51, 51, 51);"> 10、按空格键 选择安装 OpenSSH Server 服务 </font>![](../../images/1700457760277-cd792525-adc7-432e-85ef-a3972a86cc3c.png)<font style="color:rgb(51, 51, 51);">11、选择预置环境，按需选取，不需要则直接选择Done回车继续</font>

<font style="color:rgb(51, 51, 51);">  
</font><font style="color:rgb(51, 51, 51);"> </font>![](../../images/1700457772843-dca85631-6d25-4795-bfcd-30b5081035a2.png)

<font style="color:rgb(51, 51, 51);"> 12、开始安装系统</font>![](../../images/1700457783048-c66afc93-6691-406a-b47f-75c9c3e14531.png)<font style="color:rgb(51, 51, 51);"> 13、直接选择 [reboot Now]不安装更新直接重启</font>![](../../images/1700457793034-d10bfeef-0a4e-4b8e-941b-290710f88afe.png)

<font style="color:rgb(51, 51, 51);">14、输入 账号、密码 后成功登录系统</font>![](../../images/1700457802806-a29c17c0-f7fe-4b16-a8b1-d1a495a91055.png)![](../../images/1700457809332-6e854ed3-d7b5-4ff8-ac13-26ab1397bd51.png)

<font style="color:rgb(51, 51, 51);">到这里就算是简单的安装完成了，可以ping百度官网看看联网是否正常？（CTRL+C退出ping）</font>

<font style="color:rgb(51, 51, 51);">或者安装jdk，配置环境，写代码</font>

<font style="color:rgb(51, 51, 51);">补充设置更新系统</font>

```plain
sudo apt update
sudo apt upgrade
```

## <font style="color:rgb(51, 51, 51);"> 开启root用户登录</font>
```plain
给root账户设置密码
在当前普通用户界面下输入命令:
sudo passwd root
然后按提示两次输入密码即可
修改sshd配置
sudo vim /etc/ssh/sshd_config
按i进入编辑模式，找到#PermitRootLogin prohibit-password，默认是注释掉的。直接在下面添加一行：
PermitRootLogin yes
然后按esc，输入:wq保存并退出。
重启sshd服务
sudo systemctl restart ssh
```

## <font style="color:rgb(51, 51, 51);">修改IP</font>
```plain
1、sudo  vim /etc/netplan/00-installer-config.yaml
备注：编辑yaml 配置文件，注意缩进，否则后面应用就会报错
2、应用配置生效:
sudo netplan apply
```

![](../../images/1700458093777-70796f91-aa34-4e49-8b85-695973cee875.png)

查看计算机当前名称



```shell
hostname
```



编辑配置文件



终端输入：



```shell
sudo vi /etc/hostname
```



临时修改主机名：



```shell
hostname 临时主机名
```



永久修改主机名：



```shell
hostnamectl set-hostname永久主机名 是对/etc/hostname文件的内容进行修改
```

