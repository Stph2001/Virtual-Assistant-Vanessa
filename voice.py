import os
import pyautogui
from answer import Answer
from speaking import speak
import subprocess
import datetime
import webbrowser as wb
from webFunctions import changeApp
from readContacts import matcher
from time import sleep
import pygame
from global_variables import r1, m

dic = {'uno': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
       '11': 11, '12': 12, '13': 13, '14': 14, '15': 15}


def speechRecognition(r, m):
    r.energy_threshold = 3000
    r.dynamic_energy_threshold = False
    aux = ' '
    with m as source:
        r.adjust_for_ambient_noise(source)
        pygame.mixer.music.play()
        os.system('cls')
        while True:
            r, source, record = Answer(r, source)
            if 'otra vez' in record:
                record = aux

            if ('silencio' in record or 'adiós' in record) and 'vanessa' in record:
                speak('Nos vemos luego ')
                break

            elif 'pantalla' in record and 'completa' in record:
                pyautogui.hotkey('f')

            elif 'haz clic' in record:
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

            elif ('minimiza' in record or 'minimizar' in record) and ('ventana' in record or 'pantalla'):
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
                cmd = f'python .\youtube.py'
                p = subprocess.Popen(cmd, shell=True)
                p.communicate()

            elif ('reproduce' in record or 'pon' in record) and 'canción' in record:
                cmd = f'python .\\reproduceSong.py'
                p = subprocess.Popen(cmd, shell=True)
                p.communicate()

            elif ('busca' in record or 'encuentra' in record) and ('artista' in record or 'cantante'):
                cmd = f'python .\\findArtist.py'
                p = subprocess.Popen(cmd, shell=True)
                p.communicate()

            elif 'whatsapp' == record:
                preguntas = ['¿A quién se lo quieres enviar?', '¿Cuál es el mensaje?']
                cmd = "python .\sendWpp.py"
                p = subprocess.Popen(cmd, shell=True)
                out, err = p.communicate()
                speak(preguntas[0])

            elif 'escribe' in record or 'escribir' in record:
                speak("¿Qué quieres escribir?")
                r, source, ans = Answer(r, source)
                if ans is None: return
                pyautogui.write(ans)

            elif 'whatsapp' in record and 'web' in record:
                preguntas = ['¿A quién se lo quieres enviar?', '¿Cuál es el mensaje?']
                cmd = "python .\sendWppWeb.py"
                p = subprocess.Popen(cmd, shell=True)
                out, err = p.communicate()
                speak(preguntas[0])

            elif ('elige' in record or 'lista' in record) and ('nombre' in record or 'nombres' in record):
                speak("¿Qué nombre buscas?")
                r, source, ans = Answer(r, source)
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
                    r, source, ans = Answer(r, source)
                    if ans is ' ': continue
                    if dic.get(ans):
                        number = dic[ans]
                        pyautogui.write(out[number-1])

            if record != ' ': aux = record

        cmd = "python .\wpp.py"
        p = subprocess.Popen(cmd, shell=True)
        out, err = p.communicate()


if __name__ == '__main__':
    pygame.mixer.init()
    pygame.mixer.music.load(".\sound.mp3")
    speechRecognition(r1, m)