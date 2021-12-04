from openpyxl import load_workbook

class ParseExcel():
    def __init__(self,excelPath):
        self.wb = load_workbook(excelPath)
        self.sheet = self.wb.active

    
    def getDatasFromSheet(self):
        dataList = []
        for line in self.sheet:
            tmpList=[]
            tmpList.append(line[0].value)
            tmpList.append(line[1].value)
            dataList.append(tmpList)
            #0 1 从第二行开始打印
        # print(dataList,"---------",dataList[1:])
        return dataList

if __name__ == '__main__':
    excelPath = 'D:/test.xlsx'
    sheetName = '搜索数据表'
    pe = ParseExcel(excelPath)
    pe.getDatasFromSheet()