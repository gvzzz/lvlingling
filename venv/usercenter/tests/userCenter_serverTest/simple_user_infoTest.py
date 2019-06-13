import xlwt
import base.userCenter_server
import utils.lion
import json
from dictdiffer import diff, patch, swap, revert
import datetime

#第0个json入参
def dev_simple_user_info_Open(i):
    #将lion开关打开
    utils.lion.modifylion(17439, 3, "true", 30)
    path = "../hcbdata/simple_user_info.json"
    url = "http://ucenter.dev-ag.56qq.com"
    i = 0
    openLionStr = base.userCenter_server.simple_user_info(url,path,i)
    openLionJson = json.loads(openLionStr)
    return openLionJson


def dev_simple_user_info_Clost(i):
    #将lion开关关闭
    path = "../hcbdata/simple_user_info.json"
    url = "http://ucenter.dev-ag.56qq.com"
    utils.lion.modifylion(17439, 3, "false", 30)
    closeLionStr = base.userCenter_server.simple_user_info(url, path, i)
    closeLionJson = json.loads(closeLionStr)
    return closeLionJson


def jsondif(i):
    result = diff(dev_simple_user_info_Open(i), dev_simple_user_info_Clost(i))
    return str(list(result))





#写入excel
def writeExcelDaliy(openList,closeList,inputIsSameList,difList):
    myWorkbook = xlwt.Workbook()   #创建Excel工作薄
    mySheet = myWorkbook.add_sheet('A Test Sheet',cell_overwrite_ok= True) #添加Excel工作表,可更改
    myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 数据格式
    mySheet.write(0, 0, '环境')  #A1
    mySheet.write(0, 1, '一致性or不一致')  # A2
    mySheet.write(0, 2, '开关打开的response')  # A3
    mySheet.write(0, 3, '开关关闭的response')  # A4
    mySheet.write(0, 4, 'response对比结果')  # A4
    for i in range(len(openList)):
        mySheet.write(1 + i, 0, "dev")
        mySheet.write(1 + i, 1, inputIsSameList[i])
        mySheet.write(1 + i, 2, str(openList[i]))
        mySheet.write(1 + i, 3, str(closeList[i]))
        mySheet.write(1 + i, 4, difList[i])
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    myWorkbook.save(today +"simple_user_info"+"dev"+ '.xls')


if __name__ == '__main__':
    openList =[]
    closeList = []
    inputIsSameList= []
    difList = []
    openList.append(dev_simple_user_info_Open(0))
    print(openList)
    closeList.append(dev_simple_user_info_Clost(0))
    inputIsSameList.append("第0个json入参是一致性")
    difList.append(jsondif(0))
    writeExcelDaliy(openList, closeList,inputIsSameList,difList)
