<font style="color:rgb(31, 35, 40);">PDM 旨在成为下一代 Python 软件包管理工具。它最初是为个人兴趣而诞生的。如果你觉得 </font>`<font style="color:rgb(31, 35, 40);">pipenv</font>`<font style="color:rgb(31, 35, 40);"> 或者 </font>`<font style="color:rgb(31, 35, 40);">poetry</font>`<font style="color:rgb(31, 35, 40);"> 用着非常好，并不想引入一个新的包管理器，那么继续使用它们吧；但如果你发现有些东西这些 工具不支持，那么你很可能可以在 </font>`<font style="color:rgb(31, 35, 40);">pdm</font>`<font style="color:rgb(31, 35, 40);"> 中找到。</font>

## <font style="color:rgb(31, 35, 40);">主要特性</font>
+ <font style="color:rgb(31, 35, 40);">一个简单且相对快速的依赖解析器，特别是对于大的二进制包发布。</font>
+ <font style="color:rgb(31, 35, 40);">兼容</font><font style="color:rgb(31, 35, 40);"> </font>[PEP 517](https://www.python.org/dev/peps/pep-0517)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">的构建后端，用于构建发布包(源码格式与 wheel 格式)</font>
+ <font style="color:rgb(31, 35, 40);">灵活且强大的插件系统</font>
+ [PEP 621](https://www.python.org/dev/peps/pep-0621)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">元数据格式</font>
+ <font style="color:rgb(31, 35, 40);">功能强大的用户脚本</font>
+ <font style="color:rgb(31, 35, 40);">支持从</font><font style="color:rgb(31, 35, 40);"> </font>[indygreg's python-build-standalone](https://github.com/indygreg/python-build-standalone)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">安装 Python。</font>
+ <font style="color:rgb(31, 35, 40);">像</font><font style="color:rgb(31, 35, 40);"> </font>[pnpm](https://pnpm.io/motivation#saving-disk-space-and-boosting-installation-speed)<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">一样的中心化安装缓存，节省磁盘空间</font>

## <font style="color:rgb(31, 35, 40);">与其他包管理器的比较</font>
### [Pipenv](https://pipenv.pypa.io/)
<font style="color:rgb(31, 35, 40);">Pipenv 是一个依赖管理器，它结合了</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">pip</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">和</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">venv</font>`<font style="color:rgb(31, 35, 40);">，正如其名称所暗示的。它可以从一种自定义格式文件</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">Pipfile.lock</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">或</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">Pipfile</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">中安装软件包。 然而，Pipenv 并不处理任何与构建、打包和发布相关的工作。所以它只适用于开发不可安装的应用程序（例如 Django 网站）。 如果你是一个库的开发者，无论如何你都需要</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">setuptools</font>`<font style="color:rgb(31, 35, 40);">。</font>

### [Poetry](https://python-poetry.org/)
<font style="color:rgb(31, 35, 40);">Poetry 以类似于 Pipenv 的方式管理环境和依赖，它也可以从你的代码构建</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">.whl</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">文件，并且可以将轮子和源码发行版上传到 PyPI。 它有一个漂亮的用户界面，用户可以通过贡献插件来定制它。Poetry 使用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">pyproject.toml</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">标准。</font>

### [Hatch](https://hatch.pypa.io/)
<font style="color:rgb(31, 35, 40);">Hatch 也可以管理环境（它允许每个项目有多个环境，但不允许把它们放在项目目录中），并且可以管理包（但不支持 lockfile）。Hatch 也可以用来打包一个项目（用符合 PEP 621 标准的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">pyproject.toml</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">文件）并上传到 PyPI。</font>

### <font style="color:rgb(31, 35, 40);">本项目</font>
<font style="color:rgb(31, 35, 40);">PDM 也可以像 Pipenv 那样在项目或集中的位置管理 venvs。它从一个标准化的</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">pyproject.toml</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">文件中读取项目元数据，并支持 lockfile。用户可以在插件中添加更多的功能，并将其作为一个发行版上传，以供分享。</font>

<font style="color:rgb(31, 35, 40);">此外，与 Poetry 和 Hatch 不同，PDM 并没有被和一个特定的构建后端绑定，你可以选择任何你喜欢的构建后端。</font>

## <font style="color:rgb(31, 35, 40);">安装</font>
<font style="color:rgb(31, 35, 40);">PDM 需要 Python 3.9 或更高版本。</font>

### <font style="color:rgb(31, 35, 40);">通过安装脚本</font>
<font style="color:rgb(31, 35, 40);">像 pip 一样，PDM 也提供了一键安装脚本，用来将 PDM 安装在一个隔离的环境中。</font>

**<font style="color:rgb(31, 35, 40);">Linux/Mac 安装命令</font>**

<font style="color:rgb(31, 35, 40);">curl -sSL https://pdm-project.org/install-pdm.py | python3 -</font>

**<font style="color:rgb(31, 35, 40);">Windows 安装命令</font>**

<font style="color:rgb(31, 35, 40);">powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"</font>

<font style="color:rgb(31, 35, 40);">为安全起见，你应该检查</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">install-pdm.py</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">文件的正确性。 校验和文件下载地址：</font>[install-pdm.py.sha256](https://pdm-project.org/install-pdm.py.sha256)

<font style="color:rgb(31, 35, 40);">默认情况下，此脚本会将 PDM 安装在 Python 的用户目录下，具体位置取决于当前系统：</font>

+ <font style="color:rgb(31, 35, 40);">Unix 上是</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">$HOME/.local/bin</font>`
+ <font style="color:rgb(31, 35, 40);">MacOS 上是</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">$HOME/Library/Python/<version>/bin</font>`
+ <font style="color:rgb(31, 35, 40);">Windows 上是</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">%APPDATA%\Python\Scripts</font>`

<font style="color:rgb(31, 35, 40);">你还可以通过命令行的选项来改变安装脚本的行为：</font>

```plain
usage: install-pdm.py [-h] [-v VERSION] [--prerelease] [--remove] [-p PATH] [-d DEP]

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION | envvar: PDM_VERSION
                        Specify the version to be installed, or HEAD to install from the main branch
  --prerelease | envvar: PDM_PRERELEASE    Allow prereleases to be installed
  --remove | envvar: PDM_REMOVE            Remove the PDM installation
  -p PATH, --path PATH | envvar: PDM_HOME  Specify the location to install PDM
  -d DEP, --dep DEP | envvar: PDM_DEPS     Specify additional dependencies, can be given multiple times
```

<font style="color:rgb(31, 35, 40);">你既可以通过直接增加选项，也可以通过设置对应的环境变量来达到这一效果。</font>

### <font style="color:rgb(31, 35, 40);">其他安装方法</font>
<font style="color:rgb(31, 35, 40);">如果你使用的是 macOS 并且安装了</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">homebrew</font>`<font style="color:rgb(31, 35, 40);">：</font>

<font style="color:rgb(31, 35, 40);">brew install pdm</font>

<font style="color:rgb(31, 35, 40);">如果你在 Windows 上使用</font><font style="color:rgb(31, 35, 40);"> </font>[Scoop](https://scoop.sh/)<font style="color:rgb(31, 35, 40);">, 运行以下命令安装：</font>

```plain
scoop bucket add frostming https://github.com/frostming/scoop-frostming.git
scoop install pdm
```

<font style="color:rgb(31, 35, 40);">否则，强烈推荐把</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">pdm</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">安装在一个隔离环境中， 用</font><font style="color:rgb(31, 35, 40);"> </font>`<font style="color:rgb(31, 35, 40);">pipx</font>`<font style="color:rgb(31, 35, 40);"> </font><font style="color:rgb(31, 35, 40);">是最好的。</font>

<font style="color:rgb(31, 35, 40);">pipx install pdm</font>

<font style="color:rgb(31, 35, 40);">或者你可以将它安装在用户目录下:</font>

<font style="color:rgb(31, 35, 40);">pip install --user pdm</font>

[asdf-vm](https://asdf-vm.com/)

```plain
asdf plugin add pdm
asdf install pdm latest
```

## <font style="color:rgb(31, 35, 40);">快速上手</font>
**<font style="color:rgb(31, 35, 40);">初始化一个新的 PDM 项目</font>**

```python
pdm init
```

<font style="color:rgb(31, 35, 40);">按照指引回答提示的问题，一个 PDM 项目和对应的</font>`<font style="color:rgb(31, 35, 40);">pyproject.toml</font>`<font style="color:rgb(31, 35, 40);">文件就创建好了。</font>

**<font style="color:rgb(31, 35, 40);">添加依赖</font>**

```python
pdm add requests flask
```

<font style="color:rgb(31, 35, 40);">你可以在同一条命令中添加多个依赖。稍等片刻完成之后，你可以查看</font>`<font style="color:rgb(31, 35, 40);">pdm.lock</font>`<font style="color:rgb(31, 35, 40);">文件看看有哪些依赖以及对应版本。</font>

<font style="color:rgb(31, 35, 40);"></font>

## 官方文档
[https://pdm-project.org/en/latest/](https://pdm-project.org/en/latest/)

[https://pdm-project.org/zh-cn/latest/](https://pdm-project.org/zh-cn/latest/)

# 使用 uv
<font style="color:rgba(0, 0, 0, 0.87);">PDM 对 </font>[uv](https://github.com/astral-sh/uv)<font style="color:rgba(0, 0, 0, 0.87);"> 作为解析器和安装器有实验性支持。要启用它：</font>

```toml
pdm config use_uv true
```

<font style="color:rgba(0, 0, 0, 0.87);">PDM 将自动检测系统上的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`uv`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">二进制文件。你需要先安装</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`uv`<font style="color:rgba(0, 0, 0, 0.87);">。更多详细信息请参阅</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[uv 的安装指南](https://docs.astral.sh/uv/getting-started/installation/)<font style="color:rgba(0, 0, 0, 0.87);">。</font>

## <font style="color:rgba(0, 0, 0, 0.87);">Reuse the Python installations of uv</font>[#](https://pdm-project.org/zh-cn/latest/usage/uv/#reuse-the-python-installations-of-uv)
<font style="color:rgba(0, 0, 0, 0.87);">uv 也支持安装 Python 解释器。为避免开销，你可以通过以下方式配置 PDM 以复用 uv 的 Python 安装：</font>

```toml
pdm config python.install_root $(uv python dir)
```

## <font style="color:rgba(0, 0, 0, 0.87);">局限性</font>
<font style="color:rgba(0, 0, 0, 0.87);">尽管 uv 带来了显著的性能提升，但需要注意 uv 的以下局限性：</font>

+ <font style="color:rgba(0, 0, 0, 0.87);">缓存文件存储在 uv 自己的缓存目录中，你必须使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`uv`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">命令来管理它们。</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">不支持 PEP 582 本地包布局。</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">uv 不支持</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`inherit_metadata`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">锁定策略。 在写入锁定文件时，这将被忽略。</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">不支持除</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`all`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">和</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`reuse`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">之外的更新策略。</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">可编辑需求必须是本地路径。像</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`-e git+<git_url>`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">这样的需求不被支持。</font>
+ `[tool.pdm.resolution]`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">下的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`excludes`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">设置不被支持。</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">uv 解析器不支持跨平台锁定目标，即，你无法针对与当前平台不同的平台进行锁定操作。</font>

## 配置项目
### <font style="color:rgba(0, 0, 0, 0.87);">依赖管理</font>
<font style="color:rgba(0, 0, 0, 0.87);">依赖管理对于开发者能够工作并执行以下操作是必需的：</font>

+ `lock`<font style="color:rgba(0, 0, 0, 0.87);">：从</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的依赖计算一个锁定文件。</font>
+ `sync`<font style="color:rgba(0, 0, 0, 0.87);">：同步（添加/删除/更新）PEP582 包，从锁定文件中安装当前项目为可编辑状态。</font>
+ `add`<font style="color:rgba(0, 0, 0, 0.87);">：添加一个依赖</font>
+ `remove`<font style="color:rgba(0, 0, 0, 0.87);">：移除一个依赖</font>

<font style="color:rgba(0, 0, 0, 0.87);">所有这些步骤都直接可用，具体命令如下：</font>

+ [pdm lock](https://pdm-project.org/zh-cn/latest/reference/cli/#lock)<font style="color:rgba(0, 0, 0, 0.87);">: 执行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`lock`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">任务</font>
+ [pdm sync](https://pdm-project.org/zh-cn/latest/reference/cli/#sync)<font style="color:rgba(0, 0, 0, 0.87);">: 执行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`sync`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">任务</font>
+ [pdm install](https://pdm-project.org/zh-cn/latest/reference/cli/#install)<font style="color:rgba(0, 0, 0, 0.87);">: 执行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`sync`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">任务，如果需要，则在此之前执行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`lock`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">任务</font>
+ [pdm add](https://pdm-project.org/zh-cn/latest/reference/cli/#add)<font style="color:rgba(0, 0, 0, 0.87);">: 添加一个依赖要求，重新锁定，然后同步</font>
+ [pdm remove](https://pdm-project.org/zh-cn/latest/reference/cli/#remove)<font style="color:rgba(0, 0, 0, 0.87);">: 删除一个依赖要求，重新锁定，然后同步</font>
+ [pdm update](https://pdm-project.org/zh-cn/latest/reference/cli/#update)<font style="color:rgba(0, 0, 0, 0.87);">: 从它们的最新版本重新锁定依赖项，然后同步</font>

<font style="color:rgba(0, 0, 0, 0.87);">它们触发以下钩子：</font>

+ [pre_install](https://pdm-project.org/zh-cn/latest/reference/api/#pdm.signals.pre_install)
+ [post_install](https://pdm-project.org/zh-cn/latest/reference/api/#pdm.signals.post_install)
+ [pre_lock](https://pdm-project.org/zh-cn/latest/reference/api/#pdm.signals.pre_lock)
+ [post_lock](https://pdm-project.org/zh-cn/latest/reference/api/#pdm.signals.post_lock)

### 配置文件范例
```toml
[project]
name = "my-package"
version = "0.1.0"
description = "这是一个简单的Python示例包"
readme = "README.md"
license = { text = "MIT" }

authors = [
    { name = "Your Name", email = "your.email@example.com" }
]

# 注意：maintainers 字段不是标准 PEP 621 字段，可注释
# maintainers = [
#     { name = "Maintainer Name", email = "maintainer.email@example.com" }
# ]

requires-python = ">=3.7"

keywords = ["example", "package", "pdm"]

classifiers = [
    "Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]

homepage = "https://example.com"
repository = "https://github.com/your-username/my-package"
documentation = "https://example.com/docs"

dependencies = [
    "requests>=2.25.1"
]

[project.optional-dependencies]
mysql = ["mysqlclient>=1.3"]
pgsql = ["psycopg2>=2.9"]

[project.scripts]
my_package_cli = "my_package.console:run"

[build-system]
requires = ["pdm-backend"]
build-backend = "pdm.backend"

# pdm 专属配置
[tool.pdm]
use_venv = true

[tool.pdm.dev-dependencies]
test = ["pytest"]
lint = ["black", "ruff"]

# 自定义脚本（可通过 pdm run 使用）
[tool.pdm.scripts]
test = "pytest"
lint = "black ."

# 下载源配置
[[tool.pdm.source]]
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
type = "index"
verify_ssl = true
default = true

[[tool.pdm.source]]
name = "aliyun"
url = "https://mirrors.aliyun.com/pypi/simple/"
type = "index"
verify_ssl = true

```

## Dockerfile集成
<font style="color:rgba(0, 0, 0, 0.87);">可以在多阶段 Dockerfile 中使用 PDM，先将项目和依赖项安装到 </font>`__pypackages__`<font style="color:rgba(0, 0, 0, 0.87);"> 中， 然后将此文件夹复制到最终阶段，并将其添加到 </font>`PYTHONPATH`<font style="color:rgba(0, 0, 0, 0.87);"> 中。</font>

```dockerfile
ARG PYTHON_BASE=3.10-slim
# 构建阶段
FROM python:$PYTHON_BASE AS builder

# 安装 PDM
RUN pip install -U pdm
# 禁用更新检查
ENV PDM_CHECK_UPDATE=false
# 复制文件
COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src

# 安装依赖项和项目到本地包目录
WORKDIR /project
RUN pdm install --check --prod --no-editable

# 运行阶段
FROM python:$PYTHON_BASE

# 从构建阶段获取包
COPY --from=builder /project/.venv/ /project/.venv
ENV PATH="/project/.venv/bin:$PATH"
# 设置命令/入口点，根据需要进行调整
COPY src /project/src
CMD ["python", "src/__main__.py"]
```

## <font style="color:rgba(0, 0, 0, 0.87);">使用 PDM 管理多仓库</font>
<font style="color:rgba(0, 0, 0, 0.87);">使用 PDM，您可以在单个项目中拥有多个子包，每个子包都有自己的 pyproject.toml 文件。您可以创建一个 pdm.lock 文件来锁定所有依赖项。子包可以相互作为它们的依赖项。要实现这一点，请按照以下步骤操作：</font>

`project/pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);">:</font>

```toml
[dependency-groups]
dev = [
    "-e file:///${PROJECT_ROOT}/packages/foo-core",
    "-e file:///${PROJECT_ROOT}/packages/foo-cli",
    "-e file:///${PROJECT_ROOT}/packages/foo-app",
]
```

`packages/foo-cli/pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);">:</font>

```toml
[project]
dependencies = ["foo-core"]
```

`packages/foo-app/pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);">:</font>

```toml
[project]
dependencies = ["foo-core"]
```

<font style="color:rgba(0, 0, 0, 0.87);">现在，在项目根目录中运行 </font>`pdm install`<font style="color:rgba(0, 0, 0, 0.87);">，您将获得一个带有所有依赖项锁定的 </font>`pdm.lock`<font style="color:rgba(0, 0, 0, 0.87);">。所有子包将以可编辑模式安装。</font>

<font style="color:rgba(0, 0, 0, 0.87);">查看 </font>[🚀 示例存储库](https://github.com/pdm-project/pdm-example-monorepo)<font style="color:rgba(0, 0, 0, 0.87);"> 获取更多详细信息。</font>

## 构建和发布
<font style="color:rgba(0, 0, 0, 0.87);">如果您正在开发库，则在向项目添加依赖项并完成编码后，就可以构建和发布包了。它就像一个命令一样简单：</font>

```toml
pdm publish
```

<font style="color:rgba(0, 0, 0, 0.87);">这将自动构建一个轮子和一个源分发（sdist），并将它们上传到 PyPI 索引。</font>

<font style="color:rgba(0, 0, 0, 0.87);">PyPI 需要 API 令牌才能发布包，可以使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`__token__`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">作为用户名，使用 API 令牌作为密码。</font>

<font style="color:rgba(0, 0, 0, 0.87);">要指定 PyPI 以外的其他存储库，请使用选项 </font>`--repository`<font style="color:rgba(0, 0, 0, 0.87);"> ，参数可以是上传 URL，也可以是存储在配置文件中的存储库的名称。</font>

```toml
pdm publish --repository testpypi
pdm publish --repository https://test.pypi.org/legacy/
```

### <font style="color:rgba(0, 0, 0, 0.87);">使用受信任的发布者发布</font>
<font style="color:rgba(0, 0, 0, 0.87);">可以为 PyPI 配置受信任的发布者，这样就不需要在发布工作流中公开 PyPI 令牌。 为此，请按照</font>[指南](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)<font style="color:rgba(0, 0, 0, 0.87);">添加发布者并编写 GitHub Actions 工作流，如下所示：</font>

```toml
on:
  release:
    types: [published]


jobs:
  pypi-publish:
    name: upload release to PyPI
    runs-on: ubuntu-latest
    permissions:
      # 这个权限是为了私有仓库。
      contents: read
      # 重要提示：这个权限对于可信发布是必需的。
      id-token: write
    steps:
      - uses: actions/checkout@v4

      - uses: pdm-project/setup-pdm@v4

      - name: Publish package distributions to PyPI
        run: pdm publish
```

<font style="color:rgba(0, 0, 0, 0.87);"></font>

### <font style="color:rgba(0, 0, 0, 0.87);">单独生成和发布</font>
<font style="color:rgba(0, 0, 0, 0.87);">您还可以通过两个步骤构建包并上传它，以便您在上传之前检查构建的项目。</font>

```toml
pdm build
```

<font style="color:rgba(0, 0, 0, 0.87);">有许多选项可以控制生成过程，具体取决于使用的后端。有关更多详细信息，请参阅</font>[构建配置](https://pdm-project.org/zh-cn/latest/reference/build/)<font style="color:rgba(0, 0, 0, 0.87);">部分。</font>

<font style="color:rgba(0, 0, 0, 0.87);">工件将在 PyPI 处创建 </font>`dist/`<font style="color:rgba(0, 0, 0, 0.87);"> 并能够上传到 PyPI。</font>

```toml
pdm publish --no-build
```

