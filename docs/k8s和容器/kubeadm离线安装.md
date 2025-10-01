[https://kubernetes.io/zh-cn/docs/reference/setup-tools/kubeadm/](https://kubernetes.io/zh-cn/docs/reference/setup-tools/kubeadm/)

## 环境准备
### 环境准备
| 角色 | 操作系统 | IP | CPU | MEM | disk |
| --- | :---: | --- | --- | --- | --- |
| master | Rockey9 | 192.168.107.100 | 4 | 8 | 20+30 |
| node01 | Rockey9 | 192.168.107.101 | 4 | 8 | 20+30 |
| node02 | Rockey9 | 192.168.107.102 | 4 | 8 | 20+30 |


### 下载离线包
```bash

# （版本可以视情况更换成新的）
# 下载containerd
wget https://github.com/containerd/containerd/releases/download/v2.0.5/containerd-2.0.5-linux-amd64.tar.gz
wget https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
# 下载runc
wget https://github.com/opencontainers/runc/releases/download/v1.3.0-rc.2/runc.amd64

# （版本可以视情况更换成新的）
# 下载cni-plugins
wget https://github.com/containernetworking/plugins/releases/download/v1.6.2/cni-plugins-linux-amd64-v1.6.2.tgz

# （版本可以视情况更换成新的）
# 下载crictl
$ wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.25.0/crictl-v1.25.0-linux-amd64.tar.gz



# （版本可以视情况更换成新的）
# 下载kubeadm、kubelet
$ RELEASE="$(curl -sSL https://dl.k8s.io/release/stable.txt)"
$ ARCH="amd64"
$ curl -L --remote-name-all https://dl.k8s.io/release/${RELEASE}/bin/linux/${ARCH}/{kubeadm,kubelet}

# 下载kubectl
$ wget https://storage.googleapis.com/kubernetes-release/release/${RELEASE}/bin/linux/${ARCH}/kubectl

# 下载对应的kubelet.service
RELEASE_VERSION="v0.4.0"
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/kubepkg/templates/latest/deb/kubelet/lib/systemd/system/kubelet.service" | sed "s:/usr/bin:/usr/local/bin:g" | tee kubelet.service

mkdir kubelet.service.d
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/kubepkg/templates/latest/deb/kubeadm/10-kubeadm.conf" | sed "s:/usr/bin:/usr/local/bin:g" | tee kubelet.service.d/10-kubeadm.conf



# 获取镜像列表
$ kubeadm config images list > images.list
# 上传images.list到互联网机器
# 拉取镜像
$ cat images.list | awk '{print $1}' | xargs -L1 docker pull 

# 存成tar
$ docker save -o k8s_images.tgz $(cat images.list | tr -s "\n" " ")



# 下载calico配置文件
$ wget https://raw.githubusercontent.com/projectcalico/calico/release-v3.25/manifests/calico.yaml
# 获取镜像列表
$ cat calico.yaml | grep "image:" | awk "{print $1}" | awk '{print substr($0 ,18)}' | sort | uniq > calico_image.list

# 根据镜像列表拉取镜像
$ cat calico_image.list | awk '{print $1}' | xargs -L1 docker pull

# 镜像导出成压缩包
$ docker save -o cni_images.tgz $(cat calico_image.list | tr -s "\n" " ")

```

### 环境初始化
```bash
#在各自节点配置
echo "k8s-master.liyedong.com" > /etc/hostname
echo "k8s-node01.liyedong.com" > /etc/hostname
echo "k8s-node02.liyedong.com" > /etc/hostname
#配置hosts解析，每台节点执行
echo "192.168.107.100 k8s-master.liyedong.com k8s-master master" >> /etc/hosts
echo "192.168.107.101 k8s-node01.liyedong.com k8s-node01 node01" >> /etc/hosts
echo "192.168.107.102 k8s-node02.liyedong.com k8s-node02 node02" >> /etc/hosts
#配置SSH免密,默认生成即可  master
ssh-keygen
#复制到其他节点
[root@k8s-master ~]# cat /root/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDv4N1oQ88qbYPfwBZQ4PjHW2xbqZx7gdzGGwrasgIwYDMAZeIn4ZFEgm73VMSm+fIUrvgIdKgsRXckati5KtANhKhcCPcMW8iLTB4Tn7ebsW1cKgi1nr9BhXA1p3IjMASp5X58v4gVNBvHRrvYxxL0CH2AB2rPC9DF7WUER4HMkOxAP/9xpM9MH9CsHa23KLPixN9UvJU1LMesilC5shcheaemV7u3IAD8FLLB2EAF4wXPT8AkPrhoCSG8SZyYr7qWiTNeHZJWFnMKUEmHE/2qQ4b4se085Njzh1BSwd3qle6otUYofxEDOKV9Frt1VXN/+gQEw7q9XpynEpzHbf13ZrKHjKKPmRRwSOfXJ2AS4o9a2r97G5GKLDrmauQLD9zKg8BVwtecvUMSjqGShmOdr6pudCzLkAzujP2xMDHoHouz2o0zPUk7ujLQVTYlv5FhsZDlcbIsIbHiR0Cnl0A2OZpsTMaEOtxxkKb5xEE9QNLqP/uwdFM4u3a6FaB5ODU= root@k8s-master.liyedong.com
#复制到master节点和两台node节点
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDv4N1oQ88qbYPfwBZQ4PjHW2xbqZx7gdzGGwrasgIwYDMAZeIn4ZFEgm73VMSm+fIUrvgIdKgsRXckati5KtANhKhcCPcMW8iLTB4Tn7ebsW1cKgi1nr9BhXA1p3IjMASp5X58v4gVNBvHRrvYxxL0CH2AB2rPC9DF7WUER4HMkOxAP/9xpM9MH9CsHa23KLPixN9UvJU1LMesilC5shcheaemV7u3IAD8FLLB2EAF4wXPT8AkPrhoCSG8SZyYr7qWiTNeHZJWFnMKUEmHE/2qQ4b4se085Njzh1BSwd3qle6otUYofxEDOKV9Frt1VXN/+gQEw7q9XpynEpzHbf13ZrKHjKKPmRRwSOfXJ2AS4o9a2r97G5GKLDrmauQLD9zKg8BVwtecvUMSjqGShmOdr6pudCzLkAzujP2xMDHoHouz2o0zPUk7ujLQVTYlv5FhsZDlcbIsIbHiR0Cnl0A2OZpsTMaEOtxxkKb5xEE9QNLqP/uwdFM4u3a6FaB5ODU= root@k8s-master.liyedong.com" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
#master进行测试
ssh node01
ssh node02
#关闭selinux
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
#关闭firewalld
systemctl disable firewalld
systemctl stop firewalld
```

### 部署ansible(支持debian\rhel)
联网下载ansible并且导出环境

```bash
#!/bin/bash
mkdir ansible && cd ansible
# 安装 Miniconda 到本地目录
curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p ./miniconda

# 初始化 conda 环境
source ./miniconda/bin/activate
conda create -y -n ansible-env python=3.9
conda activate ansible-env
pip install \
  ansible==8.7.0 \
  ansible-core==2.15.13 \
  ansible-lint==6.22.2 \
  molecule[docker]==6.0.3 \
  docker==7.1.0 \
  netaddr==1.3.0 \
  jmespath==1.0.1 \
  requests==2.32.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
conda install -y conda-pack
conda-pack -o ansible-env.tar.gz

```

放置到/opt

```bash
#!/bin/bash
#部署
mkdir -p /opt/ansible-env
tar -xzf ansible-env.tar.gz -C /opt/ansible-env
cd /opt/ansible-env
sudo echo "export PATH=/opt/ansible-env/bin:$PATH" > /etc/profile.d/ansible_path.sh
sudo echo "export ANSIBLE_CONFIG=/opt/ansible-env/ansible.cfg" >> /etc/profile.d/ansible_path.sh
source /etc/profile.d/ansible_path.sh
ln -s /opt/ansible-env /opt/ansible
ansible --version
```

初始化配置文件

```bash
cat > /opt/ansible/inventory.ini <<EOF
[node_group]
node01 ansible_host=192.168.107.101 ansible_user=root
node02 ansible_host=192.168.107.102 ansible_user=root
[master_group]
master ansible_host=192.168.107.100 ansible_user=root
EOF
#指定默认的ansible配置文件
cat > /etc/ansible/ansible.cfg <<EOF
[defaults]
inventory = /opt/ansible/inventory.ini
EOF
```

测试

```bash
# 测试 ping
[root@k8s-master ~]# ansible all -m ping
node02 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
node01 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

playbook测试

```yaml
cat > /root/testplaybook.yaml <<EOF
- name: 安装 nginx 并启动
  hosts: node_group
  become: true
  tasks:
    - name: 安装 nginx
      package:
        name: nginx
        state: present
EOF

ansible-playbook  /root/testplaybook.yaml
```

### 配置NTP
这边是rocky的chrony的配置，如果是debian系列的需要修改/etc/chrony.conf，配置文件位置为

```yaml
---
- name: 配置 chronyd 使用阿里云 NTP 服务并检查同步状态
  hosts: all
  become: true
  tasks:

    - name: 安装 chrony
      package:
        name: chrony
        state: present

    - name: 移除默认的 server/pool 设置
      lineinfile:
        path: /etc/chrony.conf
        regexp: '^(pool|server)\s+'
        state: absent
      notify: Restart chronyd

    - name: 添加阿里云 NTP pool
      lineinfile:
        path: /etc/chrony.conf
        line: 'pool ntp.aliyun.com iburst'
        insertafter: BOF
        state: present
      notify: Restart chronyd

    - name: 启用并启动 chronyd 服务
      systemd:
        name: chronyd
        enabled: true
        state: started

    - name: 等待 5 秒钟以便时间同步
      wait_for:
        timeout: 5

    - name: 检查 Chrony 时间同步状态
      command: chronyc tracking
      register: chrony_tracking

    - name: 显示同步状态
      debug:
        var: chrony_tracking.stdout_lines

  handlers:
    - name: Restart chronyd
      systemd:
        name: chronyd
        state: restarted

```





```bash
ansible-playbook aliyun_ntp_chronyd.yaml
...
TASK [显示同步状态] ***************************************************************************************
ok: [node01] => {
    "chrony_tracking.stdout_lines": [
        "Reference ID    : CB6B0658 (203.107.6.88)",
        "Stratum         : 3",
        "Ref time (UTC)  : Sun Apr 20 13:55:01 2025",
        "System time     : 0.000549837 seconds slow of NTP time",
        "Last offset     : -0.000387320 seconds",
        "RMS offset      : 0.002453989 seconds",
        "Frequency       : 18.888 ppm slow",
        "Residual freq   : -2.793 ppm",
        "Skew            : 1.374 ppm",
        "Root delay      : 0.063698597 seconds",
        "Root dispersion : 0.002801374 seconds",
        "Update interval : 65.1 seconds",
        "Leap status     : Normal"
    ]
}
ok: [node02] => {
    "chrony_tracking.stdout_lines": [
        "Reference ID    : CB6B0658 (203.107.6.88)",
        "Stratum         : 3",
        "Ref time (UTC)  : Sun Apr 20 13:55:15 2025",
        "System time     : 0.000167559 seconds slow of NTP time",
        "Last offset     : +0.000329751 seconds",
        "RMS offset      : 0.001446691 seconds",
        "Frequency       : 19.428 ppm slow",
        "Residual freq   : -4.966 ppm",
        "Skew            : 5.579 ppm",
        "Root delay      : 0.068820104 seconds",
        "Root dispersion : 0.002838721 seconds",
        "Update interval : 64.2 seconds",
        "Leap status     : Normal"
    ]
}
ok: [master] => {
    "chrony_tracking.stdout_lines": [
        "Reference ID    : 74CB974A (a.chl.la)",
        "Stratum         : 3",
        "Ref time (UTC)  : Sun Apr 20 13:55:28 2025",
        "System time     : 0.001512848 seconds fast of NTP time",
        "Last offset     : +0.001579409 seconds",
        "RMS offset      : 0.008764669 seconds",
        "Frequency       : 20.859 ppm slow",
        "Residual freq   : +0.663 ppm",
        "Skew            : 13.335 ppm",
        "Root delay      : 0.229020581 seconds",
        "Root dispersion : 0.006072027 seconds",
        "Update interval : 64.1 seconds",
        "Leap status     : Normal"
    ]
}
...
```

## 配置ipvs
### 安装软件包管理
在使用 IPVS 模式之前，还应在节点上安装 `ipset` 等软件包。

依赖软件包（推荐）  
ipset（用于设置 IP 集）

ipvsadm（管理和调试 IPVS）

```bash
# CentOS / RHEL
ansible all -m shell -a "yum install -y ipset ipvsadm"

# Ubuntu / Debian
ansible all -m shell -a "apt install -y ipset ipvsadm"
```



### 导入内核参数以启用ipvs
确保 IPVS 需要内核模块（ **注意** ：对于 Linux 内核 4.19 及更高版本，使用 `nf_conntrack` 而不是 `nf_conntrack_ipv4` ）

查看内核版本

```bash
# uname -a 
Linux k8s-master.liyedong.com 5.14.0-427.13.1.el9_4.x86_64 #1 SMP PREEMPT_DYNAMIC Wed May 1 19:11:28 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux
```

使用nf_conntrack

```bash
ip_vs
ip_vs_rr
ip_vs_wrr
ip_vs_sh
nf_conntrack
```

写入配置文件确保开机自启动

```bash
# 写入配置
ansible all -m shell -a "cat <<EOF | sudo tee /etc/modules-load.d/ipvs.conf 
ip_vs 
ip_vs_rr
ip_vs_wrr
ip_vs_sh
nf_conntrack
EOF"

# 立即加载模块（无需重启）
ansible all -m shell -a "sudo systemctl restart systemd-modules-load.service"

# 验证是否加载成功
ansible all -m shell -a "lsmod | grep -e ip_vs -e nf_conntrack"
```



如果不满足这些要求，Kube-proxy 将回退到 IPTABLES 模式。

### <font style="color:rgb(34, 34, 34);">允许防火墙进行过滤和转发</font>
论是 `iptables` 还是 `ipvs` 模式，这些参数都建议设置：

+ `ipvs` 本质上依然依赖内核中的路由机制和部分 iptables 行为（如初始化连接、防火墙控制）。
+ 特别是在 `bridge` 网络存在时，`net.bridge.*` 系列参数必须开启，确保 Pod 流量能进入 `iptables` 或被 ipvs 接管。

**允许桥接网络（bridge）上的数据包被 iptables 检查与处理**。  

```bash
ansible all -m shell -a "cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
br_netfilter 
EOF"
# 立即加载模块（无需重启）
ansible all -m shell -a "sudo systemctl restart systemd-modules-load.service"

# 验证是否加载成功
ansible all -m shell -a "lsmod | grep -e br_netfilter"
```

**需要导入上面的br_netfilter模块，下面的配置才会生效**

```bash
ansible all -m shell -a "cat > /etc/sysctl.d/ipvs-kubernetes.conf <<EOF
# 开启 IPv4 转发和 bridge 网络支持
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
EOF"
# 立即生效
ansible all -m shell -a "sysctl --system "
ansible all -m shell -a "sysctl -a | grep bridge"
ansible all -m shell -a "sysctl -a | grep net.ipv4.ip_forward"
```

## 安装容器运行时containerd
### <font style="color:rgb(0, 0, 0);">下载contained</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# （版本可以视情况更换成新的）
# 下载containerd
wget https://github.com/containerd/containerd/releases/download/v2.0.5/containerd-2.0.5-linux-amd64.tar.gz
wget https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
# 下载runc
wget https://github.com/opencontainers/runc/releases/download/v1.3.0-rc.2/runc.amd64

```

### <font style="color:rgb(0, 0, 0);">安装containerd</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 上传上一步下载的文件到主节点机器

# 解压containerd程序
$ tar xvf containerd-1.6.18-linux-amd64.tar.gz
$ mv bin/* /usr/local/bin/

# runc程序
$ mv runc.amd64 /usr/local/bin/runc
$ chmod +x /usr/local/bin/runc

# 生成配置文件
$ mkdir -p /etc/containerd
$ containerd config default | tee /etc/containerd/config.toml

# 编辑containerd的配置文件
$ sed -i "s#k8s.gcr.io#registry.cn-hangzhou.aliyuncs.com/google_containers#g"  /etc/containerd/config.toml
$ sed -i 's/SystemdCgroup = false/#SystemdCgroup = false/' /etc/containerd/config.toml
$ sed -i '/containerd.runtimes.runc.options/a\ \ \ \ \ \ \ \ \ \ \ \ SystemdCgroup = true' /etc/containerd/config.toml
$ sed -i "s#https://registry-1.docker.io#https://registry.cn-hangzhou.aliyuncs.com#g"  /etc/containerd/config.toml

# 配置containerd为系统服务
$ cat >/etc/systemd/system/containerd.service <<EOF
# Copyright The containerd Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

[Unit]
Description=containerd container runtime
Documentation=https://containerd.io
After=network.target local-fs.target

[Service]
#uncomment to enable the experimental sbservice (sandboxed) version of containerd/cri integration
#Environment="ENABLE_CRI_SANDBOXES=sandboxed"
ExecStartPre=-/sbin/modprobe overlay
ExecStart=/usr/local/bin/containerd

Type=notify
Delegate=yes
KillMode=process
Restart=always
RestartSec=5
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNPROC=infinity
LimitCORE=infinity
LimitNOFILE=infinity
# Comment TasksMax if your systemd version does not supports it.
# Only systemd 226 and above support this version.
TasksMax=infinity
OOMScoreAdjust=-999

[Install]
WantedBy=multi-user.target
EOF

# 重载systemd配置
$ systemctl daemon-reload

# 设置自启动
$ systemctl enable containerd

# 启动containerd
$ systemctl start containerd

```

## <font style="color:rgb(0, 0, 0);">安装CNI</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# （版本可以视情况更换成新的）
# 下载cni-plugins
wget https://github.com/containernetworking/plugins/releases/download/v1.6.2/cni-plugins-linux-amd64-v1.6.2.tgz
```

+ **<font style="color:rgb(0, 0, 0);">从节点机器</font>**

```bash
# 把cni-plugins程序拷贝过来
$ scp -r k8s-master:/opt/cni /opt

```

## <font style="color:rgb(0, 0, 0);">安装crictl</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# （版本可以视情况更换成新的）
# 下载crictl
$ wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.25.0/crictl-v1.25.0-linux-amd64.tar.gz

```

+ **<font style="color:rgb(0, 0, 0);">从节点机器</font>**

```bash
# 把crictl程序拷贝过来
$ scp k8s-master:/usr/local/bin/crictl /usr/local/bin/

# 把crictl配置文件拷贝过来
$ scp k8s-master:/etc/crictl.yaml /etc/

```

## <font style="color:rgb(0, 0, 0);">安装kubeadm、kubelet、kubectl</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# （版本可以视情况更换成新的）
# 下载kubeadm、kubelet
$ RELEASE="$(curl -sSL https://dl.k8s.io/release/stable.txt)"
$ ARCH="amd64"
$ curl -L --remote-name-all https://dl.k8s.io/release/${RELEASE}/bin/linux/${ARCH}/{kubeadm,kubelet}

# 下载kubectl
$ wget https://storage.googleapis.com/kubernetes-release/release/${RELEASE}/bin/linux/${ARCH}/kubectl

# 下载对应的kubelet.service
RELEASE_VERSION="v0.4.0"
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/kubepkg/templates/latest/deb/kubelet/lib/systemd/system/kubelet.service" | sed "s:/usr/bin:/usr/local/bin:g" | tee kubelet.service

mkdir kubelet.service.d
curl -sSL "https://raw.githubusercontent.com/kubernetes/release/${RELEASE_VERSION}/cmd/kubepkg/templates/latest/deb/kubeadm/10-kubeadm.conf" | sed "s:/usr/bin:/usr/local/bin:g" | tee kubelet.service.d/10-kubeadm.conf

```

+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 上传上面下载的文件到主节点机器

# 给予执行权限
$ chmod +x kubelet kubectl kubeadm
# 移动到系统PATH目录
$ mv kubelet \
	 kubectl \
	 kubeadm /usr/local/bin
# systemd配置文件移动到/etc/systemd/system/目录
$ mv kubelet.service /etc/systemd/system/
$ mv kubelet.service.d /etc/systemd/system/

# 重载systemd配置
$ systemctl daemon-reload

# 设置自启动
$ systemctl enable --now kubelet

# 启动containerd
$ systemctl start kubelet

```

+ **<font style="color:rgb(0, 0, 0);">从节点机器</font>**

```bash
# 拷贝主节点机器程序和systemd到从节点
$ scp k8s-master:/usr/local/bin/kube* /usr/local/bin
$ scp -r k8s-master:/etc/systemd/system/kubelet.service* /etc/systemd/system/

# 重载systemd配置
$ systemctl daemon-reload

# 设置自启动
$ systemctl enable --now kubelet

# 启动containerd
$ systemctl start kubelet

```

## <font style="color:rgb(0, 0, 0);">下载k8s镜像</font>
```bash
# 获取镜像列表
$ kubeadm config images list > images.list
# 上传images.list到互联网机器
# 拉取镜像
$ cat images.list | awk '{print $1}' | xargs -L1 docker pull 

# 存成tar
$ docker save -o k8s_images.tgz $(cat images.list | tr -s "\n" " ")

```

+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# 上传images.list到互联网机器
# 拉取镜像
$ cat images.list | awk '{print $1}' | xargs -L1 docker pull 

# 存成tar
$ docker save -o k8s_images.tgz $(cat images.list | tr -s "\n" " ")

```

+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 上传镜像的压缩包k8s_images.tgz到主节点
# 导入镜像
$ ctr -n k8s.io image import k8s_images.tgz

```

## <font style="color:rgb(0, 0, 0);">kubeadm初始化</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 输出默认初始化配置文件
$ kubeadm config print init-defaults > kubeadm.yaml

# 修改配置文件
$ sed -i "s/kubernetesVersion:/#kubernetesVersion:/" kubeadm.yaml && \
sed -i "s/advertiseAddress: 1.2.3.4/advertiseAddress: $(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | awk 'NR<2{print $1}')/" kubeadm.yaml && \
sed -i "s/name: node/name: k8s-master/" kubeadm.yaml
echo "kubernetesVersion: $(kubeadm version -o short)" >> kubeadm.yaml

# 如果你是用阿里云拉取的镜像，那就需要对应的修改imageRepository，不然会找不到镜像
# sed -i "s#imageRepository: registry.k8s.io#imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers#" kubeadm.yaml

# 执行初始化
$ kubeadm init --config kubeadm.yaml

# 等待初始化完成会输出类似如下内容：

```

+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 设置一个环境变量
$ echo "export KUBECONFIG=/etc/kubernetes/admin.conf" > /etc/profile.d/kube.sh
$ source /etc/profile.d/kube.sh

```

## <font style="color:rgb(0, 0, 0);">安装Pod 网络附加组件</font>
<font style="color:rgb(0, 0, 0);">上面的操作做完coredns还是起不来，必须部署一个基于 Pod 网络插件的 </font>[容器网络接口](https://kubernetes.io/zh-cn/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)<font style="color:rgb(0, 0, 0);"> (CNI)，以便 Pod 可以相互通信，在安装网络之前，集群 DNS (CoreDNS) 不会启动。</font>

### <font style="color:rgb(0, 0, 0);">下载CNI的配置文件</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# 下载calico配置文件
$ wget https://raw.githubusercontent.com/projectcalico/calico/release-v3.25/manifests/calico.yaml
# 获取镜像列表
$ cat calico.yaml | grep "image:" | awk "{print $1}" | awk '{print substr($0 ,18)}' | sort | uniq > calico_image.list

# 根据镜像列表拉取镜像
$ cat calico_image.list | awk '{print $1}' | xargs -L1 docker pull

# 镜像导出成压缩包
$ docker save -o cni_images.tgz $(cat calico_image.list | tr -s "\n" " ")

```

### <font style="color:rgb(0, 0, 0);">拉取对应的镜像</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# 获取镜像列表
$ cat calico.yaml | grep "image:" | awk "{print $1}" | awk '{print substr($0 ,18)}' | sort | uniq > calico_image.list

# 根据镜像列表拉取镜像
$ cat calico_image.list | awk '{print $1}' | xargs -L1 docker pull

# 镜像导出成压缩包
$ docker save -o cni_images.tgz $(cat calico_image.list | tr -s "\n" " ")

```

### <font style="color:rgb(0, 0, 0);">启动calico</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 上传calico配置文件calico.yaml到主节点

# 上传镜像的压缩包cni_images.tgz到主节点
# 导入镜像
$ ctr -n k8s.io image import cni_images.tgz

# kubectl启动calico
$ kubectl apply -f calico.yaml

```

### <font style="color:rgb(0, 0, 0);">验证</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 看看对应的pod都起来没有
$ kubectl -n kube-system get pods

```

## <font style="color:rgb(0, 0, 0);">从节点加入集群</font>
```bash
# 这是kube init的时候系统打印的
# 忘记了就去主节点用这个打印出来
# kubeadm token create --print-join-command
$ kubeadm join <这是个apiserver ip>:6443 --token abcdef.0123456789abcdef \
     --discovery-token-ca-cert-hash sha256:cbe9bd17dbdbeaf4acbf69b485c949f5db9b9ceee00895a2eab5cc9ab54cb4d0

```

## <font style="color:rgb(0, 0, 0);">安装dashboard</font>
### <font style="color:rgb(0, 0, 0);">下载dashboard配置文件</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# 下载calico配置文件
$ wget https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml

```

### <font style="color:rgb(0, 0, 0);">拉取dashboard所需镜像</font>
+ **<font style="color:rgb(0, 0, 0);">互联网机器</font>**

```bash
# 获取镜像列表
$ cat dashboard.yaml | grep "image:" | awk "{print $1}" | awk '{print substr($0 ,18)}' | sort | uniq > dash_image.list

# 根据镜像列表拉取镜像
$ cat dash_image.list | awk '{print $1}' | xargs -L1 docker pull

# 镜像导出成压缩包
$ docker save -o dash_images.tgz $(cat dash_image.list | tr -s "\n" " ")

```

### <font style="color:rgb(0, 0, 0);">部署dashboard</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 上传dashboard配置文件recommended.yaml到主节点

# 上传镜像的压缩包dash_images.tgz到主节点
# 导入镜像
$ ctr -n k8s.io image import dash_images.tgz

# 启动dashboard
$ kubectl apply -f recommended.yaml

```

### <font style="color:rgb(0, 0, 0);">配置dashboard访问</font>
#### <font style="color:rgb(0, 0, 0);">开放访问端口</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 其实还有其他的方式，我这里写一种，配置NodePort方式访问
$ kubectl -n kubernetes-dashboard edit service kubernetes-dashboard

apiVersion: v1
kind: Service
...
...
  ports:
  - nodePort: <端口>
    port: 443
    protocol: TCP
    targetPort: 8443
  selector:
    k8s-app: kubernetes-dashboard
  sessionAffinity: None
  type: NodePort	#修改这一行即可，原为type: ClusterIP
status:
  loadBalancer: {}

```

#### <font style="color:rgb(0, 0, 0);">配置登录密钥</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
# 通过yaml文件创建服务用户Service Account和集群角色权限ClusterRoleBinding

$ cat > dash_accout.yaml <<EOF
# Creating a Service Account
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard

---
# Creating a ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
EOF

```

#### <font style="color:rgb(0, 0, 0);">创建角色</font>
+ **<font style="color:rgb(0, 0, 0);">主节点机器</font>**

```bash
$ kubectl apply -f dash_accout.yaml

```

#### <font style="color:rgb(0, 0, 0);">网页登录</font>
+ **<font style="color:rgb(0, 0, 0);">存在浏览器并与k8s网络通畅的机器</font>**

```bash
# <master-ip>      =>  主节点ip
# <apiserver-port> =>  上面的nodePort: <端口>，这个端口

# 访问https://<master-ip>:<apiserver-port>/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
# 填入上一步获取的token

```

