# -*- coding:utf-8 -*-
import json
from urllib import request
import urllib.parse

#json数据的post
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


#Form类型 数据的post
def PostForm(url,headers,body):
        # 需要使用 urllib.parse.urlencode() 将字典转化为字符串，再使用 bytes() 转为字节流。
        data = bytes(urllib.parse.urlencode(body), encoding='utf8')
        req = request.Request(url=url,data = data, method="POST",headers=headers)
        #response = urllib.request.urlopen(url,data=data,method="POST",headers=headers)


        #try:
                #result = urllib2.urlopen(req)
                #response = result.read()
                #response = urllib.request.urlopen(req).read()
        #except urllib2.HTTPError, e:
                #print e.code
        response = request.urlopen(req).read()
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
        #url = "http://docker-beidou.ymmoa.com/internal/api/get_service_port/?name=uc-check-service"
        #headers ={}
        #Get(url,headers)
        headers={}
        headers["Cookie"] = 'seraph.confluence=17532008%3A76f9efad8b4b9a0f2e792fd106b38fc94f66c95b; confluence-sidebar.width=256.6666666666667; mywork.tab.tasks=false; ymmoa_user={%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E5%9F%BA%E7%A1%80%E5%B9%B3%E5%8F%B0%E6%B5%8B%E8%AF%95%E9%83%A8%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}; ymmoa_passport=bUyhPeUamY2Jrs95ugfqJkSgvGeVa7vhgA6_'
        headers["Content-Type"] = 'application/x-www-form-urlencoded'
        url = 'http://wiki.ymmoa.com/pages/doeditpage.action?pageId=19551062'
        data = {}
        data["title"] = '444444'
        data["wysiwygContent"] = '<table class="confluenceTable"><thead><tr><th class="confluenceTh"><div class="tablesorter-header-inner">qa环境服务</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">失败原因</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">运行成功率</div></th></tr></thead><tbody><tr><td class="confluenceTd"><span style="color: #000000;">qa_doorkeeper_center_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_uc_check_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_uc_auth_center_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_uc_info_center_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_user_reference_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_useraudit_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_userCenter_app_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_authenticate_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">98.33%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_reference_app_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_admin_app_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">96.67%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_info_app_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_userCenter4x_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_new_boss_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">qa_verifycode_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr></tbody></table><p>&nbsp;</p><p>&nbsp;</p><table class="confluenceTable"><thead><tr><th class="confluenceTh"><div class="tablesorter-header-inner">dev环境服务</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">失败原因</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">运行成功率</div></th></tr></thead><tbody><tr><td class="confluenceTd"><span style="color: #000000;">dev_doorkeeper_center_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_uc_check_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_uc_auth_center_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_uc_info_center_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_user_reference_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_useraudit_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_userCenter_app_serviceablity</span></td><td class="confluenceTd">其他原因：git超时  </td><td class="confluenceTd">98.33%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_authenticate_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_reference_app_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_admin_app_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_info_app_serviceablity</span></td><td class="confluenceTd">其他原因：git超时  </td><td class="confluenceTd">98.11%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_userCenter4x_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_new_boss_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">100.00%</td></tr><tr><td class="confluenceTd"><span style="color: #000000;">dev_verifycode_service_serviceablity</span></td><td class="confluenceTd"></td><td class="confluenceTd">88.33%</td></tr></tbody></table><p><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p><p>&nbsp;</p><p>&nbsp;</p>'
        data["notifyWatchers"] = 'true'
        data["confirm"] = 'Save'
        data["draftId"] = '0'
        data["originalVersion"] = '11'
        data["atl_token"] = '8c29bd0ec3d0c8733cd5bb910dd91d2f6dcf226f'
        PostForm(url,headers,data)





