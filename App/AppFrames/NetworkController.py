import logging
from PySide2.QtWebEngineWidgets import *
from PySide2.QtCore import *
from .Event import Event

class NetworkController():
    def __init__(self, ruta, webview):
        self.webview = webview
        self.ruta = ruta
        self.event = Event("")

    def disconnected(self):
        logging.error("Desconexión de internet")
        self.event.awake_js("alert('El Equipo se desconectó de internet')")

    def connected(self):
        self.webview.load(QUrl(self.ruta))

    def get_event(self):
        return self.event