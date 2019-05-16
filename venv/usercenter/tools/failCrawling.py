# -*- coding:utf-8 -*-
import sys
from bs4 import BeautifulSoup
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import utils.httpUtil
import time
import urllib.parse



#爬取jenkins的失败原因记录
def getRssFailedReson(jobName,startTime,endTime):
    s_time = time.mktime(time.strptime(startTime, '%Y-%m-%d'))  #转成时间戳
    e_time = time.mktime(time.strptime(endTime, '%Y-%m-%d'))  #转成时间戳
    request_url = "http://192.168.198.141:8080/jenkins/job/"+jobName+"/rssFailed"
    headers = {}
    response = utils.httpUtil.Get(request_url, headers)
    soup = BeautifulSoup(response, "html.parser")  # 创建soup对象
    tag = soup.find_all('entry')   #找过所有entry的标签的内容
    l = len(soup.find_all('entry'))
    failedReson = ''
    for i in range(l):
        if (tag[i].content != None):
            publishTimeDate = tag[i].updated.string[:10]+' '+ tag[i].updated.string[11:19]   #获取jenkins结果的update的日期
            p_time = time.mktime(time.strptime(publishTimeDate, '%Y-%m-%d %H:%M:%S'))  # 转成时间戳
            if(p_time-s_time >=0)&(e_time-p_time>0):  #去在开始日期和结束日期内的数据结果
                print(tag[i].content.string)
                failedReson = failedReson + tag[i].content.string + '  '  #将问题原因拼接下

    return failedReson


 #爬取job的通过率
def getPassRate(jobName,startTime,endTime):
    s_time = time.mktime(time.strptime(startTime, '%Y-%m-%d'))  # 转成时间戳
    e_time = time.mktime(time.strptime(endTime, '%Y-%m-%d'))  # 转成时间戳
    request_all_url = 'http://192.168.198.141:8080/jenkins/job/'+jobName+'/rssAll'  #所有的job
    request_failed_url = 'http://192.168.198.141:8080/jenkins/job/'+jobName+'/rssFailed'       #失败的job
    headers = {}
    responseAll = utils.httpUtil.Get(request_all_url, headers)
    responseFailed = utils.httpUtil.Get(request_failed_url, headers)
    soupAll = BeautifulSoup(responseAll, "html.parser")  # 创建soup对象
    soupFailed = BeautifulSoup(responseFailed, "html.parser")
    allTag = soupAll.find_all('entry')
    failedTag = soupFailed.find_all('entry')
    allRunTime = 0
    failedRunTime = 0

    for i in range(len(allTag)):
            publishTimeDate = allTag[i].updated.string[:10]  # 获取jenkins结果的update的日期
            p_time = time.mktime(time.strptime(publishTimeDate, '%Y-%m-%d'))  # 转成时间戳
            if (p_time - s_time >= 0) & (e_time - p_time >= 0):  # 去在开始日期和结束日期内的数据结果
                allRunTime = allRunTime +1             #在这个时间端内的运行次数

    for i in range(len(failedTag)):
            publishTimeDate = failedTag[i].updated.string[:10]  # 获取jenkins结果的update的日期
            p_time = time.mktime(time.strptime(publishTimeDate, '%Y-%m-%d'))  # 转成时间戳
            if (p_time - s_time >= 0) & (e_time - p_time >= 0):  # 去在开始日期和结束日期内的数据结果
                failedRunTime = failedRunTime +1             #在这个时间端内的运行次数
    PassRate = (allRunTime-failedRunTime)/allRunTime
    PassRate_percent= "%.2f%%" % (PassRate * 100)
    return  PassRate_percent

#根据wiki的名字去拿pageId
def getPageId(wikiName):
    headers = {}
    urlcode = urllib.parse.quote(wikiName)
    url = "http://wiki.ymmoa.com/display/rdTeam/"+ urlcode
    headers["Cookie"] = 'seraph.confluence=17532008%3A76f9efad8b4b9a0f2e792fd106b38fc94f66c95b; confluence-sidebar.width=256.6666666666667; mywork.tab.tasks=false; JSESSIONID=4A511CC49255C1B35436ED44AFC68A11'
    headers["Content-Type"] = 'application/x-www-form-urlencoded'
    response = utils.httpUtil.Get(url, headers)
    soup = BeautifulSoup(response, "html.parser")  # 创建soup对象
    pageId = soup.find(attrs={"name": "ajs-page-id"})['content']  #获取meta标签中的content
    return pageId

#生成wiki的时候有一个唯一性编号，拿到这个唯一性编号；还有获取一个token
def getcreate_wikiIDict(key,parent_id):
    headers = {}
    url = 'http://wiki.ymmoa.com/pages/createpage.action?'+'spaceKey='+ key + '&fromPageId='+ parent_id
    print(url)
    headers["Cookie"] = 'seraph.confluence=17532008%3A76f9efad8b4b9a0f2e792fd106b38fc94f66c95b; confluence-sidebar.width=256.6666666666667; mywork.tab.tasks=false; JSESSIONID=4A511CC49255C1B35436ED44AFC68A11'
    headers["Content-Type"] = 'application/x-www-form-urlencoded'
    response = utils.httpUtil.Get(url, headers)
    soup = BeautifulSoup(response, "html.parser")  # 创建soup对象
    create_wikiId = soup.find(attrs={"name": "ajs-attachment-source-content-id"})['content']  # 获取meta标签中的content
    create_wikiToken = soup.find(attrs={"name": "ajs-atl-token"})['content']  # 获取meta标签中的content
    create_wikiToken2 = soup.find(attrs={"name": "atlassian-token"})['content']  # 获取meta标签中的content
    print(create_wikiToken2)
    create_wikiIDict = {}
    create_wikiIDict ['create_wikiId'] = create_wikiId
    create_wikiIDict['create_wikiToken'] = create_wikiToken
    return create_wikiIDict






if __name__ == '__main__':
    #getPassRate("dev_info_app_serviceablity",'2019-01-08','2019-01-09')
   # getRssFailedReson('uc-doorkeeper-center','2019-01-08','2019-01-09')
    print(getcreate_wikiIDict('rdTeam', '22105243'))





