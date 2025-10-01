# Conda 开发与部署全流程使用笔记
适用于数据分析、Python 后端开发、科学计算等场景下的 Conda 环境管理、打包、迁移与部署流程。

---

## 🧱 1. 安装与初始化 Conda
### 1.1 安装方式（推荐 Miniconda）
```bash
# Linux
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p ./miniconda

# Windows / macOS 用户可下载图形界面安装包
```

配置清华源

```powershell
tee ${HOME}/.condarc <<EOF
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
EOF


# 确认配置
conda config list

# 创建 Python 3.8 环境
conda create -y -n pan_env python=3.8

```

### 1.2 初始化终端
linux

```bash

source ./miniconda/bin/activate
conda create -y -n  pan_env python=3.8
conda create -y -n  pan_env python=3.12
conda activate pan_env
pip install uv  -i https://pypi.tuna.tsinghua.edu.cn/simple
uv pip install pyinstaller requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```



windows

```bash
conda init powershell

```



### 1.3 禁用 base 环境自动激活
```bash
conda config --set auto_activate_base false
```

---

## 🧪 2. 创建开发环境
### 2.1 创建并激活新环境
```bash
conda create -n myapp python=3.11
conda activate myapp
```

### 2.2 安装必要包
```bash
conda install numpy pandas requests flask
conda install -c conda-forge uvicorn gunicorn
```

### 2.3 查看环境信息
```bash
conda list        # 列出当前包
conda info        # 查看 Conda 基础信息
conda env list    # 所有环境
```

---

## ⚙ 3. 开发中配置与管理
### 3.1 配置国内镜像加速（推荐清华）
```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
```

### 3.2 使用 uv 替代 pip 安装加速（可选）
```bash
# 推荐使用 micromamba 安装 uv（uv 是 Rust 编写的快速 Python 包管理器）
mamba install -c conda-forge uv

# 安装依赖（支持 pyproject.toml 或 requirements.txt）
uv pip install -r requirements.txt
```

### 3.3 导出依赖文件
```bash
# 完整依赖列表（含版本、构建信息）
conda env export > environment.yml

# 只导出用户安装的包（更干净）
conda env export --from-history > environment.yml
```

---

## 🚀 4. 部署环境打包与迁移
### 4.1 使用 `conda-pack` 打包环境
```bash
conda install -c conda-forge conda-pack
conda pack -n myapp -o myapp_env.tar.gz
```

说明：打包后可传输至其他服务器解压使用。

### 4.2 迁移至目标服务器后激活
```bash
mkdir -p ~/envs/myapp
tar -xzf myapp_env.tar.gz -C ~/envs/myapp
source ~/envs/myapp/bin/activate
```

---

## 🔄 5. 更新与清理
### 5.1 更新环境中所有包
```bash
conda update --all
```

### 5.2 清理缓存节省空间
```bash
conda clean -a
```

---

## 📦 6. 部署中的 Conda 环境管理（生产）
### 6.1 使用 conda-run 执行脚本
```bash
conda run -n myapp python script.py
```

### 6.2 使用 Supervisor / Systemd 启动
```plain
# 以 systemd 为例
[Unit]
Description=MyApp with Conda

[Service]
ExecStart=/home/user/miniconda3/envs/myapp/bin/python /opt/myapp/server.py
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 🧩 7. 高级功能与插件
### 7.1 使用 `conda compare` 比较两个环境
```bash
conda compare env1 env2
```

### 7.2 使用 `repoquery` 进行依赖分析
```bash
conda repoquery depends flask
```

### 7.3 管理插件与条款（如 ToS）
```bash
conda tos
```

---

## 🐳 8. 结合 Docker 部署 Conda 环境
### 8.1 基础镜像构建 Dockerfile 示例
```dockerfile
FROM continuumio/miniconda3

# 拷贝环境文件并创建环境
COPY environment.yml /opt/app/environment.yml
RUN conda env create -f /opt/app/environment.yml

# 激活环境并设置默认运行目录
SHELL ["/bin/bash", "-c"]
RUN echo "conda activate myapp" >> ~/.bashrc

# 拷贝应用代码并设置启动命令
COPY . /opt/app
WORKDIR /opt/app
CMD ["bash", "-c", "source ~/.bashrc && python main.py"]
```

### 8.2 构建镜像与运行容器
```bash
docker build -t myapp-conda .
docker run -it --rm myapp-conda
```

---

## 🧊 9. 使用 Nuitka 打包 Conda Python 应用
### 9.1 安装 Nuitka 并准备打包环境
```bash
conda activate myapp
pip install nuitka
```

### 9.2 打包主程序（静态链接）
```bash
nuitka --standalone --enable-plugin=numpy --enable-plugin=pylint \
       --output-dir=dist main.py
```

### 9.3 将可执行文件打入 Docker 镜像（可选）
```dockerfile
FROM ubuntu:22.04
COPY dist/main.dist /opt/app/
WORKDIR /opt/app
CMD ["./main"]
```

---

## ✅ 附录：常见问题排查命令
| 场景 | 命令 |
| --- | --- |
| 查看 Conda 健康状态 | `conda doctor` |
| 查看已安装源配置 | `conda config --show-sources` |
| 重建缓存索引 | `conda clean --index-cache` |


---

建议将此文件保存在项目根目录作为开发规范参考，也可集成进 CI/CD 流程中。

