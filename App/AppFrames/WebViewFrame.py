#Librerias de GUI ¿
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

#Librerias Navegador Web 
from PySide2.QtWebEngineWidgets import QWebEngineView as WebView, QWebEnginePage as WebPage
from PySide2.QtWebChannel import QWebChannel

#Clases externas
from .JSBridge import JSBridge
from .NavBar import NavigationBar

class WebViewFrame(QWidget):
    """
    Clase del Frame del contenedor WEb
    :param settings: dic. Configuración del navegador
    """
    def __init__(self, settings):
        """
        Clase del Frame del contenedor WEb
        :param settings: dic. Configuración del navegador
        """
        super().__init__()

        #Set Layout
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)
        
        #Creacion del contenedor
        self.view = WebView(self)
        self.view.setPage(WebPage(self.view))
        self.view.loadFinished.connect(self.on_load_finished)

        #Configuracion
        self.settings = settings
        
        #Barra de Navegacion 
        if self.settings["MostrarBarraNavegacion"]:
            self.nav_bar = NavigationBar(self.view.page())
            self.mainLayout.addWidget(self.nav_bar, 0, 0)

        self.mainLayout.addWidget(self.view, 1, 0)

        self.view.setUrl(QUrl(settings["UrlInicio"]))

        self.channel = QWebChannel(self.view.page())
        
        

        
    
    def on_load_finished(self):
        """
        Evento de finalización del estado de carga
        Carga las apis al contenedor y cambia la url de la barra de navegación
        """
        for api in list(self.apis.values()):               
            api.get_event().set_page(self.view.page())
        self.load_apis()
        if self.nav_bar:
            self.nav_bar.set_url(str(self.view.page().url().url()))
        

    def load_apis(self):
        """
        Carga las apis al Contenedor web
        """
        self.js_bridge = JSBridge(self.view.page(), self.apis)
        
        self.view.page().setWebChannel(self.channel)
        qwebchannel_js = QFile('://qtwebchannel/qwebchannel.js')
        if qwebchannel_js.open(QFile.ReadOnly):
            source = bytes(qwebchannel_js.readAll()).decode('utf-8')
            self.view.page().runJavaScript(source)
            self.channel.registerObject('external', self.js_bridge)
            qwebchannel_js.close()


        self.view.page().runJavaScript(self.js_bridge.parse_api_js())



    def set_apis(self, apis):
        """
        Establece las apis en la clase
        :param apis: list. apis
        """
        self.apis = apis