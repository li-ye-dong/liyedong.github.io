```bash
# 添加 Grafana 仓库
wget https://mirrors.tuna.tsinghua.edu.cn/grafana/yum/rpm/Packages/grafana-11.6.1-1.x86_64.rpm
sudo yum install grafana-11.6.1-1.x86_64.rpm -y
# 设置为开机启动并立即启动
sudo systemctl enable --now grafana-server
```



