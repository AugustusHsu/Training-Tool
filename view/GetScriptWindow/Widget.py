# -*- encoding: utf-8 -*-
'''
@File    :   Widget.py
@Time    :   2022/05/06 16:33:33
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from View.GetScriptWindow.SubWidget import ShowPathFlagWidget
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QCheckBox,
    QStackedWidget
)
from PySide6.QtCore import Signal

class GetSciptWidget(QWidget):
    PressOK = Signal(str, str)
    ClossBTN = Signal()
    def __init__(self, parent=None):
        super(GetSciptWidget, self).__init__(parent)
        self.showpathflag = ShowPathFlagWidget(self)
        self.close_btn = QPushButton('close', self)
        self._setupUI()
    
    def _setupUI(self):
        VBox = QVBoxLayout()
        VBox.addWidget(self.showpathflag)
        
        BtnBox = QHBoxLayout()
        BtnBox.addStretch(1)
        BtnBox.addWidget(self.close_btn)
        VBox.addLayout(BtnBox)
        self.close_btn.clicked.connect(self._press_close)
        self.setLayout(VBox)
        
    def _press_close(self):
        self.ClossBTN.emit()
