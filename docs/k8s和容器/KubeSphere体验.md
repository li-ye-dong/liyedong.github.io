# <font style="color:rgb(23, 28, 52);">在 Kubernetes 上快速安装 KubeSphere</font>
<font style="color:rgb(54, 67, 92);">本节介绍如何在单个节点上快速部署 Kubernetes 和 KubeSphere。此安装方法仅适用于测试，若要在生产环境中安装 KubeSphere，请参阅</font>[<font style="color:rgb(54, 67, 92);">安装 Kubernetes 和 KubeSphere</font>](https://kubesphere.io/zh/docs/v4.1/03-installation-and-upgrade/02-install-kubesphere/02-install-kubernetes-and-kubesphere/)<font style="color:rgb(54, 67, 92);">。</font>

## <font style="color:rgb(23, 28, 52);">前提条件</font>
+ <font style="color:rgb(54, 67, 92);">准备一台 Linux 主机，并确保其满足最低硬件要求：CPU > 2 核，内存 > 4 GB， 磁盘空间 > 40 GB。</font>
+ <font style="color:rgb(54, 67, 92);">您需要提前</font>[<font style="color:rgb(54, 67, 92);">安装 Helm</font>](https://helm.sh/zh/docs/intro/install/)<font style="color:rgb(54, 67, 92);">。</font>

## <font style="color:rgb(23, 28, 52);">操作步骤</font>
1. <font style="color:rgb(54, 67, 92);">（可选）如果您没有可用的 Kubernetes 集群，执行以下命令快速创建一个 Kubernetes 集群。</font>
    1. <font style="color:rgb(54, 67, 92);">如果您访问 GitHub/Googleapis 受限，请登录 Linux 主机，执行以下命令设置下载区域。</font>

```bash
export KKZONE=cn
```

    2. <font style="color:rgb(54, 67, 92);">执行以下命令安装⼯具 KubeKey。</font>

<font style="color:rgb(54, 67, 92);">下载完成后当前目录下将生成 KubeKey 二进制文件</font><font style="color:rgb(54, 67, 92);"> </font>**<font style="color:rgb(54, 67, 92);">kk</font>**<font style="color:rgb(54, 67, 92);">。</font>

```bash
curl -sfL https://get-kk.kubesphere.io | sh -
```

    3. <font style="color:rgb(54, 67, 92);">执行以下命令安装依赖项。</font>

```bash
apt install socat conntrack -y
```

    4. <font style="color:rgb(54, 67, 92);">执行以下命令快速创建一个 Kubernetes 集群。</font>

```bash
./kk create cluster --with-local-storage  --with-kubernetes v1.31.0 --container-manager containerd  -y
```

2. <font style="color:rgb(54, 67, 92);">如果您已经拥有可用的 Kubernetes 集群，执行以下命令通过</font><font style="color:rgb(54, 67, 92);"> </font>`<font style="color:rgb(54, 67, 92);">helm</font>`<font style="color:rgb(54, 67, 92);"> </font><font style="color:rgb(54, 67, 92);">安装 KubeSphere 的核心组件 KubeSphere Core。</font>

```bash
helm upgrade --install -n kubesphere-system --create-namespace ks-core https://charts.kubesphere.io/main/ks-core-1.1.3.tgz --debug --wait
```

| **<font style="color:rgb(255, 255, 255);">说明</font>** |
| --- |
| <font style="color:rgb(54, 67, 92);">如果您访问 Docker Hub 受限，请在命令后添加如下配置，修改默认的镜像拉取地址。</font><br/><font style="color:rgb(54, 67, 92);">如果pod出现caclio创建沙箱权限不足，增加 --kubeconfig ~/.kube/config指定kubeconfig提权</font> |


3. <font style="color:rgb(54, 67, 92);">安装完成后，输出信息会显示 KubeSphere Web 控制台的 IP 地址和端口号，默认的 NodePort 是 30880。</font>

```bash
NOTES:
Thank you for choosing KubeSphere Helm Chart.

Please be patient and wait for several seconds for the KubeSphere deployment to complete.

1. Wait for Deployment Completion

    Confirm that all KubeSphere components are running by executing the following command:

    kubectl get pods -n kubesphere-system

2. Access the KubeSphere Console

    Once the deployment is complete, you can access the KubeSphere console using the following URL:

    http://192.168.6.10:30880

3. Login to KubeSphere Console

    Use the following credentials to log in:

    Account: admin
    Password: P@88w0rd

NOTE: It is highly recommended to change the default password immediately after the first login.

For additional information and details, please visit https://kubesphere.io.
```

<font style="color:rgb(54, 67, 92);">执行以下命令检查 Pod 状态。</font>

```bash
kubectl get pods -n kubesphere-system
```

<font style="color:rgb(54, 67, 92);">当 Pod 状态都为</font><font style="color:rgb(54, 67, 92);"> </font>**<font style="color:rgb(54, 67, 92);">Running</font>**<font style="color:rgb(54, 67, 92);"> </font><font style="color:rgb(54, 67, 92);">时，使用默认的账户和密码 (admin/P@88w0rd) 通过 <NodeIP>:30880 访问 KubeSphere Web 控制台。</font>

| **<font style="color:rgb(255, 255, 255);">说明</font>** |
| --- |
| <font style="color:rgb(54, 67, 92);">取决于您的网络环境，您可能需要配置流量转发规则并在防火墙中放行 30880 端口。</font> |


```bash
--set global.imageRegistry=swr.cn-southwest-2.myhuaweicloud.com/ks
```

```bash
--set extension.imageRegistry=swr.cn-southwest-2.myhuaweicloud.com/ks
```

