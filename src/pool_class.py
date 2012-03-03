from multiprocessing import Pool
import os
'''
外部からクラスを呼び出せば、モジュール内に記述してある関数は使用可能
'''
def add(num):
    print "pid: %d" % os.getpid(), 
    print "add: %d" % (num+num)
def mul(num):
    print "pid: %d" % os.getpid(), 
    print "mul: %d" % (num*num)
class PoolTest(object):
    def pool_calc(self, list):
        pool = Pool()
        pool.map(add, list)
        pool.map(mul, list)
        
if __name__ == '__main__':
    list = range(1, 10)
    pool_test = PoolTest()
    pool_test.pool_calc(list)