import json
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import os

class PrinterTabFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.setEnabled(False)
        self.path = ""
        self.get_settings()

        
        

        #Seleccionar el fondo
        bg = QPalette()
        bg.setColor(QPalette.Window, "#eef1f2")
        self.setAutoFillBackground(True)
        self.setPalette(bg)

        #Configuracion del Layout
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)

        #Fila1
        self.path_label = QLabel("Logo:")
        self.mainLayout.addWidget(self.path_label, 0, 0, 1, 2)
        self.path_label.setFixedHeight(50)
        self.path_entry = QLineEdit(self.path)
        self.mainLayout.addWidget(self.path_entry, 0, 2, 1, 5)
        self.file_name_button = QPushButton("...")
        self.file_name_button.clicked.connect(self.select_file)
        self.mainLayout.addWidget(self.file_name_button, 0, 7)

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
            path = self.settings["Ruta"]
        with open(path, "r", encoding="utf-8-sig") as file:
            settings = json.load(file)
            for pantalla in settings["Pantallas"]:
                for controller in pantalla["Controles"]:
                    if "Control.Impresion.dll" in controller["NombreArchivo"]:
                        self.setEnabled(True)
                        self.path = controller["ObjetoBase"]["RutaLogo"]["Path"]

    def save_settings(self):
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/config.json"
        with open(path, "r") as file:
            settings = json.loads(file.read())

        if "$" == settings["Ruta"][0]:
            var =  os.environ[settings["Ruta"][1:settings["Ruta"].find("/")]]
            path = var + settings["Ruta"][settings["Ruta"].find("/"):]
        else:
            path = self.settings["Ruta"]
        with open(path, "r", encoding="utf-8-sig") as file:
            settings = json.load(file)
            for pantalla in range(len(settings["Pantallas"])):
                for controller in range(len(settings["Pantallas"][pantalla]["Controles"])):
                    if "Control.Impresion.dll" in settings["Pantallas"][pantalla]["Controles"][controller]["NombreArchivo"]:
                        settings["Pantallas"][pantalla]["Controles"][controller]["ObjetoBase"]["RutaLogo"]["Path"] = self.path_entry.text()
                        
        
        with open(path, "w", encoding="utf-8-sig") as file:
            file.write(json.dumps(settings))

    def select_file(self):
        """
        Abre un cuadro de dialogo para la seleccion del archivo de configuracion ccmj y lo guarda en la variable
        """
        file_name = QFileDialog().getOpenFileName(self, "Seleccionar Archivo", filter="Config files (*bmp)")[0]
        if file_name != "":
            self.file_name = file_name
            self.path_entry.clear()
            self.path_entry.insert(file_name)