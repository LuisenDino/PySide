from ..Event import Event
from gtts import gTTS
import subprocess
import threading 
import time

import logging

import os
from PySide2 import QtCore



class SpeechSynthesis(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.event = Event("")
        self.is_speaking = False
        self.cancel = False
        self.close = False
        self.queue = []
        self.thread = threading.Thread(target=self.start_thread)
        self.thread.start()
        
    def start_thread(self):
        while not self.close:
            while len(self.queue) > 0:
                
                if self.cancel:
                    #self.event.awake_js("window.queue = []")
                    break    
                speechSynthesisUtterance = self.queue.pop(0)
                self.speak_func(str(speechSynthesisUtterance["text"]).capitalize())
                
                #self.cancel = False        
    @QtCore.Slot(list)
    def start(self, queue):
        self.cancel = True
        self.queue = queue
        self.event.awake_js("window.queue = []")
        self.cancel = False
        
            
    def _speak(self, text):
#        self.event.awake_js("window.speechSynthesis.speaking = true;")
        self.is_speaking = True
        self.engine = gTTS(text = text, lang="es", slow=False)
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/audio.ogg"
        self.engine.save(path)
        subprocess.run(["mpg123", path], stdout=subprocess.DEVNULL)
        self.event.awake_js("window.queue.shift()")
#        self.event.awake_js("window.speechSynthesis.speaking = false;")
        self.is_speaking = False


    def speak_func(self, speechSynthesisUtterance):
        while self.is_speaking: pass
        self._speak(speechSynthesisUtterance)        

    @QtCore.Slot()    
    def getVoices(self):
        return ""
    	

    def get_event(self):
        return self.event
    
    def cancel_speech(self):
        self.queue = []
        self.cancel = True

    def close_thread(self):
        self.close = True
