## nvm安装和使用


```plain
https://github.com/coreybutler/nvm-windows/releases
```

```shell
nvm list	查看已经安装的版本
nvm list installed	查看已经安装的版本
nvm list available	查看网络可以安装的版本
nvm arch	查看当前系统的位数和当前nodejs的位数
nvm install [arch]	安装制定版本的node 并且可以指定平台 version 版本号 arch 平台
nvm on	打开nodejs版本控制
nvm off	关闭nodejs版本控制
nvm proxy [url]	查看和设置代理
nvm node_mirror [url]	设置或者查看setting.txt中的node_mirror，如果不设置的默认是 https://nodejs.org/dist/
nvm npm_mirror [url]	设置或者查看setting.txt中的npm_mirror,如果不设置的话默认的是：https://github.com/npm/npm/archive/.
nvm uninstall	卸载指定的版本
nvm use [version] [arch]	切换指定的node版本和位数
nvm root [path]	设置和查看root路径
nvm version	查看当前的版本

```

## npm和pnpm修改国内源


```plain
npm config set registry https://registry.npmmirror.com
pnpm config set registry https://registry.npmmirror.com

```



## vue3项目创建


> 前提条件
>
>  
>
> + 熟悉命令行
> + 已安装 16.0 或更高版本的 Node.js
>



```powershell
npm init vue@latest  #这一指令将会安装并执行 create-vue，它是 Vue 官方的项目脚手架工具。
```



```plain
Project name：------》项目名称，默认值：vue-project，可输入想要的项目名称，此处我写的是：vueproject1。
Add TypeScript? ------》是否加入TypeScript组件？默认值：No。
Add JSX Support? ------》是否加入JSX支持？默认值：No。
Add Vue Router for Single Page Application development? ------》是否为单页应用程序开发添加Vue Router路由管理组件？默认值：No。
Add Pinia for state management? ------》是否添加Pinia组件来进行状态管理？默认值：No。
Add Vitest for Unit testing? ------》是否添加Vitest来进行单元测试？默认值：No。
Add an End-to-End Testing Solution?------》是否添加端到端测试？默认值No。
Add ESLint for code quality? ------》是否添加ESLint来进行代码质量检查？默认值：No。
```



脚手架工程项目在指定位置被创建好。



在项目被创建后，通过以下步骤安装依赖并启动开发服务器：



```powershell
Done. Now run:
  cd vueproject1
  npm install 安装依赖
  npm run dev 运行开发
  npm run build 打包
```



## vue-router使用
```plain

```

## vue-pinia使用


main.js引入使用



```javascript
// 导入pinia
import * as Pinia from  'pinia'



// 创建app
import { createSSRApp } from 'vue'
// 导入创建app方法
export function createApp() {
	// 创建app实例
  const app = createSSRApp(App)
  // 创建pinia实例
  const pinia =  Pinia.createPinia();
  // 使用pinia
  app.use(pinia);
   // 添加一个全局的的方法
   app.config.globalProperties.$reverse = function(str){
	   return str.split('').reverse().join('');
   }
	// 返回了app
  return {
    app,
	Pinia
  }
}
```



### nvm使用淘宝源


```plain
nvm node_mirror https://cdn.npmmirror.com/binaries/node/
nvm npm_mirror https://cdn.npmmirror.com/binaries/npm/
```

### settings.txt
```shell
root: D:\Program Files\Nvm\nvm
arch: 64
proxy: none
originalpath: .
originalversion: 
node_mirror: https://cdn.npmmirror.com/binaries/node/
npm_mirror: https://cdn.npmmirror.com/binaries/npm/
```

