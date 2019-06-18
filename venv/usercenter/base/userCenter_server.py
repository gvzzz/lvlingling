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
def simple_user_info(env_url,path,i):
    request_url = env_url+"/server/simple-user-info"
    f = open(path,"r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson ["requestbodys"]
    bodyJson =bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url,headers,bodyJson)
    return response

def consignor_get(env_url,path,i):
    request_url = env_url + "/server/user/consignor/get"
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#这个方法有点问题入参是网关鉴权拿到的，对C端
def vehicle_auth_info(env_url,path,i):
    request_url = env_url + "/mobile/vehicle/auth-info"
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#还未调好 对C端
def driver_get(env_url,path,i):
    request_url = env_url + "/mobile/driver/get"
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#这个接口的返回值有问题
def server_driver_get(env_url,path,i):
    request_url = env_url + "/server/driver/get"
    print("++++++++++++"+request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23367878,这个接口开发文档写的很奇怪
def users_basic_info(env_url,path,i):
    request_url = env_url + "/server/query/users-basic-info"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23376429
def get_by_mobiles(env_url,path,i):
    request_url = env_url + "/server/user/driver/get-by-mobiles"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response


if __name__ == '__main__':
    #path = "../hcbdata/simple_user_info.json"
    #simple_user_info("http://ucenter.dev-ag.56qq.com",path,0)
    #path = "../hcbdata/consignor_get.json"
    #consignor_get ("http://ucenter.dev-ag.56qq.com",path,0)
    #path = "../hcbdata/server_driver_get.json"
    #server_driver_get("http://ucenter.dev-ag.56qq.com",path,0)
    #path = '../hcbdata/users_basic_info.json'
    #users_basic_info("http://ucenter.dev-ag.56qq.com", path, 3)
    #path = '../hcbdata/users_basic_info.json'
    #users_basic_info("http://ucenter.dev-ag.56qq.com", path, 3)
    path = '../hcbdata/get_by_mobiles.json'
    get_by_mobiles("http://ucenter.dev-ag.56qq.com", path, 0)



