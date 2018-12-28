
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.userCenter4x_service
import utils.getIpPort



class runQaUserCenter4xService_Test(unittest.TestCase):
    def test_qa_userCenter4x_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("userCenterServer4.x", "qa")
        responseJson = base.userCenter4x_service.getUserNameForWithDraw(http_host, "3123191582325473698")
        self.assertNotEqual(len(responseJson),0,"qa环境serCenter4x_service可用性运行失败")



if __name__ == '__main__':
    unittest.main()