# -*- encoding: utf-8 -*-
'''
@File    :   MainCTR.py
@Time    :   2022/05/06 09:52:50
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import enum
import os
from pydoc import pathdirs
import numpy as np
from Models.TableOperator import (
    GetTableData,
    GetFlagData,
    GetListData
)
from PySide6.QtWidgets import (
    QVBoxLayout, 
    QMessageBox,
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
        # TODO 需要確保前一個tab的.py檔有設定好 嗎?
        # 清除第二個tab的資料內容
        self.windows.getscriptwidget.showpathflag.ClearLayout()
        self.windows.getscriptwidget.showparameter.ClearTable()
        # self.windows.getscriptwidget
        
        RightStack = self.windows.getinfowidget.RightStack
        LeftTable = self.windows.getinfowidget.LeftTable
        
        # 取得table內的資料
        ABSLData = GetTableData(LeftTable.table)
        # 參數全空白時，跳出警告視
        if ABSLData == []:
            ret = QMessageBox.warning(
                self.windows.getinfowidget, 
                'Parameter is Empty!',
                'You must load at least one parameter to use this program.',
                QMessageBox.Ok
            )
            return
        ABSLData = np.array(ABSLData)
        
        # 取得對應的list資料
        ABSLValue = []
        for idx in range(ABSLData.shape[0]):
            widgetToRemove = RightStack.widget(idx)
            value = GetListData(widgetToRemove.ParameterList)
            ABSLValue.append(value)
        # ABSLValue的形狀可能會不是array的形式
        # 會跳出VisibleDeprecationWarning，加上dtype=object就不會跳出警告
        ABSLValue = np.array(ABSLValue, dtype=object)
        
        # 確保ABSLValue的名稱包含['Path', 'Folder', 'Directory']
        # ABSLValue的個數只能有1個
        path_idx, other_idx = CheckPathFlag(ABSLData, ABSLValue)
        
        # 包含path的flag
        for idx, p_idx in enumerate(path_idx):
            FlagName = ABSLData[p_idx][0]
            FlagValue = ABSLValue[p_idx][0]
            # 預防讀入的值不是路徑
            if not os.path.exists(FlagValue):
                other_idx.append(p_idx)
                continue
            self.getscriptCTR.PathFlagGenerate(FlagName, FlagValue)
            
        # 下方的表格數據
        for idx in other_idx:
            FlagName = ABSLData[idx][0]
            FlagValue = ABSLValue[idx][0]
        self.getscriptCTR.ShowParameter(ABSLData[other_idx], 
                                        ABSLValue[other_idx])
        
        # 跳轉下一個tab
        self.windows.tabWidget.setCurrentIndex(self.windows.tabWidget.currentIndex()+1)
