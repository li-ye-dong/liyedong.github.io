## 概述
在js逆向分析过程中，经常需要根据对象的调用顺序来进行判断缺少哪些环境，但是调用出错只会有错误如`undifent`这类的报错，经常不知道是缺少什么对象的什么属性值，此时需要js对象监视器，监视这个对象的set和get方法的执行。

## Proxy代理
```javascript
var yuan = {
    username: "yuan",
    age: 22
}
var alex = {
    username: "alex",
    age: 42
}

yuan = new Proxy(yuan, {
    get(target, p, receiver) {
        // console.log(target, p, receiver)
        console.log("target: ", target);
        console.log("p: ", p);
        return Reflect.get(target,p)
    },
    set(target, p, value, receiver) {

    }
});

alex = new Proxy(alex, {
    get(target, p, receiver) {
        // console.log(target, p, receiver)
        console.log("target: ", target);
        console.log("p: ", p);
        return Reflect.get(target,p)
    },
    set(target, p, value, receiver) {
        console.log("设置操作",target,p,value)
        Reflect.set(target, p, value);
    }
});


/*yuan.username
yuan.age
alex.age*/

alex.age = 10000

```



## Proxy代理监控器
```javascript
function setProxyArr(proxyObjArr) {
    for (let i = 0; i < proxyObjArr.length; i++) {
        const handler = `{
      get: function(target, property, receiver) {
        console.log("方法:", "get  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", target[property], ", 属性值类型：", typeof target[property]);
        return target[property];
      },
      set: function(target, property, value, receiver) {
        console.log("方法:", "set  ", "对象:", "${proxyObjArr[i]}", "  属性:", property, "  属性类型：", typeof property, ", 属性值：", value, ", 属性值类型：", typeof target[property]);
        return Reflect.set(...arguments);
      }
    }`;
        eval(`try {
            ${proxyObjArr[i]};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        } catch (e) {
            ${proxyObjArr[i]} = {};
            ${proxyObjArr[i]} = new Proxy(${proxyObjArr[i]}, ${handler});
        }`);
    }
}

//修改如下数组对象即可
setProxyArr(["window", "location","obj"])

```

当代理的对象，使用set或者get方法时，可以直接打印出详细的执行操作，发生异常时，可以方便我们进行跟踪补环境。

