import speech_recognition as sr
from actions import action
from answer import Answer
import pygame
import time
from speaking import speak
import datetime

def Speech_Recognition():
    sr.Microphone(device_index=1)
    r = sr.Recognizer()
    r.energy_threshold = 3000
    r.dynamic_energy_threshold = False
    m = sr.Microphone()
    ultima_accion = ' '
    switch = False
    name = 'Sebastián'
    with m as source:
        r.adjust_for_ambient_noise(source)
        while True:
            r, source, record = Answer(r, source)
            if 'vanessa' in record:
                hora = datetime.datetime.now().hour
                s = ''
                if hora<12:
                    s = 'Buenos días ' + name
                elif hora>=12 and hora<=18:
                    s = 'Buenas tardes ' + name
                else:
                    s = 'Buenas noches ' + name
                switch = True
                pygame.mixer.music.play()
                time.sleep(1)
                speak(s)
            elif 'adiós' in record and 'vanessa' in record:
                speak('Nos vemos luego ')
                switch = False
            elif record==' ':
                pass
            elif switch == True:
                if 'otra vez' in record:
                    ultima_accion = action(r,source, ultima_accion)
                else:
                    ultima_accion = action(r,source, record)

            print(str(switch))