import random
number = random.randint(1,100)
#number = 0
guess = 0
print("数字猜谜游戏！")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜你猜对了！")
    elif guess < number:
        print("数字猜小了...")
    elif guess > number:
        print("数字猜大了...")
