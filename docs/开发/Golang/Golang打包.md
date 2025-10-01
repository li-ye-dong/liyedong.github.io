## 基础打包
```go
package main

import "fmt"

func main() {

    fmt.Print("Hello, World!")
    fmt.Println("Hello, World!")
}

```

因为以上只使用了fmt库，没有使用到动态链接的库，以下结果都为静态链接

```bash
go build -o out main.go
file out | tr , "\n"
ldd out
```

## 引入动态链接库net
```go
package main

import (
	"fmt"
	"log"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/" {
		http.Error(w, "404 not found", http.StatusNotFound) //404 not found
		return
	}
	if r.Method != "GET" {
		http.Error(w, "method is not supported", http.StatusNotFound) //method is not supported
		return
	}
	fmt.Fprintf(w, "hello!") //hello!
}

func main() {
	http.HandleFunc("/", helloHandler)                        //注册路由和处理函数
	fmt.Printf("Starting server at port 8080\n")              //Starting server at port 8080
	if err := http.ListenAndServe(":8080", nil); err != nil { //监听端口8080，处理请求
		log.Fatal(err) //打印错误信息并退出程序
	}
}

```

打包后，结果为动态链接

```go
go build -o out main.go
file out | tr , "\n"
ldd out
```

## 强制静态编译
netgo 标签与 

```go
go build -o out -tags netgo main.go
file out
ldd out
```

CGO_ENABLED=0 的妙用环境变量

```go
CGO_ENABLED=0 go build -o out main.go
```

指定ldflags,构建会有一个警告，提示并非所有内容都可以静态链接，但是对我们的程序可能没问题。

```go
go build -ldflags "-linkmode external -extldflags '-static'" -o out main.go
```

## linux构建其他平台可执行程序
从 Linux 编译到 macOS

```go
CGO_ENABLED=0 GOOS=darwin GOARCH=arm64 go build -o out main.go
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o get_path_files main.go


#powershell
$env:GOOS="linux"
$env:GOARCH="amd64"
$env:CGO_ENABLED="0"
go build -ldflags "-w -s" -o get_path_files main.go
```

## 终极技巧：使用 ldflags 剥离调试信息，显著减小文件体积
```go
go build -ldflags "-w -s" -o out main.go




```

