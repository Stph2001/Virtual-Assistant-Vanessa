import subprocess
from keyboard import press, write, press_and_release
from time import sleep
import webbrowser
from word2number import w2n
from translate import Translator

def openApp(app):
    webbrowser.open('http://' + app + '.com', new=2)

def newWindow():
    subprocess.call('start msedge', shell = True)
    sleep(1)
    write("https://www.google.com/")
    press('enter')

def closeWindow():
    press_and_release('Ctrl + W')

def changeTab(move, times):
    for i in range(times):
        if move == 'izquierda':
            press_and_release('Ctrl + Shift + Tab')
        else:
            press_and_release('Ctrl + Tab')

def changeWindow():
    press_and_release('Windows + Tab')
    sleep(1)
    press_and_release('left')
    press_and_release('enter')







