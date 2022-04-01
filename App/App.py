#Librerias de GUI
from PySide2.QtWidgets import QApplication, QSplashScreen
from PySide2.QtCore import *
from PySide2.QtGui import *

"""
#Clases internas - Compilación
#Descomentar para realizar compilacion de la aplicacion
from App.ConfigGUI.MainFrame import MainFrame as Configuration
from App.Player import Player as Player
"""

#Clases internas - Pruebas 
#Descomentar para realizar pruebas con python
from ConfigGUI.MainFrame import MainFrame as Configuration
from Player import Player as Player

#Otras librerias 
import sys
import logging
import os

#Creacion del archivo de logs
logging.basicConfig(filename=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/logs/log.log", level=logging.DEBUG, format=("%(asctime)s:%(levelname)s:%(message)s"), datefmt="%m/%d/%Y %I:%M:%S %p")

#Creacion aplicacion
root = QApplication()

#Creacion del SplashScreen
pixmap = QPixmap(os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/SplashScreen.png")
splash = QSplashScreen(pixmap)
splash.show()
root.processEvents()

#Iniciacion
if len(sys.argv) == 1:
    try:
        player = Player()
        splash.finish(player)
        player.show()
    except Exception as e:
        logging.error(str(e))
        sys.exit()
elif "--config" in sys.argv:
    try:
        config = Configuration()
        splash.finish(config)
        config.show()
    except Exception as e:
        logging.error(str(e))
        sys.exit()
else:
    logging.error("Opcion no permitida")

#Fin de  la aplicacion
sys.exit(root.exec_())