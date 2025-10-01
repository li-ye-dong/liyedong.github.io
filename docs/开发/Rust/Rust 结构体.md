<font style="color:rgb(51, 51, 51);">Rust 中的结构体(Struct)与元组(Tuple)都可以将若干个类型不一定相同的数据捆绑在一起形成整体，但结构体的每个成员和其本身都有一个名字，这样访问它成员的时候就不用记住下标了。元组常用于非定义的多值传递，而结构体用于规范常用的数据结构。结构体的每个成员叫做"字段"。</font>

## <font style="color:rgb(51, 51, 51);">结构体定义</font>
<font style="color:rgb(51, 51, 51);">这是一个结构体定义：</font>

```rust
struct Site {
    domain: String,
    name: String,
    nation: String,
    found: u32
}
```

<font style="color:rgb(51, 51, 51);">注意：如果你常用 C/C++，请记住在 Rust 里 struct 语句仅用来定义，不能声明示例，结尾不需要 ; 符号，而且每个字段定义之后用 , 分隔。</font>

## <font style="color:rgb(51, 51, 51);">结构体示例</font>
<font style="color:rgb(51, 51, 51);">Rust 很多地方受 JavaScript 影响，在示例化结构体的时候用 JSON 对象的 key: value 语法来实现定义：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
let nhooo = Site {
    domain: String::from("www.cainiaoplus.com"),
    name: String::from("nhooo"),
    nation: String::from("China"),
    found: 2013
};
```

<font style="color:rgb(51, 51, 51);">如果你不了解 JSON 对象，你可以不用管它，记住格式就可以了：</font>

```rust
结构体类名 {
    字段名 : 字段值,
    ...
}
```

<font style="color:rgb(51, 51, 51);">这样的好处是不仅使程序更加直观，还不需要按照定义的顺序来输入成员的值。</font>

<font style="color:rgb(51, 51, 51);">如果正在示例化的结构体有字段名称和现存变量名称一样的，可以简化书写：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
let domain = String::from("www.cainiaoplus.com");
let name = String::from("nhooo");
let nhooo = Site {
    domain,  // 等同于 domain : domain,
    name,    // 等同于 name : name,
    nation: String::from("China"),
    traffic: 2013
};
```

<font style="color:rgb(51, 51, 51);">有这样一种情况：你想要新建一个结构体的示例，其中大部分属性需要被设置成与现存的一个结构体属性一样，仅需更改其中的一两个字段的值，可以使用结构体更新语法：</font>

```rust
let site = Site {
    domain: String::from("www.cainiaoplus.com"),
    name: String::from("nhooo"),
    ..nhooo
};
```

<font style="color:rgb(51, 51, 51);">注意：..nhooo 后面不可以有逗号。这种语法不允许一成不变的复制另一个结构体示例，意思就是说至少重新设定一个字段的值才能引用其他示例的值。</font>

## <font style="color:rgb(51, 51, 51);">元组结构体</font>
<font style="color:rgb(51, 51, 51);">有一种更简单的定义和使用结构体的方式：</font>**<font style="color:rgb(51, 51, 51);">元组结构体</font>**<font style="color:rgb(51, 51, 51);">。</font>

<font style="color:rgb(51, 51, 51);">元组结构体是一种形式是元组的结构体。</font>

<font style="color:rgb(51, 51, 51);">与元组的区别是它有名字和固定的类型格式。它存在的意义是为了处理那些需要定义类型（经常使用）又不想太复杂的简单数据：</font>

```rust
struct Color(u8, u8, u8);
struct Point(f64, f64);
let black = Color(0, 0, 0);
let origin = Point(0.0, 0.0);
```

<font style="color:rgb(51, 51, 51);">"颜色"和"点坐标"是常用的两种数据类型，但如果示例化时写个大括号再写上两个名字就为了可读性牺牲了便捷性，Rust 不会遗留这个问题。元组结构体对象的使用方式和元组一样，通过 . 和下标来进行访问：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    struct Color(u8, u8, u8);
    struct Point(f64, f64);

    let black = Color(0, 0, 0);
    let origin = Point(0.0, 0.0);

    println!("black = ({}, {}, {})", black.0, black.1, black.2);
    println!("origin = ({}, {})", origin.0, origin.1);
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

```rust
black = (0, 0, 0)
origin = (0, 0)
```

