# -*- coding:utf-8 -*-
import sys
import os
import json.tool
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from dictdiffer import diff, patch, swap, revert
#比较两个json
def json_dif(first,second):
    result = diff(first, second)
    print(list(result))

if __name__ == '__main__':
  first = {'content': {'attachment': 0, 'attachmentFolderUrl': '/dev/2019-06/18/rdPB226al8EscrF3/', 'audited': 1, 'authStatus': 3, 'bindMobile': '15660000400', 'certType': 0, 'cityId': 5411, 'companyContactPerson': '爱新觉罗', 'companyLicenseNo': '', 'countyId': 0, 'createChannel': '2084', 'deleted': 0, 'domainId': 1, 'enabled': 1, 'icNo': '130123199003231518', 'id': 20218941, 'isMaster': True, 'locationId': 5411, 'loginTimes': 0, 'master': True, 'mobile': '15660000400', 'provinceId': 54, 'realNameCertify': 1, 'realname': '爱新觉罗', 'registerTime': 1530201600000, 'source': 4, 'transParkId': '0', 'type': 1, 'unitMobile': '15660000400', 'userId': 20218941, 'username': 'CadSl30haAUWW', 'vipType': 0}, 'status': 'OK'}
  second = {'content': {'address': '', 'attachment': 0, 'attachmentFolderUrl': '/dev/2019-06/18/rdPB226al8EscrF3/', 'audited': 1, 'authStatus': 3, 'bindMobile': '15660000400', 'certType': 0, 'cityId': 5411, 'companyAddress': '', 'companyContactPerson': '爱新觉罗', 'companyLicenseNo': '', 'companyName': '', 'countyId': 0, 'createChannel': '2084', 'deleted': 0, 'domainId': 1, 'enabled': 1, 'icNo': '130123199003231518', 'id': 20218941, 'isMaster': True, 'locationId': 5411, 'loginTimes': 0, 'master': True, 'mobile': '15660000400', 'provinceId': 54, 'realNameCertify': 1, 'realname': '爱新觉罗', 'registerTime': 1530201600000, 'source': 4, 'type': 1, 'unitMobile': '15660000400', 'userId': 20218941, 'username': 'CadSl30haAUWW', 'vipType': 0}, 'status': 'OK'}
  print(type(first))
  json_dif(first,second)



