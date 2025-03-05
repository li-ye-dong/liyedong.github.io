<font style="color:rgb(82, 82, 82);">IDE都会有一套生成新项目的向导（Wizard），通过点点点，就可以得到一个可以运行的某类程序。 这样的程序，具备了推荐的项目结构，配置的基本的编译、打包、测试，尽管功能只是一个</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">helloworld</font>`<font style="color:rgb(82, 82, 82);">。 这个功能，极大地降低了初学者的进入门槛，也统一了某类项目的文件结构，是一个了不起的进步。 最早使用这类手段的，似乎是Visual Studio。</font>

<font style="color:rgb(82, 82, 82);">令人惋惜的是，Python的IDE——PyCharm并不自带这个功能。 这其中，也有Python项目千变万化的因素。 Python的适用范围太广，从桌面到服务器，从游戏到数据分析，都做一套显然投入太大。 而Python又是一门解释型语言，随便写个文件也能直接执行，似乎没有这个必要。</font>

<font style="color:rgb(82, 82, 82);">然而，我要说，还是有必要的！</font>

<font style="color:rgb(82, 82, 82);">因为Python系缺失一个Wizard，也缺少项目结构的标准，于是出现了</font>[<font style="color:rgb(82, 82, 82);">cookiecutter</font>](https://github.com/audreyr/cookiecutter)<font style="color:rgb(82, 82, 82);">。 这是一个项目生成器，也可称为引擎，因为它只完成了最核心的功能。 真正决定一个项目长什么样的模板，却可以自由定制。 也因此，它能生成任何一种语言的项目。</font>

## <font style="color:rgb(82, 82, 82);">1. 快速安装</font>
```shell
$ pip install cookiecutter
```

[<font style="color:rgb(82, 82, 82);">cookiecutter</font>](https://github.com/audreyr/cookiecutter)<font style="color:rgb(82, 82, 82);">就是一个已经发布的Python包，因此用Python的手段可以直接安装。</font>

<font style="color:rgb(82, 82, 82);">对于非Python系的程序员来说，也可以使用包管理器的方式安装。</font>

```shell
# For Mac
$ brew install cookiecutter
# For Debian/Ubuntu
$ sudo apt install cookiecutter
```

## <font style="color:rgb(82, 82, 82);">2. 如何使用</font>
<font style="color:rgb(82, 82, 82);">首先，寻找一个合适的</font>[<font style="color:rgb(82, 82, 82);">cookiecutter</font>](https://github.com/audreyr/cookiecutter)<font style="color:rgb(82, 82, 82);">项目。 最主要的方式，就是访问其GitHub主页的</font>[<font style="color:rgb(82, 82, 82);">A Pantry Full of Cookiecutters</font>](https://github.com/audreyr/cookiecutter/tree/db14e06a1dcc0187beeafde72685c3acef93eb68#a-pantry-full-of-cookiecutters)<font style="color:rgb(82, 82, 82);">。</font>

<font style="color:rgb(82, 82, 82);">如果挑选完毕（这里以</font>[<font style="color:rgb(82, 82, 82);">cookiecutter-pypackage</font>](https://github.com/audreyr/cookiecutter-pypackage)<font style="color:rgb(82, 82, 82);">为例），则可直接执行</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">cookiecutter</font>`<font style="color:rgb(82, 82, 82);">生成项目。</font>

```shell
$ cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
full_name [Yan QiDong]:
email [yanqd0@outlook.com]:
github_username [yanqd0]:
project_name [Python Boilerplate]: trycookie
project_slug [trycookie]:
project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: A description
pypi_username [yanqd0]:
version [0.1.0]:
use_pytest [n]:
use_pypi_deployment_with_travis [y]:
add_pyup_badge [n]:
Select command_line_interface:
1 - Click
2 - No command-line interface
Choose from 1, 2 (1, 2) [1]:
create_author_file [y]:
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]:
```

<font style="color:rgb(82, 82, 82);">在项目生成过程中，会产生一些提示，需要输入对应信息。 这和各类Wizard的GUI中，填写项目名、包名什么的，是同类操作。 以上是，除了项目名叫</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">trycookie</font>`<font style="color:rgb(82, 82, 82);">，基本都选默认的一个结果。</font>

<font style="color:rgb(82, 82, 82);">查看项目结构：</font>

```shell
$ tree -a trycookie
trycookie
├── .editorconfig
├── .github
│   └── ISSUE_TEMPLATE.md
├── .gitignore
├── .travis.yml
├── AUTHORS.rst
├── CONTRIBUTING.rst
├── HISTORY.rst
├── LICENSE
├── MANIFEST.in
├── Makefile
├── README.rst
├── docs
│   ├── Makefile
│   ├── authors.rst
│   ├── conf.py
│   ├── contributing.rst
│   ├── history.rst
│   ├── index.rst
│   ├── installation.rst
│   ├── make.bat
│   ├── readme.rst
│   └── usage.rst
├── requirements_dev.txt
├── setup.cfg
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_trycookie.py
├── tox.ini
└── trycookie
├── __init__.py
├── cli.py
└── trycookie.py

4 directories, 30 files
```

<font style="color:rgb(82, 82, 82);">如此庞大而复杂的一个项目结构，融合了作者</font>[<font style="color:rgb(82, 82, 82);">audreyr</font>](https://github.com/audreyr)<font style="color:rgb(82, 82, 82);">对一个开源PyPI项目的理解。 虽然未必适用于任何一个人，但对于什么也不懂的菜鸟来说，却无疑是福音。</font>

## <font style="color:rgb(82, 82, 82);">3. 基本原理</font>
[<font style="color:rgb(82, 82, 82);">cookiecutter</font>](https://github.com/audreyr/cookiecutter)<font style="color:rgb(82, 82, 82);">的工作原理，是先下载一个模板项目，然后替换模板项目的某些内容，生成新的项目。 在以上的示例中，</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">https://github.com/audreyr/cookiecutter-pypackage.git</font>`<font style="color:rgb(82, 82, 82);">就是一个项目的Git链接。 这可以换成任何一个可以用</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">git clone</font>`<font style="color:rgb(82, 82, 82);">来下载的链接，包括各种私有Git托管平台。</font>

<font style="color:rgb(82, 82, 82);">如果是GitHub，还可以用以下的等效形式：</font>

```shell
cookiecutter gh:audreyr/cookiecutter-pypackage
```

[<font style="color:rgb(82, 82, 82);">cookiecutter</font>](https://github.com/audreyr/cookiecutter)<font style="color:rgb(82, 82, 82);">的简短形式，支持以下三种平台。</font>

| <font style="color:rgb(82, 82, 82);">Platform</font> | <font style="color:rgb(82, 82, 82);">abbreviation</font> |
| --- | --- |
| [<font style="color:rgb(82, 82, 82);">GitHub</font>](https://github.com/) | `<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">gh</font>` |
| [<font style="color:rgb(82, 82, 82);">BitBucket</font>](https://bitbucket.org/) | `<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">bb</font>` |
| [<font style="color:rgb(82, 82, 82);">GitLab</font>](https://gitlab.com/) | `<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">gl</font>` |


[<font style="color:rgb(82, 82, 82);">cookiecutter</font>](https://github.com/audreyr/cookiecutter)<font style="color:rgb(82, 82, 82);">也支持Mercurial（</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">hg</font>`<font style="color:rgb(82, 82, 82);">）。</font>

```shell
cookiecutter hg+ssh://hg@bitbucket.org/audreyr/cookiecutter-pypackage
```

<font style="color:rgb(82, 82, 82);">使用过模板的项目，默认都已经被下载到</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">~/.cookiecutter</font>`<font style="color:rgb(82, 82, 82);">目录下。 如果需要再次使用，而又无需更新，可以直接用项目名。</font>

```shell
cookiecutter cookiecutter-pypackage
```

<font style="color:rgb(82, 82, 82);">利用这个特点，可以先用各种手段，把模板项目下载到</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">~/.cookiecutter</font>`<font style="color:rgb(82, 82, 82);">目录下，再来使用。</font>

<font style="color:rgb(82, 82, 82);">参考：</font>[<font style="color:rgb(82, 82, 82);">Usage — cookiecutter 1.6.0 documentation</font>](https://cookiecutter.readthedocs.io/en/latest/usage.html)

## <font style="color:rgb(82, 82, 82);">4. 配置文件</font>
<font style="color:rgb(82, 82, 82);">默认情况下，</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">~/.cookiecutterrc</font>`<font style="color:rgb(82, 82, 82);">就是配置文件。 它实际上是一个YAML文件。 以下是孤的配置文件示例。</font>

```shell
# vim: set filetype=yaml:

default_context:
full_name: "Yan QiDong"
email: "yanqd0@outlook.com"
github_username: "yanqd0"
cookiecutters_dir: "~/.cookiecutters/"
abbreviations:
pp: https://github.com/audreyr/cookiecutter-pypackage.git
gh: https://github.com/{0}.git
```

<font style="color:rgb(82, 82, 82);">可配置项中，</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">default_context</font>`<font style="color:rgb(82, 82, 82);">是设置生成项目时，一些提示信息的默认参数。</font><font style="color:rgb(82, 82, 82);"> </font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">cookiecutters_dir</font>`<font style="color:rgb(82, 82, 82);">则是项目的下载位置，一般默认就好。</font><font style="color:rgb(82, 82, 82);"> </font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">abbreviations</font>`<font style="color:rgb(82, 82, 82);">是自定义简短形式，属于高级定制功能，仅适用于重度用户。 通常，填一填</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">default_context</font>`<font style="color:rgb(82, 82, 82);">就好。</font>

<font style="color:rgb(82, 82, 82);">如果对</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">~/.cookiecutterrc</font>`<font style="color:rgb(82, 82, 82);">这个配置文件的名称和位置不满意， 可以通过环境变量</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">COOKIECUTTER_CONFIG</font>`<font style="color:rgb(82, 82, 82);">， 或者在命令行指定参数</font>`<font style="color:rgb(82, 82, 82);background-color:rgb(247, 247, 247);">--config-file</font>`<font style="color:rgb(82, 82, 82);">来指定新的配置文件。</font>

<font style="color:rgb(82, 82, 82);">参考：</font>[<font style="color:rgb(82, 82, 82);">User Config (0.7.0+) — cookiecutter 1.6.0 documentation</font>](https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html)

<font style="color:rgb(82, 82, 82);"></font>

## <font style="color:rgb(82, 82, 82);">5.文档使用</font>
#### <font style="color:rgb(31, 35, 40);">快速启动</font>
<font style="color:rgb(31, 35, 40);">将Cookiecutter用作命令行实用程序的推荐方法是使用</font>[<font style="color:rgb(31, 35, 40);">pipx</font>](https://pypa.github.io/pipx/)<font style="color:rgb(31, 35, 40);">运行它，它可以使用</font>`<font style="color:rgb(31, 35, 40);">pip install pipx</font>`<font style="color:rgb(31, 35, 40);">安装，但如果您计划以编程方式使用Cookiecutter，请运行</font>`<font style="color:rgb(31, 35, 40);">pip install cookiecutter</font>`<font style="color:rgb(31, 35, 40);">。</font>

**<font style="color:rgb(31, 35, 40);">使用GitHub模板</font>**

```plain
# You'll be prompted to enter values.
# Then it'll create your Python package in the current working directory,
# based on those values.
# For the sake of brevity, repos on GitHub can just use the 'gh' prefix
$ pipx run cookiecutter gh:audreyfeldroy/cookiecutter-pypackage
```

**<font style="color:rgb(31, 35, 40);">使用本地模板</font>**

```shell
$ pipx run cookiecutter cookiecutter-pypackage/
```

**<font style="color:rgb(31, 35, 40);">从Python使用它</font>**

```python
from cookiecutter.main import cookiecutter

# Create project from the cookiecutter-pypackage/ template
cookiecutter('cookiecutter-pypackage/')

# Create project from the cookiecutter-pypackage.git repo template
cookiecutter('gh:audreyfeldroy//cookiecutter-pypackage.git')
```

#### <font style="color:rgb(31, 35, 40);">详细使用</font>
+ <font style="color:rgb(31, 35, 40);">从本地或远程模板生成项目。</font>
+ <font style="color:rgb(31, 35, 40);">使用</font>`<font style="color:rgb(31, 35, 40);">cookiecutter.json</font>`<font style="color:rgb(31, 35, 40);">提示自定义项目。</font>
+ <font style="color:rgb(31, 35, 40);">使用pre-prompt，pre-and post-generate hooks。</font>

[<font style="color:rgb(31, 35, 40);">了解更多</font>](https://cookiecutter.readthedocs.io/en/latest/usage.html)

### <font style="color:rgb(31, 35, 40);">对于模板创建者</font>
+ <font style="color:rgb(31, 35, 40);">利用无限的目录嵌套。</font>
+ <font style="color:rgb(31, 35, 40);">使用Jinja2满足所有模板需求。</font>
+ <font style="color:rgb(31, 35, 40);">使用</font>`<font style="color:rgb(31, 35, 40);">cookiecutter.json</font>`<font style="color:rgb(31, 35, 40);">轻松定义模板变量。</font>

[<font style="color:rgb(31, 35, 40);">了解更多</font>](https://cookiecutter.readthedocs.io/en/latest/tutorials/)

## <font style="color:rgb(31, 35, 40);">可用模板</font>
<font style="color:rgb(31, 35, 40);">在</font>[<font style="color:rgb(31, 35, 40);">GitHub</font>](https://github.com/search?q=cookiecutter&type=Repositories)<font style="color:rgb(31, 35, 40);">上发现各种现成的模板。</font>

### <font style="color:rgb(31, 35, 40);">特殊模板</font>
+ [<font style="color:rgb(31, 35, 40);">cookiecutter-pypackage</font>](https://github.com/audreyfeldroy/cookiecutter-pypackage)
+ [<font style="color:rgb(31, 35, 40);">cookiecutter-django</font>](https://github.com/pydanny/cookiecutter-django)
+ [<font style="color:rgb(31, 35, 40);">cookiecutter-pytest-plugin</font>](https://github.com/pytest-dev/cookiecutter-pytest-plugin)
+ [<font style="color:rgb(31, 35, 40);">cookiecutter-plone-starter</font>](https://github.com/collective/cookiecutter-plone-starter)

## <font style="color:rgb(82, 82, 82);">5. 总结一下</font>
[<font style="color:rgb(82, 82, 82);">cookiecutter</font>](https://github.com/audreyr/cookiecutter)<font style="color:rgb(82, 82, 82);">是一个简单好用的项目生成器引擎，并且已经有很多各种类型的模板。 除了Python项目，还有很多其它语言的项目模板。 它可以极大地省去一个项目初始化的重复劳动，也可以帮助菜鸟程序员成长。</font>

<font style="color:rgb(82, 82, 82);">当然，如果不满意，还是可以自己修改、定制模板的。</font>

