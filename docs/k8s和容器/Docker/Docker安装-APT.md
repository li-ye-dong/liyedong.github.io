<font style="color:rgb(33, 37, 41);">如果你过去安装过 docker，先删掉：</font>

```bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do apt-get remove $pkg; done
```

<font style="color:rgb(33, 37, 41);">首先安装依赖：</font>

```bash
apt-get update
apt-get install ca-certificates curl gnupg
```

<font style="color:rgb(33, 37, 41);">信任 Docker 的 GPG 公钥并添加仓库：</font>

<font style="color:rgb(33, 37, 41);">发行版</font>

<font style="color:rgb(33, 37, 41);">Debian</font>

```bash
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
```

<font style="color:rgb(33, 37, 41);">最后安装</font>

```bash
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```bash
systemctl enable docker --now
```

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
    "buildkit": true
  },
  "dns":[
    "223.5.5.5",
    "114.114.114.114"
  ]

}
EOF
  # "ip": "127.0.0.1",
  # "bip": "192.168.107.10/24",
  # "fixed-cidr": "192.168.107.0/25"
  # "default-gateway": "192.168.107.2"
  # "ipv6":true,
  # "fixed-cidr-v6":"2001:db8::/64",
```

```bash
systemctl daemon-reload && systemctl restart docker
```

