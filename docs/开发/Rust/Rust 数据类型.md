<font style="color:rgb(51, 51, 51);">Rust 语言中的基础数据类型有以下几种。</font>

## <font style="color:rgb(51, 51, 51);">整数型(Integer)</font>
<font style="color:rgb(51, 51, 51);">整数型简称整型，按照比特位长度和有无符号分为一下种类：</font>

| <font style="color:rgb(254, 254, 254);">位长度</font> | <font style="color:rgb(254, 254, 254);">有符号</font> | <font style="color:rgb(254, 254, 254);">无符号</font> |
| --- | --- | --- |
| <font style="color:rgb(51, 51, 51);">8-bit</font> | <font style="color:rgb(51, 51, 51);">i8</font> | <font style="color:rgb(51, 51, 51);">u8</font> |
| <font style="color:rgb(51, 51, 51);">16-bit</font> | <font style="color:rgb(51, 51, 51);">i16</font> | <font style="color:rgb(51, 51, 51);">u16</font> |
| <font style="color:rgb(51, 51, 51);">32-bit</font> | <font style="color:rgb(51, 51, 51);">i32</font> | <font style="color:rgb(51, 51, 51);">u32</font> |
| <font style="color:rgb(51, 51, 51);">64-bit</font> | <font style="color:rgb(51, 51, 51);">i64</font> | <font style="color:rgb(51, 51, 51);">u64</font> |
| <font style="color:rgb(51, 51, 51);">128-bit</font> | <font style="color:rgb(51, 51, 51);">i128</font> | <font style="color:rgb(51, 51, 51);">u128</font> |
| <font style="color:rgb(51, 51, 51);">arch</font> | <font style="color:rgb(51, 51, 51);">isize</font> | <font style="color:rgb(51, 51, 51);">usize</font> |


<font style="color:rgb(51, 51, 51);">isize 和 usize 两种整数类型是用来衡量数据大小的，它们的位长度取决于所运行的目标平台，如果是 32 位架构的处理器将使用 32 位位长度整型。</font>

<font style="color:rgb(51, 51, 51);">整数的表述方法有以下几种：</font>

| <font style="color:rgb(254, 254, 254);">进制</font> | <font style="color:rgb(254, 254, 254);">例</font> |
| --- | --- |
| <font style="color:rgb(51, 51, 51);">十进制</font> | <font style="color:rgb(51, 51, 51);">98_222</font> |
| <font style="color:rgb(51, 51, 51);">十六进制</font> | <font style="color:rgb(51, 51, 51);">0xff</font> |
| <font style="color:rgb(51, 51, 51);">八进制</font> | <font style="color:rgb(51, 51, 51);">0o77</font> |
| <font style="color:rgb(51, 51, 51);">二进制</font> | <font style="color:rgb(51, 51, 51);">0b1111_0000</font> |
| <font style="color:rgb(51, 51, 51);">字节(只能表示 u8 型)</font> | <font style="color:rgb(51, 51, 51);">b'A'</font> |


<font style="color:rgb(51, 51, 51);">很显然，有的整数中间存在一个下划线，这种设计可以让人们在输入一个很大的数字时更容易判断数字的值大概是多少。</font>

## <font style="color:rgb(51, 51, 51);">浮点数型(Floating-Point)</font>
<font style="color:rgb(51, 51, 51);">Rust 与其它语言一样支持 32 位浮点数(f32)和 64 位浮点数(f64)。默认情况下，64.0 将表示 64 位浮点数，因为现代计算机处理器对两种浮点数计算的速度几乎相同，但 64 位浮点数精度更高。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    let x = 2.0; // f64
    let y: f32 = 3.0; // f32
}
```

## <font style="color:rgb(51, 51, 51);">数学运算</font>
<font style="color:rgb(51, 51, 51);">用一段程序反应数学运算：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() { 
    let sum = 5 + 10; // 加 
    let difference = 95.5 - 4.3; // 减 
    let product = 4 * 30; // 乘 
    let quotient = 56.7 / 32.2; // 除 
    let remainder = 43 % 5; // 求余
}
```

<font style="color:rgb(51, 51, 51);">许多运算符号之后加上 = 号是自运算的意思，例如：</font>

<font style="color:rgb(51, 51, 51);">sum += 1 等同于 sum = sum + 1。</font>

**<font style="color:rgb(51, 51, 51);">注意：</font>**<font style="color:rgb(51, 51, 51);">Rust 不支持</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">++</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">--</font>**<font style="color:rgb(51, 51, 51);">，因为这两个运算符出现在变量的前后会影响代码可读性，减弱了开发者对变量改变的意识能力。</font>

## <font style="color:rgb(51, 51, 51);">布尔型</font>
<font style="color:rgb(51, 51, 51);">布尔型用 bool 表示，值只能为 true 或 false。</font>

## <font style="color:rgb(51, 51, 51);">字符型</font>
<font style="color:rgb(51, 51, 51);">字符型用 char 表示。</font>

<font style="color:rgb(51, 51, 51);">Rust的 char 类型大小为 4 个字节，代表 Unicode标量值，这意味着它可以支持中文，日文和韩文字符等非英文字符甚至表情符号和零宽度空格在 Rust 中都是有效的 char 值。</font>

<font style="color:rgb(51, 51, 51);">Unicode 值的范围从 U+0000 到 U+D7FF 和 U+E000 到 U+10FFFF （包括两端）。 但是，"字符"这个概念并不存在于 Unicode 中，因此您对"字符"是什么的直觉可能与Rust中的字符概念不匹配。所以一般推荐使用字符串储存 UTF-8 文字（非英文字符尽可能地出现在字符串中）。</font>

**<font style="color:rgb(51, 51, 51);">注意：</font>**<font style="color:rgb(51, 51, 51);">由于中文文字编码有两种（GBK 和 UTF-8），所以编程中使用中文字符串有可能导致乱码的出现，这是因为源程序与命令行的文字编码不一致，所以在 Rust 中字符串和字符都必须使用 UTF-8 编码，否则编译器会报错。</font>

## <font style="color:rgb(51, 51, 51);">复合类型</font>
<font style="color:rgb(51, 51, 51);">元组用一对 ( ) 包括的一组数据，可以包含不同种类的数据：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
let tup: (i32, f64, u8) = (500, 6.4, 1);
// tup.0 等于 500
// tup.1 等于 6.4
// tup.2 等于 1
let (x, y, z) = tup;
// y 等于 6.4
```

<font style="color:rgb(51, 51, 51);">数组用一对 [ ] 包括的同类型数据。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
let a = [1, 2, 3, 4, 5];
// a 是一个长度为 5 的整型数组

let b = ["January", "February", "March"];
// b 是一个长度为 3 的字符串数组

let c: [i32; 5] = [1, 2, 3, 4, 5];
// c 是一个长度为 5 的 i32 数组

let d = [3; 5];
// 等同于 let d = [3, 3, 3, 3, 3];

let first = a[0];
let second = a[1];
// 数组访问

a[0] = 123; // 错误：数组 a 不可变
let mut a = [1, 2, 3];
a[0] = 4; // 正确
```

