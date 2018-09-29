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
def getuserstatus(env_url,path):
    request_url = env_url+ data.requestData.getuserstatus_request
    if env_url.find("qa") >= 0:
        env = "beta"
    else :
        env = "dev"
    f = open(path, "rb")
    PostJson = json.load(f)
    phone = PostJson["telephone"]
    usertype = PostJson["userType"]
    authJson = utils.getAuth.setenv(phone, usertype, env)
    headers = {}
    headers["Content-Type"] = 'application/json'
    headers["Authorization"] = json.loads(authJson)['auth']
    print headers
    response = utils.httpUtil.Post(request_url, headers, PostJson)
    print response

if __name__ == '__main__':
    env_url = data.requestData.qa
    path = "../data/getuserstatus_qa.json"
    getuserstatus(env_url,path)