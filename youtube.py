from speaking import speak
import webbrowser as wb
import pyautogui
from answer import AnswerSeconds
from global_variables import r2, m
from time import sleep

if __name__ == '__main__':
    r2.energy_threshold = 3000
    r2.dynamic_energy_threshold = False
    cnt = 0
    with m as source:
        r2.adjust_for_ambient_noise(source)
        while True:
            speak('¿Qué desea buscar?')
            r, source, text = AnswerSeconds(r2, source,2,10)
            if len(text) >= 3:
                speak('Abriendo')
                wb.open("https://www.youtube.com/results?search_query=" + text)
                sleep(3)
                pyautogui.keyDown('alt')
                pyautogui.keyDown('space')
                pyautogui.press('x')
                pyautogui.keyUp('space')
                pyautogui.keyUp('alt')
                sleep(1)
                pyautogui.moveTo(719, 320)
                speak('Tarea Completada')
                break
            elif cnt >0:
                speak('Lo lamento')
                speak('No se encontraron resultados')
                break
            speak('No entendí')
            cnt +=1