**<font style="color:rgb(119, 119, 119);">APIService安全控制</font>**

![](../../images/1733054247494-47ae0594-6858-4ee7-9fb8-9ad10208a98c.png)

+ <font style="color:rgb(51, 51, 51);">Authentication：身份认证</font>
    1. <font style="color:rgb(51, 51, 51);">这个环节它面对的输入是整个</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">http request</font>`<font style="color:rgb(51, 51, 51);">，负责对来自client的请求进行身份校验，支持的方法包括:</font>
    - <font style="color:rgb(51, 51, 51);">client证书验证（https双向验证）</font>
    - `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">basic auth</font>`
    - <font style="color:rgb(51, 51, 51);">普通token</font>
    - `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">jwt token</font>`<font style="color:rgb(51, 51, 51);">(用于serviceaccount)</font>
    1. <font style="color:rgb(51, 51, 51);">APIServer启动时，可以指定一种Authentication方法，也可以指定多种方法。如果指定了多种方法，那么APIServer将会逐个使用这些方法对客户端请求进行验证， 只要请求数据通过其中一种方法的验证，APIServer就会认为Authentication成功；</font>
    2. <font style="color:rgb(51, 51, 51);">使用kubeadm引导启动的k8s集群的apiserver初始配置中，默认支持</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">client证书</font>`<font style="color:rgb(51, 51, 51);">验证和</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">serviceaccount</font>`<font style="color:rgb(51, 51, 51);">两种身份验证方式。 证书认证通过设置</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">--client-ca-file</font>`<font style="color:rgb(51, 51, 51);">根证书以及</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">--tls-cert-file</font>`<font style="color:rgb(51, 51, 51);">和</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">--tls-private-key-file</font>`<font style="color:rgb(51, 51, 51);">来开启。</font>
    3. <font style="color:rgb(51, 51, 51);">在这个环节，apiserver会通过client证书或 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">http header</font>`<font style="color:rgb(51, 51, 51);">中的字段(比如serviceaccount的</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">jwt token</font>`<font style="color:rgb(51, 51, 51);">)来识别出请求的</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">用户身份</font>`<font style="color:rgb(51, 51, 51);">，包括”user”、”group”等，这些信息将在后面的</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">authorization</font>`<font style="color:rgb(51, 51, 51);">环节用到。</font>
+ <font style="color:rgb(51, 51, 51);">Authorization：鉴权，你可以访问哪些资源</font>
    1. <font style="color:rgb(51, 51, 51);">这个环节面对的输入是</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">http request context</font>`<font style="color:rgb(51, 51, 51);">中的各种属性，包括：</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">user</font>`<font style="color:rgb(51, 51, 51);">、</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">group</font>`<font style="color:rgb(51, 51, 51);">、</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">request path</font>`<font style="color:rgb(51, 51, 51);">（比如：</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/api/v1</font>`<font style="color:rgb(51, 51, 51);">、</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/healthz</font>`<font style="color:rgb(51, 51, 51);">、</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/version</font>`<font style="color:rgb(51, 51, 51);">等）、 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">request verb</font>`<font style="color:rgb(51, 51, 51);">(比如：</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">get</font>`<font style="color:rgb(51, 51, 51);">、</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">list</font>`<font style="color:rgb(51, 51, 51);">、</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">create</font>`<font style="color:rgb(51, 51, 51);">等)。</font>
    2. <font style="color:rgb(51, 51, 51);">APIServer会将这些属性值与事先配置好的访问策略(</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">access policy</font>`<font style="color:rgb(51, 51, 51);">）相比较。APIServer支持多种</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">authorization mode</font>`<font style="color:rgb(51, 51, 51);">，包括</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">Node、RBAC、Webhook</font>`<font style="color:rgb(51, 51, 51);">等。</font>
    3. <font style="color:rgb(51, 51, 51);">APIServer启动时，可以指定一种</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">authorization mode</font>`<font style="color:rgb(51, 51, 51);">，也可以指定多种</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">authorization mode</font>`<font style="color:rgb(51, 51, 51);">，如果是后者，只要Request通过了其中一种mode的授权， 那么该环节的最终结果就是授权成功。在较新版本kubeadm引导启动的k8s集群的apiserver初始配置中，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">authorization-mode</font>`<font style="color:rgb(51, 51, 51);">的默认配置是</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">”Node,RBAC”</font>`<font style="color:rgb(51, 51, 51);">。</font>
+ <font style="color:rgb(51, 51, 51);">Admission Control：</font>[<font style="color:rgb(51, 51, 51);">准入控制</font>](http://docs.kubernetes.org.cn/144.html)<font style="color:rgb(51, 51, 51);">，一个控制链(层层关卡)，偏集群安全控制、管理方面。为什么说是安全相关的机制？</font>
    - <font style="color:rgb(51, 51, 51);">以NamespaceLifecycle为例， 该插件确保处于Termination状态的Namespace不再接收新的对象创建请求，并拒绝请求不存在的Namespace。该插件还可以防止删除系统保留的Namespace:default，kube-system，kube-public。 </font>
    - <font style="color:rgb(51, 51, 51);">NodeRestriction， 此插件限制kubelet修改Node和Pod对象，这样的kubelets只允许修改绑定到Node的Pod API对象，以后版本可能会增加额外的限制 。</font>

<font style="color:rgb(51, 51, 51);">为什么我们执行命令kubectl命令，可以直接管理k8s集群资源？</font>

###### <font style="color:rgb(119, 119, 119);">kubectl的认证授权</font>
<font style="color:rgb(51, 51, 51);">kubectl的日志调试级别：</font>

| **<font style="color:rgb(51, 51, 51);">信息</font>** | **<font style="color:rgb(51, 51, 51);">描述</font>** |
| :--- | :--- |
| <font style="color:rgb(51, 51, 51);">v=0</font> | <font style="color:rgb(51, 51, 51);">通常，这对操作者来说总是可见的。</font> |
| <font style="color:rgb(51, 51, 51);">v=1</font> | <font style="color:rgb(51, 51, 51);">当您不想要很详细的输出时，这个是一个合理的默认日志级别。</font> |
| <font style="color:rgb(51, 51, 51);">v=2</font> | <font style="color:rgb(51, 51, 51);">有关服务和重要日志消息的有用稳定状态信息，这些信息可能与系统中的重大更改相关。这是大多数系统推荐的默认日志级别。</font> |
| <font style="color:rgb(51, 51, 51);">v=3</font> | <font style="color:rgb(51, 51, 51);">关于更改的扩展信息。</font> |
| <font style="color:rgb(51, 51, 51);">v=4</font> | <font style="color:rgb(51, 51, 51);">调试级别信息。</font> |
| <font style="color:rgb(51, 51, 51);">v=6</font> | <font style="color:rgb(51, 51, 51);">显示请求资源。</font> |
| <font style="color:rgb(51, 51, 51);">v=7</font> | <font style="color:rgb(51, 51, 51);">显示 HTTP 请求头。</font> |
| <font style="color:rgb(51, 51, 51);">v=8</font> | <font style="color:rgb(51, 51, 51);">显示 HTTP 请求内容。</font> |
| <font style="color:rgb(51, 51, 51);">v=9</font> | <font style="color:rgb(51, 51, 51);">显示 HTTP 请求内容，并且不截断内容。</font> |


```yaml
$ kubectl get nodes -v=7
I0329 20:20:08.633065    3979 loader.go:359] Config loaded from file /root/.kube/config
I0329 20:20:08.633797    3979 round_trippers.go:416] GET https://192.168.136.128:6443/api/v1/nodes?limit=500
```

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubeadm init</font>`<font style="color:rgb(51, 51, 51);">启动完master节点后，会默认输出类似下面的提示内容：</font>

```yaml
... ...
Your Kubernetes master has initialized successfully!

To start using your cluster, you need to run the following as a regular user:
  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config
... ...
```

<font style="color:rgb(51, 51, 51);">这些信息是在告知我们如何配置</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubeconfig</font>`<font style="color:rgb(51, 51, 51);">文件。按照上述命令配置后，master节点上的</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl</font>`<font style="color:rgb(51, 51, 51);">就可以直接使用</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">$HOME/.kube/config</font>`<font style="color:rgb(51, 51, 51);">的信息访问</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">k8s cluster</font>`<font style="color:rgb(51, 51, 51);">了。 并且，通过这种配置方式，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl</font>`<font style="color:rgb(51, 51, 51);">也拥有了整个集群的管理员(root)权限。</font>

<font style="color:rgb(51, 51, 51);">很多K8s初学者在这里都会有疑问：</font>

+ <font style="color:rgb(51, 51, 51);">当</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl</font>`<font style="color:rgb(51, 51, 51);">使用这种</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubeconfig</font>`<font style="color:rgb(51, 51, 51);">方式访问集群时，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">Kubernetes</font>`<font style="color:rgb(51, 51, 51);">的</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kube-apiserver</font>`<font style="color:rgb(51, 51, 51);">是如何对来自</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl</font>`<font style="color:rgb(51, 51, 51);">的访问进行身份验证(</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">authentication</font>`<font style="color:rgb(51, 51, 51);">)和授权(</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">authorization</font>`<font style="color:rgb(51, 51, 51);">)的呢？</font>
+ <font style="color:rgb(51, 51, 51);">为什么来自</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl</font>`<font style="color:rgb(51, 51, 51);">的请求拥有最高的管理员权限呢？</font>

<font style="color:rgb(51, 51, 51);">查看</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/root/.kube/config</font>`<font style="color:rgb(51, 51, 51);">文件：</font>

<font style="color:rgb(51, 51, 51);">前面提到过apiserver的authentication支持通过</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">tls client certificate、basic auth、token</font>`<font style="color:rgb(51, 51, 51);">等方式对客户端发起的请求进行身份校验， 从kubeconfig信息来看，kubectl显然在请求中使用了</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">tls client certificate</font>`<font style="color:rgb(51, 51, 51);">的方式，即客户端的证书。 </font>

<font style="color:rgb(51, 51, 51);">证书base64解码：</font>

$ echo xxxxxxxxxxxxxx |base64 -d > kubectl.crt

<font style="color:rgb(51, 51, 51);">说明在认证阶段，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">apiserver</font>`<font style="color:rgb(51, 51, 51);">会首先使用</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">--client-ca-file</font>`<font style="color:rgb(51, 51, 51);">配置的CA证书去验证kubectl提供的证书的有效性,基本的方式 ：</font>

```yaml
$  openssl verify -CAfile /etc/kubernetes/pki/ca.crt kubectl.crt
kubectl.crt: OK
```

<font style="color:rgb(51, 51, 51);">除了认证身份，还会取出必要的信息供授权阶段使用，文本形式查看证书内容：</font>

```yaml
$ openssl x509 -in kubectl.crt -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 4736260165981664452 (0x41ba9386f52b74c4)
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=kubernetes
        Validity
            Not Before: Feb 10 07:33:39 2020 GMT
            Not After : Feb  9 07:33:40 2021 GMT
        Subject: O=system:masters, CN=kubernetes-admin
        ...
```

<font style="color:rgb(51, 51, 51);">认证通过后，提取出签发证书时指定的CN(Common Name),</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubernetes-admin</font>`<font style="color:rgb(51, 51, 51);">，作为请求的用户名 (User Name), 从证书中提取O(Organization)字段作为请求用户所属的组 (Group)，</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">group = system:masters</font>`<font style="color:rgb(51, 51, 51);">，然后传递给后面的授权模块。</font>

<font style="color:rgb(51, 51, 51);">kubeadm在init初始引导集群启动过程中，创建了许多</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">default</font>`<font style="color:rgb(51, 51, 51);">的</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">role、clusterrole、rolebinding</font>`<font style="color:rgb(51, 51, 51);">和</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">clusterrolebinding</font>`<font style="color:rgb(51, 51, 51);">， 在k8s有关RBAC的官方文档中，我们看到下面一些</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">default clusterrole</font>`<font style="color:rgb(51, 51, 51);">列表: </font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">其中第一个cluster-admin这个cluster role binding绑定了system:masters group，这和authentication环节传递过来的身份信息不谋而合。 沿着system:masters group对应的cluster-admin clusterrolebinding“追查”下去，真相就会浮出水面。</font>

<font style="color:rgb(51, 51, 51);">我们查看一下这一binding：</font>

```yaml
$ kubectl describe clusterrolebinding cluster-admin
Name:         cluster-admin
Labels:       kubernetes.io/bootstrapping=rbac-defaults
Annotations:  rbac.authorization.kubernetes.io/autoupdate: true
Role:
  Kind:  ClusterRole
  Name:  cluster-admin
Subjects:
  Kind   Name            Namespace
  ----   ----            ---------
  Group  system:masters
```

<font style="color:rgb(51, 51, 51);">我们看到在kube-system名字空间中，一个名为cluster-admin的clusterrolebinding将cluster-admin cluster role与system:masters Group绑定到了一起， 赋予了所有归属于system:masters Group中用户cluster-admin角色所拥有的权限。</font>

<font style="color:rgb(51, 51, 51);">我们再来查看一下cluster-admin这个role的具体权限信息：</font>

```yaml
$ kubectl describe clusterrole cluster-admin
Name:         cluster-admin
Labels:       kubernetes.io/bootstrapping=rbac-defaults
Annotations:  rbac.authorization.kubernetes.io/autoupdate: true
PolicyRule:
  Resources  Non-Resource URLs  Resource Names  Verbs
  ---------  -----------------  --------------  -----
  *.*        []                 []              [*]
             [*]                []              [*]
```

<font style="color:rgb(51, 51, 51);">非资源类，如查看集群健康状态。</font>

![](../../images/1733054309066-ea14655b-125e-4e06-8e71-3246ebd52640.png)

###### <font style="color:rgb(119, 119, 119);">RBAC</font>
Role-Based Access Control，基于角色的访问控制， apiserver启动参数添加--authorization-mode=RBAC 来启用RBAC认证模式，kubeadm安装的集群默认已开启。[官方介绍](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

查看开启：

```yaml
# master节点查看apiserver进程
$ ps aux |grep apiserver
```

RBAC模式引入了4个资源：

+ Role，角色

一个Role只能授权访问单个namespace 

```yaml
## 示例定义一个名为pod-reader的角色，该角色具有读取default这个命名空间下的pods的权限
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""] # "" indicates the core API group
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
  
## apiGroups: "","apps", "autoscaling", "batch", kubectl api-versions
## resources: "services", "pods","deployments"... kubectl api-resources
## verbs: "get", "list", "watch", "create", "update", "patch", "delete", "exec"
```

+ ClusterRole

一个ClusterRole能够授予和Role一样的权限，但是它是集群范围内的。 

```yaml
## 定义一个集群角色，名为secret-reader，该角色可以读取所有的namespace中的secret资源
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  # "namespace" omitted since ClusterRoles are not namespaced
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "watch", "list"]
```

+ Rolebinding

将role中定义的权限分配给用户和用户组。RoleBinding包含主题（users,groups,或service accounts）和授予角色的引用。对于namespace内的授权使用RoleBinding，集群范围内使用ClusterRoleBinding。

```yaml
## 定义一个角色绑定，将pod-reader这个role的权限授予给jane这个User，使得jane可以在读取default这个命名空间下的所有的pod数据
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: User   #这里可以是User,Group,ServiceAccount
  name: jane 
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role #这里可以是Role或者ClusterRole,若是ClusterRole，则权限也仅限于rolebinding的内部
  name: pod-reader # match the name of the Role or ClusterRole you wish to bind to
  apiGroup: rbac.authorization.k8s.io
```

_注意：rolebinding既可以绑定role，也可以绑定clusterrole，当绑定clusterrole的时候，subject的权限也会被限定于rolebinding定义的namespace内部，若想跨namespace，需要使用clusterrolebinding_

```yaml
## 定义一个角色绑定，将dave这个用户和secret-reader这个集群角色绑定，虽然secret-reader是集群角色，但是因为是使用rolebinding绑定的，因此dave的权限也会被限制在development这个命名空间内
apiVersion: rbac.authorization.k8s.io/v1
# This role binding allows "dave" to read secrets in the "development" namespace.
# You need to already have a ClusterRole named "secret-reader".
kind: RoleBinding
metadata:
  name: read-secrets
  #
  # The namespace of the RoleBinding determines where the permissions are granted.
  # This only grants permissions within the "development" namespace.
  namespace: development
subjects:
- kind: User
  name: dave # Name is case sensitive
  apiGroup: rbac.authorization.k8s.io
- kind: ServiceAccount
  name: dave # Name is case sensitive
  namespace: demo
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

考虑一个场景： 如果集群中有多个namespace分配给不同的管理员，每个namespace的权限是一样的，就可以只定义一个clusterrole，然后通过rolebinding将不同的namespace绑定到管理员身上，否则就需要每个namespace定义一个Role，然后做一次rolebinding。

+ <font style="color:rgb(51, 51, 51);">ClusterRolebingding</font>

<font style="color:rgb(51, 51, 51);">允许跨namespace进行授权</font>

```yaml
apiVersion: rbac.authorization.k8s.io/v1
# This cluster role binding allows anyone in the "manager" group to read secrets in any namespace.
kind: ClusterRoleBinding
metadata:
  name: read-secrets-global
subjects:
- kind: Group
  name: manager # Name is case sensitive
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

  
![](../../images/1733054329989-6e743892-242e-4bca-85dc-97deb8bfc8b8.png)

###### <font style="color:rgb(119, 119, 119);">kubelet的认证授权</font>
<font style="color:rgb(51, 51, 51);">查看kubelet进程</font>

```yaml
$ systemctl status kubelet
● kubelet.service - kubelet: The Kubernetes Node Agent
   Loaded: loaded (/etc/systemd/system/kubelet.service; enabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/kubelet.service.d
           └─10-kubeadm.conf
   Active: active (running) since Wed 2020-04-01 02:34:13 CST; 1 day 14h ago
     Docs: https://kubernetes.io/docs/
 Main PID: 851 (kubelet)
    Tasks: 21
   Memory: 127.1M
   CGroup: /system.slice/kubelet.service
           └─851 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf
```

<font style="color:rgb(51, 51, 51);">查看</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">/etc/kubernetes/kubelet.conf</font>`<font style="color:rgb(51, 51, 51);">，解析证书：</font>

```yaml
$ echo xxxxx |base64 -d >kubelet.crt
$ openssl x509 -in kubelet.crt -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 9059794385454520113 (0x7dbadafe23185731)
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN=kubernetes
        Validity
            Not Before: Feb 10 07:33:39 2020 GMT
            Not After : Feb  9 07:33:40 2021 GMT
        Subject: O=system:nodes, CN=system:node:master-1
```

<font style="color:rgb(51, 51, 51);">得到我们期望的内容：</font>

Subject: O=system:nodes, CN=system:node:k8s-master

<font style="color:rgb(51, 51, 51);">我们知道，k8s会把O作为Group来进行请求，因此如果有权限绑定给这个组，肯定在clusterrolebinding的定义中可以找得到。因此尝试去找一下绑定了system:nodes组的clusterrolebinding</font>

```yaml
$ kubectl get clusterrolebinding|awk 'NR>1{print $1}'|xargs kubectl get clusterrolebinding -oyaml|grep -n10 system:nodes
98-  roleRef:
99-    apiGroup: rbac.authorization.k8s.io
100-    kind: ClusterRole
101-    name: system:certificates.k8s.io:certificatesigningrequests:selfnodeclient
102-  subjects:
103-  - apiGroup: rbac.authorization.k8s.io
104-    kind: Group
105:    name: system:nodes
106-- apiVersion: rbac.authorization.k8s.io/v1
107-  kind: ClusterRoleBinding
108-  metadata:
109-    creationTimestamp: "2020-02-10T07:34:02Z"
110-    name: kubeadm:node-proxier
111-    resourceVersion: "213"
112-    selfLink: /apis/rbac.authorization.k8s.io/v1/clusterrolebindings/kubeadm%3Anode-proxier

$ kubectl describe clusterrole system:certificates.k8s.io:certificatesigningrequests:selfnodeclient
Name:         system:certificates.k8s.io:certificatesigningrequests:selfnodeclient
Labels:       kubernetes.io/bootstrapping=rbac-defaults
Annotations:  rbac.authorization.kubernetes.io/autoupdate: true
PolicyRule:
  Resources                                                      Non-Resource URLs  Resource Names  Verbs
  ---------                                                      -----------------  --------------  -----
  certificatesigningrequests.certificates.k8s.io/selfnodeclient  []                 []              [create]
```

<font style="color:rgb(51, 51, 51);">结局有点意外，除了</font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">system:certificates.k8s.io:certificatesigningrequests:selfnodeclient</font>`<font style="color:rgb(51, 51, 51);">外，没有找到system相关的rolebindings，显然和我们的理解不一样。 尝试去找</font>[<font style="color:rgb(51, 51, 51);">资料</font>](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)<font style="color:rgb(51, 51, 51);">，发现了这么一段 :</font>

| **<font style="color:rgb(51, 51, 51);">Default ClusterRole</font>** | **<font style="color:rgb(51, 51, 51);">Default ClusterRoleBinding</font>** | **<font style="color:rgb(51, 51, 51);">Description</font>** |
| :--- | :--- | :--- |
| <font style="color:rgb(51, 51, 51);">system:kube-scheduler</font> | <font style="color:rgb(51, 51, 51);">system:kube-scheduler user</font> | <font style="color:rgb(51, 51, 51);">Allows access to the resources required by the </font>[<font style="color:rgb(51, 51, 51);">scheduler</font>](https://kubernetes.io/docs/reference/generated/kube-scheduler/)<br/><font style="color:rgb(51, 51, 51);">component.</font> |
| <font style="color:rgb(51, 51, 51);">system:volume-scheduler</font> | <font style="color:rgb(51, 51, 51);">system:kube-scheduler user</font> | <font style="color:rgb(51, 51, 51);">Allows access to the volume resources required by the kube-scheduler component.</font> |
| <font style="color:rgb(51, 51, 51);">system:kube-controller-manager</font> | <font style="color:rgb(51, 51, 51);">system:kube-controller-manager user</font> | <font style="color:rgb(51, 51, 51);">Allows access to the resources required by the </font>[<font style="color:rgb(51, 51, 51);">controller manager</font>](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)<br/><font style="color:rgb(51, 51, 51);"> component. The permissions required by individual controllers are detailed in the </font>[<font style="color:rgb(51, 51, 51);">controller roles</font>](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#controller-roles)<br/><font style="color:rgb(51, 51, 51);">.</font> |
| <font style="color:rgb(51, 51, 51);">system:node</font> | <font style="color:rgb(51, 51, 51);">None</font> | <font style="color:rgb(51, 51, 51);">Allows access to resources required by the kubelet, </font>**<font style="color:rgb(51, 51, 51);">including read access to all secrets, and write access to all pod status objects</font>**<font style="color:rgb(51, 51, 51);">. You should use the </font>[<font style="color:rgb(51, 51, 51);">Node authorizer</font>](https://kubernetes.io/docs/reference/access-authn-authz/node/)<br/><font style="color:rgb(51, 51, 51);"> and </font>[<font style="color:rgb(51, 51, 51);">NodeRestriction admission plugin</font>](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction)<br/><font style="color:rgb(51, 51, 51);"> instead of the </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">system:node</font>`<br/><font style="color:rgb(51, 51, 51);"> role, and allow granting API access to kubelets based on the Pods scheduled to run on them. The </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">system:node</font>`<br/><font style="color:rgb(51, 51, 51);"> role only exists for compatibility with Kubernetes clusters upgraded from versions prior to v1.8.</font> |
| <font style="color:rgb(51, 51, 51);">system:node-proxier</font> | <font style="color:rgb(51, 51, 51);">system:kube-proxy user</font> | <font style="color:rgb(51, 51, 51);">Allows access to the resources required by the </font>[<font style="color:rgb(51, 51, 51);">kube-proxy</font>](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)<br/><font style="color:rgb(51, 51, 51);">component.</font> |


<font style="color:rgb(51, 51, 51);">大致意思是说：之前会定义system:node这个角色，目的是为了kubelet可以访问到必要的资源，包括所有secret的读权限及更新pod状态的写权限。如果1.8版本后，是建议使用 </font>[<font style="color:rgb(51, 51, 51);">Node authorizer</font>](https://kubernetes.io/docs/reference/access-authn-authz/node/)<font style="color:rgb(51, 51, 51);"> and </font>[<font style="color:rgb(51, 51, 51);">NodeRestriction admission plugin</font>](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction)<font style="color:rgb(51, 51, 51);"> 来代替这个角色的。</font>

<font style="color:rgb(51, 51, 51);">我们目前使用1.16，查看一下授权策略：</font>

```yaml
$ ps axu|grep apiserver
kube-apiserver --authorization-mode=Node,RBAC  --enable-admission-plugins=NodeRestriction
```

<font style="color:rgb(51, 51, 51);">查看一下官网对Node authorizer的介绍：</font>

_<font style="color:rgb(51, 51, 51);">Node authorization is a special-purpose authorization mode that specifically authorizes API requests made by kubelets.</font>_

_<font style="color:rgb(51, 51, 51);">In future releases, the node authorizer may add or remove permissions to ensure kubelets have the minimal set of permissions required to operate correctly.</font>_

_<font style="color:rgb(51, 51, 51);">In order to be authorized by the Node authorizer, kubelets must use a credential that identifies them as being in the </font>_`_<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">system:nodes</font>_`_<font style="color:rgb(51, 51, 51);"> group, with a username of </font>_`_<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">system:node:<nodeName></font>_`

###### <font style="color:rgb(119, 119, 119);">Service Account</font>
<font style="color:rgb(51, 51, 51);">前面说，认证可以通过证书，也可以通过使用ServiceAccount（服务账户）的方式来做认证。大多数时候，我们在基于k8s做二次开发时都是选择通过serviceaccount的方式。我们之前访问dashboard的时候，是如何做的？</font>

```yaml
## 新建一个名为admin的serviceaccount，并且把名为cluster-admin的这个集群角色的权限授予新建的serviceaccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin
  namespace: kubernetes-dashboard
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: admin
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
subjects:
- kind: ServiceAccount
  name: admin
  namespace: kubernetes-dashboard
```

<font style="color:rgb(51, 51, 51);">我们查看一下：</font>

```yaml
$ kubectl -n kubernetes-dashboard get sa admin -o yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  creationTimestamp: "2020-04-01T11:59:21Z"
  name: admin
  namespace: kubernetes-dashboard
  resourceVersion: "1988878"
  selfLink: /api/v1/namespaces/kubernetes-dashboard/serviceaccounts/admin
  uid: 639ecc3e-74d9-11ea-a59b-000c29dfd73f
secrets:
- name: admin-token-lfsrf
```

<font style="color:rgb(51, 51, 51);">注意到serviceaccount上默认绑定了一个名为admin-token-lfsrf的secret，我们查看一下secret</font>

```yaml
$ kubectl -n kubernetes-dashboard describe secret admin-token-lfsrf
Name:         admin-token-lfsrf
Namespace:    kubernetes-dashboard
Labels:       <none>
Annotations:  kubernetes.io/service-account.name: admin
              kubernetes.io/service-account.uid: 639ecc3e-74d9-11ea-a59b-000c29dfd73f

Type:  kubernetes.io/service-account-token
Data
====
ca.crt:     1025 bytes
namespace:  4 bytes
token:      eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZW1vIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFkbWluLXRva2VuLWxmc3JmIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiNjM5ZWNjM2UtNzRkOS0xMWVhLWE1OWItMDAwYzI5ZGZkNzNmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlbW86YWRtaW4ifQ.ffGCU4L5LxTsMx3NcNixpjT6nLBi-pmstb4I-W61nLOzNaMmYSEIwAaugKMzNR-2VwM14WbuG04dOeO67niJeP6n8-ALkl-vineoYCsUjrzJ09qpM3TNUPatHFqyjcqJ87h4VKZEqk2qCCmLxB6AGbEHpVFkoge40vHs56cIymFGZLe53JZkhu3pwYuS4jpXytV30Ad-HwmQDUu_Xqcifni6tDYPCfKz2CZlcOfwqHeGIHJjDGVBKqhEeo8PhStoofBU6Y4OjObP7HGuTY-Foo4QindNnpp0QU6vSb7kiOiQ4twpayybH8PTf73dtdFt46UF6mGjskWgevgolvmO8A
```

<font style="color:rgb(51, 51, 51);">开发的时候如何去调用k8s的api:</font>

1. <font style="color:rgb(51, 51, 51);">curl演示</font>

```yaml
$ curl -k  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkZW1vIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFkbWluLXRva2VuLWxmc3JmIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiNjM5ZWNjM2UtNzRkOS0xMWVhLWE1OWItMDAwYzI5ZGZkNzNmIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlbW86YWRtaW4ifQ.ffGCU4L5LxTsMx3NcNixpjT6nLBi-pmstb4I-W61nLOzNaMmYSEIwAaugKMzNR-2VwM14WbuG04dOeO67niJeP6n8-ALkl-vineoYCsUjrzJ09qpM3TNUPatHFqyjcqJ87h4VKZEqk2qCCmLxB6AGbEHpVFkoge40vHs56cIymFGZLe53JZkhu3pwYuS4jpXytV30Ad-HwmQDUu_Xqcifni6tDYPCfKz2CZlcOfwqHeGIHJjDGVBKqhEeo8PhStoofBU6Y4OjObP7HGuTY-Foo4QindNnpp0QU6vSb7kiOiQ4twpayybH8PTf73dtdFt46UF6mGjskWgevgolvmO8A" https://62.234.214.206:6443/api/v1/namespaces/demo/pods?limit=500
```

1. <font style="color:rgb(51, 51, 51);">postman</font>

