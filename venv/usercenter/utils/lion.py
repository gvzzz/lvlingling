# -*- coding:utf-8 -*-
import sys
print(sys.path)
import os
#获取项目路径下的目录
#os.chdir('../utils')
import httpUtil
#envIds dev是3 qa是4
def modifylion(configId,envIds,value,type):
    requesturl = "http://dev-lion.ymmoa.com/lion/config/saveDefaultValueAjax.vhtml"
    headers = {}
    headers[
        "Cookie"] = "qa_passport=DEUGVIkwAvaiO-pkn7-WgHrjjM_t4prsbXfiQADo96MfeFewy2MBZwcSEPAdgLJ3GoH8Sx5N-Hbw_raAcHwSlY75NmX04rj9FXgIeOu0E4GELSNBNaF-UzcDu8OqQ5B4mXoKc-l8VEYt-G4KqeYYGUk27b-KcMfsqq0aSNkNbVA; dev_passport=YA9P31HqCljs7egJ6pIQb3Dsax1xDCEJvnLURztJADh5gIpNUE92yoiFJNA8GNWTM0hg0jO5j7P7iVjstj9Ua0XVdQ4MNrI7PaEO2MCjR7mb92doFPgCLyyv7ca_ppqum-ifOBKrSa4jehkepQQNuIC6gT-f_stViDhMlld4xlI"
    headers["Content-Type"] = 'application/x-www-form-urlencoded'
    data = {}
    data["configId"] = configId
    data["envIds"] = envIds
    data["trim"] = True
    data["value"] = value
    data["type"] = type
    httpUtil.PostForm(requesturl, headers, data)

if __name__ == '__main__':
    modifylion(17439, 3, "true", 30)



