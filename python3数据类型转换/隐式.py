num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int数据类型为：",type(num_int))
print("num_flo数据类型为：",type(num_flo))

print("num_new的值为：",num_new)
print("num_new数据类型为：",type(num_new))

num_str = "456"

print("num_str的数据类型为：",type(num_str))
print(num_str+num_int)#会报错，无法隐式转换

