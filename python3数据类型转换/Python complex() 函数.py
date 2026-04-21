#示例1：基础用法 - 创建复数
# c1 = complex(3,4)
# print(c1)
#
# c2 = complex(5,0)
# print(c2)
#
# c3 = complex(0,2)
# print(c3)
#
# c4 = complex(1,-2)
# print(c4)

# #示例2：从字符串创建复
# c1 = complex("3+4j")
# print(c1)
#
# c2 = complex(" 1+2j ")
# print(c2)
# #注意：Python 复数只支持 j，不支持 i。
# c3 = complex("3+4j")
# print(c3)

#示例 3：复数的运算
a = complex(3,4)
b = complex(1,2)

print(f"a + b={a+b}")
print(f"a - b={a-b}")
print(f"a * b={a*b}")
print(f"a / b={a/b}")
print(f"共轭：{a.conjugate()}")
print(f"模：{abs(a)}")