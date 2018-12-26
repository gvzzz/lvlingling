# -*- coding:utf-8 -*-
import sys

import os
import data.requestData
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil


#爬取jenkins的失败原因记录
def getRssFailed(jobName):
    request_url = "http://192.168.198.141:8080/jenkins/job/"+jobName+"/rssFailed"
    headers = {}
    response = utils.httpUtil.Get(request_url, headers)
    return response



if __name__ == '__main__':
    getRssFailed("runAllshark")


