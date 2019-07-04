
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import base.authenticate_service
import utils.getIpPort


class runQaAuthenticateService_Test(unittest.TestCase):
    def test_qa_authenticate_service(self):
         http_host = utils.getIpPort.get_pigon_ip_and_port("authenticate-service","qa")
         responseJson = base.authenticate_service.findByCertifyIDAndCertifyNameV2(http_host, "410101196709012881","哒哒","1")
         self.assertNotEqual(len(responseJson),0,"qa环境authenticate-service可用性运行失败")

if __name__ == '__main__':
    unittest.main()