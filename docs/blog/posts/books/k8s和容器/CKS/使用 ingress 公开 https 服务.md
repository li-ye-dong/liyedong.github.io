在 Kubernetes 中，使用 **Ingress** 可以非常方便地将外部流量路由到集群内的服务。为了公开 HTTPS 服务，你需要结合 **Ingress Controller** 和 **TLS Secret** 来配置 HTTPS。在以下步骤中，我将演示如何配置一个简单的 HTTPS 服务通过 Ingress 来公开。

### 步骤概述
1. 配置 **TLS Secret** 来存储证书和私钥。
2. 配置 **Ingress Controller**（例如 NGINX Ingress Controller）来处理流量。
3. 配置 **Ingress 资源** 来暴露 HTTPS 服务。

### 1. 创建 TLS Secret
在 Kubernetes 中，我们使用 `Secret` 来存储 TLS 证书和私钥。你需要将证书和私钥上传到 Kubernetes，并创建一个 `Secret` 来存储这些文件。

假设你有以下文件：

+ `tls.crt`（证书）
+ `tls.key`（私钥）

使用 `kubectl` 命令创建 TLS Secret：

```bash
kubectl create secret tls my-tls-secret --cert=path/to/tls.crt --key=path/to/tls.key
```

这条命令会创建一个名为 `my-tls-secret` 的 Secret，存储了你的 TLS 证书和私钥。

### 2. 部署 Ingress Controller
Ingress Controller 是负责处理集群外部流量的组件。最常用的 Ingress Controller 是 **NGINX**，你可以通过 Helm 或直接安装 NGINX 来完成。

#### 使用 Helm 安装 NGINX Ingress Controller：
```bash
helm install my-ingress ingress-nginx/ingress-nginx
```

你也可以直接通过 YAML 文件安装 NGINX Ingress Controller。可以参考官方文档来进行安装：[NGINX Ingress Controller 安装](https://kubernetes.github.io/ingress-nginx/deploy/)

#### 检查 Ingress Controller 是否安装成功：
```bash
kubectl get pods -n ingress-nginx
```

确保 Ingress Controller Pod 正在运行。

### 3. 配置 Ingress 资源
创建一个 `Ingress` 资源，指向你的服务并启用 HTTPS。

#### 示例：
假设你已经有一个服务叫做 `my-service`，并且它运行在 `default` 命名空间中，监听在 80 端口。

你需要创建一个 Ingress 资源，配置它使用 TLS 并通过 HTTPS 暴露服务。

创建一个 `ingress.yaml` 文件，内容如下：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-https-ingress
  namespace: default
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"  # 强制 HTTPS 重定向
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"  # 强制将所有 HTTP 请求重定向到 HTTPS
spec:
  tls:
  - hosts:
    - myapp.example.com  # 配置 HTTPS 的域名
    secretName: my-tls-secret  # 使用创建的 TLS Secret
  rules:
  - host: myapp.example.com  # 指定的域名
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-service  # 后端服务名称
            port:
              number: 80  # 后端服务的端口
```

#### 关键部分：
+ **tls**：指定 TLS 配置，使用 `my-tls-secret` 作为证书和私钥。 
    - `hosts`：你的 HTTPS 域名，例如 `myapp.example.com`。
    - `secretName`：指向之前创建的 `TLS Secret`。
+ **annotations**： 
    - `nginx.ingress.kubernetes.io/ssl-redirect`：当访问 HTTP 端口时，会自动重定向到 HTTPS。
    - `nginx.ingress.kubernetes.io/force-ssl-redirect`：确保强制执行 HTTPS 重定向。
+ **rules**：定义根据主机名（`myapp.example.com`）和路径（`/`）来路由流量。将流量转发到 `my-service` 服务的 80 端口。

### 4. 应用 Ingress 配置
应用 `ingress.yaml` 文件到 Kubernetes 集群：

```bash
kubectl apply -f ingress.yaml
```

### 5. 配置 DNS
为了确保外部用户能够通过 HTTPS 访问你的应用，你需要将 `myapp.example.com` 的 DNS 记录指向集群的 Ingress Controller 外部负载均衡器的 IP 地址。

可以通过以下命令获取 NGINX Ingress Controller 的外部 IP 地址：

```bash
kubectl get services -o wide -w -n ingress-nginx
```

找到 **LoadBalancer** 类型的服务的外部 IP 地址，然后在 DNS 提供商的管理控制台中配置 `myapp.example.com` 指向该 IP 地址。

### 6. 测试 HTTPS 服务
完成上述配置后，使用浏览器或 `curl` 测试你的 HTTPS 服务：

```bash
curl https://myapp.example.com
```

如果所有配置正确，你应该能够通过 HTTPS 访问你的服务，且浏览器显示锁定图标，表示 HTTPS 连接是安全的。

### 总结
通过 Kubernetes 的 **Ingress** 配置 TLS，能够轻松地将 HTTPS 服务公开到外部。关键步骤包括：

1. 使用 `Secret` 存储证书和私钥。
2. 配置 `Ingress` 资源来处理流量并使用 TLS。
3. 使用 Ingress Controller（如 NGINX）来路由流量。
4. 配置 DNS 将流量定向到集群的外部负载均衡器。

这种方法提供了灵活的流量管理，可以根据需要配置路由、重定向、认证等功能。

