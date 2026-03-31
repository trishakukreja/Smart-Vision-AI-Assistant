import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    # Optional: adjust rate
    engine.setProperty('rate', 150) 
    engine.say(text)
    engine.runAndWait()