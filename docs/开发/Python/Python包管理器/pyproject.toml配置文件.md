### <font style="color:rgb(64, 64, 64);">1. </font>**<font style="color:rgb(64, 64, 64);">理解 </font>**`**<font style="color:rgb(64, 64, 64);">pyproject.toml</font>**`**<font style="color:rgb(64, 64, 64);"> 的核心作用</font>**
+ **<font style="color:rgb(64, 64, 64);">PEP 621 标准化</font>**<font style="color:rgb(64, 64, 64);">：</font>`<font style="color:rgb(64, 64, 64);">pyproject.toml</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">是 Python 社区推出的配置文件格式，旨在统一项目元数据（如名称、版本、依赖项）和构建系统的配置（如构建工具、插件）。</font>
+ **<font style="color:rgb(64, 64, 64);">替代传统文件</font>**<font style="color:rgb(64, 64, 64);">：逐渐取代</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">setup.py</font>`<font style="color:rgb(64, 64, 64);">、</font>`<font style="color:rgb(64, 64, 64);">setup.cfg</font>`<font style="color:rgb(64, 64, 64);">、</font>`<font style="color:rgb(64, 64, 64);">requirements.txt</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">等文件，成为现代 Python 项目的核心配置。</font>

---

### <font style="color:rgb(64, 64, 64);">2.</font><font style="color:rgb(64, 64, 64);"> </font>**<font style="color:rgb(64, 64, 64);">学习</font>****<font style="color:rgb(64, 64, 64);"> </font>**`**<font style="color:rgb(64, 64, 64);">pyproject.toml</font>**`**<font style="color:rgb(64, 64, 64);"> </font>****<font style="color:rgb(64, 64, 64);">的通用结构</font>**
**<font style="color:rgb(64, 64, 64);">基础部分</font>**<font style="color:rgb(64, 64, 64);">（PEP 621 标准）：</font>

```toml
[project]
name = "my_project"
version = "0.1.0"
dependencies = ["requests>=2.25"]
authors = [{name = "Your Name", email = "you@example.com"}]
```

**<font style="color:rgb(64, 64, 64);">构建系统</font>**<font style="color:rgb(64, 64, 64);">（定义构建工具）：</font>

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"
```

**<font style="color:rgb(64, 64, 64);">工具扩展配置</font>**<font style="color:rgb(64, 64, 64);">（如 Poetry、PDM、Black 等工具的专用配置）：</font>

```toml
[tool.poetry]
[tool.pdm]
[tool.uv]
```

---

### <font style="color:rgb(64, 64, 64);">3.</font><font style="color:rgb(64, 64, 64);"> </font>**<font style="color:rgb(64, 64, 64);">工具间的配置异同</font>**
| **工具** | **特点** | **配置兼容性** |
| --- | --- | --- |
| **<font style="color:rgb(64, 64, 64);">Poetry</font>** | <font style="color:rgb(64, 64, 64);">专注于依赖管理和打包，强锁定机制（</font>`<font style="color:rgb(64, 64, 64);">poetry.lock</font>`<br/><font style="color:rgb(64, 64, 64);">）</font> | <font style="color:rgb(64, 64, 64);">使用</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[tool.poetry]</font>`<br/><font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">定义元数据和依赖，不完全兼容 PEP 621，需手动对齐。</font> |
| **<font style="color:rgb(64, 64, 64);">PDM</font>** | <font style="color:rgb(64, 64, 64);">支持 PEP 621，依赖解析快，使用</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">__pypackages__</font>`<br/><font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">目录</font> | <font style="color:rgb(64, 64, 64);">完全兼容 PEP 621，配置在</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[project]</font>`<br/><font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">下，部分扩展在</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[tool.pdm]</font>`<br/><font style="color:rgb(64, 64, 64);">。</font> |
| **<font style="color:rgb(64, 64, 64);">UV</font>** | <font style="color:rgb(64, 64, 64);">由 Astral 开发，极速的依赖安装器，兼容</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">pip</font>`<br/><font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">和</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">pip-tools</font>` | <font style="color:rgb(64, 64, 64);">主要作为安装器，不直接管理</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">pyproject.toml</font>`<br/><font style="color:rgb(64, 64, 64);">，但可安装符合 PEP 621 标准的依赖。</font> |


+ **<font style="color:rgb(64, 64, 64);">共性</font>**<font style="color:rgb(64, 64, 64);">：</font>
    - <font style="color:rgb(64, 64, 64);">所有工具都支持</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[project]</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">中的 PEP 621 元数据（如</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">name</font>`<font style="color:rgb(64, 64, 64);">,</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">version</font>`<font style="color:rgb(64, 64, 64);">,</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">dependencies</font>`<font style="color:rgb(64, 64, 64);">）。</font>
    - <font style="color:rgb(64, 64, 64);">依赖解析逻辑类似（语义版本控制）。</font>
