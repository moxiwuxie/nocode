#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import logging.handlers

# logger = logging.getLogger(__name__)
# handler1 = logging.StreamHandler()
# handler2 = logging.handlers.RotatingFileHandler('actual.txt', mode='w', maxBytes=500, backupCount=3)
# logger.setLevel(logging.DEBUG)
# handler1.setLevel(logging.DEBUG)
# handler2.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# handler1.setFormatter(formatter)
# handler2.setFormatter(formatter)
# logger.addHandler(handler1)
# logger.addHandler(handler2)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logging.basicConfig(filename='actual.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='a')

# test_handler = logging.StreamHandler()
test_handler = logging.handlers.RotatingFileHandler('actual.txt', mode='a', maxBytes=5000, backupCount=3)
test_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(test_handler)


