# 模拟火箭倒计时发射
import os
import time

count=10
while count>=0:
    os.system('cls')

    print(count)
    time.sleep(1)

    count-=1
else:
    print('计数结束！')