👌 我帮你整理成表格形式，方便快速查阅：

---

## 🔹 Alpine.js 首页核心语法速览
### 1. Attributes（15 个）
| Attribute | 描述 |
| --- | --- |
| `x-data` | 声明一个 Alpine 组件（数据作用域） |
| `x-bind` | 将 HTML 属性绑定到表达式值 |
| `x-on` | 绑定事件监听器 |
| `x-text` | 设置元素的 `textContent` |
| `x-html` | 设置元素的 `innerHTML` |
| `x-model` | 表单控件双向数据绑定 |
| `x-show` | 控制元素显示/隐藏（`display:none`<br/>） |
| `x-transition` | 添加显示/隐藏过渡动画 |
| `x-for` | 循环渲染元素 |
| `x-if` | 条件渲染（插入/移除 DOM 节点） |
| `x-init` | 初始化时执行表达式 |
| `x-effect` | 数据变化时执行副作用 |
| `x-ref` | 定义元素引用，便于访问 |
| `x-cloak` | 隐藏元素直到 Alpine 初始化完成 |
| `x-ignore` | 忽略某些元素，不让 Alpine 处理 |


---

### 2. Properties（6 个）
| Property | 描述 |
| --- | --- |
| `$store` | 访问全局存储（跨组件共享状态） |
| `$el` | 当前元素的引用 |
| `$dispatch` | 触发自定义事件 |
| `$watch` | 监听表达式的变化 |
| `$refs` | 访问通过 `x-ref`<br/> 声明的元素集合 |
| `$nextTick` | DOM 更新完成后执行回调 |


---

### 3. Methods（2 个）
| Method | 描述 |
| --- | --- |
| `Alpine.data` | 定义一个可复用的数据组件 |
| `Alpine.store` | 定义一个全局存储（共享数据） |


---

要不要我再帮你写一个 **最小 Django 模板示例**，用到这些 Alpine.js 语法（比如按钮计数、条件显示、循环渲染），让你直观感受？





## demo.html
```python
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>Alpine.js Demo</title>
  <script src="https://unpkg.com/alpinejs" defer></script>
  <style>
    [x-cloak] { display: none; } /* 确保 x-cloak 生效 */
    .box { padding: 10px; margin: 5px; border: 1px solid #ddd; }
  </style>
</head>
<body class="p-4">

  <!-- x-data, x-text, x-on, x-model, x-show, x-transition -->
  <div x-data="{ count: 0, show: true, inputText: '' }" class="box">
    <h2>基础交互</h2>
    <button @click="count++">加一</button>
    <p>计数：<span x-text="count"></span></p>

    <button @click="show = !show">切换显示</button>
    <p x-show="show" x-transition>我会显示/隐藏</p>

    <input type="text" x-model="inputText" placeholder="输入点什么">
    <p>你输入的内容是：<span x-text="inputText"></span></p>
  </div>

  <!-- x-html -->
  <div x-data="{ html: '<strong>加粗文本</strong>' }" class="box">
    <h2>x-html 示例</h2>
    <div x-html="html"></div>
  </div>

  <!-- x-for, x-if -->
  <div x-data="{ items: ['苹果','香蕉','橘子'], showList: true }" class="box">
    <h2>循环与条件渲染</h2>
    <button @click="showList = !showList">切换列表</button>
    <template x-if="showList">
      <ul>
        <template x-for="(item, i) in items" :key="i">
          <li x-text="item"></li>
        </template>
      </ul>
    </template>
  </div>

  <!-- x-init, x-effect -->
  <div x-data="{ msg: '初始值', time: '' }" 
       x-init="time = new Date().toLocaleTimeString()" 
       x-effect="console.log('msg 改变:', msg)" class="box">
    <h2>初始化与副作用</h2>
    <p>初始化时间：<span x-text="time"></span></p>
    <input x-model="msg">
  </div>

  <!-- x-ref, $refs, $el, $nextTick -->
  <div x-data="{ focusInput() { this.$refs.myInput.focus() }, msg: '' }" class="box">
    <h2>元素引用与属性</h2>
    <input x-ref="myInput" placeholder="点按钮自动聚焦">
    <button @click="focusInput()">聚焦输入框</button>
    <p>当前元素：<span x-text="$el.tagName"></span></p>
    <button @click="$nextTick(() => msg='DOM 已更新')">触发 nextTick</button>
    <span x-text="msg"></span>
  </div>

  <!-- x-cloak, x-ignore -->
  <div x-data="{ loaded: false }" x-init="setTimeout(() => loaded = true, 1000)" class="box">
    <h2>cloak 与 ignore</h2>
    <p x-cloak>加载中...</p>
    <p x-show="loaded">页面加载完成</p>
    <div x-ignore>
      <p>这里不会被 Alpine.js 处理</p>
    </div>
  </div>

  <!-- $dispatch, $watch -->
  <div x-data="{ msg: '' }" x-init="$watch('msg', val => console.log('msg 变化:', val))" class="box">
    <h2>事件与监听</h2>
    <input x-model="msg" placeholder="输入触发 $watch">
    <button @click="$dispatch('custom', { foo: 'bar' })">派发自定义事件</button>
  </div>

  <!-- $store, Alpine.store, Alpine.data -->
  <script>
    document.addEventListener('alpine:init', () => {
      Alpine.store('counter', { total: 0 })
      Alpine.data('counterBox', () => ({
        inc() { this.$store.counter.total++ }
      }))
    })
  </script>

  <div x-data="counterBox" class="box">
    <h2>全局存储与复用组件</h2>
    <button @click="inc()">增加全局计数</button>
    <p>全局计数：<span x-text="$store.counter.total"></span></p>
  </div>

</body>
</html>

```

