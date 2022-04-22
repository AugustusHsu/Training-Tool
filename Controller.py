# -*- encoding: utf-8 -*-
'''
@File    :   Controller.py
@Time    :   2022/04/14 23:43:20
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import os
from view.MainWindow import MainWindow
from view.GetInfoWindow.SubWidget import RightListWidget
from PySide6.QtWidgets import (
    QFileDialog,
    QFormLayout,
    QLineEdit,
    QWidget,
    QInputDialog,
    QMessageBox,
    QTableWidgetItem
)
from view.Dialog import (
    NoSelectDialog_edit,
    NoSelectDialog_delete,
    ParameterEmpty
)
from PySide6 import QtCore
from utils import GetABSLFlags, ParseDict

class GetInfoController:
    def __init__(self):
        self.windows = MainWindow()
        self._SetupGetInfoWidget(self.windows.getinfowidget)
        
        self.windows.show()
    
    def _SetupOpenFileWidget(self, openfilewidget):
        @QtCore.Slot()
        def OpenPyFile():
            filename, _ = QFileDialog.getOpenFileName(
                openfilewidget,
                "Open file", 
                "./",
                "Python Files (*.py);;All Files (*)"
            )
            openfilewidget.pyfile_path.setText(filename)
        openfilewidget.PressOpen.connect(OpenPyFile)
    
    def _SetupSelectPythonWidget(self, selectpythonwidget):
        @QtCore.Slot()
        def OpenPython():
            filename, _ = QFileDialog.getOpenFileName(
                selectpythonwidget,
                "Open file", 
                "\\home",
                # "Python Files (*.py);;All Files (*)"
                "All Files (*);;Python Files (*.py)"
            )
            selectpythonwidget.python_path.setText(filename)
        selectpythonwidget.PressOpen.connect(OpenPython)
    
    # TODO Add the abls parameter loader
    def _SetupGetInfoWidget(self, getinfowidget):
        self._SetupOpenFileWidget(getinfowidget.openfilewidget)
        self._SetupSelectPythonWidget(getinfowidget.selectpythonwidget)
        @QtCore.Slot(str, str)
        def load_parameter(msg1, msg2):
            print('Path: ' + msg1)
            print('Path: ' + msg2)
            # FIXME 預防空白的輸入
            # FIXME load新的py要clear table和list
            
            # DEBUG 預設的路徑與py檔來讀入FLAG_DICT
            FLAG_DICT = GetABSLFlags('python', 'test_file/test-absl.py')
            flags, value_list, attr_list = ParseDict(FLAG_DICT)
            self._ShowData([flags, value_list, attr_list], 
                           getinfowidget.RightStack,
                           getinfowidget.LeftTable)
            
        getinfowidget.PressOK.connect(load_parameter)
        getinfowidget.ClossBTN.connect(self._exit)
        
    def _ShowData(self, FlagData, RightStack, LeftTable):
        flags, value_list, attr_list = FlagData
        # 用測試資料創建左邊list資料、添加右邊stack資料
        LeftTable.table.setRowCount(len(flags))
        
        # Load Data
        for idx, row in enumerate(attr_list):
            LeftTable.table.setItem(idx, 0, QTableWidgetItem(str(flags[idx])))
            for idj, item in enumerate(row):
                LeftTable.table.setItem(idx, idj+1, QTableWidgetItem(str(item)))
        
        def stackUI(rightitem):
            stack = RightListWidget(RightStack)
            for item in rightitem:
                stack.ParameterList.addItem(str(item))
            # 賦予右邊stack按鈕的功能
            self._SetupStackItem(stack)
            return stack
        for rightitem in value_list:
            right_widget = stackUI(rightitem)
            RightStack.addWidget(right_widget)
    
    
    def _SetupRightList(self, RightStack):
        pass
    
    def _SetupLeftTable(self, lefttablewidget):
        pass
        
    def _SetupLeftList(self, LeftTable, RightStack): 
        @QtCore.Slot()
        def _press_edit():
            list_idx = LeftTable.ParameterList.currentRow()
            sel_items = LeftTable.ParameterList.selectedItems()
            if list_idx == -1:
                NoSelectDialog_edit(self.windows)
            else: 
                text, ok = QInputDialog.getText(LeftTable, 
                                                'Edit Parameter', 
                                                'Enter a argument:',
                                                text=str(sel_items[0].text()))
                if ok and text.strip() == '':
                    ParameterEmpty(self.windows)
                    LeftTable.PressEdit.emit()
                elif ok:
                    # TODO 排除重複的名稱，或當名稱重複跳出警告
                    sel_items = LeftTable.ParameterList.selectedItems()
                    for item in sel_items:
                        item.setText(str(text))
        @QtCore.Slot()
        def _press_add():
            text, ok = QInputDialog.getText(LeftTable, 
                                            'Add Parameter', 
                                            'Enter a argument:')
            if ok and text.strip() == '':
                ParameterEmpty(self.windows)
                LeftTable.PressAdd.emit()
            elif ok:
                LeftTable.ParameterList.addItem(str(text))
                right_widget = RightListWidget(RightStack)
                # 賦予右邊stack按鈕的功能
                self._SetupStackItem(right_widget)
                RightStack.addWidget(right_widget)
        @QtCore.Slot()
        def _press_delete():
            list_idx = LeftTable.ParameterList.currentRow()
            if list_idx == -1:
                NoSelectDialog_delete(self.windows)
            else:
                sel_items = LeftTable.ParameterList.selectedItems()
                if sel_items:
                    for item in sel_items:
                        idx = LeftTable.ParameterList.row(item)
                        LeftTable.ParameterList.takeItem(idx)
                        widgetToRemove = RightStack.widget(idx)
                        RightStack.removeWidget(widgetToRemove)
        
        LeftTable.PressEdit.connect(_press_edit)
        LeftTable.PressAdd.connect(_press_add)
        LeftTable.PressDelete.connect(_press_delete)
        
    def _SetupStackItem(self, stack):
        stack.PressEdit
        stack.PressAdd
        stack.PressDelete
        @QtCore.Slot()
        def _press_edit():
            list_idx = stack.ParameterList.currentRow()
            sel_items = stack.ParameterList.selectedItems()
            if list_idx == -1:
                NoSelectDialog_edit(self.windows)
            else:
                text, ok = QInputDialog.getText(stack, 
                                                'Edit Parameter', 
                                                'Enter a argument:',
                                                text=str(sel_items[0].text()))
                if ok and text.strip() == '':
                    ParameterEmpty(self.windows)
                    stack.PressEdit.emit()
                elif ok:
                    # TODO 排除重複的名稱，或當名稱重複跳出警告
                    for item in sel_items:
                        item.setText(str(text))
        @QtCore.Slot()
        def _press_add():
            text, ok = QInputDialog.getText(stack, 
                                            'Add Parameter', 
                                            'Enter a argument:')
            if ok and text.strip() == '':
                ParameterEmpty(self.windows)
                stack.PressAdd.emit()
            elif ok:
                stack.ParameterList.addItem(str(text))
        @QtCore.Slot()
        def _press_delete():
            list_idx = stack.ParameterList.currentRow()
            if list_idx == -1:
                NoSelectDialog_delete(self.windows)
            else:
                sel_items = stack.ParameterList.selectedItems()
                if sel_items:
                    for item in sel_items:
                        idx = stack.ParameterList.row(item)
                        stack.ParameterList.takeItem(idx)
        
        stack.PressEdit.connect(_press_edit)
        stack.PressAdd.connect(_press_add)
        stack.PressDelete.connect(_press_delete)

    @QtCore.Slot()
    def _exit(self):
        self.windows.close()

