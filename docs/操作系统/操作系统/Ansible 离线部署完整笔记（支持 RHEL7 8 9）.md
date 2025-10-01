本笔记涵盖两种方式部署 Ansible：

+ 使用 Miniconda
+ 使用 Rye（现代 Python 工具链）

最终目标为实现：

+ 在无网环境下安装完整 Ansible 生态
+ 包含 molecule 测试框架与 ansible-lint 等工具
+ 内置 playbook 示例
+ 提供一键初始化与 systemd 自动执行能力

---

## 一、Miniconda 方式部署 Ansible
### 打包整个虚拟环境部署ansible(推荐)
在线搭建虚拟环境

```bash
#!/bin/bash
mkdir ansible && cd ansible
# 安装 Miniconda 到本地目录
curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p ./miniconda
    
# 初始化 conda 环境
source ./miniconda/bin/activate
conda create -y -n ansible-env python=3.9
conda activate ansible-env
pip install \
  ansible==8.7.0 \
  ansible-core==2.15.13 \
  ansible-lint==6.22.2 \
  molecule[docker]==6.0.3 \
  docker==7.1.0 \
  netaddr==1.3.0 \
  jmespath==1.0.1 \
  requests==2.32.3 -i https://pypi.tuna.tsinghua.edu.cn/simple
conda install -y conda-pack

conda-pack -o ansible-env.tar.gz

mkdir ansible
tar -xzf ansible-env.tar.gz -C ansible/
cd ansible
cat > ansible.cfg <<EOF
[defaults]
inventory = /opt/ansible/inventory.ini
EOF
cat > inventory.ini <<EOF
[master]
master ansible_host=192.168.107.101 ansible_user=root
[slave]
slave01 ansible_host=192.168.107.101 ansible_user=root
slave02 ansible_host=192.168.107.101 ansible_user=root
EOF
tee /etc/profile.d/ansible_path.sh << 'EOF'
export PATH=/opt/ansible/bin:$PATH
EOF
sudo echo "export ANSIBLE_CONFIG=/opt/ansible/ansible.cfg" > ansible_cfg_path.sh
cd ..
tar -czvf  ansible.tar.gz ansible/*
```

部署虚拟环境到其他机器

```bash
#!/bin/bash
#部署
mkdir -p /opt/ansible-env
mkdir -p /etc/ansible
tar -xzf ansible-env.tar.gz -C /opt/ansible-env
cd /opt/ansible-env
sudo echo "export PATH=/opt/ansible/bin:$PATH" > /etc/profile.d/ansible_path.sh
sudo echo "export ANSIBLE_CONFIG=/etc/ansible/ansible.cfg" > /etc/profile.d/ansible_cfg_path.sh
source /etc/profile.d/ansible_path.sh
source /etc/profile.d/ansible_cfg_path.sh
ln -s /opt/ansible-env /opt/ansible
ansible --version

#指定默认的ansible配置文件
cat > /etc/ansible/ansible.cfg <<EOF
[defaults]
inventory = /etc/ansible/inventory.ini
host_key_checking = False
EOF

touch /etc/ansible/inventory.ini
```

```bash
#!/bin/bash
tar -xzf ansible.tar.gz -C /opt/
cp /opt/ansible/*.sh /etc/profile.d/
tee /etc/profile.d/ansible_path.sh << 'EOF'
export PATH=/opt/ansible/bin:$PATH
EOF
source /etc/profile.d/ansible_path.sh
source /etc/profile.d/ansible_cfg_path.sh
```

## 二、初始化脚本（inventory + hosts 配置）
### `init-ansible-env.sh`
```bash
#!/bin/bash
set -e

# 配置 hosts 文件
cat >> /etc/hosts <<EOF
192.168.107.101 node1
192.168.107.102 node2
EOF

cat > /opt/ansible/inventory.ini <<EOF
[node_group]
node01 ansible_host=192.168.107.101 ansible_user=root
node02 ansible_host=192.168.107.102 ansible_user=root
EOF
# 测试 ping
ansible all -m ping
```

