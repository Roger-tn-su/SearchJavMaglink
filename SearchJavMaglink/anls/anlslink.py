#encoding: utf-8
"""
@project = SearchJavMaglink
@file = anlslink
@author = ThinkPad
@create_time = 2019-09-2917:00
"""
import re

import xlrd
import xlwt


def take_size(av_info_elem):
    return av_info_elem[3]


# def get_av_info(ax_xls_file, av_info_list):
#     jav_workbook = xlrd.open_workbook(ax_xls_file)
#     jav_sheet = jav_workbook.sheets()[0]
#     for i in range(0, jav_sheet.nrows):
#         av_info_list.append(jav_sheet.row(i))





# def anls_mag(mag_info_list[:],valid_mag_list,bak_mag_list):
#      while len(mag_info_list):
#          anls_slice = mag_info_list[:int(mag_info_list[0][6].value)]
#          del mag_info_list[:int(mag_info_list[0][6].value)]

# xls_file = 'jurujuesebanyantest.xls'
# xls_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/datafile/' + xls_file
# output_file = 'jurutest.xls'
# output_path_file = 'D:/Python/Project/ExcelAccess/SearchJavMaglink/outputfile/' + output_file
# av_mag_info_list = []
# av_valid_mag_list = []
# av_bak_mag_list = []
# av_act_slice = []
# av_act_mag_list = []

def anls_mag(mag_list,first_list,second_list,bak_list,error_list):
    legal_pattern = r'(\[.+\..+\])|(【入微】)|(\.mp4$)|(^\#\_)'
    illegal_pattern = r'(第一会所)|(第一會所)'
    # get_av_info(xls_path_file, av_mag_info_list)
    while len(mag_list):
        flag = 0
        av_slice = mag_list[:int(mag_list[0][6])]
        del mag_list[:int(mag_list[0][6])]
        av_slice.sort(key=take_size)
        for item in av_slice[:]:
            av_code_pattern = r'.*' + item[0].split('-', 1)[0] + r'.*' + item[0].split('-', 1)[1] \
                              + r'.*'
            if re.search(illegal_pattern, item[2], re.IGNORECASE) is not None:
                continue
            elif re.search(av_code_pattern, item[2], re.IGNORECASE) is not None:
                if (re.search(legal_pattern, item[2], re.IGNORECASE) is not None) and \
                        (flag == 0):
                    first_list.append(item)
                    flag = 1
                else:
                    second_list.append(item)
            else:
                bak_list.append(item)
        if flag == 0:
            error_list.append(
                [av_slice[0][0], av_slice[0][1], 'no matched item'])

# print(len(av_mag_info_list), av_mag_info_list)
# print (len(av_act_mag_list),av_act_mag_list)
# print(len(av_valid_mag_list), av_valid_mag_list)
# print(len(av_bak_mag_list), av_bak_mag_list)
# wt_mag_link(output_path_file, av_act_mag_list, av_valid_mag_list, av_bak_mag_list)

# anls_slice = av_mag_info_list[:int(av_mag_info_list[0][6].value)]
# del av_mag_info_list[:int(av_mag_info_list[0][6].value)]
# anls_slice.sort(key=take_size)
