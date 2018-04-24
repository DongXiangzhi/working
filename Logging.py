
import logging

logging.basicConfig(filename='My_Program_Log.txt',
                    level=logging.DEBUG,
                    format=' %(asctime)s'
                           ' -%(levelname)s'
                           ' -%(message)s')

logging.debug('Start my Program')

def factorial(n):
    logging.info('Start of factorial' + str(n))
    total=1
    for i in range(1,n+1):
        total *=i
        logging.debug('i is ' + str(i) + ',total is ' + str(total))
    logging.debug('End of factorial' + str(n))
    return total

# logging.disable(logging.DEBUG)
print(factorial(5))
logging.debug('程序结束')
