# -*- encoding: utf-8 -*-
'''
@File    :   MainCTR.py
@Time    :   2022/05/06 09:52:50
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from View import MainWindows
from Controller import GetInfoController
from PySide6 import QtCore

class MainController:
    def __init__(self):
        self.windows = MainWindows()
        self.getinfoCTR = GetInfoController(self.windows.getinfowidget)
        self.windows.getinfowidget.GenBTN.connect(self._gen)
        self.windows.getinfowidget.ClossBTN.connect(self._exit)
        self.windows.show()
        
    @QtCore.Slot()
    def _exit(self):
        self.windows.close()
        
    @QtCore.Slot()
    def _gen(self):
        print('gen')
        # TODO 取得所需的參數，跳轉下一個tab
