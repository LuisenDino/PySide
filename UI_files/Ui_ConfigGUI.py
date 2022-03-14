# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfigGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 60, 631, 301))
        self.GeneralTab = QWidget()
        self.GeneralTab.setObjectName(u"GeneralTab")
        self.verticalLayoutWidget = QWidget(self.GeneralTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 601, 268))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.verticalLayoutWidget)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout_9.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_9.addWidget(self.pushButton_16)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.pushButton_17 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_10.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_10.addWidget(self.pushButton_18)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_11.addWidget(self.lineEdit_2)

        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_11.addWidget(self.lineEdit_3)

        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_11.addWidget(self.lineEdit_4)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_11.addWidget(self.lineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.pushButton_19 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout.addWidget(self.pushButton_19)

        self.tabWidget.addTab(self.GeneralTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Archivo de Recursos", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pantalla Completa", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BordeVentana ", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Siempre Visible", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Ancho", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Alto", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Superior", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Inferior", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GeneralTab), QCoreApplication.translate("MainWindow", u"General", None))
    # retranslateUi

