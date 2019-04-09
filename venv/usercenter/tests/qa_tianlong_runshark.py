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
uc_check_service_test_suite_id = data.requestData.uc_check_service_test_suite_id
ymm_info_app_test_suite_id = data.requestData.ymm_info_app_test_suite_id


uc_check_service_timeData = before_shark.uc_check_service(env_id)
ymm_info_app_timeData = before_shark.ymm_info_app(env_id)
time.sleep(30)

class tianlong_shark_Test(unittest.TestCase):
     def test_uc_check_service(self):
         reporteponseJson = sharkUtil.queryResult(uc_check_service_timeData, str(uc_check_service_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0, msg="服务" + "uc_check_service" + "有失败的case，报告地址：" + data.requestData.report_url_service + "&ref_id=" + str(uc_check_service_test_suite_id) + "&token=" + uc_check_service_timeData)
         print("uc_check_service测试报告地址" + data.requestData.report_url_service + "&ref_id=" + str(uc_check_service_test_suite_id) + "&token=" + uc_check_service_timeData)

     def test_ymm_info_app(self):
         reporteponseJson = sharkUtil.queryResult(ymm_info_app_timeData, str(ymm_info_app_test_suite_id))
         self.assertEqual(reporteponseJson['data']['summary']['total_run_failed'], 0,msg="服务"+"ymm_info_app"+"有失败的case，报告地址："+data.requestData.report_url_service+"&ref_id="+str(ymm_info_app_test_suite_id)+"&token="+ymm_info_app_timeData)
         print("ymm_info_app测试报告地址" + data.requestData.report_url_service + "&ref_id=" + str(ymm_info_app_test_suite_id) + "&token=" + ymm_info_app_timeData)



if __name__ == '__main__':
    unittest.main()