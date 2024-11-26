@echo off

REM 使用 Poetry 执行 mkdocs build
poetry run mkdocs build

REM 提示构建完成
echo build successful！please look at site dir。
pause