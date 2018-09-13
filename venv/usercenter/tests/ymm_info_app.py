#coding:utf-8
from unittest import TestCase
import httpUtil
import data
import json
import time



class ymm_info_app_sharkTest(TestCase):
    def test_userCenter(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('ymm_info_app.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']     #从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(10)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_progress, 0, msg="有正在执行的项目")
        self.assertEqual(total_run_failed, 0, msg="有执行失败的case")




if __name__ == '__main__':
    TestCase

