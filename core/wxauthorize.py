#!/usr/bin/env python
# coding: utf8

from log.logger_helper import logger
import hashlib
from tornado.web import  RequestHandler


class WxSignatureHandler(RequestHandler):

    def get(self):
        try:
            signature = self.get_argument('signature')
            timestamp = self.get_argument('timestamp')
            nonce = self.get_argument('nonce')
            echostr = self.get_argument('echostr')
            logger.debug('wx signature %s' % signature)
            res = self.check_signature(signature, timestamp, nonce)
            if res:
                logger.debug('check is success')
                self.write(echostr)
            else:
                logger.error('check is failure.')
        except Exception as e:
            print e


    def check_signature(self, sig, ts, nonce):
        token = 'chaos'
        l = [ts, nonce, token]
        l.sort()
        s = l[0] + l[1] + l[2]
        sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
        logger.debug('sha1=%s' % sha1)
        return sha1 == sig
