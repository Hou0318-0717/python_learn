""""
t = (5,4,3,2,1)
lst = list(t)
print(lst)

s = "hello"
lst = list(s)
print(lst)

d = {"a":1,"b":2,"c":3}
lst = list(d)
print(lst)

s = {3,1,2}
lst = list(s)
print(lst)   # 输出: [1, 2, 3]（自动排序）

lst = list()
print(lst)
"""

#示例 2：列表的常用操作
lst = list((1,2,3))
lst.append(4)
lst.insert(0,0)
print(lst)

lst = [x * 2 for x in range(5)]
print(lst)

original = [1,2,3]
copy = list(original)
print(copy)