# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_project1_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 862)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#FFA500;")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color:#FFFF4D;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_4)
        self.listWidget_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("color:#000000;")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.input1 = QtWidgets.QLineEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input1.sizePolicy().hasHeightForWidth())
        self.input1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.input1.setFont(font)
        self.input1.setObjectName("input1")
        self.horizontalLayout_2.addWidget(self.input1)
        self.btn1 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("background-color:#FFFFE0;")
        self.btn1.setObjectName("btn1")
        self.horizontalLayout_2.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("background-color:#F0FFF0;")
        self.btn2.setObjectName("btn2")
        self.horizontalLayout_2.addWidget(self.btn2)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("background-color:#FFF0F5;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn3 = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(30)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("background-color:#FFD9E6;")
        self.btn3.setObjectName("btn3")
        self.verticalLayout_4.addWidget(self.btn3)
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.res1 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res1.sizePolicy().hasHeightForWidth())
        self.res1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.res1.setFont(font)
        self.res1.setStyleSheet("")
        self.res1.setObjectName("res1")
        self.horizontalLayout_3.addWidget(self.res1)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.res2 = QtWidgets.QLineEdit(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res2.sizePolicy().hasHeightForWidth())
        self.res2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.res2.setFont(font)
        self.res2.setObjectName("res2")
        self.horizontalLayout_4.addWidget(self.res2)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_6)
        self.pic_res = QtWidgets.QLabel(self.frame)
        self.pic_res.setFrameShape(QtWidgets.QFrame.Panel)
        self.pic_res.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pic_res.setText("")
        self.pic_res.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_res.setObjectName("pic_res")
        self.verticalLayout.addWidget(self.pic_res)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:#E0FFFF;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.btn4 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(30)
        self.btn4.setFont(font)
        self.btn4.setStyleSheet("background-color:#F5FFFA")
        self.btn4.setObjectName("btn4")
        self.verticalLayout_2.addWidget(self.btn4)
        self.ana_res = QtWidgets.QLabel(self.frame_2)
        self.ana_res.setMaximumSize(QtCore.QSize(490, 505))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(144)
        self.ana_res.setFont(font)
        self.ana_res.setFrameShape(QtWidgets.QFrame.Box)
        self.ana_res.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ana_res.setText("")
        self.ana_res.setObjectName("ana_res")
        self.verticalLayout_2.addWidget(self.ana_res)
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color:#FFF5EE;\n"
"color:#000000;")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(11)
        item.setFont(font)
        self.listWidget.addItem(item)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Biue Tseng 的抽獎遊戲"))
        self.label_4.setText(_translate("MainWindow", "遊  戲  規  則"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "1. 抽獎號碼共 1 ~ 20 號"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "2.請在下方框框內輸入您的幸運號碼"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "3.若沒有感覺讓系統自動幫您選號，請按自動選號"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "4.接著按下開始抽獎，等待抽獎中..."))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "5. 接著按開獎，接著便知道您是否為幸運兒~"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "6.想知道抽獎號碼有沒有公平，請按分析鈕"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "7.此小遊戲，不代表任何抽獎相關遊戲"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.btn1.setText(_translate("MainWindow", "輸入號碼"))
        self.btn2.setText(_translate("MainWindow", "自動選號"))
        self.btn3.setText(_translate("MainWindow", "開 始 抽 獎"))
        self.label_5.setText(_translate("MainWindow", "中 獎 號 碼 "))
        self.label_6.setText(_translate("MainWindow", "您 的 號 碼 "))
        self.label_2.setText(_translate("MainWindow", "抽 獎 分 析"))
        self.btn4.setText(_translate("MainWindow", "分  析"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "1.紅色虛線區間為 ± 2倍標準差"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "2.Number 為 號碼1~20號"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "3. Probability 為 每個號碼出現的機率"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "4.請確認每個號碼出現的機率(藍色部分)，是否超過或低於紅色虛線"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "5.若都沒有超過，代表此為公平的抽獎"))
        self.listWidget.setSortingEnabled(__sortingEnabled)