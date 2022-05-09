# -*- encoding: utf-8 -*-
'''
@File    :   TableOperator.py
@Time    :   2022/05/09 21:21:08
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib

def GetFlagData(table):
    flag_list = []
    n_row = table.rowCount()
    for row in range(n_row):
        item = table.item(row, 0).text()
        flag_list.append(str(item))
    return flag_list

def GetListData(ListWidget):
    item_list = []
    for row in range(ListWidget.count()):
        item = ListWidget.item(row).text()
        item_list.append(str(item))
    return item_list