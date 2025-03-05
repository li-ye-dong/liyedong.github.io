# <font style="color:rgb(51, 51, 51);">K8s Ingress 七层负载均衡</font>
#### <font style="color:rgb(51, 51, 51);">Ingress 控制器介绍</font>
<font style="color:rgb(51, 51, 51);">在前面的章节中通过Service对集群之外暴露服务的主要方式有两种：</font>

+ <font style="color:rgb(51, 51, 51);">NotePort：该方式的缺点是会占用集群Node节点的端口，当集群服务变多时，这个缺点就愈发的明显（端口不够用）</font>
+ <font style="color:rgb(51, 51, 51);">LoadBalancer：该方式的缺点是每个service都需要一个外部负载均衡设备的支持才可以</font>

<font style="color:rgb(51, 51, 51);">Ingress相当于一个7层的负载均衡器，是k8s对反向代理的一个抽象，它的工作原理类似于Nginx反向代理</font>

1. <font style="color:rgb(51, 51, 51);">用户编写Ingress规则，说明哪个域名对应集群中的Service</font>
2. <font style="color:rgb(51, 51, 51);">Ingress控制器动态感知Ingress服务规则的变化，然后生成一段对应的Nginx反向代理配置进行流量转发</font>

#### <font style="color:rgb(51, 51, 51);">Ingress 控制器种类</font>
**<font style="color:rgb(51, 51, 51);">Kubernetes Ingress Controller</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/nginxinc/kubernetes-ingress</font>](http://github.com/nginxinc/kubernetes-ingress)
+ <font style="color:rgb(51, 51, 51);">实现：Go/Lua（nginx 是用 C 写的）</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Kubernetes 的“官方”控制器（之所以称为官方，是想把它区别于 NGINX 公司的控制器）。这是社区开发的控制器，它基于 nginx Web 服务器，并补充了一组用于实现额外功能的 Lua 插件。</font>
+ <font style="color:rgb(51, 51, 51);">由于 NGINX 十分流行，再加上把它用作控制器时所需的修改较少，</font>**<font style="color:rgb(51, 51, 51);">它对于 K8s 普通工程师来说，可能是最简单和最直接的选择</font>**<font style="color:rgb(51, 51, 51);">。</font>

**<font style="color:rgb(51, 51, 51);">NGINX Ingress Controller</font>**

    - <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/kubernetes/ingress-nginx</font>](http://github.com/kubernetes/ingress-nginx)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">这是 NGINX 公司开发的官方产品，它也有一个基于 NGINX Plus 的商业版。NGINX 的控制器具有很高的稳定性、持续的向后兼容性，且没有任何第三方模块。</font>
+ <font style="color:rgb(51, 51, 51);">由于消除了 Lua 代码，和官方控制器相比，它保证了较高的速度，但也因此受到较大限制。相较之下，它的付费版本有更广泛的附加功能，如实时指标、JWT 验证、主动健康检查等。</font>
+ <font style="color:rgb(51, 51, 51);">NGINX Ingress 重要的优势是对 TCP/UDP 流量的全面支持，最主要缺点是缺乏流量分配功能。</font>

**<font style="color:rgb(51, 51, 51);">Kong Ingress</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/Kong/kubernetes-ingress-controller</font>](http://github.com/Kong/kubernetes-ingress-controller)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Kong Ingress 由 Kong Inc 开发，有两个版本：商业版和免费版。它基于 NGINX 构建，并增加了扩展其功能的 Lua 模块。</font>
+ <font style="color:rgb(51, 51, 51);">最初，Kong Ingress 主要用作 API 网关，用于 API 请求的处理和路由。现在，它已经成为成熟的 Ingress 控制器，</font>**<font style="color:rgb(51, 51, 51);">主要优点是拥有大量易于安装和配置的附加模块、插件（包括第三方插件）</font>**<font style="color:rgb(51, 51, 51);">。它开启了控制器具备大量附加功能的先河，其内置函数也提供了许多可能性。Kong Ingress 配置是用 CRD 执行的。</font>
+ <font style="color:rgb(51, 51, 51);">Kong Ingress 的一个重要特性是它只能在一个环境中运行（而不支持跨命名空间）。这是一个颇有争议的话题：有些人认为这是一个缺点，因为必须为每个环境生成实例；而另一些人认为这是一个特殊特性，因为它是更高级别的隔离，控制器故障的影响仅限于其所在的环境。</font>

**<font style="color:rgb(51, 51, 51);">Traefik</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/containous/traefik</font>](http://github.com/containous/traefik)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：MIT</font>
+ <font style="color:rgb(51, 51, 51);">最初，这个代理是为微服务请求及其动态环境的路由而创建的，因此具有许多有用的功能：</font>**<font style="color:rgb(51, 51, 51);">连续更新配置（不重新启动）、支持多种负载均衡算法、Web UI、指标导出、对各种服务的支持协议、REST API、Canary 版本</font>**<font style="color:rgb(51, 51, 51);">等。</font>
+ <font style="color:rgb(51, 51, 51);">支持开箱即用的 Let’s Encrypt 是它的另一个不错的功能，但它的主要缺点也很明显，就是为了控制器的高可用性，你必须安装并连接其 Key-value store。</font>
+ <font style="color:rgb(51, 51, 51);">在 2019 年 9 月发布的 Traefik v2.0 中，虽然它增加许多不错的新功能，如带有 SNI 的 TCP/SSL、金丝雀部署、流量镜像/shadowing 和经过改进的 Web UI，但一些功能（如 WAF 支持）还在策划讨论中。</font>
+ <font style="color:rgb(51, 51, 51);">与新版本同期推出的还有一个名叫 Mesh 的服务网格，它建在 Traefik 之上，对kubernetes内部服务访问做到受控及被监控。</font>

**<font style="color:rgb(51, 51, 51);">HAProxy Ingress</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/jcmoraisjr/haproxy-ingress</font>](http://github.com/jcmoraisjr/haproxy-ingress)
+ <font style="color:rgb(51, 51, 51);">实现：Go（HAProxy 是用 C 写的）</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">HAProxy 是众所周知的代理服务器和负载均衡器。作为 Kubernetes 集群的一部分，它提供了“软”配置更新（无流量损失）、基于 DNS 的服务发现和通过 API 进行动态配置。 HAProxy 还支持完全自定义配置文件模板（通过替换 ConfigMap）以及在其中使用 Spring Boot 函数。</font>
+ <font style="color:rgb(51, 51, 51);">通常，工程师会把重点放在已消耗资源的高速、优化和效率上。而 HAProxy 的优点之一正是支持大量负载均衡算法。值得一提的是，在2020年 6 月发布的 v2.0 中，HAProxy 增加了许多新功能，其即将推出的 v2.1 有望带来更多新功能（包括 OpenTracing 支持）。</font>

**<font style="color:rgb(51, 51, 51);">Voyager</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/appscode/voyager</font>](http://github.com/appscode/voyager)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Voyager 基于 HAProxy，并作为一个通用的解决方案提供给大量供应商。它最具代表性的功能包括 L7 和 L4 上的流量负载均衡，其中，</font>**<font style="color:rgb(51, 51, 51);">TCP L4 流量负载均衡称得上是该解决方案最关键的功能之一</font>**<font style="color:rgb(51, 51, 51);">。</font>
+ <font style="color:rgb(51, 51, 51);">在2020年早些时候，尽管 Voyager 在 v9.0.0 中推出了对 HTTP/2 和 gRPC 协议的全面支持，但总的来看，对证书管理（Let’s Encrypt 证书）的支持仍是 Voyager 集成的最突出的新功能。</font>

**<font style="color:rgb(51, 51, 51);">Contour</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/heptio/contour</font>](http://github.com/heptio/contour)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Contour 和 Envoy 由同一个作者开发，它基于 Envoy。</font>**<font style="color:rgb(51, 51, 51);">它最特别的功能是可以通过 CRD（IngressRoute）管理 Ingress 资源</font>**<font style="color:rgb(51, 51, 51);">，对于多团队需要同时使用一个集群的组织来说，这有助于保护相邻环境中的流量，使它们免受 Ingress 资源更改的影响。</font>
+ <font style="color:rgb(51, 51, 51);">它还提供了一组扩展的负载均衡算法（镜像、自动重复、限制请求率等），以及详细的流量和故障监控。对某些工程师而言，它不支持粘滞会话可能是一个严重缺陷。</font>

**<font style="color:rgb(51, 51, 51);">Istio Ingress</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://istio.io/docs/tasks/traffic-management/ingress</font>](http://istio.io/docs/tasks/traffic-management/ingress)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Istio 是 IBM、Google 和 Lyft 的联合开发项目，它是一个全面的服务网格解决方案——</font>**<font style="color:rgb(51, 51, 51);">不仅可以管理所有传入的外部流量（作为 Ingress 控制器），还可以控制集群内部的所有流量</font>**<font style="color:rgb(51, 51, 51);">。</font>
+ <font style="color:rgb(51, 51, 51);">Istio 将 Envoy 用作每种服务的辅助代理。从本质上讲，它是一个可以执行几乎所有操作的大型处理器，其中心思想是最大程度的控制、可扩展性、安全性和透明性。</font>
+ <font style="color:rgb(51, 51, 51);">通过 Istio Ingress，你可以对流量路由、服务之间的访问授权、均衡、监控、金丝雀发布等进行优化。</font>

**<font style="color:rgb(51, 51, 51);">Ambassador</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/datawire/ambassador</font>](http://github.com/datawire/ambassador)
+ <font style="color:rgb(51, 51, 51);">实现：Python</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Ambassador 也是一个基于 Envoy 的解决方案，它有免费版和商业版两个版本。</font>
+ <font style="color:rgb(51, 51, 51);">Ambassador 被称为“Kubernetes 原生 API 微服务网关”，它与 K8s 原语紧密集成，拥有你所期望的从 Ingress controller 获得的功能包，它还可以与各种服务网格解决方案，如 Linkerd、Istio 等一起使用。</font>
+ <font style="color:rgb(51, 51, 51);">顺便提一下，Ambassador 博客日前发布了一份基准测试结果，比较了 Envoy、HAProxy 和 NGINX 的基础性能。</font>

**<font style="color:rgb(51, 51, 51);">Gloo</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/solo-io/gloo</font>](http://github.com/solo-io/gloo)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Gloo 是在 Envoy 之上构建的新软件（于 2018 年 3 月发布），由于它的作者坚持认为“网关应该从功能而不是服务中构建 API”，它也被称为“功能网关”。其“功能级路由”的意思是它可以为后端实现是微服务、无服务器功能和遗留应用的混合应用路由流量。</font>
+ <font style="color:rgb(51, 51, 51);">由于拥有可插拔的体系结构，Gloo 提供了工程师期望的大部分功能，但是其中一些功能仅在其商业版本（Gloo Enterprise）中可用。</font>

**<font style="color:rgb(51, 51, 51);">Skipper</font>**

+ <font style="color:rgb(51, 51, 51);">参考链接：</font>[<font style="color:rgb(51, 51, 51);">http://github.com/zalando/skipper</font>](http://github.com/zalando/skipper)
+ <font style="color:rgb(51, 51, 51);">实现：Go</font>
+ <font style="color:rgb(51, 51, 51);">许可证：Apache 2.0</font>
+ <font style="color:rgb(51, 51, 51);">Skipper 是 HTTP 路由器和反向代理，因此不支持各种协议。从技术上讲，它使用 Endpoints API（而不是 Kubernetes Services）将流量路由到 Pod。它的优点在于其丰富的过滤器集所提供的高级 HTTP 路由功能，工程师可以借此创建、更新和删除所有 HTTP 数据。</font>
+ <font style="color:rgb(51, 51, 51);">Skipper 的路由规则可以在不停机的情况下更新。正如它的作者所述，Skipper 可以很好地与其他</font>

#### <font style="color:rgb(51, 51, 51);">Nginx Ingress 环境搭建</font>
<font style="color:rgb(51, 51, 51);">ingress-nginx资源清单文件下载地址：</font>[<font style="color:rgb(51, 51, 51);">https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/baremetal/deploy.yaml</font>](https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/baremetal/deploy.yaml)

<font style="color:rgb(119, 119, 119);">提示：由于网络原因可能无法下载，直接使用我给大家下载好的文件即可，文件名：deploy.yml</font>

```yaml
创建目录，并上传文件到目录下
[root@master01 ~]# mkdir /ingress-nginx
[root@master01 ~]# cd /ingress-nginx

创建ingress-nginx
[root@master01 ingress-nginx]# kubectl create -f deploy.yaml

查看ns（会有一个ingress-nginx的命名空间）
[root@master01 ingress-nginx]#  kubectl get ns
...
ingress-nginx     Active   2m27s
```

[deploy.yaml](https://www.yuque.com/attachments/yuque/0/2024/yaml/40598547/1727685007742-1161b007-7c00-48b5-8606-6c5f0fd75ab2.yaml)

**<font style="color:rgb(51, 51, 51);">问题1：controller日志显示 80端口被占用</font>**

```yaml
securityContext:
  allowPrivilegeEscalation: true #允许提权，解决pod显示80端口被占用
  capabilities:
    add:
    - NET_BIND_SERVICE
    drop:
    - ALL
  readOnlyRootFilesystem: false
  runAsNonRoot: false #以root运行 允许提权，解决pod显示80端口被占用
  runAsUser: 101 #无需修改
```

**<font style="color:rgb(51, 51, 51);">问题2：修改runAsUser为0后，导致证书生成显示权限不足</font>**

```yaml
  runAsUser: 101 #无需修改 改回101即可
```

```yaml
[root@master01 ingress-nginx]# kubectl apply -f deploy.yaml


查看ingress-nginx空间的pod（有两个Pod用于执行一次性任务，状态为Completed（完成），这种Pod执行后即退出。）
[root@master01 ingress-nginx]# kubectl get po -n  ingress-nginx
NAME                                       READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-cctfh       0/1     Completed   0          28m
ingress-nginx-admission-patch-rhzrk        0/1     Completed   1          28m
ingress-nginx-controller-9d98d6467-2wtnj   1/1     Running     0          23m


查看service
[root@master01 ingress-nginx]# kubectl get svc -n ingress-nginx
NAME                                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx-controller             NodePort    10.99.98.180   <none>        80:31770/TCP,443:31082/TCP   17m
ingress-nginx-controller-admission   ClusterIP   10.97.42.155   <none>        443/TCP                      17m
#提示：到此为止ingress-nginx的控制器已经安装完毕
```

#### <font style="color:rgb(51, 51, 51);">Nginx Ingress HTTP 应用案例</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过Deployment部署tomcat与nginx的pod，并通过Nginx Ingress 进行HTTP访问</font>

```yaml
[root@master01 ~]# vim ingress-http.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-nginx
  namespace: test

spec:
  selector:
    matchLabels:
      app: deploy-nginx

  template:
    metadata:
      labels:
        app: deploy-nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.18.0
        ports:
        - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: svc-nginx
  namespace: test

spec:
  selector:
    app: deploy-nginx
  clusterIP: None
  type: ClusterIP         #service类型
  ports:
    - port: 80
      targetPort: 80

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-tomcat
  namespace: test

spec:
  selector:
    matchLabels:
      app: deploy-tomcat

  template:
    metadata:
      labels:
        app: deploy-tomcat
    spec:
      containers:
      - name: tomcat
        image: tomcat:8.5-jre10-slim
        ports:
        - containerPort: 8080

---
apiVersion: v1
kind: Service
metadata:
  name: svc-tomcat
  namespace: test
spec:
  selector:
    app: deploy-tomcat
  clusterIP: None
  type: ClusterIP         #service类型
  ports:
    - port: 8080
      targetPort: 8080

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-http                   #自定义ingress名称
  namespace: test
  annotations:
    ingressclass.kubernetes.io/is-default-class: "true"   # 指定spec下方的rules的path可以使用正则表达式，如果我们没有使用正则表达式，此项则可不使用
    kubernetes.io/ingress.class: nginx  #指定控制器的类别为nginx


spec:
  rules:                         #定义主机列表
  - host: www.nginx.com          #自定义域名
    http:
      paths:
      - pathType: Prefix         #路径类型
        path: "/"                #定义站点路径
        backend:                 #定义后端引用的服务
          service:               #关联service
            name: svc-nginx      #对应上面创建的service名称
            port:
              number: 80         #service端口


  - host: www.tomcat.com         #自定义域名
    http:
      paths:
      - pathType: Prefix         #路径类型
        path: "/"                #定义站点路径
        backend:                 #定义后端引用的服务
          service:               #关联service
            name: svc-tomcat     #对应上面创建的service名称
            port:
              number: 8080       #service端口




#### 创建ingress报错
[root@master01 data]# kubectl  apply -f ingress-http.yml



查看信息
[root@master01 ~]# kubectl get all -n test


查看ingress信息
[root@master01 ~]# kubectl get ing -n test


查看详细信息
[root@master01 ~]# kubectl describe ing -n test
```

#### <font style="color:rgb(51, 51, 51);">测试Ingress HTTP 代理</font>
<font style="color:rgb(51, 51, 51);">浏览器访问由于域名无法正常解析，需要在windows内进行解析：C:\Windows\System32\drivers\etc</font>

<font style="color:rgb(51, 51, 51);">192.168.0.13 </font>[<font style="color:rgb(51, 51, 51);">www.nginx.com</font>](https://www.nginx.com)

<font style="color:rgb(51, 51, 51);">192.168.0.13 </font>[<font style="color:rgb(51, 51, 51);">www.tomcat.com</font>](https://www.tomcat.com)

**<font style="color:rgb(51, 51, 51);">访问测试</font>**<font style="color:rgb(51, 51, 51);">：在访问测试时，通过域名与ingress对外暴露的端口进行访问</font>

```yaml
#查看ingress-nginx暴露的端口
[root@master ingress]# kubectl get svc -n ingress-nginx
NAME                                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx-controller             NodePort    192.168.170.2   <none>        80:30655/TCP,443:31706/TCP   17m
ingress-nginx-controller-admission   ClusterIP   192.168.1.11    <none>        443/TCP                      17m

#随便一个节点都可以
vim /etc/hosts
10.4.7.30 www.nginx.com
10.4.7.30 www.tomcat.com

```

**<font style="color:rgb(51, 51, 51);">访问测试</font>**<font style="color:rgb(51, 51, 51);">：注意80对应的是HTTP端口，443对应的是HTTPS端口</font>

```yaml
curl -k https://www.tomcat.com:31706
curl -k https://www.nginx.com:31706
curl http://www.nginx.com:30655
curl http://www.tomcat.com:30655
```



<font style="color:rgb(51, 51, 51);">删除ingress http</font>

```yaml
[root@master01 ~]# kubectl delete -f ingress-http.yml
```

#### <font style="color:rgb(51, 51, 51);">Nginx Ingress HTTPS 应用案例</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过Deployment部署tomcat与nginx的pod，并通过Nginx Ingress 进行HTTPS访问</font>

<font style="color:rgb(51, 51, 51);">生成证书</font>

```yaml
[root@master01 ~]# openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/C=CN/ST=TJ/O=nginx/CN=thinkmo.com"
```

<font style="color:rgb(51, 51, 51);">创建密钥</font>

```yaml
[root@master01 ~]# kubectl create secret tls tls-secret --key tls.key --cert tls.crt
```

<font style="color:rgb(51, 51, 51);">创建ingress https</font>

```yaml
[root@master ~]# vim ingress-https.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-nginx
  namespace: test

spec:
  selector:
    matchLabels:
      app: deploy-nginx

  template:
    metadata:
      labels:
        app: deploy-nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.18.0
        ports:
        - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: svc-nginx
  namespace: test

spec:
  selector:
    app: deploy-nginx
  clusterIP: None
  type: ClusterIP         #service类型
  ports:
    - port: 80
      targetPort: 80

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-tomcat
  namespace: test

spec:
  selector:
    matchLabels:
      app: deploy-tomcat

  template:
    metadata:
      labels:
        app: deploy-tomcat
    spec:
      containers:
      - name: tomcat
        image: tomcat:8.5-jre10-slim
        ports:
        - containerPort: 8080

---
apiVersion: v1
kind: Service
metadata:
  name: svc-tomcat
  namespace: test
spec:
  selector:
    app: deploy-tomcat
  clusterIP: None
  type: ClusterIP         #service类型
  ports:
    - port: 8080
      targetPort: 8080

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-https                   #自定义ingress名称
  namespace: test
  annotations:
    ingressclass.kubernetes.io/is-default-class: "true"
    kubernetes.io/ingress.class: nginx  #注释名称需为nginx(不可省略)

spec:
  tls:
  - hosts:
    - www.nginx.com         #指定域名使用的密钥
    - www.tomcat.com        #指定域名使用的密钥
    secretName: tls-secret  #指定密钥

  rules:                         #定义主机列表
  - host: www.nginx.com          #自定义域名
    http:
      paths:
      - pathType: Prefix         #路径类型
        path: "/"                #定义站点路径
        backend:                 #定义后端引用的服务
          service:               #关联service
            name: svc-nginx      #对应上面创建的service名称
            port:
              number: 80          #service端口


  - host: www.tomcat.com          #自定义域名
    http:
      paths:
      - pathType: Prefix         #路径类型
        path: "/"                #定义站点路径
        backend:                 #定义后端引用的服务
          service:               #关联service
            name: svc-tomcat      #对应上面创建的service名称
            port:
              number: 8080          #service端口



                  
创建Pod
[root@master01 ~]# kubectl create -f ingress-https.yml 
ingress.extensions/ingress-https created


查看ingress信息
[root@master01 ~]# kubectl get ing ingress-https -n test
NAME            CLASS    HOSTS                          ADDRESS        PORTS     AGE
ingress-https   <none>   www.nginx.com,www.tomcat.com   192.168.0.13   80, 443   5m37s



查看详细信息
[root@master ~]# kubectl describe ing ingress-https -n test
...

  tls-secret terminates www.nginx.com,www.tomcat.com  #密钥
  
...
```

<font style="color:rgb(51, 51, 51);">查看ingress-nginx端口</font>

```yaml
[root@master ingress]# kubectl get svc -n ingress-nginx
NAME                                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx-controller             NodePort    192.168.170.2   <none>        80:30655/TCP,443:31706/TCP   25m
ingress-nginx-controller-admission   ClusterIP   192.168.1.11    <none>        443/TCP  
```

<font style="color:rgb(51, 51, 51);">访问测试（注意协议https）：访问443对应的端口</font>

```yaml
curl -k https://www.tomcat.com:31706
curl -k https://www.nginx.com:31706
```

