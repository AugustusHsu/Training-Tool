# -*- encoding: utf-8 -*-
'''
@File    :   GetScriptCTR.py
@Time    :   2022/05/09 16:53:26
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import numpy as np
from PySide6.QtWidgets import (
    QWidget, 
    QPushButton,
    QLabel,
    QLineEdit,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTableWidget,
    QHeaderView,
)
from PySide6 import QtCore
from PySide6.QtCore import Signal

class GetScriptController:
    def __init__(self, getscriptwidget):
        self._SetupShowPathFlag(getscriptwidget.showpathflag)
    
    # TODO 取得table的參數
    @QtCore.Slot(list)
    def GetTableData(self, Arr):
        print(np.array(Arr))
    
    def _SetupShowPathFlag(self, showpathflag):
        
        # TODO 用for迴圈創建和路徑相關的物件
        HBox = QHBoxLayout()
        PathFlagName = QLabel("Test Path:")
        PathFlagName.setFixedWidth(100)
        PathFlagValue = QLineEdit()
        EditBox = QPushButton('Edit')
        HBox.addWidget(PathFlagName)
        HBox.addWidget(PathFlagValue)
        HBox.addWidget(EditBox)
        
        showpathflag.VBox.addLayout(HBox)
    
    def _addPathFlag(self, flag_data):
        pass        