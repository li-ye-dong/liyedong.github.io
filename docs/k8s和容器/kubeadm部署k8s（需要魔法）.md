## K8S部署
### 环境准备
| 角色 | 操作系统 | IP | CPU | MEM | disk |
| --- | :---: | --- | --- | --- | --- |
| master | Rockey9 | 192.168.107.100 | 4 | 8 | 20+30 |
| node01 | Rockey9 | 192.168.107.101 | 4 | 8 | 20+30 |
| node02 | Rockey9 | 192.168.107.102 | 4 | 8 | 20+30 |


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

### 部署ansible
下载ansible

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

```bash
---
- name: 关闭 firewalld 和 SELinux 并禁止开机自启
  hosts: all
  become: true
  tasks:

    - name: 停止 firewalld 服务
      systemd:
        name: firewalld
        state: stopped
        enabled: false  # 禁止开机自启

    - name: 设置 SELinux 为 disabled（永久）
      replace:
        path: /etc/selinux/config
        regexp: '^SELINUX=.*'
        replace: 'SELINUX=disabled'
      notify: reboot_required

    - name: 立即设置 SELinux 为 permissive（当前生效）
      command: setenforce 0
```

### 开始部署
#### 安装容器运行时和kubelet kubectl kubeadm
```bash
#安装https://github.com/containerd/containerd/blob/main/docs/getting-started.md  containerd

wget https://github.com/containerd/containerd/releases/download/v2.0.5/containerd-2.0.5-linux-amd64.tar.gz
tar Cxzvf /usr/local containerd-2.0.5-linux-amd64.tar.gz
wget https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
mkdir -p /usr/local/lib/systemd/system/
cp containerd.service /usr/local/lib/systemd/system/
systemctl daemon-reload
systemctl enable --now containerd

wget https://github.com/opencontainers/runc/releases/download/v1.3.0-rc.2/runc.amd64
install -m 755 runc.amd64 /usr/local/sbin/runc

wget https://github.com/containernetworking/plugins/releases/download/v1.6.2/cni-plugins-linux-amd64-v1.6.2.tgz
mkdir -p /opt/cni/bin
tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.6.2.tgz
containerd config default > /etc/containerd/config.toml
systemctl daemon-reexec
systemctl restart containerd
#[root@k8s-master ~]# ctr plugins ls | grep cri
#io.containerd.cri.v1                      images                   -              ok        
#io.containerd.cri.v1                      runtime                  linux/amd64    ok        
#io.containerd.grpc.v1                     cri                      -              ok
VERSION="v1.32.0"  # 可根据你的 K8s 版本调整
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/${VERSION}/crictl-${VERSION}-linux-amd64.tar.gz

tar -zxvf crictl-${VERSION}-linux-amd64.tar.gz
mv crictl /usr/bin/
chmod +x /usr/bin/crictl
cat <<EOF > /etc/crictl.yaml
runtime-endpoint: unix:///run/containerd/containerd.sock
image-endpoint: unix:///run/containerd/containerd.sock
timeout: 10
debug: false
EOF

#[root@k8s-master ~]# crictl ps
#CONTAINER           IMAGE               CREATED             STATE               NAME                ATTEMPT           #  POD ID              POD                 NAMESPACE

# 安装kubelet kubectl kubeadm
# 此操作会覆盖 /etc/yum.repos.d/kubernetes.repo 中现存的所有配置
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.32/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.32/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF


sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
sudo systemctl enable --now kubelet



kubeadm config images list
kubeadm config images pull
```



#### 初始化控制平面节点
```bash
[root@k8s-master ~] kubeadm init
...
Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.107.100:6443 --token udwbcq.51486s5osdpygd87 \
        --discovery-token-ca-cert-hash sha256:2bcf34892c13250fcf0e5cee2aa93d23881af79ed25fac5c48c31d1fdb543af7
        
        
        
```

自定义参数

```bash
kubeadm init \
  --apiserver-advertise-address=192.168.31.61 \
  --image-repository registry.aliyuncs.com/google_containers \
  --kubernetes-version v1.20.0 \
  --service-cidr=10.96.0.0/12 \
  --pod-network-cidr=10.244.0.0/16 \
  --ignore-preflight-errors=all

```

• --apiserver-advertise-address 集群通告地址

• --image-repository 由于默认拉取镜像地址k8s.gcr.io国内无法访问，这里指定阿里云镜像仓库地址

• --kubernetes-version K8s版本，与上面安装的一致

• --service-cidr 集群内部虚拟网络，Pod统一访问入口

• --pod-network-cidr Pod网络，，与下面部署的CNI网络组件yaml中保持一致

