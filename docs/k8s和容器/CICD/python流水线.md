```bash
# 第一阶段：构建依赖层（可选）
FROM python:3.11-slim AS builder

# 设置国内源，加速构建
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装构建工具
RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /app

# 复制依赖文件并安装
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false \
    && poetry install --no-root --only main

# 第二阶段：运行阶段
FROM python:3.11-slim

# 环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 复制项目文件
COPY . .

# 复制已安装的依赖
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

# 启动命令（例如：使用 gunicorn）
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

```



```bash
FROM python:3.11-slim

# 设置国内 PyPI 源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装基础依赖
RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 启动 Uvicorn 服务
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```

