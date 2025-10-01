## docker-compose
[github](https://github.com/docker/compose/releases)

[https://github.com/docker/compose/releases/download/v2.28.1/docker-compose-linux-x86_64](https://github.com/docker/compose/releases/download/v2.28.1/docker-compose-linux-x86_64)

```shell
上传到 /usr/local/bin 目录，不需要解压
重命名为docker-compose
mv docker-compose-linux-x86_64 docker-compose
docker-compose version
chmod +x /usr/local/bin/docker-compose

```

## docker-ce二进制包安装
```python
#!/bin/sh
yum update -y;
yum install wget -y;
yum install tar -y;
cd /;
dockertgz=docker-27.0.3.tgz;
if [ -f $dockertgz ];then
	echo $dockertgz;
	echo 'file is exist';
	tar -xvf /$dockertgz && cp /docker/* /usr/local/bin/ && rm -rf /docker;
else
	wget https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/static/stable/x86_64/$dockertgz && tar -xvf /$dockertgz && cp /docker/* /usr/local/bin/ && rm -rf /docker;
fi;
dockerfiled=/etc/docker;
if [ -f $dockerfiled ];then
	cd /etc/docker;
	echo $dockerjsonfile;
    echo 'file is exist';
else
	mkdir -p /etc/docker;
	cd /etc/docker
fi
cat > /etc/docker/daemon.json << EOF
{
            "registry-mirrors": ["https://jockerhub.com","https://6l60sscb.mirror.aliyuncs.com"]
}
EOF

# 配置系统级用于启动的文件
cat > /usr/lib/systemd/system/docker.service << EOF
[Unit]
Description=Docker Application Container Engine
After=network-online.target firewalld.service
Wants=network-online.target

[Service]
Type=notify
ExecStart=/usr/local/bin/dockerd
ExecReload=/bin/kill -s HUP $MAINPID
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TimeoutStartSec=0
Delegate=yes
KillMode=process
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s

[Install]
WantedBy=multi-user.target
EOF
# 重新加载 daemon 用于启动 docker
systemctl daemon-reload;
systemctl restart docker;
systemctl enable docker;

```

```python
vim docker-install.sh
chmod +x docker-install.sh
sh docker-install.sh
```

## podman安装
```python
yum update -y
yum install podman -y
vim /etc/containers/registries.conf
[registries.search]
registries = ['docker.io']

[registries.insecure]
registries = []

[registries.block]
registries = []

[[registry]]
location = "registry.access.redhat.com"
[[registry]]
location = "registry.redhat.io"
[[registry]]
location = "docker.io"

[[registry]]
location = "jockerhub.com"
mirrors = ['https://jockerhub.com', 'https://6l60sscb.mirror.aliyuncs.com']

[[registry]]
location = "quay.io"
insecure = false

```

```bash
#!/bin/bash
podmantgz=podman-remote-static-linux_amd64.tar.gz;
yum install wget -y
cd /
wget https://github.com/containers/podman/releases/download/v5.1.1/podman-remote-static-linux_amd64.tar.gz
mkdir podmantemp
tar -xzvf $podmantgz podmantemp
mv /podmantemp/bin/podman-remote-static-linux_amd64 /usb/bin/podman
chmod +x /usr/bin/podman

```

