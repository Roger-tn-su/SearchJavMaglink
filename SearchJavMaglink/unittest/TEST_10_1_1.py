# encoding: utf-8
"""
@project = SearchJavMaglink
@file = TEST
@author = ThinkPad
@create_time = 2019-08-0917:18
"""
test = ['ggg-111 sert high', 'sss-222 try enough']
test1 = test
for i in range(0, 2):
    testsplit = test[i].split(' ', 1)
    test1[i] = testsplit[0]
    print(testsplit[0])
