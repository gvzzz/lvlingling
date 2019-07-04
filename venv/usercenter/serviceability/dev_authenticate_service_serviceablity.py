
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import base.authenticate_service
import utils.getIpPort


class runDevAuthenticateService_Test(unittest.TestCase):
    def test_dev_authenticate_service(self):
         http_host = utils.getIpPort.get_pigon_ip_and_port("authenticate-service","dev")
         responseJson = base.authenticate_service.findByCertifyIDAndCertifyNameV2(http_host,"361021198905222996","李孟柱","1")
         self.assertNotEqual(len(responseJson),0,"dev环境authenticate-service可用性运行失败")

if __name__ == '__main__':
    unittest.main()