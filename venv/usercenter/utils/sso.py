#coding=utf-8
import os
import sys
import json

from utils import httpUtil
from utils import des_utils



class Sso():
    #def __init__(self):
        #self.server_api = ServerApis
        # self.host = QA.HOST_UC
        #self.host = Shanghai.HOST_UC

    def url_encode(self, form_data):
        form_data_list = [str(key) + '=' + str(value) for key, value in form_data.items()]
        encode_url = '&'.join(form_data_list)
        return encode_url

    # 采用V1类型加密
    def encrypt(self, post_url, post_param=None, sessionId=-1, token=""):
        if not (post_url and post_param):
            raise Exception(u"请传入post请求url和post请求参数")

        if not isinstance(post_param, dict):
            raise Exception(u"传入的post请求参数不为字典，参数格式非法！")
        url_encode = self.url_encode(post_param)
        encode_data = post_url.strip() + "?" + url_encode
        print(encode_data)
        encrypt_data = des_utils.DesUtil.encrypt_data(encode_data, sessionId, token)
        return encrypt_data

    # 采用V1类型解密
    def decrypt(self, encrypt_data, token_st=None):
        return des_utils.DesUtil.decrypt_data(encrypt_data, token_st)



    def post(self, dispatch_url, api_url, form_data, token=None):
        # 如果有token传入，将token加入加密，否则使用默认token
        if token:
            encrypt_data = self.encrypt(api_url, form_data, token.get('sid'), token.get('st'))
        else:
            encrypt_data = self.encrypt(api_url, form_data)
        post_param = {"content": encrypt_data}
        #r = requests.post(dispatch_url, data=post_param)
        r = httpUtil.PostForm(dispatch_url,{},post_param)
        print("完整的请求url是：%s" % dispatch_url+api_url)
        #print("=======> sso response status code: {}".format(r.status_code))
        # 如果传入了token则解密需要传入st
        c = r.decode(encoding='utf-8')   #将byte转string
        print("===============c"+c)
        decrypt_data_dict = self.decrypt(c)
        print("============decrypt_data_dict"+decrypt_data_dict)
        json.loads(decrypt_data_dict)
        '''if token:
            decrypt_data_dict = self.decrypt(r.text, token.get('st'))
        else:
            decrypt_data_dict = self.decrypt(r.text)
        print(decrypt_data_dict)'''

        try:
            return json.loads(decrypt_data_dict)
        except Exception as e:
            print('ERROR exception caught ===>' + str(e))
            print(decrypt_data_dict)


if __name__ == '__main__':
    obj = Sso()
    '''form_data={
        "client": "Android_v7.1",
        "version":"5.14.0",
        "domainId":1,
        "appClientId":103,
        "username":"CuST3HLO2lRqO",
        "password":123456,
        "dfp":"ee3b66e1-9d09-4793-bfa2-f0ed16300b22"
    }
    #obj.post("http://sso.qa-sh.56qq.com/v1.1/mobile/dispatch.do", "/common/login.do", form_data, token=None)
    obj.post("http://sso.dev-ag.56qq.com/v1.1/mobile/dispatch.do", "/common/login.do", form_data, token=None)'''
    '''form_data = {
        "client": "Android_v7.1",
        "version": "5.14.0",
        "domainId": 1,
        "appClientId": 103,
        "mobile": 15660000300,
        "code": 8888,
        "codeType" : "VERIFICATION_CODE",
        "dfp": "ee3b66e1-9d09-4793-bfa2-f0ed16300b22"
    }
    #obj.post("http://sso.qa-sh.56qq.com/v1.1/mobile/dispatch.do", "/common/app/mobile/login-by-code.do", form_data, token=None)
    obj.post("http://sso.dev-ag.56qq.com/v1.1/mobile/dispatch.do", "/common/app/mobile/login-by-code.do", form_data, token=None)'''
    form_data = {
        "st": "0092773E0A6BFCC7",
              "sid": "2165325817"
    }
