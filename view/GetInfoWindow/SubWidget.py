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
    QInputDialog,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView
)
from utils import GetABSLFlags, ParseDict
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

class RightListWidget(QWidget):
    PressEdit = Signal()
    PressAdd = Signal()
    PressDelete = Signal()
    def __init__(self, parent=None):
        super(RightListWidget, self).__init__(parent)
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
        BtnBox = QHBoxLayout()
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

class LeftTableWidget(QWidget):
    PressEdit = Signal()
    PressAdd = Signal()
    PressDelete = Signal()
    def __init__(self, parent=None):
        super(LeftTableWidget, self).__init__(parent)
        # 設置視窗的初始位置跟大小、應用程式的標題
        # self.setGeometry(200,300,640*1.5,360*1.5)
        self.table = QTableWidget(self)
        self._setupUI()
        
        # TODO RemoveRow currentRow() (slot)removeRow()
        
    def _setupUI(self):
        VBox=QVBoxLayout()
        # 表格有5個column
        self.table.setColumnCount(5)
        # column的文字
        # FIXME default跟current不用，要刪除
        self.table.setHorizontalHeaderLabels(['flag', 'file', 'type', 
                                              'enum_value', 'meaning'])
        # self.table.horizontalHeader().setSectionResizeMode(4,QHeaderView.Stretch)
        # 設定最後一個column延伸至最大
        # self.table.horizontalHeader().setStretchLastSection(True)
        # 沿水平方向擴展到符合item內容
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 沿水平方向擴展到適當尺寸
        self.table.horizontalHeader().setSectionResizeMode(self.table.columnCount()-1, 
                                                           QHeaderView.Stretch)
        VBox.addWidget(self.table)
        
        self.edit_btn = QPushButton(' ', self)
        self.edit_btn.setIcon(QIcon('./media/edit.png'))
        self.add_btn = QPushButton('+', self)
        self.delete_btn = QPushButton('-', self)
        self.edit_btn.setFixedSize(30, 30)
        self.add_btn.setFixedSize(30, 30)
        self.delete_btn.setFixedSize(30, 30)
        BtnBox = QHBoxLayout()
        BtnBox.addStretch(1)
        BtnBox.addWidget(self.edit_btn)
        BtnBox.addWidget(self.add_btn)
        BtnBox.addWidget(self.delete_btn)
        
        self.edit_btn.clicked.connect(self._press_edit)
        self.add_btn.clicked.connect(self._press_add)
        self.delete_btn.clicked.connect(self._press_delete)
        
        VBox.addLayout(BtnBox)
        self.setLayout(VBox)
        
        # # data
        # flags, attr_list, value_list = self.get_data()
        # self.table.setRowCount(len(value_list))
        
        # for idx, row in enumerate(value_list):
        #     for idj, item in enumerate(row):
        #         self.table.setItem(idx, idj, QTableWidgetItem(str(item)))
        
    def get_data(self):
        # python_file = 'C:\\Users\\jimhs\\anaconda3\\envs\\pyside6\\python.exe'
        python_file = 'python'
        ABSL_DICT = GetABSLFlags(python_file, 'test_file/test-absl.py')
        flags, attr_list, value_list = ParseDict(ABSL_DICT)
        return flags, attr_list, value_list
    
    def test_print(self, row, _):
        print(row)
        
    def _press_edit(self):
        self.PressEdit.emit()
    
    def _press_add(self):
        self.PressAdd.emit()
        
    def _press_delete(self):
        for item in self.table.selectedRanges():
            print(item.topRow(), item.leftColumn(), 
                  item.bottomRow(), item.rightColumn())
        if self.table.selectedRanges() == []:
            print('None')
        self.PressDelete.emit()









