以下是针对 UFW（Uncomplicated Firewall）的常用命令及使用笔记，帮助你快速上手并高效管理防火墙。

---

## 一、简介
UFW（Uncomplicated Firewall）是 Ubuntu 及其它 Debian 系统上推荐的 iptables 前端工具，旨在简化防火墙配置。它默认使用 IPv4/IPv6，适合大多数场景。

---

## 二、版本查看
```bash
ufw version
# 显示 UFW 版本及版权信息
```

**建议**：定期检查版本，确保使用最新稳定版以获得最新特性和安全修复。

---

## 三、基本操作
| 操作 | 命令 | 说明 |
| --- | --- | --- |
| 启用防火墙 | `ufw enable` | 开启并启动 UFW |
| 禁用防火墙 | `ufw disable` | 关闭 UFW |
| 重载规则 | `ufw reload` | 应用已修改的规则（无需重启） |
| 重置配置 | `ufw reset` | 清空所有规则并恢复默认设置 |
| 查看状态 | `ufw status` | 简要显示允许/拒绝列表 |
| 查看编号状态 | `ufw status numbered` | 列出带编号的所有规则，便于删除 |
| 查看详细状态 | `ufw status verbose` | 显示详细状态（包括默认策略、日志级别） |


---

## 四、默认策略
设置防火墙默认行为（_在添加任何具体规则前_）：

```bash
ufw default deny incoming    # 拒绝所有入站连接（推荐）
ufw default allow outgoing   # 允许所有出站连接（推荐）
ufw default deny outgoing    # 拒绝所有出站连接（谨慎使用）
ufw default allow incoming   # 允许所有入站连接（仅测试环境）
```

**意见**：生产环境中通常采用 “拒绝入站、允许出站” 的策略，然后再开放必要端口。

---

## 五、添加/删除规则
### 1. 基本规则
```bash
ufw allow 22              # 允许 TCP 22 端口（SSH）
ufw deny 23               # 拒绝 TCP 23 端口（Telnet）
ufw reject 25             # 拒绝并回复 ICMP/TTL 信息（SMTP）
ufw limit 22              # 防暴力破解：限制 SSH 连接频率
```

**建议**：对 SSH 使用 `limit`，可有效防止暴力破解尝试。

### 2. 指定协议和源/目的 IP
```bash
ufw allow proto tcp from 192.168.1.0/24 to any port 3306
# 只允许 192.168.1.0/24 网段访问本机 MySQL

ufw deny proto udp from any to any port 631
# 拒绝所有 UDP 631（IPP） 请求
```

### 3. 删除规则
+ 按文本删除：

```bash
ufw delete allow 22
```

+ 按编号删除：

```bash
ufw status numbered            # 先查看编号
ufw delete 3                    # 删除编号为 3 的规则
```

---

## 六、插入与前置规则
+ 在最前面插入规则：

```bash
ufw insert 1 allow 80         # 将 HTTP 规则插入到第一位
```

+ 前置规则（类似插入首位）：

```bash
ufw prepend deny from 10.0.0.5
```

**场景**：当已有规则生效但需要更高优先级时，使用插入/前置功能。

---

## 七、路由规则
+ 添加路由转发规则：

```bash
ufw route allow proto tcp from any to 10.0.0.1 port 8080
```

+ 删除或插入路由规则同上，可使用 `route delete`、`route insert`。

---

## 八、日志管理
```bash
ufw logging off      # 关闭日志
ufw logging low      # 记录简要信息（默认）
ufw logging medium   # 记录更多信息
ufw logging high     # 记录详细信息（含所有数据包）
```

**意见**：排查问题时可切换到 medium；生产环境建议 low 或 off，以减少磁盘 IO。

---

## 九、应用配置
UFW 内置常见服务配置（profiles），方便一键应用。

```bash
ufw app list          # 列出所有可用应用
ufw app info OpenSSH  # 查看某个应用的端口/协议定义
ufw allow OpenSSH     # 一次性允许所有 OpenSSH 所需端口
ufw deny Deluge       # 一次性拒绝 Deluge 应用
ufw app update DNS    # 更新应用配置（需／etc/ufw/applications.d/ 定义）
ufw app default WWW   # 设置默认应用策略
```

---

## 十、实用示例
1. **开启 Web 服务**

```bash
ufw allow http       # 等同于 allow 80/tcp
ufw allow https      # 等同于 allow 443/tcp
```

2. **限制特定 IP 访问**

```bash
ufw deny from 203.0.113.5
```

3. **打开某端口范围**

```bash
ufw allow 1000:2000/tcp
```

4. **多网段放行**

```bash
ufw allow from 10.0.0.0/8 to any port 22
ufw allow from 172.16.0.0/12 to any port 22
ufw allow from 192.168.0.0/16 to any port 22
```

---

## 十一、常见注意事项
+ **规则顺序**：UFW 依照先后顺序匹配，插入/前置功能可调整优先级。
+ **状态检查**：`status verbose` 最全面，还能看到默认策略。
+ **防火墙“锁死”警告**：启用前务必确认已有 SSH 规则，避免远程断连。
+ **备份配置**：`ufw export > ufw-backup.txt`（Ubuntu 20.04 以上支持），或者脚本化 `ufw status numbered` 并保存。

---

通过上述笔记，你可以快速上手 UFW，并根据生产/测试环境灵活调整策略。建议在推送到线上前在本地或测试机器模拟演练，确保配置无误。祝使用顺利！

