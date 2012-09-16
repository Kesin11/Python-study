#coding: utf-8
'''
multiprocessing.Poolの振る舞い
'''
from multiprocessing import Process, Pool
import multiprocessing
import time
import os

def print_time():
    tm = time.localtime(time.time())
    return time.strftime("%M:%S", tm)

def sum_print(a, b, c):
    time.sleep(1)
    print "pid: %d, sum: %d, time: %s " % (os.getpid(), a+b+c, print_time())
    #return "pid: %d, sum: %d, time: %s " % (os.getpid(), a+b+c, print_time())
    
def sum(a, b, c):
    time.sleep(1)
    return "pid: %d, sum: %d, time: %s " % (os.getpid(), a+b+c, print_time())

def print_square(x):
    time.sleep(1)
    print "pid: %d, square: %d, time: %s" % (os.getpid(), x*x, print_time())

def square(x):
    time.sleep(1)
    return "pid: %d, square: %d, time: %s" % (os.getpid(), x*x, print_time())

if __name__ == '__main__':
    print "CPU Core: " + str(multiprocessing.cpu_count())
    print "Process:"
    sum_p = Process(target=sum_print, args=(2, 3, 4))
    square_p = Process(target=print_square, args=(5,))
    sum_p.start()
    square_p.start()
    sum_p.join()
    square_p.join()
    
    pool = Pool()
    print "Pool: apply()"
    for i in xrange(3, 6):
        list = [i-1, i, i+1]
        #applyはAsyncResultを返すまでブロックする
        pool.apply(sum_print, list)
        
    print "Pool: apply_async()"
    result_list = []
    for i in xrange(3, 6):
        list = [i-1, i, i+1]
        #apply_asyncは非同期でAsyncResultを返す
        result_list.append(pool.apply_async(sum, list))
    for result in result_list:
        print result.get()
        
    print "Pool: map()"
    list = range(1, 5)
    pool.map(print_square, list)
    print "map()が終わるまでブロックされる"
    
    print "Pool: map_async()"
    result_list = pool.map_async(square, list)
    print "map_async()はブロックされない"
    print "result_list: Ready? " + str(result_list.ready())
    #get(None)は結果を受け取れるまでブロックする
    print result_list.get(None)
    
    print "Pool: imap()"
    #関数を呼び出すイテレーターを作成する
    it = pool.imap(print_square, list)
    #関数を呼び出す
    it.next()
    time.sleep(1)
    it.next()
    time.sleep(1)
    
    print "Pool: map() chunksize=3"
    #chunksizeを指定するとまとめて一つのプロセスに割り当てる
    list = range(1, 10)
    result_list = pool.map(square, list, 3)
    for result in result_list:
        print result
    