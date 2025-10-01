Go是一个用于管理Go源代码的工具。

## 用法
```plain
go <command> [arguments]
```

## 命令列表
| 命令 | 描述 |
| --- | --- |
| bug | 启动一个错误报告 |
| build | 编译包和依赖项 |
| clean | 移除对象文件和缓存文件 |
| doc | 显示包或符号的文档 |
| env | 打印Go环境信息 |
| fix | 更新包以使用新的API |
| fmt | 使用gofmt（重新格式化）包源文件 |
| generate | 通过处理源文件生成Go文件 |
| get | 向当前模块添加依赖项并安装它们 |
| install | 编译并安装包和依赖项 |
| list | 列出包或模块 |
| mod | 模块维护 |
| work | 工作区维护 |
| run | 编译并运行Go程序 |
| telemetry | 管理遥测数据和设置 |
| test | 测试包 |
| tool | 运行指定的Go工具 |
| version | 打印Go版本 |
| vet | 报告包中可能存在的错误 |


使用 `go help <command>` 了解有关某个命令的更多信息。

## 附加帮助主题
| 主题 | 描述 |
| --- | --- |
| buildconstraint | 构建约束 |
| buildjson | `build -json` 编码 |
| buildmode | 构建模式 |
| c | Go和C之间的调用 |
| cache | 构建和测试缓存 |
| environment | 环境变量 |
| filetype | 文件类型 |
| goauth | `GOAUTH` 环境变量 |
| go.mod | `go.mod` 文件 |
| gopath | `GOPATH` 环境变量 |
| goproxy | 模块代理协议 |
| importpath | 导入路径语法 |
| modules | 模块、模块版本等 |
| module-auth | 使用 `go.sum` 进行模块身份验证 |
| packages | 包列表和模式 |
| private | 下载非公共代码的配置 |
| testflag | 测试标志 |
| testfunc | 测试函数 |
| vcs | 使用 `GOVCS` 控制版本控制 |


使用 `go help <topic>` 了解有关该主题的更多信息。



设置代理:

```bash
go env -w GOPROXY=https://goproxy.cn,direct

go mod init testproxy
go get github.com/gin-gonic/gin
```

Go（Golang）语言的命令行工具非常强大，主要通过 `go` 命令进行管理。以下是最常用的 Go 命令，按照用途分类总结，适合日常开发、调试、构建与部署。

---

## 🛠️ 项目管理类
### 1. 初始化项目
```bash
go mod init [模块名]
```

初始化 Go module 项目，生成 `go.mod` 文件。例如：

```bash
go mod init github.com/yourname/helloworld
```

### 2. 添加依赖
```bash
go get 包名[@版本]
```

添加或更新依赖包，例如：

```bash
go get github.com/gin-gonic/gin
```

### 3. 查看依赖树
```bash
go list -m all
```

### 4. 清理无用依赖
```bash
go mod tidy
```

自动添加遗漏和删除未使用的模块。

### 5. 升级所有依赖
```bash
go get -u ./...
```

---

## 🚀 编译与运行
### 6. 编译 Go 程序
```bash
go build
```

默认在当前目录编译，会生成可执行文件（如 `main.exe` 或 `main`）。

编译指定文件：

```bash
go build main.go
```

### 7. 运行 Go 程序
```bash
go run 文件.go
```

例如：

```bash
go run main.go
```

可以同时运行多个文件：

```bash
go run *.go
```

---

## 🧪 测试相关
### 8. 运行单元测试
```bash
go test
```

运行当前目录下的所有 `_test.go` 测试文件。

带详细日志：

```bash
go test -v
```

只运行某个函数的测试：

```bash
go test -run TestFuncName
```

---

## 🔍 调试和诊断
### 9. 检查代码格式
```bash
go fmt
```

自动格式化当前目录下的 `.go` 文件。

### 10. 静态代码检查
```bash
go vet
```

发现潜在的错误和不规范代码。

### 11. 依赖可视化
```bash
go mod graph
```

输出模块依赖关系图。

---

## 📦 打包和安装
### 12. 安装为本地工具/命令
```bash
go install 包名@版本
```

将 Go 程序编译为二进制并安装到 `$GOPATH/bin`，可用作命令行工具。

---

## 📁 GOPATH 管理（了解）
+ 查看当前环境配置：

```bash
go env
```

+ 查看 `GOPATH`：

```bash
go env GOPATH
```

---

## 🧰 实用脚本（快速测试）
一行写一个 Go 脚本运行：

```bash
go run <(echo 'package main; import "fmt"; func main() { fmt.Println("Hello") }')
```

---

如果你有特定的场景（如编写库、构建 REST API、交叉编译、打包 Docker 镜像），我可以提供更深入的命令组合方案。是否需要？

