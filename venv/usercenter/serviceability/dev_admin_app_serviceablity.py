
# -*- coding:utf-8 -*-
import sys
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest

import base.admin_app

class runDevAdminApp_Test(unittest.TestCase):
    def test_dev_admin_app_serviceablity(self):
        env_url = "http://dev-boss.ymmoa.com"
        path_base = os.path.abspath('..')  # 获取上级目录
        path = path_base + "/data/findByTelephone_dev.json"  # 拼成绝对路径
        responseJson = base.admin_app.findByTelephone(env_url, path)
        self.assertNotEqual(len(responseJson), 0, "dev环境admin_app可用性运行失败")


if __name__ == '__main__':
    unittest.main()