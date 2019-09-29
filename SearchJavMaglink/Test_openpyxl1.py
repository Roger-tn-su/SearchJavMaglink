# encoding: utf-8
"""
@project = SearchJavMaglink
@file = Test_openpyxl
@author = ThinkPad
@create_time = 2019-09-2014:55
"""

import urllib.request

import xlrd
import xlwt
from bs4 import BeautifulSoup


def GetJavNumber(JavXlsFile, JavSheetNo):
    JavWorkbook = xlrd.open_workbook(JavXlsFile)
    JavWorksheet = JavWorkbook.sheets()[JavSheetNo]
    JavTitles = JavWorksheet.col_values(0)
    JavNumbers = []
    for JavTitle in JavTitles:
        if JavTitle != '标题':
            JavTitleSplit = JavTitle.split(' ', 1)
            JavNumbers.append(JavTitleSplit[0])
    return JavNumbers


def GetJavHtmlText(JavUrl, JavNo):
    SearchUrl = JavUrl + '/search?keyword=' + JavNo
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36'}
    request = urllib.request.Request(url=SearchUrl, headers=headers)
    try:
        response = urllib.request.urlopen(request, timeout=10)
        SearchHtmlText = response.read().decode('utf-8')
    except Exception as e:
        SearchHtmlText = 'Exception' + str(e)
        print(JavNo + SearchHtmlText)
    return SearchHtmlText


def AnalyzeJavWeb(JavWeb):
    Soup = BeautifulSoup(JavWeb, 'html5lib')
    JavList = []
    items = Soup.body.find_all('h2', class_='item-title')
    for item in items:
        if item.a['title'].count('第一会所') == 0:
            JavDict = {}
            MagnetLink = 'magnet:?xt=urn:btih:' + item.a['href'].split('/')[-1]
            JavDict[item.a['title']] = MagnetLink
            JavList.append(JavDict)
    return JavList


AvFilePath = r'C:\Users\ThinkPad\Documents\tsukada shiori.xlsx'
SearchUrl = 'https://skrbt0.xyz/'
JavList = []

JavNos = GetJavNumber(AvFilePath, -3)
print(JavNos)
for JavNo in JavNos:
    JavHtmlText = GetJavHtmlText(SearchUrl, JavNo)
    if JavHtmlText.startswith('Exception') is False:
        JavList.extend(AnalyzeJavWeb(JavHtmlText))

print(JavList)

SaveFileName = 'AvStar1.xls'
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('My Worksheet')
# worksheet.write(0,0,label='iiii')
# workbook.save('Excel_test.xls')
for i, item in enumerate(JavList):
    worksheet.write(i, 0, str(item.keys()).split('\'')[-2])
    worksheet.write(i, 1, str(item.values()).split('\'')[-2])
workbook.save(SaveFileName)
