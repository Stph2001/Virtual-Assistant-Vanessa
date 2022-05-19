from time import sleep
import pyautogui
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser as wb

def songNumber(number):
    wb.open(result["tracks"]["items"][number - 1]["uri"])
    sleep(5)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('space')
    pyautogui.press('x')
    pyautogui.keyUp('space')
    pyautogui.keyUp('alt')
    sleep(1)
    pyautogui.press('enter')

def reproduceSong(sng='', autor = ''):
    flag = 0
    client_ID = '91a4b17721e34dd3bfde327815aa5386'
    pwd_ID = 'af6f59bceeb645ecbc93245c2fa51033'
    # Con autor y Nombre de sus canciones
    if len(autor) > 0:
        flag = 1
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_ID, pwd_ID))
        global result
        result = sp.search(autor)
        if result is None:
            print("No se encontró al artista")
            return

        for i in range(len(result["tracks"]["items"])):
            name_song = result["tracks"]["items"][i]["name"]
            print(str(i + 1) + ': ' + name_song)
            print()

        return

    # Sin autor
    if flag == 0:
        # sng = sng.replace(" ", "%20")
        wb.open(f'spotify:search:')
        sleep(15)
        pyautogui.write(sng)
        sleep(2)
        pyautogui.press('enter')
        sleep(1)
        pyautogui.press('tab')
        for i in range(2):
            pyautogui.press('enter')
            sleep(2)
        return

# reproduceSong(sng)
