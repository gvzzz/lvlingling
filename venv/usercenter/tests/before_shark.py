#coding:utf-8
import unittest
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import sharkUtil
import data.requestData

def userCenter4_service(env_id):
    test_suit_id = data.requestData.userCenter4_service_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return  timeData


def uc_info_center(env_id):
    test_suit_id = data.requestData.uc_info_center_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def new_boss(env_id):
    test_suit_id = data.requestData.new_boss_test_suit_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def ymm_admin_app(env_id):
    test_suit_id = data.requestData.ymm_admin_app_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData


def useraudit_service(env_id):
    test_suit_id = data.requestData.useraudit_service_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def userCenter_app(env_id):
    test_suit_id = data.requestData.ymm_userCenter_app_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def uc_auth_center(env_id):
    test_suit_id = data.requestData.uc_auth_center_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id, env_id)
    return timeData



'''def truck_service_service(env_id):
    test_suit_id = data.requestData.userCenter4_service_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return  timeData'''


def uc_check_service(env_id):
    test_suit_id = data.requestData.uc_check_service_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def ymm_info_app(env_id):
    test_suit_id = data.requestData.ymm_info_app_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def uc_doorkeeper_center(env_id):
    test_suit_id = data.requestData.uc_doorkeeper_center_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData


def reference_service(env_id):
    test_suit_id = data.requestData.reference_service_test_suit_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def ymm_refenrence_app(env_id):
    test_suit_id = data.requestData.ymm_reference_app_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData

def agreement_service(env_id):
    test_suit_id = data.requestData.agreement_service_test_suite_id
    timeData = sharkUtil.triggerGroup(test_suit_id,env_id)
    return timeData






if __name__ == '__main__':
    unittest.main()