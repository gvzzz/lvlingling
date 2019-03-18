# -*- coding:utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getIpPort
#这是pigeon接口需要去机器的host域名，还有parameter1是方法的参数

def getAllAuthItems(http_host,accountId):
    url = http_host + '/invoke.json?validate=true&direct=true&token=undefined&group=&url=http%3A%2F%2Fservice.ymm.com%2Fagreement-service%2FauthorizeService_1.0.0&method=getAllAuthItems&parameterTypes%5B%5D=java.lang.Long'+'&parameters%5B%5D='+accountId
    headers = {}
    response = utils.httpUtil.Get(url, headers)
    return response

if __name__ == '__main__':
    http_host = utils.getIpPort.get_pigon_ip_and_port("agreement-service","dev")
    getAllAuthItems(http_host,'2')