from ..Event import Event
import pyttsx3

class SpeechSynthesis():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'spanish')
        self.engine.setProperty("rate", 180)
        self.event = Event("")
        

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_event(self):
        return self.event