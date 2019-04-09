# -*- coding:utf-8 -*-
#从运维的接口里面获取

import utils.httpUtil
import json

'''
#获取IP和端口号
def get_pigon_ip_and_port(service_name, env):
    request_url = 'http://docker-beidou.ymmoa.com/internal/api/get_service_port/?name={0}'.format(service_name)
    headers = {}
    response = utils.httpUtil.Get(request_url,headers)
    responseToJson = json.loads(response)
    if  env not in ["dev","qa","prd"]:
        print( "输入的env环境有误，请重新确认下环境")
    else:
        if env == "dev":
            if responseToJson["machine_dev"]:
                machine_devJsonArray = responseToJson["machine_dev"]
                machine_devJson = machine_devJsonArray[0]
                devIp = machine_devJson["ip"]
                print ("http://" + devIp + ':4080')
                return "http://" + devIp + ':4080'
            else:
                print (service_name+"不存在dev的机器")
        elif env == "qa":
            if responseToJson["machine_qa"]:
                machine_qaJsonArray = responseToJson["machine_qa"]
                machine_qaJson = machine_qaJsonArray[0]
                qaIp = machine_qaJson["ip"]
                print ("http://" + qaIp + ':4080')
                return "http://" +qaIp + ':4080'
            else:
                print (service_name + "不存在qa的机器")
        else:
            if responseToJson["machine_prd"]:
                machine_prdJsonArray = responseToJson["machine_prd"]
                machine_prdJson = machine_prdJsonArray[0]
                prdIp = machine_prdJson["ip"]
                print ("http://" + prdIp + ':4080')
                return "http://" + prdIp + ':4080'
            else:
                print (service_name + "不存在prd的机器")
'''

#调北斗获取IP的最新的接口
def get_pigon_ip_and_port(serviceName, env):
    request_url = 'http://docker-beidou.ymmoa.com/cloud/api/get_real_ips/?project_name={0}&env={1}'.format(serviceName,env)
    headers = {}
    response = utils.httpUtil.Get(request_url, headers)
    responseToJsonArrry = json.loads(response)
    machine_prdJson = responseToJsonArrry[0]
    if(len(machine_prdJson) != 0):
        ip = machine_prdJson['ip']
        print("http://" + ip + ':4080')
        return "http://" + ip + ':4080'
    else:
        print("机器IP获取失败，请排查北斗接口")
        return None

if __name__ == '__main__':
   #get_pigon_ip_and_port("uc-doorkeeper-center","qa")
   #get_pigon_ip_and_port("ymm-verifycode-service", "qa")
   get_pigon_ip_and_port("uc-check-service", "qa")
