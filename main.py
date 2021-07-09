# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 10:10 下午
# @Author  : lipanpan03
# @Email  : lipanpan03@58.com
# @File  : main.py

from tornado.web import RequestHandler
import tornado.ioloop
import tornado.options
import tornado.httpserver
from settings import options
from route import urls



# class Application(RequestHandler):
#
#     def __init__(self, *args, **kwargs):
#         super(Application, self).__init__(*args, **kwargs)
#         # self.db =
#
#         # self.redis =

print(options.port)


def main():
    # 设置日志等级
    options.logging = 'INFO'
    # 配置日志路径
    # options.log_file_prefix = log_file
    # 配置日志切割
    tornado.options.options.log_to_stderr = True
    # print(options.port)
    app = tornado.web.Application(
        urls,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
