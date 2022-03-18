from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from .GeneralTabFrame import GeneralTabFrame
import os

class MainFrame(QWidget):
    """
    Clase de pantalla principal (configuracion)
    """
    def __init__(self):
        """
        Constructor de clase
        """
        super().__init__()
        icon = QIcon()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/LOGO-CMedia.png"
        icon.addFile(path, QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        #Nombre de la Aplicacion
        self.setWindowTitle("C-Media Player - Configuración")
        QCoreApplication.setApplicationName("C-Media Player configuration")
        #Background
        bg = QPalette()
        bg.setColor(QPalette.Window, "#eef1f2")
        self.setAutoFillBackground(True)
        self.setPalette(bg)
        
        #Set Layout
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.mainLayout)

        #TabFrame
        self.tabWidget = QTabWidget(self)
        self.generalTab = GeneralTabFrame()
        self.tabWidget.addTab(self.generalTab, "General")
        self.mainLayout.addWidget(self.tabWidget)