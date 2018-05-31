import logging
import os
import time

LOGGING_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s'
class Logger:
    def __init__(self,
                 level=logging.DEBUG,  # 日志级别
                 format=LOGGING_FORMAT,  # 日志格式
                 datefmt='%a, %d %b %Y %H:%M:%S',  # 日期格式
                 filename='',  # 日志文件名
                 filemode='a'  # 文件打开模式
                 ):
        filePath = os.path.abspath(os.path.dirname(__file__))
        log_execTime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        logfile_name = 'server.log.' + log_execTime
        logFilePath = os.path.join(os.path.dirname(filePath), 'log', logfile_name)

        self.level = level
        self.format = format
        self.datefmt = datefmt
        self.filename = logFilePath
        self.filemode = filemode

        # 初始化日志同时输出到console和日志文件
        logging.basicConfig(level=self.level,
                            format=self.format,
                            datefmt=self.datefmt,
                            filename=self.filename,
                            filemode=self.filemode)

        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，
        # 并将其添加到当前的日志处理对象
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s \
            %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('Logger').addHandler(console)
        self.log = logging.getLogger("Logger")

        # 日志输出
    def output(self, msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            # 调试信息
            self.log.debug(msg)
        elif level == logging.INFO:
            # 一般的信息
            self.log.info(msg)
        elif level == logging.WARNING:
            # 警告信息
            self.log.warning(msg)
        elif level == logging.ERROR:
            # 错误信息
            self.log.error(msg)
        else:
            # 尼玛
            self.log.critical(msg)

    def set_level(self, level=logging.DEBUG):
        self.log.set_level(level)

if __name__ == "__main__":
    print("python logging实例")
    log = Logger()
    log.output("it's debug msg", level=logging.DEBUG)
    log.output("it's info msg", level=logging.INFO)
    log.output("it's warning msg", level=logging.WARNING)
    log.output("it's error msg", level=logging.ERROR)
    log.output("it's fuck msg", level=logging.CRITICAL)