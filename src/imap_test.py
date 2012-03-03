#coding: utf-8
import time, os, itertools, multiprocessing

def print_time():
    tm = time.localtime(time.time())
    return time.strftime("%M:%S", tm)
def print_add(x):
    time.sleep(1)
    print "pid: %d, add: %d, time: %s" % (os.getpid(), x+x, print_time())
    return x+x
def print_square(x):
    time.sleep(1)
    print "pid: %d, square: %d, time: %s" % (os.getpid(), x*x, print_time())
    return x*x
def print_argument(arg):
    time.sleep(1)
    print "pid: %d, argument: %d, time: %s" % (os.getpid(), arg, print_time())
    return arg
    
if __name__ == '__main__':
    """
    list = [3,4,5]
    print "map: 引数リスト"
    print map(print_square, list)
    print "map: 引数イテレータ"
    print map(print_square, iter(list))
    "iterrools.imap"
    results = itertools.imap(print_square, iter(list))
    print "next: %s" % results.next()
    print "next: %s" % results.next()
    print "next: %s" % results.next()
    print "mapはリストを返してからループ"
    for i in map(print_square, list):
        print i
    print "imapはループするときにnext()が呼ばれる"
    for i in itertools.imap(print_square, list):
        print i
    """
    list = [2,3,4,5,6]
    pool = multiprocessing.Pool(4)
    print "Pool.map"
    for i in pool.map(print_argument, iter(list)):
        print i
        time.sleep(2)
    print "Pool.imap: イテレータ"
    for i in pool.imap(print_argument, iter(list)):
        print i
        time.sleep(2)
    print "Pool.imap: リスト"
    for i in pool.imap(print_argument, [2,3,4,5,6,7,8,9,10,11]):
        print i
        time.sleep(2)
    #print "for文の中でイテレータに追加したとき"
    #for i in pool.imap(print_square, iter(list)):
    #    for j in pool.imap(print_add, [i, i*10]):
    #        pass
    
    print "chunksizeの効果"
    pool = multiprocessing.Pool(2)
    for i in pool.imap(print_argument, xrange(2,11), chunksize=4):
        print i
        time.sleep(2)
        
        
    
    