### 1. 安装 Ubuntu 子系统
打开 PowerShell（管理员），运行以下命令安装 Ubuntu：

```powershell
wsl --install -d Ubuntu
```

如果你已经启用了 WSL 2，这条命令会自动拉取 Ubuntu 并安装。如果提示没启用 WSL 2，可以提前运行：

```powershell
wsl --update
```

---

### 2. 查看是否安装成功
```powershell
wsl --list --all
```

理想的输出应该包含：

```plain
Ubuntu
docker-desktop (默认)
```

---

### 3. 设置 Ubuntu 为默认分发（可选）
如果你之后只想用 Ubuntu，执行：

```powershell
wsl --set-default Ubuntu
```

---

### 4. 进入 Ubuntu 开始开发
```powershell
wsl
```

或者：

```powershell
wsl -d Ubuntu
```

首次进入 Ubuntu 会提示你创建一个新用户账号，设置用户名和密码。

---

### 5. 配置apt国内清华源
```bash
#配置国内源
cat <<'EOF' > set_tuna_apt.sh
#!/bin/bash
set -e
codename=$(lsb_release -cs)
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo tee /etc/apt/sources.list > /dev/null <<EOL
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ $codename main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ $codename-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ $codename-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ $codename-security main restricted universe multiverse
EOL
sudo apt update
EOF

bash set_tuna_apt.sh
```

### 6. 在 Ubuntu 中安装 Python 环境
```bash
sudo apt update
sudo apt install python3 python3-pip
```

推荐同时装个 Git、zsh、vim 等开发工具：

```bash
sudo apt install git zsh vim
```

---



