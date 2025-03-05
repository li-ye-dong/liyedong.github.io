<font style="color:rgb(51, 51, 51);">Deploy支持版本升级过程中的暂停、继续、回退等功能，具体功能如下：</font>

`<font style="color:rgb(51, 51, 51);background-color:rgb(243, 244, 244);">kubectl rollout</font>`<font style="color:rgb(51, 51, 51);"> 版本升级相关功能，支持下面的选项：</font>

+ <font style="color:rgb(51, 51, 51);">status #显示当前升级状态</font>
+ <font style="color:rgb(51, 51, 51);">history #显示升级历史记录</font>
+ <font style="color:rgb(51, 51, 51);">pause #暂停版本升级过程</font>
+ <font style="color:rgb(51, 51, 51);">resume #继续已经暂停的版本升级过程</font>
+ <font style="color:rgb(51, 51, 51);">restart #重启版本升级过程</font>
+ <font style="color:rgb(51, 51, 51);">undo #回滚到上一级版本（可以通过--to-revision回滚到指定版本）</font>

<font style="color:rgb(51, 51, 51);">案例：多次更新镜像版本，随后对镜像版本进行回退</font>

```yaml
更新镜像版本
# kubectl edit deploy deploy-nginx -n test
    spec:
      containers:
      - image: nginx:1.20.1



更新镜像版本
# kubectl edit deploy deploy-nginx -n test
    spec:
      containers:
      - image: nginx:1.21.0




查看升级历史记录
# kubectl rollout history deploy deploy-nginx -n test



查看具体版本详细信息：--revision=版本编号
# kubectl rollout history deploy deploy-nginx --revision=2 -n test



查看当前所有版本（通过rs可以查看）
# kubectl get rs -o wide -n test



查看当前使用版本（查看deploy）
# kubectl get deploy -o wide -n test



版本回退：通过--to-revision=1,可直接回滚到1版本，如果省略这个选项，就是回退到上个版本
# kubectl rollout undo deploy deploy-nginx --to-revision=1 -n test




查看当前使用的版本
# kubectl get deploy -o wide -n test




查看升级历史记录
# kubectl rollout history deploy deploy-nginx -n test

提示：新版本就是原先的1版本
```

  
 

