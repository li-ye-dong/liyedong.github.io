[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

<font style="color:rgb(37, 41, 51);">UV 是一个由 Astral 公司用 Rust 开发的高性能 Python 包管理工具，旨在提供比传统 pip 更快的包安装和依赖管理体验。本文将介绍 UV 的基础用法和最佳实践。</font>

## <font style="color:rgb(37, 41, 51);">1. 核心特性</font>
1. **<font style="color:rgb(37, 41, 51);">速度与功能</font>**
    - <font style="color:rgb(37, 41, 51);">uv比pip快10-100倍，支持安装和管理Python版本。</font>
    - <font style="color:rgb(37, 41, 51);">提供项目管理功能，包括依赖管理、锁文件、工作空间等。</font>
    - <font style="color:rgb(37, 41, 51);">支持运行单文件脚本，并管理其依赖环境。</font>
2. **<font style="color:rgb(37, 41, 51);">安装与更新</font>**
    - <font style="color:rgb(37, 41, 51);">通过官方提供的安装脚本或PyPI安装uv。</font>
    - <font style="color:rgb(37, 41, 51);">安装后，uv可以自更新到最新版本。</font>
3. **<font style="color:rgb(37, 41, 51);">项目管理</font>**
    - <font style="color:rgb(37, 41, 51);">uv可以初始化项目，添加依赖，运行检查工具。</font>
    - <font style="color:rgb(37, 41, 51);">支持构建和发布项目，即使项目不是用uv管理的。</font>
4. **<font style="color:rgb(37, 41, 51);">工具管理</font>**
    - <font style="color:rgb(37, 41, 51);">通过</font>`<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uvx</font>`<font style="color:rgb(37, 41, 51);">命令运行工具，支持临时环境。</font>
    - <font style="color:rgb(37, 41, 51);">可以安装工具并提供可执行文件。</font>
5. **<font style="color:rgb(37, 41, 51);">Python管理</font>**
    - <font style="color:rgb(37, 41, 51);">安装多个Python版本，并在不同版本间快速切换。</font>
    - <font style="color:rgb(37, 41, 51);">下载所需的Python版本，创建虚拟环境，并指定使用特定版本。</font>
6. **<font style="color:rgb(37, 41, 51);">脚本支持</font>**
    - <font style="color:rgb(37, 41, 51);">管理单文件脚本的依赖和环境。</font>
    - <font style="color:rgb(37, 41, 51);">添加内联元数据以声明依赖，运行脚本时自动安装。</font>
7. **<font style="color:rgb(37, 41, 51);">兼容性与迁移</font>**
    - <font style="color:rgb(37, 41, 51);">提供与pip兼容的接口，支持无缝迁移。</font>
    - <font style="color:rgb(37, 41, 51);">编译通用需求文件，创建虚拟环境，同步锁定需求。</font>

## <font style="color:rgb(37, 41, 51);">2. 基础命令</font>
### <font style="color:rgb(37, 41, 51);">2.1 环境管理</font>
```bash
# 创建虚拟环境
uv venv

# 指定 Python 版本
uv venv --python 3.11

# 激活环境（Windows）
.venv\Scripts\activate
```

### <font style="color:rgb(37, 41, 51);">2.2 包管理</font>
```bash
# 添加依赖（会更新 pyproject.toml）
uv add flask
uv add --dev pytest

# 安装依赖（不更新配置文件）
uv pip install flask

# 从项目配置安装
uv pip install .
```

### <font style="color:rgb(37, 41, 51);">2.3 依赖同步</font>
```bash
# 同步项目依赖
uv sync

# 更新依赖
uv sync --upgrade

# 更新特定包
uv sync --upgrade-package flask
```

## <font style="color:rgb(37, 41, 51);">3. 项目最佳实践</font>
### <font style="color:rgb(37, 41, 51);">3.1 新项目初始化</font>
```bash
# 1. 创建项目目录
mkdir my-project && cd my-project

# 2. 创建虚拟环境
uv venv --python 3.11

# 3. 激活环境
.venv\Scripts\activate

# 4. 添加依赖
uv add flask fastapi
uv add --dev pytest black

# 5. 同步依赖
uv sync
```

### <font style="color:rgb(37, 41, 51);">3.2 配置文件示例</font>
```toml
# pyproject.toml
[project]
name = "fastapi_websockets"
version = "0.1.0"
description = "Project description"
requires-python = ">=3.11"
dependencies = [
    "anyio>=4.9.0",
    "fastapi>=0.115.12",
    "httpx>=0.28.1",
    "pytest>=8.3.5",
    "trio>=0.30.0",
    "uvicorn>=0.34.2",
    "websockets>=15.0.1",
]

[project.optional-dependencies]
dev = [

]
# 下载源配置 uv sync
[[tool.uv.index]]
#[[index]]这个也可以
# 默认源
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = true
#使用uv pip时配置
[tool.uv.pip]
index-url = "https://mirrors.aliyun.com/pypi/simple/"
```

#### <font style="color:rgb(37, 41, 51);">3.3 团队协作流程</font>
1. **<font style="color:rgb(37, 41, 51);">克隆项目后</font>**<font style="color:rgb(37, 41, 51);">：</font>

```bash
uv venv
.venv\Scripts\activate
uv sync
```

1. **<font style="color:rgb(37, 41, 51);">添加新依赖时</font>**<font style="color:rgb(37, 41, 51);">：</font>

```bash
uv add new-package
uv sync  # 更新锁文件
git add pyproject.toml uv.lock
```

1. **<font style="color:rgb(37, 41, 51);">CI/CD 环境</font>**<font style="color:rgb(37, 41, 51);">：</font>

```bash
uv sync --locked  # 确保可重现的构建
```

## <font style="color:rgb(37, 41, 51);">4. UV vs pip 命令对比</font>
| <font style="color:rgb(37, 41, 51);">功能</font> | <font style="color:rgb(37, 41, 51);">UV 命令</font> | <font style="color:rgb(37, 41, 51);">pip 命令</font> |
| --- | --- | --- |
| <font style="color:rgb(37, 41, 51);">安装包</font> | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uv add flask</font>` | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">pip install flask</font>` |
| <font style="color:rgb(37, 41, 51);">安装开发依赖</font> | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uv add --dev pytest</font>` | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">pip install pytest</font>` |
| <font style="color:rgb(37, 41, 51);">从文件安装</font> | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uv sync</font>` | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">pip install -r requirements.txt</font>` |
| <font style="color:rgb(37, 41, 51);">更新包</font> | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uv sync --upgrade</font>` | `<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">pip install --upgrade</font>` |


## <font style="color:rgb(37, 41, 51);">5. 版本管理</font>
### <font style="color:rgb(37, 41, 51);">5.1 通过配置文件</font>
```toml
# pyproject.toml
[project]
requires-python = ">=3.9,<3.11"
```

### <font style="color:rgb(37, 41, 51);">5.2 通过命令行</font>
```bash
# 创建特定版本环境
uv venv --python 3.9

# 使用 .python-version 文件
echo "3.9.7" > .python-version
```

## <font style="color:rgb(37, 41, 51);">6. 最佳实践总结</font>
1. **<font style="color:rgb(37, 41, 51);">依赖管理</font>**<font style="color:rgb(37, 41, 51);">：</font>
    - <font style="color:rgb(37, 41, 51);">使用</font><font style="color:rgb(37, 41, 51);"> </font>`<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uv add</font>`<font style="color:rgb(37, 41, 51);"> </font><font style="color:rgb(37, 41, 51);">添加新依赖</font>
    - <font style="color:rgb(37, 41, 51);">使用</font><font style="color:rgb(37, 41, 51);"> </font>`<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uv sync</font>`<font style="color:rgb(37, 41, 51);"> </font><font style="color:rgb(37, 41, 51);">同步项目依赖</font>
    - <font style="color:rgb(37, 41, 51);">总是提交</font><font style="color:rgb(37, 41, 51);"> </font>`<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">uv.lock</font>`<font style="color:rgb(37, 41, 51);"> </font><font style="color:rgb(37, 41, 51);">到版本控制</font>
2. **<font style="color:rgb(37, 41, 51);">环境管理</font>**<font style="color:rgb(37, 41, 51);">：</font>
    - <font style="color:rgb(37, 41, 51);">每个项目使用独立虚拟环境</font>
    - <font style="color:rgb(37, 41, 51);">明确指定 Python 版本要求</font>
    - <font style="color:rgb(37, 41, 51);">使用</font><font style="color:rgb(37, 41, 51);"> </font>`<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">--dev</font>`<font style="color:rgb(37, 41, 51);"> </font><font style="color:rgb(37, 41, 51);">分离开发依赖</font>
3. **<font style="color:rgb(37, 41, 51);">团队协作</font>**<font style="color:rgb(37, 41, 51);">：</font>
    - <font style="color:rgb(37, 41, 51);">统一使用</font><font style="color:rgb(37, 41, 51);"> </font>`<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">pyproject.toml</font>`
    - <font style="color:rgb(37, 41, 51);">保持锁文件更新</font>
    - <font style="color:rgb(37, 41, 51);">CI/CD 中使用</font><font style="color:rgb(37, 41, 51);"> </font>`<font style="color:rgb(255, 80, 44);background-color:rgb(255, 245, 245);">--locked</font>`<font style="color:rgb(37, 41, 51);"> </font><font style="color:rgb(37, 41, 51);">标志</font>

## <font style="color:rgb(37, 41, 51);">结论</font>
<font style="color:rgb(37, 41, 51);">UV 通过现代化的设计和高性能实现，显著提升了 Python 项目的依赖管理体验。它不仅保持了与 pip 的兼容性，还带来了更快的安装速度和更好的依赖解析能力。对于新项目，强烈推荐使用 UV 作为默认的包管理工具。</font>

## <font style="color:rgb(37, 41, 51);">配置文件范例</font>
```toml
[project]
# 包名称（PEP 508 标准）
name = "my-package"

# 包版本（PEP 440 标准）
version = "0.1.0"

# 描述信息
description = "这是一个简单的Python示例包"

# 项目主页链接
homepage = "https://example.com"

# 项目文档链接
documentation = "https://example.com/docs"

# 项目代码仓库
repository = "https://github.com/your-username/my-package"

# README 文件
readme = "README.md"

# 许可证类型
license = { text = "MIT" }

# 作者信息
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]

# 维护者信息（PEP 621 标准中未明确支持，但可以扩展）
# maintainers = [
#     { name = "Maintainer Name", email = "maintainer.email@example.com" }
# ]

# Python 版本要求
requires-python = ">=3.7"

# 项目关键字
keywords = ["example", "package", "uv"]

# 分类器（与 PyPI 配合）
classifiers = [
    "Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]

# 项目依赖
dependencies = [
    "requests>=2.25.1",
    # 可选依赖（可以通过 optional-dependencies 实现）
    # "psycopg2>=2.9",
    # "mysqlclient>=1.3"
]

# 可选依赖分组（用于 pip install .[mysql]）
[project.optional-dependencies]
mysql = ["mysqlclient>=1.3"]
pgsql = ["psycopg2>=2.9"]

# 命令行入口
[project.scripts]
my_package_cli = "my_package.console:run"

# 包包含排除（暂无法指定构建格式，仅支持构建时包含/排除）
# 可用 MANIFEST.in 实现更细粒度控制

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

# 下载源配置（uv 使用 pip 格式支持 index-url）
[tool.uv.pip]
# 默认源
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"
# 备用源（uv 目前不支持多个 source 权重配置，使用 alias 替代）
extra-index-url = ["https://mirrors.aliyun.com/pypi/simple/"]

```

