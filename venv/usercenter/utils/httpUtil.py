# -*- coding:utf-8 -*-
import json
from urllib import request


def Post(url,headers,body):
        req = request.Request(url=url, data=json.dumps(body).encode(), method="POST",headers=headers)
        #req = urllib2.Request(url=url, data=json.dumps(body).encode(),headers=headers)
        response = request.urlopen(req).read()
        #try:
                #result = urllib2.urlopen(req)
                #response = result.read()
                #response = urllib.request.urlopen(req).read()
        #except urllib2.HTTPError, e:
                #print e.code
        print(response.decode('utf8'))
        return response



def Get(url,headers):


        req = request.Request(url = url,method="GET",headers=headers)
        response = request.urlopen(req).read()
        #req = urllib2.Request(url = url,headers=headers)
       # try:
                #result = urllib.request.urlopen(req)
                #response = result.read()
        # except urllib2.HTTPError, e:
        #         print ("http请求出错，response 的code码不是200！是")
        #         print (e.code)
        #print(response.decode('utf8'))
        print (response.decode('utf8'))
        return response.decode('utf8')




if __name__ == '__main__':
        url = "http://docker-beidou.ymmoa.com/internal/api/get_service_port/?name=uc-check-service"
        headers ={}
        Get(url,headers)


