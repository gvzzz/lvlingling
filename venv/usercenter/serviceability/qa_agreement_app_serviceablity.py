
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import data
import json

import base.uc_agreement_app

class runDevAgreement_App_Test(unittest.TestCase):
    def test_dev_agereement_app_serviceablity(self):
        env_url = data.requestData.dev
        path_base = os.path.abspath('..')  # 获取上级目录
        path = path_base + "/data/getAllAuthItem_dev.json"  # 拼成绝对路径
        response = base.uc_agreement_app.getAllAuthItem(env_url,path)
        responseJson = json.loads(response)
        self.assertEqual(responseJson["result"], 1, "dev环境agereement_app可用性运行失败")


if __name__ == '__main__':
    unittest.main()