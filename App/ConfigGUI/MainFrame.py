from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

from .CodeReaderTabFrame import CodeReaderTabFrame
from .GeneralTabFrame import GeneralTabFrame
from .WebTabFrame import WebTabFrame
from .PrinterTabFrame import PrinterTabFrame
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
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/Logo-CMedia_C.png"
        icon.addFile(path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(icon)
        #Nombre de la Aplicacion
        self.setWindowTitle("C-Media Player Lx - Configuración")
        self.setMinimumSize(600, 300)
        self.setMaximumSize(600, 300)
        QCoreApplication.setApplicationName("C-Media Player Lx - Configuration")
        #Background
        #bg = QPalette()
        #bg.setColor(QPalette.ColorRole.Window, "#dae7ef") #AR
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color:#dae7ef")
        #self.setPalette(bg)
        
        #Set Layout
        self.mainLayout = QGridLayout()
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.mainLayout)

        #TabFrame
        self.tabWidget = QTabWidget(self)
        self.generalTab = GeneralTabFrame()
        self.webTab = WebTabFrame()
        self.printerTab = PrinterTabFrame()
        self.readerTab = CodeReaderTabFrame()
        self.tabWidget.addTab(self.generalTab, "General")
        self.tabWidget.addTab(self.webTab, "Contenedor Web")
        self.tabWidget.addTab(self.printerTab, "Impresora")
        self.tabWidget.addTab(self.readerTab, "Lector")
        self.mainLayout.addWidget(self.tabWidget)
        

        palette = QPalette()
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, QColor(208, 222, 234))
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Base, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.AlternateBase, QColor(218, 231, 239))
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Text, QColor(88, 102, 108))
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Button, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, QColor(44, 44, 45))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(88, 102, 108))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, QColor(193, 196, 199))
        palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(88, 89, 91))

        self.setPalette(palette)