'''message='好好学习，天禧向上！好事成双。字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。两个重要的点需要记住：1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：'

count={}

for character in message:
    count.setdefault(character,0)
    count[character]+=1
print(count)'''
'''
password={'email':'F7min1BDDDumnyueeeee',
         'blog':'VmbuidopAfdsksfsa486',
         'language':123456}
import sys,pyperclip

if len(sys.argv)<2:
    print('Usage:python password [account]-copy account password')
    sys.exit()
account=sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('Password for '+account+' copied to clipboard!密码：'+str(pyperclip.))
else:
    print('没有：'+account)'''
'''def bubbleSort(lists):
    count=len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i]>lists[j]:
                a1=(id(lists[i]))
                a2=(id(lists[j]))
                lists[i],lists[j]=lists[j],lists[i]
                newA1=(id(lists[i]))
                newA2=(id(lists[j]))
    return lists

data=[1,46,55,33,88,22,66]
bubbleSort(data)
print(data)

a=2
b=3
x1=id(a)
x2=id(b)
a,b=b,a
x1=id(a)
x2=id(b)
'''

'''
class Car(object):
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def show(self):
        print('Car name:' + self.__name + 'Car color:' + self.__color)

    @property
    def xx(self):
        return self.__name

    @xx.setter
    def xx(self, value):
        self.__name = value

    def __show(self):
        print('Car name:' + self.__name + self.__color)

    def newShow(self):
        self.__show()

    def __del__(self):
        print('f22222222222222222')

    def __call__(self, *args, **kwargs):
        print('call')
        pass


c1 = Car('Lamborghini', 'Blue')
c1()
c1.show()
print(c1.xx)
c1.xx = 'fasfas'
print(c1.xx)
c1.newShow()
'''
# Main_Getopt.py
import sys
import getopt

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'h:n:w:'
                        , ['name=', 'word=', 'help'])
    name = 'No Name'
    word = 'Hello'
    for key, value in opts:
        if key in ['-h', '--help']:
            print('一个向人打招呼的程序')
            print('参数：')
            print('-h\t显示帮助')
            print('-n\t显示帮助')
            print('-w\t显n示帮助')
            sys.exit(0)
    if key in ['-n', '--name']:
        name = value
    if key in ['-w', '--word']:
        word = value
    print('你好，我叫', name, ',', word)
