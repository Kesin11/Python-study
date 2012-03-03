#coding: utf-8
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    logging.debug('Debug log test')
    logging.error('error!')

