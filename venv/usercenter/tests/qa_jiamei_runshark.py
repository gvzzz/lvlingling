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
uc_doorkeeper_center_test_suite_id = data.requestData.uc_doorkeeper_center_test_suite_id
reference_service_test_suite_id = data.requestData.reference_service_test_suit_id
ymm_refenrence_app_test_suite_id = data.requestData.ymm_reference_app_test_suite_id
agreement_service_test_suite_id = data.requestData.agreement_service_test_suite_id
userCenter4_service_test_suite_id = data.requestData.userCenter4_service_test_suite_id


uc_doorkeeper_center_timeData = before_shark.uc_doorkeeper_center(env_id)
reference_service_timeData = before_shark.reference_service(env_id)
ymm_refenrence_app_timeData = before_shark.ymm_refenrence_app(env_id)
agreement_service_timeData = before_shark.agreement_service(env_id)
userCenter4_service_timeData = before_shark.userCenter4_service(env_id)

time.sleep(90)

class jiamei_shark_Test(unittest.TestCase):
     def test_uc_doorkeeper_center(self):
         reporteponseJson = sharkUtil.queryResult(uc_doorkeeper_center_timeData, str(uc_doorkeeper_center_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务" + "test_uc_doorkeeper_center" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(uc_doorkeeper_center_test_suite_id) + "&token=" + uc_doorkeeper_center_timeData)
         print("test_uc_doorkeeper_center测试报告地址:"+data.requestData.report_url_service + "&ref_id=" + str(uc_doorkeeper_center_test_suite_id) + "&token=" + uc_doorkeeper_center_timeData)

     def test_reference_service(self):
         reporteponseJson = sharkUtil.queryResult(reference_service_timeData, str(reference_service_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务"+"reference_service"+"有失败的case，报告地址："+data.requestData.report_url_service+"&ref_id="+str(reference_service_test_suite_id)+"&token="+reference_service_timeData)
         print("reference_service测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(reference_service_test_suite_id) + "&token=" + reference_service_timeData)

     def test_ymm_refenrence_app(self):
         reporteponseJson = sharkUtil.queryResult(ymm_refenrence_app_timeData, str(ymm_refenrence_app_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务"+"refenrence_app"+"有失败的case，报告地址："+data.requestData.report_url_service+"&ref_id="+str(ymm_refenrence_app_test_suite_id)+"&token="+ymm_refenrence_app_timeData)
         print("refenrence_app测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(ymm_refenrence_app_test_suite_id) + "&token=" + ymm_refenrence_app_timeData)


     def test_agreement_service(self):
         reporteponseJson = sharkUtil.queryResult(agreement_service_timeData, str(agreement_service_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务" + "refenrence_app" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(agreement_service_test_suite_id) + "&token=" + agreement_service_timeData)
         print("agreement_service测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(agreement_service_test_suite_id) + "&token=" + agreement_service_timeData)

     def test_userCenter4_service(self):
         reporteponseJson = sharkUtil.queryResult(userCenter4_service_timeData,str(userCenter4_service_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,
                              msg="服务" + "userCenter4_service" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(
                                  userCenter4_service_test_suite_id) + "&token=" + userCenter4_service_timeData)
         print("userCenter4_service测试报告地址:" + data.requestData.report_url_service + "&ref_id=" + str(
                 userCenter4_service_test_suite_id) + "&token=" + userCenter4_service_timeData)


if __name__ == '__main__':
    unittest.main()