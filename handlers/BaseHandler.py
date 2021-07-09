# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 10:34 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : BaseHandler.py
from typing import Optional, Awaitable, Any

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.redis

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def prepare(self) -> Optional[Awaitable[None]]:
        pass

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        pass

    def set_default_headers(self) -> None:
        pass

    def initialize(self) -> None:
        pass

    def on_finish(self) -> None:
        pass
