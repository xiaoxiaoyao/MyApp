'''
log test
'''

import logging;
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

def TestLog():
    logging.debug('debug message')  
    logging.info('info message')  
    logging.warning('warning message')  
    logging.error('error message')  
    logging.critical('critical message')   
    return

if __name__ == '__main__':
    TestLog()