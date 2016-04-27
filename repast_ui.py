# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repast.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 400)
        Dialog.setMinimumSize(QtCore.QSize(500, 400))
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        Dialog.setSizeGripEnabled(False)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(61, 11, 354, 383))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.choose_file_bn = QtGui.QPushButton(self.layoutWidget)
        self.choose_file_bn.setObjectName(_fromUtf8("choose_file_bn"))
        self.verticalLayout.addWidget(self.choose_file_bn)
        self.choose_image_bn = QtGui.QPushButton(self.layoutWidget)
        self.choose_image_bn.setObjectName(_fromUtf8("choose_image_bn"))
        self.verticalLayout.addWidget(self.choose_image_bn)
        self.check_image_bn = QtGui.QPushButton(self.layoutWidget)
        self.check_image_bn.setObjectName(_fromUtf8("check_image_bn"))
        self.verticalLayout.addWidget(self.check_image_bn)
        self.choose_save_dir_bn = QtGui.QPushButton(self.layoutWidget)
        self.choose_save_dir_bn.setObjectName(_fromUtf8("choose_save_dir_bn"))
        self.verticalLayout.addWidget(self.choose_save_dir_bn)
        self.resize_image_bn = QtGui.QPushButton(self.layoutWidget)
        self.resize_image_bn.setObjectName(_fromUtf8("resize_image_bn"))
        self.verticalLayout.addWidget(self.resize_image_bn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.choose_filename = QtGui.QLineEdit(self.layoutWidget)
        self.choose_filename.setObjectName(_fromUtf8("choose_filename"))
        self.verticalLayout_2.addWidget(self.choose_filename)
        self.choose_image_dir = QtGui.QLineEdit(self.layoutWidget)
        self.choose_image_dir.setObjectName(_fromUtf8("choose_image_dir"))
        self.verticalLayout_2.addWidget(self.choose_image_dir)
        self.no_image_count = QtGui.QLineEdit(self.layoutWidget)
        self.no_image_count.setObjectName(_fromUtf8("no_image_count"))
        self.verticalLayout_2.addWidget(self.no_image_count)
        self.save_dirname = QtGui.QLineEdit(self.layoutWidget)
        self.save_dirname.setObjectName(_fromUtf8("save_dirname"))
        self.verticalLayout_2.addWidget(self.save_dirname)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.image_width = QtGui.QLineEdit(self.layoutWidget)
        self.image_width.setMaximumSize(QtCore.QSize(60, 20))
        self.image_width.setObjectName(_fromUtf8("image_width"))
        self.horizontalLayout.addWidget(self.image_width)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.image_height = QtGui.QLineEdit(self.layoutWidget)
        self.image_height.setMaximumSize(QtCore.QSize(60, 20))
        self.image_height.setObjectName(_fromUtf8("image_height"))
        self.horizontalLayout.addWidget(self.image_height)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_3.addWidget(self.label_9)
        self.scrollArea = QtGui.QScrollArea(self.layoutWidget)
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 348, 210))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.no_file_tip = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.no_file_tip.setGeometry(QtCore.QRect(0, 0, 350, 211))
        self.no_file_tip.setObjectName(_fromUtf8("no_file_tip"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.choose_file_bn.setText(_translate("Dialog", "选择汇总文件", None))
        self.choose_image_bn.setText(_translate("Dialog", "选择图片目录", None))
        self.check_image_bn.setText(_translate("Dialog", "检查图片是否存在", None))
        self.choose_save_dir_bn.setText(_translate("Dialog", "设置图片生成目录", None))
        self.resize_image_bn.setText(_translate("Dialog", "重置图片大小", None))
        self.label_4.setText(_translate("Dialog", "宽度:", None))
        self.label_6.setText(_translate("Dialog", "px", None))
        self.label_5.setText(_translate("Dialog", "高度:", None))
        self.label_7.setText(_translate("Dialog", "px", None))
        self.label_9.setText(_translate("Dialog", "以下图片不存在：", None))

