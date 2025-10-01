## 安装
```bash
pip install gooey
poetry add gooey
```



## Demo
```python
from gooey import Gooey, GooeyParser

@Gooey(
    program_name="全面 Gooey Demo",
    language="chinese",
    default_size=(700, 600),
    show_stop_warning=False,
    required_cols=2,
    optional_cols=2,
    menu=[{
        'name': '文件',
        'items': [{
            'type': 'AboutDialog',
            'menuTitle': '关于',
            'name': '全面 Gooey Demo',
            'description': '一个包含所有参数类型的 Gooey 示例',
            'version': '1.0.0',
            'copyright': 'MIT',
            'website': 'https://github.com',
        }]
    }]
)
def main():
    parser = GooeyParser(description="这是一个完整的 Gooey Demo，包含所有参数类型")

    # 1. 标准参数
    parser.add_argument('--name', type=str, help='输入你的名字', required=True)
    parser.add_argument('--age', type=int, help='输入你的年龄', required=True)
    parser.add_argument('--height', type=float, help='输入你的身高（米）')
    parser.add_argument('--debug', action='store_true', help='启用调试模式')
    parser.add_argument('--gender', choices=['男', '女', '其他'], help='选择性别')

    # 2. 文件和目录
    parser.add_argument('--file', widget='FileChooser', help='选择单个文件')
    parser.add_argument('--files', widget='MultiFileChooser', nargs='+', help='选择多个文件')
    parser.add_argument('--folder', widget='DirChooser', help='选择文件夹')
    parser.add_argument('--savefile', widget='FileSaver', help='选择保存文件')

    # 3. 其他类型
    parser.add_argument('--date', widget='DateChooser', help='选择日期')
    parser.add_argument('--time', widget='TimeChooser', help='选择时间')
    parser.add_argument('--color', widget='ColourChooser', help='选择颜色')
    parser.add_argument('--password', widget='PasswordField', help='输入密码')

    args = parser.parse_args()

    # 输出参数（避免明文密码）
    print(f"姓名: {args.name}")
    print(f"年龄: {args.age}")
    print(f"身高: {args.height}")
    print(f"调试模式: {args.debug}")
    print(f"性别: {args.gender}")
    print(f"文件: {args.file}")
    print(f"多个文件: {args.files}")  # 这里会返回文件路径列表
    print(f"文件夹: {args.folder}")
    print(f"保存文件: {args.savefile}")
    print(f"日期: {args.date}")
    print(f"时间: {args.time}")
    print(f"颜色: {args.color}")
    print(f"密码: {'*' * len(args.password)}")

if __name__ == '__main__':
    main()

```

