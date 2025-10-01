## <font style="color:rgb(38, 38, 38);">1. 下载工具</font>
[Releases · protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf/releases)

<font style="color:rgb(245, 34, 45);">注意：</font>protoc的版本需要和golang/protobuf保持一致 （尽量自己去下载最新的版本）

下载完成后解压后记得将路径添加到环境变量中

## <font style="color:rgb(38, 38, 38);">2. 下载go的依赖包</font>
```go
go get google.golang.org/grpc
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

## <font style="color:rgb(38, 38, 38);">3. proto文件</font>
```go
syntax = "proto3";
option go_package = ".;proto";
service Greeter {
    rpc SayHello (HelloRequest) returns (HelloReply);
}

message HelloRequest {
    string name = 1;
}

message HelloReply {
    string message = 1;
}
```

## <font style="color:rgb(38, 38, 38);">4. 生成go文件</font>
### <font style="color:rgb(38, 38, 38);">1. 生成消息结构体（protobuf 部分）→ 使用 </font>`<font style="color:rgb(38, 38, 38);">protoc-gen-go</font>`
```plain
protoc -I . helloworld.proto --go_out=.
```

### <font style="color:rgb(38, 38, 38);">2. 生成 gRPC 服务代码（service 部分）→ 使用 </font>`<font style="color:rgb(38, 38, 38);">protoc-gen-go-grpc</font>`
```plain
protoc -I . helloworld.proto --go-grpc_out=.
```

✅<font style="color:rgb(38, 38, 38);"> 或者你也可以将它们合并在一行（推荐）：</font>

```plain
protoc -I . helloworld.proto --go_out=. --go-grpc_out=.
```

## <font style="color:rgb(38, 38, 38);">5. 服务端代码</font>
```go
package main

import (
    "context"
    "fmt"
    "google.golang.org/grpc"
    "grpc_demo/hello"
    "net"
)

type Server struct {
}


func (s *Server)  SayHello(ctx context.Context,request *hello.HelloRequest)(*hello.HelloReply,error){
    return &hello.HelloReply{Message:"Hello "+request.Name},nil
}

func main()  {
    g := grpc.NewServer()
    s := Server{}
    hello.RegisterGreeterServer(g,&s)
    lis, err := net.Listen("tcp", fmt.Sprintf(":8080"))
    if err != nil {
        panic("failed to listen: "+err.Error())
    }
    g.Serve(lis)
}
```

## <font style="color:rgb(38, 38, 38);">6. 客户端</font>
```go
package main

import (
    "context"
    "fmt"
    "google.golang.org/grpc"
    "grpc_demo/proto"
)

func main()  {
    conn,err := grpc.Dial("127.0.0.1:8080",grpc.WithInsecure())
    if err!=nil{
        panic(err)
    }
    defer conn.Close()
    c := hello.NewGreeterClient(conn)
    r,err := c.SayHello(context.Background(),&hello.HelloRequest{Name:"bobby"})
    if err!=nil{
        panic(err)
    }
    fmt.Println(r.Message)
}
```

  


