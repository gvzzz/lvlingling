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
import before_shark

env_id = 327
useraudit_service_test_suite_id = data.requestData.useraudit_service_test_suite_id
userCenter_app_test_suite_id = data.requestData.ymm_userCenter_app_test_suite_id
uc_auth_center_test_suite_id = data.requestData.uc_auth_center_test_suite_id
uc_info_center_test_suite_id = data.requestData.uc_info_center_test_suite_id

useraudit_service_timeData = before_shark.useraudit_service(env_id)
ymm_userCenter_app_timeData = before_shark.userCenter_app(env_id)
uc_auth_center_timeData = before_shark.uc_auth_center(env_id)
uc_info_center_timeData = before_shark.uc_info_center(env_id)
time.sleep(120)

class haokun_shark_Test(unittest.TestCase):
     def test_useraudit_service(self):
         reporteponseJson = sharkUtil.queryResult(useraudit_service_timeData, str(useraudit_service_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务" + "useraudit_service" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(useraudit_service_test_suite_id) + "&token=" + useraudit_service_timeData)
         print("useraudit_service测试报告地址" + data.requestData.report_url_service + "&ref_id=" + str(useraudit_service_test_suite_id) + "&token=" + useraudit_service_timeData)

     def test_userCenter_app(self):
         reporteponseJson = sharkUtil.queryResult(ymm_userCenter_app_timeData, str(userCenter_app_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务"+"userCenter_app"+"有失败的case，报告地址："+data.requestData.report_url_service+"&ref_id="+str(userCenter_app_test_suite_id)+"&token="+ymm_userCenter_app_timeData)
         print("userCenter_app测试报告地址" + data.requestData.report_url_service + "&ref_id=" + str(userCenter_app_test_suite_id) + "&token=" + ymm_userCenter_app_timeData)

     def test_uc_auth_center(self):
         reporteponseJson = sharkUtil.queryResult(uc_auth_center_timeData, str(uc_auth_center_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务"+"uc_auth_center"+"有失败的case，报告地址："+data.requestData.report_url_service+"&ref_id="+str(uc_auth_center_test_suite_id)+"&token="+uc_auth_center_timeData)
         print("uc_auth_center测试报告地址" + data.requestData.report_url_service + "&ref_id=" + str(uc_auth_center_test_suite_id) + "&token=" + uc_auth_center_timeData)

     def test_uc_info_center(self):
         reporteponseJson = sharkUtil.queryResult(uc_info_center_timeData, str(uc_info_center_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务" + "uc_info_center" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(uc_info_center_test_suite_id) + "&token=" + uc_info_center_timeData)
         print("uc_info_center测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(uc_info_center_test_suite_id) + "&token=" + uc_info_center_timeData)


if __name__ == '__main__':
    unittest.main()