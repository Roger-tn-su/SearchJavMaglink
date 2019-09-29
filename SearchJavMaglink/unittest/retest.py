# encoding: utf-8
"""
@project = SearchJavMaglink
@file = retest
@author = ThinkPad
@create_time = 2019-09-2813:23
"""
import re

pattern = r'(\[.+\..+\])|(【入微】)|(\.mp4$)|(^\#\_)'
string = ['[Thz.la]abp-739', '【入微】CADV255', '[168x.me]jufd-944', \
          '巨乳AV女優春菜華(春菜はな)出演系列合集12部', 'JUFD-955', 'PTNOZ003mp4', '[SSNI-290].mp4', \
          '#_avop155']
for item in string:
    search = re.search(pattern, item, re.IGNORECASE)
    print(item, search)
