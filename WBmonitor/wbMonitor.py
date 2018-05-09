#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,json,sys
from lxml import etree

class weiboMonitor():

    def __init__(self, ):
        self.session = requests.session()
        self.reqHeaders = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:54.0) Gecko/20100101 Firefox/54.0'
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://passport.weibo.cn/signin/login',
            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        }

    def login(self, userName, passWord):
        loginApi = 'https://passport.weibo.cn/sso/login'
        loginPostData = {
            'username':userName,
            'password':passWord,
            'savestate':1,
            'r':'',
            'ec':'0',
            'pagerefer':'',
            'entry':'mweibo',
            'wentry':'',
            'loginfrom':'',
            'client_id':'',
            'code':'',
            'qq':'',
            'mainpageflag':1,
            'hff':'',
            'hfp':''
        }
