# -*- encoding: utf-8 -*-
'''
@File    :   MainCTR.py
@Time    :   2022/05/06 09:52:50
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from Models.TableOperator import (
    GetFlagData,
    GetListData
)
from View import MainWindows
from Controller import GetInfoController, GetScriptController
from PySide6 import QtCore

class MainController:
    def __init__(self):
        self.windows = MainWindows()
        self.getinfoCTR = GetInfoController(self.windows.getinfowidget)
        self.getscriptCTR = GetScriptController(self.windows.getscriptwidget)
        self.windows.getinfowidget.GenBTN.connect(self._gen)
        self.windows.getinfowidget.ClossBTN.connect(self._exit)
        self.windows.show()
        
    @QtCore.Slot()
    def _exit(self):
        self.windows.close()
        
    @QtCore.Slot()
    def _gen(self):
        RightStack = self.windows.getinfowidget.RightStack
        LeftTable = self.windows.getinfowidget.LeftTable
        
        # for idx in range(LeftTable.table.rowCount()):
        # 取得flag
        flag_list = GetFlagData(LeftTable.table)
        for idx, flag in enumerate(flag_list):
            widgetToRemove = RightStack.widget(idx)
            item_list = GetListData(widgetToRemove.ParameterList)
        
            print(flag, item_list)
        # TODO 取得所需的參數，將參數輸入下一個tab並跳轉
        self.windows.tabWidget.setCurrentIndex(self.windows.tabWidget.currentIndex()+1)
