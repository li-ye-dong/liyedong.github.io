# Kubernetes Dashboard
通过dashboard能够直观了解Kubernetes集群中运行的资源对象

通过dashboard可以直接管理（创建、删除、重启等操作）资源对象





获取dashboard资源清单文件



下载资源清单文件

```powershell
[root@master01 ~]# wget https://raw.githubusercontent.com/kubernetes/dashboard/v2.5.1/aio/deploy/recommended.yaml

```





#### 修改dashboard资源清单文件
```powershell
[root@master01 ~]# vi recommended.yaml
......

为了方便在容器主机上访问，下面的service需要添加NodePort类型及端口，大约39行
---

kind: Service
apiVersion: v1
metadata:
  labels:
    k8s-app: kubernetes-dashboard
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
spec:
  type: NodePort         此处添加
  ports:
    - port: 443
      targetPort: 8443
      nodePort: 30000
  selector:
    k8s-app: kubernetes-dashboard



需要修改登录kubernetes dashboard后用户的身份，不然无法显示资源情况，大约163行
---

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubernetes-dashboard
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin   一定要把原来的kubernetes-dashboard修改为cluster-admin，不然进入UI后会报错。
subjects:
  - kind: ServiceAccount
    name: kubernetes-dashboard
    namespace: kubernetes-dashboard

......

```





#### 创建dashboard
```powershell
[root@master01 ~]# kubectl create -f recommended.yaml


查看ns
[root@master01 ~]# kubectl get ns
kubernetes-dashboard   Active   56s


查看kubernetes-dashboard下pod，svc资源
[root@master01 ~]# kubectl get pod,svc -n kubernetes-dashboard
...

上述内容省略，通过NodePort暴露的端口30601进行访问

service/kubernetes-dashboard NodePort 10.111.133.19 <none>   443:30601/TCP   

```





#### 访问dashboard
浏览器访问集群任意节点`IP:NodePort端口`：[https://192.168.0.10:30601](https://192.168.0.10:30601) 

获取token

```powershell
[root@master01 ~]# kubectl get secret -n kubernetes-dashboard
...

上述内容省略，获取该token密钥进行登录验证

kubernetes-dashboard-token-g6pq7   kubernetes.io/service-account-token 


获取token密钥
[root@master01 ~]# kubectl describe secret kubernetes-dashboard-token-g6pq7 -n kubernetes-dashboard
...

上述内容省略，将token中的内容复制到dashboard

token:      eyJhbGciOiJSUzI1NiIsImtpZCI6IkpsSC1wcGRrZ3h5cmEzLWFleEZURzB4RUV4QzdMVEhDLUNtamVxLWVR1kifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uW1lc3BhY2UiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hWUiOiJrdWJlcm5ldGVzLWRhc2hib2FyZC10b2tlbi0yeDl0ZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VymljZS1hY2NvdW50Lm5hbWUiOiJrdWJlcm5ldGVzLWRhc2hib2FyZCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQv2VydmljZS1hY2NvdW50LnVpZCI6ImRmZTAzZTQxLTE5OGYtNDg1OS1iYjhmLTQwZGJhMTA2ZWZjNyIsInN1YiI6InN5c3RlTpzZXJ2aWNlYWNjb3VudDprdWJlcm5ldGVzLWRhc2hib2FyZDprdWJlcm5ldGVzLWRhc2hib2FyZCJ9.EQ_C_Unv8yiE2v2m5YAPi36MPDpqp9IMIZ-9-LWn7x5l0YWCQ5AL_b64n0BGGe2nT-hpR50EEJXYE5cbdlEjQ4ep1wRBK7471DcBs49DY0OHkJPjHf67tBSUA1fmC5mhljqDQ_FlV8Qfh46qNs8CW3RabXi_JLHzP-lV3NkfwG0FFEvGsiGvXPPS31VXZcfNoaioGVDlOLAhRSup7mj1e9Ly53_uUL9W-rx_ROczYoKdBk-qvXujVYy753uYUQW4HJN5SVzUtQTW4N6vuCW6S3SsuwydAGDmqZpNEHPnq99C07ARNG9-69HMFZ8EZrDw-v28JzAv7cN9OIX1mA

```

