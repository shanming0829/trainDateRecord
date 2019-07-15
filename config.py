#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-12 10:10:01
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import pathlib

BASEDIR = pathlib.Path(__file__).parent
DB_FILE = BASEDIR / 'train.db'

# Create dummy secrey key so we can use sessions
SECRET_KEY = '123456790'

# database connection
SQLALCHEMY_DATABASE_URI = 'sqlite:///train.db'.format(DB_FILE)
SQLALCHEMY_ECHO = True
