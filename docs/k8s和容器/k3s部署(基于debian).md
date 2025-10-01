#### <font style="color:rgb(34, 34, 34);">部署vm</font>
<font style="color:rgb(34, 34, 34);">需要准备的资源列表，可酌情调整</font>

| **资源** | **角色** | **备注** |
| --- | --- | --- |
| <font style="color:rgb(34, 34, 34);">master1</font> | <font style="color:rgb(34, 34, 34);">master</font> | <font style="color:rgb(34, 34, 34);">192.168.107.11</font> |
| <font style="color:rgb(34, 34, 34);">master2</font> | <font style="color:rgb(34, 34, 34);">master</font> | <font style="color:rgb(34, 34, 34);">192.168.107.12</font> |
| <font style="color:rgb(34, 34, 34);">master3</font> | <font style="color:rgb(34, 34, 34);">master</font> | <font style="color:rgb(34, 34, 34);">192.168.107.13</font> |
| <font style="color:rgb(34, 34, 34);">worker1</font> | <font style="color:rgb(34, 34, 34);">worker</font> | <font style="color:rgb(34, 34, 34);">192.168.107.14</font> |
| <font style="color:rgb(34, 34, 34);">worker2</font> | <font style="color:rgb(34, 34, 34);">worker</font> | <font style="color:rgb(34, 34, 34);">192.168.107.15</font> |
| <font style="color:rgb(34, 34, 34);">worker3</font> | <font style="color:rgb(34, 34, 34);">worker</font> | <font style="color:rgb(34, 34, 34);">192.168.107.16</font> |
| <font style="color:rgb(34, 34, 34);">vip</font> | <font style="color:rgb(34, 34, 34);">控制平面负载均衡vip</font> | <font style="color:rgb(34, 34, 34);">192.168.107.10</font> |
| <font style="color:rgb(34, 34, 34);">ntp</font> | <font style="color:rgb(34, 34, 34);">提供时钟服务</font> | <font style="color:rgb(34, 34, 34);">10.10.0.1</font> |
| <font style="color:rgb(34, 34, 34);">vm模板</font> | <font style="color:rgb(34, 34, 34);">克隆vm</font> | |


#### 部署ansible
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

scp -r ansible-env.tar.gz root@192.168.107.11:/root
```

部署虚拟环境到其他机器

```bash
#!/bin/bash
#部署
mkdir -p /opt/ansible-env
tar -xzf ansible-env.tar.gz -C /opt/ansible-env
cd /opt/ansible-env
sudo echo "export PATH=/opt/ansible-env/bin:$PATH" > /etc/profile.d/ansible_path.sh
sudo echo "export ANSIBLE_CONFIG=/opt/ansible-env/ansible.cfg" > /etc/profile.d/ansible_cfg_path.sh
source /etc/profile.d/ansible_path.sh
source /etc/profile.d/ansible_cfg_path.sh
ln -s /opt/ansible-env /opt/ansible
ansible --version

#指定默认的ansible配置文件
cat > /opt/ansible-env/ansible.cfg <<EOF
[defaults]
inventory = /opt/ansible-env/inventory.ini
EOF
touch /opt/ansible-env/inventory.ini
```

初始化ansible

```bash
#!/bin/bash
set -e

cat > /opt/ansible/inventory.ini <<EOF
[all]
master1 ansible_host=master1 ansible_user=root
master2 ansible_host=master2 ansible_user=root
master3 ansible_host=master3 ansible_user=root
worker1 ansible_host=worker1 ansible_user=root
worker2 ansible_host=worker2 ansible_user=root
worker3 ansible_host=worker3 ansible_user=root
EOF

# 测试 ping
ansible all -m ping
```

安装docker和containerd

```bash
---
- name: 安装 containerd 并展示版本信息
  hosts: all
  become: true
  tasks:

    - name: 更新 apt 缓存
      ansible.builtin.apt:
        update_cache: yes

    - name: 安装必要的依赖包（ca-certificates、curl 等）
      ansible.builtin.apt:
        name:
          - ca-certificates
          - curl
          - gnupg
          - lsb-release
        state: present

    - name: 添加 Docker 官方 GPG 密钥
      ansible.builtin.shell: |
        mkdir -p /etc/apt/keyrings
        curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
      args:
        creates: /etc/apt/keyrings/docker.gpg

    - name: 添加 Docker 阿里云 apt 仓库（适配 containerd）
      ansible.builtin.apt_repository:
        repo: "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.aliyun.com/docker-ce/linux/debian bullseye stable"
        filename: docker
        state: present
      when: ansible_distribution == "Debian"

    - name: 更新 apt 缓存
      ansible.builtin.apt:
        update_cache: yes

    - name: 安装 containerd
      ansible.builtin.apt:
        name: containerd.io
        state: latest

    - name: 安装 crictl 插件
      ansible.builtin.get_url:
        url: "https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.24.0/crictl-v1.24.0-linux-amd64.tar.gz"
        dest: "/tmp/crictl-v1.24.0-linux-amd64.tar.gz"
      
    - name: 解压 crictl 插件
      ansible.builtin.unarchive:
        src: "/tmp/crictl-v1.24.0-linux-amd64.tar.gz"
        dest: "/usr/local/bin/"
        remote_src: yes

    - name: 配置 containerd 默认配置文件
      ansible.builtin.shell: |
        mkdir -p /etc/containerd
        containerd config default > /etc/containerd/config.toml
      args:
        creates: /etc/containerd/config.toml

    - name: 修改 containerd 配置文件，启用 CRI 插件
      ansible.builtin.lineinfile:
        path: /etc/containerd/config.toml
        regexp: '^disabled_plugins = \[.*\]$'
        line: 'disabled_plugins = []'
        backup: yes

    - name: 创建 crictl 配置文件
      ansible.builtin.copy:
        dest: /etc/crictl.yaml
        content: |
          runtime-endpoint: unix:///run/containerd/containerd.sock
          image-endpoint: unix:///run/containerd/containerd.sock
        owner: root
        group: root
        mode: '0644'

    - name: 重启 containerd 服务以应用配置变更
      ansible.builtin.systemd:
        name: containerd
        state: restarted

    - name: 启动并设置 containerd 开机自启
      ansible.builtin.systemd:
        name: containerd
        enabled: true
        state: started

    - name: 显示 containerd 版本
      ansible.builtin.command:
        cmd: "containerd --version"
      register: containerd_version
      changed_when: false

    - name: 显示 Docker 版本
      ansible.builtin.command:
        cmd: "docker --version"
      register: docker_version
      changed_when: false

    - name: 显示 runtime 版本
      ansible.builtin.command:
        cmd: "crictl --version"
      register: crictl_version
      changed_when: false

    - name: 输出 containerd、docker、crictl 版本
      ansible.builtin.debug:
        msg:
          - "Containerd Version: {{ containerd_version.stdout }}"
          - "Docker Version: {{ docker_version.stdout }}"
          - "CRICTL Version: {{ crictl_version.stdout }}"

