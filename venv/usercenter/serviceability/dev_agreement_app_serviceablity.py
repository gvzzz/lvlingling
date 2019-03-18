
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

class runQaAgreement_App_Test(unittest.TestCase):
    def test_qa_agereement_app_serviceablity(self):
        env_url = data.requestData.qa
        path_base = os.path.abspath('..')  # 获取上级目录
        path = path_base + "/data/getAllAuthItem_qa.json"  # 拼成绝对路径
        response = base.uc_agreement_app.getAllAuthItem(env_url,path)
        responseJson = json.loads(response)
        self.assertEqual(responseJson["result"], 1, "qa环境agereement_app可用性运行失败")


if __name__ == '__main__':
    unittest.main()