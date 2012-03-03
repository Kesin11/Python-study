from multiprocessing import Pool
import os
from pool_class import PoolTest

def sum(num):
    num += 1
    print num
def print_dict(dict):
    print "pid: %d" % os.getpid()
    print dict
    

if __name__ == '__main__':
    pool = Pool()
    list = range(0, 100)
    pool.map(sum, list)
    
    dictA = {'name':'abc', 'num': 1}
    dictB = {'name':'def', 'num': 2}
    dictC = {'name':'gef', 'num': 3}
    dict_list = [dictA, dictB, dictC]
    pool.map(print_dict, dict_list)
    
    '''
    クラスを呼び出せば、そのモジュール内の関数は使用可能
    '''
    pool_test = PoolTest()
    pool_test.pool_calc(list)