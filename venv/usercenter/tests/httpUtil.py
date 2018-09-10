#import urllib.request
import urllib2
import urllib
import json

def Post(url,headers,body):
        #req = urllib.request.Request(url=url, data=json.dumps(body).encode(), method="POST",headers=headers)
        req = urllib2.Request(url=url, data=json.dumps(body).encode(),headers=headers)
        #response = urllib.request.urlopen(req).read()
        response = urllib2.urlopen(req).read()
        print(response.decode('utf8'))
        return response



def Get(url,data,headers):
        new_url = url + "?" + "token="+data
        #req = urllib.request.Request(url = new_url,method="GET",headers=headers)
        #result = urllib.request.urlopen(req)
        req = urllib2.Request(url = new_url,headers=headers)
        result = urllib2.urlopen(req)
        response = result.read()
        print(response.decode('utf8'))
        return response.decode('utf8')




if __name__ == '__main__':
        restUrl = "http://shark.ymmoa.com/api/run/runSuiteASync"
        headers = {"Content-Type": 'application/json',
                   "ymmoa_user": '{%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E5%9F%BA%E7%A1%80%E5%B9%B3%E5%8F%B0%E6%B5%8B%E8%AF%95%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}'
                   }
        PostJson = {"env_id": 327, "token": '', "test_suite_id": "393", "test_case_datas": [{"test_case_id": 541}]}
        Post(restUrl, headers, PostJson)