# encoding: utf-8
"""
@project = ExcelAccess
@file = AnalyzeJavHtml
@author = ThinkPad
@create_time = 2019-09-2322:10
"""
from bs4 import BeautifulSoup

InputFile = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/abp-739.html'
OutputFile = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/SingleJavText.xls'

TestFile = open(InputFile, 'r', encoding='utf-8')

TestText = TestFile.read()

Soup = BeautifulSoup(TestText, 'html5lib')
# JavList = []
# JavDict = {}
items = Soup.body.find_all('li', class_='search-ret-item')

# print(items[0].div.span.next_sibling.next_sibling.get_text())
# print(items[0].h2.a['title'])
# print(items[0].h2.a['href'])
# print(items[0].div.span.get_text())

for item in items:
    FileSize = item.div.span.get_text()
    FileCount = item.div.span.next_sibling.next_sibling.get_text()
    FileName = items.h2.a['title']
    FileLink = 'magnet:?xt=urn:btih:' + item.h2.a['href'].split('/')[-1]
#     JavDict = {}
#     if item.a['title'].count('第一会所') == 0 :
#         MagnetLink = 'magnet:?xt=urn:btih:'+item.a['href'].split('/')[-1]
#         JavDict[item.a['title']]= MagnetLink
#     if bool(JavDict):
#         JavList.append(JavDict)
#
#
# workbook = xlwt.Workbook(encoding = 'utf-8')
# worksheet = workbook.add_sheet('My Worksheet')
# #worksheet.write(0,0,label='iiii')
# #workbook.save('Excel_test.xls')
# for i,item in enumerate(JavList):
#     worksheet.write(i, 0, str(item.keys()).split('\'')[-2])
#     worksheet.write(i, 1, str(item.values()).split('\'')[-2])
# workbook.save('Excel_test.xls')
