from DateUtil import currentTime,currentDate
import os

'''
本文件主要用于创建目录，用于存放异常截图
创建目录的方法仅供大家参考，将来用于根据测试
需要创建测试人员需要的目录或文件等
'''

def createDir():
    #获取当前文件所在目录的绝对路径
    currentPath = os.path.dirname(os.path.abspath(__file__))
    #获取今天的日期字符串
    today = currentDate()
    #构造以今天日期命名的目录的绝对路径
    dateDir = os.path.join(currentPath,today)
    print(dateDir)
    if not os.path.exists(dateDir):
        #如果以今天日期命名的目录不存在则创建
        os.mkdir(dateDir)
    now = currentTime()
    #构造以当前时间命名的目录的绝对路径
    timeDir = os.path.join(dateDir,now)
    print(timeDir)
    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return timeDir