#coding:utf-8
import unittest
import data
import json
import time
import sharkUtil


class runAll_Test(unittest.TestCase):
    def test_All_UserCenter(self):
        runGroupASync_postJson = data.runGroupASync_postJson
        timeData = sharkUtil.runGroupASync(runGroupASync_postJson)
        #timeData = "2018-09-18-10-28-32_87"
        time.sleep(180)
        reporteponseJson = sharkUtil.queryReport(timeData)
        childrenArray =  reporteponseJson["data"]["summary"]["children"]
        for i in range(len(childrenArray)):
            self.assertEqual(childrenArray[i]["summary_info"]["total_failed"], 0,
                             msg="有执行失败的case" + "报告地址：" + "http://shark.ymmoa.com/#/report/report?token=" + timeData)



if __name__ == '__main__':
    unittest.main()