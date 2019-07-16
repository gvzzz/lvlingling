# -*- coding:utf-8 -*-
import sys
print(sys.path)
import os
#获取项目路径下的目录
#os.chdir('../utils')
import httpUtil
#envIds dev是3 qa是4
def modifylion(configId,envIds,value,type):
    requesturl = "http://dev-lion.ymmoa.com/lion/config/saveDefaultValueAjax.vhtml"
    headers = {}
    headers[
        "Cookie"] = "dev_passport=gGsRa8m9Bhrf7kNJzOq9hjl0bSWnjG38YDOVjOnesDn7qy9Vu6J892-dou55oBhFWM4-l7uZl1wu6i5OZNlGpLeKGMG8Bw0oIA8RlhcGsW5GCkYE8p-oE1qdleBFYY3LdHfUKktNSlkzZU7R_ubkrlQM-aU5XAYi_7kkypTGcOM"
    headers["Content-Type"] = 'application/x-www-form-urlencoded'
    data = {}
    data["configId"] = configId
    data["envIds"] = envIds
    data["trim"] = True
    data["value"] = value
    data["type"] = type
    httpUtil.PostForm(requesturl, headers, data)

if __name__ == '__main__':
    modifylion(17439, 3, "true", 30)



