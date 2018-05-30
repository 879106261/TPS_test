# -*- coding: utf-8 -*-
import os
import time
 
def write_log(log):
    filePath = os.path.abspath(os.path.dirname(__file__))
    logFilePath = os.path.join(os.path.dirname(filePath),'log','log.txt')
    #print(logFilePath)
    execTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    f = open(logFilePath,'a',encoding='UTF-8')
    f.write(execTime+':'+log+'\n')
    f.close()

if __name__ =='__main__':
    write_log('我的爱德华')