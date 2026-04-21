"""
#示例 1：创建字典
d = dict()
print(d)

d = dict(name="Tom",age=20)
print(d)

d1 = {"name":"Tom"}
d2 = dict(d1)
print(d2)

pairs = [("name","Tom"),("age",20)]
d = dict(pairs)
print(d)

keys = ["name","age","size"]
values = ["Tom",20,"Beijing"]
d = dict(zip(keys,values))
print(d)
"""

#示例 2：字典操作
#访问值
d = {"name":"Tom","age":20}
print(d["name"])
print(d.get("age"))
print(d.get("size"))
#添加/修改
d["city"] = "Beijing"
d["age"] = 21
print(d)
#删除
del d["age"]
print(d)
#遍历
for key,value in d.items():
    print(f"{key}:{value}")
