## conda打包
使用conda打包兼容性会比较强，缺点是包大小会比较大

使用conda进行build构建，构建出来的的可执行文件不依赖操作系统的glibc版本。但是体积会稍微大点。

```bash
# Linux
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p ./miniconda


tee ${HOME}/.condarc <<EOF
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
EOF
```



```bash
source ./miniconda/bin/activate
conda create -y -n  pan_env python=3.8
conda create -y -n  pan_env python=3.12
conda activate pan_env
pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple
uv pip install requests pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
pyinstaller 

pyinstaller --onefile xxxx.py --hidden-import=requests
```

## 静态链接可执行文件
参考这篇帖子

[https://juejin.cn/post/7369535515291959330](https://juejin.cn/post/7369535515291959330)

使用file查看文件类型可以得到文件的链接方式和架构

```bash
[root@192.168.10.129 Rhel-8.10 dist]$ file disable_dir_edit_perm | tr , "\n"
disable_dir_edit_perm: ELF 64-bit LSB executable
 x86-64
 version 1 (SYSV)
 dynamically linked
 interpreter /lib64/ld-linux-x86-64.so.2
 for GNU/Linux 3.2.0
 BuildID[sha1]=81544629ae0a32249a48b0bc5134fb7b1455adea
 stripped
[root@192.168.10.129 Rhel-8.10 dist]$ file disable_dir_edit_perm_static | tr , "\n"
disable_dir_edit_perm_static: ELF 64-bit LSB executable
 x86-64
 version 1 (SYSV)
 statically linked
 with debug_info
 not stripped
```

使用pyinstaller打包后的二进制可执行文件，使用以下命令查看是否动态链接的libc库

```bash
[root@192.168.10.129 Rhel-8.10 dist]$ ldd disable_dir_edit_perm
        linux-vdso.so.1 (0x00007ffdbc9e7000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fc44b6f9000)
        libz.so.1 => /lib64/libz.so.1 (0x00007fc44b4e1000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fc44b2c1000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fc44aeeb000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fc44b8fd000)
```

如果是静态链接的话，结果如下

```bash
[root@192.168.10.129 Rhel-8.10 dist]$ ldd disable_dir_edit_perm_static 
        not a dynamic executable
```

<font style="color:rgb(37, 41, 51);">安装</font><font style="color:rgb(37, 41, 51);">staticx</font>

```bash
pip install staticx patchelf -i https://pypi.tuna.tsinghua.edu.cn/simple

```

<font style="color:rgb(37, 41, 51);">打包</font>

```bash
staticx test_bin test_static
```

