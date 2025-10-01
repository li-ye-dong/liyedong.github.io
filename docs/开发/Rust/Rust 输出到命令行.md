<font style="color:rgb(51, 51, 51);">在正式学习 Rust 语言以前，我们需要先学会怎样输出一段文字到命令行，这几乎是学习每一门语言之前必备的技能，因为输出到命令行几乎是语言学习阶段程序表达结果的唯一方式。</font>

<font style="color:rgb(51, 51, 51);">在之前的 Hello, World 程序中大概已经告诉了大家输出字符串的方式，但并不全面，大家可能很疑惑为什么 println!( "Hello World") 中的 println 后面还有一个 ! 符号，难道 Rust 函数之后都要加一个感叹号？显然并不是这样。println 不是一个函数，而是一个宏规则。这里不需要更深刻的挖掘宏规则是什么，后面的章节中会专门介绍，并不影响接下来的一段学习。</font>

<font style="color:rgb(51, 51, 51);">Rust 输出文字的方式主要有两种：println!() 和 print!()。这两个"函数"都是向命令行输出字符串的方法，区别仅在于前者会在输出的最后附加输出一个换行符。当用这两个"函数"输出信息的时候，第一个参数是格式字符串，后面是一串可变参数，对应着格式字符串中的"占位符"，这一点与 C 语言中的 printf 函数很相似。但是，Rust 中格式字符串中的占位符不是"% + 字母"的形式，而是一对 {}。</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```plain
fn main() { 
    let a = 12; 
    println!("a is {}", a); 
}
```

<font style="color:rgb(51, 51, 51);">以上程序的输出结果是：</font>

a is 12

<font style="color:rgb(51, 51, 51);">如果我想把 a 输出两遍，那岂不是要写成：</font>

println!("a is {}, a again is {}", a, a);

<font style="color:rgb(51, 51, 51);">其实有更好的写法：</font>

println!("a is {0}, a again is {0}", a);

<font style="color:rgb(51, 51, 51);">在 {} 之间可以放一个数字，它将把之后的可变参数当作一个数组来访问，下标从 0 开始。</font>

<font style="color:rgb(51, 51, 51);">如果要输出</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">{</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">或</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">}</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">怎么办呢？格式字符串中通过</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">{{</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(51, 51, 51);"> </font>**<font style="color:rgb(51, 51, 51);">}}</font>**<font style="color:rgb(51, 51, 51);"> </font><font style="color:rgb(51, 51, 51);">分别转义代表 { 和 }。但是其他常用转义字符与 C 语言里的转义字符一样，都是反斜杠开头的形式。</font>

```plain
fn main() { 
    println!("{{}}"); 
}
```

<font style="color:rgb(51, 51, 51);">以上程序的输出结果是：</font>

{}

