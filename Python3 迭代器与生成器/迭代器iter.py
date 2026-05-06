list = [1,2,3,4]
it = iter(list)  #创建迭代器
for x in it:
    print(x,end=" ")

list2 = [1, 2, 3, 4]
it2 = iter(list2)  # 创建迭代器
print("\n",next(it2))
print(next(it2))