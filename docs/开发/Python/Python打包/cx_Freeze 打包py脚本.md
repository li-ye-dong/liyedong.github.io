```python
from cx_Freeze import setup, Executable

setup(
    name="MyApp",                        # 程序名称
    version="1.0",                       # 程序版本
    description="My GUI Application",    # 程序描述
    author="liyedong",                   # 作者
    options={
        "build_exe": {
            "packages": ["os", "sys"],           # 打包时需要包含的包
            "excludes": ["tkinter"],             # 打包时排除的包
            "includes": ["lxml", "xmltodict"],   # 额外要打包的库
            "include_files": [                   # 附带的资源文件
                ("config.yaml", "config.yaml"),
                ("assets/", "assets/"),
            ],
            "optimize": 2,                       # 代码优化级别 (0,1,2)
            "build_exe": "build/exe_output"      # 自定义输出目录
        }
    },
    executables=[
        Executable(
            script="main.py",
            base="Win32GUI",       # 去掉黑框
            target_name="myapp.exe",
            icon="app.ico"
        )
    ]
)

```



```python
# 生成构建
python setup.py build

# 清理旧的构建目录（可选）
rm -rf build/ dist/

# 如果要生成安装包（一般很少用）
python setup.py bdist_msi   # 生成 Windows 安装包

```

