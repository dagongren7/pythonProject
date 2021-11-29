from openpyxl import load_workbook

class ParseExcel():
    def __init__(self,excelPath):
        self.wb = load_workbook(excelPath)
        self.sheet = self.wb.active

    
    def getDatasFromSheet(self):
        dataList = []
        for line in self.sheet:
            print(line)
            tmpList=[]
            tmpList.append(line[1].value)
            tmpList.append(line[2].value)
            dataList.append(tmpList)
        return dataList[1:]

if __name__ == '__main__':
    excelPath='D:/test.xlsx'
    sheetName = '搜索数据表'
    pe = ParseExcel(excelPath)
    for i in pe.getDatasFromSheet()[1:]:
        print(i[0])
    pass