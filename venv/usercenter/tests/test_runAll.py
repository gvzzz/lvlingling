#coding:utf-8
import unittest
import httpUtil
import data
import json
import time




class runAll_sharkTest(unittest.TestCase):
    def test_new_boss(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('new_boss.json')
        PostJson = json.load(f)

        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']     #从触发器的接口中读出返回data，去查询对应的报告

        time.sleep(25)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_progress, 0, msg="new_boss有正在执行的项目")
        self.assertEqual(total_run_failed, 0, msg="new_boss执行失败")


    def test_userCenter(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('userCenter4_service.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(35)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="userCenter有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="userCenter有正在执行的项目")


    def test_ymm_admin_app(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('ymm_admin_app.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']     #从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(40)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_admin_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_admin_app有正在执行的项目")



    def test_ymm_info_app(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('ymm_info_app.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(40)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_info_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_info_app有正在执行的项目")



    def test_ymm_reference_app(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('ymm_reference_app.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(40)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_reference_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_reference_app有正在执行的项目")

    def test_authenticate_service(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('authenticate_service.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(40)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="authenticate_service有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="authenticate_service有正在执行的项目")


    def test_ymm_userCenter_app(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('ymm_userCenter_app.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(50)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_userCenter_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_userCenter_app有正在执行的项目")

    def test_uc_check_service(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('uc_check_service.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(15)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="uc_check_service有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="uc_check_service有正在执行的项目")


    def test_uc_doorkeeper_center(self):
        triggerUrl = data.trigger_url
        triggerHeaders = data.trigger_header
        f = file('uc_doorkeeper_center.json')
        PostJson = json.load(f)
        triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
        triggerReponseJson = json.loads(triggerResponse)
        timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
        time.sleep(20)
        reportUrl = data.report_url
        reportHeaders = data.report_header
        reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
        reporteponseJson = json.loads(reportResponse)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="uc_doorkeeper_center有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="uc_doorkeeper_center有正在执行的项目")


if __name__ == '__main__':
    unittest.main()