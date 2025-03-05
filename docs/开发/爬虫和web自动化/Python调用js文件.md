```python
pip install pyexecjs
```

```python
js_code = open("03 fjzy.js").read()
js_compile = execjs.compile(js_code)
data = js_compile.call("b",base64_encrypt_data)
```