#### kubeadm详细初始化配置
| 参数 | 描述 | 默认值 |
| --- | --- | --- |
| `--add-dir-header` | 在日志中包含更多目录头部信息，用于调试 | `false` |
| `--dry-run` | 模拟运行，不会实际更改系统，仅显示即将执行的操作 | `false` |
| `--service-cidr` | 指定集群中服务 IP 地址范围，如 `10.96.0.0/12` | `10.96.0.0/12` |
| `--apiserver-advertise-address` | 指定 API 服务器的广告地址 | 自动使用机器的 IP 地址 |
| `--feature-gates` | 启用或禁用 Kubernetes 特性，如 `IPv6DualStack=true` | 无默认值 |
| `--service-dns-domain` | 指定服务的 DNS 域名后缀 | `cluster.local` |
| `--apiserver-bind-port` | API 服务器绑定的端口 | `6443` |
| `--ignore-preflight-errors` | 忽略预检错误，如证书或网络配置错误 | `""`（不忽略错误） |
| `--skip-certificate-key-print` | 跳过打印证书密钥，通常用于自动化部署 | `false` |
| `--apiserver-cert-extra-sans` | 为 API 服务器证书提供额外的 SANs（Subject Alternative Names） | 无默认值 |
| `--image-repository` | 设置镜像仓库地址，默认为 `k8s.gcr.io` | `k8s.gcr.io` |
| `--skip-headers` | 跳过日志输出中的头部信息 | `false` |
| `--skip-phases` | 跳过某些初始化阶段，格式为 `<phase1>,<phase2>` | 无默认值 |
| `--cert-dir` | 指定证书存储目录，默认是 `/etc/kubernetes/pki` | `/etc/kubernetes/pki` |
| `--kubernetes-version` | 指定 Kubernetes 版本，如 `v1.22.0` | `latest` |
| `--skip-token-print` | 跳过在控制台上打印 token | `false` |
| `--config` | 指定配置文件路径，用于自定义初始化参数 | 无默认值 |
| `--patches` | 指定补丁文件路径，修改默认配置 | 无默认值 |
| `--control-plane-endpoint` | 指定控制平面节点的入口点，通常用于负载均衡器 | 无默认值 |
| `--pod-network-cidr` | 指定 Pod 网络的 CIDR 范围 | 无默认值 |
| `--upload-certs` | 允许上传证书，用于新节点加入集群时使用 | `false` |
| `--cri-socket` | 指定 CRI 套接字路径，指向容器运行时的 API 套接字 | 无默认值 |
| `--rootfs` | 指定 kubeadm 初始化过程中使用的根文件系统路径 | 无默认值 |
| `--node-name` | 设置节点的名称 | 自动获取节点名 |
| `--token` | 指定工作节点加入集群时的认证 token | 无默认值 |
| `--token-ttl` | 指定 token 的过期时间，默认为 24 小时 | `24h0m0s` |
| `--v` | 设置日志级别，控制 kubeadm 输出的日志详细程度，范围为 0 到 10 | `0` |


或者使用配置文件引导：

```yaml
kubeadm config print init-defaults
apiVersion: kubeadm.k8s.io/v1beta4
bootstrapTokens:
- groups:
  - system:bootstrappers:kubeadm:default-node-token
  token: abcdef.0123456789abcdef
  ttl: 24h0m0s
  usages:
  - signing
  - authentication
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 1.2.3.4
  bindPort: 6443
nodeRegistration:
  criSocket: unix:///var/run/containerd/containerd.sock
  imagePullPolicy: IfNotPresent
  imagePullSerial: true
  name: node
  taints: null
timeouts:
  controlPlaneComponentHealthCheck: 4m0s
  discovery: 5m0s
  etcdAPICall: 2m0s
  kubeletHealthCheck: 4m0s
  kubernetesAPICall: 1m0s
  tlsBootstrap: 5m0s
  upgradeManifests: 5m0s
---
apiServer: {}
apiVersion: kubeadm.k8s.io/v1beta4
caCertificateValidityPeriod: 87600h0m0s
certificateValidityPeriod: 8760h0m0s
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
controllerManager: {}
dns: {}
encryptionAlgorithm: RSA-2048
etcd:
  local:
    dataDir: /var/lib/etcd
imageRepository: registry.k8s.io
kind: ClusterConfiguration
kubernetesVersion: 1.32.0
networking:
  dnsDomain: cluster.local
  serviceSubnet: 10.96.0.0/12
proxy: {}
scheduler: {}
```



