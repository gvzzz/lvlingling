
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.info_app



class runDevnfoApp_Test(unittest.TestCase):
    def test_dev_info_app_serviceablity(self):
        env_url = data.requestData.dev
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getDriverInfo_dev.json"     #拼成绝对路径
        responseJson= base.info_app.getDriverInfo(env_url,path)
        self.assertNotEqual(len(responseJson),0,"dev环境info_app可用性运行失败")



if __name__ == '__main__':
    unittest.main()