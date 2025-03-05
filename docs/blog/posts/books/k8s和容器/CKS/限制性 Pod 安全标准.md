**限制性 Pod 安全标准（Pod Security Standards, PSS）** 是 Kubernetes 提供的一种机制，用于控制和管理容器在集群中运行的安全性。这些标准帮助集群管理员定义哪些行为和配置是允许的，哪些是禁止的，从而增强 Pod 和容器的安全性。

在 Kubernetes 中，Pod 安全性被定义为几个级别的标准，这些标准基于 Pod 的配置和行为来评估安全性。通过这些限制性标准，可以防止恶意行为或错误配置对集群的安全性造成风险。

### **Pod 安全标准的三个级别**
Kubernetes 中的 Pod 安全标准分为三个级别：

1. **Privileged**：这是最宽松的安全标准，允许 Pod 执行几乎所有操作，包括所有容器的特权模式、使用 host 网络、暴露敏感端口等。这个级别通常用于不受信任的开发环境中。
2. **Baseline**：这是一个中等严格的标准，限制了一些高风险操作，适用于大多数生产环境。它允许使用某些特权和敏感功能，但限制了可能被滥用的功能。例如，禁止使用特权容器，限制访问宿主机的某些资源。
3. **Restricted**：这是最严格的安全标准，适用于高度安全敏感的环境。这个级别禁止了大部分不安全的操作，只有那些经过严格限制的配置才能通过。例如，禁止容器运行时特权、禁止容器以 root 用户身份运行、禁止暴露敏感端口等。

### **限制性 Pod 安全标准的关键配置项**
1. **运行时安全性**
    - **禁止特权模式容器（Privileged Containers）**：禁止容器运行在特权模式下，这种模式下容器拥有宿主机的几乎所有权限。`Restricted` 模式下会要求所有容器禁止运行特权模式。

```yaml
securityContext:
  privileged: false
```

    - **禁止 root 用户**：容器中的进程不允许以 root 用户身份运行。这减少了容器被攻击者利用后对宿主机的危害。

```yaml
securityContext:
  runAsUser: 1000  # 设置容器内进程的用户
  runAsGroup: 1000  # 设置容器内进程的用户组
  runAsNonRoot: true  # 强制容器以非 root 用户身份运行
```

2. **网络安全性**
    - **禁止使用 host 网络模式**：容器默认运行在自己的网络命名空间中，除非明确指定使用宿主机的网络命名空间。`Restricted` 模式要求禁止容器使用 `hostNetwork`，以减少容器与宿主机之间的网络隔离。

```yaml
spec:
  hostNetwork: false
```

    - **禁止使用 hostPorts**：Pod 中的容器如果暴露特权端口，可能会给系统带来潜在的安全问题。`Restricted` 模式会禁止 Pod 暴露特权端口（如 80、443 等）。
3. **文件系统安全性**
    - **禁止挂载宿主机文件系统**：`Restricted` 模式下不允许挂载宿主机的目录或文件，容器的文件系统应该完全隔离于宿主机。

```yaml
volumes:
  - name: host-mount
    hostPath:
      path: /host/path
      type: Directory
```

    - **只读文件系统**：容器的文件系统尽可能设置为只读，避免容器写入重要的文件或配置。

```yaml
securityContext:
  readOnlyRootFilesystem: true
```

4. **API 安全性**
    - **禁止使用 hostPID 和 hostIPC**：这些选项允许容器访问宿主机的进程和 IPC 命名空间，通常会使容器与宿主机之间的隔离性减弱。`Restricted` 模式下会禁止使用这些功能。

```yaml
spec:
  hostPID: false
  hostIPC: false
```

5. **容器安全性**
    - **使用非 root 用户运行**：容器进程不应该以 root 身份运行，这可以通过配置容器的 `securityContext` 来实现。使用 `runAsNonRoot: true` 确保容器不以 root 用户身份运行。

```yaml
securityContext:
  runAsNonRoot: true
```

    - **容器运行时配置**：在 `Restricted` 模式下，容器的运行时必须符合严格的配置要求，防止可能的权限提升和漏洞利用。例如，不允许容器通过 `CAP_SYS_ADMIN` 等特权能力来提升权限。
6. **容器的镜像安全性**
    - **限制容器镜像的来源**：`Restricted` 模式下，通常会要求容器镜像来自可信的注册中心，并且使用的镜像应该是经过扫描的，确保没有已知的漏洞。
7. **审核与合规性**
    - **启用审计日志**：确保集群启用了审计日志，以便跟踪安全相关的活动，快速发现和响应潜在的安全威胁。
    - **使用容器扫描工具**：如 `Trivy`、`Clair` 等工具扫描容器镜像，以检测镜像中的漏洞和恶意软件。

---

### **实践：如何在 Kubernetes 中应用限制性 Pod 安全标准**
Kubernetes 提供了 **PodSecurityPolicy (PSP)**（已在 Kubernetes 1.21 中弃用，推荐使用 **PodSecurity Admission**）和 **Pod Security Admission** 来实现 Pod 安全标准。

**PodSecurityAdmission** 是 Kubernetes 1.22 版本引入的一个内置功能，旨在实现 Pod 安全标准。它允许用户根据命名空间设置不同级别的 Pod 安全性要求。

#### **启用 PodSecurityAdmission**
首先，确保你的集群启用了 `PodSecurityAdmission` 插件，并在 `Namespace` 中指定安全标准。

1. **创建命名空间并设置安全标准**

```bash
kubectl create namespace alpine
```

1. **为命名空间设置 Pod 安全标准**

你可以使用 `kubectl` 设置不同的安全级别，例如：

```bash
kubectl label namespace alpine pod-security.kubernetes.io/enforce=restricted
kubectl label namespace alpine pod-security.kubernetes.io/enforce-version=v1.24
```

+ `restricted`：最严格的安全标准。
+ `baseline`：适中安全标准。
+ `privileged`：最宽松的安全标准。

通过这种方式，Pod 将在创建时自动应用相应的安全标准，并限制不符合要求的配置。

1. **查看当前命名空间的安全标准**

```bash
kubectl get ns alpine -o=jsonpath='{.metadata.labels.pod-security\.kubernetes\.io/enforce}'
```

#### **示例 Deployment 配置**
假设你希望在 `alpine` 命名空间中运行一个符合 `restricted` 安全标准的 Pod，可以像下面这样配置 Deployment：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: alpine-app
  namespace: alpine
spec:
  replicas: 1
  selector:
    matchLabels:
      app: alpine-app
  template:
    metadata:
      labels:
        app: alpine-app
    spec:
      containers:
        - name: alpine
          image: alpine:3.14.0
          securityContext:
            runAsUser: 1000
            runAsNonRoot: true
            readOnlyRootFilesystem: true
```

在这个配置中，我们确保容器以非 root 用户运行，并且启用了只读文件系统，以符合 `restricted` 安全标准。

---

### **总结**
**限制性 Pod 安全标准** 是 Kubernetes 中的一种安全控制机制，用于限制 Pod 的行为，增强集群的安全性。通过使用不同的安全级别（如 `privileged`、`baseline` 和 `restricted`），管理员可以确保容器的配置符合安全要求，避免潜在的安全漏洞和攻击。

**PodSecurityAdmission** 是 Kubernetes 实现 Pod 安全标准的机制之一，它通过标签来强制要求命名空间内的 Pod 符合指定的安全标准。这是提高 Kubernetes 集群安全性的一项重要实践。

