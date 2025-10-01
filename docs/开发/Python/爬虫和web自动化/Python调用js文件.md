## 使用pyexecjs库
```python
pip install pyexecjs
```

```python
import execjs

js_code = open("03 fjzy.js").read()
js_compile = execjs.compile(js_code)
data = js_compile.call("b",base64_encrypt_data)
```

## **使用 **`**subprocess**`** 调用 Node.js**
如果你已经安装了 Node.js，可以使用 `subprocess` 运行 JavaScript 代码。

#### **示例代码**
```python
import subprocess

js_code = """
console.log(3 + 5);
"""

result = subprocess.run(["node", "-e", js_code], capture_output=True, text=True)
print(result.stdout.strip())  # 输出 8
```

适用于简单脚本执行，但不适合复杂交互。

## **使用 **`**Js2Py**`** 直接在 Python 里执行 JS**
`Js2Py` 可以将 JavaScript 代码转换为 Python 并执行，但不支持所有 JS 语法（如 `window`、`document`）。

#### **安装 **`**Js2Py**`
```python
pip install js2py
```

#### **示例代码**
```python
import js2py

js_code = """
function add(a, b) {
    return a + b;
}
"""

js_func = js2py.eval_js(js_code + "add")  # 转换 JS 函数
result = js_func(3, 5)
print(result)  # 输出 8
```

**优点**：不需要 Node.js 依赖。  
**缺点**：不支持 DOM 操作，部分现代 JS 语法可能不兼容。

## **用 **`**selenium**`** 在浏览器环境执行 JS**
如果你的 JS 代码依赖浏览器环境（如 `document`、`window`），可以用 `selenium` 在 Chrome、Edge 等浏览器执行。

#### **安装 **`**selenium**`
```python
pip install selenium
```

#### **示例代码**
```python
from selenium import webdriver

driver = webdriver.Chrome()  # 需要安装 ChromeDriver
driver.get("https://www.example.com")  # 打开网页
result = driver.execute_script("return 3 + 5;")  # 执行 JS 代码
print(result)  # 输出 8
driver.quit()
```

**适用于**：需要操作网页的 JS 代码，例如爬虫、自动化测试。  
**缺点**：依赖浏览器，运行效率较低。

---

## **使用 **`**py_mini_racer**`** 轻量级 V8 引擎**
`py_mini_racer` 直接在 Python 内部运行 JavaScript，性能较好，但不支持 DOM 相关 API。

#### **安装 **`**py_mini_racer**`
```python
pip install py_mini_racer
```

#### **示例代码**
```python
from py_mini_racer import py_mini_racer

ctx = py_mini_racer.MiniRacer()
result = ctx.eval("3 + 5")
print(result)  # 输出 8
```

**适用于**：执行计算、逻辑处理的 JS 代码，适合无浏览器依赖的场景。

