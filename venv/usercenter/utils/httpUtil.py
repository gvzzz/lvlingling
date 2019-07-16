# -*- coding:utf-8 -*-
import json
from urllib import request
import urllib.parse
from utils import des_utils
from utils import sso

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



def url_encode(form_data):
        form_data_list = [str(key) + '=' + str(value) for key, value in form_data.items()]
        encode_url = '&'.join(form_data_list)
        return encode_url


 # 采用V1类型加密
def encrypt(post_url, post_param=None, sessionId=-1, token=""):
        '''if not (post_url and post_param):
            raise Exception(u"请传入post请求url和post请求参数")

        if not isinstance(post_param, dict):
            raise Exception(u"传入的post请求参数不为字典，参数格式非法！")'''
        if (len(post_param)!= 0):
                #url_encode = url_encode(post_param)
                encode_data = post_url.strip() + "?" + url_encode(post_param)
        elif (len(post_param)== 0):
                encode_data = post_url
        print("====encode_data=====加密前入参"+encode_data)
        encrypt_data = des_utils.DesUtil.encrypt_data(encode_data, sessionId, token)
        print("====encrypt_data====加密后入参"+encrypt_data)
        return encrypt_data


 # 采用V1类型解密
def decrypt(encrypt_data, token_st=None):
        return des_utils.DesUtil.decrypt_data(encrypt_data, token_st)


def hcbPostForm(dispatch_url, api_url, form_data, token=None):
        # 如果有token传入，将token加入加密，否则使用默认token
        if token:
                encrypt_data = encrypt(api_url, form_data, token.get('sid'), token.get('st'))
        else:
                encrypt_data = encrypt(api_url, form_data)
        post_param = {"content": encrypt_data}
        r = PostForm(dispatch_url, {}, post_param)
        print("完整的请求url是：%s" % dispatch_url + api_url)
        c = r.decode(encoding='utf-8')  # 将byte转string
        print("===============c" + c)
        decrypt_data_dict = decrypt(c)
        print("============decrypt_data_dict" + decrypt_data_dict)
        json.loads(decrypt_data_dict)
        try:
                return json.loads(decrypt_data_dict)
        except Exception as e:
                print('ERROR exception caught ===>' + str(e))
                print(decrypt_data_dict)


if __name__ == '__main__':
        #url = "http://docker-beidou.ymmoa.com/internal/api/get_service_port/?name=uc-check-service"
        #headers ={}
        #Get(url,headers)
        '''headers={}
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

        url = 'http://dev-lion.ymmoa.com/lion/config/saveDefaultValueAjax.vhtml'


        headers["Cookie"] = "qa_passport=HVCPSJBe4ZIDA5Jdu1O59-iCGuI5dRUt8C_Yof2Z3MjneXBlkC6xtzeVBK3yDiapOHwplKvT0K2XpIZ97XN00AWxe6gsWXRscUA1dW4ujuOSvT8Mapya6IBa770ssgzuv2yVpxAPH3Bw6rB8ep0FSPlXd8SpK9WFPWbdhJ2Jfks; dev_passport=AT8L9xP4LsiHAEUbjPbFjZ_wSLflhfL3NxvmzyVDjgJB3mm-KNaRMX0o9Avo34EDcV3YT8R2etBqEXx8jHS0vm3080qIQclZ4dZzrDh3Rt2L3YYMc2I-Kkqn0p1Y2RS4dckSSE0_MJZwB0TSKal8W4vqVIa9ccTo3hKo5u3rIgs"
        headers["Content-Type"] = 'application/x-www-form-urlencoded'
        data = {}
        data["configId"] = 17439
        data["envIds"] = 3
        data["envIds"] = 4
        data["trim"] = True
        data["value"] = False
        data["type"] = 30
        PostForm(url, headers, data)'''

        dispatch_url= 'http://ucenter.dev-ag.56qq.com/mobile/vehicle/auth-info'
        api_url =""
        obj = sso.Sso()
        form_data = {
        "client": "Android_v7.1",
        "version": "5.14.0",
        "domainId": 1,
        "appClientId": 107,
        "mobile": 13521100003,
        "code": 8888,
        "codeType" : "VERIFICATION_CODE",
        "dfp": "ee3b66e1-9d09-4793-bfa2-f0ed16300b22"

}
        response_dict = obj.post("http://sso.dev-ag.56qq.com/v1.1/mobile/dispatch.do","/common/app/mobile/login-by-code.do", form_data, None)
        #response_dict = obj.post("http://sso.qa-sh.56qq.com/v1.1/mobile/dispatch.do", "/common/app/mobile/login-by-code.do", form_data,None)
        print(response_dict)
        token = {'sid': response_dict['content']['id'], 'st': response_dict['content']['token']}
        form_data1 = {
                "st": token.get("st"),
                "sid": token.get("sid")
        }
        #hcbPostForm("http://ucenter.qa-sh.56qq.com/v1.1/mobile/dispatch.do", "/mobile/vehicle/auth-info", form_data1, None)
        #hcbPostForm("http://ucenter.dev-ag.56qq.com/v1.1/mobile/dispatch.do", "/mobile/vehicle/auth-info", form_data1,None)
        hcbPostForm("http://192.168.206.110:8080/v1.1/mobile/dispatch.do", "/mobile/vehicle/auth-info", form_data1,None)
        headers = {}
        headers["x-ag-decryption"] = 'true'
        PostForm('http://192.168.206.110:8080/mobile/vehicle/auth-info',headers,form_data1)











