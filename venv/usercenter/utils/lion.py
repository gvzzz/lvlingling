# -*- coding:utf-8 -*-
import sys
print(sys.path)
import os
#获取项目路径下的目录
os.chdir('../utils')
import httpUtil
#envIds dev是3 qa是4
def modifylion(configId,envIds,value,type):
    requesturl = "http://dev-lion.ymmoa.com/lion/config/saveDefaultValueAjax.vhtml"
    headers = {}
    headers[
        "Cookie"] = "qa_passport=HVCPSJBe4ZIDA5Jdu1O59-iCGuI5dRUt8C_Yof2Z3MjneXBlkC6xtzeVBK3yDiapOHwplKvT0K2XpIZ97XN00AWxe6gsWXRscUA1dW4ujuOSvT8Mapya6IBa770ssgzuv2yVpxAPH3Bw6rB8ep0FSPlXd8SpK9WFPWbdhJ2Jfks; dev_passport=AT8L9xP4LsiHAEUbjPbFjZ_wSLflhfL3NxvmzyVDjgJB3mm-KNaRMX0o9Avo34EDcV3YT8R2etBqEXx8jHS0vm3080qIQclZ4dZzrDh3Rt2L3YYMc2I-Kkqn0p1Y2RS4dckSSE0_MJZwB0TSKal8W4vqVIa9ccTo3hKo5u3rIgs"
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



