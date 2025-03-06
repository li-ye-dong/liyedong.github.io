# GithubPage搭建博客
## <font style="color:rgb(79, 79, 79);">什么是Mkdocs</font>
[<font style="color:rgb(25, 27, 31);">Material for MkDocs</font>](https://link.zhihu.com/?target=https%3A//squidfunk.github.io/mkdocs-material/)<font style="color:rgb(25, 27, 31);"> 是 MkDocs的一个主题配置，同时也是一个功能齐全的静态网站生成工具，能够解决上面提到的GitHub Pages的问题。</font>

<font style="color:rgb(25, 27, 31);">Material for MkDocs 使用广泛，下面是一些大公司和知名开源项目的使用例子：</font>

+ [<font style="color:rgb(25, 27, 31);">AWS Copilot CLI</font>](https://link.zhihu.com/?target=https%3A//aws.github.io/copilot-cli/)
+ [<font style="color:rgb(25, 27, 31);">Google Accompanist</font>](https://link.zhihu.com/?target=https%3A//google.github.io/accompanist/)
+ [<font style="color:rgb(25, 27, 31);">MicroSoft Code With Engineering Playbook</font>](https://link.zhihu.com/?target=https%3A//microsoft.github.io/code-with-engineering-playbook/)
+ [<font style="color:rgb(25, 27, 31);">Mozilla Foundation Engineering Handbook</font>](https://link.zhihu.com/?target=https%3A//mozillafoundation.github.io/engineering-handbook/)
+ [<font style="color:rgb(25, 27, 31);">Netflix Titus</font>](https://link.zhihu.com/?target=https%3A//netflix.github.io/titus/)
+ [<font style="color:rgb(25, 27, 31);">CentOS Infra docs</font>](https://link.zhihu.com/?target=https%3A//docs.infra.centos.org/)
+ [<font style="color:rgb(25, 27, 31);">electron-builder</font>](https://link.zhihu.com/?target=https%3A//www.electron.build/)
+ [<font style="color:rgb(25, 27, 31);">Kubernetes</font>](https://link.zhihu.com/?target=https%3A//kops.sigs.k8s.io/)

<font style="color:rgb(25, 27, 31);">虽然我还没有比较复杂的开源项目需要用mkdocs-material来管理文档，但看到GitHub Pages的一些限制，最近有空还是学了一下这个工具，以备后续项目中使用。这里做一些简单记录，方便以后查找。</font>

<font style="color:rgb(25, 27, 31);">需要说明的是，Material for MkDocs 是一个比较复杂的工具，很多配置项这里没有提到，根据需要在官方</font>[<font style="color:rgb(25, 27, 31);">Setup</font>](https://link.zhihu.com/?target=https%3A//squidfunk.github.io/mkdocs-material/setup/)<font style="color:rgb(25, 27, 31);">文档中查看使用说明。</font>

<font style="color:rgb(25, 27, 31);">另外一种学习配置的方式是直接查看上面提到的开源项目源码根目录下的</font>`<font style="color:rgb(25, 27, 31);background-color:rgb(248, 248, 250);">mkdocs.yml</font>`<font style="color:rgb(25, 27, 31);">文件，复制这个文件过去，就能得到类似的布局效果。</font>

<font style="color:rgb(25, 27, 31);">这个教程里面的示例页面：</font>[<font style="color:rgb(25, 27, 31);">https://vra.github.io/mkdocs-material-example/</font>](https://link.zhihu.com/?target=https%3A//vra.github.io/mkdocs-material-example/)

<font style="color:rgb(25, 27, 31);">示例页面的配置文件：</font>[<font style="color:rgb(25, 27, 31);">https://github.com/vra/mkdocs-m</font>](https://link.zhihu.com/?target=https%3A//github.com/vra/mkdocs-material-example/blob/main/mkdocs.yml)

## <font style="color:rgb(25, 27, 31);">使用</font>
<font style="color:rgba(0, 0, 0, 0.87);">在完成</font>[<font style="color:rgba(0, 0, 0, 0.87);">Material for MkDocs的安装</font>](https://mkdoc-material.llango.com/getting-started/)<font style="color:rgba(0, 0, 0, 0.87);">后，可以使用</font>`mkdocs`<font style="color:rgba(0, 0, 0, 0.87);">相关命令来启动文档。转到要放置项目的目录，然后输入：</font>

```plain
mkdocs new .
```

<font style="color:rgba(0, 0, 0, 0.87);">如果你正在使用的是Docker中的Material for MkDocs，则使用以下命令：</font>

- [x] **Unix**

```plain
docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material new .
```

- [x] **Windows**

<font style="color:rgba(0, 0, 0, 0.87);">以上操作会新建以下结构的文件：</font>

```plain
.
├─ docs/
│  └─ index.md
└─ mkdocs.yml
```

## <font style="color:rgba(0, 0, 0, 0.87);">配置</font>[<font style="color:rgba(0, 0, 0, 0.87);">¶</font>](https://mkdoc-material.llango.com/creating-your-site/#_2)
```yaml
#[Info]
site_name: liyedong Docs   #网站名字
site_description: the notes record by liyedong
site_author: liyedong #作者名
site_url: https://li-ye-dong.github.io/  #网站地址
copyright: Copyright &copy; 2024 liyedong # 左下角的版权声明

# [Navigtion]
nav:
  - Home: index.md
  - Redis: 
    - redis/Redis学习.md
    #- 设计模式: java/设计模式/index.md
  - Dokcer:
    - docker/docker笔记.md
 #   - Installation: guide/installation.md
 #   - Basics: guide/basics.md
 #   - Configuration: guide/config.md
  - Nginx:
    - nginx/Nginx学习.md

#[UI]
theme:
  name: material
  language: zh # 一些提示性的文字会变成中文
  font:
    text: Roboto
    code: Roboto Mono
  features:
    - header.autohide  #自动隐藏
    #- announce.dismiss #呈现可标记为由用户读取的临时公告，可以包含一个用于取消当前公告的按钮
    - navigation.instant #自动隐藏
    - navigation.tracking #地址栏中的 URL 将自动更新为在目录中突出显示的活动锚点
    - content.code.annotate
    - toc.integrate
    - toc.follow
    - navigation.path
    - navigation.top # 返回顶部的按钮 在上滑时出现
    - navigation.tabs
    - navigation.prune
    - navigation.footer
    - navigation.tabs.sticky  #启用粘性选项卡后，导航选项卡将锁定在标题下方，并在向下滚动时始终保持可见
    - navigation.sections #启用部分后，顶级部分在边栏中呈现为1220px以上视口的组，但在移动设备上保持原样
    # - navigation.expand # 打开Tab时左侧目录全部展开
    - content.code.copy
    - navigation.indexes #启用节索引页后，可以将文档直接附加到节
    - search.share #搜索分享按钮
    - search.suggest # 搜索输入一些字母时推荐补全整个单词
    - search.highlight # 搜索出的文章关键词加入高亮
  palette: 
    # Palette toggle for light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default # 日间模式
      toggle:
        icon: material/brightness-7  # 图标
        name: Switch to dark mode
      primary: deep ## 上方的, [red, pink, purple, deep, purple, indigo, blue, light blue, cyan, teal, green, light green, lime, yellow, amber, orange, deep orange, brown, grey, blue, grey, black, white]
      accent: deep # # 链接等可交互元件的高亮色 [red, pink, purple, deep, purple, indigo, blue, light, blue, cyan, teal, green, light, green, lime, yellow, amber, orange, deep orange]

    # Palette toggle for dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate # 夜间模式
      primary: deep #, [red, pink, purple, deep, purple, indigo, blue, light blue, cyan, teal, green, light green, lime, yellow, amber, orange, deep orange, brown, grey, blue, grey, black, white]
      accent: deep # [red, pink, purple, deep, purple, indigo, blue, light, blue, cyan, teal, green, light, green, lime, yellow, amber, orange, deep orange]
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
    
  icon: 
    repo: fontawesome/brands/github #右上角图标
repo_name: li-ye-dong.github.io # 右上角的名
repo_url: https://github.com/li-ye-dong/liyedong.github.io.git # 右上角点击跳转的链接


markdown_extensions:
  - admonition
  - abbr
  - pymdownx.caret    
  - pymdownx.details
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.tilde
  - pymdownx.tabbed:
      alternate_style: true 
  - md_in_html
  - pymdownx.arithmatex:  # latex支持
      generic: true
  - toc:
      permalink: true # 固定标题位置为当前位置
      title: On this page
  - pymdownx.highlight: # 代码块高亮
      anchor_linenums: true
      # linenums: true # 显示行号
      # auto_title: true # 显示编程语言名称
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - attr_list
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
  - pymdownx.superfences # 代码块高亮插件
  - meta # 支持Markdown文件上方自定义标题标签等
  - tables
     
extra_javascript:
  - javascripts/extra.js
  - javascripts/mathjax.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
extra_css:
  - stylesheets/extra.css


extra:
  generator: false  #删除页脚显示“使用 MkDocs 材料制造”
 # social:
  #  - icon: fontawesome/brands/twitter 
  #    link: https://twitter.com/
  #  - icon: fontawesome/brands/github
  #    link: https://github.com/
  #  - icon: fontawesome/brands/bilibili
  #    link: https://space.bilibili.com/
  #  - icon: fontawesome/solid/paper-plane
  #    link: mailto:<xxxxxx@qq.com> #联系方式
  #
  
#  analytics: 
#    provider: google
#    property: G-XXXXXXXXXX # Google Analytics ID
#    feedback:
#      title: 此页面有帮助吗？
#      ratings:
#        - icon: material/thumb-up-outline
#          name: This page was helpful
#          data: 1
#          note: >-
#            谢谢你的反馈！
#        - icon: material/thumb-down-outline
#          name: This page could be improved
#          data: 0
#          note: >- 
#            Thanks for your feedback! Help us improve this page by
#            using our <a href="https://marketingplatform.google.com/about/analytics/" target="_blank" rel="noopener">feedback form</a>.
#  
#  consent:
#    title: Cookie consent
#    description: >- 
#      我们也使用cookies来识别您的重复访问和偏好来衡量我们文档的有效性以及用户是否找到他们要找的东西。
#      如果你同意,你可以帮助我们让我们的网站更好


# plugins:
  # - search
  # - tags:
      # tags_file: tag.md #标签

```

### <font style="color:rgba(0, 0, 0, 0.87);">最小配置</font>[<font style="color:rgba(0, 0, 0, 0.87);">¶</font>](https://mkdoc-material.llango.com/creating-your-site/#_3)
<font style="color:rgba(0, 0, 0, 0.87);">只需要简单的添加以下几行内容到</font>`mkdocs.yml`<font style="color:rgba(0, 0, 0, 0.87);">即可启用主题。请注意，由于有几种不同的</font>[<font style="color:rgba(0, 0, 0, 0.87);">安装</font>](https://mkdoc-material.llango.com/creating-your-site/getting-started.md/#_2)<font style="color:rgba(0, 0, 0, 0.87);">方法，因此配置可能会略有不同：</font>

- [x] **pip, docker**

```plain
theme:
  name: material
```

- [x] **git**

_<font style="color:rgba(0, 0, 0, 0.87);">如果是从GitHub克隆的MkDocs from GitHub，那么应当列出所有主题的默认项，因为</font>_[_<font style="color:rgba(0, 0, 0, 0.87);">mkdocs_theme.yml</font>_](https://github.com/squidfunk/mkdocs-material/blob/master/src/mkdocs_theme.yml)_<font style="color:rgba(0, 0, 0, 0.87);">不会作为</font>_[_<font style="color:rgba(0, 0, 0, 0.87);">官方的描述文件</font>_](https://www.mkdocs.org/user-guide/custom-themes/#creating-a-custom-theme)_<font style="color:rgba(0, 0, 0, 0.87);">被自动载入</font>_

### <font style="color:rgba(0, 0, 0, 0.87);">高级设置</font>[<font style="color:rgba(0, 0, 0, 0.87);">¶</font>](https://mkdoc-material.llango.com/creating-your-site/#_4)
<font style="color:rgba(0, 0, 0, 0.87);">Material for MkDocs包含许多可配置项，_设置_章节有如何设置或者自定义颜色、字体、图标等等的详细说明。</font>

+ [<font style="color:rgba(0, 0, 0, 0.87);">修改颜色</font>](https://mkdoc-material.llango.com/setup/changing-the-colors/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">修改字体</font>](https://mkdoc-material.llango.com/setup/changing-the-fonts/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">修改语言</font>](https://mkdoc-material.llango.com/setup/changing-the-language/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">修改logo图片和icon图标</font>](https://mkdoc-material.llango.com/setup/changing-the-logo-and-icons/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">设置导航</font>](https://mkdoc-material.llango.com/setup/setting-up-navigation/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">设置站内搜索</font>](https://mkdoc-material.llango.com/setup/setting-up-site-search/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">设置访问统计</font>](https://mkdoc-material.llango.com/setup/setting-up-site-analytics/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">设置versioning</font>](https://mkdoc-material.llango.com/setup/setting-up-versioning/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">设置头部(header)</font>](https://mkdoc-material.llango.com/setup/setting-up-the-header/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">设置底部(footer)</font>](https://mkdoc-material.llango.com/setup/setting-up-the-footer/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">添加Github库(repository)</font>](https://mkdoc-material.llango.com/setup/adding-a-git-repository/)
+ [<font style="color:rgba(0, 0, 0, 0.87);">添加评论系统</font>](https://mkdoc-material.llango.com/setup/adding-a-comment-system/)

## <font style="color:rgba(0, 0, 0, 0.87);">预览</font>[<font style="color:rgba(0, 0, 0, 0.87);">¶</font>](https://mkdoc-material.llango.com/creating-your-site/#_5)
<font style="color:rgba(0, 0, 0, 0.87);">MkDocs包含一个试试预览的服务，所有可以在撰写文档的过程中进行实时预览。当文档修改保存后，这个服务会自动重建整个网站的文档。使用以下命令启动：</font>

```plain
mkdocs serve
```

<font style="color:rgba(0, 0, 0, 0.87);">如果使用的是Docker中的Material for MkDocs，则使用以下命令：</font>

- [x] **Unix**

```plain
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

- [x] **Windows**

<font style="color:rgba(0, 0, 0, 0.87);">浏览器打开</font>[<font style="color:rgba(0, 0, 0, 0.87);">localhost:8000</font>](http://localhost:8000/)<font style="color:rgba(0, 0, 0, 0.87);"></font>

## <font style="color:rgb(25, 27, 31);">配置自动化</font>
新建.github/workflows/static.yml

```javascript
# Simple workflow for deploying static content to GitHub Pages
name: Deploy static content to Pages

on:
  # Runs on pushes targeting the default branch
  push:
    branches: ["master"]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
# However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Single deploy job since we're just deploying
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v5
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          # Upload entire repository
          path: '.'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

部署完成后访问

[github.io](https://li-ye-dong.github.io/liyedong.github.io/site/)

或者使用

```javascript
name: ci 
on:
  push:
    branches:
      - master # 根据实际的分支情况设置
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest 
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v3
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material 
      - run: mkdocs gh-deploy --force

```

这个yml文件编写后，push到远程仓库后，会直接运行镜像，部署静态页面。



