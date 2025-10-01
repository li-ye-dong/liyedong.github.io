👌 来了，给你整理一份 **Go 开发技巧对照表**，左边是常见坑点（很多初学者或者写快了容易犯），右边是推荐的正确写法，方便你快速查错。

---

# 🐹 Go 开发技巧对照表（坑点 vs 正确写法）
| 类别 | 坑点写法 🚨 | 正确写法 ✅ | 说明 |
| --- | --- | --- | --- |
| **变量声明** | `var x int; x = 10` | `x := 10` | 用短变量声明更简洁。 |
| **未使用变量** | `var tmp = 123`<br/>（编译报错） | `_ = tmp` | Go 不允许声明未使用变量，必要时用 `_`<br/> 占位。 |
| **字符串拼接** | `s += "a"; s += "b"` | `var sb strings.Builder; sb.WriteString("a"); sb.WriteString("b"); s := sb.String()` | 避免频繁拷贝，性能差。 |
| **方法接收者** | `func (s server) Run() { s.name = "xxx" }` | `func (s *server) Run() { s.name = "xxx" }` | 值接收者修改不会影响外部，通常用指针接收者。 |
| **跨包调用** | `utils.myFunc()`<br/>（小写函数） | `utils.MyFunc()`<br/>（首字母大写） | 导出标识符必须首字母大写。 |
| **map 并发写** | `m := make(map[string]int); go func(){ m["a"]=1 }()` | `var m sync.Map; m.Store("a",1)`<br/> 或加锁 | 原生 map 不是线程安全的。 |
| **for range 闭包** | `for i := 0; i < 3; i++ { go func(){ fmt.Println(i) }() }`<br/>（打印 333） | `for i := 0; i < 3; i++ { i := i; go func(){ fmt.Println(i) }() }` | 闭包会捕获同一个变量，要重新声明。 |
| **错误包装** | `return fmt.Errorf("failed: %v", err)` | `return fmt.Errorf("failed: %w", err)` | 用 `%w`<br/> 才能被 `errors.Is/As`<br/> 解包。 |
| **defer 顺序** | `defer fmt.Println("A"); defer fmt.Println("B")`<br/> → 输出 A B？（错，输出 B A） | 知道 defer 是 **后进先出** | 经常被考，执行顺序要注意。 |
| **资源泄漏** | `f, _ := os.Open("file")`<br/>（没关闭） | `f, _ := os.Open("file"); defer f.Close()` | 一定要用 `defer`<br/> 关闭文件/连接。 |
| **超时控制** | 手写 `time.After`<br/> + `select` | 用 `context.WithTimeout` | context 更统一、可传递。 |
| **panic 恢复** | 直接 `recover()` | 在 defer 中调用：`defer func(){ if r:=recover(); r!=nil { log.Println(r) } }()` | `recover()`<br/> 必须在 `defer`<br/> 内才能生效。 |
| **slice 扩容** | 手动循环 append | 预分配容量：`make([]int,0,100)` | 避免频繁扩容导致 GC 压力。 |
| **json 序列化** | `type User struct { Name string }`<br/>（Name 小写字段） | `type User struct { Name string `json:"name"` }` | json 包只导出大写字段，要写 tag。 |
| **time.Sleep** | 直接阻塞：`time.Sleep(time.Second*5)` | 用 `context.WithTimeout`<br/> 或 `ticker` | 更灵活，支持取消。 |
| **goroutine 泄漏** | 开 goroutine 没有退出条件 | 用 `ctx.Done()`<br/> 控制退出 | 防止 goroutine 一直挂着。 |


---

### 🔑 总结
+ **变量**：少写冗余，用 `:=` 简洁。
+ **方法接收者**：默认用 `*T`，避免值拷贝。
+ **跨包**：首字母大写才导出。
+ **并发**：注意 `map` 不是线程安全，`for` 闭包坑很常见。
+ **错误处理**：用 `%w` 包装，方便追踪。
+ **资源释放**：`defer` 是标配。
+ **context**：推荐全局用来做取消/超时。

---

要不要我再帮你出一份 **Go 并发专属坑点对照表**（专门列 goroutine、channel、锁的常见坑）？

