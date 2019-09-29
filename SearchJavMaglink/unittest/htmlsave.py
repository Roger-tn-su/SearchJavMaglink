# encoding: utf-8
"""
@project = SearchJavMaglink
@file = htmlsave
@author = ThinkPad
@create_time = 2019-09-2321:45
"""

import urllib.request

JavNo = 'meyd-450'
url = 'https://skrbt3.xyz/'
SearchUrl = url + '/search?keyword=' + JavNo
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/56.0.2924.87 Safari/537.36'}
request = urllib.request.Request(url=SearchUrl, headers=headers)
response = urllib.request.urlopen(request)
SearchHtmlText1 = response.read().decode('utf-8')

GenHtml = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/' + JavNo \
          + '.html'

File = open(GenHtml, 'w', encoding='utf-8')

File.write(SearchHtmlText1)
