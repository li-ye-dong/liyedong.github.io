<font style="color:rgb(51, 51, 51);">安全高效的处理并发是 Rust 诞生的目的之一，主要解决的是服务器高负载承受能力。</font>

<font style="color:rgb(51, 51, 51);">并发(concurrent)的概念是只程序不同的部分独立执行，这与并行(parallel)的概念容易混淆，并行强调的是"同时执行"。</font>

<font style="color:rgb(51, 51, 51);">并发往往会造成并行。</font>

<font style="color:rgb(51, 51, 51);">本章讲述与并发相关的编程概念和细节。</font>

## <font style="color:rgb(51, 51, 51);">线程</font>
<font style="color:rgb(51, 51, 51);">线程(thread)是一个程序中独立运行的一个部分。</font>

<font style="color:rgb(51, 51, 51);">线程不同于进程(process)的地方是线程是程序以内的概念，程序往往是在一个进程中执行的。</font>

<font style="color:rgb(51, 51, 51);">在有操作系统的环境中进程往往被交替地调度得以执行，线程则在进程以内由程序进行调度。</font>

<font style="color:rgb(51, 51, 51);">由于线程并发很有可能出现并行的情况，所以在并行中可能遇到的死锁、延宕错误常出现于含有并发机制的程序。</font>

<font style="color:rgb(51, 51, 51);">为了解决这些问题，很多其它语言（如 Java、C#）采用特殊的运行时(runtime)软件来协调资源，但这样无疑极大地降低了程序的执行效率。</font>

<font style="color:rgb(51, 51, 51);">C/C++ 语言在操作系统的最底层也支持多线程，且语言本身以及其编译器不具备侦察和避免并行错误的能力，这对于开发者来说压力很大，开发者需要花费大量的精力避免发生错误。</font>

<font style="color:rgb(51, 51, 51);">Rust 不依靠运行时环境，这一点像 C/C++ 一样。</font>

<font style="color:rgb(51, 51, 51);">但 Rust 在语言本身就设计了包括所有权机制在内的手段来尽可能地把最常见的错误消灭在编译阶段，这一点其他语言不具备。</font>

<font style="color:rgb(51, 51, 51);">但这不意味着我们编程的时候可以不小心，迄今为止由于并发造成的问题还没有在公共范围内得到完全解决，仍有可能出现错误，并发编程时要尽量小心！</font>

<font style="color:rgb(51, 51, 51);">Rust 中通过 std::thread::spawn 函数创建新进程：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::thread;
use std::time::Duration;

fn spawn_function() {
    for i in 0..5 {
        println!("spawned thread print {}", i);
        thread::sleep(Duration::from_millis(1));
    }
}

fn main() {
    thread::spawn(spawn_function);

    for i in 0..3 {
        println!("main thread print {}", i);
        thread::sleep(Duration::from_millis(1));
    }
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

```rust
main thread print 0
spawned thread print 0
main thread print 1
spawned thread print 1
main thread print 2
spawned thread print 2
```

<font style="color:rgb(51, 51, 51);">这个结果在某些情况下顺序有可能变化，但总体上是这样打印出来的。</font>

<font style="color:rgb(51, 51, 51);">此程序有一个子线程，目的是打印 5 行文字，主线程打印三行文字，但很显然随着主线程的结束，spawn 线程也随之结束了，并没有完成所有打印。</font>

<font style="color:rgb(51, 51, 51);">std::thread::spawn 函数的参数是一个无参函数，但上述写法不是推荐的写法，我们可以使用闭包(closures)来传递函数作为参数：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 0..5 {
            println!("spawned thread print {}", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 0..3 {
        println!("main thread print {}", i);
        thread::sleep(Duration::from_millis(1));
    }
}
```

<font style="color:rgb(51, 51, 51);">闭包是可以保存进变量或作为参数传递给其他函数的匿名函数。闭包相当于 Rust 中的 Lambda 表达式，格式如下：</font>

```rust
|参数1, 参数2, ...| -> 返回值类型 {
    // 函数体
}
```

<font style="color:rgb(51, 51, 51);">例如：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    let inc = |num: i32| -> i32 {
        num + 1
    };
    println!("inc(5) = {}", inc(5));
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

inc(5) = 6

<font style="color:rgb(51, 51, 51);">闭包可以省略类型声明使用 Rust 自动类型判断机制：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
fn main() {
    let inc = |num| {
        num + 1
    };
    println!("inc(5) = {}", inc(5));
}
```

<font style="color:rgb(51, 51, 51);">结果没有变化。</font>

## <font style="color:rgb(51, 51, 51);">join 方法</font>
**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 0..5 {
            println!("spawned thread print {}", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 0..3 {
        println!("main thread print {}", i);
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

```rust
main thread print 0 
spawned thread print 0 
spawned thread print 1 
main thread print 1 
spawned thread print 2 
main thread print 2 
spawned thread print 3 
spawned thread print 4
```

<font style="color:rgb(51, 51, 51);">join 方法可以使子线程运行结束后再停止运行程序。</font>

## <font style="color:rgb(51, 51, 51);">move 强制所有权迁移</font>
<font style="color:rgb(51, 51, 51);">这是一个经常遇到的情况：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::thread;

fn main() {
    let s = "hello";

    let handle = thread::spawn(|| {
        println!("{}", s);
    });

    handle.join().unwrap();
}
```

<font style="color:rgb(51, 51, 51);">在子线程中尝试使用当前函数的资源，这一定是错误的！因为所有权机制禁止这种危险情况的产生，它将破坏所有权机制销毁资源的一定性。我们可以使用闭包的 move 关键字来处理：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::thread;

fn main() {
    let s = "hello";

    let handle = thread::spawn(move || {
        println!("{}", s);
    });

    handle.join().unwrap();
}
```

## <font style="color:rgb(51, 51, 51);">消息传递</font>
<font style="color:rgb(51, 51, 51);">Rust 中一个实现消息传递并发的主要工具是通道(channel)，通道有两部分组成，一个发送者(transmitter)和一个接收者(receiver)。</font>

<font style="color:rgb(51, 51, 51);">std::sync::mpsc 包含了消息传递的方法：</font>

**<font style="color:rgb(51, 51, 51);background-color:rgb(239, 239, 239);">示例</font>**

```rust
use std::thread;
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Got: {}", received);
}
```

<font style="color:rgb(51, 51, 51);">运行结果：</font>

Got: hi

<font style="color:rgb(51, 51, 51);">子线程获得了主线程的发送者 tx，并调用了它的 send 方法发送了一个字符串，然后主线程就通过对应的接收者 rx 接收到了。</font>

