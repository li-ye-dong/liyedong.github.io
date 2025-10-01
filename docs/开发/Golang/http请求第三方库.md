## resty
### 安装
```bash
go get github.com/go-resty/resty/v2
```

### GET请求
```go
package main

import (
    "fmt"
    "log"

    "github.com/go-resty/resty/v2"
)

// 定义一个响应结构体（用于解析 JSON）
type User struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email"`
}

func main() {
    // 创建客户端实例
    client := resty.New()

    // ========== 1. GET 请求 ==========
    resp, err := client.R().
    SetQueryParams(map[string]string{
        "page":  "1",
        "limit": "10",
    }).
    SetHeader("Accept", "application/json"). // 设置 HTTP 头
    Get("https://jsonplaceholder.typicode.com/users")

    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("GET Status Code:", resp.StatusCode())
    fmt.Println("GET Body:", resp.String())

    // ========== 2. GET 并解析 JSON 到结构体 ==========
    var users []User
    _, err = client.R().
    SetResult(&users). // 自动反序列化到结构体
    Get("https://jsonplaceholder.typicode.com/users")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("解析到的用户数量:", len(users))
    fmt.Println("第一个用户:", users[0])

}

```

### POST请求
```go
package main

import (
    "fmt"
    "log"

    "github.com/go-resty/resty/v2"
)

// 定义一个响应结构体（用于解析 JSON）
type User struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email"`
}

func main() {
    // 创建客户端实例
    client := resty.New()


    // ========== 3. POST JSON 请求 ==========
    newUser := User{
        Name:  "Alice",
        Email: "alice@example.com",
    }
    postResp, err := client.R().
    SetHeader("Content-Type", "application/json").
    SetBody(newUser). // 自动序列化为 JSON
    Post("https://jsonplaceholder.typicode.com/users")

    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("POST Status Code:", postResp.StatusCode())
    fmt.Println("POST Body:", postResp.String())

    // ========== 4. 自动重试机制 ==========
    client.SetRetryCount(3)                 // 最多重试 3 次
    client.SetRetryWaitTime(2 * 1000000000) // 每次重试间隔 2 秒（单位：纳秒）
    client.SetRetryMaxWaitTime(10 * 1000000000)

    _, err = client.R().Get("https://httpbin.org/status/500") // 故意触发 500 错误测试
    if err != nil {
        log.Fatal(err)
    }
}

```

### DEMO
```go
package main

import (
    "fmt"
    "log"

    "github.com/go-resty/resty/v2"
)

// 定义一个响应结构体（用于解析 JSON）
type User struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email"`
}

func main() {
    // 创建客户端实例
    client := resty.New()

    // ========== 1. GET 请求 ==========
    resp, err := client.R().
    SetQueryParams(map[string]string{
        "page":  "1",
        "limit": "10",
    }).
    SetHeader("Accept", "application/json"). // 设置 HTTP 头
    Get("https://jsonplaceholder.typicode.com/users")

    if err != nil {
        log.Fatal(err)
    }

    fmt.Println("GET Status Code:", resp.StatusCode())
    fmt.Println("GET Body:", resp.String())

    // ========== 2. GET 并解析 JSON 到结构体 ==========
    var users []User
    _, err = client.R().
    SetResult(&users). // 自动反序列化到结构体
    Get("https://jsonplaceholder.typicode.com/users")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("解析到的用户数量:", len(users))
    fmt.Println("第一个用户:", users[0])

    // ========== 3. POST JSON 请求 ==========
    newUser := User{
        Name:  "Alice",
        Email: "alice@example.com",
    }
    postResp, err := client.R().
    SetHeader("Content-Type", "application/json").
    SetBody(newUser). // 自动序列化为 JSON
    Post("https://jsonplaceholder.typicode.com/users")

    if err != nil {
        log.Fatal(err)
    }
    fmt.Println("POST Status Code:", postResp.StatusCode())
    fmt.Println("POST Body:", postResp.String())

    // ========== 4. 自动重试机制 ==========
    client.SetRetryCount(3)                 // 最多重试 3 次
    client.SetRetryWaitTime(2 * 1000000000) // 每次重试间隔 2 秒（单位：纳秒）
    client.SetRetryMaxWaitTime(10 * 1000000000)

    _, err = client.R().Get("https://httpbin.org/status/500") // 故意触发 500 错误测试
    if err != nil {
        log.Fatal(err)
    }
}

```

## gorequest
### 安装
```go
go get github.com/parnurzeal/gorequest
```

### GET请求
```go
// go get github.com/parnurzeal/gorequest
package main

import (
	"encoding/json"
	"fmt"
	"log"

	"github.com/parnurzeal/gorequest"
)

type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

func main() {
	request := gorequest.New()

	// GET 请求
	resp, body, errs := request.
		Get("https://jsonplaceholder.typicode.com/users").
		Query("page=1").
		Query("limit=5").
		End()
	if len(errs) > 0 {
		log.Fatal(errs)
	}
	fmt.Println("GET 请求状态码:", resp.StatusCode)
	var users []User
	if err := json.Unmarshal([]byte(body), &users); err != nil {
		log.Fatal(err)
	}
	fmt.Println("[gorequests] 第一个用户:", users[0])

}

```

### POST请求
```go
// go get github.com/parnurzeal/gorequest
package main

import (
	"encoding/json"
	"fmt"
	"log"

	"github.com/parnurzeal/gorequest"
)

type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

func main() {
	request := gorequest.New()

	// POST JSON 请求
	newUser := User{Name: "Alice", Email: "alice@example.com"}
	resp, body, errs = request.
		Post("https://jsonplaceholder.typicode.com/users").
		Send(newUser).
		End()
	if len(errs) > 0 {
		log.Fatal(errs)
	}
	var created User
	if err := json.Unmarshal([]byte(body), &created); err != nil {
		log.Fatal(err)
	}
	fmt.Println("[gorequests] 新用户ID:", created.ID)
}

```

### DEMO
```go
// go get github.com/parnurzeal/gorequest
package main

import (
	"encoding/json"
	"fmt"
	"log"

	"github.com/parnurzeal/gorequest"
)

type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

func main() {
	request := gorequest.New()

	// GET 请求
	resp, body, errs := request.
		Get("https://jsonplaceholder.typicode.com/users").
		Query("page=1").
		Query("limit=5").
		End()
	if len(errs) > 0 {
		log.Fatal(errs)
	}
	fmt.Println("GET 请求状态码:", resp.StatusCode)
	var users []User
	if err := json.Unmarshal([]byte(body), &users); err != nil {
		log.Fatal(err)
	}
	fmt.Println("[gorequests] 第一个用户:", users[0])

	// POST JSON 请求
	newUser := User{Name: "Alice", Email: "alice@example.com"}
	resp, body, errs = request.
		Post("https://jsonplaceholder.typicode.com/users").
		Send(newUser).
		End()
	if len(errs) > 0 {
		log.Fatal(errs)
	}
	var created User
	if err := json.Unmarshal([]byte(body), &created); err != nil {
		log.Fatal(err)
	}
	fmt.Println("[gorequests] 新用户ID:", created.ID)
}

```

