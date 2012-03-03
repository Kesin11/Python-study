#coding: utf-8
import numpy as np

if __name__ == '__main__':
    print "int basic:"
    a = np.array([1,3,5,7,9])
    print "a=", a
    b = np.array([[0,0,0,1,2],
                 [1,2,3,4,5]])
    print "b=", b
    print "vstack a,b"
    print np.vstack((a,b))
    print "vstack b,a"
    print np.vstack((b,a))
    print "hstack a,b[0]"
    print np.hstack((a,b[0]))
    print "column_stack a,b[0]"
    print np.column_stack((a,b[0]))
    
    print "\nint and unicode:"
    #or can use "str b.astype(str)
    b_uni = b.astype(unicode)
    print b_uni
    col_label = np.array([u'赤い', u'黄色', u'あか', u'アカ', u'キイロ'])
    print col_label
    print "vstack col_label, b_str"
    mix = np.vstack((col_label, b_uni))
    print np.vstack((col_label, b_uni))
    row_label = np.array(['color', 'd1', 'd2'])
    print "column_stack row_label, mix"
    print np.column_stack((row_label, mix))
    mix = np.column_stack((row_label, mix))
    print "slice number:"
    print mix[1:, 1:].astype(int)
    
    print "\nset([]) of numpy:"
    st_array = col_label
    st_array = np.append(st_array, [u'赤い', u'黄色'])
    st_array.sort()
    for st in st_array:
        print st,
    print "\n"
    "return set, index number of original"
    unique, indices = np.unique(st_array, return_index=True)
    for st in unique:
        print st,
    print "\n"
    print indices
    for i, value in enumerate(unique):
        print value, i
