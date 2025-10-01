<font style="color:rgb(51, 51, 51);">函数在 Rust 语言中是普遍存在的。</font>

<font style="color:rgb(51, 51, 51);">通过之前的章节已经可以了解到 Rust 函数的基本形式：</font>

fn <函数名> ( <参数> ) <函数体>

<font style="color:rgb(51, 51, 51);">其中 Rust 函数名称的命名风格是小写字母以下划线分割：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    println!("Hello, world!");
    another_function();
}

fn another_function() {
    println!("Hello, nhooo!");
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

```rust
Hello, world!
    Hello, nhooo!
```

<font style="color:rgb(51, 51, 51);">注意，我们在源代码中的 main 函数之后定义了another_function。 Rust不在乎您在何处定义函数，只需在某个地方定义它们即可。</font>

## <font style="color:rgb(51, 51, 51);">函数参数</font>
<font style="color:rgb(51, 51, 51);">Rust 中定义函数如果需要具备参数必须声明参数名称和类型：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    another_function(5, 6);
}

fn another_function(x: i32, y: i32) {
    println!("x 的值为 : {}", x);
    println!("y 的值为 : {}", y);
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

```rust
x 的值为 : 5
y 的值为 : 6
```

## <font style="color:rgb(51, 51, 51);">函数体的语句和表达式</font>
<font style="color:rgb(51, 51, 51);">Rust 函数体由一系列可以以表达式(Expression)结尾的语句(Statement)组成。到目前为止，我们仅见到了没有以表达式结尾的函数，但已经将表达式用作语句的一部分。</font>

<font style="color:rgb(51, 51, 51);">语句是执行某些操作且没有返回值的步骤。例如：</font>

let a = 6;

<font style="color:rgb(51, 51, 51);">这个步骤没有返回值，所以以下语句不正确：</font>

let a = (let b = 2);

<font style="color:rgb(51, 51, 51);">表达式有计算步骤且有返回值。以下是表达式（假设出现的标识符已经被定义）：</font>

```rust
a = 7
b + 2
c * (a + b)
```

<font style="color:rgb(51, 51, 51);">Rust 中可以在一个用 {} 包括的块里编写一个较为复杂的表达式：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    let x = 5;

    let y = {
        let x = 3;
        x + 1
    };

    println!("x 的值为 : {}", x);
    println!("y 的值为 : {}", y);
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

```rust
x 的值为 : 5
y 的值为 : 4
```

<font style="color:rgb(51, 51, 51);">很显然，这段程序中包含了一个表达式块：</font>

```rust
{
    let x = 3;
    x + 1
};
```

<font style="color:rgb(51, 51, 51);">而且在块中可以使用函数语句，最后一个步骤是表达式，此表达式的结果值是整个表达式块所代表的值。这种表达式块叫做函数体表达式。</font>

<font style="color:rgb(51, 51, 51);">注意：x + 1 之后没有分号，否则它将变成一条语句！</font>

<font style="color:rgb(51, 51, 51);">这种表达式块是一个合法的函数体。而且在 Rust 中，函数定义可以嵌套：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    fn five() -> i32 {
        5
    }
    println!("five() 的值为: {}", five());
}
```

## <font style="color:rgb(51, 51, 51);">函数返回值</font>
<font style="color:rgb(51, 51, 51);">在上一个嵌套的实例中已经显示了 Rust 函数声明返回值类型的方式：在参数声明之后用 -> 来声明函数返回值的类型（不是 : ）。</font>

<font style="color:rgb(51, 51, 51);">在函数体中，随时都可以以 return 关键字结束函数运行并返回一个类型合适的值。这也是最接近大多数开发者经验的做法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn add(a: i32, b: i32) -> i32 {
    return a + b;
}
```

<font style="color:rgb(51, 51, 51);">但是 Rust 不支持自动返回值类型判断！如果没有明确声明函数返回值的类型，函数将被认为是"纯过程"，不允许产生返回值，return 后面不能有返回值表达式。这样做的目的是为了让公开的函数能够形成可见的公报。</font>

**<font style="color:rgb(51, 51, 51);">注意：</font>**<font style="color:rgb(51, 51, 51);">函数体表达式并不能等同于函数体，它不能使用 </font>**<font style="color:rgb(51, 51, 51);">return 关键字。</font>**

