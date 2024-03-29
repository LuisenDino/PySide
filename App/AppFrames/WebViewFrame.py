#Librerias de GUI 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

#Librerias Navegador Web 
from PyQt6.QtWebEngineWidgets import QWebEngineView as WebView 
from PyQt6.QtWebEngineCore import QWebEnginePage as WebPage, QWebEngineSettings
from PyQt6.QtWebChannel import QWebChannel

from pynput.mouse import Button, Controller


#Clases externas
from .JSBridge import JSBridge
from .NavBar import NavigationBar
from .Controllers.NetworkController import NetworkController
from .Controllers.SpeechSynthesis import SpeechSynthesis



class WebViewFrame(QWidget):
    """
    Clase del Frame del contenedor Web
    :param settings: dic. Configuración del navegador
    """
    def __init__(self, settings):
        """
        Clase del Frame del contenedor Web
        :param settings: dic. Configuración del navegador
        """
        super().__init__()

        #Set Layout
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)
        
        #Creacion del contenedor
        self.view = WebView(self)
        self.view.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.view.setPage(WebPage(self.view))
        self.nav_bar = None

        self.view.page().certificateError.connect(self.on_cert_error)

        self.loaded = False
        self.view.settings().setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        self.grabGesture(Qt.GestureType.PinchGesture, Qt.GestureFlag.DontStartGestureOnChildren)
        #Configuracion
        self.settings = settings
        
        #Barra de Navegacion 
        if self.settings["MostrarBarraNavegacion"]:
            self.nav_bar = NavigationBar(self.view.page())
            self.mainLayout.addWidget(self.nav_bar, 0, 0)

        self.mainLayout.addWidget(self.view, 1, 0)
        self.view.setUrl(QUrl(settings["UrlInicio"]))
        
        self.channel = QWebChannel(self.view.page())
        self.view.loadFinished.connect(self.on_load_finished)

    def showEvent(self, e):
        if self.loaded:
            for api in list(self.apis.values()):               
                api.get_event().loaded()
        else:
            self.loaded = True

    def on_cert_error(self, e):
        print("Error en el certificado")
        e.acceptCertificate()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F5:
            self.view.setUrl(QUrl(self.settings["UrlInicio"]))
        event.accept()
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
        
        if self.loaded:
            for api in list(self.apis.values()):               
                api.get_event().loaded()
        elif self.loaded is not None:
            self.loaded = True
        else:
            self.loaded = None
        m = Controller()
        m.click(Button.left, 1)

        
        
    def load_apis(self):
        """
        Carga las apis al Contenedor web
        """
        api = self.apis
        
        self.js_bridge = JSBridge(self.view.page(), api)
        
        self.view.page().setWebChannel(self.channel)
        qwebchannel_js = QFile('://qtwebchannel/qwebchannel.js')
        if qwebchannel_js.open(QFile.OpenModeFlag.ReadOnly):
            source = qwebchannel_js.readAll().data().decode('utf-8')
            self.view.page().runJavaScript(source)
            self.channel.registerObject('external', self.js_bridge)
            self.channel.registerObject('speech', self.apis["speech"])
            qwebchannel_js.close()


        self.view.page().runJavaScript(self.js_bridge.parse_api_js())


    def set_apis(self, apis):
        """
        Establece las apis en la clase
        :param apis: list. apis
        """
        self.apis = apis
        self.apis["speech"] = SpeechSynthesis()
        self.apis["network"] = NetworkController(self.settings["UrlInicio"], self.view, self.apis["speech"])
        

    def close_speech_synth(self):
        self.apis["speech"].close_thread()
