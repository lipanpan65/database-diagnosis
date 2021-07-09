# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 11:04 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : index.py

from tornado.web import RequestHandler
from handlers import BaseHandler

import logging
# logger = logging.getLogger("")


class IndexHandler(BaseHandler):

    def get(self):
        logging.info("test")
        self.write('Hello Tornado')
