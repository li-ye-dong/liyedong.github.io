# <font style="color:rgb(51, 51, 51);">RHEL网络管理</font>
<font style="color:rgb(51, 51, 51);">修改ip</font>

```plain
vi /etc/sysconfig/network-scripts/ifcfg-ens33
dhcp修改为static
添加
IPADDR=
NETMASK=
GATEWAY=
DNS1=
DNS2=
```

<font style="color:rgb(51, 51, 51);">8以后通过NetworkManager这个服务来管理，可以使用nmcli和nmtui来进行管理</font>

```plain
systemctl status NetworkManager
systemctl start NetworkManager
systemctl enable NetworkManager
```

<font style="color:rgb(51, 51, 51);">重载配置文件</font>

nmcli c reload

<font style="color:rgb(51, 51, 51);">重启网卡，使用以下命令之一：</font>

```plain
nmcli c up ens33  
nmcli d reapply ens33  
nmcli d connect ens33
```

<font style="color:rgb(51, 51, 51);">以上命令中的"ens33"是网卡名称，您可能需要根据实际情况替换为您的网卡名称。执行这些命令后，网络服务应该会被重新启动。</font>

