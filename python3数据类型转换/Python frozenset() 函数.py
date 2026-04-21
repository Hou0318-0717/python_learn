"""
#示例 1：创建 frozenset
lst = [1,2,3,2,1]
fs = frozenset(lst)
print(fs)               #frozenset 会自动去重。

s = "hello"
fs = frozenset(s)
print(fs)

d = {"a":1,"b":2,"c":3}
fs = frozenset(d)
print(fs)

fs = frozenset()
print(fs)
"""

#示例 2：frozenset 的用途
d = {frozenset([1,2]):"A",frozenset([3,4]):"B"}
print(d)

s = {frozenset([1,2]),frozenset([3,4])}
print(s)

fs1 = frozenset([1,2,3])
fs2 = frozenset([2,3,4])
print(fs1 & fs2)
print(fs1 | fs2)