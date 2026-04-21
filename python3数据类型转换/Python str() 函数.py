"""
#示例 1：基础用法 - 转换各种类型
print(str(123))
print(type(str(123)))
print(str(3.14159))
print(str(True))
print(str(False))
print(str([1, 2, 3]))
print(str((1,2,3)))
print(str({"name":"Tom","age":20}))
print(str())
"""
"""
#示例 2：字符串拼接
name = "Tom"
age = 20
height = 1.75
info = name +" "+str(age) + "岁" +" " + str(height) + "米"
print(info)

info = f"{name} {age}岁 {height}米"
print(info)

print("姓名："+str(name))
"""

#示例 3：处理字节和编码
data = b"Hello"
s = str(data,encoding = 'utf-8')
print(s)

data = b"Hello\x80"
s = str(data,encoding='utf-8',errors='ignore')
print(s)