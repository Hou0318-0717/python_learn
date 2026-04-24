n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print("1到%d之和为：%d"%(n,sum))
print("1到100之和为：",sum)
print("1到100之和为：%d"%sum)
print("1到%d之和为："%n,sum)
print(f"1到{n}之和为：{sum}")
print("1到{}之和为：{}".format(n,sum))

#无限循环
var = 1
while var == 1:
    num = int(input("输入一个数字："))
    print("你输入的数字是：",num)
print("Good bye!")