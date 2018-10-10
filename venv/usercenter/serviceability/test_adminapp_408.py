
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.admin_app



class runAll_Test(unittest.TestCase):
    def test_qa_408(self):

        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getTelephoneAudit_qa.json"     #拼成绝对路径
        env_url = "http://qa.ymmoa.com"
        for i in range(1000):
            responseJson= base.admin_app.getTelephoneAudit(env_url, path)
            self.assertNotEqual(len(responseJson), 0, "运行失败")
