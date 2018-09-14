#coding:utf-8
import httpUtil
import data
import json
import time

#触发shark平台
def trigger(jsonName):
    triggerUrl = data.trigger_url
    triggerHeaders = data.trigger_header
    f = file(jsonName)
    PostJson = json.load(f)

    triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
    triggerReponseJson = json.loads(triggerResponse)
    timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
    return timeData

#查询报告
def queryReport(timeData):
    reportUrl = data.report_url
    reportHeaders = data.report_header
    reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
    reporteponseJson = json.loads(reportResponse)
    return reporteponseJson

def queryTestIdBytest_suite_id(test_suite_id):
    queryTestIdBytest_suite_id_url = data.queryTestId_url
    queryTestIdBytest_suite_id_header = data.queryTestId_header
    PostJson = {"operation": "query", "data": {"test_suite_id": "810"}}
    PostJson['data']['test_suite_id']
    queryTestIdResponse = httpUtil.Post(queryTestIdBytest_suite_id_url, queryTestIdBytest_suite_id_header, PostJson)


def triggerAll():
    timeData_newBoss = trigger('new_boss.json')
    timeData_userCenter = trigger('userCenter4_service.json')
    timeData_ymm_admin_app = trigger('ymm_admin_app.json')
    timeData_ymm_info_app = trigger('ymm_info_app.json')
    timeData_ymm_reference_app = trigger('ymm_reference_app.json')
    timeData_authenticate_service = trigger('authenticate_service.json')
    timeData_ymm_userCenter_app = trigger('ymm_userCenter_app.json')
    timeData_uc_check_service = trigger('uc_check_service.json')
    timeData_uc_doorkeeper_center = trigger('uc_doorkeeper_center.json')
    list = []
    list.append(timeData_newBoss)
    time.sleep(5)
    list.append(timeData_userCenter)
    time.sleep(5)
    list.append(timeData_ymm_admin_app)
    time.sleep(5)
    list.append(timeData_ymm_info_app)
    time.sleep(5)
    list.append(timeData_ymm_reference_app)
    time.sleep(5)
    list.append(timeData_authenticate_service)
    time.sleep(5)
    list.append(timeData_ymm_userCenter_app)
    time.sleep(5)
    list.append(timeData_uc_check_service)
    time.sleep(5)
    list.append(timeData_uc_doorkeeper_center)
    return list

if __name__ == '__main__':
    triggerAll()
