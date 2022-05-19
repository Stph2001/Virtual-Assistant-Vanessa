import speech_recognition as sr
import datetime
import pyttsx3
import subprocess

def Answer(r, source):
    print('Listening wpp...')
    audio = r.listen(source)
    try:
        record = r.recognize_google(audio, language="es-PE")
        record = record.lower()
        print(record)
        return r, source, record
    except Exception:
        return r, source, ' '


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 8 #9 ingles, #0 español
    engine.say(text)
    engine.runAndWait()


def Speech_Recognition():
    sr.Microphone(device_index=1)
    r = sr.Recognizer()
    r.energy_threshold = 3000
    r.dynamic_energy_threshold = False
    m = sr.Microphone()
    name = 'Sebastián'
    with m as source:
        r.adjust_for_ambient_noise(source)
        while True:
            r, source, record = Answer(r, source)
            if 'vanessa' in record:
                hora = datetime.datetime.now().hour
                s = ''
                if hora < 12:
                    s = 'Buenos días ' + name
                elif hora >= 12 and hora <= 18:
                    s = 'Buenas tardes ' + name
                else:
                    s = 'Buenas noches ' + name

                speak(s)
                cmd = f'python .\\voice.py'
                p = subprocess.Popen(cmd, shell=True)
                out, err = p.communicate()
                # pygame.mixer.music.play()


if __name__ == '__main__':
    Speech_Recognition()


