## 一、`apt` 常用命令
| 分类 | 命令示例 | 说明 |
| --- | --- | --- |
| **更新索引** | `sudo apt update` | 更新本地软件包列表，使系统能识别最新可用版本 |
| **升级软件** | `sudo apt upgrade` | 升级所有已安装的软件包（不移除任何包） |
| **彻底升级** | `sudo apt full-upgrade` | 升级并根据需要自动添加或移除依赖包 |
| **安装软件** | `sudo apt install <package>` | 安装指定软件包及其依赖 |
| **下载包文件** | `apt download <package>` | 仅下载 `.deb`<br/> 包文件到当前目录，不执行安装 |
| **卸载软件** | `sudo apt remove <package>` | 卸载指定软件包，但保留其配置文件 |
| **彻底卸载** | `sudo apt purge <package>` | 卸载软件包并删除所有相关配置文件 |
| **清理依赖** | `sudo apt autoremove` | 自动移除不再被任何软件包依赖的孤立包 |
| **清理缓存** | `sudo apt autoclean`<br/>`sudo apt clean` | `autoclean`<br/> 删除旧版本包缓存；`clean`<br/> 删除所有下载的包缓存 |
| **搜索软件** | `apt search <关键词>` | 在已配置的仓库中按名称或描述搜索软件包 |
| **查看信息** | `apt show <package>` | 显示软件包的详细信息（版本、依赖、维护者、描述等） |
| **列出已装** | `apt list --installed` | 列出所有已安装的软件包 |
| **列出可升** | `apt list --upgradable` | 列出当前可升级的软件包 |
| **编辑源** | `sudo apt edit-sources` | 用编辑器打开 `/etc/apt/sources.list`<br/> 及 `/etc/apt/sources.list.d/` |


---

## 二、`dpkg` 常用命令
| 分类 | 命令示例 | 说明 |
| --- | --- | --- |
| **安装本地包** | `sudo dpkg -i <file>.deb` | 安装当前目录下的本地 `.deb`<br/> 包（不处理远程依赖） |
| **卸载软件（保配置）** | `sudo dpkg -r <package>` | 卸载软件包，但保留其配置文件 |
| **彻底卸载** | `sudo dpkg -P <package>` | 卸载软件包并删除所有相关配置文件 |
| **列出已装** | `dpkg -l`<br/> 或 `dpkg-query -l` | 显示系统中所有已安装的软件包及其状态 |
| **查看状态** | `dpkg -s <package>` | 查看已安装软件包的状态、版本和描述 |
| **列出文件** | `dpkg -L <package>` | 列出指定软件包安装到系统的所有文件路径 |
| **查看包内容** | `dpkg -c <file>.deb` | 列出本地 `.deb`<br/> 包中的文件列表 |
| **文件归属查询** | `dpkg -S <file>` | 查询某个文件属于哪个已安装的软件包 |
| **修复配置** | `sudo dpkg --configure -a` | 对所有已解包但未配置的软件包执行配置操作 |
| **导出选中状态** | `dpkg --get-selections > selections.txt` | 导出当前软件包的“安装/未安装”状态，用于备份或批量恢复 |


---

**使用建议**

+ 先用 `sudo apt update` + `sudo apt upgrade` 保持系统最新；
+ 如遇依赖问题，先用 `sudo apt -f install` 尝试修复；
+ 本地 `.deb` 安装前可用 `dpkg -c` 查看包内文件，避免与系统文件冲突；
+ 定期执行 `sudo apt autoremove` 清理孤立包，保持系统整洁。

希望这份日常使用笔记，能帮助您在 Debian 系统上快速、精准地完成软件包管理。





##  三、aptitude、apt-get和 apt 命令  
下面是三个包管理工具的日常使用笔记，按功能分类整理，方便快速查阅：

---

### 1. `aptitude` 常用命令
**工具特点**：支持交互式界面（`aptitude` 启动后可上下翻页、标记安装/卸载），依赖解决更智能。