```

```yaml
---
- name: 完全卸载 Docker 和 containerd
  hosts: all
  become: true
  tasks:

    - name: 停止 Docker 服务
      ansible.builtin.systemd:
        name: docker
        state: stopped
      ignore_errors: true

    - name: 禁用 Docker 服务开机启动
      ansible.builtin.systemd:
        name: docker
        enabled: false
      ignore_errors: true

    - name: 停止 containerd 服务
      ansible.builtin.systemd:
        name: containerd
        state: stopped
      ignore_errors: true

    - name: 禁用 containerd 服务开机启动
      ansible.builtin.systemd:
        name: containerd
        enabled: false
      ignore_errors: true

    - name: 卸载 Docker 和 containerd 包
      ansible.builtin.apt:
        name:
          - docker.io
          - containerd.io
        state: absent

    - name: 删除 Docker 配置文件
      ansible.builtin.file:
        path: /etc/docker
        state: absent
        recurse: yes

    - name: 删除 containerd 配置文件
      ansible.builtin.file:
        path: /etc/containerd
        state: absent
        recurse: yes

    - name: 删除 Docker 日志文件
      ansible.builtin.file:
        path: /var/log/docker
        state: absent
        recurse: yes

    - name: 删除 containerd 日志文件
      ansible.builtin.file:
        path: /var/log/containerd
        state: absent
        recurse: yes

    - name: 删除 Docker 和 containerd 的缓存目录
      ansible.builtin.file:
        path: /var/lib/docker
        state: absent
        recurse: yes

    - name: 删除 containerd 的缓存目录
      ansible.builtin.file:
        path: /var/lib/containerd
        state: absent
        recurse: yes

    - name: 删除 Docker 二进制文件
      ansible.builtin.file:
        path: /usr/local/bin/docker
        state: absent

    - name: 删除 containerd 二进制文件
      ansible.builtin.file:
        path: /usr/local/bin/containerd
        state: absent

    - name: 删除 crictl 配置文件
      ansible.builtin.file:
        path: /etc/crictl.yaml
        state: absent

    - name: 删除 crictl 二进制文件
      ansible.builtin.file:
        path: /usr/local/bin/crictl
        state: absent

    - name: 确认 Docker 已卸载
      ansible.builtin.command:
        cmd: "docker --version"
      register: docker_version
      changed_when: false
      ignore_errors: true

    - name: 确认 containerd 已卸载
      ansible.builtin.command:
        cmd: "containerd --version"
      register: containerd_version
      changed_when: false
      ignore_errors: true

    - name: 输出 Docker 和 containerd 卸载结果
      ansible.builtin.debug:
        msg:
          - "Docker version: {{ docker_version.stderr }}"
          - "Containerd version: {{ containerd_version.stderr }}"

```



##### 主机名设置
```bash
hostnamectl set-hostname k3s-master1.liyedong.com
hostnamectl set-hostname k3s-master2.liyedong.com
hostnamectl set-hostname k3s-master3.liyedong.com
hostnamectl set-hostname k3s-worker1.liyedong.com
hostnamectl set-hostname k3s-worker2.liyedong.com
hostnamectl set-hostname k3s-worker3.liyedong.com
sed -i 's/template/master1/g' /etc/hosts
sed -i 's/template/master2/g' /etc/hosts
sed -i 's/template/master3/g' /etc/hosts
sed -i 's/template/worker1/g' /etc/hosts
sed -i 's/template/worker2/g' /etc/hosts
sed -i 's/template/worker3/g' /etc/hosts



