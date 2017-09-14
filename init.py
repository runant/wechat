#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import tornado.ioloop
from tornado import web
from tornado.httpserver import HTTPServer
from tornado.options import define, options

define('port', default=8000, help='run on this port', type=int)
define('debug', default=True, help='enable debug mode')
define('project_path', default=sys.path[0], help='deploy_path')

options.parse_command_line()

URLS = [
    #(r'/?', 'handler.web.IndexHandler'),
    (r'/wechat', 'core.wxauthorize.WxSignatureHandler'),
]
class Application(web.Application):
    def __init__(self):
        settings = {
                'debug': options.debug,
                'gzip': True,
                'autoescape': None,
                'xsrf_cookies': False,
                'template_path': os.path.join(options.project_path, 'template'),
                'static_path': os.path.join(options.project_path, 'static'),
                'cookie_secret': 'exoOr1WYSg6+W7lbDbmtNmt6U0ZmrkwbvnnqyWksvCY='
                }
        tornado.web.Application.__init__(self, URLS, **settings)

if __name__ == '__main__':
    http_server = HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
