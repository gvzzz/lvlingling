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

#qa和dev环境的 域名头  body里面的json数据  头文件的鉴权都不一样 所以需要把三个参数提出来写
def findByTelephone(env_url,path):
    request_url = env_url+ data.requestData.findByTelephone_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    bodyJson = PostJson["body"]
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    print response
    return response


def getTelephoneAudit(env_url,path):
    if env_url.find("qa") >= 0:
        env = "beta"
    else :
        env = "dev"
    request_url = env_url + data.requestData.getTelephoneAudit_request
    f = open(path, "r")
    PostJson = json.load(f)
    headers = PostJson["header"]
    bodyJson = PostJson["body"]
    response = utils.httpUtil.Post(request_url, headers, bodyJson)
    print response
    return response

if __name__ == '__main__':
    env_url = "http://qa.ymmoa.com"
    path = "../data/getTelephoneAudit_qa.json"
    getTelephoneAudit(env_url,path)