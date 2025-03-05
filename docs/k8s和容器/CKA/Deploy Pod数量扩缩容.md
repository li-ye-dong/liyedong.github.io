**<font style="color:rgb(51, 51, 51);">案例</font>**<font style="color:rgb(51, 51, 51);">：通过Deploy对pod数量进行扩缩容</font>

```yaml
创建Pod
# kubectl create -f deploy_nginx.yml
# kubectl get pod -n test


通过edit（修改配置文件）方式扩容pod数量
# kubectl get deploy -n test
# kubectl edit deploy deploy-nginx -n test
...
  replicas: 2    #修改pod数量


查看pod信息
# kubectl get pod -n test


删除deploy
# kubectl delete -f deploy_nginx.yml
```

  
 

