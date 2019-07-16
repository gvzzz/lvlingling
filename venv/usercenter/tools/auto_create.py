'''自动生成有效手机号、生成有效的身份证号码'''

from datetime import date
from datetime import timedelta
import random
class auto_create_number():
    def phoneCreate(self):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

    def idCardCreate(self):
        codelist = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428', '362429', '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105', '110106', '110107', '110108', '110109', '110111', '320681', '320626', '310115']
        id = random.choice(codelist)  # 地区项
        id = id + str(random.randint(1930, 2000))  # 年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  # 月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  # ，顺序号简单处理

        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码
        return id


if __name__ == '__main__':
    pc = auto_create_number()
    print(pc.phoneCreate())
    print(pc.idCardCreate())


