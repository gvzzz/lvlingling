#coding:utf-8

import unittest

import time
import sharkUtil


class new_boss_sharkTest(unittest.TestCase):
    def test_new_boss(self):
        timeData = sharkUtil.trigger('new_boss.json')
        time.sleep(25)
        reporteponseJson = sharkUtil.queryReport(timeData)
        total_run_failed = reporteponseJson['data']['summary']['total_run_failed']
        total_run_progress = reporteponseJson['data']['summary']['total_run_progress']
        self.assertEqual(total_run_progress, 0, msg="new_boss有正在执行的项目")
        self.assertEqual(total_run_failed, 0, msg="new_boss执行失败")




if __name__ == '__main__':
    unittest.main()
