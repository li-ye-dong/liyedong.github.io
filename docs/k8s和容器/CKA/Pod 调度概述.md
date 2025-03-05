#### <font style="color:rgb(51, 51, 51);"></font>
<font style="color:rgb(51, 51, 51);">在默认情况下，一个pod被调度到哪个Node节点运行是由Scheduler组件采用相应的算法计算出来的，这个过程是不受人工控制的，但是在实际工作中，我们想要控制某些pod调度到指定的Node节点，就需要用到pod调度</font>

<font style="color:rgb(51, 51, 51);">k8s提供了四种调度方式：</font>

+ <font style="color:rgb(51, 51, 51);">自动调度：pod运行在哪个Node节点上，完全由Scheduler经过算法分配（默认的调度策略）</font>
+ <font style="color:rgb(51, 51, 51);">定向调度：NodeName、NodeSelector</font>
+ <font style="color:rgb(51, 51, 51);">亲和性调度与反亲和性调度：NodeAffinity、PodAffinity、PodAntiAffinity</font>
+ <font style="color:rgb(51, 51, 51);">污点（容忍）调度：Taints、Toleration</font>

  
 

