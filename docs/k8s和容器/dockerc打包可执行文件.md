### 1. 安装 `dockerc`
你可以从 [最新版本发布页面](https://github.com/NilsIrl/dockerc/releases) 下载并安装 `dockerc`。

### 2. 构建 `dockerc`（如果需要从源代码构建）
如果你希望从源代码构建 `dockerc`，需要注意该项目使用了 Git 子模块。克隆仓库后，运行以下命令初始化并更新子模块：

```bash
git submodule init
git submodule update
```

然后，使用以下命令编译 `dockerc`：

```bash
zig build -Doptimize=ReleaseSafe -Dtarget=x86_64-linux-musl
zig build -Doptimize=ReleaseSafe -Dtarget=aarch64-linux-musl
```

### 3. 使用 `dockerc` 编译 Docker 镜像
你可以使用以下命令将 Docker 镜像编译为可执行文件：

```bash
# 从 Docker Hub 获取镜像
$ dockerc --image docker://oven/bun --output bun
# 从本地 Docker 守护进程存储中获取镜像
$ dockerc --image docker-daemon:mysherlock-image:latest --output sherlock_bin
# 指定目标指令集架构
$ dockerc --image docker://hello-world --arch arm64 --output hello
```

### 4. 运行生成的二进制文件
生成的二进制文件可以像普通二进制文件一样运行。你还可以使用 `-e` 和 `-v` 选项，就像在使用 `docker run` 时一样：

```bash
# 运行生成的二进制文件
./bun
# 指定环境变量
./bun -e VAR_NAME=VAR_VALUE
# 指定挂载卷
./bun -v /host/path:/container/path
```

### 5. 注意事项和建议
+ **依赖管理**：确保生产环境中安装了 `dockerc` 所需的所有依赖项，如 `libzstd-dev` 和 `libfuse3-dev`。你可以使用以下命令安装这些依赖项：

```bash
sudo apt install libzstd-dev libfuse3-dev
```

+ **性能优化**：在构建时使用 `-Doptimize=ReleaseSafe` 选项可以优化性能。
+ **兼容性**：`dockerc` 当前支持 x86_64 和 arm64 架构，但对 macOS 和 Windows 的支持仍在开发中（使用 QEMU）。在选择目标架构时，请确保与生产环境兼容。
+ **持续集成/持续部署（CI/CD）**：可以在 CI/CD 流程中集成 `dockerc`，以自动化构建和部署过程。例如，在 `.github/workflows/ci.yml` 文件中，可以添加以下步骤：

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: goto-bus-stop/setup-zig@v2
        with:
          version: 0.13.0
      - run: sudo apt install autoconf libtool pkg-config make libzstd-dev libfuse3-dev
      - run: zig build -Doptimize=ReleaseSafe -Dtarget=x86_64-linux-musl
      - run: zig-out/bin/dockerc --image docker://your-image --output your-binary
      - run: # 部署生成的二进制文件到生产环境
```



