from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from PySide2.QtWebEngineWidgets import QWebEngineView as WebView, QWebEnginePage as WebPage
from PySide2.QtWebChannel import QWebChannel

from .JSBridge import JSBridge

class WebViewFrame(QWidget):
    def __init__(self, settings):
        super().__init__()

        #Set Layout
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)

        self.view = WebView(self)
        self.view.setPage(WebPage(self.view))
        self.view.loadFinished.connect(self.on_load_finished)

        
        

        #Configuracion
        self.settings = settings
        
        if self.settings["MostrarBarraNavegacion"]:
            pass
            #self.nav_bar = NavigationBar(self.parent)
            #self.mainLayout.addWidget(self.nav_bar, 0, 0)

        self.mainLayout.addWidget(self.view, 1, 0)

        self.view.setUrl(QUrl(settings["UrlInicio"]))

        self.channel = QWebChannel(self.view.page())
            
    
    def on_load_finished(self):
        for api in list(self.apis.values()):
            api.get_event().set_page(self.view.page())
        self.load_apis()

        
        

    def load_apis(self):
        self.js_bridge = JSBridge(self.view.page(), self.apis)
        
        self.view.page().setWebChannel(self.channel)
        qwebchannel_js = QFile('://qtwebchannel/qwebchannel.js')
        if qwebchannel_js.open(QFile.ReadOnly):
            source = bytes(qwebchannel_js.readAll()).decode('utf-8')
            self.view.page().runJavaScript(source)
            self.channel.registerObject('external', self.js_bridge)
            qwebchannel_js.close()


        self.view.page().runJavaScript(self.js_bridge.parse_api_js())

        print(self.view.page().runJavaScript("alert(Object.values(window.external))"))

    def set_apis(self, apis):
        self.apis = apis
