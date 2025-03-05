在 Kubernetes 中，**网络策略 (Network Policy)** 是一种用于定义 Pod 之间通信的规则，它允许你控制哪些 Pod 可以访问哪些服务、哪些端口以及协议。**Deny** 和 **Allow** 是两个核心概念，代表着网络策略中的允许和拒绝通信的规则。

### 1. **Network Policy 的基本概念**
Network Policy 允许通过指定规则来限制 Pod 之间、Pod 与服务之间或外部流量的流动。网络策略可以通过 **Deny** 和 **Allow** 规则来定义流量控制。

+ **Allow**：允许符合条件的流量通过，常用于指定哪些 Pod 可以相互通信，哪些外部流量可以访问 Pod。
+ **Deny**：拒绝符合条件的流量，这可以作为一个隐式的保护措施，阻止未明确允许的流量。

Kubernetes 默认没有启用网络策略功能。要使用网络策略，你的集群需要使用支持网络策略的网络插件（如 Calico、Cilium、Weave 等）。

### 2. **网络策略的工作原理**
网络策略通过 `spec.ingress` 和 `spec.egress` 字段来控制进入和出去的流量。网络策略可以指定以下内容：

+ **Ingress**：控制允许哪些流量可以进入 Pod。
+ **Egress**：控制 Pod 可以向哪些目标发送流量。

默认情况下，在 Kubernetes 集群中没有启用任何网络策略时，所有 Pod 都可以互相通信。如果启用了网络策略，只有显式允许的流量才能通过，未明确允许的流量将被拒绝。

### 3. **Deny 和 Allow 网络策略配置**
#### 3.1 **Allow 网络策略**
`Allow` 规则显式允许指定的流量通过。你可以定义哪些来源的流量可以进入 Pod，哪些流量可以从 Pod 发出。

例如，允许从 `frontend` 命名空间的 Pod 向 `backend` 命名空间的 Pod 发送流量：

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: backend
spec:
  podSelector: {}  # 选择应用该网络策略的 Pod
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend  # 允许来自 frontend 命名空间的流量
```

在这个例子中：

+ **podSelector**：指定哪些 Pod 应用此网络策略。在此例中，`backend` 命名空间中的所有 Pod 都会被包含。
+ **ingress**：定义允许从 `frontend` 命名空间流入 `backend` 命名空间的流量。

#### 3.2 **Deny 网络策略**
`Deny` 规则通常通过不显式允许流量来隐式实现。Kubernetes 中没有 `deny` 关键字，但你可以通过不定义某些规则，或者通过定义默认拒绝的网络策略来实现流量的拒绝。

一个常见的做法是定义一个拒绝所有流量的网络策略，即通过设置 `ingress` 和 `egress` 为空来拒绝所有入站和出站流量：

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: default
spec:
  podSelector: {}  # 应用于所有 Pod
  ingress: []  # 不允许任何入站流量
  egress: []  # 不允许任何出站流量
```

在此配置中：

+ `ingress: []`：没有定义任何入站规则，表示拒绝所有入站流量。
+ `egress: []`：没有定义任何出站规则，表示拒绝所有出站流量。

这个网络策略会应用于所有 Pod，拒绝所有的流量。

#### 3.3 **Allow 与 Deny 组合策略**
可以结合 **Allow** 和 **Deny** 网络策略来实现更细粒度的访问控制。例如，首先应用一个 `Deny` 策略，阻止所有流量，然后应用特定的 `Allow` 策略来显式允许某些流量：

+ **Step 1**：默认拒绝所有流量。

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
  namespace: default
spec:
  podSelector: {}  # 应用于所有 Pod
  ingress: []  # 不允许任何入站流量
  egress: []  # 不允许任何出站流量
```

+ **Step 2**：允许来自特定 IP 地址或命名空间的流量。

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-some-traffic
  namespace: default
spec:
  podSelector: {}  # 应用于所有 Pod
  ingress:
  - from:
    - ipBlock:
        cidr: 192.168.1.0/24  # 允许来自特定 IP 范围的流量
  egress:
  - to:
    - ipBlock:
        cidr: 10.1.1.0/24  # 允许流量发送到特定 IP 范围
```

### 4. **总结**
+ **Allow 网络策略** 通过明确的规则来允许流量，常用于允许特定的流量从特定的源进入 Pod，或者从 Pod 发出。
+ **Deny 网络策略** 通过不显式允许流量来拒绝所有其他流量。这通常通过不设置 `ingress` 或 `egress` 规则，或者应用一个全面拒绝的网络策略来实现。
+ Kubernetes 默认的行为是没有网络策略时，所有 Pod 可以相互通信；当启用网络策略时，未被明确允许的流量会被拒绝。

通过合理设计和应用网络策略，能够有效地加强 Kubernetes 集群中的安全性，控制 Pod 之间的通信，并防止潜在的攻击。

