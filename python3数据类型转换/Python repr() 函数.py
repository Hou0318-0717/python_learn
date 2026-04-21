"""
repr() 是 Python 中用于获取对象可打印表示的内置函数。
repr() 返回一个对象的官方字符串表示，通常可以用来重新创建该对象。它与 str() 的区别在于，repr() 更侧重于调试和开发，而 str() 侧重于用户友好。
单词释义： repr 是 representation（表示）的缩写。
"""
"""
#示例 1：repr() vs str()
s = "hello"            #字符串的区别
print(f"str:'{str(s)}'")
print(f"repr:'{repr(s)}'")

from datetime import datetime  #日期时间的区别
dt = datetime.now()
print(f"str:'{str(dt)}'")
print(f"repr:'{repr(dt)}'")

#自定义类的区别
class Person:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Person:{self.name}"
    def __repr__(self):
        return f"Person(name='{self.name}')"

p = Person("Tom")
print(f"str:'{str(p)}'")
print(f"repr:'{repr(p)}'")
"""

#示例 2：使用 repr() 调试
#显示隐藏符
s = "hello\nword"
print(f"str:{str(s)}")
print(f"repr:{repr(s)}")

#显示符号
text = "She said 'hello'"
print(f"str:{str(text)}")
print(f"repr:{repr(text)}")
