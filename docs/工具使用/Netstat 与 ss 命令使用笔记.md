# Netstat 与 ss 命令使用笔记
---

## 一、`netstat` 命令详解
### 1.1 常用参数表格
#### 命令参数
| 参数 | 说明 | 使用场景示例 |
| --- | --- | --- |
| `-a` | 显示所有连接（包括监听和非监听） | `netstat -a` 查看所有活动连接 |
| `-t` | 仅显示 TCP 连接 | `netstat -tn` 查看所有 TCP 连接（数值格式） |
| `-u` | 仅显示 UDP 连接 | `netstat -u` 查看 UDP 数据传输 |
| `-n` | 以数值格式显示地址和端口号 | `netstat -tnl` 避免 DNS 解析延迟 |
| `-l` | 仅显示监听端口 | `netstat -l` 快速定位服务监听状态 |
| `-p` | 显示 PID 和进程名称（需 root 权限） | `sudo netstat -tulp` 排查端口占用进程 |
| `-r` | 显示路由表 | `netstat -rn` 检查网络路由配置 |
| `-s` | 显示各协议的统计信息 | `netstat -s` 分析丢包/错误统计 |
| `-c` | 持续实时刷新输出 | `netstat -ct` 监控实时连接变化 |
| `-e` | 显示扩展信息（如 MAC 地址） | `netstat -ie` 查看网卡物理地址 |
| `-W` | 不截断长输出内容 | `netstat -aW` 完整显示长进程名 |
| `-g` | 显示多播组信息 | `netstat -g` 检查组播订阅情况 |


#### `ss` 支持的 TCP 连接状态
`ss -nt state <状态>` 可以筛选指定状态的连接。常见的 TCP 连接状态如下：

| 状态 | 说明 |
| --- | --- |
| **ESTABLISHED** | 连接已建立，数据正在传输 |
| **SYN-SENT** | 发送了 SYN 连接请求，等待对方响应（通常表示客户端主动连接服务器） |
| **SYN-RECV** | 服务器收到了 SYN 并回复了 SYN-ACK，等待客户端的 ACK |
| **FIN-WAIT-1** | 主动关闭连接，已发送 FIN 请求，等待对方 ACK |
| **FIN-WAIT-2** | 进入半关闭状态，等待对方发送 FIN |
| **TIME-WAIT** | 收到了 FIN，并发送了 ACK，等待一段时间后关闭（防止旧数据包干扰新连接） |
| **CLOSE-WAIT** | 收到了 FIN，但本地还未关闭连接（等待应用程序关闭 socket） |
| **LAST-ACK** | 已发送 FIN 并等待对方 ACK，等待后关闭连接 |
| **LISTEN** | 服务器监听状态，等待新的连接 |
| **CLOSING** | 发送了 FIN，同时收到了对方的 FIN，等待关闭（不常见） |
| **CLOSED** | 连接已关闭，不再使用 |


#### `ss` 显示的 UDP 连接状态
| 状态 | 说明 |
| --- | --- |
| **UNCONN** | 无连接状态（UDP 是无连接的，所以 UDP 套接字通常处于此状态） |
| **ESTAB** | 仅在某些特定情况下（如某些内核实现的 UDP 连接跟踪）会出现 |
| **CLOSE** | 关闭状态（不常见） |


### 1.2 实际场景示例
#### 场景1：检查 Web 服务是否监听
```bash
# 查看 80/443 端口监听状态（TCP）
sudo netstat -tulnp | grep -E ':80|:443'
```

#### 场景2：诊断网络路由问题
```bash
# 显示 IPv4 路由表（数值格式）
netstat -rn -4
```

#### 场景3：分析网络吞吐瓶颈
```bash
# 持续监控 TCP 连接变化（每秒刷新）
watch -n 1 "netstat -ctn | grep ESTABLISHED"
```

---

## 二、`ss` 命令详解
### 2.1 常用参数表格
| 参数 | 说明 | 使用场景示例 |
| --- | --- | --- |
| `-a` | 显示所有连接（监听+非监听） | `ss -a` 全面扫描所有 sockets |
| `-t` | 仅显示 TCP 连接 | `ss -t` 快速过滤 TCP 协议 |
| `-u` | 仅显示 UDP 连接 | `ss -u` 检查 UDP 数据流 |
| `-n` | 数值格式显示地址/端口 | `ss -nt` 避免反向解析提升速度 |
| `-l` | 仅显示监听端口 | `ss -lt` 查看 TCP 监听服务 |
| `-p` | 显示进程信息（需 root） | `sudo ss -tp` 定位端口占用进程 |
| `-r` | 解析主机名和服务名 | `ss -tr` 直观显示域名和服务 |
| `-s` | 显示统计摘要 | `ss -s` 统计连接状态分布 |
| `-4` | 仅显示 IPv4 连接 | `ss -t4` 排查 IPv4 网络问题 |
| `-6` | 仅显示 IPv6 连接 | `ss -u6` 检查 IPv6 服务状态 |
| `-m` | 显示 socket 内存使用 | `ss -tm` 分析内存占用情况 |
| `-i` | 显示 TCP 内部信息 | `ss -ti` 查看拥塞窗口/RTT 等 |


### 2.2 实际场景示例
#### 场景1：快速定位高并发连接
```bash
# 统计每个 IP 的连接数（TOP 5）
ss -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head -5
```

#### 场景2：分析 TCP 性能指标
```bash
# 查看 ESTABLISHED 连接的详细参数
ss -tni state established
```

#### 场景3：检查端口复用情况
```bash
# 显示重用 TIME-WAIT 的 sockets
ss -to state time-wait
```

---

## 三、高级技巧与对比
### 3.1 性能对比
| 操作 | netstat 耗时 | ss 耗时 | 差异原因 |
| --- | --- | --- | --- |
| 扫描 10K 连接 | ~2.3s | ~0.15s | netstat 解析 `/proc/net`，ss 直接读取内核数据 |


### 3.2 特殊状态过滤（ss 独有）
```bash
# 查看所有 TIME-WAIT 连接
ss -nt state time-wait

# 过滤 SYN-SENT 状态的连接
ss -nt state syn-sent
```

---



## 四、注意事项
1. **生产环境优先使用 ss**：在处理大量连接时速度更快
2. **权限管理**：查看进程信息（`-p`）需 root 权限
3. **连接状态解读**：
    - `LISTEN`：服务端等待连接
    - `ESTABLISHED`：活跃数据交换
    - `TIME-WAIT`：等待关闭（持续 2MSL）
4. **数值显示建议**：排查问题时始终使用 `-n` 参数避免 DNS 延迟

---

**常用组合命令**  

```bash
# 黄金命令：显示所有 TCP 连接详情
sudo ss -ntupo

# 监控实时连接变化（每秒刷新）
watch -n 1 "ss -ntu -a"
```

此版本文档通过：

1. 结构化表格明确参数用途
2. 真实场景命令示例
3. 性能数据对比
4. 状态机关键知识提示  
使内容更符合运维实际需求。

