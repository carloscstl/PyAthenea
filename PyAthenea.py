import speech_recognition as sr
import pyttsx3, pywhatkit

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def assist(command):
    if 'athenea' in command:
        command=command.replace('athenea','')
        if 'reproduce' in command:
            music= command.replace('reproduce','')
            print("Reproduciendo"+ music)
            talk("Reproduciendo"+music)
            pywhatkit.playonyt(music)
    elif 'atenea' in command:
        command=command.replace('atenea','')
        if 'reproduce' in command:
            music= command.replace('reproduce','')
            print("Reproduciendo"+ music)
            talk("Reproduciendo"+music)
            pywhatkit.playonyt(music)



#Escucha el comando si se nombra athenea o atena el comando lo pasa a la funcion assist

try:
    with sr.Microphone() as source:
        print("Escuchando ... ")
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language = "es-MX")
        command = command.lower()
        if 'athenea' in command:
            assist(command)
        elif 'atenea' in command:
            assist(command)
except:
    pass
