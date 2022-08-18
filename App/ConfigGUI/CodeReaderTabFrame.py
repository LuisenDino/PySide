import json
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


import os

class CodeReaderTabFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.setEnabled(False)
        self.readers = ["Honeywell", "Magellam"]
        self.get_settings()
        
        

        #Seleccionar el fondo
        bg = QPalette()
        bg.setColor(QPalette.Window, "#eef1f2")
        self.setAutoFillBackground(True)
        self.setPalette(bg)

        #Configuracion del Layout
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)


        #Fila2
        
        self.reader_label = QLabel("Lector:")
        self.mainLayout.addWidget(self.reader_label, 0, 0, 1, 2)
        self.combo_box_reader = QComboBox()
        self.combo_box_reader.addItems(self.readers)
        self.combo_box_reader.setCurrentIndex(self.index)
        self.mainLayout.addWidget(self.combo_box_reader, 0, 2, 1, 6)

        #Fila6
        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.save_settings)
        self.mainLayout.addWidget(self.save_button, 2, 3, 1, 2)


    def get_settings(self):
        """
        Obtiene la configuracion del archivo json y las guarda en un atributo de la clase
        """

        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/config.json"
        with open(path, "r") as file:
            settings = json.loads(file.read())

        if "$" == settings["Ruta"][0]:
            var =  os.environ[settings["Ruta"][1:settings["Ruta"].find("/")]]
            path = var + settings["Ruta"][settings["Ruta"].find("/"):]
        else:
            path = settings["Ruta"]
        with open(path, "r", encoding="utf-8-sig") as file:
            settings = json.load(file)
            for pantalla in settings["Pantallas"]:
                for controller in pantalla["Controles"]:
                    if "Control.Captura.CodigoBarras.Omnidireccional" in controller["NombreArchivo"]:
                        self.setEnabled(True)
                        name = controller["NombreArchivo"][45:]
                        name = name[:name.find(".")]
                        self.index = self.readers.index(name)

    def save_settings(self):
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/config.json"
        with open(path, "r") as file:
            settings = json.loads(file.read())

        if "$" == settings["Ruta"][0]:
            var =  os.environ[settings["Ruta"][1:settings["Ruta"].find("/")]]
            path = var + settings["Ruta"][settings["Ruta"].find("/"):]
        else:
            path = settings["Ruta"]
        with open(path, "r", encoding="utf-8-sig") as file:
            settings = json.load(file)
            for pantalla in range(len(settings["Pantallas"])):
                for controller in range(len(settings["Pantallas"][pantalla]["Controles"])):
                    if "Control.Captura.CodigoBarras.Omnidireccional" in settings["Pantallas"][pantalla]["Controles"][controller]["NombreArchivo"]:
                        settings["Pantallas"][pantalla]["Controles"][controller]["NombreArchivo"] = "Control.Captura.CodigoBarras.Omnidireccional." + self.combo_box_reader.currentText() + ".dll"
        
        with open(path, "w", encoding="utf-8-sig") as file:
            file.write(json.dumps(settings))

