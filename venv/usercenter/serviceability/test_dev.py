
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import utils.getIpPort
import utils.getAuth
import json


#dev环境检测登录
class runDevLogin_Test(unittest.TestCase):

    def test_dev_checkUserStatus(self):
        env_url = data.requestData.dev
        request_url = env_url + data.requestData.checkUserStatus_request
        headers = {}
        headers["Content-Type"] = 'application/json'
        headers["client-info"] = data.requestData.shipper_client
        bodyJson = {"telephone": "15660000090"}
        response = utils.httpUtil.Post(request_url, headers, bodyJson)
        responseJson = json.loads(response)
        self.assertEqual(responseJson['result'],1,"判断是否注册的接口有问题")
        self.assertEqual(responseJson['success'], True, "判断是否注册的接口有问题")
        self.assertEqual(responseJson['errorMsg'],'成功',"判断是否注册的接口有问题")



    def test_dev_getloginverifycode(self):
        env_url = data.requestData.dev
        request_url = env_url + data.requestData.getloginverifycode_request
        headers = {}
        headers["Content-Type"] = 'application/json'
        headers["client-info"] = data.requestData.shipper_client
        bodyJson = {"from": 6, "telephone": "15660000090"}
        response = utils.httpUtil.Post(request_url, headers, bodyJson)
        responseJson = json.loads(response)
        self.assertEqual(responseJson['result'], 1, "获取二维码接口有问题")
        self.assertEqual(responseJson['success'], True, "获取二维码接口有问题")



    #注意要保证下这个账号的状态，不能随便乱动
    def test_dev_login(self):
        env_url = data.requestData.dev
        request_url = env_url + data.requestData.login_request
        headers = {}
        headers["Content-Type"] = 'application/json'
        headers["client-info"] = data.requestData.shipper_client
        bodyJson = {"cmToken": "", "code": "1234", "telephone": "15660000000"}
        response = utils.httpUtil.Post(request_url, headers, bodyJson)
        responseJson = json.loads(response)
        print(responseJson)
        self.assertEqual(responseJson['result'], 1, "登录接口有问题")
        self.assertEqual(responseJson['success'], True, "登录接口有问题")
        self.assertIsNotNone(responseJson['info'])



    def test_dev_partnerToken(self):
        env_url = data.requestData.dev
        request_url = env_url + data.requestData.partnerToken_request
        headers = {}
        authResponseJson = utils.getAuth.generateAuthApi(15823445455, 1, 'dev')
        headers["Content-Type"] = 'application/json'
        headers["client-info"] = data.requestData.driver_client
        headers["Authorization"] = json.loads(authResponseJson)['auth']
        bodyJson = {}
        response = utils.httpUtil.Post(request_url, headers, bodyJson)
        responseJson = json.loads(response)
        print(responseJson)
        self.assertEqual(responseJson['result'], 1, "调货车帮的接口有问题，请联系货车帮")
        self.assertEqual(responseJson['errorMsg'], "成功", "调货车帮的接口有问题，请联系货车帮")






if __name__ == '__main__':
    unittest.main()