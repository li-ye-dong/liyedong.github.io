# liyedong.github.io

为了使用 Poetry 进行管理，并通过 `build.cmd` 和 `serve.cmd` 进行构建和预览 MkDocs 生成的静态页面，你可以按照以下步骤来配置：

### 1. 使用 Poetry 管理依赖

首先，确保你已经通过 Poetry 安装了 MkDocs 和其他相关依赖：

```bash
poetry install
```

### 2. `build.cmd`：构建静态页面

`build.cmd` 脚本将执行 `mkdocs build`，并生成静态文件到 `site` 目录。以下是该脚本的内容：

### 3. `serve.cmd`：本地预览静态页面

`serve.cmd` 脚本将启动一个本地开发服务器，用于预览 `site` 目录中的静态页面。以下是该脚本的内容：

### 4. 使用步骤

- **构建静态页面：** 双击 `build.cmd`，将会自动在 `site` 目录下生成 MkDocs 的静态 HTML 页面。
- **预览静态页面：** 双击 `serve.cmd`，会启动一个本地开发服务器，默认在浏览器中访问 `http://127.0.0.1:8000` 来预览你生成的静态网站。

### 注意事项

这样，通过 `build.cmd` 和 `serve.cmd`，你可以方便地管理 MkDocs 项目，构建静态页面并在本地预览。