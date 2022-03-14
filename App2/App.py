import sys
import logging
#import Player
from ConfigGUI.MainFrame import MainFrame as Configuration
from Player import Player as Player
#from App import Player
#from App import Configuration
import os
from screeninfo import get_monitors

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import *
from PySide2.QtGui import *

logging.basicConfig(filename=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/logs/log.log", level=logging.DEBUG, format=("%(asctime)s:%(levelname)s:%(message)s"), datefmt="%m/%d/%Y %I:%M:%S %p")


root = QApplication()

#root = tk.Tk(className="C-Media Player")

#root.setWindowTitle("C-Media")

#icon = QIcon()
#icon.addFile(u"/home/luis/Escritorio/PySide/App/Media/LOGO-CMedia.png", QSize(), QIcon.Normal, QIcon.Off)
#Form.setWindowIcon(icon)
if len(sys.argv) == 1:
    try:
        player = Player()
        player.show()
    except Exception as e:
        logging.error(str(e))
elif "--config" in sys.argv:
    try:
        config = Configuration()
        config.show()
    except Exception as e:
        logging.error(str(e))
else:
    logging.error("Opcion no permitida")

"""
image = tk.PhotoImage(file=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/LOGO-CMedia.png")
root.tk.call('wm', 'iconphoto', root._w, image)
monitors = get_monitors()
for monitor in monitors:
    if monitor.is_primary:
        h=250
        w=402
        root.geometry(str(w)+"x"+str(h)+"+"+str(monitor.width//2-w//2)+"+"+str(monitor.height//2-h//2)) 
root.configure(background="#f3f3f3")
#root.configure(background="#0a3749")

img = tk.PhotoImage(file=os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/Media/SplashScreen.png")
#tk.Label(root, image=img, bg="#0a3749").pack(fill=tk.BOTH, expand=True)
tk.Label(root, image=img, bg="#f3f3f3").pack(fill=tk.BOTH, expand=True)
root.overrideredirect(True)


    

root.after(2000, call_app)
"""
sys.exit(root.exec_())