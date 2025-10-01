<font style="color:rgb(51, 51, 51);">变量，基本类型，函数，注释和控制流，这些几乎是每种编程语言都具有的编程概念。</font>

<font style="color:rgb(51, 51, 51);">这些基础概念将存在于每个 Rust 程序中，及早学习它们将使你以最快的速度学习 Rust 的使用。</font>

## <font style="color:rgb(51, 51, 51);">变量</font>
<font style="color:rgb(51, 51, 51);">首先必须说明，Rust 是强类型语言，但具有自动判断变量类型的能力。这很容易让人与弱类型语言产生混淆。</font>

<font style="color:rgb(51, 51, 51);">如果要声明变量，需要使用 let 关键字。例如：</font>

let a = 123;

<font style="color:rgb(51, 51, 51);">只学习过 JavaScript 的开发者对这句话很敏感，只学习过 C 语言的开发者对这句话很不理解。</font>

<font style="color:rgb(51, 51, 51);">在这句声明语句之后，以下三行代码都是被禁止的：</font>

```rust
a = "abc";
a = 4.56; 
a = 456;
```

<font style="color:rgb(51, 51, 51);">第一行的错误在于当声明 a 是 123 以后，a 就被确定为整型数字，不能把字符串类型的值赋给它。</font>

<font style="color:rgb(51, 51, 51);">第二行的错误在于自动转换数字精度有损失，Rust 语言不允许精度有损失的自动数据类型转换。</font>

<font style="color:rgb(51, 51, 51);">第三行的错误在于 a 不是个可变变量。</font>

<font style="color:rgb(51, 51, 51);">前两种错误很容易理解，但第三个是什么意思？难道 a 不是个变量吗？</font>

<font style="color:rgb(51, 51, 51);">这就牵扯到了 Rust 语言为了高并发安全而做的设计：在语言层面尽量少的让变量的值可以改变。所以 a 的值不可变。但这不意味着 a 不是"变量"（英文中的 variable），官方文档称 a 这种变量为"不可变变量"。</font>

<font style="color:rgb(51, 51, 51);">如果我们编写的程序的一部分在假设值永远不会改变的情况下运行，而我们代码的另一部分在改变该值，那么代码的第一部分可能就不会按照设计的意图去运转。由于这种原因造成的错误很难在事后找到。这是 Rust 语言设计这种机制的原因。</font>

<font style="color:rgb(51, 51, 51);">当然，使变量变得"可变"(mutable)只需一个 mut 关键字。</font>

```rust
let mut a = 123;
a = 456;
```

<font style="color:rgb(51, 51, 51);">这个程序是正确的。</font>

## <font style="color:rgb(51, 51, 51);">常量与不可变变量的区别</font>
<font style="color:rgb(51, 51, 51);">既然不可变变量是不可变的，那不就是常量吗？为什么叫变量？</font>

<font style="color:rgb(51, 51, 51);">变量和常量还是有区别的。在 Rust 中，以下程序是合法的：</font>

```rust
let a = 123;
let a = 456;
```

<font style="color:rgb(51, 51, 51);">但是如果 a 是常量就不合法：</font>

```rust
const a: i32 = 123;
let a = 456;
```

<font style="color:rgb(51, 51, 51);">变量的值可以"重新绑定"，但在"重新绑定"以前不能私自被改变，这样可以确保在每一次"绑定"之后的区域里编译器可以充分的推理程序逻辑。 虽然 Rust 有自动判断类型的功能，但有些情况下声明类型更加方便：</font>

let a: u64 = 123;

<font style="color:rgb(51, 51, 51);">这里声明了 a 为无符号 64 位整型变量，如果没有声明类型，a 将自动被判断为有符号 32 位整型变量，这对于 a 的取值范围有很大的影响。</font>

## <font style="color:rgb(51, 51, 51);">重影(Shadowing)</font>
<font style="color:rgb(51, 51, 51);">重影的概念与其他面向对象语言里的"重写"(Override)或"重载"(Overload)是不一样的。重影就是刚才讲述的所谓"重新绑定"，之所以加引号就是为了在没有介绍这个概念的时候代替一下概念。</font>

<font style="color:rgb(51, 51, 51);">重影就是指变量的名称可以被重新使用的机制：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    let x = 5;
    let x = x + 1;
    let x = x * 2;
    println!("The value of x is: {}", x);
}
```

<font style="color:rgb(51, 51, 51);">这段程序的运行结果：</font>

The value of x is: 12

<font style="color:rgb(51, 51, 51);">重影与可变变量的赋值不是一个概念，重影是指用同一个名字重新代表另一个变量实体，其类型、可变属性和值都可以变化。但可变变量赋值仅能发生值的变化。</font>

```rust
let mut s = "123";
s = s.len();
```

<font style="color:rgb(51, 51, 51);">这段程序会出错：不能给字符串变量赋整型值。</font>

