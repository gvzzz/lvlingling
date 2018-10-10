
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.userCenter_app
import base.new_boss
import base.info_app
import base.reference_app
import base.userCenter4x_service
import base.uc_check_service
import base.uc_doorkeeper_center
import base.admin_app
import base.authenticate_service
import base.uc_auth_center
import base.verifycode_service
import utils.getIpPort


class runAll_Test(unittest.TestCase):
    def test_qa_userCenter_app_serviceablity(self):
        env_url = data.requestData.qa
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getShipperInfo_qa.json"     #拼成绝对路径
        responseJson= base.userCenter_app.getShipperInfo(env_url, path)
        self.assertNotEqual(len(responseJson),0,"qa环境userCenter_app可用性运行失败")

    def test_qa_new_boss_serviceablity(self):
        env_url = data.requestData.qa
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getuserstatus_qa.json"     #拼成绝对路径
        responseJson= base.new_boss.getuserstatus(env_url, path)
        self.assertNotEqual(len(responseJson),0,"qa环境new_boss可用性运行失败")

    def test_qa_info_app_serviceablity(self):
        env_url = data.requestData.qa
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getDriverInfo_qa.json"     #拼成绝对路径
        responseJson = base.info_app.getDriverInfo(env_url,path)
        self.assertNotEqual(len(responseJson),0,"qa环境info_app可用性运行失败")

    def test_qa_reference_app_serviceablity(self):
        env_url = data.requestData.qa
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/getCopilotlist_qa.json"     #拼成绝对路径
        responseJson= base.reference_app.getCopilotlist(env_url,path)
        self.assertNotEqual(len(responseJson),0,"qa环境reference_app可用性运行失败")

    def test_qa_admin_app_serviceablity(self):
        env_url = "http://qa-boss.ymmoa.com"
        path_base = os.path.abspath('..')  #获取上级目录
        path = path_base + "/data/findByTelephone_qa.json"     #拼成绝对路径
        responseJson= base.admin_app.findByTelephone(env_url,path)
        self.assertNotEqual(len(responseJson),0,"qa环境admin_app可用性运行失败")

    def test_qa_userCenter4x_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("userCenterServer4.x", "qa")
        responseJson = base.userCenter4x_service.getUserNameForWithDraw(http_host, "3123191582325473698")
        self.assertNotEqual(len(responseJson),0,"qa环境serCenter4x_service可用性运行失败")

    def test_qa_uc_check_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-check-service","qa")
        responseJson = base.uc_check_service.getTelephone(http_host, "18916377820")
        self.assertNotEqual(len(responseJson),0,"qa环境uc_check_service可用性运行失败")


    def test_qa_doorkeeper_center(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-doorkeeper-center","qa")
        responseJson = base.uc_doorkeeper_center.selectByAccountId(http_host, "0")
        self.assertNotEqual(len(responseJson),0,"qa环境uc-doorkeeper-center可用性运行失败")

    def test_qa_authenticate_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("authenticate-service","qa")
        responseJson = base.authenticate_service.findByCertifyIDAndCertifyNameV2(http_host, "410101196709012881","哒哒","1")
        self.assertNotEqual(len(responseJson),0,"qa环境authenticate-service可用性运行失败")

    def test_qa_uc_auth_center(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-auth-center","qa")
        responseJson = base.uc_auth_center.findUserBlacklistInfo(http_host,"2")
        self.assertNotEqual(len(responseJson),0,"qa环境uc-auth-center可用性运行失败")


    def test_qa_verifycode_service(self):
        http_host = utils.getIpPort.get_pigon_ip_and_port("ymm-verifycode-service","qa")
        responseJson = base.verifycode_service.querySMSVerifyCode(http_host,"2")
        self.assertNotEqual(len(responseJson),0,"qa环境verifycode_service可用性运行失败")


if __name__ == '__main__':
    unittest.main()