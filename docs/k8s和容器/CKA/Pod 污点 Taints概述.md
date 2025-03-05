<font style="color:rgb(51, 51, 51);">前面的调度方式都是站在pod的角度上，通过在pod上添加属性，来确定pod是否要调度到指定的node上，其实我们也可以站在node的角度上，通过在node上添加污点属性，来决定是否允许pod调度过来</font>

<font style="color:rgb(51, 51, 51);">node被设置上污点以后，就和pod之间存在了一种相互排斥的关系，进而拒绝pod调度进来，甚至可以将已经存在的pod驱逐出去</font>

<font style="color:rgb(51, 51, 51);">污点的格式：key=value:污点，key和value是污点的标签，目前支持如下三个污点：</font>

+ <font style="color:rgb(51, 51, 51);">PreferNoSchedule：尽量避免调度（软限制），除非没有其他节点可调度</font>
+ <font style="color:rgb(51, 51, 51);">NoSchedule：拒绝调度（硬限制），但不会影响当前已经存在的pod</font>
+ <font style="color:rgb(51, 51, 51);">NoExecute：拒绝调度，同时也会将节点上已经存在的pod清除（尽量不要设置，会导致Pod异常）</font>

<font style="color:rgb(65, 131, 196);">提示</font><font style="color:rgb(51, 51, 51);">：如果通过定向调度的方式去创建Pod，那么定向调度的优先级要高于污点。</font>

<font style="color:rgb(51, 51, 51);">使用kubectl设置和去除污点的命令实例如下：</font>

```plain
设置污点
kubectl taint nodes worker01 key:污点

去除污点
kubectl taint nodes worker01 key:污点-

去除所有污点
kubectl taint nodes worker01 key-
```

  
 

