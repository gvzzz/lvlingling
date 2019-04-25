#coding:utf-8
report_url = "http://shark.ymmoa.com/api/show/status?ref_id=326&report_type=project&"#查报告的url
report_header = {"ymmoa_user": '{%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}'} #查报告的header


report_url_service = "http://shark.ymmoa.com/#/report/report?report_type=service"  #按照服务维度查询报告的url
result_url_service = "http://shark.ymmoa.com/api/show/status?report_type=service" #按照服务维度查询报告的url


trigger_url = "http://shark.ymmoa.com/api/run/runSuiteASync"   #触发构建的url
trigger_header = {"Content-Type": 'application/json', "ymmoa_user": '{%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}'} #触发构建的header
queryTestId_url = "http://shark.ymmoa.com/api/case/TestSuite" #根据TestSuite_id查询test_Id的url
queryTestId_header  = {"Content-Type": 'application/json', "ymmoa_user": '{%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}'}  #查询testId的header

runGroupASync_url = "http://shark.ymmoa.com/api/run/runGroupASync" #一个组去触发构建
runGroupASync_header = {"Content-Type": 'application/json', "ymmoa_user": '{%22name%22:%22%E6%9D%8E%E4%BD%B3%E7%BE%8E%22%2C%22avatarUrl%22:%22%22%2C%22departmentName%22:%22%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86%E4%B8%AD%E5%BF%83%22%2C%22id%22:10236%2C%22jobNumber%22:%22Y0010236%22}'}
runGroupASync_postJson = {"project_id": 326, "env_id": 327, "suite_id": None}



#test_suite_id

userCenter4_service_test_suite_id = 392
uc_info_center_test_suite_id = 1094
new_boss_test_suit_id = 393
ymm_admin_app_test_suite_id = 401

truck_service_test_suite_id = 0
uc_check_service_test_suite_id = 809
ymm_info_app_test_suite_id = 406

uc_doorkeeper_center_test_suite_id = 810
reference_service_test_suit_id = 433
ymm_reference_app_test_suite_id = 438
agreement_service_test_suite_id = 1554
uc_agreement_app = 0

ymm_userCenter_app_test_suite_id =512
useraudit_service_test_suite_id = 830
uc_auth_center_test_suite_id = 1373


authenticate_service_test_suite_id = 497




#服务的url
qa = "http://qa.ymm56.com"
dev = "http://dev.ymm56.com"
#new_boss
getuserstatus_request = "/new_boss/users/getuserstatus"
getuserstatus_header_qa= {"Content-Type": 'application/json',"Authorization":"Basic YV83MDo0OWRjNTJlNmJmMmFiZTVlZjZlMmJiNWIwZjFlZTJkNzY1YjkyMmFlNmNjOGI5NWQzOWRjMDZjMjFjODQ4Zjhj"}
getuserstatus_header_dev={"Content-Type": 'application/json',"Authorization":"Basic YV83MDo0OWRjNTJlNmJmMmFiZTVlZjZlMmJiNWIwZjFlZTJkNzY1YjkyMmFlNmNjOGI5NWQzOWRjMDZjMjFjODQ4Zjhj"}


#userCenter_app
getShipperInfo_request = "/ymm-userCenter-app/authenticate/getShipperInfo"
checkUserStatus_request = "/ymm-userCenter-app/user/checkUserStatus"
getloginverifycode_request = "/ymm-userCenter-app/user/getloginverifycode"
login_request = "/ymm-userCenter-app/account/login"
partnerToken_request = '/ymm-userCenter-app/token/partnerToken'


#info_app
getDriverInfo_request = "/ymm-info-app/authenticate/getDriverInfo"


#reference_app
getCopilotlist_request = "/ymm-reference-app/copilot/list"


#admin_app
findByTelephone_request = "/ymm-admin-app/audit/review/findByTelephone"
getTelephoneAudit_request = "/ymm-admin-app/selfUpdate/getTelephoneAudit"


#clientinfo
shipper_client = "ed9a0bb4fbf0d079ff46659323c7e1e8/shipper/5.17.0.0/android/com.xiwei.logistics.consignor"
driver_client = "ed9a0bb4fbf0d079ff46659323c7e1e8/driver/6.17.0.0/android/com.xiwei.logistics"


#uc_agreement_app
getAllAuthItem_request = '/uc-agreement-app/authorize/getAllAuthItem'