## <font style="color:rgb(51, 51, 51);">结构体所有权</font>
<font style="color:rgb(51, 51, 51);">结构体必须掌握字段值所有权，因为结构体失效的时候会释放所有字段。</font>

<font style="color:rgb(51, 51, 51);">这就是为什么本章的案例中使用了 String 类型而不使用 &str 的原因。</font>

<font style="color:rgb(51, 51, 51);">但这不意味着结构体中不定义引用型字段，这需要通过"生命周期"机制来实现。</font>

<font style="color:rgb(51, 51, 51);">但现在还难以说明"生命周期"概念，所以只能在后面章节说明。</font>

## <font style="color:rgb(51, 51, 51);">输出结构体</font>
<font style="color:rgb(51, 51, 51);">调试中，完整地显示出一个结构体示例是非常有用的。但如果我们手动的书写一个格式会非常的不方便。所以 Rust 提供了一个方便地输出一整个结构体的方法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
#[derive(Debug)]

struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };

    println!("rect1 is {:?}", rect1);
}
```

<font style="color:rgb(51, 51, 51);">如第一行所示：一定要导入调试库</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">#[derive(Debug)]</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">，之后在 println 和 print 宏中就可以用 {:?} 占位符输出一整个结构体：</font>

rect1 is Rectangle { width: 30, height: 50 }

<font style="color:rgb(51, 51, 51);">如果属性较多的话可以使用另一个占位符 {:#?} 。</font>

<font style="color:rgb(51, 51, 51);">输出结果：</font>

```rust
rect1 is Rectangle {
    width: 30,
    height: 50
}
```

## <font style="color:rgb(51, 51, 51);">结构体方法</font>
<font style="color:rgb(51, 51, 51);">方法(Method)和函数(Function)类似，只不过它是用来操作结构体示例的。</font>

<font style="color:rgb(51, 51, 51);">如果你学习过一些面向对象的语言，那你一定很清楚函数一般放在类定义里并在函数中用 this 表示所操作的示例。</font>

<font style="color:rgb(51, 51, 51);">Rust 语言不是面向对象的，从它所有权机制的创新可以看出这一点。但是面向对象的珍贵思想可以在 Rust 实现。</font>

<font style="color:rgb(51, 51, 51);">结构体方法的第一个参数必须是 &self，不需声明类型，因为 self 不是一种风格而是关键字。</font>

<font style="color:rgb(51, 51, 51);">计算一个矩形的面积：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };
    println!("rect1's area is {}", rect1.area());
}
```

<font style="color:rgb(51, 51, 51);">输出结果：</font>

rect1's area is 1500

<font style="color:rgb(51, 51, 51);">请注意，在调用结构体方法的时候不需要填写 self ，这是出于对使用方便性的考虑。</font>

<font style="color:rgb(51, 51, 51);">一个多参数的实例：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn wider(&self, rect: &Rectangle) -> bool {
        self.width > rect.width
    }
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };
    let rect2 = Rectangle { width: 40, height: 20 };

    println!("{}", rect1.wider(&rect2));
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

false

<font style="color:rgb(51, 51, 51);">这个程序计算 rect1 是否比 rect2 更宽。</font>

## <font style="color:rgb(51, 51, 51);">结构体关联函数</font>
<font style="color:rgb(51, 51, 51);">之所以"结构体方法"不叫"结构体函数"是因为"函数"这个名字留给了这种函数：它在 impl 块中却没有 &self 参数。</font>

<font style="color:rgb(51, 51, 51);">这种函数不依赖示例，但是使用它需要声明是在哪个 impl 块中的。</font>

<font style="color:rgb(51, 51, 51);">一直使用的 String::from 函数就是一个"关联函数"。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn create(width: u32, height: u32) -> Rectangle {
        Rectangle { width, height }
    }
}

fn main() {
    let rect = Rectangle::create(30, 50);
    println!("{:?}", rect);
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

Rectangle { width: 30, height: 50 }

**<font style="color:rgb(51, 51, 51);">贴士：</font>**<font style="color:rgb(51, 51, 51);">结构体 impl 块可以写几次，效果相当于它们内容的拼接！</font>

## <font style="color:rgb(51, 51, 51);">单元结构体</font>
<font style="color:rgb(51, 51, 51);">结构体可以只作为一种象征而无需任何成员：</font>

struct UnitStruct;

<font style="color:rgb(51, 51, 51);">我们称这种没有身体的结构体为单元结构体（Unit Struct）。</font>

