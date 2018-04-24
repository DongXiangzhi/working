birthday={'Jeremiah':'Apr 1'
          ,'Salome':'Dec 12'
          ,'Nehemiah':'Mar 4'}

while True:
    print('Enter a name:(空退出）')
    name=input()
    if name=='':
        break
    if name in  birthday:
        print(birthday[name] + ' is the birthday of ' + name)

    else:
        print("没有生日："+name)
        print('What is their birthday?')
