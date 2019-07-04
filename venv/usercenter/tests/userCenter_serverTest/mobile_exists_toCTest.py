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
def qa_mobile_exists_toC(i):
    #将lion开关打开qa是4 dev是3
    utils.lion.modifylion(17439, 3, "true", 30)
    time.sleep(1)
    #获取上上级目录
    path_base = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    path = path_base + "/hcbdata/mobile_exists_toC.json"  # 拼成绝对路径
    #diapatch_url = "http://ucenter.qa-sh.56qq.com/v1.1/mobile/dispatch.do"
    diapatch_url = "http://192.168.206.110:8080/mobile/user/mobile/exists"
    openLionJson = base.userCenter_server.mobile_exists_toC(diapatch_url,path,i)

    # 将lion开关关闭qa是4 dev是3
    utils.lion.modifylion(17439, 3, "false", 30)
    time.sleep(1)
    closeLionJson = base.userCenter_server.mobile_exists_toC(diapatch_url, path, i)

    result = diff(openLionJson, closeLionJson)  # 对比的list
    dic = {"openLionJson": openLionJson, "closeLionJson": closeLionJson, 'difStr': str(list(result))}

    return dic




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
    myWorkbook.save(today +"mobile_exists_toC"+"dev"+ '.xls')


if __name__ == '__main__':
    openList =[]
    closeList = []
    inputIsSameList= []
    difList = []
    dict0 = qa_mobile_exists_toC(0)
    openList.append(dict0.get("openLionJson"))
    closeList.append(dict0.get("closeLionJson"))
    inputIsSameList.append("第0个json是随机")
    difList.append(dict0.get("difStr"))
    writeExcelDaliy(openList, closeList,inputIsSameList,difList)


