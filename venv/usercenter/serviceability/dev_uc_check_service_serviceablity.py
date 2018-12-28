
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import base.uc_check_service
import utils.getIpPort


class runDevUcCheckService_Test(unittest.TestCase):
    def test_qa_uc_check_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-check-service","dev")
        responseJson = base.uc_check_service.getOcrSupplierBillCounts(http_host,'','')
        self.assertNotEqual(len(responseJson),0,"dev环境uc_check_service可用性运行失败")



if __name__ == '__main__':
    unittest.main()