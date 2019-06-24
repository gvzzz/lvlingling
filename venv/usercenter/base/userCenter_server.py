# -*- coding:utf-8 -*-
import sys
import os
import data.requestData
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.sso

def sso(form_data):
    obj = utils.sso.Sso()
    response_dict = obj.post("http://sso.qa-sh.56qq.com/v1.1/mobile/dispatch.do", "/common/app/mobile/login-by-code.do",
                             form_data,
                             token=None)
    return  response_dict
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
def vehicle_auth_info(dispatch_url,path,i):
    api_url =  "/mobile/vehicle/auth-info"
    f = open(path, "r")
    PostJson = json.load(f)
    headerJsonArray = PostJson["requsetHeaders"]
    headerJson = headerJsonArray[i]
    #先拿着header调sso
    ssoResponse = sso(headerJson)
    try:
        sid = ssoResponse['content']['id']
        st = ssoResponse['content']['token']
        bodyJson = {}
        bodyJson['sid'] = sid
        bodyJson['st'] = st
        response = utils.httpUtil.hcbPostForm(dispatch_url, api_url, bodyJson)
        return response
    except KeyError:
        print("sso返回值中不含content")


#=
def driver_get(dispatch_url,path,i):
    api_url = "/mobile/driver/get"
    f = open(path, "r")
    PostJson = json.load(f)
    headerJsonArray = PostJson["requsetHeaders"]
    headerJson = headerJsonArray[i]
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    # 先拿着header调sso
    ssoResponse = sso(headerJson)
    try:
        sid = ssoResponse['content']['id']
        st = ssoResponse['content']['token']
        bodyJson['sid'] = sid
        bodyJson['st'] = st
        response = utils.httpUtil.hcbPostForm(dispatch_url, api_url, bodyJson)
        return response
    except KeyError:
        print("sso返回值中不含content")

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23376043
def mobile_exists_toC(dispatch_url,path,i):
    api_url = "/mobile/user/mobile/exists"
    f = open(path, "r")
    PostJson = json.load(f)
    headerJsonArray = PostJson["requsetHeaders"]
    headerJson = headerJsonArray[i]
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    # 先拿着header调sso
    ssoResponse = sso(headerJson)
    try:
        sid = ssoResponse['content']['id']
        st = ssoResponse['content']['token']
        bodyJson['sid'] = sid
        bodyJson['st'] = st
        response = utils.httpUtil.hcbPostForm(dispatch_url, api_url, bodyJson)
        return response
    except KeyError:
        print("sso返回值中不含content")




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

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23368330
def realname(env_url,path,i):
    request_url = env_url + "/server/user/realname"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23375731
def batch_get_by_mobiles(env_url,path,i):
    request_url = env_url + "/server/user/batch-get-by-mobiles"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23376190
def mobile_exists(env_url,path,i):
    request_url = env_url + "/server/mobile/exists"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23376477
def get_with_virtual_info(env_url,path,i):
    request_url = env_url + "/server/user/get-with-virtual-info"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23378616
def get_all_domain(env_url,path,i):
    request_url = env_url + "/server/user/consignor/get-all-domain"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response
#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23378725
def can_register(env_url,path,i):
    request_url = env_url + "/server/user/mobile/can-register"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23383621
def simple_user_info2(env_url,path,i):
    request_url = env_url + "/server/simple-user-info2"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23376909
def get_by_userIds(env_url,path,i):
    request_url = env_url + "/server/user/get-by-userIds"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23370142
def getUserByUserIdAndDomainId(env_url,path,i):
    request_url = env_url + "/server/dubbo/getUserByUserIdAndDomainId"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23375639
def get_by_bindMobiles(env_url,path,i):
    request_url = env_url + "/server/user/get-by-bindMobiles"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23376018
def get_driver_by_userIds(env_url,path,i):
    request_url = env_url + "/server/user/get-driver-by-userIds"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response


#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23376176
def auth_get(env_url,path,i):
    request_url = env_url + "/server/vehicle/auth/get"
    print("++++++++++++" + request_url)
    f = open(path, "r")
    PostJson = json.load(f)
    bodyJsonArry = PostJson["requestbodys"]
    bodyJson = bodyJsonArry[i]
    headers = {}
    response = utils.httpUtil.PostForm(request_url, headers, bodyJson)
    return response

#http://wiki.ymmoa.com/pages/viewpage.action?pageId=23379670
def get_users(env_url,path,i):
    request_url = env_url + "/server/saas/user/get-users"
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
    #path = '../hcbdata/get_users.json'
    #get_users("http://ucenter.dev-ag.56qq.com", path, 0)
    path = '../hcbdata/mobile_exists_toC.json'
    #vehicle_auth_info("http://ucenter.dev-ag.56qq.com/v1.1/mobile/dispatch.do", path, 0)
    mobile_exists_toC("http://ucenter.qa-sh.56qq.com/v1.1/mobile/dispatch.do", path, 0)


