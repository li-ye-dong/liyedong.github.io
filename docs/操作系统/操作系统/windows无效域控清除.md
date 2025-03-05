```shell
运行CMD。
在命令提示符下输入ntdsutil。
输入metadata cleanup,可以用？显示帮助。
输入connections,连接到服务器。
输入connet to server 服务器名，连接到具体的服务器。
输入quit，返回到上一级菜单，并输入select operation target 。
输入list sites，列出站点。
输入select site 站点编号，选择站点。
输入list domains in site，列出站点中的域名。
输入select domain 域编号，选择域。
输入list servers in site，列出站点中的域控制器。
输入select server 服务器编号，选择需要清除元数据的服务器。
选择好服务器后，输入quit，返回上一级菜单，输入remove selected server，清除这台服务器的元数据，在弹出框点击是。
成功清除元数据。
从站点和服务器中删除这台服务器。
清除dns残留
```

