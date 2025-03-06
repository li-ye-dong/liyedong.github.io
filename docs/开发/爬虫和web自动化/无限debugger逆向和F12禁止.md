## 概述
反爬技术中，会有禁止调试的选项，如禁止F12，无限debugger，都会影响到我们断点调试，本次介绍如何绕过无限debugger，和页面禁止使用F12如何逆向。

## 逆向无限debugger
使用js注入，将debugger函数进行重写，注入后即可正常断点

```javascript
let _Function = Function;
// 重写 Function 构造函数
Function = function (s) {
  // 如果传入字符串为 "debugger"，则输出日志并返回 null
  if (s === "debugger") {
    console.log(s);
    return null;
  }
  // 否则执行原始 Function 构造函数
  return _Function(s);
};

let _constructor = Function.prototype.constructor;
// 重写 Function.prototype.constructor
Function.prototype.constructor = function (s) {
  if (s === "debugger") {
    console.log(s);
    return null;
  }
  return _constructor(s);
};

```

## F12禁止
+ **通过右键菜单打开开发者工具：** 即使F12被禁用，通常可以通过右键点击页面空白处，选择“检查”或“Inspect”来打开开发者工具。
+ **移除键盘事件监听器：** 如果页面通过JavaScript监听并阻止F12键，可以注入以下代码来移除这些监听器：

```javascript
// 移除所有的键盘事件监听器
window.onkeydown = null;
window.onkeypress = null;
window.onkeyup = null;

// 如果使用了addEventListener绑定事件
const events = ['keydown', 'keypress', 'keyup'];
events.forEach(event => {
  window.removeEventListener(event, someFunction); // 需要知道具体的处理函数
});
```

**注意：** 有时事件处理函数是匿名的，无法直接移除。这时可以重载事件处理器：

```javascript
window.addEventListener('keydown', function(event) {
  if (event.key === 'F12') {
    event.preventDefault();
  }
}, true);
```

通过在捕获阶段覆盖之前的事件处理，可以阻止F12被禁用。

+ **使用浏览器扩展或开发者工具的独立功能：** 一些浏览器扩展可以帮助绕过这些限制，或者使用浏览器内置的功能，如`Ctrl+Shift+I`（Windows）或`Cmd+Option+I`（Mac）来打开开发者工具。

