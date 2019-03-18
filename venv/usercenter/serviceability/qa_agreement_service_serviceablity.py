
# -*- coding:utf-8 -*-
import sys
import os.path
import agreement_service
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import utils.getIpPort
import json


class runQaAgreementService_Test(unittest.TestCase):
    def test_qa_agreement_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("agreement-service", "qa")
        response = agreement_service.getAllAuthItems(http_host, '52')
        responseJson = json.loads(response)
        self.assertEqual(responseJson['errorCode'],0,"qa环境agreement-service可用性运行失败")

if __name__ == '__main__':
    unittest.main()