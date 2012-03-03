
'''
Created on 2011/10/04

@author: kase
'''
import argparse, sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test')
    
    parser.add_argument('-m', action="store_true", default=False, dest='multi_option', help='enable multi process')
    parser.add_argument('-f', action="store", dest='filename')
    option = parser.parse_args()
    
    print 'multicore option is ', option.multi_option
    print 'file name is ', option .filename
    print option