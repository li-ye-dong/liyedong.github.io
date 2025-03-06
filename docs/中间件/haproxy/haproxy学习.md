# Haproxy+Keeplived实践

在 **RHEL 7.9** 上配置 **HAProxy** 和 **Keepalived** 的高可用负载均衡架构时，目标是确保高可用性、负载均衡和自动故障转移。以下是配置 **HAProxy + Keepalived** 的最佳实践步骤。

### 1. 安装 HAProxy 和 Keepalived

在两台服务器上分别安装 **HAProxy** 和 **Keepalived**。

#### 安装 HAProxy

1. 在 **Server1** 和 **Server2** 上安装 **HAProxy**：

   ```bash
   sudo yum install -y haproxy
   ```

2. 启动并设置开机启动：

   ```bash
   sudo systemctl start haproxy
   sudo systemctl enable haproxy
   ```

#### 安装 Keepalived

1. 在 **Server1** 和 **Server2** 上安装 **Keepalived**：

   ```bash
   sudo yum install -y keepalived
   ```

2. 启动并设置开机启动：

   ```bash
   sudo systemctl start keepalived
   sudo systemctl enable keepalived
   ```

### 2. 配置 HAProxy

**HAProxy** 提供负载均衡功能，我们需要配置后端服务器以及监听前端虚拟 IP。

#### 配置文件 `/etc/haproxy/haproxy.cfg`

假设你有两个后端应用服务器，分别是 `192.168.1.20` 和 `192.168.1.21`，也可以使用域名，根据场景来使用，你希望将 HTTP 请求均衡到这两个后端服务器。

```bash
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    maxconn 200
    user haproxy
    group haproxy
    daemon

defaults
    mode                    http
    log                     global
    option                  httplog
    option                  dontlognull
    option http-server-close
    option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000
#前端配置
frontend https_frontend
  bind *:443
  mode tcp
  default_backend vcs_clus
#后端配置
backend vcs_clus
  mode tcp
  balance roundrobin
  stick-table type ip size 200k expire 30m
  stick on src
  server vcs1 xmview04-c-m.kehua.org:443 check
  server vcs2 xmview04-c-s.kehua.org:443 check
#监控页面
listen stats
        mode http
        bind :9999
        stats enable
        log global
        stats uri /haproxy-status
        stats auth haadmin:P@ssw0rd

```

### 3. 配置 Keepalived

**Keepalived** 配置负责虚拟 IP 地址（VIP）的高可用性。设置 VIP 地址，当主节点失效时，VIP 会自动切换到备节点。

#### 配置文件 `/etc/keepalived/keepalived.conf`

##### 主节点（Server1）的配置：

```bash
vrrp_instance VI_1 {
    state MASTER
    interface eth0  # 根据实际网卡调整
    virtual_router_id 51
    priority 101  # 主节点优先级高
    advert_int 1
    virtual_ipaddress {
        192.168.1.100  # 配置虚拟 IP 地址
    }
}
```

##### 从节点（Server2）的配置：

```bash
vrrp_instance VI_1 {
    state BACKUP
    interface eth0  # 根据实际网卡调整
    virtual_router_id 51
    priority 100  # 从节点优先级低
    advert_int 1
    virtual_ipaddress {
        192.168.1.100  # 配置虚拟 IP 地址
    }
}
```

#### 配置说明：

- `state MASTER` 和 `state BACKUP`：定义了主节点和备节点的角色。
- `priority`：主节点的优先级应该高于从节点，主节点优先接管虚拟 IP。
- `advert_int`：VRRP 广播间隔时间，默认是 1 秒。
- `virtual_ipaddress`：指定虚拟 IP 地址，该地址将由 Keepalived 管理并在节点之间自动切换。

### 4. 配置防火墙和 SELinux

#### 开放防火墙端口

1. 开放 **HAProxy** 的 HTTP 端口（默认 80）：

   ```bash
   sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
   sudo firewall-cmd --reload
   ```

2. 开放 **Keepalived** 所需端口，尤其是 VRRP 使用的端口（默认是 `112`）：

   ```bash
   sudo firewall-cmd --zone=public --add-port=112/udp --permanent
   sudo firewall-cmd --reload
   ```

