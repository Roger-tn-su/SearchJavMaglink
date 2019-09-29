#encoding: utf-8
"""
@project = SearchJavMaglink
@file = xlop
@author = ThinkPad
@create_time = 2019-09-2916:31
"""
import xlwt
import xlrd

def get_av_nos(av_xls_file, av_xsl_sheet_no, av_nos_list):
    jav_workbook = xlrd.open_workbook(av_xls_file)
    jav_titles = jav_workbook.sheets()[av_xsl_sheet_no].col_values(0)
    for jav_title in jav_titles:
        jav_number = jav_title.split(' ', 1)[0]
        jav_name = jav_title.split(' ', 1)[1]
        av_nos_list.append([jav_number, jav_name])
    return jav_workbook.sheet_names()[av_xsl_sheet_no]

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