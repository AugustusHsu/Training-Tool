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
    QInputDialog
)
from PySide6 import QtCore

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
    
    # TODO Add the abls parameter
    def _SetupGetInfoWidget(self, getinfowidget):
        self._SetupOpenFileWidget(getinfowidget.openfilewidget)
        self._SetupSelectPythonWidget(getinfowidget.selectpythonwidget)
        self._SetupShowParameter(getinfowidget.showparameter)
        @QtCore.Slot(str, str)
        def print_path(msg1, msg2):
            print('Path: ' + msg1)
            print('Path: ' + msg2)
            leftlist, rightlist = self.test()
            self.load_parameter(getinfowidget.showparameter, leftlist, rightlist)
        getinfowidget.PressOK.connect(print_path)
        
    # TODO abls test data
    def test(self):
        rightlist = [[1,2,3], [True,False,3], ['1','2','3'], [44345,26234]]
        leftlist = ['test{}'.format(i) for i in range(len(rightlist))]
        return leftlist, rightlist
    
    def load_parameter(self, showparameter, leftlist, rightlist):
        # 用測試資料創建左邊list資料、添加右邊stack資料
        for idx, left_item in enumerate(leftlist):
            showparameter.LeftList.ParameterList.insertItem(idx, left_item)
        def stackUI(rightitem):
            # FIXME 如果parameter有東西，需要添加保護，或是有其他對應stack的方法使其對應變成唯一
            stack = ParameterListWidget(showparameter.RightStack)
            for item in rightitem:
                stack.ParameterList.addItem(str(item))
            return stack
        for rightitem in rightlist:
            right_widget = stackUI(rightitem)
            showparameter.RightStack.addWidget(right_widget)
        
    def _SetupShowParameter(self, showparameter):
        self._SetupLeftList(showparameter.LeftList,
                            showparameter.RightStack)
        # self._SetupRightStack(showparameter.RightStack)
        
    def _SetupLeftList(self, LeftList, RightStack):
        @QtCore.Slot()
        def _press_edit():
            list_idx = LeftList.ParameterList.currentRow()
            if list_idx == -1:
                # TODO 跳出警告 
                print('No parameter selected.')
            else:
                text, ok = QInputDialog.getText(LeftList, 
                                                'Input Dialog', 
                                                'Enter your name:')
                if ok:
                    # FIXME 排除重複的名稱
                    sel_items = LeftList.ParameterList.selectedItems()
                    for item in sel_items:
                        item.setText(str(text))
        @QtCore.Slot()
        def _press_add():
            text, ok = QInputDialog.getText(LeftList, 
                                            'Input Dialog', 
                                            'Enter your name:')
            # TODO 字串為空時跳出警告
            if ok and not text.strip() == '':
                LeftList.ParameterList.addItem(str(text))
                right_widget = ParameterListWidget(RightStack)
                RightStack.addWidget(right_widget)
        @QtCore.Slot()
        def _press_delete():
            # FIXME 連續刪除會有問題 (刪除後會跳到最後的list對應的stack，所以導致stack刪掉的是最後一個而list不是)
            sel_items = LeftList.ParameterList.selectedItems()
            for item in sel_items:
                LeftList.ParameterList.removeItemWidget(item)
            RightStack.removeWidget(RightStack.currentWidget())
        
        LeftList.PressEdit.connect(_press_edit)
        LeftList.PressAdd.connect(_press_add)
        LeftList.PressDelete.connect(_press_delete)
        
        
    def _SetupRightStack(self, RightStack):
        RightStack.PressEdit
        RightStack.PressAdd
        RightStack.PressDelete
        
        # RightStack.add_btn.clicked.connect(_press_add)
        # RightStack.delete_btn.clicked.connect(_press_delete)
        # RightStack.edit_btn.clicked.connect(_press_edit)
        
        # @QtCore.Slot()
        # def _press_edit(self):
        #     list_idx = self.ParameterList.currentRow()
        #     if list_idx == -1:
        #         print('No parameter selected.')
        #     self.PressEdit.emit()
        
        # @QtCore.Slot()
        # def _press_add(self):
        #     text, ok = QInputDialog.getText(self, 'Input Dialog', 
        #         'Enter your name:')
        #     # TODO Check the input parameter whether is in the legal list
        #     if ok:
        #         self.ParameterList.addItem(str(text))
        #     print(text, ok)
        #     self.PressAdd.emit()
            
        # @QtCore.Slot()
        # def _press_delete(self):
        #     list_idx = self.ParameterList.currentRow()
        #     if list_idx == -1:
        #         print('No parameter selected.')
        #     else:
        #         self.ParameterList.removeItemWidget(self.ParameterList.takeItem(list_idx))
        #     self.PressDelete.emit()