
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import unittest
import base.new_boss

class runQaNewboss_Test(unittest.TestCase):
    def test_qa_new_boss_serviceablity(self):
         env_url = data.requestData.qa
         path_base = os.path.abspath('..')  #获取上级目录
         path = path_base + "/data/getuserstatus_qa.json"     #拼成绝对路径
         responseJson= base.new_boss.getuserstatus(env_url, path)
         self.assertNotEqual(len(responseJson),0,"qa环境new_boss可用性运行失败")




if __name__ == '__main__':
    unittest.main()