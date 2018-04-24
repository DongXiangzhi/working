import random
secret_number = random.randint(1, 20)
print('我想到了一个1-20之间的数')
for times in range(1, 7):
    print('猜一下吧，老铁！')
    guess = int(input())
    if guess < secret_number:
        print('你才小了！')
    elif guess > secret_number:
        print('你猜大了！')
    else:
        print('你猜对了')
        print('真棒！你猜了'+str(times))
        break

