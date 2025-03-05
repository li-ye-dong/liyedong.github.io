### **任务概述**
在 Kubernetes 集群中，出于安全加固的目的，我们需要配置 Kubernetes API 服务器以禁止匿名身份验证，启用授权模式 `Node` 和 `RBAC`，并使用准入控制器 `NodeRestriction`。此外，我们还需要清理对匿名用户的权限，即删除 `ClusterRoleBinding system:anonymous`。

### **涉及的知识点与概念**
1. **身份验证（Authentication）**
    - **匿名身份验证**：Kubernetes 默认允许通过匿名身份访问 API 服务器，这意味着没有提供有效的身份信息就可以访问集群资源。为了增强集群安全性，禁止匿名访问是必需的。
    - **身份验证模式**：Kubernetes 支持多种身份验证模式，包括： 
        * **证书认证（x509）**
        * **Bearer Token**
        * **Webhook 认证**
    - 在加固集群时，我们将禁用匿名身份验证，确保 API 请求必须经过身份验证。
2. **授权（Authorization）**
    - Kubernetes 提供了多种授权模式来控制用户和服务的权限： 
        * **Node Authorization**：允许节点在 API 服务器上访问集群的相关资源，但仅限于节点自己。
        * **RBAC（Role-Based Access Control）**：基于角色的访问控制，是 Kubernetes 推荐的权限管理机制，通过定义角色和角色绑定来控制权限。
3. **准入控制器（Admission Controllers）**
    - **NodeRestriction**：一个内置的准入控制器，确保节点只能访问与其相关的资源（例如，Pod 和服务）。它是限制节点访问 API 的重要手段。
4. **ClusterRoleBinding system:anonymous**
    - `ClusterRoleBinding system:anonymous` 是将匿名用户与默认的 `ClusterRole` 绑定的资源。它赋予匿名用户访问集群的权限。删除它可以防止未经身份验证的用户访问集群资源。

### **步骤 1: 禁止匿名身份验证**
Kubernetes API 服务器默认启用了匿名身份验证。我们需要禁用它，确保所有请求都必须进行身份验证。

#### **操作：禁用匿名身份验证**
1. 打开 `kube-apiserver` 配置文件。对于使用 `kubeadm` 部署的集群，配置文件通常位于 `/etc/kubernetes/manifests/kube-apiserver.yaml`。

```bash
sudo vi /etc/kubernetes/manifests/kube-apiserver.yaml
```

1. 在 `command` 部分，添加或修改以下参数： 
    - 禁用匿名身份验证：`--anonymous-auth=false`
    - 启用 Bearer Token 认证（通常已经启用）：`--enable-aggregator-routing=true`

```yaml
spec:
  containers:
  - name: kube-apiserver
    command:
    - kube-apiserver
    - --anonymous-auth=false  # 禁止匿名访问
    - --authorization-mode=Node,RBAC  # 启用 Node 和 RBAC 授权模式
    - --admission-control=NodeRestriction  # 启用 NodeRestriction 准入控制器
    ...
```

1. 保存并退出编辑器。`kube-apiserver` 会自动重新加载配置，并应用新的身份验证设置。

---

### **步骤 2: 使用授权模式 Node 和 RBAC**
在 Kubernetes 中，**Node** 授权模式允许节点访问与自己相关的资源（例如，Pod 和服务），而 **RBAC** 用于对集群中所有资源进行细粒度访问控制。

#### **操作：配置授权模式**
1. 在 `kube-apiserver.yaml` 中设置授权模式：

```yaml
spec:
  containers:
  - name: kube-apiserver
    command:
    - kube-apiserver
    - --authorization-mode=Node,RBAC  # 启用 Node 和 RBAC 授权模式
    ...
```

`Node` 模式适用于集群中的节点，它只允许节点访问与自己相关的资源，而 `RBAC` 则为集群提供了全面的权限控制，基于角色和角色绑定来授权访问。

1. **RBAC 配置**： 
    - 使用 `kubectl` 创建 `Role`、`ClusterRole` 和 `RoleBinding` 或 `ClusterRoleBinding` 来定义和绑定权限。
2.  例如，创建一个用户角色并授予其对 Pod 资源的访问权限：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
```

创建一个 `ClusterRoleBinding` 将该角色绑定到某个用户：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: pod-reader-binding
subjects:
- kind: User
  name: "user_name"  # 用户名
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

---

### **步骤 3: 使用准入控制器 NodeRestriction**
**NodeRestriction** 是 Kubernetes 的一个内置准入控制器，它限制了节点只能访问与自己相关的资源。具体来说，节点只能获取和更新与自己所在节点相关的 Pod 和节点资源。

#### **操作：启用 NodeRestriction 准入控制器**
1. 确保 `kube-apiserver.yaml` 中包含以下设置：

```yaml
spec:
  containers:
  - name: kube-apiserver
    command:
    - kube-apiserver
    - --admission-control=NodeRestriction  # 启用 NodeRestriction
    ...
```

NodeRestriction 控制器会在创建和更新资源时执行验证，确保节点只能够访问与它自己相关的资源。

---

### **步骤 4: 删除 ClusterRoleBinding system:anonymous**
在默认情况下，`system:anonymous` 用户被赋予了集群角色绑定，允许未经身份验证的用户访问集群资源。为了增强安全性，我们需要删除这个绑定。

#### **操作：删除 **`**ClusterRoleBinding system:anonymous**`
1. 运行以下命令删除 `ClusterRoleBinding`：

```bash
kubectl delete clusterrolebinding system:anonymous
```

这将删除对匿名用户的所有授权。

---

### **步骤 5: 测试与验证**
完成上述配置后，集群的 API 服务器已经禁止了匿名身份验证，并启用了授权模式 `Node` 和 `RBAC`，同时使用了准入控制器 `NodeRestriction`。此时，如果尝试使用未经身份验证的请求访问集群，应该会返回权限不足的错误。

#### **验证步骤**：
1. 使用不带身份验证的 `kubectl` 命令进行测试：

```bash
kubectl get pods
```

此时，你会看到类似以下的错误消息，提示访问被拒绝：

```plain
error: You must be logged in to the server (the server has asked for the client to provide credentials).
```

1. 使用管理员的配置文件 `/etc/kubernetes/admin.conf` 访问集群：

```bash
KUBEVERSION=$(kubectl version -o json | jq -r .serverVersion.gitVersion)
KUBECONFIG=/etc/kubernetes/admin.conf kubectl get pods --kubeconfig=$KUBECONFIG
```

这应该会成功列出集群中的 Pod。

---

### **总结**
通过以上步骤，我们完成了 Kubernetes API 服务器的安全加固配置：

1. 禁用了匿名身份验证，确保所有 API 请求都必须经过身份验证。
2. 启用了授权模式 `Node` 和 `RBAC`，提供了基于角色的细粒度访问控制。
3. 启用了准入控制器 `NodeRestriction`，限制节点只能访问与自己相关的资源。
4. 删除了 `ClusterRoleBinding system:anonymous`，清除了对匿名用户的权限。

这些配置确保了 Kubernetes 集群的安全性，并防止了未经授权的访问。

