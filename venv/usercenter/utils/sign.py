#coding=utf-8
'''
import requests
import base64
from base64 import b64decode
from collections import OrderedDict
from Cryptodome.Hash import SHA
from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5

from . comm_utils import Singleton
from conf.env import Dev


class Sign(Singleton):
    def __init__(self, params, appid=Dev.SERVER_APP_ID, privatekey=Dev.PRIVATE_KEY, key_algorithm='RSA'):
        self.private_key = privatekey
        self.params = params
        self.appid = appid
        self.key_algorithm = key_algorithm

        self.s = requests.Session()
        self.s.headers.update({"x-ap-id": appid})
        self.s.headers.update({"x-sign-type": key_algorithm})
        self.s.headers.update({"x-sign": self.get_sign_data()})

    def sign(self, message):
        digest = SHA.new()
        digest.update(message.encode())
        sign = self.signer.sign(digest)
        signature = base64.b64encode(sign)
        return signature

    def get_sign_data(self):
        key = b64decode(self.private_key)
        rsa_key = RSA.importKey(key)
        self.signer = Signature_pkcs1_v1_5.new(rsa_key)

        # Sign 中会对request中的参数进行排序和sign解密出来的数据进行对比
        # 所以再sign之前必须要对sign的参数进行排序
        ordered_form_data = OrderedDict(sorted(self.params.items(), key=lambda x: x[0]))
        # for key in sorted(params.keys()):
        #     ordered_form_data[key] = params.get(key)

        url_encode = self.url_encode(ordered_form_data)
        print(url_encode)

        sign_privatekey = self.sign(url_encode)
        print(sign_privatekey)
        return sign_privatekey

    def url_encode(self, form_data):
        form_data_list = [key + '=' + str(value) for key, value in form_data.items()]
        encode_url = '&'.join(form_data_list)
        return encode_url

    def post(self, dispatch_url, api_url, form_data=None, json=None, files=None):
        print("sign form data ===> {}".format(form_data))
        print("请求地址为：%s" % dispatch_url+api_url)
        r = self.s.post(dispatch_url + api_url, data=form_data, json=json, files=files)
        print("=======> sign.py response status code: {}".format(r.status_code))
        print("=======> {}".format(r.text))
        self.s.close()
        if r.status_code == 200:
            return r.json()
        return {'status': 'FAILED', 'message': r.content}

    def wallet_post(self, dispatch_url, api_url, form_data=None, json=None, files=None):
        sign_data = {
            "sign": self.get_sign_data(),
            "sign_type": self.key_algorithm,
        }
        form_data.update(sign_data)
        return self.post(dispatch_url, api_url, form_data, json, files)

'''


