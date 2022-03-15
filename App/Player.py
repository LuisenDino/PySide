from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from .AppFrames.MainFrame import MainFrame

import os
import logging
import json

class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        #Icono de la Aplicacion
        icon = QIcon()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/LOGO-CMedia.png"
        icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        #Nombre de la Aplicacion
        
        QCoreApplication.setApplicationName("C-Media Player v2.0")

        self.sett = self.get_sett()
        self.screen_config = self.get_screen_config(self.sett["Ruta"])

        if self.sett["PantallaCompleta"]:
            self.showFullScreen()
        
        if self.sett["SiempreVisible"]:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)

        if not(self.sett["MostrarBordeVentana"]):
            self.setWindowFlags(Qt.FramelessWindowHint)

        self.setGeometry(self.sett["LeftRequerido"],self.sett["TopRequerido"] , self.sett["AnchoRequerido"], self.sett["AltoRequerido"])        


        pantallas = {}
        for pantalla in self.screen_config["Pantallas"]:
            pantallas[pantalla["ScreenNumber"]] = MainFrame(pantalla["Controles"])
            if(pantalla["ScreenNumber"]==1):
                self.setWindowTitle(pantalla["TitleName"])

        #setCentralWidget
        self.setCentralWidget(pantallas[1])

        if self.sett["PantallaCompleta"]:
            self.showFullScreen()
    

    def closeEvent(self, event):
        self.centralWidget().closeEvent()
        event.accept()

    def get_screen_config(self, ruta):
        """
        Obtiene la informacion de las pantallas y su configuracion
        :param ruta: str. Ruta donde se encuentra el archivo de configuracion
        :return: dic. Configuracion extraida del archivo json
        """
        try:
            with open(ruta, 'r', encoding="utf-8-sig") as file:
                screen_config = json.load(file)
            return screen_config
        except Exception as e:
            logging.error(str(e))
            return str(e)

    def get_sett(self):
        """
        Obtiene la informacion de configuracion de la aplicacion
        :return: dic. Configuracion extraida del archivo json
        """
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/config.json"
        try:
            with open(path, "r") as file:
                sett = json.load(file)
            return sett
        except Exception as e:
            logging.error(str(e))
            return str(e)