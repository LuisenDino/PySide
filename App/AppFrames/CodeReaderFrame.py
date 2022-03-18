#Librerias de GUI
from PySide2.QtCore import * 
from PySide2.QtWidgets import *
from PySide2.QtGui import * 

class CodeReaderFrame(QWidget):
    def __init__(self, settings):
        """
        Constructor de clase
        :param settings: Configuracion del lector
        """
        
        from .Controllers.CodeReaders.Honeywell3320g import BarCodeReader
        
        self.code_reader = BarCodeReader(settings["PuertoSerial"])

        super().__init__()
        
    def get_code_reader(self):
        """
        Obtiene el lector
        """
        return self.code_reader