from PySide2.QtWebEngineWidgets import QWebEngineView


class WebView (QWebEngineView):
    def __inint__(self, parent=None):
        super(WebView, self).__init__(parent)
        
