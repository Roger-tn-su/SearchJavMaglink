#encoding: utf-8
"""
@project = SearchJavMaglink
@file = anls
@author = ThinkPad
@create_time = 2019-09-2916:34
"""

from bs4 import BeautifulSoup


def anls_av_web(av_web, av_info, av_mags_list):
    soup = BeautifulSoup(av_web, 'html5lib')
    items = soup.body.find_all('li', class_='search-ret-item')
    if len(items):
        for item in items:
            file_size_text = item.div.span.get_text()
            if file_size_text.split(' ')[-1] == 'MB':
                file_size = float(file_size_text.split(' ')[0]) / 1024
            else:
                file_size = float(file_size_text.split(' ')[0])
            file_count = int(item.div.span.next_sibling.next_sibling.get_text())
            file_name = item.h2.a['title']
            file_link = 'magnet:?xt=urn:btih:' + item.h2.a['href'].split('/')[-1]
            av_mags_list.append(
                [av_info[0], av_info[1], file_name, file_size, file_count, file_link,
                 len(items)])
    else:
        av_mags_list.append([av_info[0], av_info[1], 'Not found', 'None', 0, 0, 0])

