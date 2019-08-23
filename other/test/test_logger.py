# -*- coding: utf-8 -*-
import logging
from logging import FileHandler, StreamHandler
from logging.handlers import HTTPHandler, SMTPHandler

log = logging.Logger('Tornado', logging.DEBUG)

fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

fileHandler = FileHandler('test.log')
fileHandler.setLevel(logging.WARNING)
fileHandler.setFormatter(fmt=fmt)

streamHandler = StreamHandler()
streamHandler.setLevel(logging.INFO)
streamHandler.setFormatter(fmt=fmt)

httpHandler = HTTPHandler(host='127.0.0.1:8000', url='/', method='POST')
httpHandler.setLevel(logging.ERROR)


if __name__ == '__main__':
    log.addHandler(streamHandler)
    log.addHandler(fileHandler)
    log.addHandler(httpHandler)
    log.info('hello info')
    log.debug('hello debug')
    log.warning('hello warning')
    log.error('hello error')
    log.critical('hello critical')


