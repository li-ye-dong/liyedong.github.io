#### <font style="color:rgb(51, 51, 51);">Label标签概述</font>
<font style="color:rgb(51, 51, 51);">如果k8s集群资源数量非常多，可将给具体的资源打上对应的标签，然后通过标签进行筛选及查看或者管理资源，这样可以更好的进行资源对象的相关选择与匹配。</font>

+ <font style="color:rgb(51, 51, 51);">一个Label会以key/value键值对的形式附加到各种对象上，如Node、Pod、Service等等</font>
+ <font style="color:rgb(51, 51, 51);">一个资源对象可以定义任意数量的Label，同一个Label也可以被添加到任意数量的资源对象上</font>
+ <font style="color:rgb(51, 51, 51);">Label通常在资源对象定义时确定，也可以在对象创建后动态添加或者删除</font>

<font style="color:rgb(51, 51, 51);">常用的Label示例如下：</font>

<font style="color:rgb(119, 119, 119);">版本标签："version":"1.0"</font>

<font style="color:rgb(119, 119, 119);">环境标签："env":"dev","env":"test"</font>

<font style="color:rgb(119, 119, 119);">架构标签："tier":"frontend","tier":"backend"</font>

#### <font style="color:rgb(51, 51, 51);">查看标签信息</font>
```shell
查看node节点标签:--show-labels
# kubectl get node --show-labels

查看pod标签:--show-labels
# kubectl get pod --show-labels
```

#### <font style="color:rgb(51, 51, 51);">设置标签信息</font>
```shell
为pod打version标签：label
# kubectl label pod nginx -n test version=1.0


查看pod标签:--show-labels
# kubectl get pod -n test --show-labels


再次为该pod打标签（一个资源可以定义任意数量的Label）
# kubectl label pod nginx -n test env=test


查看pod标签:--show-labels
# kubectl get pod -n test --show-labels
```

#### <font style="color:rgb(51, 51, 51);">更新标签信息</font>
<font style="color:rgb(51, 51, 51);">更新version标签：--overwrite</font>

```shell
将pod版本标签更新为2.0
# kubectl label pod nginx -n test version=2.0 --overwrite


查看pod标签
# kubectl get pod -n test --show-labels
```

<font style="color:rgb(51, 51, 51);">YAML文件形式更新标签</font>

<font style="color:rgb(119, 119, 119);">kubectl explain pod.metadata #在metadata属性中指定标签信息</font>

```shell
# vim nginx.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: test
  labels:           #定义标签
   version: "3.0"   #标签信息（属性之间缩进一个空格）
spec:
  containers:
  - name: nginxpod
    image: nginx:1.18.0
```

```bash
更新资源
# kubectl apply -f nginx.yaml


查看标签
# kubectl get pod -n test --show-labels
```

#### <font style="color:rgb(51, 51, 51);">标签选择器</font>
<font style="color:rgb(51, 51, 51);">标签定义完毕以后还要考虑标签的筛选，标签选择器主要有2类:</font>

+ <font style="color:rgb(51, 51, 51);">等值关系: =, !=</font>
+ <font style="color:rgb(51, 51, 51);">集合关系: KEY in (VALUE1, VALUE2......)</font>

**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：根据标签选择器筛选pod</font>

```shell
等式筛选：筛选test空间"version=3.0"标签的pod
# kubectl get pod -l "version=3.0" -n test --show-labels


等式筛选：筛选test空间"version!=3.0"标签的pod
# kubectl get pod -l "version!=3.0" -n dev --show-labels


集合筛选：version in(3.0) 包含3.0
# kubectl get pod -l "version in (3.0)" -n test --show-labels


集合筛选：version notin(3.0) 排除3.0
kubectl get pod -l "version notin (3.0)" -n test --show-labels
```

#### <font style="color:rgb(51, 51, 51);">标签删除</font>
<font style="color:rgb(51, 51, 51);">使用key加一个 </font>`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">-</font>`<font style="color:rgb(51, 51, 51);"> （减号）的写法来删除标签</font>

```shell
删除标签：标签名-
# kubectl label pod nginx -n test version-


查看标签
# kubectl get pod nginx -n test --show-labels
```

<font style="color:rgb(119, 119, 119);">  
</font><font style="color:rgb(119, 119, 119);"> </font>

