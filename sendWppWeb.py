#!/usr/bin/python
# -*- coding: cp1252 -*-
from time import sleep
import pyautogui
import psutil
import os
import cv2
from win32 import win32gui
import win32con
import webbrowser as wb


def Running(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return False
    return False


photos = {'contacts': ['./whatsappContact.png', './whatsappContact2.png']}


def whatsappWeb():
    wb.open(f'https://web.whatsapp.com')
    sleep(5)
    try:
        window = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
    except:
        print('No se pudo maximizar la ventana de WhatsApp')
        return

    coordinates1 = None
    sleep(2)

    while coordinates1 is None:
        for photo in photos['contacts']:
            photo = cv2.imread(photo)
            coordinates1 = pyautogui.locateOnScreen(photo)
            if coordinates1 is None:
                pass
            else:
                x = coordinates1.left
                y = coordinates1.top
                pyautogui.click(x, y)
                sleep(1)
                break
    if coordinates1 is None:
        print('No se encontró al contacto')
        return

if __name__ == '__main__':
    whatsappWeb()