---

## 三、playbook 示例：`playbooks/site.yml`
### 安装 nginx
```yaml
- name: 安装 nginx 并启动
  hosts: node_group
  become: true
  tasks:
    - name: 安装 nginx
      package:
        name: nginx
        state: present

    - name: 启动 nginx
      service:
        name: nginx
        state: started
        enabled: true
```

---

## 四、systemd 自动化服务（ansible-pull）
### `/etc/systemd/system/ansible-pull.service`
```toml
[Unit]
Description=Run Ansible Pull
After=network.target

[Service]
Type=oneshot
ExecStart=/root/miniconda/envs/ansible-env/bin/ansible-pull -i /opt/ansible/inventory.ini -U file:///opt/ansible/playbooks -C master -d /tmp/ansible

[Install]
WantedBy=multi-user.target
```

### 启用服务
```bash
systemctl daemon-reexec
systemctl enable --now ansible-pull.service
```

---

这份笔记可以作为内部交付、离线部署文档或 Git 项目模板，后续我也可以帮你封装一键打包脚本或完整打包压缩包。

## 五、扩展介绍
### 📦 `ansible`
+ **核心工具**：包含完整的 Ansible CLI（如 `ansible`、`ansible-playbook` 等）。
+ 已包含 `ansible-core`，是最常用的包。
+ 推荐直接安装它，而不是单独安装 `ansible-core`。

---

### 📦 `ansible-core`
+ **Ansible 的最基础组件**，包括：
    - 命令解析器
    - 模块运行引擎
    - 插件机制等
+ 如果你只做二次开发或需要极简版本才需要单独安装。

✅ 正常使用只需装 `ansible`，它会自动依赖 `ansible-core`。

---

### 📦 `ansible-lint`
+ **Ansible 语法规范检查工具**。
+ 可自动识别：
    - YAML 格式错误
    - 变量未定义
    - 模块使用不规范
+ 是 DevOps 团队中非常常见的质量保障工具。

---

### 📦 `molecule[docker]`
+ **测试 Ansible Role/Playbook 的标准框架**。
+ `molecule` 本身支持多种 provider，这里 `[docker]` 是启用 Docker backend 的支持。
+ 可以用来在本地容器里运行 playbook 做验证（尤其适合开发时测试角色 role）。

---

### 📦 `docker`
+ 是 Python 的 Docker SDK，给 `molecule[docker]` 使用的。
+ 也可以用来编写自动化脚本，控制 Docker 镜像和容器。

---

### 📦 `netaddr`
+ 用于处理 IP 地址、CIDR、网段等操作。
+ Ansible 中的某些网络模块或过滤器（如 `ipaddr()`）依赖此包。

---

### 📦 `jmespath`
+ 用于对 JSON/YAML 数据结构执行查询（在 playbook 中经常用于 `json_query` filter）。
+ 类似于 jq 的语法，Ansible 自带支持，但可以指定版本。

---

### 📦 `requests`
+ 常用的 Python HTTP 客户端库。
+ 虽然不是 Ansible 的直接依赖，但很多模块（如 `uri`、某些自定义模块）使用它访问 API。

---

### ✅ 总结（建议用途分类）
| 包名 | 作用分类 | 推荐场景 |
| --- | --- | --- |
| `ansible` | 核心工具 | 必装 |
| `ansible-core` | 可选核心 | 特殊需求可选（如容器极简） |
| `ansible-lint` | 代码规范 | 开发/团队协作建议装 |
| `molecule[docker]` | 测试框架 | 开发、CI/CD 场景 |
| `docker` | 容器控制 | molecule、自动化运维 |
| `netaddr` | 网络工具 | 复杂网络配置 playbook |
| `jmespath` | 数据查询 | 使用 `json_query`<br/> 时必须 |
| `requests` | 通用依赖 | 编写 API 自动化任务时有用 |