#### 配置 SELinux（如果启用了）

1. 设置 SELinux 为允许 HTTP 服务和虚拟 IP 的操作：

   ```bash
   sudo setsebool -P httpd_can_network_connect 1
   sudo setsebool -P net_admin 1
   ```

### 5. 启动服务并验证配置

#### 启动并验证 **HAProxy** 和 **Keepalived** 服务

1. 启动 **HAProxy**：

   ```bash
   sudo systemctl restart haproxy
   ```

2. 启动 **Keepalived**：

   ```bash
   sudo systemctl restart keepalived
   ```

3. 确认服务正常运行：

   ```bash
   sudo systemctl status haproxy
   sudo systemctl status keepalived
   ```

#### 验证虚拟 IP 地址（VIP）

1. 在 **Server1** 上，检查 VIP 地址（`192.168.1.100`）是否已分配：

   ```bash
   ip a show eth0
   ```

   你应该看到虚拟 IP 地址已经绑定到 `eth0` 接口上。

2. 在 **Server2** 上，确保没有 VIP 地址绑定。如果主节点（`Server1`）故障，VIP 会切换到 **Server2**。

3. 停止 **Server1** 上的 **Keepalived** 服务，检查 VIP 是否会切换到 **Server2**：

   ```bash
   sudo systemctl stop keepalived
   ```

4. 使用 `ip a show eth0` 在 **Server2** 上检查虚拟 IP 地址是否已经迁移。

### 6. 测试负载均衡和高可用性

#### 测试负载均衡

1. 向 VIP 地址（`192.168.1.100`）发送请求：

   ```bash
   curl http://192.168.1.100
   ```

2. 确认请求轮询分发到后端服务器 `192.168.1.20` 或 `192.168.1.21`，你可以根据不同的响应标识来确认请求是否均衡到不同的服务器。

#### 测试故障转移

1. 停止 **Server1** 上的 **HAProxy** 和 **Keepalived** 服务：

   ```bash
   sudo systemctl stop haproxy
   sudo systemctl stop keepalived
   ```

2. 验证 **Server2** 是否接管了 VIP，检查是否可以通过 `192.168.1.100` 访问负载均衡服务。

3. 启动 **Server1** 上的服务，VIP 应该自动切换回主节点。

### 7. 高可用性优化

#### 健康检查

- 确保后端服务器的健康检查功能启用，HAProxy 会定期检查后端服务器的状态，并根据健康状态调整负载均衡策略。

- 可以通过添加 

  ```
  check
  ```

   选项来启用健康检查：

  ```bash
  server server1 192.168.1.20:80 check
  server server2 192.168.1.21:80 check
  ```

#### Keepalived 警报设置

- 可以配置 Keepalived 的警报通知功能，当节点发生故障时发送邮件或其他通知：

  ```bash
  notify_master /usr/local/bin/send_email_master
  notify_backup /usr/local/bin/send_email_backup
  ```

#### 日志和监控

- 配置 HAProxy 日志输出，以便监控请求情况：

  ```bash
  global
      log /dev/log local0
  ```

- 配置 **Zabbix**、**Prometheus** 等监控工具，实时监控 HAProxy 和 Keepalived 服务的状态和负载情况。









### 8.高可用脚本

要在 `HAProxy` 和 `Keepalived` 配置中检测 `HAProxy` 是否存活，通常会使用一个 `healthcheck` 脚本来验证 `HAProxy` 服务的状态。`Keepalived` 会定期检查此脚本的返回值，如果返回 0（成功），则认为 `HAProxy` 存活；如果返回非 0（失败），则会触发故障转移。

以下是实现此功能的步骤：

#### 1. 创建检测 `HAProxy` 存活的脚本

你可以编写一个简单的脚本来检测 `HAProxy` 是否在监听其 HTTP/HTTPS 服务端口。可以通过 `curl` 来检查端口是否响应。

#### **示例脚本：**

假设你使用的是 HTTP 或 HTTPS 协议进行负载均衡（比如 `HAProxy` 配置的端口是 80 或 443）。

创建一个名为 `haproxy_check.sh` 的脚本文件：

