# Loggger Singleton:
import datetime
import logging
import datetime as dt
import sys
from configparser import ConfigParser

class Logger(object):
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    config = ConfigParser()
    config.read("config.conf")
    LOG_LEVEL = config["logging"]["level"]
    LOG_FILE_NAME_PREFIX = config["logging"]["logfile_name_prefix"]
    LOG_FILE_NAME_EXT = config["logging"]["logfile_name_ext"]
    print(LOG_LEVEL)
    print(LOG_FILE_NAME_PREFIX)
    print(LOG_FILE_NAME_EXT)


    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.name = 'Matan' # maybe from config
        return cls._instance

    def print_hello(self):
        print('hello')

sing1 = Logger.get_instance()
sing2 = Logger.get_instance()
print(sing1 == sing2)
print(sing1)
print(sing2)
print(sing1.name)
sing1.print_hello()