# -*- coding:utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getIpPort
#这是pigeon接口需要去机器的host域名，还有parameter1是方法的参数
def getTelephone(http_host,parameter1):
    url = http_host + "/invoke.json?validate=true&direct=false&token=undefined&url=http%3A%2F%2Fcom.ymm.services%2Fucs%2FcmLoginAuthService&method=getTelephone&parameterTypes%5B%5D=java.lang.String" + "&group=&parameters%5B%5D=" + parameter1
    headers = {}
    response = utils.httpUtil.Get(url,headers)
    return response

if __name__ == '__main__':
    http_host = utils.getIpPort.get_pigon_ip_and_port("uc-check-service","qa")
    getTelephone(http_host, "18916377820")