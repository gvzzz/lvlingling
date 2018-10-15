#coding:utf-8
import unittest
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time
import sharkUtil
import data.requestData
import base.admin_app


class runAll_Test(unittest.TestCase):

     #专门跑408的问题
     # def test_qa_408(self):
     #    path_base = os.path.abspath('..')  #获取上级目录
     #    path = path_base + "/data/getTelephoneAudit_qa.json"     #拼成绝对路径
     #    env_url = "http://qa.ymmoa.com"
     #    for i in range(10):
     #        responseJson= base.admin_app.getTelephoneAudit(env_url, path)
     #        self.assertNotEqual(len(responseJson), 0, msg="专门跑408运行失败")


    def test_All_UserCenter(self):
        runGroupASync_postJson = data.requestData.runGroupASync_postJson
        timeData = sharkUtil.runGroupASync(runGroupASync_postJson)
        #timeData = "2018-09-29-19-04-20_19"
        time.sleep(180)
        reporteponseJson = sharkUtil.queryReport(timeData)
        print  reporteponseJson
        childrenArray =  reporteponseJson["data"]["summary"]["children"]
        for i in range(len(childrenArray)):
            self.assertEqual(childrenArray[i]["summary_info"]["total_failed"], 0,
                             msg="有执行失败的case" + "报告地址：" + "http://shark.ymmoa.com/#/report/reportTable?token=" + timeData)



if __name__ == '__main__':
    unittest.main()