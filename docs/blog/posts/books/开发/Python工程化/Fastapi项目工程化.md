## <font style="color:rgba(0, 0, 0, 0.87);">1. 开发环境搭建</font>
### <font style="color:rgba(0, 0, 0, 0.87);">1.1 Python 环境</font>
<font style="color:rgba(0, 0, 0, 0.87);">鉴于官方已经停止对 Python 2 的支持</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<sup><font style="color:rgba(0, 0, 0, 0.87);">1</font></sup>](https://pyloong.github.io/pythonic-project-guidelines/practices/web/#fn:1)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，我们不推荐再使用 Python 2 进行开发。根据当前 Python 版本使用情况，推荐使用 Python 3.7+ 。</font>

<font style="color:rgba(0, 0, 0, 0.87);">具体的版本的 Python 环境可以在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">官网</font>](https://www.python.org/downloads/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">下载。为了使用便利性，可以选择 Anaconda</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<sup><font style="color:rgba(0, 0, 0, 0.87);">2</font></sup>](https://pyloong.github.io/pythonic-project-guidelines/practices/web/#fn:2)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1.2 开发工具</font>
<font style="color:rgba(0, 0, 0, 0.87);">推荐使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Pycharm</font>](https://www.jetbrains.com/pycharm/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">作为主要开发工具，可以选择社区版本免费使用。</font>

[<font style="color:rgba(0, 0, 0, 0.87);">Visual Studio Code</font>](https://code.visualstudio.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是微软开发的一款免费轻量文本编辑器，通过安装插件可以自定义成一款功能强大的 IDE 。在对 Python 的支持上，已经有了较为完善的插件体系，此方案也可以作为备用。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1.3 虚拟环境工具</font>
<font style="color:rgba(0, 0, 0, 0.87);">推荐使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">poetry</font>](https://python-poetry.org/)<font style="color:rgba(0, 0, 0, 0.87);">。poetry 相比使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`requirements.txt`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">管理依赖列表，更加强大。它支持同时管理开发生产环境依赖，自动查找虚拟环境，生成依赖锁定文件等其他特性。</font>

<font style="color:rgba(0, 0, 0, 0.87);">在安装好 Python 环境后，应该在全局环境中安装 poetry 。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1.4 Git 使用</font>
<font style="color:rgba(0, 0, 0, 0.87);">推荐使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Git</font>](https://git-scm.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">对项目进行版本管理。所以需要提前安装 Git ，并熟悉常用 Git 的概念和常用 Git 命令。</font>

## <font style="color:rgba(0, 0, 0, 0.87);">2. 项目初始化</font>
### <font style="color:rgba(0, 0, 0, 0.87);">2.1 初始化项目结构</font>
<font style="color:rgba(0, 0, 0, 0.87);">项目结构采用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录结构，详见</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pypa/sampleproject</font>](https://github.com/pypa/sampleproject)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。</font>

<font style="color:rgba(0, 0, 0, 0.87);">创建项目目录结构：</font>

```python
.
├── README.md
├── src
│   └── example_blog
│       └── __init__.py
└── tests
└── __init__.py
```

<font style="color:rgba(0, 0, 0, 0.87);">初始化项目虚拟环境：</font>

```python
poetry init
```

<font style="color:rgba(0, 0, 0, 0.87);">根据交互式提示，进行相应内容选取填写，安装完成后，项目目录会自动生成</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">2.2 初始化项目基本信息</font>
<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件， 配置项目描述信息：</font>

```python
[tool.poetry]
name = "example_blog"
version = "0.1.0"
description = "This is example blog system."
authors = ["huagang517 <huagang517@126.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### <font style="color:rgba(0, 0, 0, 0.87);">2.3 增加项目自述文件</font>
<font style="color:rgba(0, 0, 0, 0.87);">编写</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`README.md`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件</font>

```python
# 一个简单博客系统示例.

此项目是一个简单的博客系统，提供一些用户管理和博客文章管理。目的是演示如何做一个更加 Pythonic 的项目。

如果您有任何意见和建议，欢迎开启 ISSUE 发起讨论。期待与您打造更加完美的 Python 示例。

## 协作开发

- Fork 仓库
- 编写代码，测试，提交
- 发起 PR
- 审核通过后合并，协作完成
```

### <font style="color:rgba(0, 0, 0, 0.87);">2.4 增加</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`.gitignore`
```python
# Created by .ignore support plugin (hsz.mobi)
### Python template
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    pip-wheel-metadata/
    share/python-wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    MANIFEST

    # PyInstaller
    #  Usually these files are written by a python script from a template
    #  before PyInstaller builds the exe, so as to inject date/other infos into it.
    *.manifest
    *.spec

    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt

    # Unit test / coverage reports
    htmlcov/
    .tox/
    .nox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *.cover
    *.py,cover
    .hypothesis/
    .pytest_cache/
    cover/

    # Translations
    *.mo
    *.pot

    # Django stuff:
    *.log
    local_settings.py
    db.sqlite3
    db.sqlite3-journal

    # Flask stuff:
    instance/
    .webassets-cache

    # Scrapy stuff:
    .scrapy

    # Sphinx documentation
    docs/_build/

    # PyBuilder
    .pybuilder/
    target/

    # Jupyter Notebook
    .ipynb_checkpoints

    # IPython
    profile_default/
    ipython_config.py

    # pyenv
    #   For a library or package, you might want to ignore these files since the code is
    #   intended to run in multiple environments; otherwise, check them in:
    # .python-version

    # pipenv
    #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
    #   However, in case of collaboration, if having platform-specific dependencies or dependencies
    #   having no cross-platform support, pipenv may install dependencies that don't work, or not
    #   install all needed dependencies.
    #Pipfile.lock

    # PEP 582; used by e.g. github.com/David-OConnor/pyflow
    __pypackages__/

    # Celery stuff
    celerybeat-schedule
    celerybeat.pid

    # SageMath parsed files
    *.sage.py

    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/

    # Spyder project settings
    .spyderproject
    .spyproject

    # Rope project settings
    .ropeproject

    # mkdocs documentation
    /site

    # mypy
    .mypy_cache/
    .dmypy.json
    dmypy.json

    # Pyre type checker
    .pyre/

    # pytype static type analyzer
    .pytype/

    # Cython debug symbols
    cython_debug/

    ### Windows template
    # Windows thumbnail cache files
    Thumbs.db
    Thumbs.db:encryptable
    ehthumbs.db
    ehthumbs_vista.db

    # Dump file
    *.stackdump

    # Folder config file
    [Dd]esktop.ini

    # Recycle Bin used on file shares
    $RECYCLE.BIN/

    # Windows Installer files
    *.cab
    *.msi
    *.msix
    *.msm
    *.msp

    # Windows shortcuts
    *.lnk

    ### Linux template
    *~

    # temporary files which can be created if a process still has a handle open of a deleted file
    .fuse_hidden*

    # KDE directory preferences
    .directory

    # Linux trash folder which might appear on any partition or disk
    .Trash-*

    # .nfs files are created when an open file is removed but is still being accessed
    .nfs*

    ### macOS template
    # General
    .DS_Store
    .AppleDouble
    .LSOverride

    # Icon must end with two \r
    Icon

    # Thumbnails
    ._*

    # Files that might appear in the root of a volume
    .DocumentRevisions-V100
    .fseventsd
    .Spotlight-V100
    .TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

.vscode
.idea
```

### <font style="color:rgba(0, 0, 0, 0.87);">2.5 安装开发包</font>
```python
poetry install
```

### <font style="color:rgba(0, 0, 0, 0.87);">2.6 初始 Git 提交</font>
```python
git init
git config user.name example
git config user.email example@example.com
git add .
    git commit -m "feat: First commit!"
```

## <font style="color:rgba(0, 0, 0, 0.87);">3. 项目功能开发</font>
### <font style="color:rgba(0, 0, 0, 0.87);">3.1 创建命令行入口</font>
<font style="color:rgba(0, 0, 0, 0.87);">命令行入口是启动项目的主入口，常见的做法是使用一个</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`__main__`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">函数，调用启动代码，然后使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`python`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">命令启动该文件。但对于多级命令参数的情况就比较麻烦，推荐使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">click</font>](https://click.palletsprojects.com/en/7.x/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">工具编写入口逻辑。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add click
```

<font style="color:rgba(0, 0, 0, 0.87);">查看</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，将增加安装依赖：</font>

```python
[tool.poetry.dependencies]
click = "^8.1.3"
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件：</font>

```python
@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-V', '--version', is_flag=True, help='Show version and exit.')
def main(ctx, version):
    if version:
        click.echo(__version__)
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
```

<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，将命令行入口注册到项目描述文件中：</font>

```python
[tool.poetry.scripts]
example_blog = "example_blog.cmdline:main"
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
    git commit -m "feat: Add cmdline."
```

### <font style="color:rgba(0, 0, 0, 0.87);">3.2 引入项目配置系统</font>
<font style="color:rgba(0, 0, 0, 0.87);">项目的配置系统是一个项目的核心驱动，使用配置系统便于管理散落在各处的配置参数，也方便在启动前通过调整配置，改变系统行为。</font>

[<font style="color:rgba(0, 0, 0, 0.87);">Dynaconf</font>](https://www.dynaconf.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个高度灵活的配置管理工具，支持多环境分层，多种配置导入等有点。在项目开发中，推荐使用如下实践。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add dynaconf
```

<font style="color:rgba(0, 0, 0, 0.87);">查看</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，将增加安装依赖：</font>

```python
[tool.poetry.dependencies]
click = "^8.1.3"
dynaconf = "^3.1.11"
```

<font style="color:rgba(0, 0, 0, 0.87);">建立配置包，和配置文件：</font>

```python
mkdir src/example_blog/config
touch src/example_blog/config/__init__.py
touch src/example_blog/config/settings.yml
```

<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/config/__init__.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">， 初始化全局配置对象：</font>

```python
import os
import sys
from pathlib import Path

from dynaconf import Dynaconf

_BASE_DIR = Path(__file__).parent.parent

settings_files = [
    Path(__file__).parent / 'settings.yml',
]  # 指定绝对路径加载默认配置

settings = Dynaconf(
    envvar_prefix="EXAMPLE_BLOG",  # 环境变量前缀。设置`EXAMPLE_BLOG_FOO='bar'`，使用`settings.FOO`
    settings_files=settings_files,
    environments=False,  # 启用多层次日志，支持 dev, pro
    load_dotenv=True,  # 加载 .env
    env_switcher="EXAMPLE_BLOG_ENV",  # 用于切换模式的环境变量名称 EXAMPLE_BLOG_ENV=production
    lowercase_read=False,  # 禁用小写访问， settings.name 是不允许的
    includes=[os.path.join(sys.prefix, 'etc', 'example_blog', 'settings.yml')],  # 自定义配置覆盖默认配置
    base_dir=_BASE_DIR,  # 编码传入配置
)
```

<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/config/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，初始化配置：</font>

```python
LOG_LEVEL: INFO
```

<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/config/settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，增加本地开发配置：</font>

```python
LOG_LEVEL: DEBUG
```

<font style="color:rgba(0, 0, 0, 0.87);">根据</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Dynaconf</font>](https://www.dynaconf.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">规则，</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的配置为本地配置，且优先级比</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">低，所以本地配置会在后面加载，覆盖之前的配置。</font>

<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`.gitignore`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，将所有本地配置排除版本控制之外。</font>

```python
**/settings.local.yml
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码:</font>

```python
git add .
    git commit -m "feat: Add config."
```

### <font style="color:rgba(0, 0, 0, 0.87);">3.3 引入日志</font>
<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/log.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，初始化 log ：</font>

```python
from logging.config import dictConfig

from example_blog.config import settings


def init_log():
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'sample': {'format': '%(asctime)s %(levelname)s %(message)s'},
            'verbose': {'format': '%(asctime)s %(levelname)s %(name)s %(process)d %(thread)d %(message)s'},
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            },
        },
        'handlers': {
            "console": {
                "formatter": 'verbose',
                'level': 'DEBUG',
                "class": "logging.StreamHandler",
            },
        },
        'loggers': {
            '': {'level': settings.LOG_LEVEL, 'handlers': ['console']},
        },
    }

    dictConfig(log_config)
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
    git commit -m "feat: Add log"
