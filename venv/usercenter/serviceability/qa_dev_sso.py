
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import utils.getAuth



class sso_Test(unittest.TestCase):
    def test_qa_sso(self):
        path_base = os.path.abspath('..')  # 获取上级目录
        path = path_base + "/data/sso_qa.json"  # 拼成绝对路径
        passport = utils.getAuth.getSso(path, "qa")
        self.assertNotEqual(passport,'', "qa的sso运行失败")
