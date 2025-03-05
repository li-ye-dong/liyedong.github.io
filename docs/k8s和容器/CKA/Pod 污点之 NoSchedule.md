<font style="color:rgb(51, 51, 51);">设置worker01污点为：worker01:NoSchedule</font>

```yaml
[root@master01 ~]# kubectl taint node worker01 worker01:NoSchedule


查看污点信息
[root@master01 ~]# kubectl describe node worker01 | grep Taints
Taints:             worker01:NoSchedule



创建Pod
[root@master01 ~]# kubectl create -f deploy_nginx.yml



查看Pod所在节点健康状态
[root@master01 ~]# kubectl get pod -n test -o wide
#提示：可以发现当前的pod状态为Pending（挂起状态）



删除deploy
[root@master01 ~]# kubectl delete -f deploy_nginx.yml
```

<font style="color:rgb(65, 131, 196);">提示</font><font style="color:rgb(51, 51, 51);">：使用kubeadm搭建的集群，默认就会给master节点添加一个污点，所以pod不会被调度到master节点。</font>

```yaml
#  kubectl describe node master01 | grep Taints
Taints:   node-role.kubernetes.io/master:NoSchedule

#  kubectl describe node master02 | grep Taints
Taints:   node-role.kubernetes.io/master:NoSchedule

#  kubectl describe node master03 | grep Taints
Taints:   node.kubernetes.io/unreachable:NoExecute
```

  
 

