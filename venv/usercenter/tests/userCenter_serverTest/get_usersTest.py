import xlwt
import base.userCenter_server
import json
import os.path
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
from dictdiffer import diff, patch, swap, revert
import datetime
import time
import utils.lion


#第0个json入参
def dev_get_users_Open(i):
    #将lion开关打开
    utils.lion.modifylion(17439, 3, "true", 30)
    time.sleep(5)
    #获取上上级目录
    path_base = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    path = path_base + "/hcbdata/get_users.json"  # 拼成绝对路径
    url = "http://ucenter.dev-ag.56qq.com"
    openLionStr = base.userCenter_server.get_users(url,path,i)
    openLionJson = json.loads(openLionStr)
    return openLionJson


def dev_get_users_Clost(i):
    # 获取上上级目录
    path_base = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    path = path_base + "/hcbdata/get_users.json"  # 拼成绝对路径
    url = "http://ucenter.dev-ag.56qq.com"
    # 将lion开关关闭
    utils.lion.modifylion(17439, 3, "false", 30)
    time.sleep(5)
    closeLionStr = base.userCenter_server.get_users(url, path, i)
    closeLionJson = json.loads(closeLionStr)
    return closeLionJson


def jsondif(i):
    result = diff(dev_get_users_Open(i), dev_get_users_Clost(i))
    return str(list(result))





#写入excel
def writeExcelDaliy(openList,closeList,inputIsSameList,difList):
    myWorkbook = xlwt.Workbook()   #创建Excel工作薄
    mySheet = myWorkbook.add_sheet('A Test Sheet',cell_overwrite_ok= True) #添加Excel工作表,可更改
    myStyle = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 数据格式
    mySheet.write(0, 0, '环境')  #A0
    mySheet.write(0, 1, '一致性or不一致')  # B0
    mySheet.write(0, 2, '开关打开的response')  # C0
    mySheet.write(0, 3, '开关关闭的response')  # D0
    mySheet.write(0, 4, 'response对比结果')  # E0
    for i in range(len(openList)):
        mySheet.write(1 + i, 0, "dev")
        mySheet.write(1 + i, 1, inputIsSameList[i])
        mySheet.write(1 + i, 2, str(openList[i]))
        mySheet.write(1 + i, 3, str(closeList[i]))
        mySheet.write(1 + i, 4, difList[i])
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    myWorkbook.save(today +"get_users"+"dev"+ '.xls')


if __name__ == '__main__':
    openList =[]
    closeList = []
    inputIsSameList= []
    difList = []
    openList.append(dev_get_users_Open(0))
    closeList.append(dev_get_users_Clost(0))
    inputIsSameList.append("第0个json入参是一致性司机")
    difList.append(jsondif(0))
    writeExcelDaliy(openList, closeList,inputIsSameList,difList)

    openList.append(dev_get_users_Open(1))
    closeList.append(dev_get_users_Clost(1))
    inputIsSameList.append("第1个json入参是非一致性司机")
    difList.append(jsondif(1))
    writeExcelDaliy(openList, closeList, inputIsSameList, difList)

    openList.append(dev_get_users_Open(2))
    closeList.append(dev_get_users_Clost(2))
    inputIsSameList.append("第2个json入参是一致性货主")
    difList.append(jsondif(2))
    writeExcelDaliy(openList, closeList, inputIsSameList, difList)

    openList.append(dev_get_users_Open(3))
    closeList.append(dev_get_users_Clost(3))
    inputIsSameList.append("第3个json入参是非一致性货主")
    difList.append(jsondif(3))
    writeExcelDaliy(openList, closeList, inputIsSameList, difList)
