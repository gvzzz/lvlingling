# -*- coding:utf-8 -*-
#从wrench平台获取auth头 参考林放的接口

import httpUtil
import json


#获取司机或者货主的auth头
def generateAuthApi(phone,usertype,env):
    request_url = "http://qa.ymmoa.com/wrench/ymm/GenerateAuthApi"
    headers = {"Content-Type": 'application/json'}
    data = {}
    data["telephone"] = phone
    data["usertype"] = usertype
    data["env"] = env
    response = httpUtil.Post(request_url, headers, data)
    print (response)
    return response

#登录sso拿到ymmoa-passport  env填入qa或者dev
def getSso(path,env):
    request_url = "http://" + env + "-sso.ymmoa.com/sso/login"
    headers = {"Content-Type": 'application/json'}
    f = open(path, "r")
    PostJson = json.load(f)
    response = httpUtil.Post(request_url,headers,PostJson)
    responseToJson = json.loads(response)
    ymmoa_passport = responseToJson["result"]["passport"]
    print (ymmoa_passport)


if __name__ == '__main__':
    #generateAuthApi(13423300016,1,"dev")
    path = "../data/sso_qa.json"
    getSso(path,"qa")


