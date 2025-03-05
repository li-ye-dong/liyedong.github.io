<font style="color:rgb(51, 51, 51);">实验准备：</font>

<font style="color:rgb(51, 51, 51);">1）为了演示污点的效果更加明显，暂时停止worker02节点，将worker02节点关机即可，关机后验证节点状态。</font>

```yaml
# kubectl get nodes
...
worker02   NotReady
```

<font style="color:rgb(51, 51, 51);">2）将前边案例配置文件中定向调度删除后在进行创建，否则看不到效果。</font>

```yaml
# vim deploy_nginx.yml
```

<font style="color:rgb(51, 51, 51);">3）为worker01设置污点，名称为：worker01:PreferNoSchedule</font>

```yaml
[root@master01 ~]# kubectl taint node worker01 worker01:PreferNoSchedule


查看污点信息
[root@master01 ~]#  kubectl describe node worker01 | grep Taints

Taints:     worker01:PreferNoSchedule



创建Pod验证
[root@master01 ~]# kubectl create -f deploy_nginx.yml


查看Pod所在节点健康状态
[root@master01 ~]# kubectl get pod -n test -o wide


删除deploy
[root@master01 ~]# kubectl delete -f deploy_nginx.yml


删除PreferNoSchedule污点
[root@master01 ~]# kubectl taint node worker01 worker01:PreferNoSchedule-
```

  
 

