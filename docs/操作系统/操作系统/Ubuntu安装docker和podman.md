```bash
#!/bin/sh
apt update
apt install wget 
apt install tar 
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

