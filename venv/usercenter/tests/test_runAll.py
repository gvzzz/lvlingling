#coding:utf-8
import unittest
import data
import json
import time
import sharkUtil




class runAll_sharkTest(unittest.TestCase):
    def test_new_boss(self):
        timeData = sharkUtil.trigger('new_boss.json')
        time.sleep(25)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_progress, 0, msg="new_boss有正在执行的项目")
        self.assertEqual(total_run_failed, 0, msg="new_boss执行失败")


    def test_userCenter(self):
        timeData = sharkUtil.trigger('userCenter4_service.json')
        time.sleep(35)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="userCenter有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="userCenter有正在执行的项目")


    def test_ymm_admin_app(self):
        timeData = sharkUtil.trigger('ymm_admin_app.json')
        time.sleep(40)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_admin_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_admin_app有正在执行的项目")



    def test_ymm_info_app(self):
        timeData = sharkUtil.trigger('ymm_info_app.json')
        time.sleep(50)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_info_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_info_app有正在执行的项目")



    def test_ymm_reference_app(self):
        timeData = sharkUtil.trigger('ymm_reference_app.json')
        time.sleep(40)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_reference_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_reference_app有正在执行的项目")

    def test_authenticate_service(self):
        timeData = sharkUtil.trigger('authenticate_service.json')
        time.sleep(40)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="authenticate_service有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="authenticate_service有正在执行的项目")


    def test_ymm_userCenter_app(self):
        timeData = sharkUtil.trigger('ymm_userCenter_app.json')
        time.sleep(50)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_userCenter_app有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="ymm_userCenter_app有正在执行的项目")

    def test_uc_check_service(self):
        timeData = sharkUtil.trigger('uc_check_service.json')
        time.sleep(15)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="uc_check_service有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="uc_check_service有正在执行的项目")


    def test_uc_doorkeeper_center(self):
        timeData = sharkUtil.trigger('uc_doorkeeper_center.json')
        time.sleep(20)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="uc_doorkeeper_center有执行失败的case")
        self.assertEqual(total_run_progress, 0, msg="uc_doorkeeper_center有正在执行的项目")


if __name__ == '__main__':
    unittest.main()