echo "192.168.107.11 k3s-master1.liyedong.com master1" >> /etc/hosts
echo "192.168.107.12 k3s-master2.liyedong.com master2" >> /etc/hosts
echo "192.168.107.13 k3s-master3.liyedong.com master3" >> /etc/hosts
echo "192.168.107.14 k3s-worker1.liyedong.com worker1" >> /etc/hosts
echo "192.168.107.15 k3s-worker2.liyedong.com worker2" >> /etc/hosts
echo "192.168.107.16 k3s-worker3.liyedong.com worker3" >> /etc/hosts
```



##### <font style="color:rgb(34, 34, 34);">使用govc调用vCenter接口批量部署vm</font>
```bash
#vm克隆
seq 3|xargs -i govc vm.clone -vm /dc/vm/tmpl/tmpl-debian -c 8 -m 16384 -on=false -host esxi.example.com -ds os master{}
seq 3|xargs -i govc vm.clone -vm /dc/vm/tmpl/tmpl-debian -c 16 -m 32768 -on=false -host esxi.example.com -ds os worker{}
#对vm应用虚拟机自定义规范，主要用来自动化设置主机名，或不更新模板来统一设置部分配置
seq 3|xargs -i govc vm.customize -vm /dc/vm/production/k3s/master{} debian
seq 3|xargs -i govc vm.customize -vm /dc/vm/production/k3s/worker{} debian
#对vm附加1T精简制备磁盘
for i in  `govc ls /dc/vm/production/k3s/master*`; do vmname=`echo $i |awk -F/ '{print $NF}'`;govc vm.disk.create -vm $i -name /$vmname/$vmname -size 1T -ds data; done
for i in  `govc ls /dc/vm/production/k3s/worker*`; do vmname=`echo $i |awk -F/ '{print $NF}'`;govc vm.disk.create -vm $i -name /$vmname/$vmname -size 1T -ds data; done
#批量开机
govc ls /dc/vm/production/k3s/|xargs -i govc vm.power -on {}
#不部署vsphere-csi，可跳过
govc ls /dc/vm/k3s/|xargs -i govc vm.change -vm {} -e disk.enableUUID=TRUE
```

#### <font style="color:rgb(34, 34, 34);">系统优化</font>
##### <font style="color:rgb(34, 34, 34);">关闭swap</font>
```bash
ansible k3s -m shell -a "swapoff -a"
ansible k3s -m shell -a "sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab"
```

##### <font style="color:rgb(34, 34, 34);">启用必要模块</font>
```bash
ansible k3s -m shell -a "cat > /etc/modules-load.d/ipvs.conf <<EOF
ip_vs
# 负载均衡调度算法-最少连接
ip_vs_lc
# 负载均衡调度算法-加权最少连接
ip_vs_wlc
# 负载均衡调度算法-轮询
ip_vs_rr
# 负载均衡调度算法-加权轮询
ip_vs_wrr
# 源地址散列调度算法
ip_vs_sh
EOF
cat > /etc/modules-load.d/nf_conntrack.conf <<EOF
nf_conntrack
EOF
cat > /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF"
```

##### <font style="color:rgb(34, 34, 34);">允许防火墙进行过滤和转发</font>
```bash
ansible k3s -m shell -a "cat > /etc/sysctl.d/99-kubernetes-k3s.conf <<EOF
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1 
net.bridge.bridge-nf-call-ip6tables = 1 
EOF"
```

##### <font style="color:rgb(34, 34, 34);">系统软件源公钥导入，</font><font style="color:rgb(34, 34, 34);">跳过</font>
<font style="color:rgb(34, 34, 34);">如果使用公共源，请跳过</font>

```bash
ansible k3s -m shell -a "curl -fsSL https://reg.example.com/api/v2/repositories/debian/keyPairs/primary/public |gpg --dearmor -o   /etc/apt/trusted.gpg.d/example.gpg"
```

##### <font style="color:rgb(34, 34, 34);">软件更新，</font><font style="color:rgb(34, 34, 34);">跳过</font>
```bash
ansible k3s -m apt -a "name=* state=latest"
```

##### <font style="color:rgb(34, 34, 34);">安装chrony(时间同步)</font>
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

```yaml
ansible-playbook ntp.yaml
```

##### <font style="color:rgb(34, 34, 34);">磁盘分区，</font><font style="color:rgb(34, 34, 34);">跳过</font>
```bash
ansible k3s -m shell -a "disk=\$(fdisk -l|grep '1 TiB'|awk -F'[ :]+' '{print \$2}') && parted \$disk mklabel gpt"
ansible k3s -m shell -a "disk=\$(fdisk -l|grep '1 TiB'|awk -F'[ :]+' '{print \$2}') && parted -s \$disk mkpart primary 0 100%"
ansible k3s -m shell -a "disk=\$(fdisk -l|grep '1 TiB'|awk -F'[ :]+' '{print \$2}') && mkfs.ext4 \${disk}1"
ansible k3s -m shell -a "mkdir /data"
ansible k3s -m shell -a "disk=\$(fdisk -l|grep '1 TiB'|awk -F'[ :]+' '{print \$2}') && lsblk -o NAME,UUID \${disk}1|sed -n 2p|awk '{print \$2}'|xargs -i echo 'UUID={} /var/lib/rancher ext4 defaults,usrquota,grpquota 0 0 '>> /etc/fstab"
ansible k3s -m shell -a "systemctl daemon-reload && mount -a && df -Th /var/lib/rancher"
```

#### <font style="color:rgb(34, 34, 34);">部署</font>
配置docker代理

```bash
ansible k3s -m shell -a "mkdir -p /etc/systemd/system/docker.service.d"

ansible k3s -m shell -a "tee /etc/systemd/system/docker.service.d/http-proxy.conf <<EOF
[Service]
Environment="HTTP_PROXY=http://192.168.31.254:7890/"
Environment="HTTPS_PROXY=http://192.168.31.254:7890/"
Environment="NO_PROXY=localhost,127.0.0.1,::1"
EOF"
ansible k3s -m shell -a "systemctl daemon-reload"
ansible k3s -m shell -a "systemctl restart docker"


