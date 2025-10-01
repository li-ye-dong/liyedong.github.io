<font style="color:rgb(51, 51, 51);">泛型是一个编程语言不可或缺的机制。</font>

<font style="color:rgb(51, 51, 51);">C++ 语言中用"模板"来实现泛型，而 C 语言中没有泛型的机制，这也导致 C 语言难以构建类型复杂的工程。</font>

<font style="color:rgb(51, 51, 51);">泛型机制是编程语言用于表达类型抽象的机制，一般用于功能确定、数据类型待定的类，如链表、映射表等。</font>

## <font style="color:rgb(51, 51, 51);">在函数中定义泛型</font>
<font style="color:rgb(51, 51, 51);">这是一个对整型数字选择排序的方法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn max(array: &[i32]) -> i32 {
    let mut max_index = 0;
    let mut i = 1;
    while i < array.len() {
        if array[i] > array[max_index] {
            max_index = i;
        }
        i += 1;
    }
    array[max_index]
}

fn main() {
    let a = [2, 4, 6, 3, 1];
    println!("max = {}", max(&a));
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

max = 6

<font style="color:rgb(51, 51, 51);">这是一个简单的取最大值程序，可以用于处理 i32 数字类型的数据，但无法用于 f64 类型的数据。通过使用泛型我们可以使这个函数可以利用到各个类型中去。但实际上并不是所有的数据类型都可以比大小，所以接下来一段代码并不是用来运行的，而是用来描述一下函数泛型的语法格式：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn max<T>(array: &[T]) -> T {
    let mut max_index = 0;
    let mut i = 1;
    while i < array.len() {
        if array[i] > array[max_index] {
            max_index = i;
        }
        i += 1;
    }
    array[max_index]
}
```

## <font style="color:rgb(51, 51, 51);">结构体与枚举类中的泛型</font>
<font style="color:rgb(51, 51, 51);">在之前我们学习的 Option 和 Result 枚举类就是泛型的。</font>

<font style="color:rgb(51, 51, 51);">Rust 中的结构体和枚举类都可以实现泛型机制。</font>

```rust
struct Point<T> {
    x: T,
    y: T
}
```

<font style="color:rgb(51, 51, 51);">这是一个点坐标结构体，T 表示描述点坐标的数字类型。我们可以这样使用：</font>

```rust
let p1 = Point {x: 1, y: 2};
let p2 = Point {x: 1.0, y: 2.0};
```

<font style="color:rgb(51, 51, 51);">使用时并没有声明类型，这里使用的是自动类型机制，但不允许出现类型不匹配的情况如下：</font>

let p = Point {x: 1, y: 2.0};

<font style="color:rgb(51, 51, 51);">x 与 1 绑定时就已经将 T 设定为 i32，所以不允许再出现 f64 的类型。如果我们想让 x 与 y 用不同的数据类型表示，可以使用两个泛型标识符：</font>

```rust
struct Point<T1, T2> {
    x: T1,
    y: T2
}
```

<font style="color:rgb(51, 51, 51);">在枚举类中表示泛型的方法诸如 Option 和 Result：</font>

```rust
enum Option<T> {
    Some(T),
    None,
}
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

<font style="color:rgb(51, 51, 51);">结构体与枚举类都可以定义方法，那么方法也应该实现泛型的机制，否则泛型的类将无法被有效的方法操作。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

fn main() {
    let p = Point { x: 1, y: 2 };
    println!("p.x = {}", p.x());
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

p.x = 1

<font style="color:rgb(51, 51, 51);">注意，impl 关键字的后方必须有 <T>，因为它后面的 T 是以之为榜样的。但我们也可以为其中的一种泛型添加方法：</font>

```rust
impl Point<f64> {
    fn x(&self) -> f64 {
        self.x
    }
}
```

<font style="color:rgb(51, 51, 51);">impl 块本身的泛型并没有阻碍其内部方法具有泛型的能力：</font>

```rust
impl<T, U> Point<T, U> {
    fn mixup<V, W>(self, other: Point<V, W>) -> Point<T, W> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}
```

<font style="color:rgb(51, 51, 51);">方法 mixup 将一个 Point<T, U> 点的 x 与 Point<V, W> 点的 y 融合成一个类型为 Point<T, W> 的新点。</font>

## <font style="color:rgb(51, 51, 51);">特性</font>
<font style="color:rgb(51, 51, 51);">特性(trait)概念接近于 Java 中的接口(Interface)，但两者不完全相同。特性与接口相同的地方在于它们都是一种行为规范，可以用于标识哪些类有哪些方法。</font>

<font style="color:rgb(51, 51, 51);">特性在 Rust 中用 trait 表示：</font>

```rust
trait Descriptive {
    fn describe(&self) -> String;
}
```

<font style="color:rgb(51, 51, 51);">Descriptive 指定了实现者必须有是 describe(&self) -> String 方法。</font>

<font style="color:rgb(51, 51, 51);">我们用它实现一个结构体：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
struct Person {
    name: String,
    age: u8
}

impl Descriptive for Person {
    fn describe(&self) -> String {
        format!("{} {}", self.name, self.age)
    }
}
```

<font style="color:rgb(51, 51, 51);">格式是：</font>

impl <特性名> for <所实现的类型名>

<font style="color:rgb(51, 51, 51);">Rust 同一个类可以实现多个特性，每个 impl 块只能实现一个。</font>

## <font style="color:rgb(51, 51, 51);">默认特性</font>
<font style="color:rgb(51, 51, 51);">这是特性与接口的不同点：接口只能规范方法而不能定义方法，但特性可以定义方法作为默认方法，因为是"默认"，所以对象既可以重新定义方法，也可以不重新定义方法使用默认的方法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
trait Descriptive {
    fn describe(&self) -> String {
        String::from("[Object]")
    }
}

struct Person {
    name: String,
    age: u8
}

impl Descriptive for Person {
    fn describe(&self) -> String {
        format!("{} {}", self.name, self.age)
    }
}

fn main() {
    let cali = Person {
        name: String::from("Cali"),
        age: 24
    };
    println!("{}", cali.describe());
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

Cali 24

<font style="color:rgb(51, 51, 51);">如果我们将 impl Descriptive for Person 块中的内容去掉，那么运行结果就是：</font>

[Object]

## <font style="color:rgb(51, 51, 51);">特性做参数</font>
<font style="color:rgb(51, 51, 51);">很多情况下我们需要传递一个函数做参数，例如回调函数、设置按钮事件等。在 Java 中函数必须以接口实现的类示例来传递，在 Rust 中可以通过传递特性参数来实现：</font>

```rust
fn output(object: impl Descriptive) {
    println!("{}", object.describe());
}
```

<font style="color:rgb(51, 51, 51);">任何实现了 Descriptive 特性的对象都可以作为这个函数的参数，这个函数没必要了解传入对象有没有其他属性或方法，只需要了解它一定有 Descriptive 特性规范的方法就可以了。当然，此函数内也无法使用其他的属性与方法。</font>

<font style="color:rgb(51, 51, 51);">特性参数还可以用这种等效语法实现：</font>

```rust
fn output<T: Descriptive>(object: T) {
    println!("{}", object.describe());
}
```

<font style="color:rgb(51, 51, 51);">这是一种风格类似泛型的语法糖，这种语法糖在有多个参数类型均是特性的情况下十分实用：</font>

```rust
fn output_two<T: Descriptive>(arg1: T, arg2: T) {
    println!("{}", arg1.describe());
    println!("{}", arg2.describe());
}
```

<font style="color:rgb(51, 51, 51);">特性作类型表示时如果涉及多个特性，可以用 + 符号表示，例如：</font>

```rust
fn notify(item: impl Summary + Display)
    fn notify<T: Summary + Display>(item: T)
```

**<font style="color:rgb(51, 51, 51);">注意：</font>**<font style="color:rgb(51, 51, 51);">仅用于表示类型的时候，并不意味着可以在 impl 块中使用。</font>

<font style="color:rgb(51, 51, 51);">复杂的实现关系可以使用 where 关键字简化，例如：</font>

fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U)

<font style="color:rgb(51, 51, 51);">可以简化成：</font>

```rust
fn some_function<T, U>(t: T, u: U) -> i32
    where T: Display + Clone,
    U: Clone + Debug
```

<font style="color:rgb(51, 51, 51);">在了解这个语法之后，泛型章节中的"取最大值"案例就可以真正实现了：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
trait Comparable {
    fn compare(&self, object: &Self) -> i8;
}

fn max<T: Comparable>(array: &[T]) -> &T {
    let mut max_index = 0;
    let mut i = 1;
    while i < array.len() {
        if array[i].compare(&array[max_index]) > 0 {
            max_index = i;
        }
        i += 1;
    }
    &array[max_index]
}

impl Comparable for f64 {
    fn compare(&self, object: &f64) -> i8 {
        if &self > &object { 1 }
        else if &self == &object { 0 }
        else { -1 }
    }
}

fn main() {
    let arr = [1.0, 3.0, 5.0, 4.0, 2.0];
    println!("maximum of arr is {}", max(&arr));
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

maximum of arr is 5

**<font style="color:rgb(51, 51, 51);">Tip:</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">由于需要声明 compare 函数的第二参数必须与实现该特性的类型相同，所以 Self （注意大小写）关键字就代表了当前类型（不是示例）本身。</font>

## <font style="color:rgb(51, 51, 51);">特性做返回值</font>
<font style="color:rgb(51, 51, 51);">特性做返回值格式如下：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn person() -> impl Descriptive {
    Person {
        name: String::from("Cali"),
        age: 24
    }
}
```

<font style="color:rgb(51, 51, 51);">但是有一点，特性做返回值只接受实现了该特性的对象做返回值且在同一个函数中所有可能的返回值类型必须完全一样。比如结构体 A 与结构体 B 都实现了特性 Trait，下面这个函数就是错误的：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn some_function(bool bl) -> impl Descriptive {
    if bl {
        return A {};
    } else {
        return B {};
    }
}
```

## <font style="color:rgb(51, 51, 51);">有条件实现方法</font>
<font style="color:rgb(51, 51, 51);">impl 功能十分强大，我们可以用它实现类的方法。但对于泛型类来说，有时我们需要区分一下它所属的泛型已经实现的方法来决定它接下来该实现的方法：</font>

```rust
struct A<T> {}
impl<T: B + C> A<T> {
    fn d(&self) {}
}
```

<font style="color:rgb(51, 51, 51);">这段代码声明了 A<T> 类型必须在 T 已经实现 B 和 C 特性的前提下才能有效实现此 impl 块。</font>

