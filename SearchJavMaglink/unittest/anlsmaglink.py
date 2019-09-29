# encoding: utf-8
"""
@project = SearchJavMaglink
@file = anlsmaglink
@author = ThinkPad
@create_time = 2019-09-2716:22
"""
import re

import xlrd
import xlwt


def take_size(av_info_elem):
    return av_info_elem[3]


def get_av_info(ax_xls_file, av_info_list):
    jav_workbook = xlrd.open_workbook(ax_xls_file)
    jav_sheet = jav_workbook.sheets()[0]
    for i in range(0, jav_sheet.nrows):
        av_info_list.append(jav_sheet.row(i))


def wt_mag_link(output_file, act_list, valid_list, bak_list):
    out_xls = xlwt.Workbook(encoding='utf-8')
    act_sheet = out_xls.add_sheet('act', cell_overwrite_ok=True)
    valid_sheet = out_xls.add_sheet('valid', cell_overwrite_ok=True)
    bak_sheet = out_xls.add_sheet('bak', cell_overwrite_ok=True)
    for i, item in enumerate(act_list):
        if item[2] is not None:
            act_sheet.write(i, 0, item[0].value)
            act_sheet.write(i, 1, item[1].value)
            act_sheet.write(i, 2, item[2].value)
            act_sheet.write(i, 3, item[3].value)
            act_sheet.write(i, 4, item[4].value)
            act_sheet.write(i, 5, item[5].value)
            act_sheet.write(i, 6, item[6].value)
        else:
            act_sheet.write(i, 0, item[0])
            act_sheet.write(i, 1, item[1])

    for i, item in enumerate(valid_list):
        valid_sheet.write(i, 0, item[0].value)
        valid_sheet.write(i, 1, item[1].value)
        valid_sheet.write(i, 2, item[2].value)
        valid_sheet.write(i, 3, item[3].value)
        valid_sheet.write(i, 4, item[4].value)
        valid_sheet.write(i, 5, item[5].value)
        valid_sheet.write(i, 6, item[6].value)
    for i, item in enumerate(bak_list):
        bak_sheet.write(i, 0, item[0].value)
        bak_sheet.write(i, 1, item[1].value)
        bak_sheet.write(i, 2, item[2].value)
        bak_sheet.write(i, 3, item[3].value)
        bak_sheet.write(i, 4, item[4].value)
        bak_sheet.write(i, 5, item[5].value)
        bak_sheet.write(i, 6, item[6].value)
    out_xls.save(output_file)


# def anls_mag(mag_info_list[:],valid_mag_list,bak_mag_list):
#      while len(mag_info_list):
#          anls_slice = mag_info_list[:int(mag_info_list[0][6].value)]
#          del mag_info_list[:int(mag_info_list[0][6].value)]

xls_file = 'jurujuesebanyantest.xls'
xls_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/' + xls_file
output_file = 'jurutest.xls'
output_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/outputfile/' + output_file
av_mag_info_list = []
av_valid_mag_list = []
av_bak_mag_list = []
av_act_slice = []
av_act_mag_list = []
legal_pattern = r'(\[.+\..+\])|(【入微】)|(\.mp4$)|(^\#\_)'
illegal_pattern = r'(第一会所)|(第一會所)'
get_av_info(xls_path_file, av_mag_info_list)
print(len(av_mag_info_list))
while len(av_mag_info_list):
    flag = 0
    av_slice = av_mag_info_list[:int(av_mag_info_list[0][6].value)]
    del av_mag_info_list[:int(av_mag_info_list[0][6].value)]
    for item in av_slice[:]:
        av_code_pattern = r'.*' + item[0].value.split('-', 1)[0] + r'.*' + \
                          item[0].value.split('-', 1)[1] + r'.*'
        if re.search(illegal_pattern, item[2].value, re.IGNORECASE) is not None:
            continue
        elif re.search(av_code_pattern, item[2].value, re.IGNORECASE) is not None:
            if (re.search(legal_pattern, item[2].value, re.IGNORECASE) is not None) and (flag == 0):
                av_act_mag_list.append(item)
                flag = 1
            else:
                av_valid_mag_list.append(item)
        else:
            av_bak_mag_list.append(item)
    if flag == 0:
        av_act_mag_list.append(
            [av_slice[0][0].value, av_slice[0][1].value, None, None, None, None, None])

# print(len(av_mag_info_list), av_mag_info_list)
# print (len(av_act_mag_list),av_act_mag_list)
# print(len(av_valid_mag_list), av_valid_mag_list)
# print(len(av_bak_mag_list), av_bak_mag_list)
wt_mag_link(output_path_file, av_act_mag_list, av_valid_mag_list, av_bak_mag_list)

# anls_slice = av_mag_info_list[:int(av_mag_info_list[0][6].value)]
# del av_mag_info_list[:int(av_mag_info_list[0][6].value)]
# anls_slice.sort(key=take_size)