```

### <font style="color:rgba(0, 0, 0, 0.87);">3.4 数据访问</font>
<font style="color:rgba(0, 0, 0, 0.87);">数据层是应用的最底层，和数据存储打交道。使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">sqlalchemy</font>](https://www.sqlalchemy.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">作底层数据模型建模和数据访问操作。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add sqlalchemy mysqlclient
```

<font style="color:rgba(0, 0, 0, 0.87);">查看</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，将增加安装依赖：</font>

```python
[tool.poetry.dependencies]
click = "^8.1.3"
dynaconf = "^3.1.11"
sqlalchemy = "^1.4.44"
mysqlclient = "^2.1.1"
```

<font style="color:rgba(0, 0, 0, 0.87);">编写</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/config/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，增加数据库配置信息：</font>

```python
# ######################################################################################################
# # https://docs.sqlalchemy.org/en/13/core/engines.html
DATABASE:
DRIVER: mysql
NAME: example_blog
HOST: 127.0.0.1
PORT: 3306
USERNAME: root
PASSWORD: root
QUERY:
charset: utf8mb4
```

**<font style="color:rgba(0, 0, 0, 0.87);">警告</font>**

`settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">为系统默认配置，会被 git 追踪管理，不要填写真正的数据库连接信息。真实配置信息可以写在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件中，会覆盖默认配置。</font>

<font style="color:rgba(0, 0, 0, 0.87);">新建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/db.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">sqlalchemy</font>](https://www.sqlalchemy.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">访问对象：</font>

```python
"""Database connections"""

