# -*- coding: utf-8 -*-
import traceback
from .write_log import write_log
from .log_info import Logger
import logging

log = Logger()
#使用装饰器，func为传入的函数
def exe_deco(func):
    def _deco(*args, **kwargs):
        result = ()
        ret = None
        try:
            ret = func(*args, **kwargs)
        except Exception as e:
            log = 'Exception in '+func.__name__+' method: '+str(e)
            #将错误写入日志中
            #write_log(log)
            log.output(log, level=logging.ERROR)
            result = result + str(log)
        else:
            log = 'No exception in '+func.__name__+' method.'
            #write_log(log)
            log.output(log, level=logging.DEBUG)
            result = result+str(log)
        finally:
            return ret,result
    return _deco

