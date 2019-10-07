#encoding: utf-8
"""
@project = SearchJavMaglink
@file = getinfo
@author = ThinkPad
@create_time = 2019-09-2916:37
"""
import urllib.request


def crawl_web(sch_url,info,error_list):
    search_href = sch_url + '/search?keyword=' + info[0]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) '
                      'Chrome/56.0.2924.87 Safari/537.36'}
    request = urllib.request.Request(url=search_href, headers=headers)
    try:
        response = urllib.request.urlopen(request, timeout=10)
        search_html_text = response.read().decode('utf-8')
    except Exception as e:
        search_html_text = None
        print(info[0] + ' ' + str(e))
        error_list.append([av_info[0], av_info[1], str(e)])
    return search_html_text