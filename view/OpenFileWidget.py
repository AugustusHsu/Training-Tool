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
    QFileDialog,
    QHBoxLayout,
    QLineEdit,
)

class OpenFileWidget(QWidget):
    def __init__(self, parent=None):
        super(OpenFileWidget, self).__init__(parent)
        # 目的路徑
        # 設置視窗初始位置和大小
        self.setFixedHeight(42)
        self._setupUI()
        self._SetupOpenFile()
        
    def _setupUI(self):
        self.pyfile_title = QLabel('Python File :')
        self.pyfile_path = QLineEdit()
        self.get_pyfile_btn = QPushButton('open')
        self.get_pyfile_btn.setIcon(QIcon('./media/import.svg'))
        self.ok_btn = QPushButton('OK')
        f_layout = QHBoxLayout()
        f_layout.addWidget(self.pyfile_title)
        f_layout.addWidget(self.pyfile_path)
        f_layout.addWidget(self.get_pyfile_btn)
        f_layout.addWidget(self.ok_btn)
        # g_layout = QGridLayout()
        # g_layout.addLayout(openfile, 0, 0)
        self.setLayout(f_layout)
    
    def _SetupOpenFile(self):
        self.get_pyfile_btn.clicked.connect(self.OpenFileNameDialog)
        
    def OpenFileNameDialog(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Open file", 
                                                         "./",
                                                         "Python Files (*.py);;All Files (*)")
        # print(filename, filetype)
        self.pyfile_path.setText(filename)
        
    def OpenFolderDialog(self):
        filename = QFileDialog.getExistingDirectory(self,
                                                    "Open file",
                                                    "./",)
        # print(filename)
        self.pyfile_path.setText(filename)