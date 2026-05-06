names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)

#计算30以内能被3整除的整数
multiples = [i for i in range(30) if i % 3 ==0]
print(multiples)

#使用字符串及其长度创建字典
listdemo = ['Google','Baidu','Taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict)

#集合推导式
dic = {x:x**2 for x in(2,4,6)}
print(dic,type(dic))

setnew = {i**2 for i in (1,2,3)}
print(setnew)

a = {x for x in 'abcacadabra' if x not in'abc'}
print(a)

#元组推导式（生成器表达式）
a = (x for x in range(1,10))
print(a)
print(tuple(a))