+ **<font style="color:rgb(64, 64, 64);">差异</font>**<font style="color:rgb(64, 64, 64);">：</font>
    - **<font style="color:rgb(64, 64, 64);">依赖格式</font>**<font style="color:rgb(64, 64, 64);">：Poetry 允许更灵活的版本语法（如</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">^1.2.3</font>`<font style="color:rgb(64, 64, 64);">），PDM 使用 PEP 440 标准。</font>
    - **<font style="color:rgb(64, 64, 64);">锁定文件</font>**<font style="color:rgb(64, 64, 64);">：Poetry 生成</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">poetry.lock</font>`<font style="color:rgb(64, 64, 64);">，PDM 生成</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">pdm.lock</font>`<font style="color:rgb(64, 64, 64);">，UV 支持</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">requirements.txt</font>`<font style="color:rgb(64, 64, 64);">。</font>
    - **<font style="color:rgb(64, 64, 64);">插件系统</font>**<font style="color:rgb(64, 64, 64);">：各工具可能有自定义配置（如</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[tool.poetry.scripts]</font>`<font style="color:rgb(64, 64, 64);">）。</font>

---

### <font style="color:rgb(64, 64, 64);">4.</font><font style="color:rgb(64, 64, 64);"> </font>**<font style="color:rgb(64, 64, 64);">学习路径建议</font>**
+ **<font style="color:rgb(64, 64, 64);">从 PEP 621 开始</font>**<font style="color:rgb(64, 64, 64);">：</font>
    1. <font style="color:rgb(64, 64, 64);">阅读</font><font style="color:rgb(64, 64, 64);"> </font>[PEP 621 文档](https://peps.python.org/pep-0621/)<font style="color:rgb(64, 64, 64);">，理解标准字段。</font>
    2. <font style="color:rgb(64, 64, 64);">手动编写一个简单的</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">pyproject.toml</font>`<font style="color:rgb(64, 64, 64);">（仅使用</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[project]</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">和</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[build-system]</font>`<font style="color:rgb(64, 64, 64);">）。</font>
+ **<font style="color:rgb(64, 64, 64);">选择工具并实践</font>**<font style="color:rgb(64, 64, 64);">：</font>

**<font style="color:rgb(64, 64, 64);">Poetry</font>**<font style="color:rgb(64, 64, 64);">：适合需要严格依赖锁定的项目。</font>

```plain
poetry init  # 生成 pyproject.toml
poetry add requests  # 添加依赖
```

**<font style="color:rgb(64, 64, 64);">PDM</font>**<font style="color:rgb(64, 64, 64);">：适合 PEP 621 原生支持的项目。</font>

```plain
pdm init    # 生成 pyproject.toml
pdm add requests
```

**<font style="color:rgb(64, 64, 64);">UV</font>**<font style="color:rgb(64, 64, 64);">：适合替代 </font>`<font style="color:rgb(64, 64, 64);">pip</font>`<font style="color:rgb(64, 64, 64);"> 提升安装速度。</font>

```toml
  uv pip install -r requirements.txt  # 兼容 pip 命令
```

+ **<font style="color:rgb(64, 64, 64);">对比迁移</font>**<font style="color:rgb(64, 64, 64);">：</font>
    - <font style="color:rgb(64, 64, 64);">尝试将一个项目的配置从 Poetry 迁移到 PDM，观察哪些字段需要修改。</font>
    - <font style="color:rgb(64, 64, 64);">使用</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">uv</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">安装基于不同工具的依赖，测试兼容性。</font>

---

### <font style="color:rgb(64, 64, 64);">5.</font><font style="color:rgb(64, 64, 64);"> </font>**<font style="color:rgb(64, 64, 64);">关键注意事项</font>**
+ **<font style="color:rgb(64, 64, 64);">工具锁文件不互通</font>**<font style="color:rgb(64, 64, 64);">：</font>`<font style="color:rgb(64, 64, 64);">poetry.lock</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">和</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">pdm.lock</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">格式不同，不能混用。</font>
+ **<font style="color:rgb(64, 64, 64);">构建系统差异</font>**<font style="color:rgb(64, 64, 64);">：如果使用</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">setuptools</font>`<font style="color:rgb(64, 64, 64);">、</font>`<font style="color:rgb(64, 64, 64);">flit</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">或</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">hatch</font>`<font style="color:rgb(64, 64, 64);">，需配置对应的</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">build-backend</font>`<font style="color:rgb(64, 64, 64);">。</font>
+ **<font style="color:rgb(64, 64, 64);">动态字段</font>**<font style="color:rgb(64, 64, 64);">：某些字段（如</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">version</font>`<font style="color:rgb(64, 64, 64);">）可以通过工具动态生成（如 Poetry 的</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">version = "0.0.0"</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">配合</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">poetry version</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">命令）。</font>

---

### <font style="color:rgb(64, 64, 64);">6.</font><font style="color:rgb(64, 64, 64);"> </font>**<font style="color:rgb(64, 64, 64);">总结</font>**
+ **<font style="color:rgb(64, 64, 64);">配置部分相通</font>**<font style="color:rgb(64, 64, 64);">：所有工具在 PEP 621 标准部分（</font>`<font style="color:rgb(64, 64, 64);">[project]</font>`<font style="color:rgb(64, 64, 64);">）是兼容的。</font>
+ **<font style="color:rgb(64, 64, 64);">工具扩展不互通</font>**<font style="color:rgb(64, 64, 64);">：如</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[tool.poetry]</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">和</font><font style="color:rgb(64, 64, 64);"> </font>`<font style="color:rgb(64, 64, 64);">[tool.pdm]</font>`<font style="color:rgb(64, 64, 64);"> </font><font style="color:rgb(64, 64, 64);">是各自专用的。</font>
+ **<font style="color:rgb(64, 64, 64);">学习核心逻辑后，工具可快速切换</font>**<font style="color:rgb(64, 64, 64);">：理解 PEP 621 后，只需熟悉各工具的扩展语法即可。</font>

