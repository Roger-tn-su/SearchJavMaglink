# encoding: utf-8
"""
@project = SearchJavMaglink
@file = beautifulsouptest
@author = ThinkPad
@create_time = 2019-09-2111:20
"""
import xlwt
from bs4 import BeautifulSoup

TestFile = open('test.html', 'r', encoding='utf-8')

TestText = TestFile.read()

Soup = BeautifulSoup(TestText, 'html5lib')
JavList = []
JavDict = {}
items = Soup.body.find_all('h2', class_='item-title')
for item in items:
    JavDict = {}
    if item.a['title'].count('第一会所') == 0:
        MagnetLink = 'magnet:?xt=urn:btih:' + item.a['href'].split('/')[-1]
        JavDict[item.a['title']] = MagnetLink
    if bool(JavDict):
        JavList.append(JavDict)

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('My Worksheet')
# worksheet.write(0,0,label='iiii')
# workbook.save('Excel_test.xls')
for i, item in enumerate(JavList):
    worksheet.write(i, 0, str(item.keys()).split('\'')[-2])
    worksheet.write(i, 1, str(item.values()).split('\'')[-2])
workbook.save('Excel_test.xls')
