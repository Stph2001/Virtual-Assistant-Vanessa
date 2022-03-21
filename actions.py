import pygame
import datetime
from speaking import speak
from answer import Answer
from sendWpp1 import whatsappMsg
from contactoWpp import match, contacts
import pyautogui as py
import difflib
from webFunctions import openApp, newWindow, closeWindow,changeTab, changeWindow
from time import sleep

def action(r, source, record):
    if 'qué hora es' in record:
        tiempo = datetime.datetime.now()
        hora = tiempo.hour
        minutos = tiempo.minute
        print(str(hora) + ':' + str(minutos))
        speak(f'Hora: {hora} con {minutos} minutos')
    
    elif 'envía' in record and 'whatsapp' in record:
        preguntas = ['¿A quién se lo quieres enviar?', '¿Cuál es el mensaje?']
        speak(preguntas[0])
        r, source, name = Answer(r, source,2,5)
        name = match(name)
        while name.lower() not in contacts:
            speak('Nombre no encontrado')
            speak(preguntas[0])
            r, source, name = Answer(r, source,2,5)
            name = match(name)            
        print(name)
        speak(preguntas[1])
        r, source, msg = Answer(r, source, 2, 5)
        while msg == ' ':
            speak('Mensaje no encontrado')
            speak(preguntas[1])
            r, source, msg = Answer(r, source, 2, 5)
        try:
            whatsappMsg(name, msg)
        except Exception:
            speak('No se pudo enviar el mensaje')
    
    elif 'hasta pronto' in record:
        speak('Hasta pronto.')
        py.hotkey('win', 'up')
        py.click(x=1889,y=9)
        exit(0)

    elif 'abre' in record or 'abrir' in record:
        app = record.replace('abre ', '')
        openApp(app)

    #Cundo esté en edge, se activan algunas funciones, sino no
    elif ('cambiar' in record or 'cambia' in record or 'cambio' in record) and 'aplicación' in record:
        appDictionary = {'whatsapp': ['wpp.png', 'whatsappContact.png'], 'google': ['edge.png','edge2.png', 'edge3.png'], 'visual studio': ['vscode.png', 'vscode2.png']}
        speak('Que aplicación busca?')
        r, source, app = Answer(r, source, 2, 3)
        while app not in appDictionary.keys():
            speak('Aplicación no encontrada')
            speak('¿Qué aplicación busca?')
            r, source, app = Answer(r, source, 2, 5)
        speak('Buscando..')
        img = None  
        found = False
        while found == False:
            changeWindow()
            for photo in appDictionary[app]:
                print(photo)
                sleep(2)
                try:
                    img = py.locateOnScreen(photo, grayscale = True)
                    py.click(100, img.top+15)
                    if img != None: 
                        found = True
                        break
                except Exception:
                    pass
        speak('Aplicación encontrada')
            
    elif 'nueva' in record and 'ventana' in record:
        newWindow()

    elif ('cambia' in record or 'cambiar' in record or 'cambio' in record) and 'pestaña' in record:
        speak("¿Hacia dónde?")
        try:
            wordToNum = {'una': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete':7, 'ocho':8, 'nueve':9, 'diez':10}
            r, source, ans = Answer(r, source, 2, 5)
            move = ans.split()[len(ans.split())-1]
            times = wordToNum[ans.split()[0]]
            changeTab(move, times)
        except:
            speak('No se pudo cambiar de pestaña')
    
    elif 'cierra' in record and 'pestaña' in record:
        closeWindow()

    else:
        speak('No entendí el mensaje.')

    return record