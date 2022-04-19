# -*- encoding: utf-8 -*-
'''
@File    :   GetInfoWidget.py
@Time    :   2022/04/14 23:45:05
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from view.GetInfoWindow.SubWidget import (
    OpenFileWidget, 
    SelectPythonWidget,
    ShowParameterWidget,
    ParameterListWidget
)
from PySide6.QtWidgets import (
    QWidget, 
    QVBoxLayout,
)
from PySide6.QtCore import Signal

class GetInfoWidget(QWidget):
    PressOK = Signal(str, str)
    def __init__(self, parent=None):
        super(GetInfoWidget, self).__init__(parent)
        self.openfilewidget = OpenFileWidget(self)
        self.selectpythonwidget = SelectPythonWidget(self)
        self.showparameter = ShowParameterWidget(self)
        self._setupUI()
        
    def _setupUI(self):
        f_layout = QVBoxLayout()
        f_layout.addWidget(self.selectpythonwidget)
        f_layout.addWidget(self.openfilewidget)
        f_layout.addWidget(self.showparameter)
        
        self.setLayout(f_layout)
        self.openfilewidget.ok_btn.clicked.connect(self._press_ok)
        
    def _press_ok(self):
        self.PressOK.emit(self.selectpythonwidget.python_path.text(),
                          self.openfilewidget.pyfile_path.text())