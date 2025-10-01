已思考若干秒

**Fail2ban** 是一款用 Python 编写的入侵防御工具，主要用于自动检测并阻止针对服务器的暴力破解攻击。以下是关于 Fail2ban 的要点整理和一些个人建议：

---

## 一、什么是 Fail2ban
1. **核心功能**
    - 监控日志文件（如 `/var/log/auth.log`、`/var/log/secure` 等），实时检测错误登录或可疑行为。
    - 一旦发现超过设定次数的失败尝试，即自动在防火墙（iptables、UFW、firewalld 等）中添加临时或永久的封禁规则，阻止该 IP 继续攻击。
2. **适用场景**
    - SSH、FTP、邮件服务（Postfix/Dovecot）、Web 面板等常见网络服务的暴力破解防护。
    - 可用于各类 Linux 发行版，以及部分支持 Python 的类 Unix 系统。
3. **优点**
    - **轻量易用**：默认配置即能覆盖大多数场景，且扩展性强。
    - **可定制**：可以针对任意日志格式和服务编写自定义 Filter（过滤器）和 Jail（监狱）。
    - **日志中心化**：统一通过日志文件进行安全监控，不需要在服务端额外埋点。

---

## 二、安装与启动
```bash
# Ubuntu / Debian
sudo apt update
sudo apt install fail2ban

# CentOS / RHEL
sudo yum install epel-release
sudo yum install fail2ban

# 启动与开机自启
sudo systemctl enable --now fail2ban
sudo systemctl status fail2ban  # 查看运行状态
```

---

## 三、工作原理简述
1. **Filter（过滤器）**
    - 存放在 `/etc/fail2ban/filter.d/` 下，以正则表达式匹配日志中的“失败”条目。
2. **Jail（监狱）**
    - 存放在 `/etc/fail2ban/jail.d/` 或主配置 `/etc/fail2ban/jail.conf`，定义要监控哪个日志、用哪个 Filter、触发多少次失败后封禁、多长时间，以及封禁时调用哪个动作（action，如 iptables 封禁）。
3. **Action（动作）**
    - 默认使用 iptables 或 UFW 来添加封禁规则，也可配置发送邮件通知或调用自定义脚本。

---

## 四、常见配置项（`/etc/fail2ban/jail.local`）
```plain
[DEFAULT]
# 监控失败次数，超过后封禁
maxretry = 5              
# 检测窗口：多少分钟内累计失败次数
findtime = 10m            
# 封禁多长时间，默认 10 分钟；设置为 -1 表示永久封禁
bantime = 10m             

[sshd]
enabled = true            # 启用 SSH 监控
port    = ssh             
logpath = /var/log/auth.log
```

**个人建议**：

+ 把公共配置写在 `[DEFAULT]`，针对不同服务单独在 `[service]` 下调整 `maxretry`、`bantime`；
+ 对重要服务（如 VPN、数据库管理面板）可用更严格的 `maxretry=3` 和更长的 `bantime`；
+ 对内网 IP 段或可信 IP，可在 `ignoreip` 中添加白名单，避免误封。

---

## 五、常用命令
+ 查看当前被封禁的 IP：

```bash
sudo fail2ban-client status sshd
# 输出 Jail “sshd” 的状态和被封禁 IP 列表
```

+ 解封某个 IP：

```bash
sudo fail2ban-client set sshd unbanip 1.2.3.4
```

+ 暂停 / 恢复某个 Jail：

```bash
sudo fail2ban-client stop sshd
sudo fail2ban-client start sshd
```

+ 查看所有 Jail：

```bash
sudo fail2ban-client status
```

---

## 六、日志与监控
+ Fail2ban 本身会将操作记录到 `/var/log/fail2ban.log`，包括检测到的失败尝试和封禁/解封行为。
+ 可结合系统监控（如 Zabbix、Prometheus + Grafana）对日志进行报警和可视化。

---

## 七、进阶与扩展
1. **自定义 Filter**
    - 在 `filter.d` 下创建新文件，如 `custom.conf`，用正则定义需要匹配的日志模式；
    - 在 `jail.local` 中新增 `[custom]` 监控该 filter。
2. **邮件通知**
    - 修改 `action` 为 `action_mw`（邮件+警告），确保 `mta`（Postfix/Sendmail）已配置；
3. **与 UFW 配合**
    - 默认 Action 可自动适配 UFW，不需额外改动；
    - 若未生效，可在 `action.d/ufw.conf` 中检查命令模板。

---

## 八、 Fail2ban 配合 UFW  
下面示范如何让 Fail2ban 配合 UFW，自动对多次登录失败的 IP 进行封禁，并能在 UFW 里一目了然地查看和管理这些规则。

---

### 一、前提准备
1. **UFW 已安装并启用**

```bash
sudo ufw enable               # 启用 UFW（若还未启用）
sudo ufw default deny incoming  
sudo ufw default allow outgoing
```

2. **安装 Fail2ban**

```bash
sudo apt update
sudo apt install fail2ban     # Ubuntu/Debian 安装
sudo systemctl enable --now fail2ban
```

---

### 二、配置 Fail2ban 使用 UFW 作为封禁后端
1. 编辑 Fail2ban 的本地配置文件 `/etc/fail2ban/jail.local`（没有就新建）

```plain
[DEFAULT]
# 使用 UFW 来封禁 IP
# 翻译自英文: “Ban action to use. Default is iptables-multiport”
action = ufw  

# 其它全局策略，可根据需要调整
maxretry = 5               # 5 次失败后触发封禁
findtime = 10m             # 在 10 分钟内累计
bantime  = 1h              # 封禁 1 小时；-1 表示永久
ignoreip = 127.0.0.1/8 ::1 # 本机和本地 IPv6 不会被封
```

2. 针对 SSH 服务启用监控

```plain
[sshd]
enabled  = true                 # 启用 SSH 监控
port     = ssh                  # 监控默认 SSH 端口 22
logpath  = /var/log/auth.log    # SSH 登录的日志路径
```

3. 保存后重载 Fail2ban

```bash
sudo fail2ban-client reload
```

---

### 三、验证与管理
1. **查看所有 Jail 状态**

```bash
sudo fail2ban-client status
```

会列出 `sshd` 等已启用的监狱（Jail）。

2. **查看 SSH Jail 详细状态和被封 IP**

```bash
sudo fail2ban-client status sshd
```

输出示例：

```plain
Status for the jail: sshd
|- Filter
|  |- Currently failed: 0
|  `- Total failed:     12
`- Actions
   |- Currently banned: 2           # 当前被封的 IP 数量
   `- Banned IP list: 192.0.2.5 203.0.113.7
```

3. **在 UFW 中查看对应规则**

```bash
sudo ufw status numbered
```

你会看到类似：

```plain
[ 1] 192.0.2.5                  DENY IN    Anywhere
[ 2] 203.0.113.7                DENY IN    Anywhere
```

4. **手动解封某个 IP**
    - 通过 Fail2ban：

```bash
sudo fail2ban-client set sshd unbanip 192.0.2.5
```

    - 或直接在 UFW 删除对应规则编号：

```bash
sudo ufw delete 1
```

---

### 四、扩展思路
+ **全局都用 UFW**  
如果想让所有 Jail 默认都走 UFW，确保 `[DEFAULT] action = ufw` 写在最前面。
+ **自定义日志检测**  
对 Web 登录、FTP、数据库面板等服务，同样在 `jail.local` 加上相应区块即可。
+ **邮件通知**  
将 `action = ufw` 改为 `action = ufw-mwl`（mwl = mail with log），当封禁时会给管理员发邮件。

---

