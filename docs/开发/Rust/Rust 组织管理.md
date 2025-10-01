<font style="color:rgb(51, 51, 51);">任何一门编程语言如果不能组织代码都是难以深入的，几乎没有一个软件产品是由一个源文件编译而成的。</font>

<font style="color:rgb(51, 51, 51);">本教程到目前为止所有的程序都是在一个文件中编写的，主要是为了方便学习 Rust 语言的语法和概念。</font>

<font style="color:rgb(51, 51, 51);">对于一个工程来讲，组织代码是十分重要的。</font>

<font style="color:rgb(51, 51, 51);">Rust 中有三个重要的组织概念：箱、包、模块。</font>

## <font style="color:rgb(51, 51, 51);">箱(Crate)</font>
<font style="color:rgb(51, 51, 51);">"箱"是二进制程序文件或者库文件，存在于"包"中。</font>

<font style="color:rgb(51, 51, 51);">"箱"是树状结构的，它的树根是编译器开始运行时编译的源文件所编译的程序。</font>

<font style="color:rgb(51, 51, 51);">注意："二进制程序文件"不一定是"二进制可执行文件"，只能确定是是包含目标机器语言的文件，文件格式随编译环境的不同而不同。</font>

## <font style="color:rgb(51, 51, 51);">包(Package)</font>
<font style="color:rgb(51, 51, 51);">当我们使用 Cargo 执行 new 命令创建 Rust 工程时，工程目录下会建立一个 Cargo.toml 文件。工程的实质就是一个包，包必须由一个 Cargo.toml 文件来管理，该文件描述了包的基本信息以及依赖项。</font>

<font style="color:rgb(51, 51, 51);">一个包最多包含一个库"箱"，可以包含任意数量的二进制"箱"，但是至少包含一个"箱"（不管是库还是二进制"箱"）。</font>

<font style="color:rgb(51, 51, 51);">当使用 cargo new 命令创建完包之后，src 目录下会生成一个 main.rs 源文件，Cargo 默认这个文件为二进制箱的根，编译之后的二进制箱将与包名相同。</font>

## <font style="color:rgb(51, 51, 51);">模块(Module)</font>
<font style="color:rgb(51, 51, 51);">对于一个软件工程来说，我们往往按照所使用的编程语言的组织规范来进行组织，组织模块的主要结构往往是树。Java 组织功能模块的主要单位是类，而 JavaScript 组织模块的主要方式是 function。</font>

<font style="color:rgb(51, 51, 51);">这些先进的语言的组织单位可以层层包含，就像文件系统的目录结构一样。Rust 中的组织单位是模块(Module)。</font>

```rust
mod nation {
    mod government {
        fn govern() {}
    }
    mod congress {
        fn legislate() {}
    }
    mod court {
        fn judicial() {}
    }
}
```

<font style="color:rgb(51, 51, 51);">这是一段描述法治国家的程序：国家(nation)包括政府(government)、议会(congress)和法院(court)，分别有行政、立法和司法的功能。我们可以把它转换成树状结构：</font>

```rust
nation
├── government
│ └── govern
├── congress
│ └── legislate
└── court
└── judicial
```

<font style="color:rgb(51, 51, 51);">在文件系统中，目录结构往往以斜杠在路径字符串中表示对象的位置，Rust 中的路径分隔符是 :: 。</font>

<font style="color:rgb(51, 51, 51);">路径分为绝对路径和相对路径。绝对路径从 crate 关键字开始描述。相对路径从 self 或 super 关键字或一个标识符开始描述。例如：</font>

crate::nation::government::govern();

<font style="color:rgb(51, 51, 51);">是描述 govern 函数的绝对路径，相对路径可以表示为：</font>

nation::government::govern();

<font style="color:rgb(51, 51, 51);">现在你可以尝试在一个源程序里定义类似的模块结构并在主函数中使用路径。</font>

<font style="color:rgb(51, 51, 51);">如果你这样做，你一定会发现它不正确的地方：government 模块和其中的函数都是私有(private)的，你不被允许访问它们。</font>

## <font style="color:rgb(51, 51, 51);">访问权限</font>
<font style="color:rgb(51, 51, 51);">Rust 中有两种简单的访问权：公共(public)和私有(private)。</font>

<font style="color:rgb(51, 51, 51);">默认情况下，如果不加修饰符，模块中的成员访问权将是私有的。</font>

<font style="color:rgb(51, 51, 51);">如果想使用公共权限，需要使用 pub 关键字。</font>

<font style="color:rgb(51, 51, 51);">对于私有的模块，只有在与其平级的位置或下级的位置才能访问，不能从其外部访问。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
mod nation {
    pub mod government {
        pub fn govern() {}
    }

    mod congress {
        pub fn legislate() {}
    }

    mod court {
        fn judicial() {
            super::congress::legislate();
        }
    }
}

