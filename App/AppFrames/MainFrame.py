import logging
#import tkinter as tk
from PySide2.QtWidgets import QMainWindow
import sys
from .CodeReaderFrame import CodeReaderFrame
from .WebViewFrame import WebViewFrame
from .PrinterFrame import PrinterFrame
from cefpython3 import cefpython as cef

class MainFrame(QMainWindow):
    """
    Clase de pantalla principal
    :param root: tk.Tk. aplicacion tkinter.
    :param config: dic. Configuracion de la aplicacion.
    """
    def __init__(self, root, controllers):
        """
        Constructor de clase
        :param root: tk.Tk. aplicacion tkinter.
        :param config: dic. Configuracion de la aplicacion.
        """
        self.webview_frame = None
        self.printer_frame = None
        self.code_reader_frame = None
        self.controllers = controllers


        #MainFrame
        super().__init__()
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.master.bind("<Configure>", self.on_root_configure)
        self.bind("<Configure>", self.on_configure)
        
        self.apis = {}
        
        for controller in controllers:
            
            #BrowserFrame
            if "Control.NavegadorWebChrome.dll" in controller["NombreArchivo"]:
                self.webview_frame = WebViewFrame(self, settings = controller["ObjetoBase"])
                

            #PrinterFrame
            elif "Control.Impresion.dll" in controller["NombreArchivo"]:
                self.printer_frame = PrinterFrame(controller["ObjetoBase"])
                self.apis["printer"] = self.printer_frame.get_printer()

            elif "Control.Captura.CodigoBarras.Omnidireccional.Honeywell.dll" in controller["NombreArchivo"]:
                self.code_reader_frame = CodeReaderFrame(controller["ObjetoBase"])
                self.apis["code_reader"] = self.code_reader_frame.get_code_reader()
                
        #tk.Grid.rowconfigure(self, 1, weight=1)
        #tk.Grid.columnconfigure(self, 0, weight=1)
        #tk.Grid.rowconfigure(self, 1, weight=1)
        #tk.Grid.columnconfigure(self, 0, weight=1)
        #self.pack(fill=tk.BOTH, expand=tk.YES)
        """if(self.webview_frame):
            try:
                app_settings = {
                    "downloads_enabled" : True
                }
                cef.Initialize(settings =  app_settings)
                cef.PostTask(cef.TID_UI, lambda : self.webview_frame.load_apis(self.apis))
                
            except Exception as e :
                logging.error(str(e))
                return e 
        """
        self.setCentralWidget(self.webview_frame) 
        self.show()
        

    def on_close(self):
        """
        Llama a los metodos de cierre
        El metodo se ejecuta al cerrar la aplicacion
        """
        if self.webview_frame:
            self.webview_frame.on_root_close()
        self.master.destroy()
        if(self.webview_frame):
            try:
                cef.Shutdown()  
            except Exception as e:
                logging.error(str(e))
        if self.code_reader_frame:
            self.code_reader_frame.get_code_reader().disconnect()
        sys.exit()

    def on_root_configure(self, _):
        """
        Llama a los metodos de configuracion de la aplicacion
        Se ejecuta cuando se configura la aplicacion
        """
        if self.webview_frame:
            self.webview_frame.on_root_configure()
    
    def on_configure(self, event):
        """
        Llama a los metodos de configuracion de la vista
        se ejecuta cuando se configura la vista
        :param event: event. evento de configuracion
        """
        if self.webview_frame:
            width = event.width
            height = event.height
            self.webview_frame.on_mainframe_configure(width, height)

    def get_WebView_frame(self):
        """
        Obtiene el frame del contenedor web
        """
        return self.webview_frame

    def get_printer_frame(self):
        """
        Obtiene el frame de la impresora
        """
        return self.printer_frame
        
    def get_code_reader_frame(self):
        return self.code_reader_frame

    