# -*- coding:utf-8 -*-
#从wrench平台获取auth头 参考林放的接口
import sys
print(sys.path)
import os
#获取项目路径下的目录
os.chdir('../utils')
#打印出项目路径下的目录
for file in os.listdir(os.getcwd()):
    sys.path.append('../utils')
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
    #取到auth值为空的话进行10次尝试
    for i in range(10) :
        response = httpUtil.Post(request_url, headers, data)
        auth = json.loads(response)['auth']
        print(auth)
        if(auth is not None):
            break;
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
    #generateAuthApi(15660000090, 2, 'dev')
    generateAuthApi(15678525356, 1, 'beta')
    #path = "../data/sso_qa.json"
    #getSso(path,"qa")


