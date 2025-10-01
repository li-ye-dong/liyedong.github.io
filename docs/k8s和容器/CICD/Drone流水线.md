### 工具镜像准备(tag根据需要)
```bash
#drone-server
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/drone/drone:2
docker tag  swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/drone/drone:2  docker.io/drone/drone:2
#drone-runner-docker
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/drone/drone-runner-docker:1
docker tag  swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/drone/drone-runner-docker:1  docker.io/drone/drone-runner-docker:1
#git、ssh、plugins/docker
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/alpine/git:v2.49.0
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/ghcr.io/appleboy/drone-ssh:1.7.7
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/plugins/docker:20.18

```

### <font style="color:rgb(26, 32, 44);">登录到drone</font>
<font style="color:rgb(74, 85, 104);">您可以通过访问浏览器中的服务器地址来登录您的无人机服务器。您需要使用您的 Gogs 用户名和密码进行身份验证。</font>_<font style="color:rgb(74, 85, 104);"> 这是必需的，因为 Gogs 不支持 oauth。</font>_

### <font style="color:rgb(74, 85, 104);">docker compose和配置文件</font>
```yaml
version: '3'

services:
  drone-server:
    image: drone/drone:2
    container_name: drone-server
    ports:
      - 8080:80
    volumes:
      - /u01/drone/data:/data
    env_file:
      - drone.env
    restart: always

  drone-runner:
    image: drone/drone-runner-docker:1
    container_name: drone-runner
    depends_on:
      - drone-server
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /etc/hosts:/etc/hosts
      - /etc/docker:/etc/docker
    env_file:
      - runner.env
    restart: always
```

```bash
DRONE_GOGS_SERVER="http://192.168.107.99:10880/"

DRONE_SERVER_HOST="192.168.107.99:8080"  
DRONE_SERVER_PROTO=http
DRONE_RPC_SECRET=liyedong

DRONE_USER_CREATE="username:liyedong,admin:true"
DRONE_USER_FILTER=liyedong
DRONE_GOGS_SKIP_VERIFY=true
DRONE_LOGS_TRACE=true
DRONE_LOGS_DEBUG=true

DRONE_ANGENTS_ENABLED=true
```

```bash
DRONE_RPC_PROTO=http
#通过容器docker compose网络访问，不需要访问宿主机8080端口，也可以使用192.168.107.99:8080
DRONE_RPC_HOST=drone-server:80   
DRONE_RPC_SECRET=liyedong

DRONE_RUNNER_CAPACITY=2
DRONE_RUNNER_NAME=docker-runner-1

DRONE_LOGS_TRACE=true
DRONE_LOGS_DEBUG=true
```



```bash
cd /u01/drone
docker compose up -d
docker compose ps
```



### 配置流水线
![](../../images/1754153469855-e6af50cf-d500-4740-82e4-84d1420c07bc.png)



![](../../images/1754153477880-40493c5f-b63a-4fc1-bd7c-0490522c052a.png)

```bash
liyedong
liyedong
```

![](../../images/1754153508882-4c21c857-9d9a-4d9b-a7fc-8f09fc361496.png)

跳过即可

![](../../images/1754153534852-710ad56d-6656-415b-acc8-4351658c7076.png)

进入页面

![](../../images/1754153551823-dba02fbb-c298-4e19-8aef-558b75ae17b6.png)

激活

![](../../images/1754153571608-8503645f-d5f9-4354-b3ab-fd29f874119c.png)

提权，然后save change

![](../../images/1754200463771-37e1c4f1-45b7-4ef8-bff0-18795641af91.png)

添加 Secret（Harbor 认证信息）

进入 Drone UI：

1. 打开你的 Gogs 项目；
2. 右上角点击「仓库设置」；
3. 找到 **Secrets**；
4. 添加如下两项：
    - `harbor_user`
    - `harbor_pass`
    - `<font style="color:rgb(0, 0, 0);">gogs_user</font>`
    - `<font style="color:rgb(0, 0, 0);">gogs_pass</font>`
    - `<font style="color:rgb(0, 0, 0);">ssh_password</font>`

