sites = {'Google' ,'Taobao','Runoob','Facebook','Zhihu','Baidu'}
print(sites)

if 'Runoob' in sites:
    print("Runoob在集合中")
else:
    print("Runoob不在集合中")

#set进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)          #a中的唯一字符
print(a - b)      #a和b的差集
print(a | b)      #a和b的并集
print(a & b)      #a和b的交集
print(a ^ b)      #a和b的对称差集