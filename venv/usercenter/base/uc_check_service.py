# -*- coding:utf-8 -*-
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import utils.getIpPort
#这是pigeon接口需要去机器的host域名，还有parameter1是方法的参数

def getOcrSupplierBillCounts(http_host,parameter1,parameter2):
    url = http_host + "/invoke.json?validate=true&direct=true&token=undefined&group=&url=http%3A%2F%2Fcom.ymm.services%2Fucs%2FucCheckForICService&method=getOcrSupplierBillCounts&parameterTypes%5B%5D=java.util.Date&parameterTypes%5B%5D=java.util.Date" + "&parameters%5B%5D=1540555246000&parameters%5B%5D=1540555246000"
    headers = {}
    response = utils.httpUtil.Get(url, headers)
    return response

if __name__ == '__main__':
    http_host = utils.getIpPort.get_pigon_ip_and_port("uc-check-service","dev")
    #getTelephone(http_host, "18916377820")
    getOcrSupplierBillCounts(http_host,'','')