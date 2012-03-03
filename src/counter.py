#coding: utf-8
from collections import Counter

if __name__ == '__main__':
    c = Counter({'word':10, 'he':20, 'she':30})
    d = Counter({'word':20, 'we':5, 'they':10})
    dic = {'word':10, 'we':50}
    
    print c
    print d
    #+は加算
    print c+d
    #-は要素での積集合
    print c-d
    
    c.update(d)
    print c
    c.update(dic)
    print c
    
    for name, i in c.items():
        print "name: %s, count: %d" % (name, i)
        