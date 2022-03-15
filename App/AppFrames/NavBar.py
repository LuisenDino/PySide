from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEnginePage as QPage
from PySide2.QtCore import QUrl

import os

class NavigationBar(QWidget):
    def __init__(self, page):
        self.page = page

        super().__init__()

        self.setFixedHeight(30)
        #Set Layout
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(10, 5, 10, 0)
        self.setLayout(self.mainLayout)

        #Back Button
        self.back_button = QToolButton()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-back-50.png"
        pixmap = QPixmap(path)
        self.back_button.setIcon(pixmap)
        self.back_button.clicked.connect(self.go_backward)
        self.mainLayout.addWidget(self.back_button, 0 , 0)

        #Forward Button
        self.fwd_button = QToolButton()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-forward-50.png"
        pixmap = QPixmap(path)
        self.fwd_button.setIcon(pixmap)
        self.fwd_button.clicked.connect(self.go_forward)
        self.mainLayout.addWidget(self.fwd_button, 0 , 1)
        
        #Forward Button
        self.reload_button = QToolButton()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-rotate-50.png"
        pixmap = QPixmap(path)
        self.reload_button.setIcon(pixmap)
        self.reload_button.clicked.connect(self.reload)
        self.mainLayout.addWidget(self.reload_button, 0 , 2)

        #Url Entry
        self.url_entry = QLineEdit("url")
        self.url_entry.returnPressed.connect(self.load_url)
        self.mainLayout.addWidget(self.url_entry, 0, 3, 1,4)

    def go_backward(self):
        self.page.triggerAction(QPage.Back)

    def go_forward(self):
        self.page.triggerAction(QPage.Forward)

    def reload(self):
        self.page.triggerAction(QPage.Reload)

    def load_url(self):
        self.page.load(QUrl(self.url_entry.text()))

    def set_url(self, url):
        self.url_entry.clear()
        self.url_entry.insert(url)

    