#coding:utf-8
import unittest
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time
import data.requestData
import before_shark
import sharkUtil

env_id = 327
userCenter4_service_test_suite_id = data.requestData.userCenter4_service_test_suite_id
uc_info_center_test_suite_id = data.requestData.uc_info_center_test_suite_id
new_boss_test_suite_id = data.requestData.new_boss_test_suit_id
ymm_admin_app_test_suite_id = data.requestData.ymm_admin_app_test_suite_id

userCenter4_service_timeData = before_shark.userCenter4_service(env_id)
uc_info_center_timeData = before_shark.uc_info_center(env_id)
new_boss_timeData = before_shark.new_boss(env_id)
ymm_admin_app_timeData = before_shark.ymm_admin_app(env_id)
time.sleep(90)

class dakun_shark_Test(unittest.TestCase):
     def test_userCenter4_service(self):
         reporteponseJson = sharkUtil.queryResult(userCenter4_service_timeData, str(userCenter4_service_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,
                          msg="服务" + "userCenter4_service" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(
                              userCenter4_service_test_suite_id) + "&token=" + userCenter4_service_timeData)
         print("userCenter4_service测试报告地址:"+data.requestData.report_url_service + "&ref_id=" + str(userCenter4_service_test_suite_id) + "&token=" + userCenter4_service_timeData)

     def test_uc_info_center(self):
         reporteponseJson = sharkUtil.queryResult(uc_info_center_timeData, str(uc_info_center_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务"+"uc_info_center"+"有失败的case，报告地址："+data.requestData.report_url_service+"&ref_id="+str(uc_info_center_test_suite_id)+"&token="+uc_info_center_timeData)
         print("uc_info_center测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(uc_info_center_test_suite_id) + "&token=" + uc_info_center_timeData)

     def test_new_boss(self):
         reporteponseJson = sharkUtil.queryResult(new_boss_timeData, str(new_boss_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务"+"new_boss"+"有失败的case，报告地址："+data.requestData.report_url_service+"&ref_id="+str(new_boss_test_suite_id)+"&token="+new_boss_timeData)
         print("new_boss测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(new_boss_test_suite_id) + "&token=" + new_boss_timeData)

     def test_ymm_admin_app(self):
         reporteponseJson = sharkUtil.queryResult(ymm_admin_app_timeData, str(ymm_admin_app_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,
                          msg="服务" + "ymm-admin-app" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(
                              ymm_admin_app_test_suite_id) + "&token=" + ymm_admin_app_timeData)
         print("ymm_admin_app测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(ymm_admin_app_test_suite_id) + "&token=" + ymm_admin_app_timeData)

if __name__ == '__main__':
    unittest.main()