ansible k3s -m shell -a "mkdir -p /etc/systemd/system/containerd.service.d"

ansible k3s -m shell -a "tee /etc/systemd/system/containerd.service.d/http-proxy.conf <<EOF
[Service]
Environment="HTTP_PROXY=http://192.168.31.254:7890/"
Environment="HTTPS_PROXY=http://192.168.31.254:7890/"
Environment="NO_PROXY=localhost,127.0.0.1,::1"
EOF"
ansible k3s -m shell -a "systemctl daemon-reload"
ansible k3s -m shell -a "systemctl restart containerd"
```

##### <font style="color:rgb(34, 34, 34);">控制平面负载均衡</font>
<font style="color:rgb(34, 34, 34);">实现方式有很多种，比如keepalived+haproxy/nginx 、kube-vip等，这里介绍下kube-vip，如果不想自己生成，直接用下面的即可，注意替换</font>`vip_interface`<font style="color:rgb(34, 34, 34);">，</font>`address`<font style="color:rgb(34, 34, 34);">，</font>`image`<font style="color:rgb(34, 34, 34);">的值</font>

```bash
# 获取最新kube-vip版本
curl -sL https://api.github.com/repos/kube-vip/kube-vip/releases | jq -r ".[0].name" 
# 生成kube-vip清单
--address #虚拟IP用于访问控制平面地址
--interface #设置控制平面所在主机的网卡名称
#生成kube-vip DaemonSet清单
docker run --network host --rm ghcr.io/kube-vip/kube-vip:v0.8.9 manifest daemonset \
    --interface ens33 \
    --address 192.168.107.10 \
    --inCluster \
    --taint \
    --controlplane \
    --services \
    --arp \
    --leaderElection > kube-vip.yaml
```

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  creationTimestamp: null
  labels:
    app.kubernetes.io/name: kube-vip-ds
    app.kubernetes.io/version: v0.8.9
  name: kube-vip-ds
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: kube-vip-ds
  template:
    metadata:
      creationTimestamp: null
      labels:
        app.kubernetes.io/name: kube-vip-ds
        app.kubernetes.io/version: v0.8.9
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: node-role.kubernetes.io/master
                operator: Exists
            - matchExpressions:
              - key: node-role.kubernetes.io/control-plane
                operator: Exists
      containers:
      - args:
        - manager
        env:
        - name: vip_arp
          value: "true"
        - name: port
          value: "6443"
        - name: vip_nodename
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
        - name: vip_interface
          value: ens33
        - name: vip_cidr
          value: "32"
        - name: dns_mode
          value: first
        - name: cp_enable
          value: "true"
        - name: cp_namespace
          value: kube-system
        - name: svc_enable
          value: "true"
        - name: svc_leasename
          value: plndr-svcs-lock
        - name: vip_leaderelection
          value: "true"
        - name: vip_leasename
          value: plndr-cp-lock
        - name: vip_leaseduration
          value: "5"
        - name: vip_renewdeadline
          value: "3"
        - name: vip_retryperiod
          value: "1"
        - name: address
          value: 192.168.107.10
        - name: prometheus_server
          value: :2112
        image: ghcr.io/kube-vip/kube-vip:v0.8.9
        imagePullPolicy: IfNotPresent
        name: kube-vip
        resources: {}
        securityContext:
          capabilities:
            add:
            - NET_ADMIN
            - NET_RAW
      hostNetwork: true
      serviceAccountName: kube-vip
      tolerations:
      - effect: NoSchedule
        operator: Exists
      - effect: NoExecute
        operator: Exists
  updateStrategy: {}
```

<font style="color:rgb(34, 34, 34);">获取RBAC清单，并将</font>`kube-vip.yaml`<font style="color:rgb(34, 34, 34);">和</font>`kube-vip-rbac.yaml`<font style="color:rgb(34, 34, 34);">放到</font>`/var/lib/rancher/k3s/server/manifests`<font style="color:rgb(34, 34, 34);">目录下</font>

```bash
curl https://kube-vip.io/manifests/rbac.yaml > kube-vip-rbac.yaml
```

##### <font style="color:rgb(34, 34, 34);">部署etcd工具</font>
```bash
ansible master -m shell -a "curl -L https://github.com/etcd-io/etcd/releases/download/v3.5.19/etcd-v3.5.19-linux-amd64.tar.gz -o /tmp/etcd-v3.5.19-linux-amd64.tar.gz && tar -xvf /tmp/etcd-v3.5.19-linux-amd64.tar.gz -C /usr/local/bin/ --strip-components=1 etcd-v3.5.19-linux-amd64/etcdctl etcd-v3.5.19-linux-amd64/etcdutl && rm -f /tmp/etcd-v3.5.19-linux-amd64.tar.gz"
#设置别名，方便后续操作etcd
ansible master -m shell -a "echo \"alias etcdctl=\\\"ETCDCTL_API=3 etcdctl --cacert=/var/lib/rancher/k3s/server/tls/etcd/server-ca.crt --cert=/var/lib/rancher/k3s/server/tls/etcd/client.crt --key=/var/lib/rancher/k3s/server/tls/etcd/client.key --endpoints='https://192.168.107.11:2379,https://192.168.107.12:2379,https://192.168.107.13:2379' --write-out=table \\\$@\\\"\" >> ~/.bashrc"
```

##### <font style="color:rgb(34, 34, 34);">部署helm工具</font>
```bash
ansible master -m shell -a "curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash"
```

##### <font style="color:rgb(34, 34, 34);">部署自定义证书</font>
<font style="color:rgb(34, 34, 34);">使用k3s自签证书，请跳过</font>

