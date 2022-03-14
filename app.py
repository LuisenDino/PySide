import sys
from time import sleep
from PySide2.QtWidgets import QApplication, QSplashScreen
from controllers.Browser import Browser
from PySide2.QtCore import *
from PySide2.QtGui import *
from App2.ConfigGUI.MainFrame import MainFrame
if __name__ == "__main__":
    app = QApplication()
    pixmap = QPixmap("/home/luis/Escritorio/C-Media_Linux_player/App/Media/SplashScreen.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    app.processEvents()
    
    browser = MainFrame()
    #browser =  Browser()
    
    splash.finish(browser)
    #sleep(5)
    browser.show()
    sys.exit(app.exec_()) 