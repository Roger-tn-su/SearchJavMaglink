#encoding: utf-8
"""
@project = SearchJavMaglink
@file = xlop
@author = ThinkPad
@create_time = 2019-09-2916:31
"""
import xlwt
import xlrd


def get_av_info(filename,sheet_no,info_list):
    jav_workbook = xlrd.open_workbook(filename)
    jav_titles = jav_workbook.sheets()[sheet_no].col_values(0)
    for jav_title in jav_titles:
        jav_number = jav_title.split(' ', 1)[0]
        jav_name = jav_title.split(' ', 1)[1]
        info_list.append([jav_number, jav_name])
    return jav_workbook.sheet_names()[sheet_no]


def wt_av_info(filename,sheet_name,title,wt_list):
    out_file = xlwt.Workbook(encoding='utf-8')
    out_sheet = out_file.add_sheet(sheet_name, cell_overwrite_ok=True)
    wt_list.insert(0,title)
    for i, item in enumerate(wt_list):
        for j, elem in enumerate(item):
            out_sheet.write(i,j,elem)
    out_file.save(filename)