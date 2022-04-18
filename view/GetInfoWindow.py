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
)
from view.GetInfoWidget import GetInfoWidget
from view.GetInfoWidget import GetInfoWidget

class GetInfoWindow(QMainWindow):
    def __init__(self):
        super(GetInfoWindow, self).__init__()
        self._widget = QWidget()
        # 設置視窗的初始位置跟大小、應用程式的標題
        self.setGeometry(600,300,500,50)
        self.setWindowTitle('StackedWidget 例子')
        self.getinfowidget = GetInfoWidget(self)
        self.setCentralWidget(self.getinfowidget)