from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from example_blog.config import settings

url = URL(
    drivername=settings.DATABASE.DRIVER,
    username=settings.DATABASE.get('USERNAME', None),
    password=settings.DATABASE.get('PASSWORD', None),
    host=settings.DATABASE.get('HOST', None),
    port=settings.DATABASE.get('PORT', None),
    database=settings.DATABASE.get('NAME', None),
    query=settings.DATABASE.get('QUERY', None),
)

engine: Engine = create_engine(url, echo=True)

SessionFactory = sessionmaker(bind=engine, autocommit=False, autoflush=True)

ScopedSession = scoped_session(SessionFactory)
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/models.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建数据模型：</font>

```python
"""Models"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class CustomBase:
    """https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html"""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_collate': 'utf8mb4_general_ci'
    }

    id = Column(Integer, primary_key=True, autoincrement=True)


BaseModel = declarative_base(cls=CustomBase)


class Article(BaseModel):
    """Article table"""
    title = Column(String(500))
    body = Column(Text(), nullable=True)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
```

<font style="color:rgba(0, 0, 0, 0.87);">为了在应用中更方便的使用数据模型对象，引入</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pydantic</font>](https://pydantic-docs.helpmanual.io/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">来定义一些对象模型的基本信息。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add pydantic
```

<font style="color:rgba(0, 0, 0, 0.87);">查看</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，将增加安装依赖：</font>

```python
[tool.poetry.dependencies]
click = "^8.1.3"
dynaconf = "^3.1.11"
sqlalchemy = "^1.4.44"
mysqlclient = "^2.1.1"
pydantic = "^1.10.2"
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/schemas.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建对象模型：</font>

```python
from datetime import datetime
from typing import Optional, TypeVar

from pydantic import BaseModel, constr

from example_blog.models import BaseModel as DBModel

ModelType = TypeVar('ModelType', bound=DBModel)
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)


class InDBMixin(BaseModel):
    id: int

    class Config:
        orm_mode = True


class BaseArticle(BaseModel):
    title: constr(max_length=500)
    body: Optional[str] = None


class ArticleSchema(BaseArticle, InDBMixin):
    create_time: datetime
    update_time: datetime


class CreateArticleSchema(BaseArticle):
    pass


class UpdateArticleSchema(BaseArticle):
    title: Optional[constr(max_length=500)] = None
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/dao.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建数据访问层：</font>

```python
from typing import Generic, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from example_blog.models import Article
from example_blog.schemas import CreateSchema, ModelType, UpdateSchema, CreateArticleSchema, UpdateArticleSchema


class BaseDAO(Generic[ModelType, CreateSchema, UpdateSchema]):
    model: ModelType

    def get(self, session: Session, offset=0, limit=10) -> List[ModelType]:
        result = session.query(self.model).offset(offset).limit(limit).all()
        return result

    def get_by_id(self, session: Session, pk: int, ) -> ModelType:
        return session.query(self.model).get(pk)

    def create(self, session: Session, obj_in: CreateSchema) -> ModelType:
        """Create"""
        obj = self.model(**jsonable_encoder(obj_in))
        session.add(obj)
        session.commit()
        return obj

    def patch(self, session: Session, pk: int, obj_in: UpdateSchema) -> ModelType:
        """Patch"""
        obj = self.get_by_id(session, pk)
        update_data = obj_in.dict(exclude_unset=True)
        for key, val in update_data.items():
            setattr(obj, key, val)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def delete(self, session: Session, pk: int) -> None:
        """Delete"""
        obj = self.get_by_id(session, pk)
        session.delete(obj)
        session.commit()

    def count(self, session: Session):
        return session.query(self.model).count()


class ArticleDAO(BaseDAO[Article, CreateArticleSchema, UpdateArticleSchema]):
    model = Article
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "feat: Add models and DAO"
```

### <font style="color:rgba(0, 0, 0, 0.87);">3.5 服务层</font>
<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/services.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建服务：</font>

```python
"""Service"""
from typing import Generic, List

from sqlalchemy.orm import Session

from example_blog.dao import ArticleDAO, BaseDAO
from example_blog.models import Article
from example_blog.schemas import CreateSchema, ModelType, UpdateSchema


class BaseService(Generic[ModelType, CreateSchema, UpdateSchema]):
    dao: BaseDAO

    def get(self, session: Session, offset=0, limit=10) -> List[ModelType]:
        """"""
        return self.dao.get(session, offset=offset, limit=limit)

    def total(self, session: Session) -> int:
        return self.dao.count(session)

    def get_by_id(self, session: Session, pk: int) -> ModelType:
        """Get by id"""
        return self.dao.get_by_id(session, pk)

    def create(self, session: Session, obj_in: CreateSchema) -> ModelType:
        """Create a object"""
        return self.dao.create(session, obj_in)

    def patch(self, session: Session, pk: int, obj_in: UpdateSchema) -> ModelType:
        """Update"""
        return self.dao.patch(session, pk, obj_in)

    def delete(self, session: Session, pk: int) -> None:
        """Delete a object"""
        return self.dao.delete(session, pk)


class ArticleService(BaseService[Article, CreateSchema, UpdateSchema]):
    dao = ArticleDAO()
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "feat: Add services."
```

### <font style="color:rgba(0, 0, 0, 0.87);">3.6 引入 Fastapi</font>
[<font style="color:rgba(0, 0, 0, 0.87);">Fastapi</font>](https://fastapi.tiangolo.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个轻量的 Web 框架，现在引入，使其作为 API 层</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add fastapi uvicorn
```

<font style="color:rgba(0, 0, 0, 0.87);">查看</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，增加安装依赖：</font>

```python
[tool.poetry.dependencies]
click = "^8.1.3"
dynaconf = "^3.1.11"
sqlalchemy = "^1.4.44"
mysqlclient = "^2.1.1"
pydantic = "^1.10.2"
fastapi = "^0.88.0"
uvicorn = "^0.20.0"
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/examp.e_blog/views.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建视图：</font>

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from example_blog.dependencies import CommonQueryParams, get_db
from example_blog.schemas import (ArticleSchema, CreateArticleSchema,
                                  UpdateArticleSchema)
from example_blog.services import ArticleService

router = APIRouter()

_service = ArticleService()


@router.get('/articles')
def get(
        session: Session = Depends(get_db),
        commons: CommonQueryParams = Depends()
):
    return _service.get(session, offset=commons.offset, limit=commons.limit)


@router.get('/articles/{pk}')
def get_by_id(
        pk: int,
        session: Session = Depends(get_db)
):
    return _service.get_by_id(session, pk)


@router.post('/articles', response_model=ArticleSchema)
def create(
        obj_in: CreateArticleSchema,
        session: Session = Depends(get_db),
):
    return _service.create(session, obj_in)


@router.patch('/articles/{pk}', response_model=ArticleSchema)
def patch(
        pk: int,
        obj_in: UpdateArticleSchema,
        session: Session = Depends(get_db)
):
    return _service.patch(session, pk, obj_in)


@router.delete('/articles/{pk}')
def delete(
        pk: int,
        session: Session = Depends(get_db)
):
    return _service.delete(session, pk)
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/middlewares.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建数据库会话中间件：</font>

```python
from typing import Callable

from fastapi import FastAPI, Request, Response

from example_blog.db import SessionFactory


async def db_session_middleware(request: Request, call_next: Callable) -> Response:
    response = Response('Internal server error', status_code=500)
    try:
        request.state.db = SessionFactory()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response


def init_middleware(app: FastAPI) -> None:
    app.middleware('http')(db_session_middleware)
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/dependencies.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建 Fastapi 的依赖项：</font>

```python
from fastapi import Request
from sqlalchemy.orm import Session


def get_db(request: Request) -> Session:
    return request.state.db


class CommonQueryParams:
    def __init__(self, offset: int = 1, limit: int = 10):
        self.offset = offset - 1
        if self.offset < 0:
            self.offset = 0
        self.limit = limit

        if self.limit < 0:
            self.limit = 10
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/routes.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建路由：</font>

```python
from fastapi import APIRouter, FastAPI

from example_blog import views


def router_v1():
    router = APIRouter()
    router.include_router(views.router, tags=['Article'])
    return router


def init_routers(app: FastAPI):
    app.include_router(router_v1(), prefix='/api/v1', tags=['v1'])
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/server.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建服务启动逻辑：</font>

```python
"""server"""
import uvicorn
from fastapi import FastAPI

from example_blog import middlewares, routes
from example_blog.config import settings
from example_blog.log import init_log


class Server:

    def __init__(self):
        init_log()
        self.app = FastAPI()

    def init_app(self):
        middlewares.init_middleware(self.app)
        routes.init_routers(self.app)

    def run(self):
        self.init_app()
        uvicorn.run(
            app=self.app,
            host=settings.HOST,
            port=settings.PORT,
        )
```

<font style="color:rgba(0, 0, 0, 0.87);">修改</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/config/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，增加服务配置：</font>

```python
HOST: 127.0.0.1
PORT: 8000
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "feat: Add api service."
```

### <font style="color:rgba(0, 0, 0, 0.87);">3.7 编写启动命令</font>
<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，增加启动 Server 逻辑：</font>

```python
@main.command()
@click.option('-h', '--host', show_default=True, help=f'Host IP. Default: {settings.HOST}')
@click.option('-p', '--port', show_default=True, type=int, help=f'Port. Default: {settings.PORT}')
@click.option('--level', help='Log level')
def server(host, port, level):
    """Start server."""
    kwargs = {
        'LOGLEVEL': level,
        'HOST': host,
        'PORT': port,
    }
    for name, value in kwargs.items():
        if value:
            settings.set(name, value)

    Server().run()
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "feat: Add server cmdline."
```

### <font style="color:rgba(0, 0, 0, 0.87);">3.8 启动 Server</font>
<font style="color:rgba(0, 0, 0, 0.87);">将本项目以可编辑方式安装到当前 Python 环境：</font>

```python
pip install -e .
```

<font style="color:rgba(0, 0, 0, 0.87);">命令行运行：</font>

```python
example_blog server
```

<font style="color:rgba(0, 0, 0, 0.87);">可以看到如下输出：</font>

```python
INFO:     Started server process [21687]
2020-12-28 18:11:56,341 INFO uvicorn.error 21687 139772921304768 Started server process [21687]
INFO:     Waiting for application startup.
2020-12-28 18:11:56,341 INFO uvicorn.error 21687 139772921304768 Waiting for application startup.
INFO:     Application startup complete.
2020-12-28 18:11:56,341 INFO uvicorn.error 21687 139772921304768 Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
2020-12-28 18:11:56,341 INFO uvicorn.error 21687 139772921304768 Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

<font style="color:rgba(0, 0, 0, 0.87);">浏览器打开</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">http://127.0.0.1:8000/docs</font>](http://127.0.0.1:8000/docs)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">即可查看接口文档。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码</font>

### <font style="color:rgba(0, 0, 0, 0.87);">3.9 引入迁移工具</font>
<font style="color:rgba(0, 0, 0, 0.87);">为了便于数据模型变更，引入</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">alembic</font>](https://alembic.sqlalchemy.org/en/latest/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">做数据库迁移。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add alembic
```

<font style="color:rgba(0, 0, 0, 0.87);">查看</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，将增加安装依赖：</font>

```python
[tool.poetry.dependencies]
click = "^8.1.3"
dynaconf = "^3.1.11"
sqlalchemy = "^1.4.44"
mysqlclient = "^2.1.1"
pydantic = "^1.10.2"
fastapi = "^0.88.0"
uvicorn = "^0.20.0"
alembic = "^1.8.1"
```

<font style="color:rgba(0, 0, 0, 0.87);">初始化 alembic ：</font>

```python
alembic init migration
mv alembic.ini src/example_blog/migration
```

<font style="color:rgba(0, 0, 0, 0.87);">将 alembic 的相关文件全部放到</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/migration`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录中</font>

<font style="color:rgba(0, 0, 0, 0.87);">修改</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/migration/alembic.ini`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">：</font>

```python
# A generic, single database configuration.

[alembic]
# path to migration scripts
;script_location = src/example_blog/migration
script_location = .

# template used to generate migration files
# file_template = %%(rev)s_%%(slug)s

# timezone to use when rendering the date
# within the migration file as well as the filename.
# string value is passed to dateutil.tz.gettz()
# leave blank for localtime
# timezone =

# max length of characters to apply to the
# "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; this defaults
# to src/example_blog/migration/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path
# version_locations = %(here)s/bar %(here)s/bat src/example_blog/migration/versions

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

;sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks=black
# black.type=console_scripts
# black.entrypoint=black
# black.options=-l 79

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
```

<font style="color:rgba(0, 0, 0, 0.87);">修改</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/migration/env.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">：</font>

```python
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from example_blog import db
from example_blog.models import BaseModel

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None

target_metadata = BaseModel.metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=db.url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = str(db.url)
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

<font style="color:rgba(0, 0, 0, 0.87);">编写</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建迁移命令：</font>

```python
from pathlib import Path

from alembic import config
from click import Context


@main.command()
@click.pass_context
@click.option('-h', '--help', is_flag=True)
@click.argument('args', nargs=-1)
def migrate(ctx: Context, help, args):
    """usage migrate -- arguments    """
    with utils.chdir(Path(__file__).parent / 'migration'):
        argv = list(args)
        if help:
            argv.append('--help')
        config.main(prog=ctx.command_path, argv=argv)
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`utils.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">：</font>

```python
"""Utils"""

import contextlib
import os
from os import PathLike
from typing import Union


@contextlib.contextmanager
def chdir(path: Union[str, PathLike]):
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)
```

**<font style="color:rgba(0, 0, 0, 0.87);">提示</font>**

<font style="color:rgba(0, 0, 0, 0.87);">由于使用了 click 包装了 alembic 命令，在使用上会有点不同，默认应该使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`migrate --`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">后加 alembic 的其他参数，否则多参数的情况下会无法识别。</font>

<font style="color:rgba(0, 0, 0, 0.87);">为了将</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/migration`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">打包到项目中，需要将其变成 Python 包。</font>

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/migration/__init__.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">和</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/migration/versions/__init__.py`

