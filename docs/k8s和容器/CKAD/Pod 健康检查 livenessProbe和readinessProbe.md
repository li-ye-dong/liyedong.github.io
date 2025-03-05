在 Kubernetes 中，`livenessProbe` 和 `readinessProbe` 是 Pod 的健康检查机制，用于确保容器运行状态正常，并能够对外提供服务。

---

### **1. 概念**
#### **livenessProbe**
+ **目的**：检查容器是否还“活着”。 
    - 如果失败，Kubernetes 会重启容器。
    - 常用于检测应用进入了无法恢复的错误状态，比如死锁或崩溃。

#### **readinessProbe**
+ **目的**：检查容器是否“准备好”对外提供服务。 
    - 如果失败，Kubernetes 会从对应的 Service 的后端池中移除这个 Pod。
    - 常用于延迟提供服务的场景，比如需要加载配置文件或依赖其他服务。

---

### **2. 工作机制**
+ **探针类型**：两者的探测方式相同。
    1. **HTTP GET**： 
        * 通过 HTTP 请求指定的路径，判断返回的状态码是否是 `200~399`。
    2. **TCP Socket**： 
        * 尝试连接指定的端口，如果连接成功，则表示探测成功。
    3. **命令（exec）**： 
        * 执行容器内部的命令，判断命令返回状态码是否为 `0`。
+ **执行周期**：
    - 可以通过 `initialDelaySeconds`、`periodSeconds` 等参数配置探测的频率和时间。

---

### **3. 配置示例**
#### **基本示例**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: health-check-demo
spec:
  containers:
    - name: demo-app
      image: my-app:latest
      ports:
        - containerPort: 80
      livenessProbe:                # 配置 livenessProbe
        httpGet:
          path: /healthz            # HTTP 请求的路径
          port: 80                 # 监听的端口
        initialDelaySeconds: 5     # 启动后延迟 5 秒开始探测
        periodSeconds: 10          # 每隔 10 秒探测一次
      readinessProbe:               # 配置 readinessProbe
        httpGet:
          path: /readiness          # HTTP 请求的路径
          port: 80
        initialDelaySeconds: 3     # 启动后延迟 3 秒开始探测
        periodSeconds: 5           # 每隔 5 秒探测一次
```

---

#### **使用 exec 示例**
```yaml
livenessProbe:
  exec:
    command:
      - cat
      - /tmp/healthy
  initialDelaySeconds: 5
  periodSeconds: 10
```

+ 解释：探针会在容器内部检查文件 `/tmp/healthy` 是否存在。如果不存在，探测失败。

---

#### **使用 TCP Socket 示例**
```yaml
readinessProbe:
  tcpSocket:
    port: 3306
  initialDelaySeconds: 10
  periodSeconds: 5
```

+ 解释：探针会尝试连接容器的 3306 端口（通常是 MySQL）。如果连接失败，表示容器暂时不可用。

---

### **4. 配置参数说明**
| 参数 | 作用 |
| --- | --- |
| `initialDelaySeconds` | 容器启动后，延迟多长时间开始探测。 |
| `periodSeconds` | 每隔多长时间探测一次。 |
| `timeoutSeconds` | 探测超时时间，默认 1 秒。 |
| `successThreshold` | 探测成功的最少次数，只有达到这个值后，探测才被认为成功（仅适用于 `readinessProbe`<br/>）。 |
| `failureThreshold` | 探测失败的最大次数，如果超过这个值，则认为探测失败。 |


---

### **5. livenessProbe 和 readinessProbe 的区别**
| **功能** | **livenessProbe** | **readinessProbe** |
| --- | --- | --- |
| **作用** | 检查容器是否还活着，是否需要重启。 | 检查容器是否准备好对外提供服务。 |
| **失败处理方式** | 重启容器。 | 将 Pod 从 Service 的 Endpoints 中移除。 |
| **应用场景** | 应用可能会出现死锁、逻辑错误等无法自愈的状态。 | 应用启动慢、依赖服务未就绪，或需要临时维护时使用。 |


---

### **6. 实践场景**
1. **Web 服务**
    - `livenessProbe`：确保服务逻辑正常。
    - `readinessProbe`：延迟加载后端资源，准备好后才接收流量。
2. **数据库服务**
    - `livenessProbe`：探测数据库服务是否正常运行，防止挂起。
    - `readinessProbe`：等待数据库初始化完成或主从同步完成。
3. **长时间运行任务**
    - `livenessProbe`：检测任务是否进入死循环或卡住。
    - `readinessProbe`：检测任务是否完全启动并接受请求。

---

### **7. 注意事项**
1. **livenessProbe 与 readinessProbe 不要滥用**
    - 不合适的配置可能导致容器频繁重启，影响性能。
2. **精确设置延迟时间**
    - 如果延迟时间不足，可能导致误判。
3. **对容器内应用无侵入**
    - HTTP 和 TCP 探针对应用无侵入，更推荐使用。
4. **监控与日志**
    - 配合监控系统（如 Prometheus）和日志分析工具排查探针相关问题。

---

### **8. 示例问题及解答**
#### **问题：Pod 一直重启**
+ **原因**：`livenessProbe` 配置不当，导致 Kubernetes 频繁重启容器。
+ **解决方案**： 
    - 检查探针的路径是否正确。
    - 确保 `initialDelaySeconds` 足够长，避免误判容器刚启动时未就绪。

#### **问题：Pod 状态一直为 NotReady**
+ **原因**：`readinessProbe` 配置不当，容器没有通过探针。
+ **解决方案**： 
    - 确保探测目标的端口或路径是可访问的。
    - 检查探针的超时时间是否合理。

---

通过正确配置 `livenessProbe` 和 `readinessProbe`，可以提高应用的可靠性和可用性，是 Kubernetes 健康检查中的关键工具。

