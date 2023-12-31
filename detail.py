# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import pyx
from sniff import *
import os

### 保存子进程
class pdfWorker(QThread):
    def __init__(self):
        super().__init__()
        self.filename=""
        self.pkt=Packet()
    def run(self):
        self.pkt.canvas_dump().writePDFfile(self.filename)  ## 将数据包解析结果输出pdf
        os.system(r"start " + self.filename)    ## 打开PDF

class Ui_Dialog_detail(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(650, 850)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.textBrowser1 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser1.setGeometry(QtCore.QRect(20, 40, 610, 300))
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 380, 610, 400))
        self.pkt = Packet()

        ### 标题
        detail_title = QtWidgets.QTextBrowser(Dialog)
        detail_title.setGeometry(QtCore.QRect(20, 350, 600, 30))
        detail_title.setHtml("<h3>Detail</h3>")
        detail_title.setStyleSheet('background:transparent;border-width:0;border-style:outset')
        content_title = QtWidgets.QTextBrowser(Dialog)
        content_title.setGeometry(QtCore.QRect(20, 10, 600, 30))
        content_title.setHtml("<h3>Content</h3>")
        content_title.setStyleSheet('background:transparent;border-width:0;border-style:outset')

        ### 保存
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(510, 800, 120, 30))
        self.saveButton.clicked.connect(self.save_canvas)
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.saveButton.setText(_translate("Form", "保存详细解析"))

    def save_canvas(self):
        try:
            filename,filetype = QFileDialog.getSaveFileName(None, '选择保存路径', '.', 'pdf(*.pdf)')
        except Exception as e:
            QMessageBox.critical(None, "错误", "错误警告：" + str(e))
        if filename=='':
            return
        try:
            self.cal=pdfWorker()
            self.cal.filename=filename
            self.cal.pkt=self.pkt
            self.cal.start()  # 线程启动
        except Exception as e:
            QMessageBox.critical(None, "错误","错误警告：" + str(e))
