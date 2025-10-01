```bash
# Pull image from Docker Hub.
docker pull gogs/gogs:0.12.11
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/gogs/gogs:0.12.11
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/gogs/gogs:0.12.11
docker tag  swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/gogs/gogs:0.12.11 docker.io/gogs/gogs:0.12.11# Create local directory for volume.
mkdir -p /u01/gogs

tee /u01/gogs/docker-compose.yml << 'EOF'
version: '3'

services:
  gogs:
    image: gogs/gogs:0.12.11
    container_name: gogs
    restart: always
    ports:
      - "10022:22"       # SSH 端口
      - "10880:3000"     # Web 访问端口
    volumes:
      - /u01/gogs:/data  # 数据卷挂载
EOF
cd /u01/gogs
docker-compose up -d
docker compose up -d

```

[http://192.168.107.99:10880/install](http://192.168.107.99:10880/install)

![](../../images/1753879987209-9d274529-33cf-411a-a64b-488548173ffe.png)

![](../../images/1753880717479-829e65a8-2c93-4214-8025-bfdb69bb877a.png)

![](../../images/1753880720881-ae563d03-a8d3-4807-9d53-b3633ecc3026.png)



添加sshkey

```bash
PS C:\Users\Administrator\.ssh> cat .\id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEJtS/DdUM5mt4dEXdl07sME/Geu1HlHF4mEso2/U4Jp administrator@WIN-GKO56FN7DCD
```

两个都可以

![](../../images/1753881140793-d67ca4ae-4e11-4535-9d49-18d957fceea2.png)

![](../../images/1753881101788-11a19cbb-5a30-4397-b953-6bd3ebd15c2e.png)



![](../../images/1753881174669-6b5c9d74-e13d-4d0f-be94-b23ecfc6c210.png)

![](../../images/1753881215325-0c7d30d2-e5df-4e82-90d1-de022c5977f1.png)