```bash
vi kubeadm.conf
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
kubernetesVersion: v1.20.0
imageRepository: registry.aliyuncs.com/google_containers 
networking:
    podSubnet: 10.244.0.0/16 
    serviceSubnet: 10.96.0.0/12 

kubeadm init --config kubeadm.conf --ignore-preflight-errors=all  
```

导出了 KUBECONFIG, 如果没有执行这句命令，`kubectl` 是不知道如何连接 API Server 的。

```bash
export KUBECONFIG=/etc/kubernetes/admin.conf
echo 'export KUBECONFIG=/etc/kubernetes/admin.conf' >> ~/.bashrc
source ~/.bashrc
#查看节点状态，noready
kubectl get nodes
```

或者拷贝admin.conf到.kube/config下

```plain
初始化完成后，最后会输出一个join命令，先记住，下面用。
拷贝kubectl使用的连接k8s认证文件到默认路径：
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```



#### 初始化网络插件
```bash
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.29.3/manifests/calico.yaml


#等待几分钟后
[root@k8s-master ~]# kubectl get nodes
NAME                      STATUS   ROLES           AGE   VERSION
k8s-master.liyedong.com   Ready    control-plane   31m   v1.32.3
```

#### node节点加入集群
```bash
#查看加入集群的命令
[root@k8s-master ~]# kubeadm token create --print-join-command
kubeadm join 192.168.107.100:6443 --token n9zwpe.ucz0pg5smrmk85kf --discovery-token-ca-cert-hash sha256:2bcf34892c13250fcf0e5cee2aa93d23881af79ed25fac5c48c31d1fdb543af7

#等待几分钟后
[root@k8s-master ~]# kubectl get nodes
NAME                      STATUS   ROLES           AGE    VERSION
k8s-master.liyedong.com   Ready    control-plane   42m    v1.32.3
k8s-node01.liyedong.com   Ready    <none>          118s   v1.32.3
k8s-node02.liyedong.com   Ready    <none>          96s    v1.32.3

#为node节点打上worker标签角色
kubectl label node k8s-node01.liyedong.com node-role.kubernetes.io/worker=worker
kubectl label node k8s-node02.liyedong.com node-role.kubernetes.io/worker=worker


#master节点配置bash补全
echo "source <(kubectl completion bash)" >> ~/.bashrc
echo "source <(kubeadm completion bash)" >> ~/.bashrc
echo "source <(crictl completion bash)" >> ~/.bashrc
source ~/.bashrc
```

#### 测试网络插件
```bash
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=NodePort
kubectl get pods -o wide
[root@k8s-master ~]# kubectl get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP        64m
nginx        NodePort    10.96.43.147   <none>        80:30164/TCP   33s
#验证svc是否成功映射端口
curl node01:30164
curl node02:30164

```

