
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.uc_auth_center
import utils.getIpPort


class runQaUcAuthCenter_Test(unittest.TestCase):
    def test_qa_uc_auth_center(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-auth-center","qa")
        responseJson = base.uc_auth_center.findUserBlacklistInfo(http_host,"2")
        self.assertNotEqual(len(responseJson),0,"qa环境uc-auth-center可用性运行失败")

if __name__ == '__main__':
    unittest.main()