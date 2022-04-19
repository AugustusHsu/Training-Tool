# -*- encoding: utf-8 -*-
'''
@File    :   Controller.py
@Time    :   2022/04/14 23:43:20
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import os
from view.MainWindow import MainWindow
from PySide6.QtWidgets import (
    QFileDialog,
)
from PySide6 import QtCore

class GetInfoController:
    def __init__(self):
        self.windows = MainWindow()
        self._SetupGetInfoWidget(self.windows.getinfowidget)
        
        self.windows.show()
        
    def _SetupGetInfoWidget(self, getinfowidget):
        @QtCore.Slot(str, str)
        def print_path(msg1, msg2):
            print('Path: ' + msg1)
            print('Path: ' + msg2)
            
        @QtCore.Slot()
        def OpenPyFile():
            filename, _ = QFileDialog.getOpenFileName(
                getinfowidget.openfilewidget,
                "Open file", 
                "./",
                "Python Files (*.py);;All Files (*)"
            )
            getinfowidget.openfilewidget.pyfile_path.setText(filename)
        
        @QtCore.Slot()
        def OpenPython():
            filename, _ = QFileDialog.getOpenFileName(
                getinfowidget.selectpythonwidget,
                "Open file", 
                "./",
                # "Python Files (*.py);;All Files (*)"
                "All Files (*);;Python Files (*.py)"
            )
            getinfowidget.selectpythonwidget.python_path.setText(filename)
            
        getinfowidget.openfilewidget.PressOpen.connect(OpenPyFile)
        getinfowidget.selectpythonwidget.PressOpen.connect(OpenPython)
        getinfowidget.PressOK.connect(print_path)
        
        