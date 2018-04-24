'''kidNmae1="Jone"
kidNmae2="Jone2"
kidNmae3="Jone3"
kidNmae4="Jone4"
kidNmae5="Jone5"
kidNmae6="Jone6"
print(kidNmae1+kidNmae2+kidNmae3+kidNmae4+kidNmae5+kidNmae6)'''

kidsNames=[]
while True:
    print('输入名字：'
          +str(len(kidsNames))+'什么也不输入结束！')
    name=input()
    if name=='':
        break
    kidsNames+=[name]

for name in kidsNames:
    print(' '+name)

