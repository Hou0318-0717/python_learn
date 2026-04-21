
"""
#示例 1：从列表转换
lst = [1,2,3,4,5]
t = tuple(lst)
print(t)
print(type(t))

s = "hello"
t = tuple(s)
print(t)

d = {"a":1,"b":2}
print(d.values())
print(d.keys())
print(d.items())
t = tuple(d)
print(t)


s = {1,2,3}
t = tuple(s)
print(t)

t = tuple()
print(t)
"""

#示例 2：元组的特点
t = (1,2,3)
d = {(1,2):"point",(3,4):"origin"}
print(d)

t = ((1,2),(3,4))
print(t)

a,b,c = (1,2,3)
print(f"a={a},b={b},c={c}")

