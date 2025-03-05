### **Pod 的资源请求和限制**
Kubernetes 提供了**资源请求（Resource Requests）**和**资源限制（Resource Limits）**的功能，用于控制 Pod 中容器对 CPU 和内存等资源的分配和使用。

---

### **资源请求和限制的概念**
1. **资源请求 (requests)**:
    - 表示容器启动时需要的最小资源。
    - 调度器会根据资源请求值，将 Pod 安排到有足够资源的节点上。
    - 这部分资源是“保证分配”的。
2. **资源限制 (limits)**:
    - 表示容器能使用的最大资源。
    - 限制容器使用资源的上限，防止单个容器占用过多资源，影响其他 Pod。
    - 超过限制可能会导致容器被杀死或限制其 CPU 使用。

---

### **定义资源请求和限制**
资源请求和限制通过 YAML 文件定义在 Pod 的 spec 部分，具体配置如下：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-demo-pod
spec:
  containers:
    - name: resource-demo-container
      image: nginx
      resources:
        requests:
          memory: "128Mi"  # 最小请求 128Mi 内存
          cpu: "500m"      # 最小请求 500m CPU（即 0.5 个 CPU 核心）
        limits:
          memory: "256Mi"  # 最大限制 256Mi 内存
          cpu: "1"         # 最大限制 1 CPU 核心
```

+ **内存单位**：`Mi`（兆字节）、`Gi`（千兆字节）。
+ **CPU 单位**：`1` 表示一个 CPU 核心，`500m` 表示 0.5 个 CPU 核心。

---

### **资源调度与运行机制**
1. **调度阶段**：
    - Kubernetes 调度器会根据 `requests` 值判断哪个节点有足够资源来运行 Pod。
    - 如果没有满足 `requests` 的节点，Pod 将保持 Pending 状态，无法被调度。
2. **运行阶段**：
    - 容器启动后，如果资源使用超过 `limits`： 
        * CPU：容器的 CPU 使用会被限制，但不会被终止。
        * 内存：容器会被直接杀死（`OOMKilled`），因为 Kubernetes 无法限制内存的使用。

---

### **资源请求和限制的最佳实践**
1. **合理设置 **`**requests**`** 和 **`**limits**`:
    - `requests` 应设置为应用的正常运行需求。
    - `limits` 应设置为应用的性能峰值需求。
2. **避免过高或过低设置**:
    - 如果 `requests` 设置过高，调度器可能找不到满足条件的节点，导致 Pod 无法调度。
    - 如果 `limits` 设置过低，可能会导致应用在高负载时被限制或杀死。
3. **为所有容器设置资源限制**:
    - 未设置资源限制的容器可能会无限制占用节点资源，影响其他容器运行。
4. **监控与调整**:
    - 使用 Kubernetes 的监控工具（如 Prometheus、Grafana、Lens 等）监控资源使用情况，动态调整请求和限制值。

---

### **资源分配的详细机制**
+ **CPU 分配**：
    - CPU 是可压缩资源，容器的 CPU 使用可以超过 `requests`，但会被限制在 `limits` 内。
    - 超过 `limits` 的 CPU 使用会被限制，但不会终止容器。
+ **内存分配**：
    - 内存是不可压缩资源，容器只能使用 `requests` 到 `limits` 之间的内存。
    - 如果超过 `limits`，容器会被直接杀死，并显示 `OOMKilled` 状态。

---

### **资源隔离的实现**
+ **CPU 隔离**： Kubernetes 使用 cgroups（Control Groups）来限制 CPU 的使用。
+ **内存隔离**： 内存的限制同样是通过 cgroups 实现，超过限制时会触发 OOM（Out Of Memory）杀死容器。

---

### **示例场景**
#### **1. 未设置资源限制的情况**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: no-resources-pod
spec:
  containers:
    - name: my-container
      image: nginx
```

+ 容器可以使用节点上的所有资源，不受限制。
+ 如果某个容器无限制使用资源，可能会导致其他 Pod 无法正常运行。

---

#### **2. 设置合理的请求和限制**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: optimized-resources-pod
spec:
  containers:
    - name: my-container
      image: nginx
      resources:
        requests:
          memory: "200Mi"
          cpu: "100m"
        limits:
          memory: "500Mi"
          cpu: "1"
```

+ 保证容器启动时至少有 200Mi 内存和 0.1 CPU 核心。
+ 容器的内存最多可使用 500Mi，CPU 最多可使用 1 核。

---

### **总结**
资源请求和限制是 Kubernetes 中资源管理的重要工具。合理设置 `requests` 和 `limits` 能确保应用在稳定运行的同时，不会占用超出预期的资源，影响其他应用。通过监控和调整，动态优化资源分配可以提高集群整体的运行效率。

