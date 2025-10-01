<font style="color:rgb(51, 51, 51);">面向对象的编程语言通常实现了数据的封装与继承并能基于数据调用方法。</font>

<font style="color:rgb(51, 51, 51);">Rust 不是面向对象的编程语言，但这些功能都得以实现。</font>

## <font style="color:rgb(51, 51, 51);">封装</font>
<font style="color:rgb(51, 51, 51);">封装就是对外显示的策略，在 Rust 中可以通过模块的机制来实现最外层的封装，并且每一个 Rust 文件都可以看作一个模块，模块内的元素可以通过 pub 关键字对外明示。这一点在"组织管理"章节详细叙述过。</font>

<font style="color:rgb(51, 51, 51);">"类"往往是面向对象的编程语言中常用到的概念。"类"封装的是数据，是对同一类数据实体以及其处理方法的抽象。在 Rust 中，我们可以使用结构体或枚举类来实现类的功能：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
pub struct ClassName {
    pub field: Type,
}

pub impl ClassName {
    fn some_method(&self) {
        // 方法函数体
    }
}

pub enum EnumName {
    A,
    B,
}

pub impl EnumName {
    fn some_method(&self) {

    } 
}
```

<font style="color:rgb(51, 51, 51);">下面建造一个完整的类：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
second.rs
    pub struct ClassName {
    field: i32,
    }

    impl ClassName {
        pub fn new(value: i32) -> ClassName {
            ClassName {
                field: value
            }
        }

        pub fn public_method(&self) {
            println!("from public method");
            self.private_method();
        }

        fn private_method(&self) {
            println!("from private method");
        }
    }
    main.rs
    mod second;
use second::ClassName;

fn main() {
    let object = ClassName::new(1024);
    object.public_method();
}
```

<font style="color:rgb(51, 51, 51);">输出结果：</font>

```rust
from public method
from private method
```

## <font style="color:rgb(51, 51, 51);">继承</font>
<font style="color:rgb(51, 51, 51);">几乎其他的面向对象的编程语言都可以实现"继承"，并用"extend"词语来描述这个动作。</font>

<font style="color:rgb(51, 51, 51);">继承是多态(Polymorphism)思想的实现，多态指的是编程语言可以处理多种类型数据的代码。在 Rust 中，通过特性(trait)实现多态。有关特性的细节已在"特性"章节给出。但是特性无法实现属性的继承，只能实现类似于"接口"的功能，所以想继承一个类的方法最好在"子类"中定义"父类"的示例。</font>

<font style="color:rgb(51, 51, 51);">总结地说，Rust 没有提供跟继承有关的语法糖，也没有官方的继承手段（完全等同于 Java 中的类的继承），但灵活的语法依然可以实现相关的功能。</font>

