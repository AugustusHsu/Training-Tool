# -*- encoding: utf-8 -*-
'''
@File    :   MainController.py
@Time    :   2022/05/06 09:52:50
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from view import MainWindow
from controller import GetInfoController
from PySide6 import QtCore

class MainController:
    def __init__(self):
        self.windows = MainWindow()
        self.getinfoCTR = GetInfoController(self.windows.getinfowidget)
        self.windows.getinfowidget.ClossBTN.connect(self._exit)
        self.windows.show()
        
    @QtCore.Slot()
    def _exit(self):
        self.windows.close()
