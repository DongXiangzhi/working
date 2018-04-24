import random


def get_answer(answer):
    if answer==1:
        return '恭喜你中了五百万！'
    elif answer==2:
        return 'fsdafa'
    elif answer==3:
        return 'fasfasfasd111'


r=random.randint(1,3)
for i in range(100):
    print(r)
# print(get_answer(r))
