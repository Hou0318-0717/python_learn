#布尔类型的值和类型
a = True
b = False
print(type(a))
print(type(b))

#布尔类型的整数表现
print(int(True))
print(int(False))

#使用bool()函数进行转换
print(bool(0))
print(bool(42))
print(bool(''))
print(bool('python'))
print(bool([]))
print(bool([1,2,3]))

#布尔逻辑运算
print(True and False)
print(True or False)
print(not True)

#布尔比较运算
print(5 > 3)
print(2 == 2)
print(7 < 4)

#布尔值在控制流中的应用
if True:
    print("This will always print")

if not True:
    print("This will also always print")

x = 10
if x :
    print("x是非零值，在布尔上下文中为 True")