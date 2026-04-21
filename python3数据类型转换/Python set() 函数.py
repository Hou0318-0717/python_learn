
"""
#示例 1：创建集合
# 从列表创建（自动去重）
lst = [1,2,2,3,3,3,4]
s = set(lst)
print(s)

s = set("hello")
print(s)

t = (1,2,3,2,1)
s = set(t)
print(s)

d = {"a":1,"b":2,"c":3}
s = set(d)
print(s)

s = set()
print(s)
print(type(s))
"""

A = {1,2,3,4}
B = {3,4,5,6}
#并集
print(A|B)
print(A.union(B))
#交集
print(A&B)
print(A.intersection(B))
#差集
print(A - B)
print(A.difference(B))
#对称差集
print(A^B)
print(A.symmetric_difference(B))