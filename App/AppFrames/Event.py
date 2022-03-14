class Event():
    """
    Clase que permite el manejo de eventos de la aplicación
    :param nombre_js: str. nombre del controlador al que pertenece el evento
    """
    def __init__(self, nombre_js):
        """
        Clase que permite el manejo de eventos de la aplicación
        :param nombre_js: str. nombre del controlador al que pertenece el evento
        """
        self.value = False
        self.nombre_js = nombre_js
        self.function = ""
        self.params = ""
        self.browser = None

    def awake(self, function, params):
        """
        Enciende el evento
        :param function: nombre de la funcion a llamar en js
        :param params: list. Lista de los parametros a la funcion js
        """
        self.value = True
        self.function = function
        self.params = params
        if self.browser:
            js = "Ciel.MPC.WebPlayer.Controles."+self.nombre_js+"."+self.function+"("+",".join(self.params)+")"
            self.browser.ExecuteJavascript(js)
            self.clear()

    def clear(self):
        """
        Limpia el evento
        """
        self.value = False
        self.function = ""
        self.params = ""

    def get(self):
        """
        Obtiene el evento
        """
        return self.value

    def set_browser(self, browser):
        """
        Establece el navegador en el que se desplegara el evento
        """
        self.browser = browser