<font style="color:rgba(0, 0, 0, 0.87);">创建空白数据库迁移版本：</font>

```python
example_blog migrate -- revision -m "init"
```

<font style="color:rgba(0, 0, 0, 0.87);">执行迁移：</font>

```python
example_blog migrate -- upgrade head
```

<font style="color:rgba(0, 0, 0, 0.87);">创建第一个数据库迁移版本：</font>

```python
example_blog migrate -- revision --autogenerate -m "init_table"
```

<font style="color:rgba(0, 0, 0, 0.87);">执行迁移：</font>

```python
example_blog migrate -- upgrade head
```

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "Add alembic migrate."
```

## <font style="color:rgba(0, 0, 0, 0.87);">4. 测试和优化代码</font>
<font style="color:rgba(0, 0, 0, 0.87);">测试是软件开发中重要的一环，能够在发布之前检查出更多可能出现的异常情况。</font>

<font style="color:rgba(0, 0, 0, 0.87);">测试框架选用比较常用的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pytest</font>](https://docs.pytest.org/en/stable/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，它具有强大的功能和很好的兼容性。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add -D pytest
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，初始化测试配置：</font>

```python
DEBUG: false
LOG_LEVEL: INFO

HOST: 127.0.0.1
PORT: 8000

DATABASE:
  DRIVER: mysql
  NAME: example_blog
  HOST: 127.0.0.1
  PORT: 3306
  USERNAME: root
  PASSWORD: root
  QUERY:
    charset: utf8mb4
