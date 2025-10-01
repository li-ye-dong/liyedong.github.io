```bash
# 第一阶段：构建
FROM harbor.liyedong.com/kyem/golang:1.24 AS builder

# 设置 Go 模块代理为中国源
ENV GOPROXY=https://goproxy.cn,direct

# 设置工作目录
WORKDIR /app

# 拷贝 go.mod 和 go.sum 并下载依赖
COPY go.mod go.sum ./
RUN go mod download

# 拷贝源码并编译
COPY . .
RUN go build -o main .

# 第二阶段：精简运行镜像
FROM harbor.liyedong.com/kyem/debian:bookworm-slim

# 创建非 root 用户（可选）
#RUN useradd -m appuser

WORKDIR /app

# 复制构建出的二进制文件
COPY --from=builder /app/main .

# 使用非 root 用户（可选）
#USER appuser

# 暴露服务端口
EXPOSE 8080

# 启动程序
CMD ["./main"]


#docker build -t my-go-app-test .
```

