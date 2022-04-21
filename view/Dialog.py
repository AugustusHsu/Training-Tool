# -*- encoding: utf-8 -*-
'''
@File    :   Dialog.py
@Time    :   2022/04/16 03:08:43
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from PySide6.QtWidgets import (
    QMessageBox
)

def NoSelectDialog_edit(windows):
    ret = QMessageBox.warning(
        windows, 
        'No Select Parameter!',
        'You need to select one parameter to edit it.',
        QMessageBox.Ok
    )
    
def NoSelectDialog_delete(windows):
    ret = QMessageBox.warning(
        windows, 
        'No Select Parameter!',
        'You need to select one parameter to delete it.',
        QMessageBox.Ok
    )

def ParameterEmpty(windows):
    ret = QMessageBox.warning(
        windows, 
        'Parameter is Empty!',
        'You must enter at least one string.',
        QMessageBox.Ok
    )
    
# def NoSelectDialog_delete(windows):
#     ret = QMessageBox.warning(
#         windows, 
#         'No Select Parameter!',
#         'You need to select one parameter to delete it.',
#         QMessageBox.Ok
#     )

