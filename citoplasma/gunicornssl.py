#!/usr/bin/python3

from bottle import ServerAdapter
import ssl

class GunicornServerSSL(ServerAdapter):
    """ Untested. See http://gunicorn.org/configure.html for options. """

    cert_pem=''
    privkey_pem=''
    workers=2

    def run(self, handler):
        from gunicorn.app.base import Application

        #'ciphers': 'TLSv1'
        #, 'ssl_version': ssl.PROTOCOL_TLSv1

        config = {'bind': "%s:%d" % (self.host, int(self.port)), 'workers': self.workers, 'keyfile': self.privkey_pem, 'certfile': self.cert_pem, 'ssl_version': ssl.PROTOCOL_TLSv1}
        config.update(self.options)

        class GunicornApplication(Application):
            def init(self, parser, opts, args):
                return config

            def load(self):
                return handler

        GunicornApplication().run()