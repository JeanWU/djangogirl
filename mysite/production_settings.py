# -*- coding: utf-8 -*-
#"""
#Created on Wed Jan 20 15:24:58 2016

#@author: jean
#""" 

from .settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT='staticfiles'
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https')
ALLOWED_HOSTS=['*']
DEBUG = False