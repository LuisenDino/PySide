from ..Event import Event
from gtts import gTTS
import subprocess
import threading 

import os

class SpeechSynthesis():
    def __init__(self):
        self.event = Event("")
        
        
    def speak(self, speechSynthesisUtterance):
        self.thread = threading.Thread(target=self.speak_func, args=[speechSynthesisUtterance["text"]])
        self.thread.start()

    def speak_func(self, speechSynthesisUtterance):
        
        self.engine = gTTS(text = speechSynthesisUtterance, lang="es", slow=False)
        path = os.path.expanduser('~')+"/.config/Ciel/C-Media_Player/configs/audio.ogg"
        self.engine.save(path)
        subprocess.call(["mpg123", path])

    def getVoices(self):
        return ""
    	
    def speaking(self):
        return False

    def get_event(self):
        return self.event
    
    def cancel(self):    
    	pass