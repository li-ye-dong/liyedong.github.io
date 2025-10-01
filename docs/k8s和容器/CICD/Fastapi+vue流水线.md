[https://gitee.com/sdfsdfs445/vue-fastapi-admin-liyedong.git](https://gitee.com/sdfsdfs445/vue-fastapi-admin-liyedong.git)



```dockerfile
# 第一阶段：构建依赖层
FROM python:3.11-slim AS builder

# 设置国内 PyPI 源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装编译依赖（如 psycopg2、uvicorn 需依赖）
RUN apt-get update && apt-get install -y build-essential libpq-dev

# 设置工作目录
WORKDIR /app

# 复制 Poetry 配置文件并安装依赖
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# 第二阶段：运行环境
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 复制完整项目代码
COPY . .

# 从构建阶段复制已安装依赖
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

# 暴露端口
EXPOSE 9999

# 启动命令（可按需改为 uvicorn）
CMD ["python", "run.py"]

```



```dockerfile
# 构建阶段
FROM node:20.2.0-alpine AS builder

WORKDIR /web

# 使用淘宝镜像加速安装
RUN npm config set registry https://registry.npmmirror.com/

COPY web/package*.json ./
RUN npm install

COPY web/ ./
RUN npm run build

# 部署阶段（使用 nginx）
FROM nginx:stable-alpine

# 拷贝打包后的静态文件
COPY --from=builder /web/dist /usr/share/nginx/html

# 自定义 nginx 配置（可选）
# COPY web/web.conf /etc/nginx/nginx.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

```





```nginx
server {
  listen 80;
  server_name localhost;
  location / {
    root /usr/share/nginx/html
      index index.html index.htm;
    try_files $uri /index.html;
  }
  location /api/ {
    proxy_pass http://localhost:9999/api/;
    proxy_set_header Host   $host;
    proxy_set_header X-Real-IP      $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }

  location /docs {
    proxy_pass http://localhost:9999/docs;
    proxy_set_header Host   $host;
    proxy_set_header X-Real-IP      $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
  location /openapi.json{
    proxy_pass http://localhost:9999/openapi.json;
  }


}
```

