# -*- encoding: utf-8 -*-
'''
@File    :   MainCTR.py
@Time    :   2022/05/06 09:52:50
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from Models.TableOperator import (
    GetTableData,
    GetFlagData,
    GetListData
)
from View import MainWindows
from Controller import GetInfoController, GetScriptController
from PySide6 import QtCore
from PySide6.QtCore import Signal

class MainController:
    def __init__(self):
        self.windows = MainWindows()
        self.getinfoCTR = GetInfoController(self.windows.getinfowidget)
        self.getscriptCTR = GetScriptController(self.windows.getscriptwidget)
        # self.windows.getinfowidget.GenBTN.connect(self._gen)
        self.windows.getinfowidget.GenBTN.connect(self.getscriptCTR.GetTableData)
        # getinfowidget.PressOK.connect(load_parameter)
        
        self.windows.getinfowidget.ClossBTN.connect(self._exit)
        self.windows.getscriptwidget.ClossBTN.connect(self._exit)
        self.windows.show()
        
    @QtCore.Slot()
    def _exit(self):
        self.windows.close()
        
    @QtCore.Slot()
    def _gen(self):
        GenFlag = Signal()
        
        RightStack = self.windows.getinfowidget.RightStack
        LeftTable = self.windows.getinfowidget.LeftTable
        
        # for idx in range(LeftTable.table.rowCount()):
        # 取得table內的資料
        ABSLData = GetTableData(LeftTable.table)
        print(ABSLData)
        # 取得對應的list資料
        item_list = []
        # 取得flag
        flag_list = GetFlagData(LeftTable.table)
        for idx, flag in enumerate(flag_list):
            widgetToRemove = RightStack.widget(idx)
            item_list = GetListData(widgetToRemove.ParameterList)
        
            print(flag, item_list)
        # TODO 取得所需的參數，將參數輸入下一個tab並跳轉
        self.windows.tabWidget.setCurrentIndex(self.windows.tabWidget.currentIndex()+1)
