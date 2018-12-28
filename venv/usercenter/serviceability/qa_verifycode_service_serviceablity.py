
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import base.verifycode_service
import utils.getIpPort


class runQaVerifycodeService_Test(unittest.TestCase):
    def test_qa_verifycode_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("ymm-verifycode-service","qa")
        responseJson = base.verifycode_service.querySMSVerifyCode(http_host,"2")
        self.assertNotEqual(len(responseJson),0,"qa环境verifycode-service可用性运行失败")


if __name__ == '__main__':
    unittest.main()