```sh
#!/bin/bash
set -x
# 打印调试信息
echo "Checking HAProxy status..."

# 使用curl检查HAProxy是否在端口上响应
A=$(pidof -x haproxy | wc -l)

# 打印调试信息
echo "curl response count: $A"

# 如果HAProxy不可用（没有找到 200 OK），则认为HAProxy不可用
if [ $A -eq 0 ]; then
  echo "HAProxy is down"

  # 尝试杀掉HAProxy进程
  echo "Killing HAProxy..."
  pkill -x haproxy

  # 重启HAProxy
  echo "Restarting HAProxy..."
  systemctl restart haproxy
  sleep 2  # 等待2秒
  
  # 再次检查HAProxy状态
  A=$(pidof -x haproxy | wc -l)
  if [ $A -eq 0 ]; then
    echo "HAProxy still down, stopping keepalived..."
    systemctl stop keepalived  # 停止 keepalived
    exit 1  # 如果HAProxy依然不可用，返回1
  else 
    echo "HAProxy already started success!"
  fi
else
  echo "HAProxy is up"
  exit 0  # 如果HAProxy服务可用，返回0
fi
```

保存此文件到 `/etc/keepalived/` 或其他合适的目录，并赋予执行权限：

```
chmod +x /etc/keepalived/haproxy_check.sh
```

#### 2. 配置 `Keepalived` 来使用该脚本检测 `HAProxy` 状态

在 `Keepalived` 的配置文件 `/etc/keepalived/keepalived.conf` 中，你可以将该脚本作为 `check` 动作的一部分。`Keepalived` 会定期调用此脚本来检查 `HAProxy` 是否存活。

**示例 `keepalived.conf` 配置：**

```sh
global_defs {
router_id HA-01
vrrp_skip_check_adv_addr
# vrrp_strict
vrrp_garp_interval 0
vrrp_gna_interval 0
script_user root 
}

vrrp_script check_haproxy {
    script "/etc/keepalived/haproxy_check.sh"
    interval 2
    weight -5
    rise 2
    fall 3
}


vrrp_instance VI_1 {
state MASTER
interface ens192
virtual_router_id 51
priority 100
advert_int 1

authentication {
auth_type PASS
auth_pass 1111
}

virtual_ipaddress {
192.168.108.51
}
track_script {
    check_haproxy
}
}
```





```
global_defs {
router_id HA-01
vrrp_skip_check_adv_addr
# vrrp_strict
vrrp_garp_interval 0
vrrp_gna_interval 0
script_user root 
}

vrrp_script check_haproxy {
    script "/etc/keepalived/haproxy_check.sh"
    interval 2
    weight -5
    rise 2
    fall 3
}


vrrp_instance VI_1 {
state BACKUP
interface ens192
virtual_router_id 51
priority 90
advert_int 1

authentication {
auth_type PASS
auth_pass 1111
}

virtual_ipaddress {
192.168.108.51
}
track_script {
    check_haproxy
}
}
```



#### 3. 启动并测试

- 配置完成后，重启 `Keepalived` 服务：

```sh
systemctl restart keepalived
```

- 使用以下命令检查 `Keepalived` 和 `HAProxy` 状态：

```sh
systemctl status keepalived
systemctl status haproxy
```

- 在 `HAProxy` 服务不可用的情况下，通过脚本重启haproxy，如果。

```sh
systemctl stop haproxy
```

- 

#### 4. 高级配置

你还可以根据需要定制检测方式，比如：

- 检查 `HAProxy` 进程是否存在：

  ```sh
  bash复制代码#!/bin/bash
  ps aux | grep -v grep | grep haproxy > /dev/null
  if [ $? -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
  ```

- 检查 `HAProxy` 配置是否正确：

  ```sh
  bash复制代码#!/bin/bash
  haproxy -c -f /etc/haproxy/haproxy.cfg > /dev/null
  if [ $? -eq 0 ]; then
    exit 0
  else
    exit 1
  fi
  ```

#### 总结

通过上述步骤，你可以设置 `Keepalived` 定期检测 `HAProxy` 服务的存活情况，确保高可用性。如果 `HAProxy` 服务不可用，`Keepalived` 会触发故障转移操作，确保流量转发到可用的后端服务器。

