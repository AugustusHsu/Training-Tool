# -*- encoding: utf-8 -*-
'''
@File    :   GetInfoWidget.py
@Time    :   2022/04/14 23:45:05
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import numpy as np
from View.GetInfoWindow.SubWidget import (
    OpenFileWidget, 
    SelectPythonWidget,
    LeftTableWidget
)
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QCheckBox,
    QStackedWidget
)
from PySide6.QtCore import Signal

class GetInfoWidget(QWidget):
    PressOK = Signal(str, str)
    ClossBTN = Signal()
    GenBTN = Signal()
    SaveBTN = Signal()
    LoadBTN = Signal()
    ClearBTN = Signal()
    def __init__(self, parent=None):
        super(GetInfoWidget, self).__init__(parent)
        self.openfilewidget = OpenFileWidget(self)
        self.selectpythonwidget = SelectPythonWidget(self)
        self.RightStack = QStackedWidget(self)
        self.LeftTable = LeftTableWidget(self)
        self._setupUI()
        
    def _setupUI(self):
        f_layout = QVBoxLayout()
        f_layout.addWidget(self.selectpythonwidget)
        f_layout.addWidget(self.openfilewidget)
        
        ParameterBox = QHBoxLayout()
        ParameterBox.addWidget(self.LeftTable)
        ParameterBox.addWidget(self.RightStack)
        # TODO 可用滑動調整比例
        # 左右布局的比例
        ParameterBox.setStretch(0, 5)
        ParameterBox.setStretch(1, 2)
        f_layout.addLayout(ParameterBox)
        
        self.LeftTable.table.cellClicked.connect(self.display)
        
        self.gen_btn = QPushButton('generate', self)
        self.close_btn = QPushButton('close', self)
        self.save_btn = QPushButton('save', self)
        self.load_btn = QPushButton('load', self)
        # TODO 加一個clear table的按鈕
        self.clear_btn = QPushButton('clear', self)
        # self.checkbox = QCheckBox('show', self)
        BtnBox = QHBoxLayout()
        BtnBox.addWidget(self.save_btn)
        BtnBox.addWidget(self.load_btn)
        BtnBox.addStretch(1)
        BtnBox.addWidget(self.clear_btn)
        BtnBox.addWidget(self.gen_btn)
        BtnBox.addWidget(self.close_btn)
        
        f_layout.addLayout(BtnBox)
        
        self.setLayout(f_layout)
        self.save_btn.clicked.connect(self._press_save)
        self.load_btn.clicked.connect(self._press_load)
        self.openfilewidget.ok_btn.clicked.connect(self._press_ok)
        self.clear_btn.clicked.connect(self._press_clear)
        self.gen_btn.clicked.connect(self._press_gen)
        self.close_btn.clicked.connect(self._press_close)
        
    def _press_ok(self):
        self.PressOK.emit(self.selectpythonwidget.python_path.text(),
                          self.openfilewidget.pyfile_path.text())
    
    def _press_close(self):
        self.ClossBTN.emit()
    
    def _press_gen(self):
        self.GenBTN.emit()
        
    def _press_save(self):
        self.SaveBTN.emit()
        
    def _press_load(self):
        self.LoadBTN.emit()
        
    def _press_clear(self):
        self.ClearBTN.emit()
        
    def display(self, index, column):
        # 設置當前可視選項的索引
        self.RightStack.setCurrentIndex(index)