```

<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/__init__.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，加载测试配置：</font>

```python
import os

from example_blog.config import settings

settings.load_file(os.path.join(os.path.dirname(__file__), 'settings.yml'))
settings.load_file(os.path.join(os.path.dirname(__file__), 'settings.local.yml'))
```

<font style="color:rgba(0, 0, 0, 0.87);">虽然本地开发配置可以临时调整，但对于开发环境和测试环境依然有些不一样。从上面代码中可以看到加载了两个测试配置，和 Dynaconf 规则一样，</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">配置为本地配置，不会被代码追踪，只不过这里是手动实现的。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "test: Init test."
```

### <font style="color:rgba(0, 0, 0, 0.87);">4.1 测试数据访问层</font>
<font style="color:rgba(0, 0, 0, 0.87);">编写测试配置：</font>

<font style="color:rgba(0, 0, 0, 0.87);">新建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/conftest.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建测试配置：</font>

```python
"""Test config"""

import os
from pathlib import Path

import pytest
from alembic import command, config

from sqlalchemy.orm import Session

from example_blog import migration
from example_blog.config import settings
from example_blog.db import SessionFactory
from example_blog.models import Article


@pytest.fixture()
def migrate():
    """Re-init database when run a test."""
    os.chdir(Path(migration.__file__).parent)
    alembic_config = config.Config('./alembic.ini')
    alembic_config.set_main_option('script_location', os.getcwd())
    print('\n----- RUN ALEMBIC MIGRATION: -----\n')
    command.downgrade(alembic_config, 'base')
    command.upgrade(alembic_config, 'head')
    try:
        yield
    finally:
        command.downgrade(alembic_config, 'base')
        db_name = settings.DATABASE.get('NAME')
        if settings.DATABASE.DRIVER == 'sqlite' and os.path.isfile(db_name):
            try:
                os.remove(db_name)
            except FileNotFoundError:
                pass


@pytest.fixture()
def session(migrate) -> Session:
    """session fixture"""
    _s = SessionFactory()
    yield _s
    _s.close()


@pytest.fixture()
def init_article(session):
    """Init article"""
    a_1 = Article(title='Hello world', body='Hello world, can you see me?')
    a_2 = Article(title='Love baby', body='I love you everyday, and i want with you.')
    a_3 = Article(title='Tomorrow', body='When the sun rises, this day is fine day, cheer up.')
    session.add_all([a_1, a_2, a_3])
    session.commit()
```

