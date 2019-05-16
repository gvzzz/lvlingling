# -*- coding:utf-8 -*-
import sys
import os
import json

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getIpPort
#这是pigeon接口需要去机器的host域名，还有parameter1是方法的参数
def getEnterpriseInfoByAccountId(http_host,account_id):
    url = http_host + "/invoke.json?validate=true&direct=false&token=undefined&group=&url=http%3A%2F%2Fcom.ymm.services%2Fuic%2FenterpriseService&method=getEnterpriseInfoByAccountId&parameterTypes%5B%5D=java.lang.Long"+"&parameters%5B%5D="+account_id
    headers = {}
    response = utils.httpUtil.Get(url,headers)
    return response

def getAccountInfoByMobile(http_host,mobile):
    url = http_host + "/invoke.json?validate=true&direct=false&token=undefined&group=&url=http%3A%2F%2Fcom.ymm.services%2Fuic%2FaccountCenterService&method=getAccountInfoByMobile&parameterTypes%5B%5D=java.lang.Long"+"&parameters%5B%5D="+mobile
    headers = {}
    response = utils.httpUtil.Get(url, headers)
    responseJson = json.loads(response)
    account_id = responseJson['data'][0]['accountId']
    return account_id


if __name__ == '__main__':
    http_host = utils.getIpPort.get_pigon_ip_and_port("uc-info-center","dev")
    #getEnterpriseInfoByAccountId(http_host, "2")
    getAccountInfoByMobile(http_host, '15660000000')