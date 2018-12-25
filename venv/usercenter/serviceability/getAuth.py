
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import utils.getAuth
import json

class auth_Test(unittest.TestCase):
    def test_qa_auth(self):
        env = "beta"
        phonelist = [17321040084,18490736431,18163910002]
        usertypelist = [1,1,2]
        for i in range(50):
            authResponseJson0 = utils.getAuth.generateAuthApi(phonelist[0], usertypelist[0], env)
            auth0 = json.loads(authResponseJson0)['auth']
            self.assertNotEqual(auth0,None,"qa auth0获取失败")
            authResponseJson1 = utils.getAuth.generateAuthApi(phonelist[1], usertypelist[1], env)
            auth1 = json.loads(authResponseJson1)['auth']
            self.assertNotEqual(auth1, None, "qa auth1获取失败")
            authResponseJson2 = utils.getAuth.generateAuthApi(phonelist[2], usertypelist[2], env)
            auth2 = json.loads(authResponseJson2)['auth']
            self.assertNotEqual(auth2, None, "qa auth2获取失败")




    def test_dev_auth(self):
        env = "dev"
        phonelist = [13423300016, 13057580010, 18163910002]
        usertypelist = [1, 1, 2]
        for i in range(50):
            authResponseJson0 = utils.getAuth.generateAuthApi(phonelist[0], usertypelist[0], env)
            auth0 = json.loads(authResponseJson0)['auth']
            self.assertNotEqual(auth0, None, "dev auth0获取失败")
            # authResponseJson1 = utils.getAuth.generateAuthApi(phonelist[1], usertypelist[1], env)
            # auth1 = json.loads(authResponseJson1)['auth']
            # self.assertNotEqual(auth1, None, "dev auth1获取失败")
            # authResponseJson2 = utils.getAuth.generateAuthApi(phonelist[2], usertypelist[2], env)
            # auth2 = json.loads(authResponseJson2)['auth']
            # self.assertNotEqual(auth2, None, "dev auth2获取失败")
            #

