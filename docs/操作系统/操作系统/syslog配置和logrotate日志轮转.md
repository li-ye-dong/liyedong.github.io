如bind9  dns的syslog配置,/etc/named.conf

```sql
logging {
    channel syslog_channel {
        syslog local0;             // 使用 syslog 的 local0 facility
        severity info;             // 设置日志级别，可改为 debug、notice 等
        print-time yes;
        print-severity yes;
        print-category yes;
    };
    channel debug_channel {
        file "data/debug.log" versions 3 size 10m;
        severity debug 3;
        print-time yes;
        print-severity yes;
        print-category yes;
    };
    category queries { syslog_channel; };
    category debug { debug_channel; };
};

```

配置syslog写入 

/etc/rsyslog.d/bind9.conf

```sql
# 1. 本地保存日志到文件
local0.*    /var/log/named.log

# 2. 远程转发日志到 syslog 服务器（使用 UDP）@ UDP   @@为TCP
local0.*    @192.168.xxx.xxx:514

```

配置日志轮转

/etc/logrotate.d/bind

```sql
/var/log/named.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
    su root root
    create 644 root root
}

```

**说明**：

+ `/var/log/named.log`：指定轮转的日志文件。
+ `daily`：每天轮转一次日志。
+ `rotate 7`：保留最多 7 个轮转文件（例如 `named.log.1`, `named.log.2`, ...）。
+ `compress`：启用日志压缩，通常使用 `.gz` 格式。
+ `delaycompress`：推迟一轮才压缩日志，以防止正在写入的日志文件被压缩。
+ `copytruncate`：轮转时复制日志并截断原文件（对正在写入的日志非常重要）。
+ `create 644 root root`：指定创建新的日志文件时的权限和所有者。

```sql
#检查文件配置
sudo logrotate -d /etc/logrotate.d/bind
#强制轮转一次
sudo logrotate -f /etc/logrotate.d/bind

```

| 配置项 | 含义说明 |
| --- | --- |
| `daily`<br/> / `weekly`<br/> / `monthly`<br/> / `yearly` | 日志轮转周期 |
| `rotate N` | 保留 N 个旧日志文件，超过会删除 |
| `compress` | 使用 gzip 压缩旧日志（生成 `.gz`<br/> 文件） |
| `nocompress` | 禁止压缩旧日志 |
| `delaycompress` | 推迟一轮再压缩（与 `compress`<br/> 一起用） |
| `missingok` | 如果日志文件不存在，继续执行，不报错 |
| `nomissingok` | 文件不存在时报错（默认） |
| `notifempty` | 如果日志为空，就不轮转 |
| `ifempty` | 即使日志为空，也轮转（默认） |
| `create MODE OWNER GROUP` | 创建新日志文件并设置权限/属主 |
| `copytruncate` | 复制日志后截断原日志（不关闭原文件） |
| `nocopytruncate` | 禁用此行为（默认） |
| `sharedscripts` | 所有日志轮转后只执行一次 postrotate 脚本（默认建议） |
| `postrotate ... endscript` | 日志轮转后执行的脚本（如重启日志服务） |
| `prerotate ... endscript` | 日志轮转前执行的脚本 |
| `dateext` | 使用日期扩展而不是 `.1`、`.2`<br/> 命名 |
| `dateformat .%Y-%m-%d` | 配合 `dateext`<br/> 指定日期格式（如 `.2025-04-30`<br/>） |


## 777目录配置日志轮转
```sql
tee /etc/logrotate.d/nginx << 'EOF'
/u01/sinoservices/logs/nginx/host.access.log {
    daily
    rotate 15
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
    su root root
    create 777 root root
}
EOF



logrotate -d /etc/logrotate.d/nginx
#强制轮转一次
sudo logrotate -f /etc/logrotate.d/nginx
```

