## ✅ 一、临时配置（仅当前终端有效）
在当前 shell 中运行即可：

```bash
export PATH="/your/path/bin:$PATH"
```

例如你使用 miniconda：

```bash
export PATH="$HOME/miniconda3/bin:$PATH"
```

⚠️ 这类设置**关闭终端后就失效**。

---

## ✅ 二、永久配置（建议方式）
把变量写入用户或系统配置文件中：

### 🔹 用户级别（只影响当前用户）
在你的 home 目录下编辑 `~/.bashrc` 或 `~/.bash_profile`（有的系统是 `.zshrc`）：

```bash
nano ~/.bashrc
```

添加一行：

```bash
export PATH="$HOME/miniconda3/bin:$PATH"
```

保存后执行：

```bash
source ~/.bashrc
```

### 🔹 系统级别（所有用户生效）
编辑 `/etc/profile` 或 `/etc/profile.d/your_env.sh`：

```bash
sudo vim /etc/profile.d/conda_path.sh
export PATH="/opt/miniconda3/bin:$PATH"
source /etc/profile.d/conda_path.sh
```

添加内容：

```bash
export PATH="/opt/miniconda3/bin:$PATH"
```

保存后让它立即生效：

```bash
source /etc/profile.d/conda_path.sh
```

---

## ✅ 验证是否成功
```bash
echo $PATH
which python
which conda
```

---

## 🔁 小提示
+ 环境变量不仅可以设置 `PATH`，也可以设置如 `PYTHONPATH`、`ANSIBLE_CONFIG`、`DOCKER_HOST` 等等；
+ 如果你要让 `conda activate` 可用，推荐配置：

```bash
source ~/miniconda3/etc/profile.d/conda.sh
```

写入 `.bashrc` 即可。

---

需要我给你写一个脚本，自动添加这些配置吗？或者你可以告诉我你要加哪个路径，我给你整套。

