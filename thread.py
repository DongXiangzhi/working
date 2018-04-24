'''
import os
import time
import random
from multiprocessing import Pool


def long_time_task(args):
    print('Run task')
    start = time.time()
    time.sleep(1)
    end = time.time()
    print('Task秒')


if __name__ == '__main__':
    print('Parent process')
    i=5
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有线程结束....')
    p.close()  # close后不能加入process
'''
'''
import os, random, time
from multiprocessing import Process, Queue


def write(q):
    for value in ['a', 'b', 'c']:
        print('Put' + str(value) + ' to queue...')
        q.put(value)
        time.sleep(3)


def read(q):
    while True:
        value = q.get(True)
        print('Get ' + value + ' from queue...')


if __name__ == '__main__':
    # 父进程创建Queue，并传给子进程
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q, ))
    # 启动写进程
    pw.start()
    # 启动读进程
    pr.start()

    # 等待写完
    pw.join()
    # 如果
    pr.terminate()'''
import threading
import time


def loop():
    print('Thread is running..' + str(threading.current_thread().name))
    n = 0
    while n < 5:
        n += 1
        print('thread' + threading.current_thread().name
              + '>>>' + str(n))
        time.sleep(1)
    print('结束' + threading.current_thread().name)


if __name__ == '__main__':
    print('thread is:'+threading.current_thread().name)
    t=threading.Thread(target=loop,name='Loopthread')
    t.start()
    t.join()
    print('dddd')
