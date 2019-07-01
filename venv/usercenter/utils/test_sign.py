# coding=utf-8

from utils.sign import Sign
from conf.env import Dev
from api.serverapi import ServerApis


class GetConsignorInfo():
    def __init__(self):
        self.uc_url = Dev.HOST_UC

    def run(self, userId, domainId='1'):
        form_data = {
            "userId": userId,
            "domainId": domainId,
            "showPics": "false"
        }

        self.sign = Sign(form_data, Dev.SERVER_APP_ID, Dev.PRIVATE_KEY)
        self.sign.post(self.uc_url, ServerApis.SERVER_USER_CONSIGNOR_GET, form_data)


if __name__ == '__main__':
    obj = GetConsignorInfo()
    obj.run('2225981')
