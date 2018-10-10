# -*- coding:utf-8 -*-
#从运维的接口里面获取

import httpUtil
import json


#获取IP和端口号
def get_pigon_ip_and_port(service_name, env):
    request_url = 'http://docker-beidou.ymmoa.com/internal/api/get_service_port/?name={0}'.format(service_name)
    headers = {}
    response = httpUtil.Get(request_url,headers)
    responseToJson = json.loads(response)
    if  env not in ["dev","qa","prd"]:
        print "输入的env环境有误，请重新确认下环境"
    else:
        if env == "dev":
            if responseToJson["machine_dev"]:
                machine_devJsonArray = responseToJson["machine_dev"]
                machine_devJson = machine_devJsonArray[0]
                devIp = machine_devJson["ip"]
                print "http://" + devIp + ':4080'
                return "http://" + devIp + ':4080'
            else:
                print service_name+"不存在dev的机器"
        elif env == "qa":
            if responseToJson["machine_qa"]:
                machine_qaJsonArray = responseToJson["machine_qa"]
                machine_qaJson = machine_qaJsonArray[0]
                qaIp = machine_qaJson["ip"]
                print "http://" + qaIp + ':4080'
                return "http://" +qaIp + ':4080'
            else:
                print service_name + "不存在qa的机器"
        else:
            if responseToJson["machine_prd"]:
                machine_prdJsonArray = responseToJson["machine_prd"]
                machine_prdJson = machine_prdJsonArray[0]
                prdIp = machine_prdJson["ip"]
                print "http://" + prdIp + ':4080'
                return "http://" + prdIp + ':4080'
            else:
                print service_name + "不存在prd的机器"




if __name__ == '__main__':
   #get_pigon_ip_and_port("uc-doorkeeper-center","qa")
   get_pigon_ip_and_port("user-reference-service", "dev")
   #get_pigon_ip_and_port("uc-check-service", "prd")
