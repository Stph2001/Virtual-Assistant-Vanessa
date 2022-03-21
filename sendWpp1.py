from pyautogui import click
from time import sleep
from keyboard import press, write
import subprocess
import pyautogui

def whatsappMsg(name, msg):
    try:
        subprocess.Popen(["cmd", "/C", "start whatsapp://"], shell=True)
        print('Se abrió WhatsApp Desktop')
        sleep(13)
    except:
        print('Debe instalar Whatsapp Desktop')
    try:
        coordinates1 = pyautogui.locateOnScreen('whatsappContact.png')
        #locateAllOnScreen
        pyautogui.click(coordinates1.left, coordinates1.top)
        sleep(2)
        write(name)
    except:
        print('No se encontró al contacto')
    
    try:
        sleep(3)
        coordinates2 = pyautogui.locateOnScreen('whatsappChats.png')
        pyautogui.click(coordinates2.left, coordinates2.top)
        sleep(3)
        coordinates3 = pyautogui.locateOnScreen('whatsappMessage.png')
        pyautogui.click(coordinates3.left, coordinates3.top)
        sleep(2)
        write(msg)
        sleep(2)
        press('enter')
        print('Se entregó el mensaje')
    except:
        print('Error al escribir el mensaje')

# whatsappMsg('Gianpaul', 'tas chekando los cursos?')