### 启用ipvs在集群
参考：[https://github.com/kubernetes/kubernetes/blob/master/pkg/proxy/ipvs/README.md](https://github.com/kubernetes/kubernetes/blob/master/pkg/proxy/ipvs/README.md)

#### 导入内核参数以启用ipvs
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

#### <font style="color:rgb(34, 34, 34);">允许防火墙进行过滤和转发</font>
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

## 
#### Kubeadm 创建的集群启用ipvs
##### 为初始化之前指定IPVS
如果您使用带有[配置文件的 ](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/#config-file)kubeadm，则必须在 KubeProxyConfiguration 中添加模式：ipvs（以 -- 分隔，也传递给 kubeadm init）。

```yaml
...
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: ipvs
...
```

run之前

```plain
kubeadm init --config <path_to_configuration_file>
```

##### 集群已初始化为 iptables 模式，如何切换成 IPVS？
1. 编辑 kube-proxy 的 ConfigMap：

```bash
kubectl -n kube-system edit configmap kube-proxy
```

找到 `mode: iptables` 改为：

```yaml
mode: ipvs
```

2. 删除当前的 kube-proxy Pod，让其重新拉起生效：

```bash
kubectl -n kube-system delete pod -l k8s-app=kube-proxy
[root@k8s-master ~]# kubectl -n kube-system logs -l k8s-app=kube-proxy --tail 100 | grep ipvs
I0422 16:31:46.968176       1 server_linux.go:231] "Using ipvs Proxier"
I0422 16:32:46.584864       1 server_linux.go:231] "Using ipvs Proxier"
I0422 16:32:05.752752       1 server_linux.go:231] "Using ipvs Proxier"
```

pass:如果kubeadm升级后需要重新指定ipvs，除非初始化的config文件指定这个配置



### 部署helm包管理器
```bash
wget https://get.helm.sh/helm-v3.17.3-linux-amd64.tar.gz
cd /root
tar -zxvf helm-v3.17.3-linux-amd64.tar.gz
mv linux-amd64/helm /usr/local/bin/helm
chmod +x /usr/local/bin/helm


helm version
#配置命令补全
source <(helm completion bash)
source ~/.bashrc
```



打包一组 Helm 离线包 + 常用 Chart

```bash
# 添加 Bitnami 和 Kubernetes 仓库
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add kubernetes https://charts.kubernetes.io/

# 更新仓库索引
helm repo update

# 拉取需要的 Charts
helm search repo ingress-nginx
helm search repo redis
helm search repo metrics-server
helm search repo nginx
helm pull bitnami/nginx --version 19.1.1
helm pull bitnami/redis --version 20.12.1
helm pull bitnami/metrics-server --version 7.4.2
helm pull ingress-nginx/ingress-nginx --version 4.12.1


mkdir -p helm-offline-pack/charts
mv *.tgz helm-offline-pack/charts/
#将多个 Charts 放入一个离线仓库
#helm repo index helm-offline-pack/charts --url http://your-server-ip/charts/

#删除上面测试插件的nginx deployment和svc
kubectl delete svc nginx
kubectl delete deployments.apps nginx
#安装helm的nginx
helm install nginx ./nginx-19.1.1.tgz
[root@k8s-master charts]# kubectl get svc
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP                      99m
nginx        LoadBalancer   10.107.139.13   <pending>     80:32044/TCP,443:31249/TCP   20s
#安装ingress-nginx
helm install ingress-nginx ./ingress-nginx-4.12.1.tgz
[root@k8s-master charts]# kubectl get ingressclasses.networking.k8s.io nginx 
NAME    CONTROLLER             PARAMETERS   AGE
nginx   k8s.io/ingress-nginx   <none>       42s
```

### 部署Meatllb使k8s支持LoadBalancer
MetalLB 是一个 Kubernetes 的网络负载均衡器实现，专门设计来在本地部署或裸金属环境中提供 LoadBalancer 类型的服务。

+ **Kubernetes 原生支持的 Service 类型：**
    - `ClusterIP`：默认，集群内部访问。
    - `NodePort`：通过任意节点的特定端口访问服务。
    - `LoadBalancer`：通常由云服务提供商（如 AWS ELB）提供负载均衡器 IP。

> 在裸机环境下，K8s 本身没有外部负载均衡器，`LoadBalancer` 类型不会生效，这时就需要 MetalLB 来提供这一功能。
>

```bash
# 添加repo源
helm repo add metallb https://metallb.github.io/metallb
[root@k8s-master playbooks]# helm  search repo metallb
NAME            CHART VERSION   APP VERSION     DESCRIPTION                                       
bitnami/metallb 6.4.9           0.14.9          MetalLB is a load-balancer implementation for b...
metallb/metallb 0.14.9          v0.14.9         A network load-balancer implementation for Kube...
# 安装
helm install metallb metallb/metallb --version 0.14.9

#查看pod状态
kubectl get pods | grep metallb


```



```yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: first-pool
spec:
  addresses:
  - 192.168.163.200-192.168.163.220 
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: example
```



```bash
kubectl apply -f meatllb.yaml
```





### 部署yudao 微服务管理系统
#### 制作后端Docker镜像[¶](https://www.ymyw.net/shizhan_01/05.服务容器化/#docker)
后端有3个服务,gateway,system,infra

分别进入各自的子目录,项目自己提供了Dockerfile文件,不需要我们生成。可以更改FROM基于的镜像下载更快。

```plain
 mkdir -p /opt/gitdir
 cd /opt/gitdir
 git clone https://gitee.com/zhijiantianya/yudao-cloud.git
 git checkout v2.1.0\(jdk17/21\)
 mvn clean package -Dmaven.test.skip=true
```



```plain
FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/eclipse-temurin:21-jre
```

之后制作镜像：

```plain
# 制作gateway镜像
cd /opt/gitdir/yudao-cloud/yudao-gateway
docker build -t yudao_gateway .

# 制作system镜像
cd /opt/gitdir/yudao-cloud/yudao-module-system/yudao-module-system-biz
docker build -t yudao_system .

# 制作infra镜像
cd /opt/gitdir/yudao-cloud/yudao-module-infra/yudao-module-infra-biz
docker build -t yudao_infra .

docker tag yudao_infra 192.168.107.128:5000/library/yudao_infra
docker tag yudao_system 192.168.107.128:5000/library/yudao_system
docker tag yudao_gateway 192.168.107.128:5000/library/yudao_gateway
```

制作前端镜像

```bash
pnpm config set registry https://registry.npmmirror.com
git clone https://gitee.com/yudaocode/yudao-ui-admin-vue3.git
cd .\yudao-ui-admin-vue3\
git checkout v2.1.0
 pnpm install
 pnpm build:dev
 
 vim Dockerfile
FROM nginx:1.27
ADD ./dist/ /usr/share/nginx/html/
 
docker build -t yudao_ui_admin .
docker tag yudao_ui_admin 192.168.107.128:5000/library/yudao_ui_admin
```



导出镜像

```bash
docker save -o yudao_ui_admin.tar 192.168.107.128:5000/library/yudao_ui_admin:latest
docker save -o yudao_infra.tar 192.168.107.128:5000/library/yudao_infra:latest
docker save -o yudao_system.tar 192.168.107.128:5000/library/yudao_system:latest
docker save -o yudao_gateway.tar 192.168.107.128:5000/library/yudao_gateway:latest
```

导入到containerd

```bash
scp -r yudao_* node01:/root
scp -r yudao_* node02:/root

ctr -n k8s.io image import /root/yudao_ui_admin.tar
ctr -n k8s.io image import /root/yudao_infra.tar
ctr -n k8s.io image import /root/yudao_system.tar
ctr -n k8s.io image import /root/yudao_gateway.tar
```



#### yudao-gateway-deployment.yaml网关deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: yudao-gateway
  labels:
    app: yudao-gateway
spec:
  replicas: 1
  selector:
    matchLabels:
      app: yudao-gateway
  template:
    metadata:
      labels:
        app: yudao-gateway
    spec:
      containers:
      - name: yudao-gateway
        image: 192.168.107.128:5000/library/yudao_gateway:latest
        imagePullPolicy: IfNotPresent

```

#### yudao-system-deployment.yaml系统deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: yudao-system
  labels:
    app: yudao-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: yudao-system
  template:
    metadata:
      labels:
        app: yudao-system
    spec:
      containers:
      - name: yudao-system
        image: 192.168.107.128:5000/library/yudao_system:latest
        imagePullPolicy: IfNotPresent

```

#### yudao-infray-deployment.yaml基础设施deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: yudao-infra
  labels:
    app: yudao-infra
spec:
  replicas: 1
  selector:
    matchLabels:
      app: yudao-infra
  template:
    metadata:
      labels:
        app: yudao-infra
    spec:
      containers:
      - name: yudao-infra
        image: 192.168.107.128:5000/library/yudao_infra:latest
        imagePullPolicy: IfNotPresent

```

#### yudao-ui-admin-deployment.yaml前端deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: yudao_ui_admin
  labels:
    app: yudao_ui_admin
spec:
  replicas: 1
  selector:
    matchLabels:
      app: yudao-ui-admin
  template:
    metadata:
      labels:
        app: yudao-ui-admin
    spec:
      containers:
      - name: yudao-ui-admin
        image: 192.168.107.128:5000/library/yudao_ui_admin:latest
        imagePullPolicy: IfNotPresent

```

#### svc_yudao.yaml 4层负载svc
```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    app: yudao-gateway
  name: yudao-gateway
spec:
  ports:
  - port: 48080
    protocol: TCP
    targetPort: 48080
  selector:
    app: yudao-gateway
  type: ClusterIP
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: yudao-ui-admin
  name: yudao-ui-admin
spec:
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: yudao-ui-admin
  type: ClusterIP
```

#### ingress_yudao.yaml 7层负载ingress
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  creationTimestamp: null
  name: yudao
spec:
  ingressClassName: nginx
  rules:
  - host: api.liyedong.com
    http:
      paths:
      - backend:
          service:
            name: yudao-gateway
            port:
              number: 48080
        path: /
        pathType: Prefix
  - host: www.liyedong.com
    http:
      paths:
      - backend:
          service:
            name: yudao-ui-admin
            port:
              number: 80
        path: /
        pathType: Prefix
```



增加hosts解析

```plain
192.168.107.200 api.liyedong.com
192.168.107.200 www.liyedong.com
```

访问测试

[www.liyedong.com](http://www.liyedong.com)

## 问题记录
### 集群时间不同步问题修复
```bash
#由于重新配置了时间同步，并且发生了时间变更，导致网络插件的认证token的时间戳失效了
# 所有节点上执行
systemctl restart kubelet

# 然后重启 calico-node
kubectl -n kube-system delete pod -l k8s-app=calico-node

#检查 Calico 是否恢复正常
kubectl get pods -A | grep calico
```

### 证书更新