```bash
admin
admin
liyedong
liyedong
root
```

![](../../images/1754153683349-87fb9fed-e484-4f79-81fd-4b79afb6fbcb.png)

```bash
echo "192.168.107.99 gogs.liyedong.com" >> /etc/hosts
```

```yaml
kind: pipeline
type: docker
name: default
clone:
  disable: true  #禁止drone自己的git操作
#各个工具尽量使用本地已有的镜像
steps:
  - name: 拉取代码
    image: harbor.liyedong.com/library/alpine/git:v2.49.0
    volumes:
      - name: hosts
        path: /etc/hosts
      - name: docker-ca
        path: /etc/docker
    environment:
      GOGS_USER:
        from_secret: gogs_user
      GOGS_PASS:
        from_secret: gogs_pass
    commands:
      - git config --global http.sslVerify false  # 忽略 SSL 验证
      - git clone http://${GOGS_USER}:${GOGS_PASS}@gogs.liyedong.com:10880/liyedong/kyem.git .
      - git checkout ${DRONE_COMMIT_SHA}

  - name: 构建并推送镜像
    image: harbor.liyedong.com/library/plugins/docker:20.18
    environment:
      DOCKER_BUILDKIT: 0  #使用传统方式构建，不使用buildkit
    volumes:
      - name: hosts
        path: /etc/hosts
      - name: docker-ca
        path: /etc/docker
      - name: dockersock
        path: /var/run/docker.sock
    settings:
      registry: harbor.liyedong.com
      repo: harbor.liyedong.com/kyem/kyem-backend
      tags:
        - latest
        - ${DRONE_BUILD_NUMBER}
      dockerfile: Dockerfile
      context: .
      username:
        from_secret: harbor_user
      password:
        from_secret: harbor_pass
  - name: ssh commands
    image: harbor.liyedong.com/library/appleboy/drone-ssh:1.7.7
    settings:
      host: 192.168.107.99
      username: root
      password:
        from_secret: ssh_password
      port: 22
      script:
        #拉取镜像并重启 注意--需要提前在目标主机完成docker login
        - if [ $(docker ps -a | grep kyem-backend | wc -l) -ge 1 ];then docker stop kyem-backend && docker rm kyem-backend; fi
        - docker pull harbor.liyedong.com/kyem/kyem-backend:latest
        - docker run --name kyem-backend --restart=always -d -p8082:8080 harbor.liyedong.com/kyem/kyem-backend:latest    
trigger:
  branch:
    - master
#映射解析和harbor ca证书
volumes:
  - name: hosts
    host:
      path: /etc/hosts
  - name: docker-ca
    host:
      path: /etc/docker
  - name: dockersock
    host:
      path: /var/run/docker.sock
```

```yaml
git add .
git commit -m "add .drone.yml"
git push origin master
```

### Gogs推送失败处理
![](../../images/1754154730231-e35cddaa-e52a-4a47-b592-6335fbcd106d.png)

发现如下：<font style="color:rgb(51, 51, 51);background-color:rgb(248, 248, 248);">Payload URL resolved </font>**<font style="color:rgb(51, 51, 51);">to</font>**<font style="color:rgb(51, 51, 51);background-color:rgb(248, 248, 248);"> a local</font><font style="color:rgb(0, 134, 179);"> network address </font><font style="color:rgb(51, 51, 51);background-color:rgb(248, 248, 248);">that is implicitly blocked.</font>

<font style="color:rgb(51, 51, 51);background-color:rgb(248, 248, 248);">解决</font>

![](../../images/1754154803618-fe17a7e9-7299-45b8-9607-14f1457e6f40.png)

在gogs的配置文件中找到[security]，添加白名单，

```yaml
vim /u01/gogs/gogs/conf/app.ini
```

