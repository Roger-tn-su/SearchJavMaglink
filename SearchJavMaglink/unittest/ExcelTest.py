# encoding: utf-8
"""
@project = ExcelAccess
@file = ExcelTest
@author = ThinkPad
@create_time = 2019-09-248:32
"""
import xlrd
import xlwt

# def GetJavNumber(JavXlsFile,JavSheetNo):
#      JavWorkbook = xlrd.open_workbook(JavXlsFile)
#      JavWorksheet = JavWorkbook.sheets()[JavSheetNo]
#      JavTitles = JavWorksheet.col_values(0)
#      JavNumbers = []
#      for JavTitle in JavTitles:
#          JavTitleSplit = JavTitle.split(' ',1)
#          JavNumbers.append(JavTitleSplit[0])
#      return JavNumbers

inputxls = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/tsukada ' \
           'shiori.xlsx'
outputpath = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/outputfile/'
JavSheetNo = -1

JavWorkbook = xlrd.open_workbook(inputxls)
outputxls = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/outputfile/' + \
            JavWorkbook.sheet_names()[JavSheetNo] + '.xls'
# print(JavWorkbook.sheet_names())
# print(outputxls)
JavTitles = JavWorkbook.sheets()[JavSheetNo].col_values(0)
JavList = []
for JavTitle in JavTitles:
    JavNumber = JavTitle.split(' ', 1)[0]
    JavName = JavTitle.split(' ', 1)[1]
    JavList.append([JavNumber, JavName])
RegXls = xlwt.Workbook(encoding='utf-8')
RegSheet = RegXls.add_sheet(JavWorkbook.sheet_names()[JavSheetNo], \
                            cell_overwrite_ok=True)
MagSch = RegXls.add_sheet('MagSchRt')
for i, item in enumerate(JavList):
    RegSheet.write(i, 0, item[0])
    RegSheet.write(i, 1, item[1])
RegXls.save(outputxls)
