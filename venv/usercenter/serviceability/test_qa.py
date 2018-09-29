
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.userCenter_app



class runAll_Test(unittest.TestCase):
    def test_qa_userCenter_app_serviceablity(self):
        env_url = data.requestData.qa
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getShipperInfo_qa.json"     #拼成绝对路径
        responseJson= base.userCenter_app.getShipperInfo(env_url, path)
        self.assertIsNotNone(responseJson)


if __name__ == '__main__':
    unittest.main()