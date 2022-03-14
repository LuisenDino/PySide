from PySide2 import QtCore

from PySide2.QtWidgets import QMainWindow
from views.WebView import WebView
from views.WebPage import WebPage

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = WebView(self)
        self.view.setPage(WebPage(self.view))
        self.view.page().loadFinished.connect(self.on_load_finished)
        
        self.setCentralWidget(self.view)

        self.view.setUrl(QtCore.QUrl("file:///home/luis/Escritorio/C-Media_Linux_player/example.html"))

    def on_load_finished(self):
        print("hola")

