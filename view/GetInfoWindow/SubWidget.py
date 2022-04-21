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
    QSizePolicy,
    QInputDialog
)
from PySide6.QtCore import Signal
from PySide6 import QtCore
from PySide6 import QtGui

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

class ShowParameterWidget(QWidget):
    def __init__(self, parent=None):
        super(ShowParameterWidget, self).__init__(parent)
        self.LeftList = ParameterListWidget(self)
        self.RightStack = QStackedWidget(self)
        self._setupUI()
        
    def _setupUI(self):
        #水平布局，添加部件到布局中
        HBox=QHBoxLayout()
        HBox.addWidget(self.LeftList)
        HBox.addWidget(self.RightStack)
        
        # TODO 可用滑動調整比例
        # 左右布局的比例
        HBox.setStretch(0, 1)
        HBox.setStretch(1, 2)

        self.setLayout(HBox)
 
        self.LeftList.ParameterList.currentRowChanged.connect(self.display)
        
    def display(self, index):
        # 設置當前可視選項的索引
        self.RightStack.setCurrentIndex(index)

class ParameterListWidget(QWidget):
    PressEdit = Signal()
    PressAdd = Signal()
    PressDelete = Signal()
    def __init__(self, parent=None):
        super(ParameterListWidget, self).__init__(parent)
        self.ParameterList = QListWidget()
        self._setupUI()
        
    def _setupUI(self):
        self.edit_btn = QPushButton(' ', self)
        self.edit_btn.setIcon(QIcon('./media/edit.png'))
        self.add_btn = QPushButton('+', self)
        self.delete_btn = QPushButton('-', self)
        self.edit_btn.setFixedSize(30, 30)
        self.add_btn.setFixedSize(30, 30)
        self.delete_btn.setFixedSize(30, 30)
        BtnBox=QHBoxLayout()
        BtnBox.addStretch(1)
        BtnBox.addWidget(self.edit_btn)
        BtnBox.addWidget(self.add_btn)
        BtnBox.addWidget(self.delete_btn)
        VBox=QVBoxLayout()
        VBox.addWidget(self.ParameterList)
        VBox.addLayout(BtnBox)
        self.setLayout(VBox)
        
        self.edit_btn.clicked.connect(self._press_edit)
        self.add_btn.clicked.connect(self._press_add)
        self.delete_btn.clicked.connect(self._press_delete)
        
    def _press_edit(self):
        self.PressEdit.emit()
    
    def _press_add(self):
        self.PressAdd.emit()
        
    def _press_delete(self):
        self.PressDelete.emit()
        










