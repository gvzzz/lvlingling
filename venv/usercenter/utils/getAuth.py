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
import base.uc_info_center
import utils.getIpPort
import base.uc_auth_center
import base64



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
    if env.find("beta") >= 0:
        env2 = "qa"
    else :
        env2 = "dev"
    if (auth is None):
        #如果拿到的auth头为null那么调auth-center的获取已经登录的账户的token，只有经登录过才能拿得到（wrench接口是从登录接口里面拿的）
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-info-center", str(env2))
        account_id = base.uc_info_center.getAccountInfoByMobile(http_host,str(phone))
        http_host = utils.getIpPort.get_pigon_ip_and_port("uc-auth-center", str(env2))
        token = base.uc_auth_center.getAuthTokenByUserId(http_host,str(account_id),'YMM')
        a64CookieStr = 'u_' + str(account_id) + ':' + token
        return 'Basic ' + str(base64.b64encode(a64CookieStr.encode('utf-8')), 'utf-8')
    return auth

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
    generateAuthApi(15660000000, 2, 'beta')
    #path = "../data/sso_qa.json"
    #getSso(path,"qa")


