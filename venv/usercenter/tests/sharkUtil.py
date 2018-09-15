# -*- coding:utf-8 -*-
import httpUtil
import data
import json
import time
import numpy as np

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


#按照test_suite_id查询需要每日dayliy的testId的数组
def queryTestIdBytest_suite_id(test_suite_id):
    queryTestIdBytest_suite_id_url = data.queryTestId_url
    queryTestIdBytest_suite_id_header = data.queryTestId_header
    PostJson = {"operation": "query", "data": {"test_suite_id": "0"}}
    PostJson['data']['test_suite_id']= test_suite_id
    queryTestIdResponse = httpUtil.Post(queryTestIdBytest_suite_id_url, queryTestIdBytest_suite_id_header, PostJson)
    queryTestIdResponseJson = json.loads(queryTestIdResponse)
    childrenArray = json.loads(json.dumps(queryTestIdResponseJson['data'][0]['children'], ensure_ascii=False))   #把children那层遍历出来
    #childrenArrayNoAscii =  json.dumps(childrenArray, ensure_ascii=False)
    print childrenArray[1]
    print len(childrenArray)
    list = []
    for i in range(len(childrenArray)-1):            #遍历children 但是第一个object弃用
        test_id = childrenArray[i+1]['test_case_id']   #不取第一个object
        list.append(test_id)
    print list
    return list

#将testId重新组装到json里面
def rebuildJson(test_suite_id):
    #f = file(jsonName)
    #PostJson = json.load(f)
    #test_case_dataArray =  json.loads(json.dumps(PostJson['test_case_datas'], ensure_ascii=False))

   # testIdlist = queryTestIdBytest_suite_id(test_suite_id)
   # test_case_dataArray[len(testIdlist)]

    list = [11,12,13,14]




        #newTestList.insert(i,j)

    list1 = []
    for i in range(len(list)):
        dict = {}
        dict['test_case_id'] = list[i]
        list1.append(dict)

        print list1

    data = {}
    data["env_id"] = 327  # 暂时写死
    data["token"] = None
    data["test_suite_id"] = str(test_suite_id)


    data["test_case_datas"] = list1
    print data
    jsonStr = json.dumps(data)

    print jsonStr



    #test_case_dataArray = newTestList
















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
    rebuildJson(393)