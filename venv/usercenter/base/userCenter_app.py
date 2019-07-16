# -*- coding:utf-8 -*-
import sys
import os
import data.requestData
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getAuth
import enumData.accountTypeEnum
#qa和dev环境的 域名头  body里面的json数据  头文件的鉴权都不一样 所以需要把三个参数提出来写
def getShipperInfo(env_url,path):
    request_url = env_url+ data.requestData.getShipperInfo_request
    if env_url.find("qa") >= 0:
        env = "beta"
    else :
        env = "dev"
    #f = open(path, "rb")
    f = open(path,"r")
    PostJson = json.load(f)
    authJson = PostJson ["auth"]
    bodyJson = PostJson ["body"]
    phone = authJson["telephone"]
    usertype = authJson["userType"]
    auth = utils.getAuth.generateAuthApi(phone, usertype, env)
    headers = {}
    headers["Content-Type"] = 'application/json'
    headers["Authorization"] = str(auth)
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    print (response)
    return response

def login(env_url,telephone,account_type):
    request_url = env_url + data.requestData.login_request
    headers = {}
    headers["Content-Type"] = 'application/json'
    if(account_type == enumData.accountTypeEnum.accountType.shipper.value):
        headers["client-info"] = data.requestData.shipper_client
    elif((account_type == enumData.accountTypeEnum.accountType.driver.value)):
        headers["client-info"] = data.requestData.driver_client
    else:
        print("输入的account_type有误，请检查！")
    bodyJson = {"cmToken": "", "code": "1234", "telephone": telephone}
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson


def shipperAuthenticate(env_url,path,telephone,idCard):
    request_url = env_url + data.requestData.shipperAuthenticate_request
    if env_url.find("qa") >= 0:
        env = "beta"
    else:
        env = "dev"
    f = open(path, "r")
    auth = utils.getAuth.generateAuthApi(telephone, enumData.accountTypeEnum.accountType.shipper.value, env)
    headers = {}
    headers["Content-Type"] = 'application/json'
    headers["Authorization"] = str(auth)
    bodyJson = json.load(f)
    bodyJson['idCard'] = idCard
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson


def shipperUploadChangedInfoNew(env_url,path,telephone):
    request_url = env_url + data.requestData.shipperUploadChangedInfoNew_request
    if env_url.find("qa") >= 0:
        env = "beta"
    else:
        env = "dev"
    f = open(path, "r")
    auth = utils.getAuth.generateAuthApi(telephone, enumData.accountTypeEnum.accountType.shipper.value, env)
    headers = {}
    headers["Content-Type"] = 'application/json'
    headers["Authorization"] = str(auth)
    headers['client-info'] = data.requestData.shipper_client
    bodyJson = json.load(f)
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson
#司机端提交认证资料
def driverAuthenticate(env_url,path,telephone,idCard):
    request_url = env_url + data.requestData.driverAuthenticate_request
    if env_url.find("qa") >= 0:
        env = "beta"
    else:
        env = "dev"
    f = open(path, "r")
    auth = utils.getAuth.generateAuthApi(telephone, enumData.accountTypeEnum.accountType.driver.value, env)
    headers = {}
    headers["Content-Type"] = 'application/json'
    headers["Authorization"] = str(auth)
    headers['client-info'] = data.requestData.driver_client
    bodyJson = json.load(f)
    bodyJson['idCard'] = idCard
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson

#司机端提交行驶证
def submitVehicleLicense(env_url,path,telephone):
    request_url = env_url + data.requestData.submitVehicleLicense_request
    if env_url.find("qa") >= 0:
        env = "beta"
    else:
        env = "dev"
    f = open(path, "r")
    auth = utils.getAuth.generateAuthApi(telephone, enumData.accountTypeEnum.accountType.driver.value, env)
    headers = {}
    headers["Content-Type"] = 'application/json'
    headers["Authorization"] = str(auth)
    headers['client-info'] = data.requestData.driver_client
    bodyJson = json.load(f)
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson







if __name__ == '__main__':
    env_url = data.requestData.qa
    #path = "../data/getShipperInfo_dev.json"
    #getShipperInfo(env_url,path)
    #path = '../data/shipperAuthenticate_qa.json'
    #telephone = '15668000004'
    #idCard = "330127198909306711"
    #login("http://qa.ymm56.com", 15668000008, 2)
    path = '../data/submitVehicleLicense_qa.json'
    telephone = 13037815083
    submitVehicleLicense(env_url, path, telephone)