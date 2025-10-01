```bash
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/gitea/gitea:1.24.3
docker tag  swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/gitea/gitea:1.24.3  docker.io/gitea/gitea:1.24.3
```

[https://docs.gitea.com/zh-cn/installation/install-with-docker](https://docs.gitea.com/zh-cn/installation/install-with-docker)

```bash
mkdir -p /u01/gitea
tee /u01/gitea/docker-compose.yml << 'EOF'
version: "3"

networks:
  gitea:
    external: false

services:
  server:
    image: docker.gitea.com/gitea:1.24.3
    container_name: gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
    restart: always
    networks:
      - gitea
    volumes:
      - /u01/gitea:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    ports:
      - "3000:3000"
      - "222:22"
EOF
cd /u01/gitea
docker-compose up -d
docker compose up -d

```

