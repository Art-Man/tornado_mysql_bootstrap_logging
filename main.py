# -.- coding:utf-8 -.-
# __author__ = 'LDS'
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.concurrent
import tornado.log
import logging
import os

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/', DemoHandler),
        ]
        self.settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret='MEZzzzzzl4NkRWFtb3zzzzg3Y1JMZm5IMnBDcZEXOVhCNXNzzzzRWXJ6ax2d0pzzzz=',
            xsrf_cookies=True,
            compress_response=True,
            login_url='/',
        )
        super(Application, self).__init__(handlers, **self.settings)


class DemoHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('hello world!')
        self.render("index.html")

class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            fmt='%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )


def main():
    tornado.options.define("port", default=8889, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    tornado.options.define("log_file_prefix", default="logs/tornado_main.log")
    tornado.options.define("log_rotate_mode", default='time')   # 轮询模式: time or size
    tornado.options.define("log_rotate_when", default='D')      # 单位: S / M / H / D / W0 - W6
    tornado.options.define("log_rotate_interval", default=1)    # 间隔: 1天
    tornado.options.parse_command_line()
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()



# referer:
# https://my.oschina.net/zhengtong0898/blog/729067          tornado 日志管理
# http://www.cnblogs.com/sunshine-anycall/p/4293977.html    tornado+bootstrap急速搭建你自己的网站