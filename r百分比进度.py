#1.使用 \r 实现百分比进度：
import time
for i in range(101):
    bar = '[' + '=' * (i // 2)+' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:5}%",end='',flush = True)
    time.sleep(0.5)
print()

import time

#定义的类
def progress_bar(total=100, length=50):
    for j in range(total + 1):
        filled = int(length * j / total)
        bar1 = '[' + '=' * filled + ' ' * (length - filled) + ']'
        print(f"\r{bar1} {j:5}%", end='', flush=True)
        time.sleep(0.5)
    print()

progress_bar()