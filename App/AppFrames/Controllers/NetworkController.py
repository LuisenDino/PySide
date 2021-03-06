import logging
import time
from tokenize import Special
from PySide2.QtWebEngineWidgets import *
from PySide2.QtCore import *
from ..Event import Event


class NetworkController():
    def __init__(self, ruta, webview, speech_synthesis):
        self.webview = webview
        self.ruta = ruta
        self.event = Event("")
        self.speech_synthesis = speech_synthesis

    def disconnected(self):
        logging.error("Desconexión de internet")
        self.event.awake_js("alert('El Equipo se desconectó de internet')")
        self.speech_synthesis.cancel_speech()

    def connected(self):
        time.sleep(10)
        self.webview.load(QUrl(self.ruta))

    def get_event(self):
        return self.event