<font style="color:rgba(0, 0, 0, 0.87);">编写数据访问层用例：</font>

```python
import pytest

from example_blog.dao import ArticleDAO
from example_blog.models import Article
from example_blog.schemas import CreateArticleSchema, UpdateArticleSchema


class TestArticle:

    @pytest.fixture()
    def dao(self, init_article):
        yield ArticleDAO()

    def test_get(self, dao, session):
        users = dao.get(session)
        assert len(users) == 3
        users = dao.get(session, limit=2)
        assert len(users) == 2
        users = dao.get(session, offset=4)
        assert not users

    def test_get_by_id(self, dao, session):
        user = dao.get_by_id(session, 1)
        assert user.id == 1

    def test_create(self, dao, session):
        origin_count = session.query(dao.model).count()
        obj_in = CreateArticleSchema(title='test')
        dao.create(session, obj_in)
        count = session.query(dao.model).count()
        assert origin_count + 1 == count

    def test_patch(self, dao, session):
        obj: Article = session.query(dao.model).first()
        body = obj.body
        obj_in = UpdateArticleSchema(body='test')
        updated_obj: Article = dao.patch(session, obj.id, obj_in)
        assert body != updated_obj.body

    def test_delete(self, dao, session):
        origin_count = session.query(dao.model).count()
        dao.delete(session, 1)
        count = session.query(dao.model).count()
        assert origin_count - 1 == count

    def test_count(self, dao, session):
        count = dao.count(session)
        assert count == 3
```

