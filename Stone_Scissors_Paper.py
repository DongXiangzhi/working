# 石头剪刀布
import random

def rock_paper_scissor(decision):
    computer = int(random.randint(1, 3))
    if computer == 1:
        ind = 'Rock'
    elif computer == 2:
        ind = 'Scissors'
    elif computer == 3:
        ind = 'Paper'
    if decision == computer:
        print('电脑出了：' + ind + ',平局')
    elif decision == 'Rock' and ind == 'Scissors' or \
            decision == 'Scissors' and ind == 'Paper' or \
            decision == 'Paper' and ind == 'Rock':
        print('电脑出了：' + ind + ',你赢了！')
    elif decision == 'Rock' and ind == 'Paper' or \
            decision == 'Scissors' and ind == 'Rock' or \
            decision == 'Paper' and ind == 'Scissors':
        print('电脑出了：' + ind + ',你输了！')


blist= ['Rock', 'Scissors', 'Paper']
while 1:
    decision = input('输入：Rock、Scissors、Paper，输入exit结束！')
    if (decision not in blist) and (decision != 'exit'):
        print('输入错误，请重新输入！')
    elif (decision not in blist) and (decision == 'exit'):
        print('游戏结束！')
        break
    else:
        rock_paper_scissor(decision)
