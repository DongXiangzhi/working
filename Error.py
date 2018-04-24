def temp():
    try:
        hello()
    except Exception as err:
        print('异常：'+str(err))

def hello():
    raise Exception('This is the error message')

temp()

import traceback
try:
    raise Exception("This is a error")
except:
    errorFile=open('e:\Error4_Info.txt','w')

    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('写完了！')