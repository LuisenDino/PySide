#Librerias de GUI
from PySide2.QtWidgets import QApplication, QSplashScreen
from PySide2.QtCore import *
from PySide2.QtGui import *

#Otras librerias 
import sys
import logging
import os

argv = sys.argv
debug = "--debug" in sys.argv

if debug:
    #Clases internas - Pruebas 
    #Descomentar para realizar pruebas con python
    from ConfigGUI.MainFrame import MainFrame as Configuration
    from Player import Player as Player
    argv.remove("--debug")
else:
    #Clases internas - Compilación
    #Descomentar para realizar compilacion de la aplicacion
    from App.ConfigGUI.MainFrame import MainFrame as Configuration
    from App.Player import Player as Player



#Creacion del archivo de logs
logging.basicConfig(filename=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/logs/log.log", level=logging.DEBUG, format=("%(asctime)s:%(levelname)s:%(message)s"), datefmt="%m/%d/%Y %I:%M:%S %p")

#Creacion aplicacion
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-pinch"
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
root = QApplication()
QCoreApplication.setApplicationName("C-Media Player v2.0")
#Creacion del SplashScreen
pixmap = QPixmap(os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/SplashScreen.png")
splash = QSplashScreen(pixmap)
splash.show()
root.processEvents()



#Iniciacion
if len(argv) == 1:
    try:
        player = Player(debug)
        splash.finish(player)
        player.show()
    except Exception as e:
        logging.error(str(e))
        sys.exit()
elif "--config" in argv:
    try:
        config = Configuration()
        splash.finish(config)
        config.show()
    except Exception as e:
        logging.error(str(e))
        sys.exit()
else:
    logging.error("Opcion no permitida")
    sys.exit()
root.lastWindowClosed.connect(root.quit)
#Fin de  la aplicacion
sys.exit(root.exec_())
