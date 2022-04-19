# -*- encoding: utf-8 -*-
'''
@File    :   OpenFileWidget.py
@Time    :   2022/04/14 23:41:09
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
    QStackedWidget,
    QListWidget,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QSpacerItem,
    QSizePolicy
)
from PySide6.QtCore import Signal
from PySide6 import QtCore

class SelectPythonWidget(QWidget):
    PressOpen = Signal()
    def __init__(self, parent=None):
        super(SelectPythonWidget, self).__init__(parent)
        # 設置widget的高度
        self.setFixedHeight(42)
        self._setupUI()

    def _setupUI(self):
        self.python_title = QLabel('Choose Python :')
        self.python_title.setFixedWidth(90)
        self.python_path = QLineEdit()
        self.select_python_btn = QPushButton('select')
        self.select_python_btn.setIcon(QIcon('./media/python_logo.svg'))
        
        HBox = QHBoxLayout()
        HBox.addWidget(self.python_title)
        HBox.addWidget(self.python_path)
        HBox.addWidget(self.select_python_btn)
        
        self.setLayout(HBox)

        self.select_python_btn.clicked.connect(self._press_open)
    
    def _press_open(self):
        self.PressOpen.emit()
        
class OpenFileWidget(QWidget):
    PressOpen = Signal()
    def __init__(self, parent=None):
        super(OpenFileWidget, self).__init__(parent)
        # 設置widget的高度
        self.setFixedHeight(42)
        self._setupUI()
        
    def _setupUI(self):
        self.pyfile_title = QLabel('Python File :')
        self.pyfile_title.setFixedWidth(90)
        self.pyfile_path = QLineEdit()
        self.get_pyfile_btn = QPushButton('Open')
        self.get_pyfile_btn.setIcon(QIcon('./media/import.svg'))
        self.ok_btn = QPushButton('Get Info')
        
        HBox = QHBoxLayout()
        HBox.addWidget(self.pyfile_title)
        HBox.addWidget(self.pyfile_path)
        HBox.addWidget(self.get_pyfile_btn)
        HBox.addWidget(self.ok_btn)
        
        self.setLayout(HBox)

        self.get_pyfile_btn.clicked.connect(self._press_open)
    
    def _press_open(self):
        self.PressOpen.emit()










