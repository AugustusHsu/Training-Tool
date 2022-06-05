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
    QFileDialog
)
from PySide6 import QtCore
from PySide6.QtCore import Signal

class GetScriptController:
    def __init__(self, getscriptwidget):
        self.getscriptwidget = getscriptwidget
        self._SetupShowPathFlag(getscriptwidget.showpathflag)
    
    def PathFlagGenerate(self, FlagName, FlagValue):
        HBox = QHBoxLayout()
        PathFlagName = QLabel(FlagName + ' :')
        PathFlagName.setFixedWidth(100)
        PathFlagValue = QLineEdit(FlagValue)
        EditBTN = QPushButton('...')
        EditBTN.setFixedSize(30, 30)
        
        @QtCore.Slot()
        def OpenPython():
            filename, _ = QFileDialog.getOpenFileName(
                self.getscriptwidget.showpathflag,
                "Open file", 
                FlagValue,
                "Exe Files (*.exe);;All Files (*)"
                # "All Files (*);;Python Files (*.py)"
            )
        EditBTN.clicked.connect(OpenPython)
        
        HBox.addWidget(PathFlagName)
        HBox.addWidget(PathFlagValue)
        HBox.addWidget(EditBTN)
        
        self.getscriptwidget.showpathflag.VBox.addLayout(HBox)
    
    def _SetupShowPathFlag(self, showpathflag):
        pass
    
    def _addPathFlag(self, flag_data):
        pass        