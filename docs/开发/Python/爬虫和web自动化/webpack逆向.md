## Webpack 逆向工程的概述
Webpack 在打包时会将原始代码和模块信息打包成一个或多个文件。逆向工程的目的是解读这些打包文件，还原各模块的结构和功能。Webpack 通过模块 ID 和 Webpack 调度器（runtime）来管理模块依赖，逆向时需要重点分析调度器和模块定义部分。

## 逆向步骤
### 关键步骤
1. **识别 Webpack 调度器**：
+ Webpack 通过一个调度器函数（通常形如 `webpackJsonp`、`webpack_require` 等）来调用和管理各个模块，逆向时首先识别出此调度器。
+ Webpack 调度器负责加载模块、解析依赖，通过 `module.exports` 和 `__webpack_require__` 实现模块加载与调用。
2. **提取模块映射**：
+ Webpack 将各模块以 `{ module_id: function(module, exports, __webpack_require__) {...} }` 的形式定义，模块 ID 可能是整型或字符串。
+ 通过提取这些模块映射关系，可以还原出各模块的原始代码。
3. **分析模块 ID 和依赖关系**：
+ Webpack 调用模块时通常使用 `__webpack_require__(module_id)` 的形式，逆向时需要分析模块 ID 与模块内容之间的映射，弄清依赖关系。
+ 追踪 `__webpack_require__` 的调用，了解模块加载的流程。
4. **还原核心逻辑**：
+ 对于核心功能代码，Webpack 通常会对其混淆或压缩。可以通过反混淆工具（如 `js-beautify`）还原其结构，或通过断点调试进行代码还原。
5. **补充运行环境**：
+ Webpack 打包的代码一般运行于浏览器环境，逆向时可以通过 `jsdom` 等工具在 Node.js 中模拟浏览器环境，减少缺少 `window`、`document` 等对象的报错。
+ 可以创建 `env.js` 文件，补充所需的环境变量或对象。

## 个人逆向步骤
#### 步骤 1：识别加密结构
首先查看加密代码的形式。通常，通过 `a=n('1234')`、`a=n('abc')` 形式对函数进行调用，如果代码形如 `a.getEncrypt(username+password)`，说明 `n` 是一个 Webpack 调度器对象，它将各个函数以 `k:v` 对象的形式存储，例如 `n('1234'): function(){...}`。

快速查找a对象的webpack调度对象,使用正则

```plain
 a = [a-zA-Z0-9]+(\((["\w\d]+)\))\s*$
```

#### 步骤 2：准备环境文件
新建四个 JS 文件，分别是：

+ `**env.js**`：用于存放环境变量。
+ `**loader.js**`：用于存放主要加载代码。
+ `**module1.js**`：用于存放拆解后的各个库函数，如果有多个module，则使用`module2.js等`。
+ `**app.js**`：用于执行主程序和测试输出。

#### 步骤 3：拦截调度对象
在代码中对 `a=n['1234']` 或类似的代码打上断点。断点触发后，定位 `n` 的源代码。将整个源 JS 文件内容复制到 `loader.js`，这一部分代码是webpack的loader，便于进行下一步分析。

#### 步骤 4：补充环境变量
在 `env.js` 中补充缺少的环境变量，如 `window=global`，模拟浏览器环境。 在 `loader.js` 中的 `call` 调用处对变量进行 `console.log` 打印，以追踪加载时缺少的环境或对象。

```plain
function o(t){
  ...
  console.log("t::",t)
}
```

#### 步骤 5：赋值window.loader
在 `loader.js` 中调度器函数下方添加`window.loader=o` o是调度器函数。

#### 步骤 6：检查自执行函数是否有其他初始化操作
在`loader.js` 中，查看自执行函数中，是否存在一个调度器函数的执行如`o(xxx)` 或者 `o(xx=xx` 注释掉以后，继续下一步。

#### 步骤 7：追踪依赖函数
在 `app.js` 中调用 `console.log(window.loader('1234'))`  来查看控制台输出。若输出缺少特定的 Webpack 库（如 `'4321'`），则在源代码中全局搜索 `1234`，找到对应的函数，并将其添加到 `module1.js` 中。（pass:如果有很多未知对象，可能是浏览器对象，简单阅读后进行注释，跳过，继续执行）

#### 步骤 8：运行并补充缺少的环境
不断运行 `app.js`，根据报错信息逐步补全缺少的环境。具体可使用对象监视工具或调试器跟踪调用缺失的依赖。



### Webpack 逆向的常用技巧
+ **源码美化**：使用 `js-beautify` 等工具对压缩代码格式化，使代码结构更清晰。
+ **断点调试**：在浏览器中利用调试工具，结合 `source maps`，找到加密逻辑和解密函数。
+ **自动化提取模块**：编写脚本提取 Webpack 的模块映射，便于逐个分析模块。
+ **动态分析**：通过打断点、监控函数调用栈，可以识别核心函数及参数，逆向核心加密逻辑。

## 环境补充方法
在 Node.js 环境下通过 `jsdom` 模拟浏览器环境来减少调试工作：

1. **安装 **`**jsdom**`：

```javascript
npm install jsdom
```

2. **设置环境变量**：  
在 `env.js` 中通过 `const { JSDOM } = require('jsdom')` 创建一个 `window` 对象，模拟浏览器 DOM 环境。
3. **补充其他缺失对象**：  
可能还会缺少 `document`、`location` 等对象，使用 `jsdom` 创建 `window.document`、`window.location` 等来模拟实际运行环境。

```javascript
// env.js
const { JSDOM } = require('jsdom');
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
window = global;
global.document = dom.window.document;

// loader.js
function xxx(){
  xxx.call(i);
  console.log("i::",i);
}
window.loader=xxx


// module1.js
// 假设 '1234' 对应的函数
n['1234'] = function() {
  console.log('Function 1234 executed');
};

// app.js
require('./env.js');
require('./loader.js');
require('./module1.js');
console.log(n['1234']());  // 测试调用
console.log(window.loader)
```

