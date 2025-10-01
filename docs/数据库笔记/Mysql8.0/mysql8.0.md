## MySQL 8.0 主要命令
---

### **一、服务器管理命令**
| 命令 | 功能 | 基本用法 |
| --- | --- | --- |
| **mysqld** | MySQL 服务器主程序 | `mysqld --verbose --help`   `mysqld --datadir=/var/lib/mysql` |
| **mysql_secure_installation** | 安全初始化向导 | `mysql_secure_installation` |
| **mysql_upgrade** | 升级系统表结构 | `mysql_upgrade -u root -p` |
| **mysql_tzinfo_to_sql** | 加载时区数据 | `mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root -p mysql` |


---

### **二、客户端工具**
| 命令 | 功能 | 基本用法 |
| --- | --- | --- |
| **mysql** | 命令行客户端 | `mysql -u root -p`   `mysql -e "SHOW DATABASES;"` |
| **mysqladmin** | 管理操作工具 | `mysqladmin -u root -p status`   `mysqladmin shutdown` |
| **mysql_config_editor** | 安全登录路径配置 | `mysql_config_editor set --login-path=local --host=localhost --user=root --password` |


---

### **三、备份与恢复**
| 命令 | 功能 | 基本用法 |
| --- | --- | --- |
| **mysqldump** | 逻辑备份工具 | `mysqldump -u root -p dbname > backup.sql`   `mysqldump --all-databases > full_backup.sql` |
| **mysqlpump** | 并行备份工具 | `mysqlpump -u root -p --parallel-workers=4 dbname` |
| **mysqlimport** | 数据导入工具 | `mysqlimport -u root -p dbname datafile.txt` |


---

### **四、日志与诊断**
| 命令 | 功能 | 基本用法 |
| --- | --- | --- |
| **mysqlbinlog** | 二进制日志工具 | `mysqlbinlog /var/lib/mysql/binlog.000123`   `mysqlbinlog --start-datetime="2024-01-01 00:00:00"` |
| **mysqldumpslow** | 慢查询日志分析 | `mysqldumpslow /var/lib/mysql/mysql-slow.log` |
| **myisamlog** | MyISAM 日志工具 | `myisamlog /var/lib/mysql/mysql.log` |


---

### **五、表维护工具**
| 命令 | 功能 | 基本用法 |
| --- | --- | --- |
| **myisamchk** | MyISAM 表检查修复 | `myisamchk /var/lib/mysql/db/tbl.MYI`   `myisamchk --recover tbl` |
| **myisampack** | MyISAM 表压缩工具 | `myisampack tbl.MYI` |
| **mysqlcheck** | 表维护工具 | `mysqlcheck -u root -p --optimize dbname` |


---

### **六、实用工具**
| 命令 | 功能 | 基本用法 |
| --- | --- | --- |
| **mysqlshow** | 查看数据库对象 | `mysqlshow -u root -p`   `mysqlshow dbname tblname` |
| **mysqlslap** | 负载模拟测试 | `mysqlslap -u root -p --concurrency=50 --iterations=100` |
| **my_print_defaults** | 读取选项文件配置 | `my_print_defaults client mysqld` |


---

### **七、加密与安全**
| 命令 | 功能 | 基本用法 |
| --- | --- | --- |
| **mysql_ssl_rsa_setup** | 生成SSL证书 | `mysql_ssl_rsa_setup --datadir=/var/lib/mysql` |
| **mysql_migrate_keyring** | 密钥迁移工具 | `mysql_migrate_keyring --help` |


---

### **典型使用场景示例**
#### 1. **创建备份并恢复**
```bash
# 备份单个数据库
mysqldump -u root -p mydb > mydb_backup.sql

# 恢复数据库
mysql -u root -p mydb < mydb_backup.sql
```

#### 2. **监控服务器状态**
```bash
# 查看服务器状态
mysqladmin -u root -p status

# 查看活跃进程
mysqladmin -u root -p processlist
```

#### 3. **修复损坏的MyISAM表**
```bash
myisamchk --recover /var/lib/mysql/db/tbl.MYI
```

#### 4. **分析慢查询**
```bash
mysqldumpslow -s t /var/lib/mysql/mysql-slow.log
```

---

### **注意事项**
1. 所有命令需确保MySQL服务已启动
2. 涉及权限操作时需使用`-u root -p`指定管理员账户
3. 生产环境操作前建议先备份数据

如需查看完整手册，可使用`man <command>`或`<command> --help`获取详细帮助信息。

## 安装和更新
### 二进制安装
[https://downloads.mysql.com/archives/community/](https://downloads.mysql.com/archives/community/)

```python
tar -xzf mysql-5.7.*.tar.gz -C /opt
ln -s /opt/mysql* /usr/local/mysql
ls /usr/local/mysql/bin
echo 'export=$PATH:/usr/local/mysql/bin' >> ~/.bashrc 
source ~/.bashrc
tee /etc/my.cnf << 'EOF'
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
user=mysql
[client-server]
!includedir /etc/my.cnf.d
[mysql]
auto-rehash
[mysqld_safe]
log-error=/var/log/mysqld.log
pid-file=/var/mysqld/mysqld.pid
EOF

useradd -r mysql
mysqld --initialize  #根据my.cnf创建数据目录
mkdir /var/run/mysqld 
chown mysql:mysql /var/run/mysqld


mysqld_safe
```

