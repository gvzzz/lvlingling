import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append("venv/usercenter/data")
sys.setdefaultencoding('utf-8')
sys.path.append("venv/usercenter/utils")
sys.path.append("venv/usercenter/base")