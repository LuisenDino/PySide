#http://192.168.1.138:8823/Player.aspx?Recurso=Tablero1%20OfficeMax&idoficina=1&idtablero=1&fullscreen=1

from App.AppFrames.Controllers.Printers.NCR7197 import Printer

def main():
    printer = Printer({"NombrePuerto":"USB"})
    printer.imprimir("Linea1\nLinea2\nLinea3\nLinea4\nLinea5\nLinea6\nLinea7\nLinea8")

if __name__ == "__main__":
    main()