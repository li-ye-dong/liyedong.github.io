重启vcenter，按e进入安全模式    

![](../../images/1736932988253-5f34347d-135b-4593-afad-cbb41889e34d.png)

<font style="color:rgb(100, 100, 109);">按F10，启动，使用chpasswd或者passwd 命令修改root密码</font>

<font style="color:rgb(100, 100, 109);">推荐使用以下方式修改，避免因为输入法原因无法修改</font>

```shell
echo "root:password" | chpasswd #适合大部分发行版
umount /
reboot -f
```

![](../../images/1736933004198-ff716afc-dd83-4fd4-9c6f-378e56832f39.png)

<font style="color:rgb(100, 100, 109);">为了规避90天之后又出现同样的无法登录问题，登录https://vcsa_fqdn:5480；系统管理，密码过期设置，编辑，密码到期修改为否。</font>

![](../../images/1736933180062-ab664799-3858-4d50-888b-dc2065a0b6cc.png)

