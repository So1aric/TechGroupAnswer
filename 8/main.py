from hashlib import md5
from base64 import b64decode

h = lambda x: md5(x.encode()).hexdigest()

code = b64decode("RVZBe1czMWMwbUVfVG9fekp1RVY0X1QzY2hAPz8/Pz99Ck1ENTo5NDY4NkM1N0U1MTIzNDkyOEIzNDQ5MjRGOTkyRDlDOQ==").decode()

code, goal = code.split('\n')
code = 'ZJU' + code

key = '0123456789abcdefghijklmnopqrstuvwxyz'
def make(n):
    if n == 1: return key
    return [j + i for j in key for i in make(n-1)]

cand = make(5)

print(len(cand))

result = None
for i, x in enumerate(cand):
    x = code.replace('?????', x)

    if i % 200 == 0:
        print(i, x)

    if h(x) == '94686C57E51234928B344924F992D9C9':
        result = x

print(result)
