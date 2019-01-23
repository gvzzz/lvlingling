# -*- coding:utf-8 -*-
import sys
import failCrawling
import xlwt
import datetime


#获取当前的时间，采用第二天早上去拉取第一天的结果
def writeWiki(joblist,beginTime,endTime,wikiName):
    joblistQa = []
    joblistDev = []
    strQa = ''
    strDev = ''
    for i in range(len(joblist)):
        if joblist[i].find("qa") >= 0:
            joblistQa.append(joblist[i])
            failReson = failCrawling.getRssFailedReson(joblist[i], beginTime, endTime)
            PassRate_percent = failCrawling.getPassRate(joblist[i], beginTime, endTime)
            strQa = strQa + '<tr><td class="confluenceTd"><span style="color: #000000;">'+joblist[i]+'</span></td><td class="confluenceTd">'+failReson+'</td><td class="confluenceTd">'+PassRate_percent+'</td></tr>'
            print("服务名" + joblist[i] + "失败原因" + failReson + "每日稳定性" + PassRate_percent)
        else:
            joblistDev.append(joblist[i])
            failReson = failCrawling.getRssFailedReson(joblist[i], beginTime, endTime)
            PassRate_percent = failCrawling.getPassRate(joblist[i], beginTime, endTime)
            print("服务名"+joblist[i]+"失败原因"+failReson+"每日稳定性"+PassRate_percent)
            strDev = strDev + '<tr><td class="confluenceTd"><span style="color: #000000;">' + joblist[
                i] + '</span></td><td class="confluenceTd">' + failReson + '</td><td class="confluenceTd">' + PassRate_percent + '</td></tr>'
    str = '<table class="confluenceTable"><thead><tr><th class="confluenceTh"><div class="tablesorter-header-inner">qa环境服务</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">失败原因</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">运行成功率</div></th></tr></thead><tbody>'\
              +strQa+'</tbody></table><p>&nbsp;</p><p>&nbsp;</p>' \
              + '<table class="confluenceTable"><thead><tr><th class="confluenceTh"><div class="tablesorter-header-inner">dev环境服务</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">失败原因</div></th><th class="confluenceTh"><div class="tablesorter-header-inner">运行成功率</div></th></tr></thead><tbody>'\
              +strDev+'</tbody></table><p><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p><p>&nbsp;</p><p>&nbsp;</p>'

    url = 'http://wiki.ymmoa.com/pages/doeditpage.action?pageId='+ failCrawling.getPageId(wikiName)  #按照wiki的名字查找出id然后拼成post的url请求
    #utils.httpUtil.PostForm(url,header,body)

#写入excel
def writeExcelDaliy(joblist,beginTime,endTime):
    myWorkbook = xlwt.Workbook()   #创建Excel工作薄
    mySheet = myWorkbook.add_sheet('A Test Sheet',cell_overwrite_ok= True) #添加Excel工作表,可更改
    myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 数据格式
    mySheet.write(0,0,beginTime+'服务可用性')  #A1
    mySheet.write(1, 0, '服务名')  #A2
    mySheet.write(1,1,'失败原因')  #B2
    mySheet.write(1,2,'成功率')    #C2
    for i in range(len(joblist)):
        failReson = failCrawling.getRssFailedReson(joblist[i], beginTime, endTime)
        PassRate_percent = failCrawling.getPassRate(joblist[i], beginTime, endTime)
        mySheet.write(2+i, 0, joblist[i])  #写入A3，数值等于joblist[i] 就是服务名
        mySheet.write(2+i, 1, failReson)  # 写入B3，数值等于失败原因
        mySheet.write(2+i, 2, PassRate_percent) #写入C3，数值等于成功率
        print("服务名" + joblist[i] + "失败原因" + failReson + "每日稳定性" + PassRate_percent)
    myWorkbook.save(beginTime+'.xls')






if __name__ == '__main__':
    joblist = []
    joblist.append('qa_doorkeeper_center_serviceablity')
    joblist.append('qa_uc_check_service_serviceablity')
    joblist.append('qa_uc_auth_center_serviceablity')
    joblist.append('qa_uc_info_center_serviceablity')
    joblist.append('qa_user_reference_service_serviceablity')
    joblist.append('qa_useraudit_service_serviceablity')
    joblist.append('qa_userCenter_app_serviceablity')
    joblist.append('qa_authenticate_service_serviceablity')
    joblist.append('qa_reference_app_serviceablity')
    joblist.append('qa_admin_app_serviceablity')
    joblist.append('qa_info_app_serviceablity')
    joblist.append('qa_userCenter4x_service_serviceablity')
    joblist.append('qa_new_boss_serviceablity')
    joblist.append('qa_verifycode_service_serviceablity')

    joblist.append('dev_doorkeeper_center_serviceablity')
    joblist.append('dev_uc_check_service_serviceablity')
    joblist.append('dev_uc_auth_center_serviceablity')
    joblist.append('dev_uc_info_center_serviceablity')
    joblist.append('dev_user_reference_service_serviceablity')
    joblist.append('dev_useraudit_service_serviceablity')
    joblist.append('dev_userCenter_app_serviceablity')
    joblist.append('dev_authenticate_service_serviceablity')
    joblist.append('dev_reference_app_serviceablity')
    joblist.append('dev_admin_app_serviceablity')
    joblist.append('dev_info_app_serviceablity')
    joblist.append('dev_userCenter4x_service_serviceablity')
    joblist.append('dev_new_boss_serviceablity')
    joblist.append('dev_verifycode_service_serviceablity')
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    writeExcelDaliy(joblist,yesterday, today)

