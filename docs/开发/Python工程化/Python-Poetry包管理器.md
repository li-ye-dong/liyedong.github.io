## 安装和卸载
```python
pipx install poetry
pipx install poetry==1.2.0

```

`**pipx**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">还可以并行安装 Poetry 的各个版本，这样可以轻松测试替代版本或预发布版本。每个版本都被赋予一个唯一的、用户指定的后缀，它将用于创建唯一的二进制名称：</font>

```python
pipx install --suffix=@1.2.0 poetry==1.2.0
poetry@1.2.0 --version

pipx install --suffix=@preview --pip-args=--pre poetry
poetry@preview --version
```

```python
pipx upgrade poetry
```

```python
pipx uninstall poetry
```

## <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">为 Bash启用制表符补全</font>
### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">自动加载（推荐）</font>
```bash
poetry completions bash >> ~/.bash_completion
```

## 基础用法
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">为了介绍基本用法，我们将安装</font>`**pendulum**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">日期时间库。如果您尚未安装 Poetry，请参阅</font>[简介](https://python-poetry.org/docs/)<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">章节</font>

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">项目设置</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">首先，让我们创建我们的新项目，我们称之为</font>`**poetry-demo**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：</font>

```python
poetry new poetry-demo
```

这将创建`**poetry-demo**`包含以下内容的目录：

```plain
poetry-demo
├── pyproject.toml
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py
```

这里最重要的是这个`**pyproject.toml**`文件。它将协调你的项目及其依赖项。目前，它看起来像这样：

```python
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]
readme = "README.md"
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Poetry 假设您的包中包含一个与项目根目录中同名的包</font>`**tool.poetry.name**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">。如果不是，请填写</font>[<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">tool.poetry.packages</font>](https://python-poetry.org/docs/pyproject/#packages)<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">以指定您的包及其位置。</font>

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">类似地，传统的文件被、和 部分</font>`**MANIFEST.in**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">所取代。另外还由您的 隐式填充。有关项目格式的完整文档，请参阅文档的</font>[<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">pyproject 部分。</font>](https://python-poetry.org/docs/pyproject/)`**tool.poetry.readme**``**tool.poetry.include**``**tool.poetry.exclude**``**tool.poetry.exclude**``**.gitignore**`

### pyproject.toml详细配置
`pyproject.toml` 文件的 `tool.poetry` 部分是 Poetry 配置的核心，包含以下主要配置项：

1. **基本信息**：
    - `name`: 包名称，必填。
    - `version`: 包版本，必填。
    - `description`: 包描述。
    - `license`: 包的许可证，如 MIT、GPL 等。
    - `authors`: 作者列表，必填。
2. **资源链接**：
    - `homepage`: 项目主页。
    - `repository`: 代码库地址。
    - `documentation`: 文档地址。
3. **包定义**：
    - `packages`: 自定义包的包含路径和排除路径，适用于非标准项目结构。
    - `include` 和 `exclude`: 包含或排除指定文件/文件夹到最终的包中。
4. **依赖管理**：
    - `dependencies`: 核心依赖项，指定版本和依赖源。
    - `group`: 依赖项组管理，可用于开发、测试等不同环境的依赖。
    - `extras`: 可选依赖，用于指定额外的依赖，例如数据库驱动。
5. **脚本**：
    - `scripts`: 自定义命令行脚本，方便通过命令行调用包的功能。
6. **插件**：
    - `plugins`: 定义自定义插件，按需扩展功能。
7. **项目链接**：
    - `urls`: 自定义链接，如 Bug 追踪器等。
8. **构建系统**：
    - `build-system`: 指定构建系统，用于项目构建，通常配置 `poetry-core`。

### 配置示例
以下是一个示例 `pyproject.toml` 文件，包含了所有配置项，并添加了中文注释供参考：

```toml
[tool.poetry]
## 包名称（PEP 508 标准）
name = "my-package" 

## 包版本（PEP 440 标准）
version = "0.1.0"  

## 包描述
description = "这是一个简单的Python示例包"

## 包的许可证类型（SPDX 许可标识）
license = "MIT"  

## 包作者（姓名和邮箱，至少填写一个）
authors = ["Your Name <your.email@example.com>"]

## 包维护者信息（可选）
maintainers = ["Maintainer Name <maintainer.email@example.com>"]

## README 文件路径，可以是相对路径或数组形式
readme = "README.md"  

## 项目主页链接
homepage = "https://example.com"

## 项目代码库链接
repository = "https://github.com/your-username/my-package"

## 项目文档链接
documentation = "https://example.com/docs"

## 关键字标签，用于描述项目相关内容
keywords = ["example", "package", "poetry"]

## 分类器标签，用于描述项目性质（主要用于 PyPI）
classifiers = [
    "Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]

## 包定义，如果包结构非标准，可以自定义包路径
packages = [
    { include = "my_package", from = "lib" },
    { include = "extra_package/**/*.py" },
]

## 包的包含和排除设置，支持特定构建格式
include = [
    { path = "CHANGELOG.md", format = "sdist" },
    { path = "LICENSE.txt", format = ["sdist", "wheel"] }
]
exclude = ["my_package/excluded.py"]

[tool.poetry.dependencies]
## Python 版本要求
python = "^3.7"  #要求3.7及其更高
## python = ">=3.7,<3.14"
## 必要依赖项及版本
requests = "^2.25.1"

## 可选依赖项
psycopg2 = { version = "^2.9", optional = true }
mysqlclient = { version = "^1.3", optional = true }

[tool.poetry.extras]
## 可选依赖组（如数据库支持）
mysql = ["mysqlclient"]
pgsql = ["psycopg2"]

[tool.poetry.scripts]
## 定义脚本，通过命令行调用包功能
my_package_cli = "my_package.console:run"

[tool.poetry.urls]
## 自定义项目链接
"Bug Tracker" = "https://github.com/your-username/my-package/issues"

[build-system]
## 构建系统要求，使用 poetry-core 作为构建后端
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

## 配置项目下载源
[[tool.poetry.source]]
name = "tsinghua"
priority = "primary"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
[[tool.poetry.source]]
name = "aliyun"
url = "https://mirrors.aliyun.com/pypi/simple/"
priority = "supplemental"
```

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">初始化现有项目</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">无需创建新项目，Poetry 可用于“初始化”预填充的目录。要</font>`**pyproject.toml**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">在目录中以交互方式创建文件</font>`**pre-existing-project**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：</font>

![](../../images/1730614914524-9545ef18-3eb3-40a7-ae0e-c12bf84d0311.svg)

```bash
cd pre-existing-project
poetry init
```

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">打包操作模式</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Poetry 可以在两种不同的模式下运行。默认模式是</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">包模式</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">，如果你想将项目打包到 sdist 或 wheel 中，并将其发布到包索引中，这是正确的模式。在此模式下，打包所需的一些元数据（如</font>`**name**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">和</font>`**version**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">）是必需的。此外，运行时项目本身将以可编辑模式安装</font>`**poetry install**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">。</font>

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">如果你只想使用 Poetry 进行依赖管理而不是打包，那么可以使用</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">非打包模式</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：</font>

![](../../images/1730614941980-06e8babb-d5cf-41a8-a9cd-11d33cb134f8.svg)

```toml
[tool.poetry]
package-mode = false
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">在此模式下，元数据（例如</font>`**name**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">和 ）</font>`**version**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">是可选的。因此，无法构建分发版或将项目发布到包索引。此外，在运行 时</font>`**poetry install**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">，Poetry 不会尝试安装项目本身，而只会安装其依赖项（与 相同</font>`**poetry install --no-root**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">）。</font>

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">指定依赖项</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">如果您想向您的项目添加依赖项，您可以在</font>`**tool.poetry.dependencies**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">部分中指定它们。</font>

![](../../images/1730614998275-d78e5506-aa39-4baf-b676-a3352597be72.svg)

```toml
[tool.poetry.dependencies]
pendulum = "^2.1"
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">如您所见，它采用了</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">包名称</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">和</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">版本约束</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">的映射。</font>

`**tool.poetry.source**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Poetry 使用此信息在您在部分中注册的包“存储库”中或</font><font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">默认在</font>[<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">PyPI</font>](https://pypi.org/)<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">上搜索正确的文件集。</font>

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">另外，您可以使用命令，而不必</font>`**pyproject.toml**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">手动修改文件</font>`**add**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">。</font>

![](../../images/1730614998307-2b38d09d-627e-4e0b-972c-9e1362f1976e.svg)

```bash
$ poetry add pendulum
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">它会自动找到合适的版本约束</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">并安装</font>**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">包和子依赖项。</font>

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Poetry 支持丰富的</font>[<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">依赖规范</font>](https://python-poetry.org/docs/dependency-specification/)<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">语法，包括插入符号、波浪号、通配符、不等式和 </font>[<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">多重约束</font>](https://python-poetry.org/docs/dependency-specification/#multiple-constraints-dependencies)<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">要求。</font>

### 虚拟环境
使用外部虚拟环境venv

```bash
cd projectdir
python -m venv venv
./venv/Scripts/activate #linux则是 source ./venv/bin/activate
poetry init #初始化一个配置文件
poetry install #安装依赖
poetry build #打包成wheel包
poetry lock #更新依赖项
poetry add pyexecjs="^1.5.1" #添加指定版本依赖
poetry remove pyexecjs #删除一个已有包
./venv/Scripts/deactivate #退出虚拟环境linux则是 deactivate  #export已导出，无需指定路径
```

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">更新依赖项至最新版本</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">如上所述，该</font>`**poetry.lock**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">文件会阻止您自动获取依赖项的最新版本。要更新到最新版本，请使用该</font>`**update**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">命令。这将获取最新的匹配版本（根据您的</font>`**pyproject.toml**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">文件）并使用新版本更新锁定文件。（这相当于删除</font>`**poetry.lock**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">文件并</font>`**install**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">再次运行。）</font>

如果和 不同步，Poetry在执行安装命令时将显示**警告。**`**poetry.lock**``**pyproject.toml**`

## 高级用法
### 多组依赖管理
对于使用 Poetry 管理依赖关系时，要有效地区分和管理开发环境、测试环境以及生产环境的依赖项，可以借助依赖项组（dependency groups）以及可选依赖项（extras）来实现。下面通过示例展示如何配置这些不同环境的依赖项。

### 1. 项目结构配置
以下是项目 `pyproject.toml` 文件的一个示例，通过 `main` 组（生产环境）、`dev` 组（开发环境）和 `test` 组（测试环境）来分别管理不同的依赖项：

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "Example project with dependency groups"
authors = ["Your Name <youremail@example.com>"]

## 主依赖项（生产环境）
[tool.poetry.dependencies]
httpx = "^0.22.0"
pendulum = "^2.1.2"

## 开发环境依赖项组
[tool.poetry.group.dev.dependencies]
black = "^21.12b0"   ## 代码格式化工具
mypy = "^0.910"      ## 类型检查工具

## 测试环境依赖项组
[tool.poetry.group.test.dependencies]
pytest = "^6.2.5"    ## 测试框架
pytest-mock = "^3.6.1"  ## Mock工具，用于单元测试
```

在这个配置中，`httpx` 和 `pendulum` 属于主依赖项组，即生产环境会用到的库。在开发环境中，我们会用到 `black` 和 `mypy`，而测试环境需要 `pytest` 和 `pytest-mock`。

### 2. 安装不同的依赖项组
配置好 `pyproject.toml` 后，可以通过不同的 `poetry install` 命令来安装各个环境的依赖项：

#### 仅安装生产环境依赖项
```bash
poetry install --only main
```

#### 安装生产环境和开发环境的依赖项
```bash
poetry install --with dev
```

#### 安装生产环境和测试环境的依赖项
```bash
poetry install --with test
```

#### 安装所有依赖项（生产、开发、测试环境）
```bash
poetry install --with dev,test
```

### 3. 添加和删除依赖项
Poetry 支持使用 `--group` 选项直接向特定的依赖项组添加或删除依赖项：

#### 向测试环境添加新依赖项
```bash
poetry add requests-mock --group test
```

#### 从开发环境删除依赖项
```bash
poetry remove mypy --group dev
```

### 4. 同步依赖项
`poetry install --sync` 命令会确保当前环境的依赖项与 `poetry.lock` 文件中一致。此功能在管理多环境部署时特别有用，可以删除任何未被锁定的依赖项，保持环境一致。

例如：

```bash
## 仅同步生产环境依赖项
poetry install --only main --sync

## 同步生产和测试环境依赖项
poetry install --with test --sync
```

### 5. 使用可选依赖项（Extras）
对于在生产环境中可能不常用到的依赖项，可以将它们配置为可选依赖项。使用 `extras` 可以方便用户在安装包时选择性地安装特定功能：

```toml
## 可选依赖项定义
[tool.poetry.extras]
docs = ["mkdocs"]  ## 文档构建工具
```

使用可选依赖项的安装命令如下：

```bash
poetry install --extras "docs"
```

### 总结
通过上述配置和命令，Poetry 能够轻松管理开发、测试和生产环境的依赖项。

### 打包管理
使用 Poetry 进行库管理和发布可以简化 Python 库的创建、打包和发布流程。以下是使用 Poetry 进行库管理的流程总结、实例以及相关介绍：

### 1. 版本控制
Poetry 采用 [PEP 440](https://www.python.org/dev/peps/pep-0440/) 规范来进行版本管理。虽然不强制使用语义化版本，但 PEP 440 鼓励版本格式的规范化。例如：

+ `1.0.0` 表示主要版本发布
+ `1.0.0.post1` 表示修复或补丁版本
+ **注意**：`1.0.0-hotfix.1` 这样的格式不符合 PEP 440，需改用 `1.0.0.post1`。

### 2. 锁定依赖项
`poetry.lock` 文件可以记录库的依赖版本，有助于团队在相同依赖版本下进行测试。对于库项目，是否提交该文件视具体情况而定：

+ **提交 **`poetry.lock`** 文件**：确保团队测试版本一致。
+ **不提交**：将 `poetry.lock` 文件添加到 `.gitignore` 中，让库用户选择自己的依赖版本。

### 3. 打包库
在发布库之前，需先将其打包。使用 `poetry build` 命令来生成两种格式的包：

```bash
poetry build
```

生成的包格式包括：

+ `sdist`：源码包。
+ `wheel`：编译后的包。

### 4. 发布到 PyPI
Poetry 默认会将库发布到 [PyPI](https://pypi.org/)，并且发布到 PyPI 的包可以供 Python 社区的其他项目使用。

**步骤：**

1. **配置 PyPI 账户**：确保已注册并配置好 PyPI 的凭证。
2. **发布库**：
    - 直接发布：使用 `poetry publish`。
    - 构建并发布：使用 `poetry publish --build`。

例如：

```bash
poetry publish --build
```

一旦发布完成，该库将会自动在 PyPI 上可用，供任何用户下载使用。

### 5. 发布到私有仓库
如果希望库仅供团队内部使用，需将库发布到私有仓库。流程如下：

1. **添加私有仓库**：在 Poetry 配置中添加私有仓库地址。

```bash
poetry config repositories.my-repository https://example.com/simple/
```

2. **发布到私有仓库**：在 `publish` 命令中指定私有仓库。

```bash
poetry publish -r my-repository
```

### 6. 完整示例
#### 首先新建一个项目
```toml
poetry new poetry-demo
cd poetry-demo
python -m venv venv

```

#### 添加依赖
```toml
[tool.poetry]
name = "liyedong-poetry-demo"
version = "0.1.0"
description = ""
authors = ["liyedong <lyd1446034545@gmail.com>"]
readme = "README.md"
## 包定义，如果包结构非标准，可以自定义包路径
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.32.3"
drissionpage = "^4.1.0.7"
apscheduler = "^3.10.4"
pypiwin32 = "^223"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

#### 安装
```toml
.\venv\Scripts\activate
poetry install
```

#### 设置token
```toml
poetry config pypi-token.pypi pypi-AgEIcHlwaS5vcmcCJDBhZWJjZThmLTU1NGEtNGMzNy1iZjgzLWI2NDc0MTA5MDA3YwACKlszLCI4MTA0ZjE4Ny01YzQ3LTQ2NGMtYmY2Yi1hM2I1N2NiY2NmZDYiXQAA
BiBGU2UDZxJyE8x5dvPmLbJ-jHTtcEKCKeRLG6lzT3A1CQ
```

[pypi官网](https://pypi.org/)

#### 打包和发布命令
```bash
## 打包库
poetry build

## 发布到 PyPI
poetry publish --build

## 发布到私有仓库（需要预先配置私有仓库）
poetry publish -r my-repository --build
```

[https://pypi.org/manage/projects/](https://pypi.org/manage/projects/)

访问网站查看上传的项目

### 总结
通过以上步骤可以轻松管理和发布 Python 库，利用 Poetry 的功能，开发者能够：

+ 使用 PEP 440 标准化版本号
+ 根据项目需求选择是否锁定依赖
+ 支持源码和 Wheel 格式打包
+ 选择发布到 PyPI 或私有仓库

### 命令及其参数
以下是 Poetry 的常用命令及其参数的详细总结和解释。

### 1. 项目初始化
+ `poetry new <project_name>`  
用于创建一个新的 Poetry 项目。
    - `--src`: 创建源代码目录为 `src/`，便于组织代码。
    - `--name <name>`: 设置包名称，与项目名称不同的情况下可使用。
+ `poetry init`  
交互式地初始化当前目录下的 Poetry 项目，生成 `pyproject.toml` 文件。参数：
    - `--name <name>`: 指定项目名称。
    - `--description <description>`: 添加项目描述。
    - `--author <author>`: 设置作者信息。
    - `--license <license>`: 指定项目许可证类型。
    - `--dependency <package>`: 添加初始依赖项。
    - `--dev-dependency <package>`: 添加初始开发依赖项。

### 2. 依赖管理
+ `poetry add <package_name>`  
添加依赖到项目中并写入 `pyproject.toml`。
    - `--group <group>`: 指定依赖组（如 `dev`），用于非生产环境的依赖。
    - `--optional`: 将依赖标记为可选，通常与 `extras` 配合使用。
    - `--source <repository>`: 从特定仓库安装依赖。
    - `--lock`: 添加依赖并更新 `poetry.lock` 文件。
+ `poetry remove <package_name>`  
从项目中移除依赖。
    - `--group <group>`: 从特定依赖组中移除依赖项。
+ `poetry update`  
更新所有依赖至最新版本，并更新 `poetry.lock` 文件。
    - `--dry-run`: 模拟更新，不实际更改文件。
    - `--lock`: 仅重新生成锁文件，不进行实际安装。
    - `--group <group>`: 仅更新特定组的依赖。

### 3. 安装依赖
+ `poetry install`  
安装项目的所有依赖，并创建或使用已存在的 `poetry.lock` 文件。
    - `--no-dev`: 仅安装非开发依赖项，适合生产环境。
    - `--with <group>`: 安装指定依赖组的依赖项。
    - `--without <group>`: 排除指定依赖组。
    - `--only <group>`: 仅安装特定依赖组。
    - `--sync`: 同步锁文件和安装的依赖项，删除多余的包。

### 4. 虚拟环境管理
+ `poetry shell`  
激活 Poetry 创建的虚拟环境。可以直接使用所有安装的依赖。
    - `--path <path>`: 指定虚拟环境的路径。
+ `poetry env use <python_path>`  
指定项目所使用的 Python 解释器。
    - `<python_path>`: 指定 Python 解释器的路径。
+ `poetry env remove <python_path|python_version>`  
移除与项目关联的 Python 虚拟环境。
+ `poetry env info`  
显示项目的虚拟环境信息。
    - `--path`: 仅返回虚拟环境的路径。
    - `--format <format>`: 指定输出格式，例如 `json`。

### 5. 构建与发布
+ `poetry build`  
将项目打包成 `.tar.gz` (sdist) 和 `.whl` (wheel) 格式。
    - `--format <format>`: 选择打包格式 (`sdist` 或 `wheel`)。
+ `poetry publish`  
将项目发布到 PyPI 或指定仓库。
    - `--build`: 在发布之前构建项目。
    - `-r, --repository <repository>`: 指定发布到的仓库，默认是 PyPI。
    - `--username <username>`: 发布时使用的用户名。
    - `--password <password>`: 发布时使用的密码。
    - `--dry-run`: 仅模拟发布过程，不实际执行发布。

### 6. 其他常用命令
+ `poetry lock`  
生成或更新 `poetry.lock` 文件，锁定项目的依赖版本。
+ `poetry check`  
检查项目配置和依赖是否有效。
+ `poetry run <command>`  
在虚拟环境中运行指定的命令。例如：`poetry run python script.py`。
    - `<command>`: 要运行的命令，可以是任何已安装的包的命令行工具。
+ `poetry cache clear --all`  
清除 Poetry 缓存，释放空间或解决缓存问题。
    - `--all`: 删除所有缓存

### 配置
### 配置 Poetry
Poetry 可以通过 `config` 命令进行配置，您可以在首次运行命令时自动创建的 `config.toml` 文件中进行配置。该文件通常位于以下目录之一：

+ **macOS**：`~/Library/Application Support/pypoetry`
+ **Windows**：`%APPDATA%\pypoetry`
+ **Unix**：遵循 XDG 规范，默认位置为 `~/.config/pypoetry`

### 本地配置
Poetry 允许通过 `--local` 选项设置特定于项目的配置。例如：

```bash
poetry config virtualenvs.create false --local
```

Poetry 的本地配置存储在 `poetry.toml` 文件中，该文件与 `pyproject.toml` 一起存在。请注意将此文件加入版本控制，因为它可能包含用户特定或敏感信息。

### 列出当前配置
要列出当前配置，可以使用 `--list` 选项：

```bash
poetry config --list
```

这将显示类似于以下内容的输出：

```bash
(venv) PS D:\Users\Administrator\Desktop\python学习demo\poetry-demo> poetry config --list
cache-dir = "C:\\Users\\Administrator\\AppData\\Local\\pypoetry\\Cache"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
keyring.enabled = true
solver.lazy-wheel = true
virtualenvs.create = false
virtualenvs.in-project = null
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}\\virtualenvs"  ## C:\Users\Administrator\AppData\Local\pypoetry\Cache\virtualenvs
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
warnings.export = true

```

### 设置单个配置
如果要查看特定设置的值，可以将其名称提供给 `config` 命令：

```bash
poetry config virtualenvs.path
```

有关支持的设置的完整列表，请参阅可用设置。

### 添加或更新配置设置
要更改或添加新的配置设置，可以在设置名称后传递一个值：

```bash
poetry config virtualenvs.path /path/to/cache/directory/virtualenvs
```

### 删除特定设置
如果要删除以前设置的配置，可以使用 `--unset` 选项：

```bash
poetry config virtualenvs.path --unset
```

这样，设置将恢复为默认值。

### 使用环境变量
在某些情况下，特别是在将 Poetry 与 CI 工具一起使用时，使用环境变量进行配置可能更方便。任何设置都可以通过使用环境变量进行设置。环境变量必须以 `POETRY_` 为前缀，并由设置的名称组成，用下划线替换点和破折号。例如：

```bash
export POETRY_VIRTUALENVS_PATH=/path/to/virtualenvs/directory
```

这同样适用于秘密设置，例如凭据：

```bash
export POETRY_HTTP_BASIC_MY_REPOSITORY_PASSWORD=secret
```

### 默认目录
Poetry 使用以下默认目录：

**配置目录**

+ **Linux**：`$XDG_CONFIG_HOME/pypoetry` 或 `~/.config/pypoetry`
+ **Windows**：`%APPDATA%\pypoetry`
+ **macOS**：`~/Library/Application Support/pypoetry`

您可以通过设置 `POETRY_CONFIG_DIR` 环境变量来覆盖配置目录。

**数据目录**

+ **Linux**：`$XDG_CONFIG_HOME/pypoetry` 或 `~/.config/pypoetry`
+ **Windows**：`%APPDATA%\pypoetry`
+ **macOS**：`~/Library/Application Support/pypoetry`

您可以通过设置 `POETRY_DATA_DIR` 或 `POETRY_HOME` 环境变量来覆盖数据目录。如果设置了 `POETRY_HOME`，它将优先于其他设置。

**缓存目录**

+ **Linux**：`$XDG_CONFIG_HOME/pypoetry` 或 `~/.config/pypoetry`
+ **Windows**：`%APPDATA%\pypoetry`
+ **macOS**：`~/Library/Application Support/pypoetry`

您可以通过设置 `POETRY_CACHE_DIR` 环境变量来覆盖缓存目录。

### 可用设置
以下是一些可用的配置设置及其说明：

+ **cache-dir**  
类型：`string`  
环境变量：`POETRY_CACHE_DIR`  
Poetry 使用的缓存目录路径。
+ **virtualenvs.create**  
类型：`boolean`  
默认值：`false`  
环境变量：`POETRY_VIRTUALENVS_CREATE`  
创建一个新的虚拟环境（如果还不存在）。
+ **virtualenvs.in-project**  
类型：`boolean`  
默认值：`false`  
环境变量：`POETRY_VIRTUALENVS_IN_PROJECT`  
在项目根目录中创建虚拟环境。
+ **virtualenvs.path**  
类型：`string`  
默认值：`{cache-dir}/virtualenvs`  
环境变量：`POETRY_VIRTUALENVS_PATH`  
创建虚拟环境的目录。

更多设置的完整列表及其详细信息，请查阅官方文档。

通过以上配置和命令，您可以根据需要自定义 Poetry 的行为，以更好地满足您的开发需求。

### 仓库配置
```toml
[tool.poetry]
name = "liyedong-poetry-demo"
version = "0.1.0"
description = ""
authors = ["liyedong <lyd1446034545@gmail.com>"]
readme = "README.md"
## 包定义，如果包结构非标准，可以自定义包路径
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.32.3"
drissionpage = "^4.1.0.7"
apscheduler = "^3.10.4"
pypiwin32 = "^223"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
## 配置项目下载源
[[tool.poetry.source]]
name = "tsinghua"
priority = "primary"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
[[tool.poetry.source]]
name = "aliyun"
url = "https://mirrors.aliyun.com/pypi/simple/"
priority = "supplemental"
```

### 多个解释器切换
<font style="color:rgb(47, 41, 151);background-color:rgb(245, 245, 252);">如果你使用</font>[<font style="color:rgb(47, 41, 151);background-color:rgb(245, 245, 252);">pyenv</font>](https://github.com/pyenv/pyenv)<font style="color:rgb(47, 41, 151);background-color:rgb(245, 245, 252);">这样的工具来管理不同的Python版本，你可以将实验性的</font>`<font style="background-color:rgb(245, 245, 252);">virtualenvs.prefer-active-python</font>`<font style="color:rgb(47, 41, 151);background-color:rgb(245, 245, 252);">选项设置为</font>`<font style="background-color:rgb(245, 245, 252);">true</font>`<font style="color:rgb(47, 41, 151);background-color:rgb(245, 245, 252);">。Poetry将尝试找到当前的</font>`<font style="background-color:rgb(245, 245, 252);">python</font>`<font style="color:rgb(47, 41, 151);background-color:rgb(245, 245, 252);">shell。</font>

<font style="color:rgb(47, 41, 151);background-color:rgb(245, 245, 252);">例如，如果您的项目需要比您的系统可用的更新的Python，则标准工作流程将是：</font>

```bash
pyenv install 3.9.8
pyenv local 3.9.8  ## Activate Python 3.9 for the current project
poetry install
```

### 切换
```toml
poetry env use /full/path/to/python
poetry env use python3.7
poetry env use 3.7
poetry env use system


```

### 查看环境
```powershell

>poetry env info

Virtualenv
Python:         3.7.1
Implementation: CPython
Path:           /path/to/poetry/cache/virtualenvs/test-O3eWbxRl-py3.7
Valid:          True

Base
Platform: darwin
OS:       posix
Python:   /path/to/main/python
#如果你只想知道虚拟环境的路径，你可以将--path选项传递给env info：
>poetry env info --path
#如果你只想知道python可执行文件的路径（这对于在全局环境中运行mypy而不将其安装到虚拟环境中很有用），你可以将--executable选项传递给env info：
poetry env info --executable
```

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">列出与项目关联的环境</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">您还可以使用</font>`<font style="background-color:rgb(251, 251, 255);">env list</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">命令列出与当前项目关联的所有虚拟环境：</font>

![](../../images/1730620148916-d5a99344-2935-4c4e-9bc5-57d5e2d49c4a.svg)

```bash
poetry env list
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">将输出如下内容：</font>

![](../../images/1730620148920-a34f5562-2880-4575-8db5-8d869d3a8fe3.svg)

```plain
test-O3eWbxRl-py3.6
test-O3eWbxRl-py3.7 (Activated)
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">您可以传递选项</font>`<font style="background-color:rgb(251, 251, 255);">--full-path</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">以显示环境的完整路径：</font>

![](../../images/1730620149066-38ce8ec1-d24e-4e3a-8ca9-da18a76fbaac.svg)

```bash
poetry env list --full-path
```

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">删除环境</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">最后，您可以使用</font>`<font style="background-color:rgb(251, 251, 255);">env remove</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">删除现有的虚拟环境：</font>

![](../../images/1730620149190-71828c9c-82b7-40ba-a4b7-8f9d498b4f96.svg)

```bash
poetry env remove /full/path/to/python
poetry env remove python3.7
poetry env remove 3.7
poetry env remove test-O3eWbxRl-py3.7
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">您可以一次删除多个环境。</font>

![](../../images/1730620149209-b81d8fc1-334a-4f88-9de5-1dd4befb6e3e.svg)

```bash
poetry env remove python3.6 python3.7 python3.8
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">使用</font>`<font style="background-color:rgb(251, 251, 255);">--all</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">选项一次性删除所有虚拟环境。</font>

![](../../images/1730620149369-afe0b50e-c4f7-42ed-b5fd-f24ab5385c8f.svg)

```bash
poetry env remove --all
```

<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">如果您删除当前激活的虚拟环境，它将自动停用。</font>

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">依赖关系规范</font>
[https://python-poetry.org/docs/dependency-specification/](https://python-poetry.org/docs/dependency-specification/)

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">版本限制</font>
1. **插入符号要求 (**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">^</font>`**)**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：允许对指定版本进行 SemVer 兼容更新。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">^1.2.3</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 允许更新到 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">>=1.2.3 <2.0.0</font>`
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">^0.2.3</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 允许更新到 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">>=0.2.3 <0.3.0</font>`
2. **波浪符号要求 (**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">~</font>`**)**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：指定最低版本，允许补丁级别更新。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">~1.2.3</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 允许更新到 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">>=1.2.3 <1.3.0</font>`
3. **通配符要求 (**`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">*</font>`**)**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：允许依赖项的最新版本。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">*</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 允许更新到 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">>=0.0.0</font>`
4. **不平等要求**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：手动指定版本范围或确切版本。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">>= 1.2.0</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">, </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">< 2</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">, </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">!= 1.2.3</font>`
5. **具体要求**<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">：指定包的确切版本。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">1.2.3</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 或 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">==1.2.3</font>`

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">使用@运算符</font>
+ <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">可以在添加依赖项时使用 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">@</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 运算符来指定版本或其他说明符。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">poetry add django@^4.0.0</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 变为 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Django = "^4.0.0"</font>`

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Git 依赖项</font>
+ <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">使用 Git 存储库中的库时，需指定存储库位置和可选分支或提交。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">requests = { git = "https://github.com/requests/requests.git" }</font>`

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Path 和 URL 依赖项</font>
+ <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">使用 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">path</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 属性依赖本地目录或文件，或使用 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">url</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 属性依赖远程档案。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">my-package = { path = "../my-package/", develop = false }</font>`

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">Python 受限依赖项</font>
+ <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">可以为特定 Python 版本指定依赖项。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">tomli = { version = "^2.0.1", python = "<3.11" }</font>`

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">环境标记</font>
+ <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">使用 </font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">markers</font>`<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);"> 属性为依赖项设置复杂的安装条件。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">pathlib2 = { version = "^2.2", markers = "python_version <= '3.4'" }</font>`

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">多个约束依赖关系</font>
+ <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">可以根据目标 Python 版本定义不同的版本范围。</font>
    - <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">示例：</font>
        * `<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">foo = [{version = "<=1.9", python = ">=3.6,<3.8"}, {version = "^2.0", python = ">=3.8"}]</font>`

#### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">扩展依赖规范语法</font>
+ <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">复杂的依赖规范可以使用“标准表”语法以便于阅读。</font>

### <font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">总结</font>
<font style="color:rgb(9, 61, 141);background-color:rgb(251, 251, 255);">通过使用不同的符号和要求，可以灵活地管理项目依赖关系，确保在安装或更新依赖时符合版本兼容性和功能需求。</font>

