#Librerias de GUI
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

#Librerias de Navegador Web
from PyQt6.QtWebEngineCore import QWebEnginePage as QPage
from PyQt6.QtCore import QUrl

import os

class NavigationBar(QWidget):
    """
    Clase de barra de Navegacion
    :param page: QWebEnginePage navegador que maneja las paginas
    """
    def __init__(self, page):
        """
        Clase de barra de Navegacion
        :param page: QWebEnginePage navegador que maneja las paginas
        """
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
        self.back_button.setIcon(QIcon(pixmap))
        self.back_button.clicked.connect(self.go_backward)
        self.mainLayout.addWidget(self.back_button, 0 , 0)

        #Forward Button
        self.fwd_button = QToolButton()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-forward-50.png"
        pixmap = QPixmap(path)
        self.fwd_button.setIcon(QIcon(pixmap))
        self.fwd_button.clicked.connect(self.go_forward)
        self.mainLayout.addWidget(self.fwd_button, 0 , 1)
        
        #Forward Button
        self.reload_button = QToolButton()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/icons8-rotate-50.png"
        pixmap = QPixmap(path)
        self.reload_button.setIcon(QIcon(pixmap))
        self.reload_button.clicked.connect(self.reload)
        self.mainLayout.addWidget(self.reload_button, 0 , 2)

        #Url Entry
        self.url_entry = QLineEdit("url")
        self.url_entry.returnPressed.connect(self.load_url)
        self.mainLayout.addWidget(self.url_entry, 0, 3, 1,4)

    def go_backward(self):
        """
        Redirige a la pagina anterior del historial
        """
        self.page.triggerAction(QPage.WebAction.Back)

    def go_forward(self):
        """
        Redirige a la pagina siguiente del historial
        """
        self.page.triggerAction(QPage.WebAction.Forward)

    def reload(self):
        """
        Recarga la pagina actual
        """
        self.page.triggerAction(QPage.WebAction.Reload)

    def load_url(self):
        """
        Carga la url de la barra de busqeda
        """
        self.page.load(QUrl(self.url_entry.text()))

    def set_url(self, url):
        """
        Cambia la url de la barra de busqueda
        :param url: str. url de la pagina actual
        """
        self.url_entry.clear()
        self.url_entry.insert(url)

    