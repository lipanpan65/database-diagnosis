# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 10:05 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : common.py

import os
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
STATIC = os.path.join(BASE_DIR, 'static')
TEMPLATE = os.path.join(BASE_DIR, 'templates')
LOG_PATH = os.path.join(BASE_DIR, 'logs/log')
