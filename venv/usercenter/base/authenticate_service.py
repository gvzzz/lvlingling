# -*- coding:utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getIpPort
import urllib
#这是pigeon接口需要去机器的host域名，还有parameter1是方法的参数   未调好
def findByCertifyIDAndCertifyNameV2(http_host,parameter1,parameter2,parameter3):
    parameter2_encode =  urllib.quote(parameter2)
    url = http_host + "/invoke.json?validate=true&direct=false&token=undefined&url=http%3A%2F%2Fcom.ymm.services%2FauthenticateServiceWithMultiRoles_2.0.0&method=findByCertifyIDAndCertifyNameV2&parameterTypes%5B%5D=java.lang.String&parameterTypes%5B%5D=java.lang.String&parameterTypes%5B%5D=com.ymm.userCenter4.api.enums.UserType"+"&parameters%5B%5D=" + parameter1 + "&parameters%5B%5D=" + parameter2_encode + "&parameters%5B%5D=" + parameter3
    print url
    headers = {}
    response = utils.httpUtil.Get(url,headers)
    return response

if __name__ == '__main__':
    #http_host = utils.getIpPort.get_pigon_ip_and_port("authenticate-service","qa")
    #findByCertifyIDAndCertifyNameV2(http_host, "361021198905222996","李孟柱","1")
    http_host = utils.getIpPort.get_pigon_ip_and_port("authenticate-service", "dev")
    findByCertifyIDAndCertifyNameV2(http_host, "361021198905222996", "李孟柱", "1")