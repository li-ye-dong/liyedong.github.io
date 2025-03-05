```python
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          2025/2/6     21:44                .idea
d-----        2024/12/28     18:16                .venv
d-----          2025/1/1     21:18                app                                                                                                              
-a----          2025/2/6     21:06            135 package.cmd
-a----          2025/2/6     20:43          90692 poetry.lock
-a----          2025/2/6     21:07           1133 pyproject.toml
-a----        2024/12/28     17:50           7932 README-en.md
-a----        2024/12/28     17:50           7165 README.md
-a----          2025/2/6     21:01            351 run.py
-a----          2025/2/6     21:06            756 run.spec
-a----        2024/12/28     17:50           1089 uvicorn_loggin_config.json

```

打包命令，部分无法扫描到的模块使用显示加载

```python
pyinstaller --onefile --hidden-import=passlib.handlers.argon2 --hidden-import=aiomysql --hidden-import=tortoise.backends.mysql .\run.py
```

打包后反复重启

```python
import uvicorn
from app.log import logger
import os
if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    logger.info(os.getcwd())
    logger.info("Starting uvicorn with log config from dict")
    uvicorn.run("app:app", host="0.0.0.0", port=9999, reload=True, log_config="uvicorn_loggin_config.json")

```

nginx伪静态规则转发配置，避免跨域

```python
location /   #配置vue单页应用需要，因为vue应用只有一个index.html单页应用
{
 try_files $uri $uri/ /index.html;
}
location /api/ {   #nginx转发到后端  避免跨域
    proxy_pass http://localhost:9999/api/;
    proxy_set_header Host   $host;
    proxy_set_header X-Real-IP      $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}

location /docs {    #转发到后端docs文档网站
    proxy_pass http://localhost:9999/docs;
    proxy_set_header Host   $host;
    proxy_set_header X-Real-IP      $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}
location /openapi.json{   #转发到后端docs文档网站时需要
    proxy_pass http://localhost:9999/openapi.json;
}


```

