# -*- encoding: utf-8 -*-
'''
@File    :   Controller.py
@Time    :   2022/04/14 23:43:20
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import os
from view.GetInfoWindow import GetInfoWindow

class GetInfoController:
    def __init__(self):
        self.windows = GetInfoWindow()
        self._SetupOpenFileWidget(self.windows.getinfowidget.openfilewidget)
        
        self.windows.show()
    
    def _SetupOpenFileWidget(self, openfilewideget):
        def _load_path():
            python_path = openfilewideget.pyfile_path.text()
            
            print(os.path.isfile(python_path) and python_path[-3:] == '.py')
            
        openfilewideget.ok_btn.clicked.connect(_load_path)