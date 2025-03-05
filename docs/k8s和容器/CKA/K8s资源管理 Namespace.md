<font style="color:rgb(51, 51, 51);">Namespace（命名空间）是kubernetes系统中的一种非常重要的资源，它的主要作用是用来实现多套环境的资源隔离（例如生活中的房间）</font>

<font style="color:rgb(51, 51, 51);">默认情况下kubenetes集群中的所有Pod都是可以相互访问的，但如果Pod内运行的应用（例如：nginx与httpd）之间发生冲突，那此时就可以将不同的Pod划分到不同的Namespace（命名空间）进行隔离，可以形成逻辑上的“组”</font>

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：以一个namespace（命名空间）的创建和删除简单演示命令用法</font>

| **<font style="color:rgb(51, 51, 51);">资源名称</font>** | **<font style="color:rgb(51, 51, 51);">缩写</font>** | **<font style="color:rgb(51, 51, 51);">资源作用</font>** |
| :--- | :--- | :--- |
| <font style="color:rgb(51, 51, 51);">namespaces</font> | <font style="color:rgb(51, 51, 51);">ns</font> | <font style="color:rgb(51, 51, 51);">隔离pod</font> |


```plain
查看ns信息
# kubectl get ns
calico-apiserver  calico网络资源命名空间
calico-system     calico网络资源命名空间
default           默认的命名空间，所有未指定的Pod都会被分配在该空间下
kube-node-lease   集群节点之间的心跳维护
kube-public       该命名空间下的资源可以被所有人访问，包括未认证的用户
kube-system       所有由k8s系统创建的资源都处于这个命名空间
tigera-operator   calico网络资源命名空间

查看指定ns的信息
# kubectl get pod -n kube-system

创建一个名为dev的ns
# kubectl create ns dev
# kubectl get ns

删除ns
# kubectl  delete namespace dev
```

#### <font style="color:rgb(51, 51, 51);">资源管理之YAML语言</font>
<font style="color:rgb(51, 51, 51);">k8s中几乎所有的资源都可以通YAML编排来创建。</font>

<font style="color:rgb(51, 51, 51);">YAML是一个类似于XML、JSON的标记性语言，它强调以数据为中心，并不是以标识语言为重点，应为YAML本身的定义比较简单，号称“一种人性化的数据格式语言”。</font>

#### <font style="color:rgb(51, 51, 51);">YAML的语法特点</font>
+ <font style="color:rgb(51, 51, 51);">严格区分大小写</font>
+ <font style="color:rgb(51, 51, 51);">使用缩进表示层级关系</font>
+ <font style="color:rgb(51, 51, 51);">低版本缩进不允许使用tab键，只允许使用空格，缩进的空格数量没有严格要求，只要相同层级左对齐即可</font>
+ `<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">#</font>`<font style="color:rgb(51, 51, 51);"> 号表示注释</font>
+ <font style="color:rgb(51, 51, 51);">书写YAML切记 : 后边要加一个空格</font>
+ <font style="color:rgb(51, 51, 51);">如果需要将多段YAML配置放在同一个文件中，中间需要用 --- 作为分格</font>

#### <font style="color:rgb(51, 51, 51);">YAML常用数据结构</font>
+ <font style="color:rgb(51, 51, 51);">对象（Object）：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）</font>
+ <font style="color:rgb(51, 51, 51);">数组：一组按次序排列的值，又称为序列（sequence） / 列表 （list）</font>

<font style="color:rgb(51, 51, 51);">对象类型：对象的一组键值对，使用冒号结构表示</font>

```plain
#对象形式一（推荐）
个人信息:
  name: zhangsan
  age: 30
  address: tianjin
 
#对象形式二（了解）
个人信息: {name: zhangsan，age: 30,address: tianjin}
```

<font style="color:rgb(51, 51, 51);">数组类型：一组连词线开头的行，构成一个数组</font>

```plain
- 联系方式:
  phone: 138****6789
  QQ: 
  WeChat:
  emal:
```

<font style="color:rgb(51, 51, 51);">复合结构：对象和数组可以结合使用，形成复合结构</font>

```plain
个人信息: 
  name: zhangsan
  age: 30
  address: tianjin
  - 联系方式: 
    phone:
    QQ:
    WeChat:
    emal:
```

#### <font style="color:rgb(51, 51, 51);">K8s资源对象描述</font>
<font style="color:rgb(51, 51, 51);">在kubernetes中基本所有资源的一级属性都是一样的，主要分为五部分：</font>

+ <font style="color:rgb(65, 131, 196);">apiVersion</font><font style="color:rgb(51, 51, 51);">：资源版本，由k8s内部定义，版本号必须可以通过kubectl api-versions 查询到</font>
+ <font style="color:rgb(65, 131, 196);">kind</font><font style="color:rgb(51, 51, 51);">：资源类型，由k8s内部定义，类型必须可以通过kubectl api-resources查询到</font>
+ <font style="color:rgb(65, 131, 196);">metadata</font><font style="color:rgb(51, 51, 51);">：元数据，主要是指定资源标识与说明，常用的有name、namespace、labels等</font>
+ <font style="color:rgb(65, 131, 196);">spec</font><font style="color:rgb(51, 51, 51);">：资源描述，这是配置中最重要的一部分，里边对各种资源配置的详细描述</font>
+ <font style="color:rgb(65, 131, 196);">status</font><font style="color:rgb(51, 51, 51);">：资源状态信息，里边的内容不需要定义，有k8s自动生成</font>

#### <font style="color:rgb(51, 51, 51);">YAML文件创建资源</font>
**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过yaml文件创建一个test命名空间</font>

<font style="color:rgb(51, 51, 51);">kubect explain 资源名称 #explain用于查看资源文档</font>

<font style="color:rgb(119, 119, 119);">格式：kubectl explain ns #查看ns文档</font>

<font style="color:rgb(119, 119, 119);">查看子属性用 · 作为分隔，例如：kubectl explain ns.metadata</font>

```plain
# vim ns_test.yaml
apiVersion: v1
kind: Namespace
metadata:
    name: test
```

```plain
执行ns_test.yaml文件创建ns
# kubectl create -f ns_test.yaml


查看ns信息
# kubectl get ns
test

通过yaml文件删除ns
# kubectl delete -f ns_test.yaml
```

<font style="color:rgb(51, 51, 51);">  
</font><font style="color:rgb(51, 51, 51);"> </font>

