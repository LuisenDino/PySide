# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"../App/Media/LOGO-CMedia.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 820, 600))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.webView = QWebView(self.frame)
        self.webView.setObjectName(u"webView")
        self.webView.setGeometry(QRect(10, 0, 800, 600))
        self.webView.setStyleSheet(u"QFrame{\n"
"background-color : rgb(138, 226, 52)\n"
"}\n"
"")
        self.webView.setUrl(QUrl(u"about:blank"))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"C-Media Player", None))
    # retranslateUi

