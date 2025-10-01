## <font style="color:rgb(34, 34, 34);">简介</font>
<font style="color:rgb(34, 34, 34);">Kubernetes（K8s）是强大的容器编排系统，它简化了容器化应用的部署、扩展和管理。通过自动化部署、弹性伸缩和服务发现，K8s确保应用高效稳定运行，极大提升了开发运维效率。</font>

<font style="color:rgb(34, 34, 34);">此次部署采用的是二进制部署一套3master的高可用k8s集群，使用的工具是kubeasz，github地址：</font>[https://github.com/easzlab/kubeasz，kubeasz是使用shell和ansible-playbook结合，极大的简化了二进制部署，并且支持高可用。](https://github.com/easzlab/kubeasz%EF%BC%8Ckubeasz%E6%98%AF%E4%BD%BF%E7%94%A8shell%E5%92%8Cansible-playbook%E7%BB%93%E5%90%88%EF%BC%8C%E6%9E%81%E5%A4%A7%E7%9A%84%E7%AE%80%E5%8C%96%E4%BA%86%E4%BA%8C%E8%BF%9B%E5%88%B6%E9%83%A8%E7%BD%B2%EF%BC%8C%E5%B9%B6%E4%B8%94%E6%94%AF%E6%8C%81%E9%AB%98%E5%8F%AF%E7%94%A8%E3%80%82)

<font style="color:rgb(34, 34, 34);">由于生产环境中一般是内网，kubeasz非常适合离线部署k8s。</font>

## [p-4884785-h-3](https://linux.do/t/topic/527389#p-4884785-h-3)<font style="color:rgb(34, 34, 34);">实验环境</font>
| **主机名** | **CPU** | **Memory** | **IP地址** | **操作系统** | **角色** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| <font style="color:rgb(34, 34, 34);">deploy</font> | <font style="color:rgb(34, 34, 34);">2</font> | <font style="color:rgb(34, 34, 34);">4</font> | <font style="color:rgb(34, 34, 34);">10.0.0.60/24</font> | <font style="color:rgb(34, 34, 34);">Rocky 9.4</font> | <font style="color:rgb(34, 34, 34);">部署节点</font> |
| <font style="color:rgb(34, 34, 34);">master01</font> | <font style="color:rgb(34, 34, 34);">2</font> | <font style="color:rgb(34, 34, 34);">4</font> | <font style="color:rgb(34, 34, 34);">10.0.0.61/24</font> | <font style="color:rgb(34, 34, 34);">Rocky 9.4</font> | <font style="color:rgb(34, 34, 34);">master</font> |
| <font style="color:rgb(34, 34, 34);">master02</font> | <font style="color:rgb(34, 34, 34);">2</font> | <font style="color:rgb(34, 34, 34);">4</font> | <font style="color:rgb(34, 34, 34);">10.0.0.62/24</font> | <font style="color:rgb(34, 34, 34);">Rocky 9.4</font> | <font style="color:rgb(34, 34, 34);">master</font> |
| <font style="color:rgb(34, 34, 34);">master03</font> | <font style="color:rgb(34, 34, 34);">2</font> | <font style="color:rgb(34, 34, 34);">4</font> | <font style="color:rgb(34, 34, 34);">10.0.0.63/24</font> | <font style="color:rgb(34, 34, 34);">Rocky 9.4</font> | <font style="color:rgb(34, 34, 34);">master</font> |
| <font style="color:rgb(34, 34, 34);">node01</font> | <font style="color:rgb(34, 34, 34);">2</font> | <font style="color:rgb(34, 34, 34);">4</font> | <font style="color:rgb(34, 34, 34);">10.0.0.64/24</font> | <font style="color:rgb(34, 34, 34);">Rocky 9.4</font> | <font style="color:rgb(34, 34, 34);">node</font> |
| <font style="color:rgb(34, 34, 34);">node02</font> | <font style="color:rgb(34, 34, 34);">2</font> | <font style="color:rgb(34, 34, 34);">4</font> | <font style="color:rgb(34, 34, 34);">10.0.0.65/24</font> | <font style="color:rgb(34, 34, 34);">Rocky 9.4</font> | <font style="color:rgb(34, 34, 34);">node</font> |
| <font style="color:rgb(34, 34, 34);">node03</font> | <font style="color:rgb(34, 34, 34);">2</font> | <font style="color:rgb(34, 34, 34);">4</font> | <font style="color:rgb(34, 34, 34);">10.0.0.66/24</font> | <font style="color:rgb(34, 34, 34);">Rocky 9.4</font> | <font style="color:rgb(34, 34, 34);">node</font> |


| **组件** | **版本** |
| :---: | :---: |
| <font style="color:rgb(34, 34, 34);">k8s</font> | <font style="color:rgb(34, 34, 34);">v1.32.3</font> |
| <font style="color:rgb(34, 34, 34);">etcd</font> | <font style="color:rgb(34, 34, 34);">v3.5.20</font> |
| <font style="color:rgb(34, 34, 34);">containerd</font> | <font style="color:rgb(34, 34, 34);">2.0.4</font> |
| <font style="color:rgb(34, 34, 34);">runc</font> | <font style="color:rgb(34, 34, 34);">v1.2.6</font> |
| <font style="color:rgb(34, 34, 34);">calico</font> | <font style="color:rgb(34, 34, 34);">v3.28.3</font> |
| <font style="color:rgb(34, 34, 34);">coredns</font> | <font style="color:rgb(34, 34, 34);">1.11.4</font> |
| <font style="color:rgb(34, 34, 34);">cni</font> | <font style="color:rgb(34, 34, 34);">v1.6.2</font> |
| <font style="color:rgb(34, 34, 34);">harbor</font> | <font style="color:rgb(34, 34, 34);">v2.12.2</font> |


## [p-4884785-h-4](https://linux.do/t/topic/527389#p-4884785-h-4)<font style="color:rgb(34, 34, 34);">部署过程</font>
<font style="color:rgb(34, 34, 34);">对k8s服务器进行时间同步配置</font>

```bash
#安装chrony
dnf -y install chrony

#修改配置文件，我这里直接用的aliyun的时间服务器，在内网中要填实际的时间服务器
cat > /etc/chrony.conf <<EOF
server ntp.aliyun.com iburst
stratumweight 0
driftfile /var/lib/chrony/drift
rtcsync
makestep 10 3
bindcmdaddress 127.0.0.1
bindcmdaddress ::1
keyfile /etc/chrony.keys
commandkey 1
generatecommandkey
logchange 0.5
logdir /var/log/chrony
EOF

#配置开机自启并重启chronyd
systemctl enable --now chronyd
```

<font style="color:rgb(34, 34, 34);">确保在干净的系统上开始安装，不要使用曾经装过kubeadm或其他k8s发行版的环境。</font>

<font style="color:rgb(34, 34, 34);">如果是低版本的操作系统，需要升级内核，比如centos7，参考：</font>[kubeasz/docs/guide/kernel_upgrade.md at master · easzlab/kubeasz · GitHub](https://github.com/easzlab/kubeasz/blob/master/docs/guide/kernel_upgrade.md)

<font style="color:rgb(34, 34, 34);">配置deploy节点能免密登录所有k8s节点服务器</font>

```bash
#生成ssh密钥
ssh-keygen

#配置免密
for i in $(seq 60 66); do ssh-copy-id root@10.0.0.$i; done
```

<font style="color:rgb(34, 34, 34);">在一台能够访问互联网环境的服务器上先下载kubeasz工具，然后在通过该工具下载k8s离线文件，然后再将离线文件拷贝到内网环境里的服务器相同目录。</font>

```bash
#下载kubeasz工具
wget https://github.com/easzlab/kubeasz/releases/download/3.6.6/ezdown
chmod +x ezdown

#下载k8s离线文件
./ezdown -D
#输出如下代表下载完成，如果有镜像没下载成功就在执行一次
2025-04-02 16:42:14 [ezdown:772] INFO Action successed: download_all

#上述脚本运行成功后，所有文件（kubeasz代码、二进制、离线镜像）均已整理好放入目录/etc/kubeasz
#将/etc/kubeasz整个目录copy到内网环境中的deploy服务器上的相同位置，执行如下命令检查。
./ezdown -D
```

<font style="color:rgb(34, 34, 34);">在内网deploy服务器上配置、安装k8s</font>

```bash
#运行kubeasz容器和registry容器
./ezdown -S
#容器输出如下
[root@deploy kubeasz]# docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED         STATUS         PORTS     NAMES
05f9d0d6000b   easzlab/kubeasz:3.6.6   "tail -f /dev/null"      4 seconds ago   Up 4 seconds             kubeasz
8b01bb45b767   registry:2              "/entrypoint.sh /etc…"   8 minutes ago   Up 8 minutes             local_registry

#创建新集群 k8s-test
docker exec -it kubeasz ezctl new k8s-test
2025-04-02 16:52:27 [ezctl:145] DEBUG generate custom cluster files in /etc/kubeasz/clusters/k8s-test
2025-04-02 16:52:27 [ezctl:151] DEBUG set versions
2025-04-02 16:52:27 [ezctl:179] DEBUG cluster k8s-test: files successfully created.
2025-04-02 16:52:27 [ezctl:180] INFO next steps 1: to config '/etc/kubeasz/clusters/k8s-test/hosts'
2025-04-02 16:52:27 [ezctl:181] INFO next steps 2: to config '/etc/kubeasz/clusters/k8s-test/config.yml
```

<font style="color:rgb(34, 34, 34);">修改/etc/kubeasz/clusters/k8s-test/hosts文件和/etc/kubeasz/clusters/k8s-test/config.yml文件</font>

```bash
vim /etc/kubeasz/clusters/k8s-test/hosts
#我这里只修改了etcd节点、master节点，node节点的ip和主机名，其他保持默认
# 'etcd' cluster should have odd member(s) (1,3,5,...)
[etcd]
10.0.0.61
10.0.0.62
10.0.0.63

# master node(s), set unique 'k8s_nodename' for each node
# CAUTION: 'k8s_nodename' must consist of lower case alphanumeric characters, '-' or '.',
# and must start and end with an alphanumeric character
[kube_master]
10.0.0.61 k8s_nodename='master01'
10.0.0.62 k8s_nodename='master02'
10.0.0.63 k8s_nodename='master03'

# work node(s), set unique 'k8s_nodename' for each node
# CAUTION: 'k8s_nodename' must consist of lower case alphanumeric characters, '-' or '.',
# and must start and end with an alphanumeric character
[kube_node]
10.0.0.64 k8s_nodename='node01'
10.0.0.65 k8s_nodename='node02'
10.0.0.66 k8s_nodename='node03'

# 这里要确认好，如果没有就安装一个python3
ansible_python_interpreter=/usr/bin/python3
```

```bash
vim /etc/kubeasz/clusters/k8s-test/config.yml

#我这里只修改了这几项,其他默认，按需修改。
# 可选离线安装系统软件包 (offline|online)
INSTALL_SOURCE: "offline"
# kubeconfig 配置参数
CLUSTER_NAME: "k8s-test"
# dashboard 自动安装
dashboard_install: "no"
```

+ <font style="color:rgb(34, 34, 34);">开始安装 该工具支持一键安装，也可以按步骤安装，详细参考</font>[kubeasz/docs/setup/00-planning_and_overall_intro.md at master · easzlab/kubeasz · GitHub](https://github.com/easzlab/kubeasz/blob/master/docs/setup/00-planning_and_overall_intro.md)

```bash
#我这里采用一键安装执行如下命令
docker exec -it kubeasz ezctl setup k8s-test all

#输出如下代表k8s集群已经安装好了。
---
PLAY RECAP ***********************************************************************************************************
10.0.0.61     : ok=119  changed=107  unreachable=0    failed=0    skipped=163  rescued=0    ignored=0
10.0.0.62     : ok=105  changed=94   unreachable=0    failed=0    skipped=134  rescued=0    ignored=0
10.0.0.63     : ok=105  changed=95   unreachable=0    failed=0    skipped=134  rescued=0    ignored=0
10.0.0.64     : ok=79   changed=71   unreachable=0    failed=0    skipped=136  rescued=0    ignored=0
10.0.0.65     : ok=79   changed=71   unreachable=0    failed=0    skipped=136  rescued=0    ignored=0
10.0.0.66     : ok=79   changed=71   unreachable=0    failed=0    skipped=136  rescued=0    ignored=0
localhost     : ok=40   changed=37   unreachable=0    failed=0    skipped=53   rescued=0    ignored=0
```

<font style="color:rgb(34, 34, 34);">此时在master节点执行kubectl命令会报错，需要将deploy节点上的/root/.kube/config文件拷贝到master节点就好了。</font>

```bash
for i in $(seq 61 63); do scp /root/.kube/config root@10.0.0.$i:/root/.kube/; done
```

<font style="color:rgb(34, 34, 34);">这样就可以在master节点上执行kubectl命令管理k8s集群了。</font>

```bash
[root@master01 ~]# kubectl get nodes
NAME       STATUS                     ROLES    AGE     VERSION
master01   Ready,SchedulingDisabled   master   9m1s    v1.32.3
master02   Ready,SchedulingDisabled   master   9m1s    v1.32.3
master03   Ready,SchedulingDisabled   master   9m1s    v1.32.3
node01     Ready                      node     7m27s   v1.32.3
node02     Ready                      node     7m27s   v1.32.3
node03     Ready                      node     7m27s   v1.32.3
```

## [p-4884785-kubeasz-5](https://linux.do/t/topic/527389#p-4884785-kubeasz-5)<font style="color:rgb(34, 34, 34);">分析kubeasz高可用原理</font>
<font style="color:rgb(34, 34, 34);">kubeasz工具会安装一个kube-lb的组件，其实就是一个精简过的nginx，配置文件如下：</font>

```bash
[root@master01 ~]# cat /etc/kube-lb/conf/kube-lb.conf
user root;
worker_processes 1;

error_log  /etc/kube-lb/logs/error.log warn;

events {
    worker_connections  3000;
}

stream {
    upstream backend {
        server 10.0.0.61:6443    max_fails=2 fail_timeout=3s;
        server 10.0.0.62:6443    max_fails=2 fail_timeout=3s;
        server 10.0.0.63:6443    max_fails=2 fail_timeout=3s;
    }

    server {
        listen 127.0.0.1:6443;
        proxy_connect_timeout 1s;
        proxy_pass backend;
    }
}
#配置了一个upstream后端地址是3个master的kube-apiserver地址，监听了本地的127.0.0.1:6443地址，这样当其他组件访问本机的kube-apiserver，就有了负载均衡的功能和高可用的功能。
[root@master01 ~]# ss -ntlp | grep 6443
LISTEN 0      32768      10.0.0.61:6443       0.0.0.0:*    users:(("kube-apiserver",pid=34115,fd=3))
LISTEN 0      511        127.0.0.1:6443       0.0.0.0:*    users:(("kube-lb",pid=31610,fd=5),("kube-lb",pid=31609,fd=5))
```

<font style="color:rgb(34, 34, 34);">当然其他组件也有高可用，可以查看k8s官方文档，要下班了，就先写到这。</font>

**<font style="color:rgb(34, 34, 34);">kubeasz是一个很好用的部署工具，能很快的在内网环境中部署一个高可用的k8s集群。</font>**

