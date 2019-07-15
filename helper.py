#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-12 15:07:22
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import logging
import sys


def getLogger(name, level=logging.INFO,
              stream=None, filePath=None,
              fmtStr=None, dateStr=None):
    if fmtStr is None:
        fmtStr = "<%(asctime)s> [%(name)s] [%(levelname)s] %(message)s"
    if dateStr is None:
        dateStr = '%Y-%m-%d %H:%M:%S'

    log = logging.getLogger(name)
    log.setLevel(level)

    logFmt = logging.Formatter(fmtStr,
                               datefmt=dateStr)

    if stream is None:
        stream = sys.__stdout__

    handler1 = logging.StreamHandler(stream)
    handler1.setFormatter(logFmt)
    log.addHandler(handler1)

    if filePath:
        handler2 = logging.FileHandler(filePath, 'wt')
        handler2.setFormatter(logFmt)
        log.addHandler(handler2)

    return log
