```bash
# step 1: 安装必要的一些系统工具
sudo yum install -y yum-utils

# Step 2: 添加软件源信息
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/rhel/docker-ce.repo

# Step 3: 安装Docker
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  
# Step 4: 开启Docker服务
sudo service docker start
systemctl start docker
# 注意：
# 官方软件源默认启用了最新的软件，您可以通过编辑软件源的方式获取各个版本的软件包。例如官方并没有将测试版本的软件源置为可用，您可以通过以下方式开启。同理可以开启各种测试版本等。
# vim /etc/yum.repos.d/docker-ce.repo
#   将[docker-ce-test]下方的enabled=0修改为enabled=1
#
# 安装指定版本的Docker-CE:
# Step 1: 查找Docker-CE的版本:
# yum list docker-ce.x86_64 --showduplicates | sort -r
#   Loading mirror speeds from cached hostfile
#   Loaded plugins: branch, fastestmirror, langpacks
#   docker-ce.x86_64            17.03.1.ce-1.el7.centos            docker-ce-stable
#   docker-ce.x86_64            17.03.1.ce-1.el7.centos            @docker-ce-stable
#   docker-ce.x86_64            17.03.0.ce-1.el7.centos            docker-ce-stable
#   Available Packages
# Step2: 安装指定版本的Docker-CE: (VERSION例如上面的17.03.0.ce.1-1.el7.centos)
# sudo yum -y install docker-ce-[VERSION]

systemctl start docker
systemctl enable docker
docker version 
docker images
```

docker-ce-tuna.repo

```bash
[docker-ce-stable]
name=Docker CE Stable - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/$basearch/stable
enabled=1
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-stable-debuginfo]
name=Docker CE Stable - Debuginfo $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/debug-$basearch/stable
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-stable-source]
name=Docker CE Stable - Sources
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/source/stable
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-test]
name=Docker CE Test - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/$basearch/test
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-test-debuginfo]
name=Docker CE Test - Debuginfo $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/debug-$basearch/test
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-test-source]
name=Docker CE Test - Sources
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/source/test
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-nightly]
name=Docker CE Nightly - $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/$basearch/nightly
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-nightly-debuginfo]
name=Docker CE Nightly - Debuginfo $basearch
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/debug-$basearch/nightly
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg

[docker-ce-nightly-source]
name=Docker CE Nightly - Sources
baseurl=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/$releasever/source/nightly
enabled=0
gpgcheck=1
gpgkey=https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/rhel/gpg
```

rocky8-aliyun.repo

```bash
[baseos]
name=Rocky Linux 8 - BaseOS - Alibaba
baseurl=https://mirrors.aliyun.com/rockylinux/8/BaseOS/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/rockylinux/RPM-GPG-KEY-rockyofficial

[appstream]
name=Rocky Linux 8 - AppStream - Alibaba
baseurl=https://mirrors.aliyun.com/rockylinux/8/AppStream/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/rockylinux/RPM-GPG-KEY-rockyofficial

[extras]
name=Rocky Linux 8 - Extras - Alibaba
baseurl=https://mirrors.aliyun.com/rockylinux/8/extras/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=https://mirrors.aliyun.com/rockylinux/RPM-GPG-KEY-rockyofficial

```

```bash
dnf makecache
dnf install docker-ce -y

cat <<EOF | sudo tee /etc/docker/daemon.json > /dev/null
{
  "registry-mirrors": [
    "https://registry.cn-hangzhou.aliyuncs.com"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "live-restore": true,
  "max-concurrent-downloads": 10,
  "max-concurrent-uploads": 5,
  "default-address-pools": [
    {
      "base": "172.30.0.0/16",
      "size": 24
    }
  ],
  "mtu": 1450,
  "features": {
    "buildkit": true
  }
}
EOF
sudo systemctl daemon-reexec
sudo systemctl restart docker
systemctl start docker --now
```

# 注意：
docker 再 2024 5 月发生了国内被墙事件，请切换镜像源

[https://docker.m.daocloud.io/](https://docker.m.daocloud.io/)

总之就是在网上搜可用的镜像源。有条件的可以用梯子