fn main() {
    nation::government::govern();
}
```

<font style="color:rgb(51, 51, 51);">这段程序是能通过编译的。请注意观察 court 模块中 super 的访问方法。</font>

<font style="color:rgb(51, 51, 51);">如果模块中定义了结构体，结构体除了其本身是私有的以外，其字段也默认是私有的。所以如果想使用模块中的结构体以及其字段，需要 pub 声明：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}
pub fn eat_at_restaurant() {
    let mut meal = back_of_house::Breakfast::summer("Rye");
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);
}
fn main() {
    eat_at_restaurant()
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

I'd like Wheat toast please

<font style="color:rgb(51, 51, 51);">枚举类枚举项可以内含字段，但不具备类似的性质:</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
mod SomeModule {
    pub enum Person {
        King {
            name: String
        },
        Quene
    }
}

fn main() {
    let person = SomeModule::Person::King{
        name: String::from("Blue")
    };
    match person {
        SomeModule::Person::King {name} => {
            println!("{}", name);
        }
        _ => {}
    }
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

Blue

## <font style="color:rgb(51, 51, 51);">难以发现的模块</font>
<font style="color:rgb(51, 51, 51);">使用过 Java 的开发者在编程时往往非常讨厌最外层的 class 块——它的名字与文件名一模一样，因为它就表示文件容器，尽管它很繁琐但我们不得不写一遍来强调"这个类是文件所包含的类"。</font>

<font style="color:rgb(51, 51, 51);">不过这样有一些好处：起码它让开发者明明白白的意识到了类包装的存在，而且可以明确的描述类的继承关系。</font>

<font style="color:rgb(51, 51, 51);">在 Rust 中，模块就像是 Java 中的类包装，但是文件一开头就可以写一个主函数，这该如何解释呢？</font>

<font style="color:rgb(51, 51, 51);">每一个 Rust 文件的内容都是一个"难以发现"的模块。</font>

<font style="color:rgb(51, 51, 51);">让我们用两个文件来揭示这一点：</font>

## main.rs 文件
<font style="color:rgb(51, 51, 51);">// main.rs  
</font><font style="color:rgb(51, 51, 51);">mod second_module;  
</font><font style="color:rgb(51, 51, 51);">fn main() {  
</font><font style="color:rgb(51, 51, 51);">println!("This is the main module.");  
</font><font style="color:rgb(51, 51, 51);">println!("{}", second_module::message());  
</font><font style="color:rgb(51, 51, 51);">}</font>

## second_module.rs 文件
<font style="color:rgb(51, 51, 51);">// second_module.rs  
</font><font style="color:rgb(51, 51, 51);">pub fn message() -> String {  
</font><font style="color:rgb(51, 51, 51);">String::from("This is the 2nd module.")  
</font><font style="color:rgb(51, 51, 51);">}</font>

<font style="color:rgb(51, 51, 51);">运行结果：</font>

```rust
This is the main module.
This is the 2nd module.
```

## <font style="color:rgb(51, 51, 51);">use 关键字</font>
<font style="color:rgb(51, 51, 51);">use 关键字能够将模块标识符引入当前作用域：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
mod nation {
    pub mod government {
        pub fn govern() {}
    }
}

use crate::nation::government::govern;

fn main() {
    govern();
}
```

<font style="color:rgb(51, 51, 51);">这段程序能够通过编译。</font>

<font style="color:rgb(51, 51, 51);">因为 use 关键字把 govern 标识符导入到了当前的模块下，可以直接使用。</font>

<font style="color:rgb(51, 51, 51);">这样就解决了局部模块路径过长的问题。</font>

<font style="color:rgb(51, 51, 51);">当然，有些情况下存在两个相同的名称，且同样需要导入，我们可以使用 as 关键字为标识符添加别名：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
mod nation {
    pub mod government {
        pub fn govern() {}
    }
    pub fn govern() {}
}

use crate::nation::government::govern;
use crate::nation::govern as nation_govern;

fn main() {
    nation_govern();
    govern();
}
```

<font style="color:rgb(51, 51, 51);">这里有两个 govern 函数，一个是 nation 下的，一个是 government 下的，我们用 as 将 nation 下的取别名 nation_govern。两个名称可以同时使用。</font>

<font style="color:rgb(51, 51, 51);">use 关键字可以与 pub 关键字配合使用：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
mod nation {
    pub mod government {
        pub fn govern() {}
    }
    pub use government::govern;
}

fn main() {
    nation::govern();
}
```

## <font style="color:rgb(51, 51, 51);">引用标准库</font>
<font style="color:rgb(51, 51, 51);">Rust 官方标准库字典：</font>[<font style="color:rgb(51, 122, 183);">https://doc.rust-lang.org/stable/std/all.html</font>](https://doc.rust-lang.org/stable/std/all.html)

<font style="color:rgb(51, 51, 51);">在学习了本章的概念之后，我们可以轻松的导入系统库来方便的开发程序了：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::f64::consts::PI;

fn main() {
    println!("{}", (PI / 2.0).sin());
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

1

<font style="color:rgb(51, 51, 51);">所有的系统库模块都是被默认导入的，所以在使用的时候只需要使用 use 关键字简化路径就可以方便的使用了。</font>

