# -*- encoding: utf-8 -*-
'''
@File    :   GetScriptCTR.py
@Time    :   2022/05/09 16:53:26
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
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

class GetScriptController:
    def __init__(self, getscriptwidget):
        self._SetupShowPathFlag(getscriptwidget.showpathflag)
    
    # TODO 取得table的參數
    
    def _SetupShowPathFlag(self, showpathflag):
        self.PathFlag = []
        
        # TODO 用for迴圈創建和路徑相關的物件
        HBox = QHBoxLayout()
        PathFlagName = QLabel("Test Path:")
        PathFlagName.setFixedWidth(100)
        PathFlagValue = QLineEdit()
        EditBox = QPushButton('Edit')
        showpathflag.PathFlag.append([PathFlagName, PathFlagValue, EditBox])
        HBox.addWidget(PathFlagName)
        HBox.addWidget(PathFlagValue)
        HBox.addWidget(EditBox)
        
        showpathflag.VBox.addLayout(HBox)
    
    def _addPathFlag(self, flag_data):
        pass        