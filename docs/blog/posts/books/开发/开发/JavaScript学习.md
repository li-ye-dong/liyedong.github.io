# 异步Promise
先后发出名为a的请求和b的请求，一秒后回调成功使用resolve返回成功数据，对应then的res，reject返回的是catch里的err对象。简单来说就是resolve这个函数的回调是成功的时候调用，reject函数是失败调用

```python
function test(name) {
    return new Promise((resolve, reject) => {
        console.log('start:', name)
        let data = {}
        try {
            setTimeout(() => {
                data = {'code': 200}
                resolve(data)
                console.log('success')
            }, 1000)
        } catch (e) {
            console.log('error')
            reject(data)
        }
    })
}

test('a').then((res) => {
    console.log(res);
}).catch((err) => {
    console.log(err);
}).finally(() => {
    console.log('finally');
})
test('b').then((res) => {
    console.log(res);
}).catch((err) => {
    console.log(err);
}).finally(() => {
    console.log('finally');
})

```

