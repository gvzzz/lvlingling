
# -*- coding:utf-8 -*-
import sys
import os.path

import base.agreement_service

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import utils.getIpPort
import json


class runDevAgreementService_Test(unittest.TestCase):
    def test_dev_agreement_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("agreement-service", "dev")
        response = base.agreement_service.getAllAuthItems(http_host, '2')
        responseJson = json.loads(response)
        self.assertEqual(responseJson['errorCode'],0,"dev环境agreement-service可用性运行失败")

if __name__ == '__main__':
    unittest.main()