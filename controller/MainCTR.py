# -*- encoding: utf-8 -*-
'''
@File    :   MainCTR.py
@Time    :   2022/05/06 09:52:50
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from pydoc import pathdirs
import numpy as np
from Models.TableOperator import (
    GetTableData,
    GetFlagData,
    GetListData
)
from PySide6.QtWidgets import (
    QVBoxLayout, 
)
from Models.utils import CheckPathFlag
from View import MainWindows
from Controller import GetInfoController, GetScriptController
from PySide6 import QtCore
from PySide6.QtCore import Signal

class MainController:
    def __init__(self):
        self.windows = MainWindows()
        self.getinfoCTR = GetInfoController(self.windows.getinfowidget)
        self.getscriptCTR = GetScriptController(self.windows.getscriptwidget)
        self.windows.getinfowidget.GenBTN.connect(self._gen)
        # self.windows.getinfowidget.GenBTN.connect(self.getscriptCTR.GetTableData)
        # getinfowidget.PressOK.connect(load_parameter)
        
        self.windows.getinfowidget.ClossBTN.connect(self._exit)
        self.windows.getscriptwidget.ClossBTN.connect(self._exit)
        self.windows.show()
        
    @QtCore.Slot()
    def _exit(self):
        self.windows.close()
        
    @QtCore.Slot()
    def _gen(self):
        # FIXME 清除第二個tab的資料內容
        self.windows.getscriptwidget.showpathflag.ClearLayout()
        # self.windows.getscriptwidget
        
        RightStack = self.windows.getinfowidget.RightStack
        LeftTable = self.windows.getinfowidget.LeftTable
        
        # 取得table內的資料
        ABSLData = GetTableData(LeftTable.table)
        ABSLData = np.array(ABSLData)
        
        # 取得對應的list資料
        ABSLValue = []
        for idx in range(ABSLData.shape[0]):
            widgetToRemove = RightStack.widget(idx)
            value = GetListData(widgetToRemove.ParameterList)
            ABSLValue.append(value)
        ABSLValue = np.array(ABSLValue)
        
        path_idx, other_idx = CheckPathFlag(ABSLData, ABSLValue)
        
        # 包含path的flag
        for idx in path_idx:
            FlagName = ABSLData[idx][0]
            FlagValue = ABSLValue[idx][0]
            print(FlagName, FlagValue)
            self.getscriptCTR.PathFlagGenerate(FlagName, FlagValue)
        
        # 跳轉下一個tab
        self.windows.tabWidget.setCurrentIndex(self.windows.tabWidget.currentIndex()+1)
