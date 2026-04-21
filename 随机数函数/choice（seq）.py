import random
print("从range(100)返回一个随机数：",random.choice(range(100)))
print("从列表[1,2,3,5,9]随即返回一个元素：",random.choice([1,2,3,5,9]))
print("从字符串'Runoob'返回一个随机字符：",random.choice('Runoob'))

#以下是一个随机密码生成器的简单实现：
import string
def generate_password(length):
    # 定义密码可用字符集合
    chars = string.ascii_letters + string.digits + string.punctuation

    # 随机选择字符生成密码
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
random_pwd = generate_password(6)
print(random_pwd)