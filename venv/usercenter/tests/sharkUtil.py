#coding:utf-8
import httpUtil
import data
import json

#触发shark平台生成报告
def trigger(jsonName):
    triggerUrl = data.trigger_url
    triggerHeaders = data.trigger_header
    f = file(jsonName)
    PostJson = json.load(f)

    triggerResponse = httpUtil.Post(triggerUrl, triggerHeaders, PostJson)
    triggerReponseJson = json.loads(triggerResponse)
    timeData = triggerReponseJson['data']  # 从触发器的接口中读出返回data，去查询对应的报告
    return timeData

#查询报告
def queryReport(timeData):
    reportUrl = data.report_url
    reportHeaders = data.report_header
    reportResponse = httpUtil.Get(reportUrl, timeData, reportHeaders)
    reporteponseJson = json.loads(reportResponse)
    return reporteponseJson


