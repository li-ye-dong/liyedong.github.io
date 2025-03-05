# 概述
 逆向字体加密是许多反爬措施中的一种，主要是通过自定义字体文件（如 `woff`、`ttf`）来改变网页显示的文字，使得直接抓取的内容不易读或与实际显示不一致。逆向解密字体的流程通常包含以下几个步骤：  

工具封装

# 步骤
### 1. **获取字体文件**
+ 在网页的 HTML 或 CSS 中，字体文件通常通过 `@font-face` 定义。可以使用 `requests` 库抓取页面内容，然后找到字体文件 URL 下载。

### 2. **解析字体文件**
+ 字体文件通常是 `.woff` 或 `.ttf` 格式，可以使用 `fontTools` 库中的 `TTFont` 类来加载和解析字体文件。
+ 使用以下代码加载字体文件并查看其字符映射：

```python
from fontTools.ttLib import TTFont

# 加载字体文件
font = TTFont('path/to/font.woff')
# 打印字符映射
cmap = font['cmap'].getBestCmap()
print(cmap)  # 查看字体中的字符映射
```

### 3. **分析字符映射关系**
+ 加密字体通常是通过修改字符映射来实现的。通过查看 `cmap` 中的映射关系，可以发现特定字符编码对应的字形编码。
+ 一些反爬字体会将数字或常用汉字的字符编码映射到特定的字形上。比如，字体中编码 `U+0041` 实际对应的并不是字母 "A"，而是数字 "1" 或其他字符。

### 4. **绘制字形并识别内容**
+ 有时字符和字形的映射不规则，需要将字体中的字形提取出来并与真实文字做对比。这种情况下可以使用 `matplotlib` 和 `Pillow` 库将每个字形绘制出来并逐个识别。
+ 使用以下代码将字形绘制为图像：

```python
from PIL import Image, ImageDraw, ImageFont

# 加载自定义字体文件
font = ImageFont.truetype('path/to/font.ttf', size=40)

# 创建空白图片并绘制字符
img = Image.new('RGB', (100, 100), 'white')
draw = ImageDraw.Draw(img)
draw.text((10, 10), "A", font=font, fill="black")  # 绘制字符“A”
img.show()
```

### 5. **匹配原始字符并替换**
+ 通过上述映射关系，可以生成一个映射字典，将加密内容还原为明文。
+ 比如：

```python
encrypted_text = "加密的文本"
mapping = {'加': '1', '密': '2'}  # 假设字符对应关系
decrypted_text = ''.join(mapping.get(c, c) for c in encrypted_text)
```

### 6. **自动化处理**
+ 为了在大规模爬取中解密这些字体加密，可以使用 Python 的 `re` 库和解析库（如 `BeautifulSoup`）自动提取并解密需要的信息。

# 依赖安装
```python
poetry add ddddocr fonttools pillow
```

# 工具封装
```python
from fontTools.ttLib import TTFont
import ddddocr
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# 将 cmap 码点（字符代码）转换为图片的函数
def convert_cmap_to_image(cmap_code, font_path):
    img_size = 1024  # 定义图片大小
    # 准备三要素：image画布，draw画笔，font字体
    img = Image.new("1", (img_size, img_size), 255)  # 创建一个黑白图像对象（1表示单色模式，255为白色）
    draw = ImageDraw.Draw(img)  # 创建绘图对象
    font = ImageFont.truetype(font_path, img_size)  # 加载字体文件并设置大小为图像尺寸

    # 将 cmap code 转换为字符
    character = chr(cmap_code)
    # 获取文本在图像中的边界框，用于计算文本绘制的宽度和高度
    bbox = draw.textbbox((0, 0), character, font=font)
    width = bbox[2] - bbox[0]  # 文本的宽度
    height = bbox[3] - bbox[1]  # 文本的高度

    # 将字符绘制到图片上，并居中显示
    draw.text(((img_size - width) // 2, (img_size - height) // 2), character, font=font)
    return img  # 返回生成的图像对象

# 从字体文件中提取字符并使用 OCR 识别其文本含义
def extract_text_from_font(font_path):
    font = TTFont(font_path)  # 加载字体文件
    # OCR 模块初始化
    ocr = ddddocr.DdddOcr(beta=True, show_ad=False)  # 实例化 ddddocr 对象

    font_map = {}  # 存储字体字符映射关系的字典
    for cmap_code, glyph_name in font.getBestCmap().items():
        # 将字体字符转换为图像
        image = convert_cmap_to_image(cmap_code, font_path)

        # 使用 OCR 模块提取图像中的字符
        bytes_io = BytesIO()
        image.save(bytes_io, "PNG")
        text = ocr.classification(bytes_io.getvalue())  # 使用 ddddocr 识别图像中的字符

        # 显示 Unicode 码点、字符名及识别结果
        print(f"Unicode码点：{cmap_code} - Unicode字符:{glyph_name}，识别结果：{text}")
        font_map[cmap_code] = text  # 存储识别结果

    return font_map  # 返回字符映射关系字典

font_file_path = "font.woff"  # 字体文件路径
print(extract_text_from_font(font_file_path))

```

# 优化后工具类
```python
from fontTools.ttLib import TTFont
import ddddocr
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from concurrent.futures import ThreadPoolExecutor

# 将 cmap 码点（字符代码）转换为较小的图片，适合 OCR 识别
def convert_cmap_to_image(cmap_code, font_path, img_size=512):
    # 创建一个灰度图像对象 ('L' 表示灰度模式)
    img = Image.new("L", (img_size, img_size), 255)  # 255表示背景白色
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, img_size // 2)  # 使用较小的字体尺寸

    # 将 cmap code 转换为字符
    character = chr(cmap_code)
    bbox = draw.textbbox((0, 0), character, font=font)  # 获取文本在图像中的边界框
    width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]  # 获取文本宽度和高度

    # 将字符绘制在图像中央
    draw.text(((img_size - width) // 2, (img_size - height) // 2), character, font=font, fill=0)  # 0表示黑色字体
    return img

# 处理单个字符映射的 OCR 识别任务
def ocr_single_character(cmap_code, glyph_name, font_path, ocr):
    image = convert_cmap_to_image(cmap_code, font_path)
    bytes_io = BytesIO()
    image.save(bytes_io, "PNG")
    text = ocr.classification(bytes_io.getvalue())  # 使用 OCR 识别图像中的字符
    print(f"Unicode码点：{cmap_code} - Unicode字符:{glyph_name}，识别结果：{text}")
    return cmap_code, text

# 从字体文件中提取字符并进行并行 OCR 识别
def extract_text_from_font(font_path):
    font = TTFont(font_path)  # 加载字体文件
    ocr = ddddocr.DdddOcr(beta=True, show_ad=False)  # 初始化 ddddocr 对象
    font_map = {}  # 用于存储字符映射关系的字典

    # 使用多线程并行化 OCR 识别
    with ThreadPoolExecutor() as executor:
        # 准备所有的 OCR 任务
        tasks = [executor.submit(ocr_single_character, cmap_code, glyph_name, font_path, ocr) 
                 for cmap_code, glyph_name in font.getBestCmap().items()]
        
        # 收集任务结果
        for future in tasks:
            cmap_code, text = future.result()
            font_map[cmap_code] = text  # 存储识别结果

    return font_map  # 返回完整的字符映射

# 字体文件路径
font_file_path = "font.woff"
print(extract_text_from_font(font_file_path))

```

