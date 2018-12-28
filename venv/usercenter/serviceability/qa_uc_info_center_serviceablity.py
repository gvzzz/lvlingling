
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import base.uc_info_center
import utils.getIpPort


class runQaUcInfoCenter_Test(unittest.TestCase):
    def test_qa_uc_info_center(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-info-center", "qa")
        responseJson = base.uc_info_center.getEnterpriseInfoByAccountId(http_host, "2")
        self.assertNotEqual(len(responseJson), 0, "qa环境uc-info-center可用性运行失败")


if __name__ == '__main__':
    unittest.main()