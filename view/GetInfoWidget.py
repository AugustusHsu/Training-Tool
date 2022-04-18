# -*- encoding: utf-8 -*-
'''
@File    :   GetInfoWidget.py
@Time    :   2022/04/14 23:45:05
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from view.OpenFileWidget import OpenFileWidget
from PySide6.QtWidgets import (
    QWidget, 
    QHBoxLayout,
)

class GetInfoWidget(QWidget):
    def __init__(self, parent=None):
        super(GetInfoWidget, self).__init__(parent)
        self.openfilewidget = OpenFileWidget(self)
        self._setupUI()
        
    def _setupUI(self):
        f_layout = QHBoxLayout()
        f_layout.addWidget(self.openfilewidget)
        self.setLayout(f_layout)