| 功能 | 命令示例 | 说明 |
| --- | --- | --- |
| 启动界面 | `sudo aptitude` | 进入交互式文本 UI，浏览、搜索、安装、升级、卸载软件包 |
| 更新索引 | `sudo aptitude update` | 同步软件包列表 |
| 升级软件 | `sudo aptitude upgrade` | 升级所有可升级的软件包 |
| 彻底升级 | `sudo aptitude full-upgrade` | 类似 `apt full-upgrade`<br/>，会自动处理依赖冲突 |
| 安装软件 | `sudo aptitude install <package>` | 安装指定包 |
| 卸载软件 | `sudo aptitude remove <package>` | 卸载包但保留配置 |
| 彻底卸载 | `sudo aptitude purge <package>` | 卸载包并删除其配置 |
| 自动清理 | `sudo aptitude autoclean` | 删除旧的包缓存 |
| 修复依赖 | `sudo aptitude -f install` | 尝试修复依赖问题 |
| 搜索包 | `aptitude search <pattern>` | 搜索包名或描述中包含 `<pattern>`<br/> 的软件包 |
| 查看详情 | `aptitude show <package>` | 显示包的详细信息（依赖、说明等） |
| 列出已装 | `aptitude search '~i'` | 列出所有已安装的包 |
| 列出可升 | `aptitude search '~U'` | 列出所有有可用升级的包 |


---

### 2. `apt-get` 常用命令
**工具特点**：早期脚本化首选，和底层 `dpkg` 搭配，使用更“纯粹”。

| 功能 | 命令示例 | 说明 |
| --- | --- | --- |
| 更新索引 | `sudo apt-get update` | 更新本地软件包列表 |
| 升级软件 | `sudo apt-get upgrade` | 升级所有已安装的软件包 |
| 彻底升级 | `sudo apt-get dist-upgrade` | 会根据需要添加/移除依赖包 |
| 安装软件 | `sudo apt-get install <package>` | 安装指定包及其依赖 |
| 卸载软件 | `sudo apt-get remove <package>` | 卸载包但保留配置 |
| 彻底卸载 | `sudo apt-get purge <package>` | 卸载包并删除其所有配置 |
| 自动清理 | `sudo apt-get autoremove` | 删除不再被依赖的孤立包 |
| 清理缓存 | `sudo apt-get autoclean`<br/>`sudo apt-get clean` | `autoclean`<br/> 删除旧版包；`clean`<br/> 删除所有缓存 |
| 修复依赖 | `sudo apt-get -f install` | 修复依赖关系 |
| 搜索包 | `apt-cache search <pattern>` | 搜索包名或描述中包含 `<pattern>`<br/> 的软件包 |
| 查看详情 | `apt-cache show <package>` | 查看包的详细信息 |
| 列出已装 | `dpkg -l` | 列出所有已安装包（`apt-get`<br/> 本身不直接列装包） |


---

### 3. `apt` 常用命令
**工具特点**：集成了 `apt-get` 与 `apt-cache` 的常用功能，输出更友好，推荐交互式使用。

| 功能 | 命令示例 | 说明 |
| --- | --- | --- |
| 更新索引 | `sudo apt update` | 更新本地软件包列表 |
| 升级软件 | `sudo apt upgrade` | 升级所有已安装的软件包 |
| 彻底升级 | `sudo apt full-upgrade` | 会根据需要添加/移除依赖包 |
| 安装软件 | `sudo apt install <package>` | 安装指定包及其依赖 |
| 下载包 | `apt download <package>` | 仅下载 `.deb`<br/> 包，不安装 |
| 卸载软件 | `sudo apt remove <package>` | 卸载包但保留配置 |
| 彻底卸载 | `sudo apt purge <package>` | 卸载包并删除其所有配置 |
| 自动清理 | `sudo apt autoremove` | 删除不再被依赖的孤立包 |
| 清理缓存 | `sudo apt autoclean`<br/>`sudo apt clean` | 同 `apt-get` |
| 搜索包 | `apt search <pattern>` | 搜索包名或描述中包含 `<pattern>`<br/> 的软件包 |
| 查看详情 | `apt show <package>` | 查看包的详细信息 |
| 列出已装 | `apt list --installed` | 列出所有已安装的软件包 |
| 列出可升 | `apt list --upgradable` | 列出所有有可用升级的包 |
| 编辑源 | `sudo apt edit-sources` | 编辑软件源列表 |


---

**小贴士**

1. 日常推荐使用 `apt`，命令简洁且输出友好；
2. 遇到复杂依赖冲突时，可借助 `aptitude` 的交互界面与智能解决方案；
3. 在脚本或自动化场景，使用 `apt-get` 能保证稳定的行为与向后兼容。