```bash
BRAND_NAME = Gogs
RUN_USER   = git
RUN_MODE   = prod

[database]
TYPE     = sqlite3
HOST     = 127.0.0.1:5432
NAME     = gogs
USER     = gogs
PASSWORD = 
SSL_MODE = disable
PATH     = data/gogs.db

[repository]
ROOT = /data/git/gogs-repositories

[server]
DOMAIN           = 192.168.107.99
HTTP_PORT        = 3000
EXTERNAL_URL     = http://192.168.107.99:10880/
DISABLE_SSH      = false
SSH_PORT         = 10022
START_SSH_SERVER = false
OFFLINE_MODE     = false

[mailer]
ENABLED = false

[service]
REGISTER_EMAIL_CONFIRM = false
ENABLE_NOTIFY_MAIL     = false
DISABLE_REGISTRATION   = false
ENABLE_CAPTCHA         = true
REQUIRE_SIGNIN_VIEW    = false

[picture]
DISABLE_GRAVATAR        = false
ENABLE_FEDERATED_AVATAR = false

[session]
PROVIDER = file

[log]
MODE      = file
LEVEL     = Info
ROOT_PATH = /app/gogs/log

[security]
INSTALL_LOCK = true
SECRET_KEY   = C3B8CPB81TczACS
LOCAL_NETWORK_ALLOWLIST=192.168.107.99  #添加白名单
```



### Docker buildkit证书问题处理
`docker info` 信息来看，当前环境使用的是 **Docker 默认 BuildKit 模式**（由 Docker Daemon 启动），而不是使用独立的 `buildkitd` 守护进程（如 `moby/buildkit` 容器或 buildx 的 `buildkit-container` 驱动）。  

你可以：

```bash
docker buildx inspect
```

如果输出中是：

```bash
Driver: docker
```

说明用的是默认 Docker 守护进程的 BuildKit（不读取 buildkitd.toml）

如果是：

```bash
Driver: remote | buildkit | container
```

说明用了独立 BuildKit 守护进程（可以读取 `buildkitd.toml`）

```bash
docker buildx inspect | grep Driver
Driver:        docker
```

####  使用环境变量完全关闭 buildkit，恢复传统构建模式  （有效）
```yaml
kind: pipeline
type: docker
name: default
clone:
  disable: true  #禁止drone自己的git操作
#各个工具尽量使用本地已有的镜像
steps:
  - name: 拉取代码
    image: harbor.liyedong.com/library/alpine/git:v2.49.0
    volumes:
      - name: hosts
        path: /etc/hosts
      - name: docker-ca
        path: /etc/docker
    environment:
      GOGS_USER:
        from_secret: gogs_user
      GOGS_PASS:
        from_secret: gogs_pass
    commands:
      - git config --global http.sslVerify false  # 忽略 SSL 验证
      - git clone http://${GOGS_USER}:${GOGS_PASS}@gogs.liyedong.com:10880/liyedong/kyem.git .
      - git checkout ${DRONE_COMMIT_SHA}

  - name: 构建并推送镜像
    image: harbor.liyedong.com/library/plugins/docker:20.18
    environment:
      DOCKER_BUILDKIT: 0  #使用传统方式构建，不使用buildkit
    volumes:
      - name: hosts
        path: /etc/hosts
      - name: docker-ca
        path: /etc/docker
      - name: dockersock
        path: /var/run/docker.sock
    settings:
      registry: harbor.liyedong.com
      repo: harbor.liyedong.com/kyem/kyem-backend
      tags:
        - latest
        - ${DRONE_BUILD_NUMBER}
      dockerfile: Dockerfile
      context: .
      username:
        from_secret: harbor_user
      password:
        from_secret: harbor_pass
  - name: ssh commands
    image: harbor.liyedong.com/library/appleboy/drone-ssh:1.7.7
    settings:
      host: 192.168.107.99
      username: root
      password:
        from_secret: ssh_password
      port: 22
      script:
        #拉取镜像并重启 注意--需要提前在目标主机完成docker login
        - if [ $(docker ps -a | grep kyem-backend | wc -l) -ge 1 ];then docker stop kyem-backend && docker rm kyem-backend; fi
        - docker pull harbor.liyedong.com/kyem/kyem-backend:latest
        - docker run --name kyem-backend --restart=always -d -p8082:8080 harbor.liyedong.com/kyem/kyem-backend:latest    
trigger:
  branch:
    - master
#映射解析和harbor ca证书
volumes:
  - name: hosts
    host:
      path: /etc/hosts
  - name: docker-ca
    host:
      path: /etc/docker
  - name: dockersock
    host:
      path: /var/run/docker.sock
```

