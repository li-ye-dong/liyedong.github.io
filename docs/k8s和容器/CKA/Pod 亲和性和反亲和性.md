### **定义**
+ **Pod Affinity（亲和性）**：倾向于将 Pod 调度到与指定标签的 Pod **在同一个 Node 或拓扑域** 上。
+ **Pod Anti-Affinity（反亲和性）**：倾向于将 Pod 调度到与指定标签的 Pod **不在同一个 Node 或拓扑域** 上。

---

### **方法一：Pod 反亲和性（Preferred/Required）**
在 Deployment 中添加 `affinity.podAntiAffinity`：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values:
                      - my-app
              topologyKey: "kubernetes.io/hostname"  # 表示在不同节点
      containers:
        - name: my-app
          image: nginx:latest
```

解释：

+ `requiredDuringSchedulingIgnoredDuringExecution`：硬约束，必须满足，否则 Pod 不会调度。
+ `topologyKey: "kubernetes.io/hostname"`：按照 Node 区分，保证 Pod 不在同一个节点。
+ `preferredDuringSchedulingIgnoredDuringExecution`：软约束，K8s 会尽量满足，但调度失败不会阻止 Pod 创建。

⚠️ 注意：如果 Node 数量小于副本数，使用 `required` 可能会调度失败。

---

### **方法二：topologySpreadConstraints**
如果你希望 Pod **均匀分布在不同 Node 上**，可以用 `topologySpreadConstraints`：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      topologySpreadConstraints:
        - maxSkew: 1                  # 最大倾斜数量
          topologyKey: "kubernetes.io/hostname"  # 按 Node 分布
          whenUnsatisfiable: DoNotSchedule  # 如果无法满足则不调度
          labelSelector:
            matchLabels:
              app: my-app
      containers:
        - name: my-app
          image: nginx:latest
```

解释：

+ `maxSkew: 1`：同一个 Node 上的 Pod 数量与平均值的最大偏差。
+ `topologyKey`：按 Node 分布。
+ `whenUnsatisfiable: DoNotSchedule`：硬约束。
+ 可以保证副本尽量分散在不同 Node 上。

---

### ✅ 总结
| 方法 | 特点 | 使用场景 |
| --- | --- | --- |
| Pod Anti-Affinity | 硬约束或软约束，Pod 不在同 Node | 确保关键 Pod 不共存，防止单点故障 |
| TopologySpreadConstraints | 均匀分布，支持软/硬约束 | 多副本服务均衡分布，提高资源利用和可靠性 |


---

如果你希望，我可以帮你写一个 **实际可用的 Deployment YAML**，确保 3 个副本 **不在同一个 Node 上**，并且适用于节点数量少于副本数时也能调度成功。

你希望我直接写吗？

