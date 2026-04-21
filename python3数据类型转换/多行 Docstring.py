#对于复杂的函数，可以使用多行 Docstring：
def calculate(a,b,operation="add"):
    """
    执行数学运算

    参数：
        a：第一个数字
        b：第二个数字
        operation：操作类型，可选"add","subtract","multiply"
    返回：
        计算结果
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        raise ValueError("不支持的操作")

help(calculate)

#也可以用于类
class Person:
    """人物类，用于表示一个人的基本信息"""
    def __init__(self,name,age):
        """
        初始化人物对象

        参数：
            name：姓名
            age：年龄
        """
        self.name = name
        self.age = age
    def introduce(self):
        """介绍这个人"""
        return f"我叫{self.name}, 今年{self.age}岁"

print(Person.__doc__)

print(Person.introduce.__doc__)
a = ([1, 2, 3, 4, 5]*3)
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")