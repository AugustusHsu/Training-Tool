# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/04/14 23:42:53
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import sys
from Controller import GetInfoController
from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ctr = GetInfoController()
    app.exec_()