# Pod 控制器 DaemonSet
#### DaemonSet 介绍
DaemonSet（DS）控制器在功能方面与Deployment控制器几乎一样，支持滚动更新、版本回退等，只不过它在创建Pod时，可以保障集群中的每一个节点上都运行（Pod数量与节点数量保持一致）。

如果一个pod提供的功能是节点级别的（每个节点都需要且只需要一个），一般适用于日志收集，节点监控场景，这种类型的pod就适合使用DaemonSet类型的控制器创建





#### DaemonSet 特性
DaemonSet控制器的特点：

+ 每当像集群添加一个节点时，指定的pod副本也将添加到该节点上
+ 当节点从集群中移除时，pod也就被垃圾回收

#### DaemonSet 应用案例
**案例**：通过daemonset控制器创建Nginx Pod，并保证在每个节点都运行。

```yaml
# vim ds_nginx.yml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ds-nginx
  namespace: test

spec:
  selector:
    matchLabels:
      name: ds-nginx

  template:
    metadata:
      labels:
        name: ds-nginx

    spec:
      tolerations:                           # 添加容忍，否则pod无法被调度到master节点
      - key: node-role.kubernetes.io/master  # 污点key
        effect: NoSchedule                   # 污点类型
      containers:
      - name: nginx
        image: nginx:1.17.0
        ports:
        - containerPort: 80


          
创建pod
# kubectl create -f ds_nginx.yml



查看ds信息
# kubectl get ds -n test



查看pod详细信息
# kubectl get pod -n test -o wide



删除ds
# kubectl delete -f ds_nginx.yml

```

