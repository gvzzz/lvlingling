# coding=utf-8

from utils import sso



'''class MobileGetUserInfo():
    def __init__(self):
        self.sso =
        self.get_token =
        self.sso_dispatch_url =
        # self.sso_dispatch_url = QA.HOST_SSO + QA.DISPATCH_V1
        self.uc_dispatch_url ='http://sso.qa-sh.56qq.com/v1.1/mobile/dispatch.do/common/login.do?'
"

    def run(self, userId, domainId='1', token=None):
        form_data = {
            "userId": userId,
            "domainId": domainId,
            'st': token.get('st'),
            'sid': token.get('sid')
        }
        result = self.sso.post(self.uc_dispatch_url, MobileApis.MOBILE_USER_INFO, form_data)
        print("请求的结果是: %s" %result)
       # print("请求的SSO host是：%s" % Guiyang.HOST_SSO)


if __name__ == '__main__':
    obj = MobileGetUserInfo()
    #token = obj.get_token.getDriverToken("Dp2mXo5BTHOeo", "123456")
    #print(token)
    obj.run('1155499', token=token)'''
