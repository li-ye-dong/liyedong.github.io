<font style="color:rgb(51, 51, 51);">Rust 生命周期机制是与所有权机制同等重要的资源管理机制。</font>

<font style="color:rgb(51, 51, 51);">之所以引入这个概念主要是应对复杂类型系统中资源管理的问题。</font>

<font style="color:rgb(51, 51, 51);">引用是对待复杂类型时必不可少的机制，毕竟复杂类型的数据不能被处理器轻易地复制和计算。</font>

<font style="color:rgb(51, 51, 51);">但引用往往导致极其复杂的资源管理问题，首先认识一下垂悬引用：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
{
    let r;

    {
        let x = 5;
        r = &x;
    }

    println!("r: {}", r);
}
```

<font style="color:rgb(51, 51, 51);">这段代码是不会通过 Rust 编译器的，原因是 r 所引用的值已经在使用之前被释放。</font>

<font style="color:rgb(51, 51, 51);">上图中的绿色范围 'a 表示 r 的生命周期，蓝色范围 'b 表示 x 的生命周期。很显然，'b 比 'a 小得多，引用必须在值的生命周期以内才有效。</font>

<font style="color:rgb(51, 51, 51);">一直以来我们都在结构体中使用 String 而不用 &str，我们用一个案例解释原因：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn longer(s1: &str, s2: &str) -> &str {
    if s2.len() > s1.len() {
        s2
    } else {
        s1
    }
}
```

<font style="color:rgb(51, 51, 51);">longer 函数取 s1 和 s2 两个字符串切片中较长的一个返回其引用值。但只这段代码不会通过编译，原因是返回值引用可能会返回过期的引用：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    let r;
    {
        let s1 = "rust";
        let s2 = "ecmascript";
        r = longer(s1, s2);
    }
    println!("{} is longer", r);
}
```

<font style="color:rgb(51, 51, 51);">这段程序中虽然经过了比较，但 r 被使用的时候源值 s1 和 s2 都已经失效了。当然我们可以把 r 的使用移到 s1 和 s2 的生命周期范围以内防止这种错误的发生，但对于函数来说，它并不能知道自己以外的地方是什么情况，它为了保障自己传递出去的值是正常的，必选所有权原则消除一切危险，所以 longer 函数并不能通过编译。</font>

## <font style="color:rgb(51, 51, 51);">生命周期注释</font>
<font style="color:rgb(51, 51, 51);">生命周期注释是描述引用生命周期的办法。</font>

<font style="color:rgb(51, 51, 51);">虽然这样并不能够改变引用的生命周期，但可以在合适的地方声明两个引用的生命周期一致。</font>

<font style="color:rgb(51, 51, 51);">生命收起注释用单引号开头，跟着一个小写字母单词：</font>

```rust
&i32        // 常规引用
&'a i32     // 含有生命周期注释的引用
&'a mut i32 // 可变型含有生命周期注释的引用
```

<font style="color:rgb(51, 51, 51);">让我们用生命周期注释改造 longer 函数：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn longer<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s2.len() > s1.len() {
        s2
    } else {
        s1
    }
}
```

<font style="color:rgb(51, 51, 51);">我们需要用泛型声明来规范生命周期的名称，随后函数返回值的生命周期将与两个参数的生命周期一致，所以在调用时可以这样写：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    let r;
    {
        let s1 = "rust";
        let s2 = "ecmascript";
        r = longer(s1, s2);
        println!("{} is longer", r);
    }
}
```

<font style="color:rgb(51, 51, 51);">以上两段程序结合的运行结果：</font>

ecmascript is longer

**<font style="color:rgb(51, 51, 51);">注意：</font>**<font style="color:rgb(51, 51, 51);">别忘记了自动类型判断的原则。</font>

## <font style="color:rgb(51, 51, 51);">结构体中使用字符串切片引用</font>
<font style="color:rgb(51, 51, 51);">这是之前留下的疑问，在此解答：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    struct Str<'a> {
        content: &'a str
    }
    let s = Str {
        content: "string_slice"
    };
    println!("s.content = {}", s.content);
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

s.content = string_slice

<font style="color:rgb(51, 51, 51);">如果对结构体 Str 有方法定义：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
impl<'a> Str<'a> {
    fn get_content(&self) -> &str {
        self.content
    }
}
```

<font style="color:rgb(51, 51, 51);">这里返回值并没有生命周期注释，但是加上也无妨。这是一个历史问题，早期 Rust 不支持生命周期自动判断，所有的生命周期必须严格声明，但主流稳定版本的 Rust 已经支持了这个功能。</font>

## <font style="color:rgb(51, 51, 51);">静态生命周期</font>
<font style="color:rgb(51, 51, 51);">生命周期注释有一个特别的：'static 。所有用双引号包括的字符串常量所代表的精确数据类型都是 &'static str ，'static 所表示的生命周期从程序运行开始到程序运行结束。</font>

## <font style="color:rgb(51, 51, 51);">泛型、特性与生命周期协同作战</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(x: &'a str, y: &'a str, ann: T) -> &'a str
    where T: Display
    {
        println!("Announcement! {}", ann);
        if x.len() > y.len() {
            x
        } else {
            y
        }
    }
```

<font style="color:rgb(51, 51, 51);">这段程序出自 Rust 圣经，是一个同时使用了泛型、特性、生命周期机制的程序，不强求，可以体验，毕竟早晚用得到！</font>

