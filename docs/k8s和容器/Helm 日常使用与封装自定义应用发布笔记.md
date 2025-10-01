## 一、Helm 简介
Helm 是 Kubernetes 的包管理工具，类似于 Linux 中的 apt/yum。它将 Kubernetes 中多个资源对象组织成 Chart，方便部署、管理和复用。

## 二、日常使用
### 1. 安装 Helm
离线或在线方式，推荐离线方式：

```bash
# 下载并解压
wget https://get.helm.sh/helm-v3.17.3-linux-amd64.tar.gz
 tar -zxvf helm-v3.17.3-linux-amd64.tar.gz
 mv linux-amd64/helm /usr/local/bin/helm
```

### 2. 启用 bash 补全
```bash
helm completion bash > /etc/bash_completion.d/helm
source /etc/bash_completion.d/helm
```

### 3. 添加仓库
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### 4. 搜索 Chart
```bash
helm search repo nginx
```

### 5. 安装 Chart
```bash
helm install my-nginx bitnami/nginx --version 15.0.0
```

### 6. 查看已安装 Release
```bash
helm list
```

### 7. 升级应用
```bash
helm upgrade my-nginx bitnami/nginx --version 15.0.1
```

### 8. 卸载应用
```bash
helm uninstall my-nginx
```

### 9. 导出配置
```bash
helm get values my-nginx -o yaml > values.yaml
```

---

## 三、自定义应用封装与发布
### 1. 拉取已有 Chart 并解包
```bash
helm pull bitnami/nginx --version 15.0.0 --untar
```

### 2. 修改 Chart 实现自定义
进入 Chart 目录，修改以下内容：

#### 修改镜像
在 `values.yaml` 中：

```yaml
image:
  registry: docker.io
  repository: yourrepo/chat-frontend
  tag: "v1.0.0"
```

#### 修改部署端口等参数
根据需求调整 `values.yaml` 和 `templates/deployment.yaml`。

### 3. 重新打包 Chart
```bash
helm package ./nginx
# 生成 nginx-15.0.0.tgz
```

### 4. 离线部署
将 tgz 包复制到目标主机：

```bash
helm install chat ./nginx-15.0.0.tgz
```

---

## 四、常见问题
### 问题：资源已存在，安装失败
```bash
Error: INSTALLATION FAILED: ... label validation error: missing key "app.kubernetes.io/managed-by": must be set to "Helm"
```

**解决方案：** 删除旧的非 Helm 资源或将资源“导入”Helm 管理。

---

## 五、最佳实践
1. 每个项目维护独立的 Chart 目录，可托管在 Git 仓库中。
2. 通过 `values.yaml` 配置不同环境（dev/staging/prod）。
3. 使用 CI/CD 流程结合 Helm 进行持续部署（如 ArgoCD、GitLab CI）。

---

