#!/usr/bin/env python
# coding: utf8

import logging
from logging import Logger
from logging.handlers import TimedRotatingFileHandler as trf


def init_logger(logger_name):
    if logger_name not in Logger.manager.loggerDict:
        logger_init = logging.getLogger(logger_name)
        logger_init.setLevel(logging.INFO)

        df = '%Y-%m-%d %H:%M:%S'
        format_str = '[%(asctime)s]: %(name)s %(levelname)s %(lineno) %(message)s'
        formatter = logging.Formatter(format_str, df)

        handler_all_log = trf('/Users/lcf/wechat/log/all.log', when='D', interval=1, backupCount=7)
        handler_all_log.setFormatter(formatter)
        handler_all_log.setLevel(logging.DEBUG)

        logger_init.addHandler(handler_all_log)

        handler_error_log = trf('/Users/lcf/wechat/log/error.log', when='D', interval=1, backupCount=7)
        handler_error_log.setFormatter(formatter)
        handler_error_log.setLevel(logging.ERROR)

        logger_init.addHandler(handler_error_log)

    logger_init = logging.getLogger(logger_name)
    return logger_init

logger = init_logger('runtime_log')

if __name__=='__main__':
    logger.debug('test-debug')
    logger.info('test-info')
    logger.warn('test-warn')
    logger.error('test-error')

