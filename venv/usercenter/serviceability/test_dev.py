
# -*- coding:utf-8 -*-
import sys
import os.path
import data.requestData
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import userCenter_app



class runAll_Test(unittest.TestCase):
    def test_dev_userCenter_app_serviceablity(self):
        env_url = data.requestData.dev
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getShipperInfo_dev.json"     #拼成绝对路径
        responseJson= userCenter_app.getShipperInfo(env_url, path)
        self.assertNotEqual(len(responseJson), 0, "dev环境userCenter_app可用性运行失败")

if __name__ == '__main__':
    unittest.main()