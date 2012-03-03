class foo_class(object):
    def foo(self):
        self.a = 1
        self.b = 2
        print self.a+self.b
    def bar(self):
        print self.a+self.b
        
if __name__ == '__main__':
    f = foo_class()
    f.foo()
    
    a = 2
    b = 3
    print a+b
    f.bar()
    
    list = range(0,100)
    slice = 2
    for i in range(0,slice):
        for part_list in list[(i*len(list)/slice):((i+1)*len(list)/slice)]:
            print part_list
        print "check"