# -*- encoding: utf-8 -*-
'''
@File    :   GetInfoWindow.py
@Time    :   2022/04/14 23:44:16
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from PySide6.QtWidgets import (
    QWidget, 
    QMainWindow,
    QTabWidget,
    QTextEdit
)
from PySide6 import QtCore
from view.GetInfoWindow.Widget import GetInfoWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self._widget = QWidget()
        # 設置視窗的初始位置跟大小、應用程式的標題
        self.setGeometry(200,300,640*1.5,360*1.5)
        self.setWindowTitle('StackedWidget 例子')
        self.getinfowidget = GetInfoWidget(self)
        self.tabWidget = QTabWidget(self)
        self._SetupUI()
        
    def _SetupUI(self):
        self.tabWidget.addTab(self.getinfowidget, "OpenFile")
        
        self.setCentralWidget(self.tabWidget)