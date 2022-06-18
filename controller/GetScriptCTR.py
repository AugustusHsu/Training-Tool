# -*- encoding: utf-8 -*-
'''
@File    :   GetScriptCTR.py
@Time    :   2022/05/09 16:53:26
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import numpy as np
from PySide6.QtWidgets import (
    QWidget, 
    QPushButton,
    QLabel,
    QLineEdit,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTableWidget,
    QHeaderView,
    QFileDialog,
    QTableWidgetItem,
    QAbstractItemView,
)
from PySide6 import QtCore
from PySide6.QtCore import Signal

class GetScriptController:
    def __init__(self, getscriptwidget):
        self.getscriptwidget = getscriptwidget
    
    def PathFlagGenerate(self, FlagName, FlagValue):
        HBox = QHBoxLayout()
        DownBTN = QPushButton('↓')
        DownBTN.setFixedSize(30, 30)
        PathFlagName = QLabel(FlagName + ' :')
        PathFlagName.setFixedWidth(100)
        PathFlagValue = QLineEdit(FlagValue)
        EditBTN = QPushButton('...')
        EditBTN.setFixedSize(30, 30)
        
        @QtCore.Slot()
        def OpenDirectory():
            filename = QFileDialog.getExistingDirectory(
                self.getscriptwidget.showpathflag,
                "Open file", 
                FlagValue,
                QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
            )
            PathFlagValue.setText(filename)
        EditBTN.clicked.connect(OpenDirectory)
        
        HBox.addWidget(DownBTN)
        HBox.addWidget(PathFlagName)
        HBox.addWidget(PathFlagValue)
        HBox.addWidget(EditBTN)
        
        self.getscriptwidget.showpathflag.BoxList.append(HBox)
        
        DownBTN.clicked.connect(lambda: self._press_down(HBox))
        
        self.getscriptwidget.showpathflag.VBox.addLayout(HBox)
    
    def _press_down(self, HBox):
        # 將路徑轉到下方的表格
        ParamTable = self.getscriptwidget.showparameter.table
        takeID = self.getscriptwidget.showpathflag.BoxList.index(HBox)
        del self.getscriptwidget.showpathflag.BoxList[takeID]
        layout = self.getscriptwidget.showpathflag.layout().takeAt(takeID)
        # 新增path column
        headers = [layout.itemAt(1).widget().text()[:-2]] + \
            [ParamTable.horizontalHeaderItem(r).text() for r in range(ParamTable.columnCount())]
        ParamTable.insertColumn(0)
        ParamTable.setHorizontalHeaderLabels(headers)
        # 填充ParamTable
        numRow = ParamTable.rowCount()
        for idx in range(numRow):
            ParamTable.setItem(idx, 0, QTableWidgetItem(str(layout.itemAt(2).widget().text())))
        # 刪除layout中的widget和layout
        for i in range(layout.count()):
            layout.itemAt(i).widget().deleteLater() 
        layout.deleteLater()
    
    def ShowParameter(self, FlagName, FlagValue):
        ParamTable = self.getscriptwidget.showparameter.table
        
        # 表格有幾個column
        ColumnCount = FlagName.shape[0]
        ParamTable.setColumnCount(ColumnCount)
        # column的內容、字體加粗
        ParamTable.setHorizontalHeaderLabels(list(FlagName[:,0]))
        font = ParamTable.horizontalHeader().font()
        font.setBold(True)
        ParamTable.horizontalHeader().setFont(font)
        # 沿水平方向擴展到適當尺寸
        ParamTable.horizontalHeader().setSectionResizeMode(ParamTable.columnCount()-1, 
                                                               QHeaderView.Stretch)
        
        RowCount = 1
        for values in FlagValue:
            RowCount *= len(values)
        ParamTable.setRowCount(RowCount)
        
        tmp1 = RowCount
        tmp2 = 1
        ColumnList = []
        for idx, values in enumerate(FlagValue):
            tmp1 /= len(values)
            tmplist = []
            for _ in range(int(tmp2)):
                for value in values:
                    for _ in range(int(tmp1)):
                        tmplist.append(value)
            ColumnList.append(tmplist)
            tmp2 *= len(values)
        
        RowList = []
        for idx in range(len(ColumnList[0])):
            tmplist = []
            for item in ColumnList:
                tmplist.append(item[idx])
            RowList.append(tmplist)
        for row in RowList:
            print(row)
        
        # Load Data
        for idx, row in enumerate(RowList):
            # ParamTable.setItem(idx, 0, QTableWidgetItem(str(flags[idx])))
            for idj, item in enumerate(row):
                ParamTable.setItem(idx, idj, QTableWidgetItem(str(item)))
                
            
