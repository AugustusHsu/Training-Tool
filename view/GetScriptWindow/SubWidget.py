# -*- encoding: utf-8 -*-
'''
@File    :   SubWidget.py
@Time    :   2022/05/06 16:33:55
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from PySide6.QtGui import QIcon
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
from PySide6.QtCore import Signal

class ShowPathFlagWidget(QWidget):
    SelectPython = Signal()
    def __init__(self, parent=None):
        super(ShowPathFlagWidget, self).__init__(parent)
        self._setupUI()
    
    def _setupUI(self):
        self.PathFlag = []
        self.VBox = QVBoxLayout()
        
        # DEBUG 測試一個PathFlag
        HBox = QHBoxLayout()
        PathFlagName = QLabel("Test Path:")
        PathFlagName.setFixedWidth(100)
        PathFlagValue = QLineEdit()
        EditBox = QPushButton('Edit')
        HBox.addWidget(PathFlagName)
        HBox.addWidget(PathFlagValue)
        HBox.addWidget(EditBox)
        self.PathFlag.append([PathFlagName, PathFlagValue, EditBox])
        
        self.VBox.addLayout(HBox)
        self.setLayout(self.VBox)
        
