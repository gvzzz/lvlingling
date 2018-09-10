#coding:utf-8

import unittest
import httpUtil
import data
import json
import time

class new_boss_serviceablityTest(unittest.TestCase):
    def test_getuserinfo(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        PostJson = {"env_id": 327,"token":None, "test_suite_id": "393", "test_case_datas": [{"test_case_id": 541}]}
        triggerResponse = httpUtil.Post(triggerUrl,triggerHeaders,PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']     #从触发器的接口中读出返回data，去查询对应的报告

        time.sleep(0.1)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        self.assertEqual(total_run_failed, 0, msg="执行失败")


if __name__ == '__main__':
    unittest.main()
