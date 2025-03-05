<font style="color:rgb(51, 51, 51);">容器一旦出现了问题，K8s就会对容器所在的pod进行重启，重启操作是由pod的重启策略决定的，pod的重启策略有三种，可通过下边命令查看</font>

```plain
[root@master ~]# kubectl explain pod.spec.restartPolicy
```

<font style="color:rgb(119, 119, 119);">Always：容器失效时，自动重启该容器，默认策略</font>

<font style="color:rgb(119, 119, 119);">OnFailure：容器终止运行且退出码不为0时重启（异常终止）</font>

<font style="color:rgb(119, 119, 119);">Never：无论容器状态如何，都不重启该容器</font>

<font style="color:rgb(51, 51, 51);">重启策略适用于pod中的所有容器，首次需要重启的容器，将在其需要时立即进行重启，随后再次需要重启的操作将由kubelet延迟一段时间后进行，且反复的重启操作延时时长为10s、20s、40s、80s、160s、300s，最长延时为300s，以后重启延时均为300s，直至重启成功</font>

