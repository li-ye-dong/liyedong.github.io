好的，下面是 `systemd` 和 `supervisor` 的**全面使用笔记**，内容涵盖日常使用、配置示例、常见问题及进阶技巧。

---

## 🧩 一、Systemd 使用笔记
### 1. 基本概念
+ 单元类型（unit）：最常用的是 `service` 类型，也有 `socket`、`mount`、`timer` 等。
+ unit 文件位置：
    - 系统级：`/etc/systemd/system/`（推荐手动创建服务时放这）
    - 用户级：`~/.config/systemd/user/`
    - 软件包提供：`/lib/systemd/system/` 或 `/usr/lib/systemd/system/`
    - ExecStart=：执行的命令需要运行在前端，如果是守护进程，则会出现问题

### 2. 常用命令
```bash
# 启动 / 停止 / 重启服务
sudo systemctl start myapp.service
sudo systemctl stop myapp.service
sudo systemctl restart myapp.service

# 设置开机自启
sudo systemctl enable myapp.service

# 取消开机自启
sudo systemctl disable myapp.service

# 查看状态
systemctl status myapp.service

# 查看所有服务
systemctl list-units --type=service
```

### 3. service 配置模板
```toml
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/user/myapp.py
Restart=on-failure
User=www-data
WorkingDirectory=/home/user/
Environment="ENV=production"
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

### 4. 重载与调试
```bash
# 每次修改 .service 文件后需要 reload
sudo systemctl daemon-reload

# 查看日志
journalctl -u myapp.service -f

# 查看系统所有日志
journalctl -xe
```

### 5. 高级用法
+ **定时任务**（代替 crontab）：

```toml
# myapp.timer
[Unit]
Description=Run MyApp every hour

[Timer]
OnBootSec=10min
OnUnitActiveSec=1h
Unit=myapp.service

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl enable --now myapp.timer
```

+ **限制资源**：

```toml
MemoryLimit=200M
CPUQuota=20%
```

+ **服务依赖关系**：

```toml
Requires=mysql.service
After=mysql.service
```

---

## ⚙️ 二、Supervisor 使用笔记
### 1. 安装方式
```bash
# Debian / Ubuntu
sudo apt install supervisor

