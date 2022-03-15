import sys
import logging

from App.ConfigGUI.MainFrame import MainFrame as Configuration
from App.Player import Player as Player
import os

from PySide2.QtWidgets import QApplication, QSplashScreen
from PySide2.QtCore import *
from PySide2.QtGui import *

logging.basicConfig(filename=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/logs/log.log", level=logging.DEBUG, format=("%(asctime)s:%(levelname)s:%(message)s"), datefmt="%m/%d/%Y %I:%M:%S %p")


root = QApplication()

pixmap = QPixmap(os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/SplashScreen.png")
splash = QSplashScreen(pixmap)
splash.show()
root.processEvents()
if len(sys.argv) == 1:
    try:
        player = Player()
        splash.finish(player)
        player.show()
    except Exception as e:
        logging.error(str(e))
elif "--config" in sys.argv:
    try:
        config = Configuration()
        splash.finish(config)
        config.show()
    except Exception as e:
        logging.error(str(e))
else:
    logging.error("Opcion no permitida")

sys.exit(root.exec_())