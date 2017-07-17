#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
import time

from selenium import webdriver


class TestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://live.sioeye.cn/')
        self.assertIn("发现", self.browser.title)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main(verbosity=2)