# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 10:04 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : __init__.py.py
import os, yaml, logging
import logging.config
import tornado
from tornado.options import define, options
from settings import dev, prod, common

config_path = os.path.join(common.BASE_DIR, 'settings/dev.py')
log_config_path = os.path.join(common.BASE_DIR, 'settings/logconfig.yaml')
log_config = yaml.load(open(log_config_path, 'r'), Loader=yaml.FullLoader)
logging.config.dictConfig(log_config)

logging.basicConfig()

define("port", type=int, default=8888)
define("db", type=dict, default={})
define("env", type=str, default='prod', help='env')
tornado.options.parse_command_line()
if options.env == "test":
    options.parse_config_file(config_path)

options = options

# if options.env == "test":
# https://www.cnblogs.com/1204guo/p/8472051.html
