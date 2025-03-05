## <font style="color:rgba(0, 0, 0, 0.87);">1. 开发环境搭建</font>
### <font style="color:rgba(0, 0, 0, 0.87);">1.1 Python 开发环境</font>
<font style="color:rgba(0, 0, 0, 0.87);">本项目使用 Python 3.10 。具体版本的 Python 环境可以在</font>[<font style="color:rgba(0, 0, 0, 0.87);">官网</font>](https://www.python.org/downloads/)<font style="color:rgba(0, 0, 0, 0.87);">下载。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1.2 开发工具</font>
<font style="color:rgba(0, 0, 0, 0.87);">推荐使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Pycharm</font>](https://www.jetbrains.com/pycharm/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">开发工具，可以选择免费的社区版本。</font>

[<font style="color:rgba(0, 0, 0, 0.87);">Visual Studio Code</font>](https://code.visualstudio.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是微软开发的一款免费轻量级文本编辑器，通过安装插件可以自定义成一款功能强大的 IDE 开发工具。目前支持 Python 的插件体系已经较为完善，此方案也可以作为备用。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1.3 虚拟环境工具</font>
<font style="color:rgba(0, 0, 0, 0.87);">推荐使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Poetry</font>](https://python-poetry.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，既包含了虚拟环境管理工具也支持打包发布等功能。</font>

<font style="color:rgba(0, 0, 0, 0.87);">在安装好 Python 环境后，应该在全局环境中安装</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Poetry</font>](https://python-poetry.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。</font>

```bash
sudo python -m pip install -U pip
sudo pip install -U poetry
```

### <font style="color:rgba(0, 0, 0, 0.87);">1.4 初始化项目</font>
[<font style="color:rgba(0, 0, 0, 0.87);">cookiecutter</font>](https://cookiecutter.readthedocs.io/en/1.7.2/README.html)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个通过项目模板创建项目的命令行工具。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装 cookiecutter</font>

```bash
sudo pip3 install -U cookiecutter
```

<font style="color:rgba(0, 0, 0, 0.87);">初始化项目</font>

```bash
cd workspace
cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
```

<font style="color:rgba(0, 0, 0, 0.87);">运行命令后会出现下面的配置过程，如果你不清楚配置的具体用途，可以直接按回车使用默认配置，默认配置使用项目模板初始值。</font>

```bash
❯ cookiecutter https://github.com/pyloong/cookiecutter-pythonic-project
project_name [My Project]: Word Count
project_slug [word_count]: 
project_description [My Awesome Project!]: Word Count Project.
author_name [Author]: test
author_email [author@example.com]: test@example.com
version [0.1.0]: 
Select python_version:
1 - 3.10
2 - 3.11
Choose from 1, 2 [1]: 
use_src_layout [y]: 
use_poetry [y]: 
use_docker [n]: 
Select ci_tools:
1 - none
2 - Gitlab
3 - Github
Choose from 1, 2, 3 [1]: 
init_skeleton [n]:
```

<font style="color:rgba(0, 0, 0, 0.87);">如果你在使用项目模板过程中有任何问题或疑问，可以通过发起</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">issues</font>](https://github.com/pyloong/cookiecutter-pythonic-project/issues)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">进行反馈。</font>

<font style="color:rgba(0, 0, 0, 0.87);">生成后的项目结构如下：</font>

```bash
word_count
├── .editorconfig
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── README.md
├── docs
│   └── development.md
├── pyproject.toml
├── src
│   └── word_count
│       └── __init__.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── settings.yml
│   └── test_version.py
└── tox.ini

5 directories, 13 files
```

<font style="color:rgba(0, 0, 0, 0.87);">生成项目的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录下有一个项目模块，用来存放项目源代码，</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录用来编写模块的相关测试代码。</font>

`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">包含项目初始依赖，和项目的描述信息，</font>`tox.ini`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">定义了任务自动化执行逻辑。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1.5 初始化项目环境</font>
<font style="color:rgba(0, 0, 0, 0.87);">使用 poetry 初始化一个虚拟环境。</font>

```bash
cd word_count
poetry install -v
```

<font style="color:rgba(0, 0, 0, 0.87);">初始化完成后，会生成一个</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`poetry.lock`<font style="color:rgba(0, 0, 0, 0.87);">，可以用来锁定生产环境安装包的版本和依赖信息。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1.6 初始化 Git</font>
<font style="color:rgba(0, 0, 0, 0.87);">推荐使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Git</font>](https://git-scm.com/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">对项目进行版本管理。所以需要提前安装 Git ，并熟悉常用的 Git 概念和 Git 命令。</font>

```bash
git init
git config user.name test
git config user.email test@example.com

# 初始化项目提交
git add .
git commit -m "feat: 初始化项目提交"
```

### <font style="color:rgba(0, 0, 0, 0.87);">1.7 会用到的其他工具</font>
<font style="color:rgba(0, 0, 0, 0.87);">在生成的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件中，默认添加了一些开发环境中常用的工具。</font>

+ `isort`<font style="color:rgba(0, 0, 0, 0.87);">:</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">isort</font>](https://pycqa.github.io/isort/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个自动格式化导入工具</font>
+ `pylint`<font style="color:rgba(0, 0, 0, 0.87);">:</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pylint</font>](https://www.pylint.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个检测代码风格工具</font>
+ `pytest`<font style="color:rgba(0, 0, 0, 0.87);">:</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pytest</font>](https://docs.pytest.org/en/stable/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个更加易用的测试框架，兼容</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`unittest`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">测试框架</font>
+ `pytest-cov`<font style="color:rgba(0, 0, 0, 0.87);">:</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pytest-cov</font>](https://github.com/pytest-dev/pytest-cov)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pytest`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">Coverage</font>](https://coverage.readthedocs.io/en/latest/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">插件，用来统计测试覆盖率</font>
+ `mkdocs`<font style="color:rgba(0, 0, 0, 0.87);">:</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">mkdocs</font>](https://www.mkdocs.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个项目文档构建工具，使用 markdown 编写内容，构建生成文档页面。</font>
+ `mkdocs-material`<font style="color:rgba(0, 0, 0, 0.87);">:</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">mkdocs-material</font>](https://squidfunk.github.io/mkdocs-material/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是基于</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">mkdocs</font>](https://www.mkdocs.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">构建文档，并提供现代化主题的库。</font>
+ `tox`<font style="color:rgba(0, 0, 0, 0.87);">:</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">tox</font>](https://tox.readthedocs.io/en/latest/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">是一个任务自动化工具</font>

<font style="color:rgba(0, 0, 0, 0.87);">如果想要了解相关的功能，可以阅读对应的技术说明文档。</font>

## <font style="color:rgba(0, 0, 0, 0.87);">2. 功能开发</font>
<font style="color:rgba(0, 0, 0, 0.87);">首先将项目以可编辑方式安装到环境中：</font>

```bash
poetry install
```

<font style="color:rgba(0, 0, 0, 0.87);">这样做的目的是将</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">下的包安装到 Python 环境中，否则无法正常导入包中的模块。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">2.1 功能需求</font>
<font style="color:rgba(0, 0, 0, 0.87);">提供一个从文本文件读取数据，数据以空格分割单词，然后统计文件中的单词数量，并将结果写入到目标文件中。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">2.2 编写计数器</font>
<font style="color:rgba(0, 0, 0, 0.87);">在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/word_count/`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">下创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`counter.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，同时加入如下内容：</font>

```bash
"""Count a file """
import logging
from collections.abc import Generator
from pathlib import Path

# Config root logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def count(source_file: str, dest_file: str):
    """
    Count source
    :param source_file:
    :param dest_file:
    :return:
    """
    words = read_from_file(Path(source_file))

    total = 0

    for _ in words:
        total += 1

    write_to_file(Path(dest_file), total)


def read_from_file(source_file: Path) -> Generator[str, None, None]:
    """

    :param source_file:
    :return:
    """
    # Read source_file
    logging.debug('Read file: %s', source_file)
    with open(source_file, 'r', encoding='utf-8') as source_obj:
        for line in source_obj:
            for word in line.split(' '):
                yield word


def write_to_file(dest_file: Path, total_words: int) -> None:
    """
    Write result to file
    :param dest_file:
    :param total_words:
    :return:
    """
    logging.debug('Count %s words, write to %d', dest_file, total_words)
    with open(dest_file, 'w', encoding='utf-8') as dest_obj:
        dest_obj.write(f'Total count: {total_words}')
```

#### <font style="color:rgba(0, 0, 0, 0.87);">2.2.1 导入格式化</font>
<font style="color:rgba(0, 0, 0, 0.87);">在项目根目录运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">isort</font>](https://pycqa.github.io/isort/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">对导入进行格式化。</font>

```bash
isort .
```

<font style="color:rgba(0, 0, 0, 0.87);">此操作会自动修改代码，将导入的包格式化。如果想查看区别，可以运行如下命令：</font>

```bash
isort . --check-only --diff
```

#### <font style="color:rgba(0, 0, 0, 0.87);">2.2.2 代码风格检查</font>
<font style="color:rgba(0, 0, 0, 0.87);">在项目根目录运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pylint</font>](https://www.pylint.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">检查代码是否规范，是否符合</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">PEP8</font>](https://www.python.org/dev/peps/pep-0008/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">标准。</font>

```bash
pylint tests src
```

<font style="color:rgba(0, 0, 0, 0.87);">此操作会列出代码中不符合规范的部分，并显示对应的规范名称。可以在</font>[<font style="color:rgba(0, 0, 0, 0.87);">这里</font>](https://pylint.readthedocs.io/en/latest/technical_reference/features.html)<font style="color:rgba(0, 0, 0, 0.87);">找到所有规则。</font>

<font style="color:rgba(0, 0, 0, 0.87);">在完成修改后再次运行两个命令，直到都没有异常输出为止。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">2.2.3 测试</font>
如果你使用的是 Pycharm 开发，可以通过点击 `File` --> `Settings` --> `Tools` --> `Python Integrated Tools` --> `Testing` --> `Default runner` 选择测试框架，推荐使用 `pytest`。

<font style="color:rgba(0, 0, 0, 0.87);">为了方便使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`mock`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">需要安装</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pytest-mock`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">模块，可以在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pytest`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`fixture`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">特性上使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`mock`<font style="color:rgba(0, 0, 0, 0.87);">。</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装开发环境依赖：</font>

```bash
poetry add --group dev pytest-mock
```

<font style="color:rgba(0, 0, 0, 0.87);">添加测试配置，在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/conftest.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">中加入：</font>

```bash
"""Test config"""
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


@pytest.fixture
def mock_path() -> Path:
    """Mock a path, and clean when unit test done."""
    with TemporaryDirectory() as temp_path:
        yield Path(temp_path)
```

<font style="color:rgba(0, 0, 0, 0.87);">在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">下添加与</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/word_count`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录中文件名相同的文件，并在文件名前添加</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`test_`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">前缀。</font>

<font style="color:rgba(0, 0, 0, 0.87);">添加文件</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/test_counter.py`<font style="color:rgba(0, 0, 0, 0.87);">：</font>

```bash
"""Test counter"""
from pathlib import Path

import pytest

from word_count.counter import count, read_from_file, write_to_file


@pytest.fixture(name='mock_source_file')
def fixture_mock_source_file(mock_path) -> Path:
    """mock source_file, this file has two words."""
    words = ['hello', ' ', 'words']
    source_file = mock_path / 'source.txt'
    with open(source_file, 'w', encoding='utf-8') as obj:
        obj.write(''.join(words))
    yield source_file


def test_read_from_file(mock_source_file):
    """Test read_from_file"""
    result = read_from_file(mock_source_file)
    assert sum(1 for _ in result) == 2


def test_write_to_file(mock_path):
    """Test write_to_file"""
    dest_file = mock_path / 'dest.txt'
    write_to_file(dest_file, 100)
    with open(dest_file, 'r', encoding='utf-8') as obj:
        txt = obj.read()
        assert 'Total count: 100' in txt


def test_count(mocker, mock_path, mock_source_file):
    """Test count"""
    mock_read_from_file = mocker.patch(
        'word_count.counter.read_from_file',
        return_value=list(range(10))
    )
    mock_write_to_file = mocker.patch(
        'word_count.counter.write_to_file'
    )
    dest_file = mock_path / 'dest.txt'
    count(str(mock_source_file), str(dest_file))
    mock_read_from_file.assert_called_once_with(mock_source_file)
    mock_write_to_file.assert_called_once_with(dest_file, 10)
```

<font style="color:rgba(0, 0, 0, 0.87);">运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pytest`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，让测试正确运行。如果测试用例失败，需要根据出错堆栈找到问题原因，解决掉后再次运行测试命令，直到代码测试通过。</font>

<font style="color:rgba(0, 0, 0, 0.87);">然后运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`isort`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">和</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pylint src tests`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">格式化代码并检查代码风格。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">2.2.4 提交代码</font>
<font style="color:rgba(0, 0, 0, 0.87);">一个功能特性开发完成后，需要提交代码来保存记录，避免意外操作。</font>

```bash
git add .
git commit -m "feat(counter): 增加 Counter 逻辑，并完成测试。"
```

### <font style="color:rgba(0, 0, 0, 0.87);">2.3 编写命令行入口</font>
<font style="color:rgba(0, 0, 0, 0.87);">在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`src/word_count/`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录下，创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，加入如下内容：</font>

```python
"""Cmdline"""
import argparse
import sys

from word_count.counter import count


def init_args() -> argparse.Namespace:
    """Init argument and parse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', required=True, help='Source file used for count.')
    parser.add_argument('-d', '--dest', required=True, help='Dest file used for count result')
    return parser.parse_args(sys.argv[1:])


def main():
    """Execute"""
    args = init_args()
    count(args.source, args.dest)


if __name__ == '__main__':
    main()
```

<font style="color:rgba(0, 0, 0, 0.87);">运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`isort`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">和</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pylint`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">格式化代码并检查代码风格。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">2.3.1 测试</font>
<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tests/test_cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，加入如下内容：</font>

```python
"""Test cmdline"""
import sys

import pytest

from word_count import cmdline


def test_help(mocker, capsys):
    """test help command"""
    args = ['word_count', '-h']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        cmdline.main()

    assert ex.value.code == 0
    outerr = capsys.readouterr()
    assert '-s SOURCE' in outerr.out
    assert '-d DEST' in outerr.out

def test_only_pass_source(mocker, capsys):
    """test only pass -s """
    args = ['word_count', '-s', 'foo']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        cmdline.main()

    assert ex.value.code == 2
    outerr = capsys.readouterr()
    assert 'the following arguments are required: -d' in outerr.err

def test_only_pass_dest(mocker, capsys):
    """test only pass -d"""
    args = ['word_count', '-d', 'foo']
    mocker.patch.object(sys, 'argv', args)
    with pytest.raises(SystemExit) as ex:
        cmdline.main()

    assert ex.value.code == 2
    outerr = capsys.readouterr()
    assert 'the following arguments are required: -s' in outerr.err

def test_main(mocker):
    """test cmdline, and everything is fine."""
    args = ['word_count', '-s', 'foo', '-d', 'bar']
    mocker.patch.object(sys, 'argv', args)
    mock_count = mocker.patch('word_count.cmdline.count')
    cmdline.main()
    mock_count.assert_called_once()
```

<font style="color:rgba(0, 0, 0, 0.87);">运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pytest`<font style="color:rgba(0, 0, 0, 0.87);">，让测试正确运行。</font>

<font style="color:rgba(0, 0, 0, 0.87);">运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`isort`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">和</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pylint`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">格式化代码并检查代码风格。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">2.3.2 提交代码</font>
```bash
git add .
git commit -m "feat(cmdline): 增加 cmdline 逻辑，并完成测试。"
```

### <font style="color:rgba(0, 0, 0, 0.87);">2.4 总结</font>
<font style="color:rgba(0, 0, 0, 0.87);">至此，我们的功能已经开发完成。在整个开发过程中，我们遵循了 “添加功能特性” => “代码风格检查” => “单元测试” 的开发流程。</font>

<font style="color:rgba(0, 0, 0, 0.87);">如果感觉每次运行多个命令比较繁琐，可以在项目根目录中运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`tox`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">自动化完成代码测试、导包检查和代码风格检查。</font>

```bash
tox
```

<font style="color:rgba(0, 0, 0, 0.87);">现在可以在终端中运行单词统计：</font>

```bash
python src/word_count/cmdline.py -s LICENSE -d /tmp/res.txt
```

### <font style="color:rgba(0, 0, 0, 0.87);">2.5 打包发布</font>
<font style="color:rgba(0, 0, 0, 0.87);">如果希望别人能更方便的使用项目，可以将项目打包发布到</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">pypi</font>](https://pypi.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">中，然后在需要使用的地方运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pip install -U word-count`<font style="color:rgba(0, 0, 0, 0.87);">。</font>

<font style="color:rgba(0, 0, 0, 0.87);">但是安装到环境后去运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">会比较麻烦，所以需要将</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`cmdline.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">注册成可执行命令。</font>

<font style="color:rgba(0, 0, 0, 0.87);">修改</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pyproject.toml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，增加如下内容：</font>

```bash
[tool.poetry.plugins.console_scripts]
word_count = "word_count.cmdline:main"
```

<font style="color:rgba(0, 0, 0, 0.87);">当使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pip`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">命令将项目包安装到环境后，会自动注册一个</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`word_count`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的可执行命令。</font>

<font style="color:rgba(0, 0, 0, 0.87);">再次将本地项目以可编辑方式安装到当前 Python 环境：</font>

```bash
poetry install
```

<font style="color:rgba(0, 0, 0, 0.87);">然后就可以正常使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`word_count`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">命令：</font>

```bash
$ word_count -h
usage: word_count [-h] -s SOURCE -d DEST

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Source file used for count.
  -d DEST, --dest DEST  Dest file used for count result
```

#### <font style="color:rgba(0, 0, 0, 0.87);">2.5.1 打包</font>
<font style="color:rgba(0, 0, 0, 0.87);">运行打包命令：</font>

```bash
poetry build
```

`sdist`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">会将项目打包成源码包，</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`bdist_wheel`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">会将项目打包成编译后的二进制包。</font>

<font style="color:rgba(0, 0, 0, 0.87);">打包后的文件在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`dist`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">目录中。可以直接在其他地方运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`pip install word_count.wheel`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">安装。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">2.5.2 发布</font>
<font style="color:rgba(0, 0, 0, 0.87);">将开发好的项目发布到索引仓库，或内网的私有仓库。</font>

```bash
poetry publish
```

<font style="color:rgba(0, 0, 0, 0.87);">默认会将项目发布到 </font>[<font style="color:rgba(0, 0, 0, 0.87);">pypi</font>](https://pypi.org/)<font style="color:rgba(0, 0, 0, 0.87);"> 中，所以需要有对应的登录账号。</font>

## <font style="color:rgba(0, 0, 0, 0.87);">3.文档管理</font>[Mkdocs](https://www.mkdocs.org/)<font style="color:rgba(0, 0, 0, 0.87);"> </font>
<font style="color:rgba(0, 0, 0, 0.87);">初始化文档配置：</font>

```plain
❯ mkdocs new .
INFO     -  Writing config file: ./mkdocs.yml
INFO     -  Writing initial docs: ./docs/index.md
❯ ls
docs  mkdocs.yml  pyproject.toml  poetry.lock
```

<font style="color:rgba(0, 0, 0, 0.87);">然后启动 mkdocs 的本地服务器：</font>

```plain
❯ mkdocs serve -a 127.0.0.1:33333
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.05 seconds
INFO     -  [11:00:22] Serving on http://127.0.0.1:33333/
```

<font style="color:rgba(0, 0, 0, 0.87);">然后浏览器打开 [http://127.0.0.1:8000] 访问生成的文档站点。</font>

<font style="color:rgba(0, 0, 0, 0.87);">站点使用默认主题，风格有点复古。可以使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>[<font style="color:rgba(0, 0, 0, 0.87);">mkdocs-material</font>](https://squidfunk.github.io/mkdocs-material/)<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">让站点更好看：</font>

<font style="color:rgba(0, 0, 0, 0.87);">安装</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`mkdocs-material`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">：</font>

```plain
poetry add mkdocs-material
```

<font style="color:rgba(0, 0, 0, 0.87);">修改配置文件</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`mkdocs.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，增加如下内容：</font>

```plain
theme:
  name: material
```

<font style="color:rgba(0, 0, 0, 0.87);">重新启动</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`mkdocs serve`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，即可看到注意已经改变。</font>

<font style="color:rgba(0, 0, 0, 0.87);">对于 Mkdocs 的更多使用细节可以参考文档：</font>

+ [<font style="color:rgba(0, 0, 0, 0.87);">Mkdocs 快速开始</font>](https://www.mkdocs.org/getting-started/#getting-started-with-mkdocs)
+ [<font style="color:rgba(0, 0, 0, 0.87);">Mkdocs 配置</font>](https://www.mkdocs.org/user-guide/configuration/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">mkdocs-material 主题</font>](https://squidfunk.github.io/mkdocs-material/)

## 配置
<font style="color:rgba(0, 0, 0, 0.87);">配置是一个项目的核心驱动，可以在不更改源代码或减少源代码修改的情况下快速调整项目的运行。 使用中心配置驱动项目，能让项目的使用更加灵活，运维工作更轻松。</font>

<font style="color:rgba(0, 0, 0, 0.87);">例如 Django 框架会自带一个</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">中的配置项都会覆盖框架 级别的默认配置，方便用户自定义修改。在代码中，可以使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`django.settings`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">对象获取所有 配置项。 Scrapy 框架同样也有这种机制。</font>

<font style="color:rgba(0, 0, 0, 0.87);">这些成熟的框架增加了中心配置，就是为了通过开放出来的配置项来灵活控制框架所支持的内容。 而在一般项目中，也可以参照这种设计，让项目部署更加灵活。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">1. 一般做法</font>
<font style="color:rgba(0, 0, 0, 0.87);">常见增加中心配置的做法是在项目中增加一个</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，该文件中模块级别常量定义配置项。 在使用时，通过导入模块中的内容使用。</font>

<font style="color:rgba(0, 0, 0, 0.87);">例如：</font>

<font style="color:rgba(0, 0, 0, 0.87);">在项目中创建一个</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，在文件中定义模块级常量</font>

```python
## Settings

# File config
SOURCE_FILE = '/tmp/foo.txt'

# Log config
LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
```

<font style="color:rgba(0, 0, 0, 0.87);">创建</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`app.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，在文件中导入</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">模块，并使用该模块中的常量。</font>

```python
"""Count a file """
import logging
from pathlib import Path  

import settings


# Config root logger
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=settings.LOG_FORMAT,
)


def count_word(source_file: Path) -> None:
    """
    :param source_file:
    :return:    None
    """
    total_words = 0
    # Read source_file
    logging.debug('Read file: %s', source_file)
    with open(source_file, mode='r', encoding='utf-8') as source_obj:
        for line in source_obj.readlines():
            total_words += len(line.split(' '))
    logging.info('File has %s words', total_words)


def main():
    count_word(Path(settings.SOURCE_FILE))


if __name__ == '__main__':
    main()
```

### <font style="color:rgba(0, 0, 0, 0.87);">2. 动态配置示例</font>
<font style="color:rgba(0, 0, 0, 0.87);">Dynaconf 是一个灵活的中心配置管理工具，底层设计和 Django 一致，会延迟加载配置。</font>

<font style="color:rgba(0, 0, 0, 0.87);">其具有如下特点：</font>

+ <font style="color:rgba(0, 0, 0, 0.87);">加载多个配置源</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">配置分层</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">Django Flask 扩展</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">支持 Redis 和 Vault</font>

<font style="color:rgba(0, 0, 0, 0.87);">在项目中新建配置文件</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.yml`

**<font style="color:rgba(0, 0, 0, 0.87);">settings.yml</font>**<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">：</font>

```yaml
foo: 1
bar: 2
```

<font style="color:rgba(0, 0, 0, 0.87);">新建配置模块</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`config.py`

**<font style="color:rgba(0, 0, 0, 0.87);">config.py</font>**<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">：</font>

```yaml
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=['settings.yml'],
)
```

<font style="color:rgba(0, 0, 0, 0.87);">新建一个</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`app.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件，使用配置</font>

**<font style="color:rgba(0, 0, 0, 0.87);">app.py</font>**<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">：</font>

```yaml
from config import settings

print(settings.FOO)
print(settings.BAR)
```

<font style="color:rgba(0, 0, 0, 0.87);">然后运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`python app.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">可以看到已经能够自动获取</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">配置文件中的值。</font>

<font style="color:rgba(0, 0, 0, 0.87);">增加本地配置文件</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`

**<font style="color:rgba(0, 0, 0, 0.87);">settings.local.yml</font>**<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">:</font>

```yaml
foo: 10
bar: 20
```

<font style="color:rgba(0, 0, 0, 0.87);">再次运行</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`python app.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，程序会自动获取</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。</font>

<font style="color:rgba(0, 0, 0, 0.87);">这是因为</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`Dynaconf`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">在初始化是传入了配置文件格式为</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，在加载配置时，会同时查找</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">的配置文件。 并将两个配置文件的内容合并，如果存在相同变量，</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">会覆盖</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">中的配置。</font>

### <font style="color:rgba(0, 0, 0, 0.87);">项目实践</font>
### <font style="color:rgba(0, 0, 0, 0.87);">Django 项目</font>
<font style="color:rgba(0, 0, 0, 0.87);">Dynaconf 可以搭配 Django 一起使用。虽然 Django 有自己的配置模块，但是并不灵活。</font>

<font style="color:rgba(0, 0, 0, 0.87);">搭配 Dynaconf ，可以启动层级配置，例如支持</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`Dev`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">、</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`prod`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">和</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`test`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">多种环境的配置，而且可以通过环境变量很方便的 修改配置，包括加载其他地方的配置。</font>

<font style="color:rgba(0, 0, 0, 0.87);">在 Django 项目的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">文件最后添加如下内容：</font>

```yaml
import dynaconf  # pylint: disable=wrong-import-position

settings = dynaconf.DjangoDynaconf(
    __name__,
    envvar_prefix='BLOG',
    settings_files=[
        BASE_DIR / 'settings.local.yml'
    ],
    environments=False,
    load_dotenv=True,
    ENVVAR_FOR_DYNACONF='BLOG_SETTINGS',
    includes=[
        Path(sys.prefix, 'etc', 'blog', 'settings.yml'),
    ]
)
```

<font style="color:rgba(0, 0, 0, 0.87);">当 Django 加载</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">模块的时候，会初始化 Dynaconf 。 Dynaconf 会将 Django 的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">对象中的配置加载到 Dynaconf 中， 然后将自身的所有配置再重新加载到 Django 的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">对象中。</font>

<font style="color:rgba(0, 0, 0, 0.87);">Dynaconf 不仅会加载配置文件，也会加载以</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`BLOG_`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">开头的环境变量。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">使用配置文件</font>
<font style="color:rgba(0, 0, 0, 0.87);">在初始化 Dynaconf 时，会加载项目根目录的</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.local.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">配置文件，此文件一般是开发时使用的本地配置，并且不应该被 Git 追踪。 在不同的开发人员使用或者不同的环境中，可以使用多样化的本地配置。对于需要统一的默认配置，直接放在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">中就可以了。</font>

<font style="color:rgba(0, 0, 0, 0.87);">同时还会读取</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`<sys.prefix>/etc/blog/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。这个一般作为生产环境的系统配置。如果使用的是系统 Python 环境，可能目录是在</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`/usr/local/etc/blog/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">，如果是虚拟环境，则可能是</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`/home/foo/.virtualenvs/blog-fxage/etc/blog/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。</font>

<font style="color:rgba(0, 0, 0, 0.87);">如果想自定义配置文件位置，可以通过设置环境变量</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`BLOG_SETTINGS=/tmp/settings.yml`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">指定 Dynaconf 加载文件的位置。</font>

```yaml
DEBUG: true

ALLOWED_HOSTS:
  - '*'

INSTALLED_APPS:
 - dynaconf_merge_unique   # 指示 Dynaconf 将 INSTALLED_APPS 与默认配置合并而不是覆盖，并且进行去重
 - debug_toolbar    # 指示 Dynaconf 将 debug_toolbar 添加到 INSTALLED_APPS 列表中

MIDDLEWARE:
 - dynaconf_merge_unique
 - debug_toolbar.middleware.DebugToolbarMiddleware

DATABASES:
  default:
    ENGINE: 'django.db.backends.mysql'
    NAME: blo
    USER: root
    PASSWORD: '000000'
    HOST: 127.0.0.1
    PORT: 3306

REST_FRAMEWORK:
  # 指示 Dynaconf 将 REST_FRAMEWORK 与默认配置合并，而不是覆盖
  dynaconf_merge_unique: true
  # 指示 Dynaconf 只修改 PAGE_SIZE 的值，其他不变
  PAGE_SIZE: 10
}
```

<font style="color:rgba(0, 0, 0, 0.87);">上述配置在 Dynaconf 读取后，可以覆盖</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`settings.py`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">中的默认配置。其中有几个点需要注意：</font>

+ <font style="color:rgba(0, 0, 0, 0.87);">如果直接文件中定义配置，会覆盖默认配置。</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">如果需要和默认配置合并，可以使用</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`dynaconf_merge`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。</font>

#### <font style="color:rgba(0, 0, 0, 0.87);">使用环境变量</font>
<font style="color:rgba(0, 0, 0, 0.87);">Dynaconf 支持加载环境变量，也可以使用 .env 文件。</font>

<font style="color:rgba(0, 0, 0, 0.87);">在使用环境变量时，同样和配置文件一样，支持完全覆盖，和自动合并。</font>

<font style="color:rgba(0, 0, 0, 0.87);">需要额外强调一点的是， Dynaconf 初始化的时候，使用了</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`envvar_prefix=BLOG`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。 Dynaconf 会自动加载以</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`BLOG_`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">开头的 环境变量。包括</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`ENVVAR_FOR_DYNACONF='BLOG_SETTINGS'`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">配置的 Dynaconf 加载配置文件的环境变量</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`BLOG_SETTINGS`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">。</font>

<font style="color:rgba(0, 0, 0, 0.87);">所以在使用环境变量的时候，不要错误的将</font><font style="color:rgba(0, 0, 0, 0.87);"> </font>`BLOG_SETTINGS`<font style="color:rgba(0, 0, 0, 0.87);"> </font><font style="color:rgba(0, 0, 0, 0.87);">环境变量指定其他内容，而造成不必要的错误。</font>

```yaml
# 使用环境变量配置单值
export BLOG_DEBUG='True'

# 使用环境变量配置对象
export BLOG_DATABASES="{'default'={'ENGINE'='django.db.backends.mysql', 'NAME'='blog', 'USER'='root', 'PASSWORD'='000000', 'HOST'='localhost', 'POST'=3306}}"

# 使用环境变量配置合并内容
export BLOG_MIDDLEWARE='["dynaconf_merge_unique", "debug_toolbar.middleware.DebugToolbarMiddleware"]'   # 使用 dynaconf_merge_unique 合并并去重
export BLOG_MIDDLEWARE='@merge ["debug_toolbar.middleware.DebugToolbarMiddleware"]' # 使用 merge 关键字
export BLOG_MIDDLEWARE='@merge debug_toolbar.middleware.DebugToolbarMiddleware' # 简写

export BLOG_REST_FRAMEWORK='{PAGE_SIZE=10, dynaconf_merge=true}'    # 使用 dynaconf_merge 合并
export BLOG_REST_FRAMEWORK='@merge {PAGE_SIZE=10}'  # 使用 merge 关键字
export BLOG_REST_FRAMEWORK='@merge PAGE_SIZE=10'    # 简写

export BLOG_DATABASES__default__PASSWORD='123456'   # 使用两个下划线 (__) 作为子级
```

