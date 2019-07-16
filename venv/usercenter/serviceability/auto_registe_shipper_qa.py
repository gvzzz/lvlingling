from base import userCenter_app
from base import admin_app
from tools import auto_create
from data import requestData
import unittest
class auto_registe_shipper_qa_Test(unittest.TestCase):
    def test_auto_registe_shipper(self):
        obj = auto_create.auto_create_number()
        telephone = obj.phoneCreate()
        #第一步用手机号注册新的账户
        #telephone = '15668000004'
        env_url_c = requestData.qa
        print("====================自动化货主的手机====================="+telephone)
        loginResponseJson = userCenter_app.login(env_url_c, telephone, 2)
        self.assertEqual(loginResponseJson['result'], 1, "注册登录接口出了问题")
        account_id  = loginResponseJson['info']['profileInfo']['userId']
        #第二步开始走提交货主的资料
        shipperAuthenticate_path = '../data/shipperAuthenticate_qa.json'
        idCard = obj.idCardCreate()
        shipperAuthenticateJson = userCenter_app.shipperAuthenticate(env_url_c, shipperAuthenticate_path, telephone, idCard)
        self.assertEqual(shipperAuthenticateJson['result'], 1, "货主认证资料提交接口出了问题")
        #第三步开始走货主审核通过的流程
        env_url_b = requestData.qa_background
        shipper_approve_path = "../data/shipper_approve_qa.json"
        shipper_approveJson = admin_app.shipper_approve(env_url_b, shipper_approve_path, account_id)
        self.assertEqual(shipper_approveJson['result'], 1, "货主新头像通过接口出了问题")
        #第四步开始提交公司资料
        shipperUploadChangedInfoNew_path = '../data/shipperUploadChangedInfoNew_qa.json'
        shipperUploadChangedInfoNewJson = userCenter_app.shipperUploadChangedInfoNew(env_url_c,shipperUploadChangedInfoNew_path,telephone)
        print(shipperUploadChangedInfoNewJson['result'])
        self.assertEqual(shipperUploadChangedInfoNewJson['result'], 1, "货主公司资料提交接口出了问题")
        # 第五步查询需要资料审核的batchId的信息
        getShipperChanged_path = '../data/getShipperChanged_qa.json'
        batchId = admin_app.getShipperChanged(env_url_b, getShipperChanged_path, telephone)
        #第六步货主资料审核通过
        auditUserChanged_path = "../data/auditUserChanged_qa.json"
        auditUserChangedJson = admin_app.auditUserChanged(env_url_b, auditUserChanged_path, account_id, telephone, batchId)
        self.assertEqual(auditUserChangedJson['result'], 1, "货主公司资料审核通过接口出了问题")







if __name__ == '__main__':
    unittest.main()



