#coding:utf-8
import unittest
import data
import json
import time
import sharkUtil




class runAll_sharkTest(unittest.TestCase):
    list = sharkUtil.triggerAll()


    @classmethod
    def setUpClass(self):
        time.sleep(180)


    def test_new_boss(self):
        timeData_newBoss = runAll_sharkTest.list[0]
        reporteponseJson = sharkUtil.queryReport(timeData_newBoss)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_progress, 0, msg="new_boss有正在执行的项目")
        #self.assertEqual(total_run_failed, 0, msg="new_boss执行失败")

    def test_userCenter(self):
        timeData_userCenter = runAll_sharkTest.list[1]
        reporteponseJson = sharkUtil.queryReport(timeData_userCenter)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="userCenter有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="userCenter有正在执行的项目")

    def test_ymm_admin_app(self):

        timeData_ymm_admin_app = runAll_sharkTest.list[2]
        reporteponseJson = sharkUtil.queryReport(timeData_ymm_admin_app)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_admin_app有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="ymm_admin_app有正在执行的项目")

    def test_ymm_info_app(self):
        timeData_ymm_info_app = runAll_sharkTest.list[3]
        reporteponseJson = sharkUtil.queryReport(timeData_ymm_info_app)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_info_app有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="ymm_info_app有正在执行的项目")

    def test_ymm_reference_app(self):
        timeData_ymm_reference_app = runAll_sharkTest.list[4]
        reporteponseJson = sharkUtil.queryReport(timeData_ymm_reference_app)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_reference_app有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="ymm_reference_app有正在执行的项目")

    def test_authenticate_service(self):
        timeData_authenticate_service = runAll_sharkTest. list[5]
        reporteponseJson = sharkUtil.queryReport(timeData_authenticate_service)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="authenticate_service有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="authenticate_service有正在执行的项目")

    def test_ymm_userCenter_app(self):
        timeData_ymm_userCenter_app = runAll_sharkTest.list[6]
        reporteponseJson = sharkUtil.queryReport(timeData_ymm_userCenter_app)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="ymm_userCenter_app有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="ymm_userCenter_app有正在执行的项目")

    def test_uc_check_service(self):
        timeData_uc_check_service = runAll_sharkTest.list[7]
        reporteponseJson = sharkUtil.queryReport(timeData_uc_check_service)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="uc_check_service有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="uc_check_service有正在执行的项目")

    def test_uc_doorkeeper_center(self):
        timeData_uc_doorkeeper_center = runAll_sharkTest.list[8]
        reporteponseJson = sharkUtil.queryReport(timeData_uc_doorkeeper_center)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0, msg="uc_doorkeeper_center有执行失败的case")
        #self.assertEqual(total_run_progress, 0, msg="uc_doorkeeper_center有正在执行的项目")




if __name__ == '__main__':
    unittest.main()