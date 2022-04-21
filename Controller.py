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
from view.GetInfoWindow.SubWidget import ParameterListWidget
from PySide6.QtWidgets import (
    QFileDialog,
    QFormLayout,
    QLineEdit,
    QWidget,
    QInputDialog,
    QMessageBox
)
from view.Dialog import (
    NoSelectDialog_edit,
    NoSelectDialog_delete,
    ParameterEmpty
)
from PySide6 import QtCore
        
# TODO abls test data
def test():
    rightlist = [[1,2,3], [True,False,3], ['1','2','3'], [44345,26234]]
    leftlist = ['test{}'.format(i) for i in range(len(rightlist))]
    return leftlist, rightlist

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
                "./",
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
        def print_path(msg1, msg2):
            print('Path: ' + msg1)
            print('Path: ' + msg2)
            leftlist, rightlist = test()
            self.load_parameter(getinfowidget.showparameter, leftlist, rightlist)
        getinfowidget.PressOK.connect(print_path)
        self._SetupLeftList(getinfowidget.showparameter.LeftList,
                            getinfowidget.showparameter.RightStack)
        getinfowidget.ClossBTN.connect(self._exit)
    
    def load_parameter(self, showparameter, leftlist, rightlist):
        # 用測試資料創建左邊list資料、添加右邊stack資料
        for idx, left_item in enumerate(leftlist):
            showparameter.LeftList.ParameterList.insertItem(idx, left_item)
        def stackUI(rightitem):
            # FIXME 如果parameter有東西，需要添加保護，或是有其他對應stack的方法使其對應變成唯一
            stack = ParameterListWidget(showparameter.RightStack)
            for item in rightitem:
                stack.ParameterList.addItem(str(item))
            # 賦予右邊stack按鈕的功能
            self._SetupStackItem(stack)
            return stack
        for rightitem in rightlist:
            right_widget = stackUI(rightitem)
            showparameter.RightStack.addWidget(right_widget)
        
    def _SetupLeftList(self, LeftList, RightStack):
        @QtCore.Slot()
        def _press_edit():
            list_idx = LeftList.ParameterList.currentRow()
            sel_items = LeftList.ParameterList.selectedItems()
            if list_idx == -1:
                NoSelectDialog_edit(self.windows)
            else: 
                text, ok = QInputDialog.getText(LeftList, 
                                                'Edit Parameter', 
                                                'Enter a argument:',
                                                text=str(sel_items[0].text()))
                if ok and text.strip() == '':
                    ParameterEmpty(self.windows)
                    LeftList.PressEdit.emit()
                elif ok:
                    # TODO 排除重複的名稱，或當名稱重複跳出警告
                    sel_items = LeftList.ParameterList.selectedItems()
                    for item in sel_items:
                        item.setText(str(text))
        @QtCore.Slot()
        def _press_add():
            text, ok = QInputDialog.getText(LeftList, 
                                            'Add Parameter', 
                                            'Enter a argument:')
            if ok and text.strip() == '':
                ParameterEmpty(self.windows)
                LeftList.PressAdd.emit()
            elif ok:
                LeftList.ParameterList.addItem(str(text))
                right_widget = ParameterListWidget(RightStack)
                # 賦予右邊stack按鈕的功能
                self._SetupStackItem(right_widget)
                RightStack.addWidget(right_widget)
        @QtCore.Slot()
        def _press_delete():
            list_idx = LeftList.ParameterList.currentRow()
            if list_idx == -1:
                NoSelectDialog_delete(self.windows)
            else:
                sel_items = LeftList.ParameterList.selectedItems()
                if sel_items:
                    for item in sel_items:
                        idx = LeftList.ParameterList.row(item)
                        LeftList.ParameterList.takeItem(idx)
                        widgetToRemove = RightStack.widget(idx)
                        RightStack.removeWidget(widgetToRemove)
        
        LeftList.PressEdit.connect(_press_edit)
        LeftList.PressAdd.connect(_press_add)
        LeftList.PressDelete.connect(_press_delete)
        
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
                                                text =str(sel_items[0].text()))
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

