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
    QAbstractItemView,
)
from PySide6.QtCore import Signal
from PySide6 import QtCore

class ShowPathFlagWidget(QWidget):
    # SelectPython = Signal()
    def __init__(self, parent=None):
        super(ShowPathFlagWidget, self).__init__(parent)
        self.BoxList = []
        self._setupUI()
    
    def _setupUI(self):
        self.VBox = QVBoxLayout()
        self.setLayout(self.VBox)
        
    def ClearLayout(self):
        while self.layout().count():
            item = self.layout().takeAt(0)
            item.deleteLater()
        self.BoxList = []
        
class ShowParameterWidget(QWidget):
    def __init__(self, parent=None):
        super(ShowParameterWidget, self).__init__(parent)
        self.table = QTableWidget(self)
        # 沿水平方向擴展到符合item內容
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # # 選中為選中整行
        # ParamTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._setupUI()
    
    def _setupUI(self):
        VBox = QVBoxLayout()
        VBox.addWidget(self.table)
        self.setLayout(VBox)
    
    def ClearTable(self):
        self.table.setRowCount(0)