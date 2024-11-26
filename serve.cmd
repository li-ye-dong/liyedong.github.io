@echo off
REM 确保在虚拟环境中运行 mkdocs serve
poetry run mkdocs serve

REM 提示服务器已启动
echo http://127.0.0.1:8000
pause