#### 通过daemon.json禁用docker buildkit（有效）
既然你用的是默认 Docker BuildKit，那么最直接的做法是："buildkit": false  

编辑 `/etc/docker/daemon.json`，添加：

```bash
tee /etc/docker/daemon.json << 'EOF'
{
  "registry-mirrors": [
    "https://registry.cn-hangzhou.aliyuncs.com"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "live-restore": true,
  "max-concurrent-downloads": 10,
  "max-concurrent-uploads": 5,
  "default-address-pools": [
    {
      "base": "172.30.0.0/16",
      "size": 24
    }
  ],
  "mtu": 1450,
  "features": {
    "buildkit": false  
  },
  "insecure-registries": [
    "harbor.liyedong.com"
  ]
}
EOF
```

然后：

```bash
systemctl daemon-reexec
systemctl daemon-reload
systemctl restart docker
cd /u01/drone
docker compose down
docker compose up -d
systemctl restart harbor
```

这将告诉 **Docker 守护进程**：“此 registry 是不安全的（HTTP 或自签名证书），允许跳过 TLS 验证”。

```yaml
kind: pipeline
type: docker
name: default
clone:
  disable: true  #禁止drone自己的git操作
#各个工具尽量使用本地已有的镜像
steps:
  - name: 拉取代码
    image: harbor.liyedong.com/library/alpine/git:v2.49.0
    volumes:
      - name: hosts
        path: /etc/hosts
      - name: docker-ca
        path: /etc/docker
    environment:
      GOGS_USER:
        from_secret: gogs_user
      GOGS_PASS:
        from_secret: gogs_pass
    commands:
      - git config --global http.sslVerify false  # 忽略 SSL 验证
      - git clone http://${GOGS_USER}:${GOGS_PASS}@gogs.liyedong.com:10880/liyedong/kyem.git .
      - git checkout ${DRONE_COMMIT_SHA}

  - name: 构建并推送镜像
    image: harbor.liyedong.com/library/plugins/docker:20.18
    # environment:
    #   DOCKER_BUILDKIT: 0  #使用传统方式构建，不使用buildkit
    volumes:
      - name: hosts
        path: /etc/hosts
      - name: docker-ca
        path: /etc/docker
      - name: dockersock
        path: /var/run/docker.sock
    settings:
      registry: harbor.liyedong.com
      repo: harbor.liyedong.com/kyem/kyem-backend
      tags:
        - latest
        - ${DRONE_BUILD_NUMBER}
      dockerfile: Dockerfile
      context: .
      username:
        from_secret: harbor_user
      password:
        from_secret: harbor_pass
  - name: ssh commands
    image: harbor.liyedong.com/library/appleboy/drone-ssh:1.7.7
    settings:
      host: 192.168.107.99
      username: root
      password:
        from_secret: ssh_password
      port: 22
      script:
        #拉取镜像并重启 注意--需要提前在目标主机完成docker login
        - if [ $(docker ps -a | grep kyem-backend | wc -l) -ge 1 ];then docker stop kyem-backend && docker rm kyem-backend; fi
        - docker pull harbor.liyedong.com/kyem/kyem-backend:latest
        - docker run --name kyem-backend --restart=always -d -p8082:8080 harbor.liyedong.com/kyem/kyem-backend:latest    
trigger:
  branch:
    - master
#映射解析和harbor ca证书
volumes:
  - name: hosts
    host:
      path: /etc/hosts
  - name: docker-ca
    host:
      path: /etc/docker
  - name: dockersock
    host:
      path: /var/run/docker.sock
```

#### **Harbor 开启 HTTP 或使用可信证书（待验证）**
当然，**生产建议使用有效证书**（Let’s Encrypt、内部 CA 颁发的证书并添加到系统信任链），或：

+ 将 Harbor 改为 HTTP（`harbor.yml` 配置）
+ 并在 `daemon.json` 中加入 `insecure-registries`

