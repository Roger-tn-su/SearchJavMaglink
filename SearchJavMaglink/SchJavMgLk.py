# encoding: utf-8
"""
@project = ExcelAccess
@file = SchJavMgLk
@author = ThinkPad
@create_time = 2019-09-2418:13
"""
import urllib.request

import xlrd
import xlwt
from bs4 import BeautifulSoup


def get_av_nos(ax_xls_file, av_xsl_sheet_no, av_nos_list):
    jav_workbook = xlrd.open_workbook(ax_xls_file)
    jav_titles = jav_workbook.sheets()[av_xsl_sheet_no].col_values(0)
    for jav_title in jav_titles:
        jav_number = jav_title.split(' ', 1)[0]
        jav_name = jav_title.split(' ', 1)[1]
        av_nos_list.append([jav_number, jav_name])
    return jav_workbook.sheet_names()[av_xsl_sheet_no]


def get_av_web(av_url, av_info, av_error_log):
    search_href = av_url + '/search?keyword=' + av_info[0]
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
        print(av_info[0] + ' ' + str(e))
        av_error_log.append([av_info[0], av_info[1], str(e)])
    return search_html_text


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


def wt_mag_link(output_file, sheet_name_wt, mag_link, error_log):
    reg_xls = xlwt.Workbook(encoding='utf-8')
    reg_sheet = reg_xls.add_sheet(sheet_name_wt, cell_overwrite_ok=True)
    error_sheet = reg_xls.add_sheet('ErrorLog', cell_overwrite_ok=True)
    for i, item in enumerate(mag_link):
        reg_sheet.write(i, 0, item[0])
        reg_sheet.write(i, 1, item[1])
        reg_sheet.write(i, 2, item[2])
        reg_sheet.write(i, 3, item[3])
        reg_sheet.write(i, 4, item[4])
        reg_sheet.write(i, 5, item[5])
        reg_sheet.write(i, 6, item[6])
    for i, item in enumerate(error_log):
        error_sheet.write(i, 0, item[0])
        error_sheet.write(i, 1, item[1])
        error_sheet.write(i, 2, item[2])
    reg_xls.save(output_file)


search_url = 'https://skrbt0.xyz/'
xls_file = 'jurujuesebanyan.xlsx'
av_file_sheet_no = -1
xls_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/' + xls_file
av_mag_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/outputfile/'
av_no_list = []
av_mag_list = []
av_excp_log = []
sheet_name = get_av_nos(xls_path_file, av_file_sheet_no, av_no_list)
av_mag_file = av_mag_path_file + sheet_name + '.xls'
for JavInfo in av_no_list:
    JavHtml = get_av_web(search_url, JavInfo, av_excp_log)
    if JavHtml is not None:
        anls_av_web(JavHtml, JavInfo, av_mag_list)
wt_mag_link(av_mag_file, sheet_name, av_mag_list, av_excp_log)
