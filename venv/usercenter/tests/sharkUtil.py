# -*- coding:utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import data.requestData
import utils.httpUtil
import json
import time




#触发shark平台
def trigger(test_suite_id):
    triggerUrl = data.requestData.trigger_url
    triggerHeaders = data.requestData.trigger_header
    #f = file(jsonName)
    #PostJson = json.load(f)
    PostJson = rebuildJson(test_suite_id)

    triggerResponse = utils.httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
    triggerReponseJson = json.loads(triggerResponse)
    timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
    print (timeData)
    return timeData

#按照组来触发shark平台构建  20190408
def triggerGroup(test_suit_id,env_id):
    triggerUrl = data.requestData.runGroupASync_url
    triggerHeaders = data.requestData.trigger_header
    dict = {}
    dict['suite_id'] = test_suit_id
    dict['env_id'] = env_id
    dict['project_id'] = None
    triggerResponse = utils.httpUtil.Post(triggerUrl, triggerHeaders, dict)
    triggerReponseJson = json.loads(triggerResponse)
    timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告'''
    print("+++++++++++   "+timeData+"  ++++++++++++")
    return timeData


#查询报告
def queryReport(timeData):
    reportUrl = data.requestData.report_url + "token="+timeData
    print (reportUrl)
    reportHeaders = data.requestData.report_header
    reportResponse = utils.httpUtil.Get(reportUrl, reportHeaders)
    reporteponseJson = json.loads(reportResponse)
    return reporteponseJson

#查询结果
def queryResult(timeData,test_suit_id):
    reportUrl = data.requestData.result_url_service + "&token="+timeData + "&ref_id="+test_suit_id
    print (reportUrl)
    reportHeaders = data.requestData.report_header
    reportResponse = utils.httpUtil.Get(reportUrl, reportHeaders)
    reporteponseJson = json.loads(reportResponse)
    return reporteponseJson


#按照test_suite_id查询需要每日dayliy的testId的数组
def queryTestIdBytest_suite_id(test_suite_id):
    queryTestIdBytest_suite_id_url = data.requestData.queryTestId_url
    queryTestIdBytest_suite_id_header = data.requestData.queryTestId_header
    PostJson = {"operation": "query", "data": {"test_suite_id": "0"}}
    PostJson['data']['test_suite_id']= test_suite_id
    queryTestIdResponse = utils.httpUtil.Post(queryTestIdBytest_suite_id_url, queryTestIdBytest_suite_id_header, PostJson)
    queryTestIdResponseJson = json.loads(queryTestIdResponse)
    childrenArray = json.loads(json.dumps(queryTestIdResponseJson['data'][0]['children'], ensure_ascii=False))   #把children那层遍历出来
    print (childrenArray[1])
    print (len(childrenArray))

    list = []
    for i in range(len(childrenArray)-1):            #遍历children 但是第一个object弃用
        if(childrenArray[i+1]['is_Daily'] == 1 ):     #判断下这个case是否需要执行的状态位
            test_id = childrenArray[i+1]['test_case_id']   #不取第一个object
            list.append(test_id)
    print (list)
    return list

#将testId重新组装到json里面
def rebuildJson(test_suite_id):
    list = queryTestIdBytest_suite_id(test_suite_id)
    test_case_datas_list = []
    for i in range(len(list)):
        dict = {}
        dict['test_case_id'] = list[i]
        test_case_datas_list.append(dict)
    data = {}
    data["env_id"] = 327  # 暂时写死
    data["token"] = None
    data["test_suite_id"] = str(test_suite_id)
    data["test_case_datas"] = test_case_datas_list
    print (data)
    return data



    #test_case_dataArray = newTestList

#跑一个组的case
def runGroupASync(postJson):
    triggerUrl = data.requestData.runGroupASync_url
    triggerHeaders = data.requestData.runGroupASync_header
    # f = file(jsonName)
    # PostJson = json.load(f)
    PostJson = postJson
    triggerResponse = utils.httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
    triggerReponseJson = json.loads(triggerResponse)
    timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
    print (timeData)
    return timeData














def triggerAll():
    list = []
    timeData_newBoss = trigger(data.requestData.new_boss_test_suite_id)
    timeData_userCenter = trigger(data.requestData.userCenter4_service_test_suite_id)
    timeData_ymm_admin_app = trigger(data.requestData.ymm_admin_app_test_suite_id)
    timeData_ymm_info_app = trigger(data.requestData.ymm_info_app_test_suite_id)
    timeData_ymm_reference_app = trigger(data.requestData.ymm_reference_app_test_suite_id)
    timeData_authenticate_service = trigger(data.requestData.authenticate_service_test_suite_id)
    timeData_ymm_userCenter_app = trigger(data.requestData.ymm_userCenter_app_test_suite_id)
    timeData_uc_check_service = trigger(data.requestData.uc_check_service_test_suite_id)
    timeData_uc_doorkeeper_center = trigger(data.requestData.uc_doorkeeper_center_test_suite_id)
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
    #triggerAll()
    #queryTestIdBytest_suite_id(393)
    #rebuildJson(393)
    '''list = []
    total_sucess = 0
    list =[606, 525, 526, 527, 529, 531, 532, 535, 536, 537, 538, 539, 540, 542, 543, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 560, 561, 563, 564, 565, 569, 581, 582, 583, 584, 585, 586, 587, 591, 596, 597, 603, 654, 655, 657, 696, 697, 701, 702, 703, 704, 707, 709]
    for i in range(len(list)):
        total_sucess = total_sucess+list[i]
    print (total_sucess)'''

    queryReport("2019-04-09-11-35-38_57")