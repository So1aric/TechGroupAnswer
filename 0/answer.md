Answer: TECH

```python
decrypt = lambda code, key: ''.join([chr(int(s, 16) // ord(key[i])) for i, s in enumerate(code.split('/'))])
```

简化：可以直接join
```python
encrypt = lambda clear, key: "/".join([hex(ord(clear[i]) * ord(key[i]))[2:] for i in range(4)])
```