# 或使用 pip（更灵活）
pip install supervisor
```

### 2. 配置结构
默认配置目录：

+ `/etc/supervisor/supervisord.conf`
+ `/etc/supervisor/conf.d/*.conf` （推荐将服务写到这里）

### 3. 示例配置
```toml
# /etc/supervisor/conf.d/myapp.conf
[program:myapp]
command=/usr/bin/python3 /home/user/myapp.py
directory=/home/user/
autostart=true
autorestart=true
stderr_logfile=/var/log/myapp.err.log
stdout_logfile=/var/log/myapp.out.log
user=www-data
environment=ENV="production"
```

### 4. 常用命令
```bash
# 启动 supervisor
sudo systemctl start supervisor

# 更新配置（如新增服务）
sudo supervisorctl reread
sudo supervisorctl update

# 启动/停止服务
sudo supervisorctl start myapp
sudo supervisorctl stop myapp
sudo supervisorctl restart myapp

# 查看状态
sudo supervisorctl status
```

### 5. 进阶技巧
+ **守护多个服务**： 可以为每个服务写一个 `.conf`，集中管理。

```toml
[program:worker]
command=node worker.js

[program:api]
command=node api.js
```

+ **重启策略**：

```toml
autorestart=true
startretries=3
```

+ **Web 管理界面**（适合开发/内网）：

```toml
[inet_http_server]
port=127.0.0.1:9001
username=admin
password=1234
```

访问方式：[http://127.0.0.1:9001](http://127.0.0.1:9001/)

+ **日志查看**： 直接查看 `stdout_logfile` 和 `stderr_logfile` 指定的日志文件即可。

---

## 实践demo（systemd+supervisor）
### 安装supervisor
```bash
# 检查 SELinux
sudo setenforce 0  # 临时关闭
sudo vim /etc/selinux/config  # 永久关闭需修改为 SELINUX=disabled

# 创建 pip 配置目录
mkdir -p ~/.pip

# 配置清华源
cat << EOF > ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
EOF

# 全局配置（可选）
sudo cp ~/.pip/pip.conf /etc/pip.conf

# 使用 pip3 安装
sudo pip3 install supervisor

# 验证安装
echo_supervisord_conf |grep version
# 应显示版本号 4.x.x


# 添加环境变量
echo 'export PATH=$PATH:/usr/local/bin' > /etc/profile.d/supervisorctl.sh
source /etc/profile.d/supervisorctl.sh
```

### 生成配置文件
```bash
# 生成默认配置
sudo mkdir -p /etc/supervisor/conf.d
sudo echo_supervisord_conf > /etc/supervisord.conf

# 修改配置
# 取消include模块注释
sudo sed -i 's/;\[include\]/[include]/' /etc/supervisord.conf
# 添加conf.d的include功能，只需要在这个目录写.conf文件，就可以使用supervisor守护进程
sudo sed -i 's#;files = relative/directory/\*.ini#files = /etc/supervisor/conf.d/*.conf#' /etc/supervisord.conf
# 禁用守护进程模式，如果不禁用，会导致systemd无法守护  重要
sudo sed -i 's/nodaemon=false/nodaemon=true/' /etc/supervisord.conf

```

### <font style="color:rgb(64, 64, 64);">创建 Systemd 服务</font>
```bash
# 创建服务文件
sudo tee /etc/systemd/system/supervisord.service << EOF
[Unit]
Description=Supervisor process control system
Documentation=http://supervisord.org
After=network.target

[Service]
ExecStart=/usr/local/bin/supervisord -c /etc/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl shutdown
ExecReload=/usr/local/bin/supervisorctl reload
KillMode=process
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
EOF

# 重载 systemd
sudo systemctl daemon-reload
```

### <font style="color:rgb(64, 64, 64);">启动与管理服务</font>
```bash

# 设置开机启动
sudo systemctl enable supervisord --now

# 查看状态
sudo systemctl status supervisord

# 管理命令
sudo supervisorctl status
```

### <font style="color:rgb(64, 64, 64);">验证安装（测试用例）</font>
```bash
# 创建测试进程配置
sudo tee /etc/supervisor/conf.d/test.conf << EOF
[program:test]
command=/bin/bash -c "while true; do echo \$(date) >> /tmp/supervisor_test.log; sleep 5; done"
autostart=true
autorestart=true
EOF

# 重载配置
sudo supervisorctl update

# 查看日志
tail -f /tmp/supervisor_test.log
# 应每5秒看到时间戳输出
```

## 配置文件模板
```bash
; 基础配置
[program:myapp]                     ; 服务名称（全局唯一）
command=/usr/bin/python3 app.py     ; 启动命令（必须使用绝对路径）
directory=/opt/myapp                ; 工作目录
user=www-data                       ; 运行用户
priority=100                        ; 启动优先级（数字越小越优先）
autostart=true                      ; 随supervisor启动
autorestart=unexpected              ; 退出策略：unexpected|true|false
;unexpected：仅当退出码不在exitcodes时重启
;true：总是自动重启
;false：不自动重启
startsecs=5                         ; 启动持续时间（超过视为成功）
stopwaitsecs=30                     ; 停止等待时间（超时强制杀死）

; 日志配置
stdout_logfile=/var/log/myapp.log   ; 标准输出日志（需提前创建）
stdout_logfile_maxbytes=50MB        ; 单个日志文件大小
stdout_logfile_backups=10           ; 日志备份数量
redirect_stderr=true                ; 错误输出重定向到stdout
loglevel=info                       ; 日志级别：critical|error|warn|info|debug

; 高级配置
environment=                        ; 环境变量（多个用逗号分隔）
  PYTHONPATH="/opt/myapp",
  HOME="/home/www-data"
numprocs=3                          ; 启动进程数（配合% (process_num)s使用）
process_name=%(program_name)s_%(process_num)02d ; 进程命名规则
;需配合process_name使用，如启动3个worker进程
stopsignal=QUIT                     ; 停止信号：TERM|HUP|INT|QUIT|KILL
;推荐顺序：QUIT(3) → TERM(15) → KILL(9)
```



```bash
[Unit]
Description=My Application Service  ; 服务描述
Documentation=https://example.com   ; 文档链接
After=network.target postgresql.service  ; 依赖服务
Requires=postgresql.service         ; 强依赖关系

[Service]
Type=notify                         ; 类型：simple|forking|notify 服务通过sd_notify()发送READY=1信号
;notify：服务通过sd_notify()发送READY=1信号
;simple：直接运行ExecStart命令（默认）
ExecStart=/opt/myapp/start.sh       ; 启动命令（必须前台运行）
ExecReload=/bin/kill -HUP $MAINPID  ; 重载命令
ExecStop=/bin/kill -TERM $MAINPID   ; 停止命令
User=appuser                        ; 运行用户
Group=appgroup                      ; 运行组
WorkingDirectory=/opt/myapp         ; 工作目录
Restart=on-failure                  ; 重启策略：no|always|on-success|on-failure
;on-failure：非正常退出时重启（exit code非0）
;always：任何情况都重启
RestartSec=5s                       ; 重启间隔时间
TimeoutStopSec=30s                  ; 停止超时时间

; 资源限制
LimitNOFILE=65535                   ; 文件描述符限制
MemoryMax=2G                        ; 最大内存限制
CPUQuota=150%                       ; CPU配额（超过100%表示多核）

; 安全配置
ProtectSystem=full                  ; 文件系统保护 禁止写入/etc、/boot等系统目录
PrivateTmp=true                     ; 使用私有/tmp
NoNewPrivileges=true                ; 禁止提权

[Install]
WantedBy=multi-user.target          ; 启动级别
```



✅ 总结建议

| 场景 | 推荐使用 | 理由 |
| --- | --- | --- |
| 系统服务 | systemd | 原生支持，可靠性高 |
| 进程管理 / Web 项目 | supervisor | 易于配置、调试，支持 web 面板 |
| 定时任务 | systemd.timer | 更强大、统一管理 |
| 脚本、开发期使用 | supervisor | 修改立即生效、无需 reload |


---

## 🧩 一、Supervisor 管理所有进程
### ✅ 适合场景
适用于开发机或轻量部署，不涉及系统级服务控制。

### 📁 配置目录建议结构：
```plain
/etc/supervisor/conf.d/
├── django.conf
├── celery.conf
├── flower.conf
├── nginx.conf （一般不推荐用 supervisor 管 nginx）
├── elasticsearch.conf （可选）
```

---

### 1️⃣ django.conf
```plain
[program:django]
directory=/home/user/myproject
command=/usr/local/bin/gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
autostart=true
autorestart=true
user=www-data
stdout_logfile=/var/log/supervisor/django.out.log
stderr_logfile=/var/log/supervisor/django.err.log
```

---

### 2️⃣ celery.conf
```plain
[program:celery]
directory=/home/user/myproject
command=/usr/local/bin/celery -A myproject worker --loglevel=info
autostart=true
autorestart=true
user=www-data
stdout_logfile=/var/log/supervisor/celery.out.log
stderr_logfile=/var/log/supervisor/celery.err.log
```

---

### 3️⃣ flower.conf
```plain
[program:flower]
directory=/home/user/myproject
command=/usr/local/bin/celery -A myproject flower --port=5555
autostart=true
autorestart=true
user=www-data
stdout_logfile=/var/log/supervisor/flower.out.log
stderr_logfile=/var/log/supervisor/flower.err.log
```

---

### 🔁 常用操作命令：
```bash
sudo supervisorctl reread
sudo supervisorctl update

# 控制服务
sudo supervisorctl start django
sudo supervisorctl restart celery
sudo supervisorctl status
```

---

## ⚙️ 二、使用 systemd 管理（推荐用于正式环境）
更适合稳定运行、高可靠性的生产环境。

---

### 1️⃣ `django.service`
```plain
[Unit]
Description=Django Gunicorn Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/home/user/myproject
ExecStart=/usr/local/bin/gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
Restart=always
Environment=DJANGO_SETTINGS_MODULE=myproject.settings
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

---

### 2️⃣ `celery.service`
```plain
[Unit]
Description=Celery Worker
After=network.target redis.service

[Service]
User=www-data
WorkingDirectory=/home/user/myproject
ExecStart=/usr/local/bin/celery -A myproject worker --loglevel=info
Restart=always
Environment=DJANGO_SETTINGS_MODULE=myproject.settings

[Install]
WantedBy=multi-user.target
```

---

### 3️⃣ `flower.service`
```plain
[Unit]
Description=Celery Flower
After=network.target

[Service]
User=www-data
WorkingDirectory=/home/user/myproject
ExecStart=/usr/local/bin/celery -A myproject flower --port=5555
Restart=always

[Install]
WantedBy=multi-user.target
```

---

### 4️⃣ 其它说明
+ **Redis**、**Nginx**、**Elasticsearch** 这类服务通常使用系统默认的 systemd 服务（无需自建），比如：

```bash
sudo systemctl enable redis
sudo systemctl start nginx
sudo systemctl enable elasticsearch
```

---

## ✅ 总结：Supervisor vs systemd
| 功能/维度 | Supervisor | systemd |
| --- | --- | --- |
| 配置复杂度 | 简单 | 稍高 |
| 进程守护能力 | 较好 | 极强（支持依赖、资源限制等） |
| 系统集成度 | 低 | 高（系统服务标准方式） |
| 日志方式 | 文件 | journald（可统一集中查看） |
| 适合部署环境 | 本地开发 / 简易部署 | 生产环境 / 云服务器 |


---

## 🧰 建议选择
| 你的需求 | 推荐用法 |
| --- | --- |
| 本地测试 / 脚本部署 | Supervisor |
| 需要开机自启 + 守护运行 + 资源约束 | systemd |
| Docker 内运行 | 使用容器启动 |
| 混合方式 | 也可以让 systemd 启动 supervisord，然后 supervisor 启动进程 |


---

如果你告诉我你项目的安装路径，我可以帮你自动生成完整的 `.service` 文件或 `.conf` 文件。你希望用哪种方式来部署？是否还想加入 crontab / systemd.timer 任务计划调度？

