### **ConfigMap 的概念**
`ConfigMap` 是 Kubernetes 中的一种资源对象，用于存储非敏感的配置信息，比如应用程序所需的配置文件、环境变量或者命令行参数。

+ **用途**：
    - 将配置信息与容器化应用分离（使应用更易于移植）。
    - 可以动态更新配置，而无需重建容器镜像。
+ **特点**：
    - 主要用于存储非敏感数据（敏感数据应该使用 Secret）。
    - 可以通过挂载为环境变量、挂载为文件或者直接在命令行参数中使用。

---

### **ConfigMap 的创建**
可以通过 YAML 配置文件或者命令行创建 ConfigMap。

#### **1. 使用命令行创建**
```bash
kubectl create configmap <configmap-name> --from-literal=key1=value1 --from-literal=key2=value2
```

例如：

```bash
kubectl create configmap my-config --from-literal=APP_ENV=production --from-literal=APP_DEBUG=false
```

#### **2. 使用文件创建**
将配置存储在文件中，然后从文件创建 ConfigMap：

```bash
kubectl create configmap <configmap-name> --from-file=<file-path>
```

例如：

```bash
kubectl create configmap my-config --from-file=app-config.properties
```

#### **3. 使用 YAML 文件定义**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  APP_ENV: production
  APP_DEBUG: "false"
  LOG_LEVEL: info
```

使用以下命令应用：

```bash
kubectl apply -f configmap.yaml
```

---

### **ConfigMap 的使用**
ConfigMap 可以以以下三种方式注入到 Pod 中：

#### **1. 注入为环境变量**
在 Pod 的 `env` 字段中引用 ConfigMap：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: my-container
    image: busybox
    env:
    - name: APP_ENV
      valueFrom:
        configMapKeyRef:
          name: my-config
          key: APP_ENV
    - name: APP_DEBUG
      valueFrom:
        configMapKeyRef:
          name: my-config
          key: APP_DEBUG
```

#### **2. 挂载为文件**
将 ConfigMap 挂载到容器的文件系统中：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: my-container
    image: busybox
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: my-config
```

**效果**：ConfigMap 的键值对会以文件的形式挂载到 `/etc/config`，文件名为键，内容为值。

#### **3. 用作命令行参数**
可以通过 Pod 的 `args` 或 `command` 字段，将 ConfigMap 的值作为命令行参数：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  containers:
  - name: my-container
    image: busybox
    command: ["/bin/sh", "-c"]
    args:
    - "echo $APP_ENV && echo $APP_DEBUG"
    env:
    - name: APP_ENV
      valueFrom:
        configMapKeyRef:
          name: my-config
          key: APP_ENV
    - name: APP_DEBUG
      valueFrom:
        configMapKeyRef:
          name: my-config
          key: APP_DEBUG
```

---

### **ConfigMap 的管理**
#### **查看 ConfigMap**
```bash
kubectl get configmap
kubectl get configmap <configmap-name> -o yaml
```

#### **更新 ConfigMap**
如果是通过文件创建的 ConfigMap，可以直接编辑文件并重新应用：

```bash
kubectl apply -f configmap.yaml
```

也可以直接编辑：

```bash
kubectl edit configmap <configmap-name>
```

#### **删除 ConfigMap**
```bash
kubectl delete configmap <configmap-name>
```

---

### **ConfigMap 的优势**
1. **配置分离**：与代码解耦，提升应用的可移植性。
2. **动态更新**：在不重新构建镜像的情况下，直接修改配置。
3. **可扩展性**：支持多种数据来源，灵活满足各种需求。

**注意**：如果 ConfigMap 被更新，挂载到容器中的值不会自动更新（除非重新创建 Pod），需要使用挂载为文件的方式，并启用自动更新特性。

