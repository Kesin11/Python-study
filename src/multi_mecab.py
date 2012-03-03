#coding: utf-8
from multiprocessing import Pool
import MeCab, os
from time import time

def count_word(file_name):
    dict={}
    list=[]
    file = open(file_name)
    string = file.read()
    t = MeCab.Tagger()
    node = t.parseToNode(string)
    while node:
        if node.surface in dict:
            dict[node.surface] += 1
        else:
            dict[node.surface] = 1
        node = node.next
    #list.append("pid: " + os.getpid() + " file: " + file_name)
    print "pid: %d, file: %s" % (os.getpid(), file_name)
    #登場回数が多い単語順にソート
    for word, count in sorted(dict.items(), key=lambda x:x[1], reverse=True):
        list.append(str(count)+"\t"+word)
    return list
    
if __name__ == '__main__':
    FILE = "gingatetsudono_yoru.txt"
    
    #1コアによる処理
    t = time()
    count_list=[]
    for i in xrange(0, 100):
        count_list.append(count_word(FILE))
    single_time = time()-t
    print "single: %f sec" % (single_time)
    
    #複数コアによる処理
    t = time()
    #Pool(None)は自動的にcpu_count()の値が入る
    p = Pool()
    count_list=[]
    file_list = []
    for i in xrange(0, 100):
        file_list.append(FILE)
    count_list = p.map(count_word, file_list)
    multi_time = time()-t
    print "multi: %f sec" % (multi_time)
    
    print "single: %f sec" % (single_time)
        
