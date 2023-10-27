#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2020 <> All Rights Reserved
#
#
# File: /Users/hain/chatopera/efaqa-corpus-zh/app/sample.py
# Author: Hai Liang Wang
# Date: 2020-04-22:09:40:24
#
#===============================================================================

"""
   
"""
__copyright__ = "Copyright (c) 2020 Chatopera Inc <https://chatopera.com>. All Rights Reserved"
__author__ = "Hai Liang Wang"
__date__ = "2020-04-22:09:40:24"

import os, sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, curdir)

if sys.version_info[0] < 3:
    raise RuntimeError("Must be using Python 3")
else:
    unicode = str

import json
import efaqa_corpus_zh

def pretty(j, indent=4, sort_keys=True):
    """
    get json as pretty string
    :param j:
    :return:
    """
    return json.dumps(j, indent=indent, sort_keys=sort_keys, ensure_ascii=False)

import unittest

# run testcase: python /Users/hain/chatopera/efaqa-corpus-zh/app/sample.py Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_data(self):
        print("test_load_data")
        for x in efaqa_corpus_zh.load():
            print(pretty(x))
            sys.exit()

def test():
    suite = unittest.TestSuite()
    suite.addTest(Test("test_load_data"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    test()

if __name__ == '__main__':
    main()