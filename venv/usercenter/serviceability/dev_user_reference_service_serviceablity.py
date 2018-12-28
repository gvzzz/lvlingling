
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.user_reference_service
import utils.getIpPort


class rundevUserReferenceService_Test(unittest.TestCase):
    #最好看下代码的接口原型 看了4080无论如何传参，虽然能调通但是结果都是null
    def test_dev_user_reference_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("user-reference-service", "dev")
        responseJson = base.user_reference_service.findByUserId(http_host, "")
        print(responseJson)
    # self.assertNotEqual(len(responseJson), 0, "qa环境user-reference-service可用性运行失败")



if __name__ == '__main__':
    unittest.main()