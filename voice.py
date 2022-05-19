import pyautogui
import speech_recognition as sr
from answer import Answer
from speaking import speak
import subprocess
import datetime
import webbrowser as wb
from ReproduceSong import reproduceSong, songNumber
from webFunctions import changeApp
from readContacts import matcher
from time import sleep
import pygame

dic = {'uno': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
       '11': 11, '12': 12, '13': 13, '14': 14, '15': 15}


def speechRecognition():
    sr.Microphone(device_index=1)
    r = sr.Recognizer()
    r.energy_threshold = 3000
    r.dynamic_energy_threshold = False
    m = sr.Microphone()
    aux = ' '
    with m as source:
        r.adjust_for_ambient_noise(source)
        pygame.mixer.music.play()
        while True:
            r, source, record = Answer(r, source)
            if 'otra vez' in record:
                record = aux

            if ('silencio' in record or 'adiós' in record) and 'vanessa' in record:
                speak('Nos vemos luego ')
                break

            elif 'pantalla' in record and 'completa' in record:
                pyautogui.hotkey('f')

            elif 'clic' in record:
                pyautogui.click()

            elif all([any(['cierra' in record, 'cerrar' in record]), 'pestaña' in record]):
                pyautogui.hotkey('ctrl', 'w')

            elif ('cerrar' in record or 'cierra' in record) and ('ventana' in record or 'aplicación' in record or 'app' in record):
                pyautogui.hotkey('alt', 'f4')

            elif 'borra' in record or 'borrar' in record:
                pyautogui.hotkey('backspace')

            elif 'pestaña' in record or 'tab' in record:
                idx = list(record)[len(record)-1]
                if idx.isdigit():
                    with pyautogui.hold('Ctrl'):
                        pyautogui.press(idx)

            elif 'letra' in record:
                letra = record.replace("letra", '')
                letra = letra.strip()
                if letra != ' ' and len(letra) == 1:
                    if letra.isalpha():
                        pyautogui.hotkey(letra)

            elif 'pausa' in record or 'corre' in record:
                pyautogui.hotkey('space')

            elif 'buscar' in record or 'barra de busqueda' in record:
                pyautogui.hotkey('/')

            elif 'silencio' in record:
                pyautogui.hotkey('volumemute')

            elif 'qué hora es' in record:
                tiempo = datetime.datetime.now()
                hora = tiempo.hour
                minutos = tiempo.minute
                print(str(hora) + ':' + str(minutos))
                speak(f'Hora: {hora} con {minutos} minutos')

            elif 'enter' in record or 'center' in record:
                pyautogui.hotkey('enter')

            elif ('minimiza' in record or 'minimizar' in record) and 'ventana' in record:
                with pyautogui.hold('alt'):
                    with pyautogui.hold('space'):
                        pyautogui.press('n')

            elif ('maximiza' in record or 'maximizar' in record) and 'ventana' in record:
                sleep(1)
                pyautogui.keyDown('alt')
                pyautogui.keyDown('space')
                pyautogui.press('x')
                pyautogui.keyUp('space')
                pyautogui.keyUp('alt')


            elif (('nueva' in record and 'pestaña' in record)) or 'google' in record:
                wb.open('http://google.com', new=2)

            elif ('cambiar' in record or 'cambia' in record or 'cambio' in record) and (
                    'app' in record or 'aplicación' in record or 'ventana' in record):
                changeApp()

            elif 'copia' in record and 'texto' in record:
                pyautogui.hotkey('ctrl', 'a')

            elif 'baja' in record or 'abajo' in record or 'bajo' in record:
                pyautogui.scroll(-100)

            elif 'sube' in record or 'arriba' in record:
                pyautogui.hotkey('up')

            elif 'youtube' in record:
                speak('¿Qué deseas buscar?')
                text = Answer(r, source, 2, 5)
                if text == 'None': return
                wb.open("https://www.youtube.com/results?search_query=" + text)
                pyautogui.moveTo(719, 320)

            elif 'spotify' in record:
                speak("Cuál es la canción?")
                r, source, song = Answer(r, source, 2, 5)
                print(song)
                if (song is ' ') or ("no sé" == song) or ("no lo sé" == song):
                    speak("Cuál es el nombre del artista?")
                    r, source, autor = Answer(r, source, 2, 5)
                    if autor is ' ': return record
                    reproduceSong(song, autor)
                    speak("¿Cuál número de canción desea?")
                    r, source, ans = Answer(r, source, 2, 5)
                    if ans is ' ': return record
                    number = dic[ans]
                    songNumber(number)
                else:
                    reproduceSong(sng=song)

            elif 'whatsapp' == record:
                preguntas = ['¿A quién se lo quieres enviar?', '¿Cuál es el mensaje?']
                cmd = "python .\sendWpp.py"
                p = subprocess.Popen(cmd, shell=True)
                out, err = p.communicate()
                speak(preguntas[0])

            elif 'escribe' in record or 'escribir' in record:
                speak("¿Qué quieres escribir?")
                r, source, ans = Answer(r, source, 2, 5)
                if ans is None: return
                pyautogui.write(ans)

            elif 'whatsapp' in record and 'web' in record:
                preguntas = ['¿A quién se lo quieres enviar?', '¿Cuál es el mensaje?']
                cmd = "python .\sendWppWeb.py"
                p = subprocess.Popen(cmd, shell=True)
                out, err = p.communicate()
                speak(preguntas[0])

            elif 'nombre' in record or 'nombres' in record:
                speak("¿Qué nombre buscas?")
                r, source, ans = Answer(r, source, 2, 8)
                ans = ans.capitalize()
                out = matcher(ans)
                if len(out)==1:
                    pyautogui.write(out[0])
                elif len(out)>1:
                    speak('¿Quisiste decir ')
                    for i, name in enumerate(out):
                        speak(name + 'ó ')
                        print(str(i+1)+': ' + name)
                    speak('Elige número de contacto')
                    r, source, ans = Answer(r, source, 2, 8)
                    if ans is ' ': return record
                    if dic.get(ans):
                        number = dic[ans]
                        pyautogui.write(out[number-1])

            if record != ' ': aux = record


if __name__ == '__main__':
    pygame.mixer.init()
    pygame.mixer.music.load(".\sound.mp3")
    speechRecognition()