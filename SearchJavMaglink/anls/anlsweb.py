#encoding: utf-8
"""
@project = SearchJavMaglink
@file = anls
@author = ThinkPad
@create_time = 2019-09-2916:34
"""

from bs4 import BeautifulSoup


def anls_web(web_content,info,mag_list,error_list):
    soup = BeautifulSoup(web_content, 'html5lib')
    items = soup.body.find_all('ul', class_='list-unstyled')
    if len(items):
        for item in items:
            target = item.findChild('li',class_='result-resource-meta-info')
            file_size_text = target.span.get_text()
            if file_size_text.split(' ')[-1] == 'MB':
                file_size = float(file_size_text.split(' ')[0]) / 1024
            else:
                file_size = float(file_size_text.split(' ')[0])
            file_count = int(target.span.next_sibling.next_sibling.get_text())
            file_name = item.li.a['title']
            file_link = 'magnet:?xt=urn:btih:' + target.a['href'].split('/')[-1]
            mag_list.append(
                [info[0], info[1], file_name, file_size, file_count, file_link,
                 len(items)])
    else:
        error_list.append([info[0], info[1], 'SN Not found'])

