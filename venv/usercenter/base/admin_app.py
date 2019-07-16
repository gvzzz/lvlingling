# -*- coding:utf-8 -*-
import sys
import os
from data import requestData
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getAuth


def getPassport(env_url):
    # 调sso获取后台的aq_passport
    if env_url.find("qa") >= 0:
        sso_path = "../data/sso_qa.json"
        passport = utils.getAuth.getSso(sso_path, "qa")
        Cookie = 'qa_passport=' + passport
    else:
        sso_path = "../data/sso_dev.json"
        passport = utils.getAuth.getSso(sso_path, "dev")
        Cookie = 'dev_passport=' + passport
    return Cookie


# qa和dev环境的 域名头  body里面的json数据  头文件的鉴权都不一样 所以需要把三个参数提出来写
def findByTelephone(env_url,path):
    request_url = env_url+ requestData.findByTelephone_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    bodyJson = PostJson["body"]
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    print (response)
    return response


def getTelephoneAudit(env_url,path):
    if env_url.find("qa") >= 0:
        env = "beta"
    else :
        env = "dev"
    request_url = env_url + requestData.getTelephoneAudit_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    bodyJson = PostJson["body"]
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    print (response)
    return response

#货主新--认证审核通过
def shipper_approve(env_url,path,account_id):
    request_url = env_url + requestData.shipper_approve_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    #调sso获取后台的aq_passport
    Cookie = getPassport(env_url)
    headers['Cookie'] = Cookie
    bodyJson = PostJson["body"]
    bodyJson['userId'] = account_id
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson

#货主资料的查询，查出batchId
def getShipperChanged(env_url,path,telephone):
    request_url = env_url + requestData.getShipperChanged_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    # 调sso获取后台的aq_passport
    Cookie = getPassport(env_url)
    headers['Cookie'] = Cookie
    bodyJson = PostJson["body"]
    bodyJson['telephone'] = telephone
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseStr = response.decode('utf8')
    responseJson = json.loads(responseStr)

    try:
        batchId = responseJson['pageList'][0]['batchId']
    except (TypeError,UnboundLocalError) :
        print("后台查询不到货主资料提交审核的数据")
    return batchId


#货主资料审核通过
def auditUserChanged(env_url, path, account_id, telephone, batchId):
    request_url = env_url + requestData.auditUserChanged_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    # 调sso获取后台的aq_passport
    Cookie = getPassport(env_url)
    headers['Cookie'] = Cookie
    bodyJson = PostJson["body"]
    bodyJson['userId'] = account_id
    bodyJson['telephone'] = telephone
    bodyJson['batchId'] = batchId
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson

#司机身份认证通过即头像认证通过
def driverauditpass(env_url, path, account_id, telephone):
    request_url = env_url + requestData.driverauditpass_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    # 调sso获取后台的aq_passport
    Cookie = getPassport(env_url)
    headers['Cookie'] = Cookie
    bodyJson = PostJson["body"]
    bodyJson['userId'] = account_id
    bodyJson['telephone'] = telephone
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    responseJson = json.loads(response)
    return responseJson



if __name__ == '__main__':
    #env_url = "http://qa.ymmoa.com"
    #path = "../data/findByTelephone_qa.json"
    #findByTelephone(env_url,path)
    env_url = "http://dev-boss.ymmoa.com"
    #path = "../data/auditUserChanged_qa.json"
    #shipper_approve(env_url, path, "967933835900115673")
    #auditUserChanged(env_url, path, "967933835900115673", 15668000004)
    path = '../data/driverauditpass_dev.json'
    telephone = 13007798020
    accountId = '965006065496364523'
    driverauditpass(env_url, path, accountId, telephone)