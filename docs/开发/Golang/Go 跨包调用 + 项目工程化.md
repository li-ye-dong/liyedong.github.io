👌 你问的这个点非常关键：**Go 跨包调用** + **项目工程化设计**。很多人写 Go 项目时，容易一股脑把东西都写在 `main.go`，导致后期难以维护。  
我帮你整理一份“跨包调用+工程化最佳实践”。

---

# 🐹 Go 跨包调用 + 项目工程化
## 1. 跨包调用的基本规则
1. **导出规则**
    - 标识符（函数、结构体、方法、变量）首字母 **大写** → 可被其他包调用。
    - 首字母小写 → 仅限当前包使用。

```go
package utils
func PublicFunc() {}  // ✅ 可跨包调用
func privateFunc() {} // ❌ 只能在 utils 内部用
```

2. **import 路径**
    - 必须基于 `go.mod` 定义的 module 名称 + 相对路径。
    - 例如 `go.mod` 里是 `module myapp`：

```go
import "myapp/utils"
```

3. **调用形式**
    - 跨包调用时必须带上包名：

```go
utils.PublicFunc()
```

---

## 2. 工程化目录结构（推荐）
一个中型项目常见结构：

```plain
myapp/
  cmd/            # 各种可执行文件入口（main.go 放这里）
    server/
      main.go
  internal/       # 内部逻辑（不对外暴露）
    user/
      service.go
      repo.go
    order/
      service.go
  pkg/            # 公共库（对外可复用）
    utils/
      string.go
      time.go
  api/            # API 定义 (protobuf / swagger / http handler)
  configs/        # 配置文件
  scripts/        # 脚本工具
  go.mod
```

### 目录划分理念：
+ `cmd/` → 启动入口，每个子目录对应一个可执行程序。
+ `internal/` → 业务逻辑，只允许项目内部调用。
+ `pkg/` → 公共库，可以被跨项目调用。
+ `api/` → 对外 API 定义（HTTP handler / gRPC proto）。
+ `configs/` → 配置文件（yaml、json）。
+ `scripts/` → 辅助脚本（DB 初始化、CI/CD 脚本）。

---

## 3. 跨包调用实例
### 定义内部包
`internal/user/service.go`：

```go
package user

import "fmt"

type Service struct {
    Name string
}

// 首字母大写 -> 导出方法，可跨包调用
func (s *Service) CreateUser(name string) {
    fmt.Println("创建用户:", name)
}
```

### 在 `cmd/server/main.go` 跨包调用
```go
package main

import (
    "myapp/internal/user"
)

func main() {
    u := user.Service{}
    u.CreateUser("Alice") // 跨包调用
}
```

👉 注意：如果你把 `Service` 定义在 `internal/`，那么它只在 **myapp 内部**能用，外部项目无法 import（Go 的特性）。

---

## 4. 工程化开发技巧
1. **解耦：接口 + 实现分离**
    - 在 `internal/user/service.go` 里定义接口，方便测试和替换实现。

```go
type UserService interface {
    CreateUser(name string)
}

type userService struct{}

func (u *userService) CreateUser(name string) { ... }

func NewUserService() UserService {
    return &userService{}
}
```

外部使用时：

```go
userSvc := user.NewUserService()
userSvc.CreateUser("Alice")
```

2. **配置管理**
    - 推荐用 `spf13/viper` 加载 `config.yaml`。
    - 支持多环境配置：`configs/dev.yaml`, `configs/prod.yaml`。
3. **日志规范**
    - 用 `uber-go/zap` 或 `logrus`，结构化日志便于 ELK 收集。
4. **错误处理**
    - 用 `fmt.Errorf("msg: %w", err)` 包装错误，方便追踪。
5. **依赖注入**
    - 简单项目可手工注入，复杂项目推荐 `google/wire`。
6. **测试工程化**
    - `xxx_test.go` 写单元测试。
    - 接口驱动 + `gomock` 或 `testify/mock`。

---

## 5. 示例：跨包调用 + 工程化
假设我们要做一个用户服务：

`internal/user/service.go`：

```go
package user

import "fmt"

type Service struct{}

func (s *Service) CreateUser(name string) {
    fmt.Println("创建用户:", name)
}
```

`cmd/server/main.go`：

```go
package main

import (
    "myapp/internal/user"
)

func main() {
    svc := &user.Service{}
    svc.CreateUser("Alice") // 跨包调用
}
```

这样项目结构清晰，后续扩展 `order.Service`、`auth.Service` 也很自然。

---

✅ 总结：

+ **跨包调用要点**：首字母大写 + 正确 import。
+ **工程化目录**：`cmd/` 入口，`internal/` 业务逻辑，`pkg/` 公共库，`api/` API 定义。
+ **实践**：方法接收者+接口，解耦跨包调用，结合配置、日志、测试，形成完整工程化体系。

---

要不要我帮你画一张 **Go 工程化目录 + 跨包调用流程图**（类似 UML），让你一眼能看清调用关系？

