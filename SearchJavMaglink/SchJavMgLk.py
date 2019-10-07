# encoding: utf-8
"""
@project = ExcelAccess
@file = SchJavMgLk
@author = ThinkPad
@create_time = 2019-09-2418:13
"""
from rdwtavinfo.xlop import *
from crawl.crawlweb import crawl_web
from anls.anlsweb import anls_web
from anls.anlslink import anls_mag

search_url = 'https://skrbt0.xyz/'
xls_file = 'jurujuesebanyan.xlsx'
av_file_sheet_no = -1
xls_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/' + xls_file
av_mag_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/outputfile/'
av_no_list = []
av_mag_list = []
av_error_log = []
prior_list = []
secondary_list = []
bak_list = []
sheet_title = []
sheet_name = get_av_info(xls_path_file,av_file_sheet_no,av_no_list)
av_mag_file = av_mag_path_file + sheet_name + '.xls'
for av_info in av_no_list:
    av_html = crawl_web(search_url,av_info,av_error_log)
    if av_html is not None:
        anls_web(av_html,av_info,av_mag_list,av_error_log)
anls_mag(av_mag_list,prior_list,secondary_list,bak_list,av_error_log)
sheet_title = ['编号','标题','文件名','文件大小','文件数量','链接','搜索结果数量']
wt_av_info(av_mag_file,'首选链接',sheet_title,prior_list)
wt_av_info(av_mag_file,'符合链接',sheet_title,secondary_list)
wt_av_info(av_mag_file,'备用链接',sheet_title,bak_list)
sheet_title = ['编号','标题','错误记录']
wt_av_info(av_mag_file,'错误记录',sheet_title,av_error_log)