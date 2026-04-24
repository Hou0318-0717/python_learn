#while 中使用 break
n = 5
while n >0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束')

#while中使用continue
n =5
while n > 0:
    n -=1
    if n == 2:
        continue
    print(n)
print('循环结束')

#更多实例
for letter in "python":
    if letter == "o":
        break
    print('当前字母为：',letter)

var = 10
while var > 0:
    print("当前变量为：",var)
    var = var -1
    if var == 5:
        break
print("Good bye!")


for letter1 in "python":
    if letter1 == "o":
        continue
    print("当前字母:",letter1)

var1 = 10
while var1 > 0:
    var1 -= 1
    if var1 == 5:
        continue
    print("当前变量值：",var1)
print("Good bye!")