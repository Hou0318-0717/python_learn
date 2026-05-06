def findMinAndMax(L):
    if L==[]:
        return (None,None)
    min=L[0]
    max=L[0]
    for i in L:
        if not isinstance(i,(int,float)):
            raise ValueError("列表非数字")
        if i<min:
            min=i
        if i>max:
            max=i
    return(min,max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')