from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

#Clases Externas
from .ToggleButton import ToggleButton

#Otras librerías
import json
import os


class WebTabFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.setEnabled(False)
        self.url = ""
        self.nav_bar = False
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
        self.url_label = QLabel("Url:")
        self.mainLayout.addWidget(self.url_label, 0, 0, 1, 2)
        self.url_label.setFixedHeight(50)
        self.url_entry = QLineEdit(self.url)
        self.mainLayout.addWidget(self.url_entry, 0, 2, 1, 5)

        #Fila2
        self.nav_bar_label = QLabel("Barra de Navegación:")
        self.nav_bar_label.setFixedHeight(50)   
        self.mainLayout.addWidget(self.nav_bar_label, 1, 0, 1, 2)
        self.nav_bar_button = ToggleButton(self.nav_bar)
        self.mainLayout.addWidget(self.nav_bar_button, 1,2 , 1, 2)
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
                    if "Control.NavegadorWebChrome.dll" in controller["NombreArchivo"]:
                        self.setEnabled(True)
                        self.url = controller["ObjetoBase"]["UrlInicio"]
                        self.nav_bar = controller["ObjetoBase"]["MostrarBarraNavegacion"]

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
                    if "Control.NavegadorWebChrome.dll" in settings["Pantallas"][pantalla]["Controles"][controller]["NombreArchivo"]:
                        settings["Pantallas"][pantalla]["Controles"][controller]["ObjetoBase"]["UrlInicio"] = self.url_entry.text()
                        settings["Pantallas"][pantalla]["Controles"][controller]["ObjetoBase"]["MostrarBarraNavegacion"] = self.nav_bar_button.get()
        
        with open(path, "w", encoding="utf-8-sig") as file:
            file.write(json.dumps(settings))



