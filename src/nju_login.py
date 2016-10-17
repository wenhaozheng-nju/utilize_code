#!/usr/bin/env python
# coding=utf-8
import requests
url = 'http://p.nju.edu.cn/portal_io/login'

data = {
    'username':'hehe',
    'password':'xixi'
}

print requests.post(url,data=data).text
