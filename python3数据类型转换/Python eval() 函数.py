"""
#示例 1：基础用法
result = eval("1 + 2 + 3")
print(result)
print("1+2+3")

x = 10
result = eval("x * 2")
print(result)

result = eval("2 ** 3 + 4 * 5")
print(result)

result = eval("len('hello')")
print(result)
"""

#示例 2：受限环境
x = 10
y = 20

safe_dict = {"x":x,"y":y,"abs":abs}
result = eval("x+y",safe_dict)
print(result)

try:
    eval("__import__('os').system('ls')",{})
except NameError as e:
    print(f"安全限制：{e}")