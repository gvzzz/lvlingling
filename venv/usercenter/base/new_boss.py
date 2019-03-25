# -*- coding:utf-8 -*-
import sys
import os
#import data.requestData
from data import requestData
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getAuth

#qa和dev环境的 域名头  body里面的json数据  头文件的鉴权都不一样 所以需要把三个参数提出来写
def getuserstatus(env_url,path):
    request_url = env_url+ requestData.getuserstatus_request
    f = open(path, "rb")
    PostJson = json.load(f)
    header = PostJson["header"]
    body = PostJson["body"]
    response = utils.httpUtil.Post(request_url, header, body)
    responseJson = json.loads(response)
    print(responseJson)
    return responseJson

if __name__ == '__main__':
    env_url = requestData.dev
    path = "../data/getuserstatus_dev.json"
    getuserstatus(env_url,path)