<font style="color:rgba(0, 0, 0, 0.87);">运行测试：</font>

```python
pytest tests/test_dao.py
```

<font style="color:rgba(0, 0, 0, 0.87);">如果运行成功，则测试正确。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "test: Add dao test."
```

### <font style="color:rgba(0, 0, 0, 0.87);">4.2 测试服务层</font>
<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/test_services.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建测试用例：</font>

```python
import pytest

from example_blog.schemas import CreateArticleSchema, UpdateArticleSchema
from example_blog.services import ArticleService


class TestArticleService:

    @pytest.fixture()
    def service(self, init_article):
        yield ArticleService()

    def test_get(self, service, session):
        objs = service.get(session)
        assert len(objs) == 3
        objs = service.get(session, limit=2)
        assert len(objs) == 2
        objs = service.get(session, offset=5)
        assert not objs

    def test_total(self, service, session):
        total = service.total(session)
        assert total == 3

    def test_by_id(self, service, session):
        __obj = session.query(service.dao.model).first()
        obj = service.get_by_id(session, __obj.id)
        assert obj.id == __obj.id

    def test_create(self, service, session):
        origin_count = service.total(session)
        obj_in = CreateArticleSchema(title='test')
        service.create(session, obj_in)
        count = service.total(session)
        assert origin_count + 1 == count

    def test_patch(self, service, session):
        origin_obj = session.query(service.dao.model).first()
        body = origin_obj.body
        obj_in = UpdateArticleSchema(body='test')
        obj = service.patch(session, origin_obj.id, obj_in)
        assert body != obj.body

    def test_delete(self, service, session):
        origin_count = service.total(session)
        obj = session.query(service.dao.model).first()
        service.delete(session, obj.id)
        count = service.total(session)
        assert origin_count - 1 == count
```

<font style="color:rgba(0, 0, 0, 0.87);">运行测试：</font>

```python
pytest tests/test_services.py
```

<font style="color:rgba(0, 0, 0, 0.87);">如果运行成功，则测试正确。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "test: Add service test."
```

### <font style="color:rgba(0, 0, 0, 0.87);">4.3 测试视图层</font>
<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/conftest.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建测试配置：</font>

```python
from fastapi.testclient import TestClient

from example_blog import migration, server



@pytest.fixture
def client():
    """Fast api test client factory"""
    _s = server.Server()
    _s.init_app()
    _c = TestClient(app=_s.app)
    yield _c
```

<font style="color:rgba(0, 0, 0, 0.87);">由于 Fastapi 的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`TestClient`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">依赖</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`requests`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，所以需要先安装：</font>

```python
poetry add -D requests
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/test_views.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，测试试图：</font>

```python
import pytest
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response

from example_blog.models import Article
from example_blog.schemas import ModelType


def test_docs(client):
    """Test view"""
    response = client.get('/docs')
    assert response.status_code == 200


class BaseTest:
    version = 'v1'
    base_url: str
    model: ModelType

    @pytest.fixture()
    def init_data(self):
        pass

    def url(self, pk: int = None) -> str:
        url_split = ['api', self.version, self.base_url]
        if pk:
            url_split.append(str(pk))
        return '/'.join(url_split)

    def assert_response_ok(self, response: Response):
        assert response.status_code == 200

    def test_get(self, client, session, init_data):
        count = session.query(self.model).count()
        response = client.get(self.url())
        self.assert_response_ok(response)
        assert count == len(response.json())

    def test_get_by_id(self, client, session, init_data):
        obj = session.query(self.model).first()
        response = client.get(self.url(obj.id))
        self.assert_response_ok(response)
        assert jsonable_encoder(obj) == response.json()

    def test_delete(self, client, session, init_data):
        count = session.query(self.model).count()
        session.close()
        response = client.delete(self.url(1))
        self.assert_response_ok(response)
        after_count = session.query(self.model).count()
        assert after_count == 2
        assert count - 1 == after_count


class TestArticle(BaseTest):
    model = Article
    base_url = 'articles'

    @pytest.fixture()
    def init_data(self, init_article):
        pass

    def test_create(self, client, session, init_data):
        response = client.post(
            self.url(),
            json={'title': 'xxx'}
        )
        self.assert_response_ok(response)
        assert response.json().get('title') == 'xxx'

    def test_patch(self, client, session, init_data):
        obj = session.query(Article).first()
        response = client.patch(self.url(obj.id), json={'body': 'xxx'})
        self.assert_response_ok(response)
        assert response.json().get('body') != obj.body
```

<font style="color:rgba(0, 0, 0, 0.87);">运行测试：</font>

```python
pytest tests/test_views.py
```

<font style="color:rgba(0, 0, 0, 0.87);">如果运行成功，则测试正确。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "test: Add view test."
```

### <font style="color:rgba(0, 0, 0, 0.87);">4.4 测试命令行</font>
<font style="color:rgba(0, 0, 0, 0.87);">编辑</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/conftest.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建测试配置：</font>

```python
from click.testing import CliRunner


@pytest.fixture
def cli():
    runner = CliRunner(echo_stdin=True, mix_stderr=False)
    yield runner
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/test_cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建测试用例：</font>

```python
import uvicorn
from alembic import config

import example_blog
from example_blog import cmdline


def test_main(cli):
    result = cli.invoke(cmdline.main)
    assert result.exit_code == 0
    result = cli.invoke(cmdline.main, '-V')
    assert result.exit_code == 0
    assert str(result.output).strip() == example_blog.__version__


