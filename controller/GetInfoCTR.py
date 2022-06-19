# -*- encoding: utf-8 -*-
'''
@File    :   GetInfoCTR.py
@Time    :   2022/05/06 09:55:49
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import os
import json
from datetime import datetime
from Models.TableOperator import (
    GetFlagData,
    GetListData,
    GetTableData
)
from View.GetInfoWindow.SubWidget import RightListWidget
from PySide6.QtWidgets import (
    QFileDialog,
    QInputDialog,
    QMessageBox,
    QTableWidgetItem
)
from PySide6 import QtCore
from Models.utils import GetABSLFlags, ParseDict, ParseJsonParameter

class GetInfoController:
    def __init__(self, getinfowidget):
        self.getinfowidget = getinfowidget
        self._SetupGetInfoWidget(self.getinfowidget)
    
    def _SetupGetInfoWidget(self, getinfowidget):
        self._SetupOpenFileWidget(getinfowidget.openfilewidget)
        self._SetupSelectPythonWidget(getinfowidget.selectpythonwidget)
        @QtCore.Slot(str, str)
        def load_parameter(msg1, msg2):
            # FIXME 預防空白的輸入、確認檔案存在
            print('Path: ' + msg1)
            print('Path: ' + msg2)
            
            # DEBUG 預設的路徑與py檔來讀入FLAG_DICT
            TestABSLFile = 'test_file/test-absl.py'
            FLAG_DICT = GetABSLFlags('python', TestABSLFile)
            # FLAG_DICT = GetABSLFlags('python', os.path.relpath(msg2))
            getinfowidget.openfilewidget.pyfile_path.setText(os.path.abspath(TestABSLFile))
            # FIXME 不可執行時跳錯誤，加Log
            # FLAG_DICT = GetABSLFlags(msg1, os.path.relpath(msg2))
            self._ClearTable(getinfowidget.RightStack, getinfowidget.LeftTable.table)
            flags, value_list, attr_list = ParseDict(FLAG_DICT)
            self._ShowData([flags, value_list, attr_list], 
                           getinfowidget.RightStack,
                           getinfowidget.LeftTable)
            
        self._SetupLeftTable(getinfowidget.LeftTable, getinfowidget.RightStack)
        getinfowidget.PressOK.connect(load_parameter)
        self._SaveParameter(getinfowidget)
        self._LoadParameter(getinfowidget)
        
    def _SetupOpenFileWidget(self, openfilewidget):
        @QtCore.Slot()
        def OpenPyFile():
            filename, _ = QFileDialog.getOpenFileName(
                openfilewidget,
                "Open .py File", 
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
                "Select Python", 
                # TODO 預設路徑需要更改
                "C:\\Users\\jimhsu\\Miniconda3\\envs\\GUI",
                "Exe Files (*.exe);;All Files (*)"
                # "All Files (*);;Python Files (*.py)"
            )
            selectpythonwidget.python_path.setText(filename)
        selectpythonwidget.SelectPython.connect(OpenPython)
    
    def _ClearTable(self, RightStack, LeftTable):
        n_row = LeftTable.rowCount()
        for row in reversed(range(n_row)):
            widgetToRemove = RightStack.widget(row)
            RightStack.removeWidget(widgetToRemove)
        LeftTable.clearContents()
        
    def _ShowData(self, FlagData, RightStack, LeftTable):
        flags, value_list, attr_list = FlagData
        # 用測試資料創建左邊list資料、添加右邊stack資料
        LeftTable.table.setRowCount(len(flags))
        
        # Load Data
        for idx, row in enumerate(attr_list):
            LeftTable.table.setItem(idx, 0, QTableWidgetItem(str(flags[idx])))
            for idj, item in enumerate(row):
                LeftTable.table.setItem(idx, idj+1, QTableWidgetItem(str(item)))
        self._SetupRightList(RightStack, value_list)
    
    def _SetupRightList(self, RightStack, value_list):
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
        
    def _SetupStackItem(self, stack):
        @QtCore.Slot()
        def _press_edit():
            list_idx = stack.ParameterList.currentRow()
            current_item = stack.ParameterList.item(list_idx)
            print()
            if list_idx == -1:
                ret = QMessageBox.warning(
                    self.getinfowidget, 
                    'No Select Parameter!',
                    'You need to select one parameter to edit it.',
                    QMessageBox.Ok
                )
            else:
                text, ok = QInputDialog.getText(stack, 
                                                'Edit Parameter', 
                                                'Enter a argument:',
                                                text=str(current_item.text()))
                print(str(text))
                # 排除空字串
                if ok and text.strip() == '':
                    ret = QMessageBox.warning(
                        self.getinfowidget, 
                        'Parameter is Empty!',
                        'You must enter at least one string.',
                        QMessageBox.Ok
                    )
                    stack.PressEdit.emit()
                elif ok:
                    # 重複名稱判斷
                    item_list = GetListData(stack.ParameterList)
                    print(item_list)
                    print(str(text) in item_list)
                    if str(text) in item_list or str(text) == str(current_item.text()):
                        ret = QMessageBox.warning(
                            self.getinfowidget, 
                            'Parameter is duplicate!',
                            'You must enter unique parameter.',
                            QMessageBox.Ok
                        )
                        stack.PressEdit.emit()
                    else:
                        stack.ParameterList.takeItem(list_idx)
                        stack.ParameterList.addItem(str(text))
        @QtCore.Slot()
        def _press_add():
            text, ok = QInputDialog.getText(stack, 
                                            'Add Parameter', 
                                            'Enter a argument:')
            if ok and text.strip() == '':
                ret = QMessageBox.warning(
                    self.getinfowidget, 
                    'Parameter is Empty!',
                    'You must enter at least one string.',
                    QMessageBox.Ok
                )
                stack.PressAdd.emit()
            elif ok:
                # 重複名稱判斷
                item_list = GetListData(stack.ParameterList)
                if str(text) in item_list:
                    ret = QMessageBox.warning(
                        self.getinfowidget, 
                        'Parameter is duplicate!',
                        'You must enter unique parameter.',
                        QMessageBox.Ok
                    )
                    stack.PressAdd.emit()
                else:
                    stack.ParameterList.addItem(str(text))
        @QtCore.Slot()
        def _press_delete():
            list_idx = stack.ParameterList.currentRow()
            if list_idx == -1:
                ret = QMessageBox.warning(
                    self.getinfowidget, 
                    'No Select Parameter!',
                    'You need to select one parameter to delete it.',
                    QMessageBox.Ok
                )
            else:
                sel_items = stack.ParameterList.selectedItems()
                if sel_items:
                    for item in sel_items:
                        idx = stack.ParameterList.row(item)
                        stack.ParameterList.takeItem(idx)
        stack.PressEdit.connect(_press_edit)
        stack.PressAdd.connect(_press_add)
        stack.PressDelete.connect(_press_delete)
    
    def _SetupLeftTable(self, LeftTable, RightStack):
        @QtCore.Slot()
        def _press_edit():
            # TODO 目前只允許編輯flag，內容、類型等等尚無法
            select_cell = LeftTable.table.selectedRanges()
            if self._CheckSelectCell(select_cell):
                for item in select_cell:
                    topRow = item.topRow()
                    bottomRow = item.bottomRow()
                if not bottomRow == topRow:
                    ret = QMessageBox.warning(
                        self.getinfowidget, 
                        'Only Can Edit One Flag!',
                        'You need to select only one row to edit it.',
                        QMessageBox.Ok
                    )
                else:
                    item = LeftTable.table.item(topRow, 0)
                    text, ok = QInputDialog.getText(LeftTable, 
                                                    'Edit Flag', 
                                                    'Enter a flag:',
                                                    text=str(item.text()))
                    if ok and text.strip() == '':
                        ret = QMessageBox.warning(
                            self.getinfowidget, 
                            'Flag is Empty!',
                            'You must enter at least one string.',
                            QMessageBox.Ok
                        )
                        LeftTable.PressEdit.emit()
                    elif ok:
                        # 重複名稱判斷
                        flag_list = GetFlagData(LeftTable.table)
                        if str(text) in flag_list or str(text) == str(item.text()):
                            ret = QMessageBox.warning(
                                self.getinfowidget, 
                                'Flag is duplicate!',
                                'You must enter unique flag.',
                                QMessageBox.Ok
                            )
                            LeftTable.PressEdit.emit()
                        else:
                            LeftTable.table.setItem(topRow, 0, 
                                                    QTableWidgetItem(str(text)))
        @QtCore.Slot()
        def _press_add():
            # 需要用到Add按鈕情況應該沒有(?
            text, ok = QInputDialog.getText(LeftTable, 
                                            'Add Flag', 
                                            'Enter a flag:')
            if ok and text.strip() == '':
                ret = QMessageBox.warning(
                    self.getinfowidget, 
                    'Flag is Empty!',
                    'You must enter at least one string.',
                    QMessageBox.Ok
                )
                LeftTable.PressAdd.emit()
            elif ok:
                # 重複名稱判斷
                flag_list = GetFlagData(LeftTable.table)
                if str(text) in flag_list:
                    ret = QMessageBox.warning(
                        self.getinfowidget, 
                        'Flag is duplicate!',
                        'You must enter unique flag.',
                        QMessageBox.Ok
                    )
                    LeftTable.PressAdd.emit()
                else:
                    n_row = LeftTable.table.rowCount() + 1
                    LeftTable.table.setRowCount(n_row)
                    LeftTable.table.setItem(n_row-1, 0, 
                                            QTableWidgetItem(str(text)))
                    right_widget = RightListWidget(RightStack)
                    # 賦予右邊stack按鈕的功能
                    self._SetupStackItem(right_widget)
                    RightStack.addWidget(right_widget)
        @QtCore.Slot()
        def _press_delete():
            select_cell = LeftTable.table.selectedRanges()
            if self._CheckSelectCell(select_cell):
                for item in select_cell:
                    topRow = item.topRow()
                    bottomRow = item.bottomRow()
                # 不可跳著刪除，但可以一個範圍內刪除
                if topRow == bottomRow:
                    LeftTable.table.removeRow(topRow)
                    widgetToRemove = RightStack.widget(topRow)
                    RightStack.removeWidget(widgetToRemove)
                else:
                    for row in range(bottomRow, topRow - 1, -1):
                        LeftTable.table.removeRow(row)
                        widgetToRemove = RightStack.widget(row)
                        RightStack.removeWidget(widgetToRemove)
                    
        LeftTable.PressEdit.connect(_press_edit)
        LeftTable.PressAdd.connect(_press_add)
        LeftTable.PressDelete.connect(_press_delete)
    
    def _CheckSelectCell(self, select_cell):
        if select_cell == []:
            ret = QMessageBox.warning(
                self.getinfowidget.LeftTable, 
                'No Select Flag!',
                'You need to select one flag.',
                QMessageBox.Ok
            )
            return False
        elif len(select_cell) > 1:
            ret = QMessageBox.warning(
                self.getinfowidget.LeftTable, 
                'Only Can Edit One Flag!',
                'You need to select only row.',
                QMessageBox.Ok
            )
            return False
        else:
            return True

    def _SaveParameter(self, getinfowidget):
        LeftTable = getinfowidget.LeftTable.table
        RightStack = getinfowidget.RightStack
        @QtCore.Slot()
        def _press_save():
            FlagData = GetTableData(LeftTable)
            # TODO FlagData空白跳出警告
            
            # 取得對應的list資料
            ABSLValue = []
            for idx in range(len(FlagData)):
                widgetToRemove = RightStack.widget(idx)
                # TODO value空白跳出警告
                value = GetListData(widgetToRemove.ParameterList)
                ABSLValue.append(value)
            # 取得column的名稱
            header = []
            for col_idx in range(LeftTable.columnCount()):
                header.append(LeftTable.horizontalHeaderItem(col_idx).text())
            
            save_data = {}
            for row_idx, row in enumerate(FlagData):
                save_data[row_idx] = {}
                save_data[row_idx]['value'] = ABSLValue[row_idx]
                tmp_dict = {}
                for col_idx, data in enumerate(row):
                    tmp_dict[header[col_idx]] = data
                save_data[row_idx]['info'] = tmp_dict
            
            def pretty(d, indent=0):
                for key, value in d.items():
                    print('\t' * indent + str(key))
                    if isinstance(value, dict):
                        pretty(value, indent+1)
                    else:
                        print('\t' * (indent+1) + str(value))
            pretty(save_data)
            
            pyfile = os.path.relpath(getinfowidget.openfilewidget.pyfile_path.text())
            pyfile = os.path.basename(pyfile).split('.')[0] + '.json'
            print(pyfile)
            
            # 獲得當地時間、格式化日期
            datetime_dt = datetime.today()
            datetime_str = datetime_dt.strftime("%Y%m%d-%H%M")
            
            with open(datetime_str + '_' + pyfile, 'w') as jsonFile:
                json.dump(save_data, jsonFile)
        getinfowidget.SaveBTN.connect(_press_save)
    
    def _LoadParameter(self, getinfowidget):
        LeftTable = getinfowidget.LeftTable.table
        RightStack = getinfowidget.RightStack
        @QtCore.Slot()
        def _press_load():
            # 打開目標py檔
            # filename, _ = QFileDialog.getOpenFileName(
            #     getinfowidget.openfilewidget,
            #     "Open File", 
            #     "./",
            #     "Python Files (*.py);;All Files (*)"
            # )
            # getinfowidget.openfilewidget.pyfile_path.setText(filename)
            # 打開json檔
            filename, _ = QFileDialog.getOpenFileName(
                getinfowidget,
                "Open Json File", 
                "./",
                "JSON Files (*.json);;All Files (*)"
            )
            with open(filename) as jsonFile:
                save_data = json.load(jsonFile)
            
            self._ClearTable(RightStack, LeftTable)
            flags, value_list, attr_list = ParseJsonParameter(save_data)
            self._ShowData([flags, value_list, attr_list], 
                           getinfowidget.RightStack,
                           getinfowidget.LeftTable)
                
        getinfowidget.LoadBTN.connect(_press_load)