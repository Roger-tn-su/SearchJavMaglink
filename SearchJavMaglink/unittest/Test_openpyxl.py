# encoding: utf-8
"""
@project = SearchJavMaglink
@file = Test_openpyxl
@author = ThinkPad
@create_time = 2019-09-2014:55
"""

import urllib.request

# def GetJavNumber(JavXlsFile,JavSheetNo):
#     JavWorkbook = xlrd.open_workbook(JavXlsFile)
#     JavWorksheet = JavWorkbook.sheets()[JavSheetNo]
#     JavTitles = JavWorksheet.col_values(0)
#     JavNumbers = []
#     for JavTitle in JavTitles:
#         JavTitleSplit = JavTitle.split(' ',1)
#         JavNumbers.append(JavTitleSplit[0])
#     return JavNumbers


# FilePath=r'C:\Users\ThinkPad\Documents\tsukada shiori.xlsx'
# JavNos = GetJavNumber(FilePath,-1)

url = 'https://skrbt3.xyz/'
SearchUrl = url + '/search?keyword=' + 'rbd-456'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'}
request = urllib.request.Request(url=SearchUrl, headers=headers)
response = urllib.request.urlopen(request)
SearchHtmlText1 = response.read().decode('utf-8')

GenHtml = 'rbd-456.html'

File = open(GenHtml, 'w', encoding='utf-8')

File.write(SearchHtmlText1)
