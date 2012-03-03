#coding: utf-8
from multiprocessing import Pool
import multiprocessing
import os

class Bar(object):
    #クラスメソッドも実行できない
    @classmethod
    def class_sum(cls, num):
        num = num + 1
        print "pid:", os.getpid()
        return num 
def list_sum(list):
    for i in range(len(list)):
        list[i] = list[i] + 1
    print "pid:", os.getpid()
    return list
def sum(num):
    num = num+1
    print "pid", os.getpid()
    return num

class Foo(object):
    #メンバ関数は実行できない
    def member_sum(self, list):
        for i in range(len(list)):
            list[i] = list[i] + 1
        print "pid:", os.getpid()
        return list
    def worker(self):
        self.num_list=[]
        self.core=multiprocessing.cpu_count()
        self.dammy_list=range(0,100)
        #0-100をコア数で分割して+1して返す
        for i in range(0, self.core):
            self.num_list.append(self.dammy_list[i*len(self.dammy_list)/self.core:(i+1)*len(self.dammy_list)/self.core])
        self.p = Pool()
        '''
        メンバ関数はpoolで使えないのでエラーになる
        self.map_list = self.p.map(self.member_sum, self.num_list)
        クラスメソッドもダメ
        self.map_list = self.p.map(Bar.class_sum, self.num_list)
        '''
        print "コア数分に分割したリスト"
        self.map_list = self.p.map(list_sum, self.num_list)
        print self.map_list
        print "分割していないリスト"
        self.map_list = self.p.map(sum, self.dammy_list)
        #プロセスを立ち上げるのにオーバーヘッドが大きいので、無理に分割する必要もない？
        print self.map_list
        
if __name__ == '__main__':
    foo = Foo()
    foo.worker()
    
    '''
    メインからでもクラスメソッド、インスタンスメソッドは呼び出せない
    dummy_list = range(0, 1000, 10)
    p = Pool()
    map_list = p.map(Bar.class_sum, dummy_list)
    print map_list
    '''
    
    