def test_run(cli, mocker):
    mock_run = mocker.patch.object(uvicorn, 'run')
    result = cli.invoke(cmdline.main, ['server', '-h', '127.0.0.1', '-p', '8080'])
    assert result.exit_code == 0
    mock_run.assert_called_once_with(app=mocker.ANY, host='127.0.0.1', port=8080)


def test_migrate(cli, mocker):
    mock_main = mocker.patch.object(config, 'main')
    cli.invoke(cmdline.main, ['migrate', '--help'])
    mock_main.assert_called_once()
```

<font style="color:rgba(0, 0, 0, 0.87);">因为单元测试中使用了</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">mock</font>](https://docs.python.org/3/library/unittest.mock.html)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，所以安装配合 pytest 使用的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pytest-mock</font>](https://github.com/pytest-dev/pytest-mock/)

```python
poetry add -D pytest-mock
```

<font style="color:rgba(0, 0, 0, 0.87);">运行测试：</font>

```python
pytest tests/test_views.py
```

<font style="color:rgba(0, 0, 0, 0.87);">如果运行成功，则测试正确。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "test: Add cmdline test."
```

### <font style="color:rgba(0, 0, 0, 0.87);">4.5 其他测试</font>
<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/test_dependencies.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建测试用例：</font>

```python
import pytest

from example_blog.dependencies import CommonQueryParams


@pytest.mark.parametrize(
    ['args', 'expect_value'],
    [
        ((), (0, 10)),
        ((0,), (0, 10)),
        ((-10, -10), (0, 10)),
        ((5, 100), (4, 100)),
    ]
)
def test_common_query_params(args, expect_value):
    params = CommonQueryParams(*args)
    assert params.offset == expect_value[0]
    assert params.limit == expect_value[1]
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/test_utils.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，创建测试用例：</font>

```python
import os

from example_blog.utils import chdir


def test_chdir():
    path = '/tmp'
    cwd = os.getcwd()
    with chdir(path):
        assert path == os.getcwd()
    assert cwd == os.getcwd()
```

<font style="color:rgba(0, 0, 0, 0.87);">运行测试：</font>

```python
pytest
```

<font style="color:rgba(0, 0, 0, 0.87);">如果运行成功，则测试正确。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "test: Add other test."
```

<font style="color:rgba(0, 0, 0, 0.87);">至此，所有测试运行完毕，除了</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/example_blog/migration`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">之外的包的测试已经可以全部覆盖。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">4.6 优化代码</font>
<font style="color:rgba(0, 0, 0, 0.87);">代码风格和代码规范是一个开发人员开发修养的体现，好的代码能够让人眼前一亮。为了规范，社区开发许多工具用于检测代码。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">4.6.1 优化导入</font>
[<font style="color:rgba(0, 0, 0, 0.87);">isort</font>](https://pycqa.github.io/isort/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个自动格式化导入的工具。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add -D isort
```

<font style="color:rgba(0, 0, 0, 0.87);">格式化代码：</font>

```python
isort .
```

<font style="color:rgba(0, 0, 0, 0.87);">此时可以不用先急着提交，在后面对代码风格检测的时候可能还会再次格式化代码。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">4.6.2 优化代码风格</font>
[<font style="color:rgba(0, 0, 0, 0.87);">flake8</font>](https://flake8.pycqa.org/en/latest/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个遵循</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">PEP8</font>](https://www.python.org/dev/peps/pep-0008/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">规范检测代码的工具。使用该工具，可以检测出哪些代码不符合 PEP8 规范。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装依赖：</font>

```python
poetry add -D flake8
```

<font style="color:rgba(0, 0, 0, 0.87);">检测代码：</font>

```python
flake8
```

<font style="color:rgba(0, 0, 0, 0.87);">根据输出提示，参照</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">flake8 规则</font>](https://www.flake8rules.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">进行调整，直至完全符合为止。</font>

<font style="color:rgba(0, 0, 0, 0.87);">提交代码：</font>

```python
git add .
git commit -m "feat: Lint code"
```

## <font style="color:rgba(0, 0, 0, 0.87);">5. 打包发布</font>
<font style="color:rgba(0, 0, 0, 0.87);">到这一步，</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件应该是这样的：</font>

```python
[tool.poetry]
name = "example_blog"
version = "0.1.0"
description = "This is example blog system."
authors = ["huagang <huagang517@126.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
fastapi-sa = "^0.0.1.dev0"
sqlalchemy = "^1.4.44"
mysqlclient = "^2.1.1"
pydantic = "^1.10.2"
dynaconf = "^3.1.11"
fastapi = "^0.88.0"
uvicorn = "^0.20.0"
alembic = "^1.8.1"

[tool.poetry.group.dev.dependencies]
pytest = "^7.2.0"
isort = "^5.10.1"
requests = "^2.28.1"
pytest-mock = "^3.10.0"
flake8 = "^6.0.0"

[tool.poetry.scripts]
example_blog = "example_blog.cmdline:main"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

<font style="color:rgba(0, 0, 0, 0.87);">在整个开发过程中，是逐步丰富此文件的。这是项目的描述文件，描述了打包的配置信息。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">5.1 打包</font>
```python
poetry build
```

<font style="color:rgba(0, 0, 0, 0.87);">在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`dist`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录中可以看到两个文件，一个是</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`.tar.gz`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的源码打包文件，一个是</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`.whl`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的二进制文件。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">5.2 发布</font>
<font style="color:rgba(0, 0, 0, 0.87);">将开发好的项目发布到索引仓库，或内网的私有仓库。</font>

<font style="color:rgba(0, 0, 0, 0.87);">使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">poetry</font>](https://python-poetry.org/docs/cli/#publish)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">上传：</font>

<font style="color:rgba(0, 0, 0, 0.87);">poetry publish</font>

