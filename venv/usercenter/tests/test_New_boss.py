#coding:utf-8

import unittest

import time
import sharkUtil
import test_runAllNew


class new_boss_sharkTest(unittest.TestCase):
    def test_ymm_reference_app(self):
        timeData_ymm_reference_app = test_runAllNew.runAll_sharkTest.list[4]
        reporteponseJson = sharkUtil.queryReport(timeData_ymm_reference_app)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_failed, 0,
                         msg="ymm_reference_app有执行失败的case" + "报告地址：" + "http://shark.ymmoa.com/#/report/report?token=" + timeData_ymm_reference_app)
        # self.assertEqual(total_run_progress, 0, msg="ymm_reference_app有正在执行的项目")



if __name__ == '__main__':
    unittest.main()
