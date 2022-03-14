from PySide2.QtWebEngineWidgets import QWebEnginePage

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)