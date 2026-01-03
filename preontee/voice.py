import speech_recognition as sr
import pyttsx3
import threading

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self._set_female_voice()
        self.engine.setProperty("rate", 165)
        self.engine.setProperty("volume", 1.0)
        self.lock = threading.Lock()  # prevents overlapping runAndWait

    def _set_female_voice(self):
        voices = self.engine.getProperty("voices")
        for voice in voices:
            name = voice.name.lower()
            if "female" in name or "zira" in name:
                self.engine.setProperty("voice", voice.id)
                return
        if len(voices) > 1:
            self.engine.setProperty("voice", voices[1].id)

    def listen(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source)
                return self.recognizer.recognize_google(audio)
        except Exception:
            return None

    def speak(self, text):
        # Run speaking in a separate thread to prevent blocking
        def run():
            with self.lock:
                self.engine.stop()      # stop ongoing speech
                self.engine.say(text)
                self.engine.runAndWait()

        threading.Thread(target=run).start()
