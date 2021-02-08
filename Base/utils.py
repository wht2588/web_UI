import logging.handlers
import os


def log_conf():
    """日志初始化"""

    # 日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)

    # 处理器 -控制台
    sh = logging.StreamHandler()
    # 处理器 -文件
    trfh = logging.handlers.TimedRotatingFileHandler("./Log" + os.sep + "hm.log",
                                                     when="midnight", interval=1,
                                                     backupCount=7, encoding="utf-8")

    # 格式化字符串
    fmt = "%(asctime)s %(levelname)s [%(filename)s-%(funcName)s:%(lineno)d] -%(message)s"
    # 格式化器
    formatter = logging.Formatter(fmt)

    # 处理器添加日志器
    logger.addHandler(sh)
    logger.addHandler(trfh)

    # 格式化器 添加 处理器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)
