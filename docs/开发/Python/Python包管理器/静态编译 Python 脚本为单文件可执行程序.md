## ✅ 一、使用 Nuitka 编译 Python 脚本为单文件可执行程序（兼容性强）
支持打包为 Linux ELF 可执行，部分支持静态链接（需依赖 musl libc 或 docker 构建）

### 1. 准备一个 Python 脚本：`hello.py`
```plain
python


复制编辑
def main():
    print("你好，来自 Nuitka 编译的 Python 可执行文件！")

if __name__ == "__main__":
    main()
```

---

### 2. 安装 Nuitka 和依赖（推荐 Python 3.9）
```plain
bash


复制编辑
pip install nuitka

# 推荐安装 C 编译器
# RHEL/CentOS 上：
sudo yum install gcc gcc-c++
```

---

### 3. 编译成单一可执行程序
```plain
bash


复制编辑
nuitka hello.py --onefile
```

生成的可执行文件是：`hello.bin`（可能带版本号）

---

### 4. 高级参数（静态链接更强兼容性）
```plain
bash


复制编辑
nuitka hello.py --onefile --standalone --nofollow-import-to=unwanted_module
```

如需 **完全静态链接（Zero dependency）**，建议在基于 `musl` 或 alpine 的 Docker 环境中操作，我们可以封装个 Dockerfile。

---

## ✅ 二、使用 PyOxidizer 打包 Python 应用为本地 ELF 文件
PyOxidizer 是 Mozilla 出品的 Rust 工具，可将 Python 应用打包为完全独立的二进制。

### 1. 安装 Rust 和 PyOxidizer
```plain
bash


复制编辑
curl https://sh.rustup.rs -sSf | sh
source $HOME/.cargo/env
cargo install pyoxidizer
```

---

### 2. 初始化项目
```plain
bash


复制编辑
pyoxidizer init myapp
cd myapp
```

默认生成目录结构如下：

```plain
markdown


复制编辑
myapp/
├── build.rs
├── pyoxidizer.bzl
├── default_app/
│   └── __main__.py
```

---

### 3. 编辑 `default_app/__main__.py`
```plain
python


复制编辑
def main():
    print("你好，PyOxidizer 打包成功！")

if __name__ == "__main__":
    main()
```

---

### 4. 编译项目
```plain
bash


复制编辑
pyoxidizer build
```

生成的二进制在：

```plain
bash


复制编辑
build/x86_64-unknown-linux-gnu/release/myapp
```

---

## ✅ 总结：什么时候选哪个？
| 工具 | 语言 | 编译方式 | 适合场景 |
| --- | --- | --- | --- |
| Nuitka | Python → C | 编译成 C ➜ 再用 gcc 编译 | 脚本量中等，快速打包 |
| PyOxidizer | Python → Rust | 完全静态二进制 | 想要极致兼容、完全独立部署 |


---

## **Nuitka + Docker（基于 CentOS 7）** 
### ✅ 项目结构
```plain
nuitka_static_build/
├── hello.py
├── Dockerfile
└── build.sh
```

---

### 1️⃣ `hello.py`
```python
def main():
    print("你好，这是用 Nuitka 静态打包的程序！")

if __name__ == "__main__":
    main()
```

---

### 2️⃣ `Dockerfile`
使用 CentOS 7 构建，保证最大兼容性：

```dockerfile
FROM centos:7

# 安装编译工具
RUN yum install -y gcc gcc-c++ python3 python3-pip wget epel-release && \
    yum install -y python3-devel

# 安装 Nuitka（用国内源加速）
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple nuitka

# 拷贝代码
WORKDIR /build
COPY hello.py .

# 编译为单文件可执行程序
RUN nuitka hello.py --onefile

CMD ["./hello.bin"]
```

---

### 3️⃣ `build.sh`（一键构建脚本）
```bash
#!/bin/bash
set -e

IMAGE_NAME=nuitka-centos7
APP_NAME=hello

docker build -t $IMAGE_NAME .

# 导出构建产物
docker run --rm -v $PWD:/out -w /build $IMAGE_NAME \
  bash -c "cp ${APP_NAME}.bin /out/${APP_NAME}_static_rhel7.bin"

echo "构建完成，文件保存为：${APP_NAME}_static_rhel7.bin"
```

---

### ✅ 构建并导出可执行文件：
```bash
chmod +x build.sh
./build.sh
```

运行成功后，你会得到一个 `hello_static_rhel7.bin`，它可以直接在 RHEL 7 / 8 / 9 上运行。

---

## **PyOxidizer 静态打包项目模板**
---

### ✅ 项目结构：`pyoxidizer_demo/`
```plain
pyoxidizer_demo/
├── pyoxidizer.bzl         # 构建脚本
├── build.rs               # 空文件（保留）
├── app/
│   └── __main__.py        # 你的主程序
├── Dockerfile             # 编译环境（CentOS 7）
└── build.sh               # 一键构建脚本
```

---

### 1️⃣ `app/__main__.py`
```python
def main():
    print("你好，这是 PyOxidizer 打包的独立可执行程序！")

if __name__ == "__main__":
    main()
```

---

### 2️⃣ `pyoxidizer.bzl`
```python
# 使用默认配置
def make_python_distribution():
    return default_python_distribution(python_version = "3.9")

def make_executable():
    dist = make_python_distribution()

    policy = dist.make_python_packaging_policy()
    policy.include_stdlib = True
    policy.include_externally_referenced_resources = True
    policy.bytecode_opt_level = 2
    policy.freeze_bytecode = True

    config = dist.to_python_config(policy)
    return dist.to_executable(
        name = "pyoxidizer_demo",
        config = config,
        source_dir = "app",
    )
```

---

### 3️⃣ `Dockerfile`（推荐 RHEL 兼容环境）
```dockerfile
FROM centos:7

# 安装依赖
RUN yum install -y gcc gcc-c++ make git curl python3 python3-pip epel-release rust cargo

# 安装 pyoxidizer
RUN cargo install pyoxidizer

# 构建入口
WORKDIR /build
COPY . .

CMD ["pyoxidizer", "build"]
```

---

### 4️⃣ `build.sh`
```bash
#!/bin/bash
set -e

IMAGE_NAME=pyoxidizer-centos7
BIN_NAME=pyoxidizer_demo

docker build -t $IMAGE_NAME .

# 提取可执行文件
docker run --rm -v $PWD:/out -w /build $IMAGE_NAME \
  bash -c "cp build/x86_64-unknown-linux-gnu/release/${BIN_NAME} /out/${BIN_NAME}_static_rhel7.bin"

echo "构建完成：${BIN_NAME}_static_rhel7.bin"
```

---

### ✅ 构建方式：
```bash
chmod +x build.sh
./build.sh
```

---

### 🧪 运行：
```bash
./pyoxidizer_demo_static_rhel7.bin
# 输出：
# 你好，这是 PyOxidizer 打包的独立可执行程序！
```

---

### 📌 说明：
+ 生成的可执行文件是一个真正的 **独立二进制文件**，包含解释器和所有模块，适合部署到任何 RHEL 兼容机器上。
+ 默认使用 Python 3.9，可修改 `pyoxidizer.bzl` 中的 `python_version` 来更换版本。

