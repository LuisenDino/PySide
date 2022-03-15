from .ToggleButton import ToggleButton
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import os
import json

class GeneralTabFrame(QWidget):
    """
    Clase de vista de configuracion General
    """ 
    def __init__(self):
        super().__init__()
        self.settings = {}
        self.get_settings()

        self.file_name = self.settings["Ruta"]
        self.fullscreen = self.settings["PantallaCompleta"]
        self.window_border = self.settings["MostrarBordeVentana"]
        self.on_top = self.settings["SiempreVisible"]
        self.w = self.settings["AnchoRequerido"]
        self.h = self.settings["AltoRequerido"]
        self.t = self.settings["TopRequerido"]
        self.l = self.settings["LeftRequerido"]

        #Seleccionar el fondo
        bg = QPalette()
        bg.setColor(QPalette.Window, "#eef1f2")
        self.setAutoFillBackground(True)
        self.setPalette(bg)

        #Configuracion del Layout
        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)
        
        #Fila1
        self.mainLayout.addWidget(QLabel("Archivo de recursos:"), 0, 0, 1, 2)
        self.file_name_entry =  QLineEdit(self.file_name)
        self.file_name_entry.setReadOnly(True)
        self.mainLayout.addWidget(self.file_name_entry, 0, 2, 1, 5)
        self.file_name_button = QPushButton("...")
        self.file_name_button.clicked.connect(self.select_file)
        self.mainLayout.addWidget(self.file_name_button, 0, 7)

        #Fila2
        self.mainLayout.addWidget(QLabel("Pantalla completa:"), 1, 0, 1, 2)
        self.fullscreen_button = ToggleButton(self.fullscreen)
        self.mainLayout.addWidget(self.fullscreen_button, 1,2 , 1, 2)

        #Fila3
        self.mainLayout.addWidget(QLabel("Borde Ventana:"), 2, 0, 1, 2)
        self.window_border_button = ToggleButton(self.window_border)
        self.mainLayout.addWidget(self.window_border_button, 2,2, 1, 2)
        
        #Fila4
        self.mainLayout.addWidget(QLabel("Siempre Visible:"), 3, 0, 1, 2)
        self.on_top_button = ToggleButton(self.on_top)
        self.mainLayout.addWidget(self.on_top_button, 3,2, 1, 2)
        #Fila5
        self.mainLayout.addWidget(QLabel("Ancho"), 4, 0)
        self.width_entry = QLineEdit(str(self.w))
        self.mainLayout.addWidget(self.width_entry, 4, 1)
        self.mainLayout.addWidget(QLabel("Alto"), 4, 2)
        self.height_entry = QLineEdit(str(self.h))
        self.mainLayout.addWidget(self.height_entry, 4, 3)
        self.mainLayout.addWidget(QLabel("Superior"), 4, 4)
        self.top_entry = QLineEdit(str(self.t))
        self.mainLayout.addWidget(self.top_entry, 4, 5)
        self.mainLayout.addWidget(QLabel("Izquierda"), 4, 6)
        self.left_entry = QLineEdit(str(self.l))
        self.mainLayout.addWidget(self.left_entry, 4, 7)

        #Fila6
        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.save)
        self.mainLayout.addWidget(self.save_button, 5, 3, 1, 2)

        #Imagen
        img =  QLabel()
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/cog_edit.png"
        pixmap = QPixmap(path)
        img.setPixmap(pixmap)

        self.mainLayout.addWidget(img, 6, 7, 1, 1, Qt.AlignRight)

    def select_file(self):
        file_name = QFileDialog().getOpenFileName(self, "Seleccionar Archivo", filter="Config files (*.ccmj)")[0]
        if file_name != "":
            self.file_name = file_name
            self.file_name_entry.clear()
            self.file_name_entry.insert(file_name)
            


    def save(self):
        """
        Guarda la informacion en el archivo json de configuracion
        """

        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/config.json"
        
        with open(path, "w") as file:
            
            settings = {
                "Ruta" : self.file_name,
                "PantallaCompleta" : self.fullscreen_button.get(), 
                "SiempreVisible" : self.on_top_button.get(),
                "MostrarBordeVentana" : self.window_border_button.get(), 
                "AnchoRequerido" : int(self.width_entry.text()),
                "AltoRequerido" : int(self.height_entry.text()),
                "TopRequerido" : int(self.top_entry.text()),
                "LeftRequerido" : int(self.left_entry.text())
            }

            file.write(json.dumps(settings))

    def get_settings(self):
        """
        Obtiene la configuracion del archivo json y las guarda en un atributo de la clase
        """

        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/config.json"
        with open(path, "r") as file:
            self.settings = json.loads(file.read())