```bash
#详情访问https://docs.k3s.io/cli/certificate#custom-ca-topology
#提前准备根证书/中间证书用于证书签发,一般为了保护根证书推荐用中间证书
#根证书要求准备好root-ca.key(根证书私钥)、root-ca.pem(根证书) 
#中间证书要求准备好intermediate-ca.key(中间证书私钥)、intermediate-ca.pem(中间证书) 、root-ca.pem(根证书) 
#将准备好的证书拷贝到/var/lib/rancher/k3s/server/tls目录下
ansible master1 -m copy -a "src=/root/k3s dest=/var/lib/rancher/"
#利用脚本生成k3s需要的证书
curl -sL https://github.com/k3s-io/k3s/raw/master/contrib/util/generate-custom-ca-certs.sh | bash -
```

##### <font style="color:rgb(34, 34, 34);">初始化第一个master节点</font>
<font style="color:rgb(34, 34, 34);">这里只介绍本教程涉及的选项，更多选项请访问</font>[官方知识库](https://docs.k3s.io/zh/cli/server#%E5%85%B3%E9%94%AE%E9%85%8D%E7%BD%AE%E5%80%BC)<font style="color:rgb(34, 34, 34);">  
</font>`INSTALL_K3S_VERSION=v1.31.5+k3s1`<font style="color:rgb(34, 34, 34);">：指定要部署的k3s版本，具体版本请访问</font>[官方Github库](https://github.com/k3s-io/k3s)<font style="color:rgb(34, 34, 34);">  
</font>`--disable="traefik,servicelb"`<font style="color:rgb(34, 34, 34);">：禁用自带traefik和servicelb，本教程中会分别用nginx、metallb代替  
</font>`--cluster-cidr="172.25.64.0/18"`<font style="color:rgb(34, 34, 34);">：pod网络的CIDR范围  
</font>`--service-cidr="172.16.64.0/18"`<font style="color:rgb(34, 34, 34);">：服务网络的CIDR范围  
</font>`--tls-san=k3sapi.example.com`<font style="color:rgb(34, 34, 34);">：需要被集群信任的域名、IP，一般这里要填k3s 控制平面负载均衡域名/地址  
</font>`--flannel-backend=none`<font style="color:rgb(34, 34, 34);">：禁用默认flannel，本教程中用calico代替  
</font>`--kube-proxy-arg proxy-mode=ipvs`<font style="color:rgb(34, 34, 34);">：切换kube-proxy为ipvs模式  
</font>`--kube-proxy-arg ipvs-strict-arp=true`<font style="color:rgb(34, 34, 34);">：同上  
</font>`--disable-network-policy`<font style="color:rgb(34, 34, 34);">：禁用默认网络策略控制器  
</font>`--disable-cloud-controller`<font style="color:rgb(34, 34, 34);">：禁用默认云控制管理器  
</font>`--system-default-registry=reg.example.com`<font style="color:rgb(34, 34, 34);">：指定默认镜像仓库  
</font>`--cluster-init`<font style="color:rgb(34, 34, 34);">：初始化一个新集群  
</font><font style="color:rgb(34, 34, 34);">注意使用以下选项暴露服务端口，只是为了让kubesphere监控相关接口并展示相关数据，没有需求的可以去掉  
</font>`--etcd-expose-metrics=true --kube-controller-manager-arg bind-address=0.0.0.0 --kube-proxy-arg metrics-bind-address=0.0.0.0 --kube-scheduler-arg bind-address=0.0.0.0`

<font style="color:rgb(34, 34, 34);">注意：如果指定了私有镜像仓库以进行离线部署或统一部署，安装任何组件时镜像地址都需要指向该镜像仓库，后面不再特别指出</font>

```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.31.5+k3s1 sh -s - server \
  --disable="traefik,servicelb" \
  --cluster-cidr="172.25.64.0/18" \
  --service-cidr="172.16.64.0/18" \
  --tls-san=k3sapi.example.com \
  --flannel-backend=none \
  --disable-network-policy \
  --kube-proxy-arg proxy-mode=ipvs \
  --kube-proxy-arg ipvs-strict-arp=true \
  --disable-cloud-controller \
  --cluster-init

  --system-default-registry=reg.example.com \   
  --etcd-expose-metrics=true \
  --kube-controller-manager-arg bind-address=0.0.0.0 \
  --kube-proxy-arg metrics-bind-address=0.0.0.0 \
  --kube-scheduler-arg bind-address=0.0.0.0 \



ansible k3s -m shell -a "echo '192.168.107.10 k3sapi.example.com' >> /etc/hosts"
```

##### <font style="color:rgb(34, 34, 34);">其他master节点加入集群</font>
<font style="color:rgb(34, 34, 34);">登录master1，获取token</font>

`cat /var/lib/rancher/k3s/server/token`

<font style="color:rgb(34, 34, 34);">除了</font>`--cluster-init`<font style="color:rgb(34, 34, 34);">其他参数与第一个master节点使用参数一致  
</font><font style="color:rgb(34, 34, 34);">--token TOKEN：替换TOKEN为上面获取的token值  
</font><font style="color:rgb(34, 34, 34);">--server</font><font style="color:rgb(34, 34, 34);"> </font>[https://k3sapi.example.com:6443](https://k3sapi.example.com:6443/)<font style="color:rgb(34, 34, 34);">：指定k3s控制平面负载均衡域名/地址</font>

```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.31.5+k3s1 sh -s - server \
  --token K10c492443da4c75326be645a2049fa5e58cb973fe52526f8a491e85cb49135ad28::server:c2ba321df68da888be184cbd40556b2a \
  --disable="traefik,servicelb" \
  --cluster-cidr="172.25.64.0/18" \
  --service-cidr="172.16.64.0/18" \
  --tls-san=k3sapi.example.com \
  --flannel-backend=none \
  --disable-network-policy \
  --kube-proxy-arg proxy-mode=ipvs \
  --kube-proxy-arg ipvs-strict-arp=true \
  --disable-cloud-controller \
  --server https://k3sapi.example.com:6443

  --etcd-expose-metrics=true \
  --kube-controller-manager-arg bind-address=0.0.0.0 \
  --kube-proxy-arg metrics-bind-address=0.0.0.0 \
  --kube-scheduler-arg bind-address=0.0.0.0 \
   # --system-default-registry=reg.example.com \
```

##### <font style="color:rgb(34, 34, 34);">worker节点加入集群</font>
<font style="color:rgb(34, 34, 34);">登录master1，获取token</font>

`cat /var/lib/rancher/k3s/server/token`

```bash
ansible worker -m shell -a "curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.31.5+k3s1 sh -s - agent \
  --token K10c492443da4c75326be645a2049fa5e58cb973fe52526f8a491e85cb49135ad28::server:c2ba321df68da888be184cbd40556b2a \
  --server https://k3sapi.example.com:6443"
```

##### <font style="color:rgb(34, 34, 34);">添加自动补全</font>
```bash
ansible master -m shell -a "echo 'KUBECONFIG=/etc/rancher/k3s/k3s.yaml
source /usr/share/bash-completion/bash_completion
source <(helm completion bash)
source <(kubectl completion bash)' >> ~/.bashrc"
```

##### <font style="color:rgb(34, 34, 34);">为worker打上标签</font>
```bash
kubectl label nodes k3s-worker{1,2,3}.liyedong.com node-role.kubernetes.io/worker=true
```

#### <font style="color:rgb(34, 34, 34);">部署核心组件</font>
##### <font style="color:rgb(34, 34, 34);">部署calico</font>
<font style="color:rgb(34, 34, 34);">注意修改以下calico-node环境变量的值</font>

| **环境变量** | **值** | **备注** |
| --- | --- | --- |
| <font style="color:rgb(34, 34, 34);">IP</font> | <font style="color:rgb(34, 34, 34);">autodetect</font> | |
| <font style="color:rgb(34, 34, 34);">CALICO_IPV4POOL_IPIP</font> | <font style="color:rgb(34, 34, 34);">Always</font> | <font style="color:rgb(34, 34, 34);">开启IPIP模式</font> |
| <font style="color:rgb(34, 34, 34);">CALICO_IPV4POOL_CIDR</font> | <font style="color:rgb(34, 34, 34);">172.25.64.0/18</font> | <font style="color:rgb(34, 34, 34);">POD网络CIDR范围</font> |


```bash
curl -o calico.yaml https://raw.githubusercontent.com/projectcalico/calico/v3.29.2/manifests/calico.yaml
kubectl apply -f calico.yaml
```

##### <font style="color:rgb(34, 34, 34);">部署MetalLB</font>
###### <font style="color:rgb(34, 34, 34);">开启bgp和lb</font>
<font style="color:rgb(34, 34, 34);">注意修改以下字段值</font>

| **字段** | **值** | **备注** |
| --- | --- | --- |
| <font style="color:rgb(34, 34, 34);">addresses</font> | <font style="color:rgb(34, 34, 34);">172.25.16.0/20</font> | <font style="color:rgb(34, 34, 34);">lb网络CIDR范围</font> |
| <font style="color:rgb(34, 34, 34);">ipAddressPools</font> | <font style="color:rgb(34, 34, 34);">ipv4-lb-pool</font> | <font style="color:rgb(34, 34, 34);">与IPAddressPool类声明的名称保持一致</font> |
| <font style="color:rgb(34, 34, 34);">peerAddress</font> | <font style="color:rgb(34, 34, 34);">10.10.0.1</font> | <font style="color:rgb(34, 34, 34);">bgp邻居地址</font> |
| <font style="color:rgb(34, 34, 34);">myASN</font> | <font style="color:rgb(34, 34, 34);">65009</font> | <font style="color:rgb(34, 34, 34);">metallb的AS号</font> |
| <font style="color:rgb(34, 34, 34);">peerASN</font> | <font style="color:rgb(34, 34, 34);">65000</font> | <font style="color:rgb(34, 34, 34);">BGP邻居的AS号</font> |


```bash
kubectl create -f - <<EOF
---
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: ipv4-lb-pool
  namespace: metallb-system
spec:
  addresses:
  - 172.25.16.0/20
---
apiVersion: metallb.io/v1beta1
kind: BGPAdvertisement
metadata:
  name: bgpadvertisement
  namespace: metallb-system
spec:
  ipAddressPools:
  - ipv4-lb-pool
---
apiVersion: metallb.io/v1beta1
kind: BFDProfile
metadata:
  name: bfdprofile
  namespace: metallb-system
spec:
  receiveInterval: 380
  transmitInterval: 270
---
apiVersion: metallb.io/v1beta2
kind: BGPPeer
metadata:
  name: ipv4-bgppeer
  namespace: metallb-system
spec:
  myASN: 65009
  peerASN: 65000
  peerAddress: 10.10.0.1
  bfdProfile: bfdprofile
EOF
```

##### <font style="color:rgb(34, 34, 34);">部署cert-manager</font>
```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.17.0/cert-manager.yaml
```

###### <font style="color:rgb(34, 34, 34);">与openbao/vault集成</font>
<font style="color:rgb(34, 34, 34);">注意以下以openbao为例，因命令基本相同，所以如果你用vault，简单地将bao换成vault即可</font>

<font style="color:rgb(34, 34, 34);">k3s创建服务账户</font>

<font style="color:rgb(34, 34, 34);">注意修改以下字段值，这里以名为vault-auth的服务账户为例，且为了方便创建了vault-issuer作为ClusterIssuer为所有命名空间签发证书，你也可以改为作用于命名空间级别的Issuer</font>

| **字段** | **值** | **备注** |
| --- | --- | --- |
| <font style="color:rgb(34, 34, 34);">server</font> | [https://openbao.example.com](https://openbao.example.com/) | <font style="color:rgb(34, 34, 34);">openbao服务地址</font> |
| <font style="color:rgb(34, 34, 34);">path</font> | <font style="color:rgb(34, 34, 34);">k3s/sign/example-dot-com</font> | <font style="color:rgb(34, 34, 34);">这里path的构成为：openbao中间证书或根证书路径/sign/pki角色名</font> |
| <font style="color:rgb(34, 34, 34);">mountPath</font> | <font style="color:rgb(34, 34, 34);">/v1/auth/kubernetes</font> | <font style="color:rgb(34, 34, 34);">这里path的构成为：/v1/auth/kubernetes认证方式路径</font> |
| <font style="color:rgb(34, 34, 34);">role</font> | <font style="color:rgb(34, 34, 34);">issuer</font> | <font style="color:rgb(34, 34, 34);">openbao中kubernetes认证方式的角色名</font> |
| <font style="color:rgb(34, 34, 34);">secretRef.name</font> | <font style="color:rgb(34, 34, 34);">vault-auth</font> | <font style="color:rgb(34, 34, 34);">认证所需的服务账户名称</font> |


```bash
kubectl create -f - <<EOF
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: vault-auth
  namespace: cert-manager
---
apiVersion: v1
kind: Secret
metadata:
  name: vault-auth
  namespace: cert-manager
  annotations:
    kubernetes.io/service-account.name: vault-auth
type: kubernetes.io/service-account-token
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: role-tokenreview-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
  - kind: ServiceAccount
    name: vault-auth
    namespace: cert-manager
EOF

kubectl create -f - <<EOF
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: vault-issuer
  namespace: cert-manager
spec:
  vault:
    server: https://openbao.example.com
    path: k3s/sign/example-dot-com
    auth:
      kubernetes:
        mountPath: /v1/auth/kubernetes
        role: issuer
        secretRef:
          name: vault-auth
          key: token
EO
```

<font style="color:rgb(34, 34, 34);">openbao/vault创建secrets和认证方式</font>

```bash
export BAO_ADDR=https://openbao.example.com
bao login
#token: hvs.rE5Aaig2sfUUh5HJ2mWB7GeH
#获取服务账户的token
TOKEN_REVIEW_JWT=$(kubectl get secret vault-auth -n cert-manager -o go-template='{{ .data.token }}' | base64 --decode)
#获取集群ca证书
KUBE_CA_CERT=$(kubectl config view --raw --minify --flatten -o jsonpath='{.clusters[].cluster.certificate-authority-data}' | base64 --decode)
#获取控制平面地址
KUBE_API=$(kubectl config view --raw --minify --flatten --output='jsonpath={.clusters[].cluster.server}')
#开启认证方式
bao auth enable kubernetes
bao write auth/kubernetes/config   token_reviewer_jwt="$TOKEN_REVIEW_JWT"   kubernetes_host="$KUBE_API"   kubernetes_ca_cert="$KUBE_CA_CERT" disable_local_ca_jwt="true"
#创建访问策略，注意替换证书路径和角色名称
bao policy write k3s - <<EOF
path "k3s*"                      { capabilities = ["read", "list"] }
path "k3s/sign/example-dot-com"    { capabilities = ["create", "update"] }
path "k3s/issue/example-dot-com"   { capabilities = ["create"] }
}
EOF
#创建认证方式的角色，如果想要限制个别命名空间申请证书，请修改bound_service_account_namespaces为允许的命名空间名称
bao write auth/kubernetes/role/issuer \
  bound_service_account_names=vault-auth \
  bound_service_account_namespaces=* \
  policies=k3s \
  ttl=24h
#登录认证测试
curl \
    --request POST \
    --data '{"jwt": "'$TOKEN_REVIEW_JWT'", "role": "issuer"}' \
    https://openbao.example.com/v1/auth/kubernetes/login
#tls创建测试
kubectl create -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: tls-example-com
spec:
  secretName: tls-example-com
  issuerRef:
    name: vault-issuer
    kind: ClusterIssuer
  commonName: www.example.com
  dnsNames:
  - www.example.com
EOF
#确认是否申请成功，如果失败请检查证书角色是否限制了子域名证书的申请
kubectl describe certificates tls-example-com
```

##### <font style="color:rgb(34, 34, 34);">部署存储</font>
<font style="color:rgb(34, 34, 34);">以下存储根据自身情况择其一部署就行</font>

###### <font style="color:rgb(34, 34, 34);">部署nfs文件系统csi</font>
<font style="color:rgb(34, 34, 34);">注意修改StorageClass为实际nfs服务信息和挂载选项</font>

```bash
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm repo update
helm install csi-driver-nfs csi-driver-nfs/csi-driver-nfs \
    --namespace kube-system \
    --set driver.name="nfs.csi.k8s.io" \
    --set controller.name="csi-nfs-controller" \
    --set rbac.name=nfs \
    --set serviceAccount.controller=csi-nfs-controller-sa \
    --set serviceAccount.node=csi-nfs-node-sa \
    --set node.name=csi-nfs-node \
    --set image.baseRepo=reg.example.com \
    --version v4.10.0 -f nfs-values.yaml
```

###### <font style="color:rgb(34, 34, 34);">部署vsphere块存储csi</font>
<font style="color:rgb(34, 34, 34);">适用于vsphere vsan或vsphere datastore</font>

```bash
helm repo add vsphere-cpi https://kubernetes.github.io/cloud-provider-vsphere
helm repo update
helm upgrade --install vsphere-cpi vsphere-cpi/vsphere-cpi --version 1.31.1 --namespace kube-system -f  vsphere-cpi-values.yaml
kubectl create ns vmware-system-csi
kubectl create secret generic vsphere-config-secret --from-file=csi-vsphere.conf -n vmware-system-csi
kubectl create -f vsphere-csi-driver.yaml
```

###### <font style="color:rgb(34, 34, 34);">部署piraeus文件系统csi</font>
```bash
helm repo add piraeus-charts https://piraeus.io/helm-charts/
helm repo update
helm install snapshot-controller piraeus-charts/snapshot-controller --set controller.image.repository=reg.example.com/sig-storage/snapshot-controller -n kube-system
kubectl apply -f storageclass.yaml
kubectl apply -f snapshotclass.yaml
```

###### <font style="color:rgb(34, 34, 34);">部署pmem存储csi</font>
<font style="color:rgb(34, 34, 34);">注意intel已经不再维护pmem-csi项目，证实其存在逃逸漏洞，且官方支持kubernetes版本为1.22→1.25，这里只做记录，详情请访问</font>[官方知识库](https://intel.github.io/pmem-csi/1.1/README.html)<font style="color:rgb(34, 34, 34);">和</font>[官方仓库](https://github.com/intel/pmem-csi)

```bash
kubectl label node worker{1,2,3} storage=pmem
#部署operator-sdk
export ARCH=$(case $(uname -m) in x86_64) echo -n amd64 ;; aarch64) echo -n arm64 ;; *) echo -n $(uname -m) ;; esac)
export OS=$(uname | awk '{print tolower($0)}')
export OPERATOR_SDK_DL_URL=https://github.com/operator-framework/operator-sdk/releases/download/v1.39.1
curl -LO ${OPERATOR_SDK_DL_URL}/operator-sdk_${OS}_${ARCH}
#部署olm和nfd
operator-sdk olm install
kubectl apply -k https://github.com/kubernetes-sigs/node-feature-discovery/deployment/overlays/default?ref=v0.17.2
#部署完成后确保有pmem存储的机器有"feature.node.kubernetes.io/memory-nv.dax":"true"标签
kubectl get no -o json | jq .items[].metadata.labels
#部署pmem-csi-operator
kubectl create -f https://operatorhub.io/install/pmem-csi-operator.yaml
kubectl label nodes worker{1,2,3} pmem-csi.intel.com/convert-raw-namespaces=force
#部署sc https://github.com/intel/pmem-csi/tree/devel/deploy/kubernetes-1.25
kubectl apply -f direct.yaml
ansible worker -m shell -a "lsblk -f /dev/pmem0"
kubectl get pmemcsideployments
#重置pmem设备
kubectl label nodes data{1,2,3,4} pmem-csi.intel.com/node-
DISK="/dev/pmem0"
sgdisk --zap-all $DISK
dd if=/dev/zero of="$DISK" bs=1M count=100 oflag=direct,dsync
blkdiscard $DISK
ls /dev/mapper/PMEM设备映射 | xargs -I% -- dmsetup remove %
ansible worker -m shell -a "ndctl disable-namespace namespace0.0 && \
ndctl destroy-namespace namespace0.0 && \
ndctl create-namespace -f -e namespace0.0 && \
ndctl list -N"
```

##### <font style="color:rgb(34, 34, 34);">部署kubesphere</font>
```bash
helm upgrade --install -n kubesphere-system --create-namespace ks-core https://charts.kubesphere.io/main/ks-core-1.1.3.tgz --set global.imageRegistry=reg.example.com/ks --set extension.imageRegistry=reg.example.com/ks --debug --wait
#部署ks监控扩展前创建监控组件所需的证书
kubectl -n kubesphere-monitoring-system create secret generic kube-etcd-client-certs  \
 --from-file=etcd-client-ca.crt=/var/lib/rancher/k3s/server/tls/etcd/server-ca.crt  \
 --from-file=etcd-client.crt=/var/lib/rancher/k3s/server/tls/etcd/server-client.crt  \
 --from-file=etcd-client.key=/var/lib/rancher/k3s/server/tls/etcd/server-client.key
```

##### <font style="color:rgb(34, 34, 34);">卸载k3s</font>
```bash
ansible master -m shell -a "k3s-uninstall.sh"
ansible worker -m shell -a  "k3s-agent-uninstall.sh"
```

##### <font style="color:rgb(34, 34, 34);">强制清理资源</font>
```bash
#查看命名空间资源
kubectl api-resources --verbs=list --namespaced -o name|xargs -n 1 kubectl get --show-kind --ignore-not-found -n NAMESPACE
#patch指定资源并删除
kubectl patch crd/kibanas.kibana.k8s.elastic.co -p '{"metadata":{"finalizers":[]}}' --type=merge
#强制删除pod
kubectl delete pod podName -n NAMESPACE --force --grace-period=0
```

