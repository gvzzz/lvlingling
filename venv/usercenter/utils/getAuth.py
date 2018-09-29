# -*- coding:utf-8 -*-
#从wrench平台获取auth头 参考林放的接口

import httpUtil
def setenv(phone,usertype,env):
    request_url = "http://qa.ymmoa.com/wrench/ymm/GenerateAuthApi"
    headers = {"Content-Type": 'application/json'}
    data = {}
    data["telephone"] = phone
    data["usertype"] = usertype
    data["env"] = env
    response = httpUtil.Post(request_url, headers, data)
    return response


if __name__ == '__main__':
    setenv(13057580010,1,"dev")

