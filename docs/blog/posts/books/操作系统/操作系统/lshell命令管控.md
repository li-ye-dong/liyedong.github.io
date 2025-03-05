# <font style="color:rgb(31, 35, 40);">lshell（管理用户只能使用某些命令）</font>
[https://github.com/ghantoos/lshell](https://github.com/ghantoos/lshell)

[https://rpm.pbone.net/info_idpl_86080190_distro_redhatel7_com_snapd-devel-2.63-0.el7.noarch.rpm.html](https://rpm.pbone.net/info_idpl_86080190_distro_redhatel7_com_snapd-devel-2.63-0.el7.noarch.rpm.html)

[lshell-0.9.16-5.el7.noarch.rpm.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/40598547/1729506263634-48cca704-a422-4f97-a3a2-e3e0563355d1.txt)

[lshell_0.9.18.tar.gz.txt](https://www.yuque.com/attachments/yuque/0/2024/txt/40598547/1729506263615-4a89ceb6-5e12-4e91-b216-c5b0d470345a.txt)

```shell
vim /etc/lshell.conf #追加插入以下内容
[grp:readonlygroup]
allowed         : ['head', 'tail', 'grep', 'find','stat', 'wc','view','ls','echo','cd','ll','less','more','cat','view','tail', 'grep','wc']
forbidden       : [';', '&', '|','`','>','<', '$(', '${']
warning_counter : 2
aliases         : {'ll':'ls -l', 'vim':'rvim'}
path            : ['/*']
strict          : 0

```

## <font style="color:rgb(31, 35, 40);">lshell——有限的 shell </font>![](../../../images/68747470733a2f2f7472617669732d63692e6f72672f6768616e746f6f732f6c7368656c6c2e7376673f6272616e63683d6d6173746572)
<font style="color:rgb(31, 35, 40);">lshell 是一个用 Python 编写的 shell，它允许您将用户环境限制为有限的命令集，选择启用/禁用通过 SSH 的任何命令（例如 SCP、SFTP、rsync 等），记录用户的命令，实施时间限制等。</font>

<font style="color:rgb(31, 35, 40);">注意：以下所有信息（及更多信息）均可在手册页中找到 -</font>`<font style="color:rgb(31, 35, 40);">man -l man/lshell.1</font>`<font style="color:rgb(31, 35, 40);">或</font>`<font style="color:rgb(31, 35, 40);">man lshell</font>`<font style="color:rgb(31, 35, 40);">)</font>

[https://github.com/ghantoos/lshell](https://github.com/ghantoos/lshell)

[https://github.com/ghantoos/lshell/archive/refs/tags/0.10.tar.gz](https://github.com/ghantoos/lshell/archive/refs/tags/0.10.tar.gz)

## <font style="color:rgb(31, 35, 40);">安装</font>
```shell
#python3.11安装最新版本
pip download wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
#传入需要安装的机器
yum install python3.11 python3.11-pip -y
pip3 install *.wheel
wget https://github.com/ghantoos/lshell/archive/refs/tags/0.10.tar.gz
tar -xzvf lshell-0.10.tar.gz
cd lshell-0.10/
python3 setup.py sdist bdist_wheel
pip3 install .
cp etc/lshell.conf /etc/


#python2安装0.9.18版本
python setup.py install --no-compile --install-scripts=/usr/bin/

```

## <font style="color:rgb(31, 35, 40);">卸载</font>
```shell
pip3 uninstall lshell

pip uninstall lshell

rm -rf /usr/lib/python2.7/site-packages/lshell*
rm -rf /usr/lib/python3.6/site-packages/lshell*
rm -rf /etc/lshell.conf 
rm -rf /usr/local/bin/lshell
rm -rf /usr/bin/lshell
```



## <font style="color:rgb(31, 35, 40);">配置</font>
<font style="color:rgb(31, 35, 40);">lshell.conf 是一个模板配置文件。请参阅 etc/lshell.conf 或 man 文件以了解更多信息。</font>

<font style="color:rgb(31, 35, 40);">所有使用 lshell 的用户都可以使用 [默认] 配置文件。不过，您可以创建 [用户名] 部分或 [grp:groupname] 部分来自定义用户的偏好。</font>

<font style="color:rgb(31, 35, 40);">加载偏好设置时的优先顺序如下：</font>

1. <font style="color:rgb(31, 35, 40);">用户配置</font>
2. <font style="color:rgb(31, 35, 40);">组配置</font>
3. <font style="color:rgb(31, 35, 40);">默认配置</font>

<font style="color:rgb(31, 35, 40);">lshell 的主要目标是能够创建具有 ssh 访问权限的 shell 帐户，并将其环境限制为几个所需的命令和路径。</font>

<font style="color:rgb(31, 35, 40);">例如，用户“foo”和用户“bar”都属于“users”UNIX 组：</font>

+ <font style="color:rgb(31, 35, 40);">用户“foo”： - 必须能够访问 /usr 和 /var，但不能访问 /usr/local - 用户 PATH 中的所有命令，但“su” - 警告计数器设置为 5 - 主路径设置为“/home/users”</font>
+ <font style="color:rgb(31, 35, 40);">用户“bar”： - 必须能够访问 /etc 和 /usr  但不能访问 /usr/local - 允许使用默认命令加上“ping”减去“ls” - 严格性设置为 1（意味着不允许他输入未知命令）</font>

<font style="color:rgb(31, 35, 40);">在这种情况下，我的配置文件将如下所示：</font>

```shell
# CONFIGURATION START
[global]
logpath         : /var/log/lshell/
loglevel        : 2

[default]
allowed         : ['ls','pwd']
forbidden       : [';', '&', '|'] 
warning_counter : 2
timer           : 0
path            : ['/etc', '/usr']
env_path        : ':/sbin:/usr/foo'
scp             : 1 # or 0
sftp            : 1 # or 0
overssh         : ['rsync','ls']
aliases         : {'ls':'ls --color=auto','ll':'ls -l'}

[grp:users]
warning_counter : 5
overssh         : - ['ls']

[foo]
allowed         : 'all' - ['su']
path            : ['/var', '/usr'] - ['/usr/local']
home_path       : '/home/users'

[bar]
allowed         : + ['ping'] - ['ls'] 
path            : - ['/usr/local']
strict          : 1
scpforce        : '/home/bar/uploads/'
# CONFIGURATION END
```

## <font style="color:rgb(31, 35, 40);">用法</font>
<font style="color:rgb(31, 35, 40);">要启动 lshell，只需执行 lshell 并指定配置文件的位置：</font>

```shell
lshell --config /path/to/configuration/file
```

<font style="color:rgb(31, 35, 40);">为了登录用户，您必须将其添加到 lshell 组：</font>

```shell
usermod -aG lshell username
```

<font style="color:rgb(31, 35, 40);">为了配置用户帐户默认使用 lshell，您必须：</font>

```shell
chsh -s /usr/bin/lshell user_name
```

<font style="color:rgb(31, 35, 40);">（您可能需要确保 lshell 在 /etc/shells 中列出）</font>

<font style="color:rgb(31, 35, 40);">在此之后，无论用户使用哪种方法登录他们的帐户，他们最终都将使用您为他们配置的有限 shell！</font>

<font style="color:rgb(31, 35, 40);"></font>

```shell
grep -v ^# /etc/lshell.conf | grep -v ^$
[global]
logpath         : /var/log/lshell/
loglevel        : 2
[default]
allowed = ['ls', 'cat', 'head', 'tail', 'grep', 'find', 'less', 'more', 'stat', 'wc','view']
forbidden       : [';', '&', '|','`','>','<', '$(', '${']
warning_counter : 2
aliases         : {'ll':'ls -l', 'vim':'rvim'}
path            : ['/*']
strict          : 0
```

```shell
groupadd pythongroup
useradd -s /usr/bin/lshell -G pythongroup test1
useradd -s /usr/bin/lshell -G pythongroup test2
groupadd readonlygroup
useradd -s /usr/bin/lshell -G readonlygroup readtest1
useradd -s /usr/bin/lshell -G readonlygroup readtest2
getent group pythongroup
getent group readonlygroup

[global]
logpath         : /var/log/lshell/
loglevel        : 2
[default]
allowed         : ['head', 'tail', 'grep', 'find','stat', 'wc','view','ls','echo','cd','ll','less','more','cat','view','tail', 'grep','wc']
forbidden       : [';', '&', '|','`','>','<', '$(', '${']
warning_counter : 2
aliases         : {'ll':'ls -l', 'vim':'rvim'}
path            : ['/*']
strict          : 0
[grp:pythongroup]
allowed         : ['python']
[grp:readonlygroup]
allowed         : ['head', 'tail', 'grep', 'find','stat', 'wc','view','ls','echo','cd','ll','less','more','cat','view','tail', 'grep','wc']
forbidden       : [';', '&', '|','`','>','<', '$(', '${']
warning_counter : 2
aliases         : {'ll':'ls -l', 'vim':'rvim'}
path            : ['/*']
strict          : 0
```

配置sudo

```shell
groupadd sudogroup
echo "%sudogroup      ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers
usermod -aG sudogroup khread1
usermod -aG sudogroup khread1
#如下
[grp:readonly]
allowed         : ['head', 'tail', 'grep', 'find','stat', 'wc','view','ls','echo','cd','ll','less','more','cat','view','tail', 'grep','wc']
forbidden       : [';', '&', '|','`','>','<', '$(', '${']
warning_counter : 2
sudo_commands   : ['head', 'tail', 'grep', 'find','stat', 'wc','view','ls','echo','cd','ll','less','more','cat','view','tail', 'grep','wc']
aliases         : {'ll':'ls -l', 'vim':'rvim'}
path            : ['/*']
strict          : 0
```

## 配置sudo免密
```shell
vim /etc/sudoers
%readonly       ALL=(ALL)       NOPASSWD: ALL
```

