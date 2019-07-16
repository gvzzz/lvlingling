import base.userCenter_app
import base.admin_app
from tools import auto_create
from data import requestData
import unittest
class auto_registe_driver_qa_Test(unittest.TestCase):
    def test_auto_registe_driver(self):
        obj = auto_create.auto_create_number()
        telephone = obj.phoneCreate()
        # 第一步用手机号注册新的账户
        #telephone = '13037815083'
        env_url_c = requestData.qa
        print("==============================自动化司机的手机========================================" + telephone)
        loginResponseJson = base.userCenter_app.login(env_url_c, telephone, 1)
        self.assertEqual(loginResponseJson['result'], 1, "注册登录接口出了问题")
        account_id = loginResponseJson['info']['profileInfo']['userId']

        # 第二步开始走提交司机的资料
        driverAuthenticate_path = '../data/driverAuthenticate_qa.json'
        idCard = obj.idCardCreate()
        driverAuthenticateJson = base.userCenter_app.driverAuthenticate(env_url_c, driverAuthenticate_path, telephone, idCard)
        self.assertEqual(driverAuthenticateJson['result'], 1, "司机认证资料的提交接口出了问题")

        # 第三步开始走司机审核通过的流程
        env_url_b = requestData.qa_background
        shipper_approve_path = "../data/driverauditpass_qa.json"
        driverauditpassJson = base.admin_app.driverauditpass(env_url_b, shipper_approve_path, account_id, telephone)
        self.assertEqual(driverauditpassJson['result'], 1, "司机后台头像审核通过接口出了问题")

        # 第四步开始行驶证信息 并且AI审核通过
        submitVehicleLicense_path = '../data/submitVehicleLicense_qa.json'
        submitVehicleLicenseJson = base.userCenter_app.submitVehicleLicense(env_url_c, submitVehicleLicense_path, telephone)
        self.assertEqual(submitVehicleLicenseJson['result'], 1, "司机提交行驶证信息接口出了问题")



if __name__ == '__main__':
            unittest.main()
