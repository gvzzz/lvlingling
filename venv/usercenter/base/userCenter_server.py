# -*- coding:utf-8 -*-
import sys
import os
import data.requestData
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
#http://ucenter.dev-ag.56qq.com   i是jsonArry里面取的值 从0开始
def simple_user_info (env_url,path,i):
    request_url = env_url+"/server/simple-user-info"
    f = open(path,"r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson ["requestbodys"]
    bodyJson =bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url,headers,bodyJson)
    return response

if __name__ == '__main__':
    path = "../hcbdata/simple_user_info.json"
    simple_user_info("http://ucenter.dev-ag.56qq.com",path,0)
