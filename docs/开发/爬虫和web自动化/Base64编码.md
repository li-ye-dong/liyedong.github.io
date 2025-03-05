# 概述和原理
Base64 编码是一种将二进制数据转换为 ASCII 字符串的编码方式，主要用于在网络上传输和存储数据时避免出现非可打印字符。它的原理如下：

1. **输入数据**：Base64 编码将输入数据（通常是字节流）分为每组 3 个字节（24 位）。
2. **转换为 6 位块**：将这 24 位分为 4 个 6 位块（每个块对应一个 Base64 字符）。如果输入数据不是 3 的倍数，最后的块会用零填充。
3. **查表转换**：使用 Base64 编码表（包含 64 个字符：A-Z, a-z, 0-9, + 和 /）将每个 6 位块转换为一个字符。
4. **输出**：将转换后的字符连接起来，形成最终的 Base64 编码字符串。如果原始数据的长度不是 3 的倍数，Base64 编码结果会在末尾添加一个或两个等号（`=`）作为填充，以确保输出长度为 4 的倍数。

### Base64 编码示例
假设我们要编码字符串 "Man"：

1. **转换为字节**：`M` -> 01001101, `a` -> 01100001, `n` -> 01101110
2. **合并为一个 24 位二进制**：

```python
01001101 01100001 01101110
```

3. **分为 6 位块**：

```python
010011 010110 000101 101110
```

4. **查表转换**：
    - 010011 -> 19 -> T
    - 010110 -> 22 -> W
    - 000101 -> 5  -> F
    - 101110 -> 46 -> u
5. **最终结果**：字符串 "Man" 的 Base64 编码是 `TWFu`。

Base64 编码的应用场景包括电子邮件、数据 URI、XML 和 JSON 数据等，能够有效地将二进制数据嵌入到文本中。

# Python
## 编码和解码
```python
s4 = "我爱你中国！@alex"
ret06 = base64.b64encode(s4.encode("GBK")).decode()
print(ret06)
# base64解码
ret07 = base64.b64decode(ret06)
print(ret07.decode("GBK"))

```

## 编码的长度
```python
import base64
from Crypto.Util.Padding import pad
# s = "ztKwrsTj1tC5+qOhQGFsZXg="
# print(len(s))

s1 = "ztKwrsTj1tC5+qOhQGFsZXg"
print(len(s1))

# 解码之前一定要确认数据长度是4的倍数

s1 += (4 - len(s1) % 4) * "="
ret = base64.b64decode(s1).decode("GBK")
print(ret)
```

## 编码变种
```python
import base64

s = "Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6JKK7ArS9fJXAcsG7ufBIE0gd6fbnhFcsGmdXspZe-8 whVFbRB_8Fc9JlMHh8DDXnskDhGfEscN_rfi-A-AHB3F9Vets82vIYpkGNaJOft_JA-m5cGEjo-UNRDDpkTz_NIAvo5PbATpkh7PSna2tHcE6Hou9GBtPLB67vjScwplB96-zqZKXJJEzU5HGF0oPDY_weAkXArzXyGLBPXFCnn_IWJDkGD4vqBQQAh2n52f48GD_cb-PSCT_8b-ESsKUI9NJa11XsdaUZxAc8TzrYnXwdcQbtl_kZGKhS6_rCtuNEBouA_lvM2CbS7TTtV2U4zVmJKpp-c6nt3yZePK3Av01GWn1pH_3sZbaPEx8DUjSbdp4i4iK-Mj4p2HPoph67DR7B9MFETYku_28SgP9xsKRRvFH4aHBHESWX4FDbwaU="

s = s.replace("-", "+").replace("_", "/")
ret = base64.b64decode(s)
print(ret)

```

## base64编码图片
```python
import base64
s = "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAA7VBMVEUAAAD////////s8v////+txP+qwv+4zf/w9f/2+P+hu//Q3f+yyP+4zf/Q3f////+kvv+90P+80f+2yv/S4P/T4P/M2//z9/+cuP/V4P9Whv////9Uhf9Sg/9Pgf9NgP/8/f9di/9Xh/9lkf5aif9qlP7z9//k7P/c5v+2y/94nv51nP6lv/+LrP6Ep/6BpP5gjf7v9P+wxv/U4f/M2/+sxP+vxv73+f/P3v/J2v+5zf+ivP+fuv9xmf+Ytv6Usv6Hqf58of5vl/7m7v/g6f+zyf6QsP75+//q8P/B0v/W4//C1P6+0P6qwv6ct/76fHZiAAAAGnRSTlMAGAaVR/Py45aC9Mfy2b8t9OPZ2ce/v4L0x/e74/EAAAIZSURBVDjLZVPXYuIwEDSmQ4BLv5O0ku3Yhwu2IZTQe0hy7f8/57QSoYR5sVea1c424wgzl324LRRuH7I507hEJluYucCFEOBGhWzmy7X5+N0WwIjTbrcdBsKulM0z96onGCGE2X6n+cTkj/CqJ480igzkNXp26E9JkABSbBz8i4Bn3EkH840mKHoxs49fZQzt2Kd03FQEzSB3WsejB9Jqf1CJQBM0wCurABWBoub0gkDENwyStTHA62pwSWDtklRQ4FLfjnaiPqVW60hAYeLKNHIREOZuKTL80H6XBFCwn4BAmDOyLiOQUIlOSEjaoS+Ju57NZuul73Fml4w6yAivSLBW3MGfcfBmIegmArg3alICdJHgy1jQt8Z/6CcC4DdGXhLIoiWRACpbLYbDYW80GnXp2GH8ShP+PUvEoHsAIFq9Xm8+kXlIwkkI9pm+05Tm3yWqu9EiB0pkwjWBx2i+tND1XqeZqpPU4VhUbq/ekR8CwTRVoRxf3ifTbeIwcONNsJZ2lxFVKDMv1KNvS2zXdrnD+COvR1PQpTZKNlKD3cLCOJNnivgVxkw169BunlKFaV9/B+LQbqOsByY4IVgDB59dl/cjR9TIJV1Lh7CGqUqH/DDPhhZYOPkdLz6m0X7GrzPHsSe6zJwzxvm+5NeNi8U5ABfn7mz7zHJFrZ6+BY6rd7m8kQtcAtwwXzq4n69/vZbP1+pn6/8fsrRmHUhmpYYAAAAASUVORK5CYII="

# print(base64.b64decode(s))
with open("a.png","wb") as f:
    f.write(base64.b64decode(s))
```

# JavaScript
```javascript
// 定义要编码的字符串
const data = "Hello, World!";

// 编码
const encodedData = btoa(data);  // 使用 btoa 进行 Base64 编码
console.log("Encoded:", encodedData);

// 解码
const decodedData = atob(encodedData);  // 使用 atob 进行 Base64 解码
console.log("Decoded:", decodedData);

```

