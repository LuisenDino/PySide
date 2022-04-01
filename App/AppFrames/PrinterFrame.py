#Librerias de GUI 
import os
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class PrinterFrame(QWidget):
    """
    Clase de Frame de la impresora
    :param settings: Configuracion de la impresora
    """
    def __init__(self, settings):
        """
        Constructor de clase
        :param settings: Configuracion de la impresora
        """
        if settings["TipoImpresora"] == 0:
            from .Controllers.Printers.TM_T88V import Printer
        else:
            raise Exception("No existe controlador para la impresora seleccionada")
        self.printer = Printer(settings["PuertoSerial"])
        
        if self.printer.printer and os.path.exists(settings["RutaLogo"]["Path"]):
            self.printer.cargar(settings["RutaLogo"]["Path"])
        super().__init__()
        
    def get_printer(self):
        """
        Obtiene la impresora
        """
        return self.printer

        