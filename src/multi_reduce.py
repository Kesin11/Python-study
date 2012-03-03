#coding: utf-8
import multiprocessing as mp
from time import time, sleep
import os
'''
マルチプロセスでReduceを実装
'''
def add(x, y):
    sleep(0.1)
    print 'pid: %s, add:%d, %d' % (os.getpid(), x, y)
    return x+y
             
def in_reduce(func, li):
    return reduce(func, li)
def multi_reduce(func, arg_list, core=mp.cpu_count()):
    '''arg_listを分割して並列にfuncでまとめる
       map()だとfuncが渡せないのでapply_async()を使用
    '''
    pool = mp.Pool()
    #listがコア数以上なら等分割、以下ならlen=1のlistにする
    if len(arg_list) > core:
        split_arg_list = equal_division(arg_list, core)
    else:
        split_arg_list = equal_division(arg_list, len(arg_list))
    result_list=[]
    reduced_list=[]
    for li in split_arg_list:
        result_list.append(pool.apply_async(in_reduce, (func, li)))
    for result in result_list:
        reduced_list.append(result.get())
    #全て集約するまで再帰
    if len(reduced_list) == 1:
        return reduced_list.pop(0)
    else:
        return multi_reduce(func, reduced_list, core/2)
    
def equal_division(li, num):
    '''listを等分割。奇数でも問題なし'''
    split_li=[]
    for i in xrange(0, num):
        split_li.append(li[i*len(li)/num : (i+1)*len(li)/num])
    return split_li
        
if __name__ == '__main__':
    '''reduceで使用する関数はおそらくローカルだろうが関係なし'''
    def mul(x, y):
        sleep(0.1)
        print 'pid: %s, add:%d, %d' % (os.getpid(), x, y)
        return x*y
    list = range(1, 100)
    singe_start = time()
    single_sum = reduce(add, list)
    single_end = time() - singe_start
    
    multi_start = time()
    multi_sum = multi_reduce(add, list, 4)
    multi_end = time() - multi_start
    
    print "single reduce: %d, %fs" % (single_sum, single_end)
    print "multi reduce: %d, %fs" % (multi_sum, multi_end)
    
    list = range(1, 100)
    singe_start = time()
    single_mul = reduce(mul, list)
    single_end = time() - singe_start
    
    multi_start = time()
    multi_mul = multi_reduce(mul, list, 4)
    multi_end = time() - multi_start
    
    print "single reduce: %d, %fs" % (single_mul, single_end)
    print "multi reduce: %d, %fs" % (multi_mul, multi_end)
    