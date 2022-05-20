import datetime
import os
import subprocess
from global_variables import r, m
from answer import Answer
from speaking import speak
#Convert to exe and put it here C:\Users\Sebastián\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
def WakeVanessa(r,m):
    r.energy_threshold = 3000
    r.dynamic_energy_threshold = False
    name = 'Sebastián'
    with m as source:
        r.adjust_for_ambient_noise(source)
        while True:
            r, source, record = Answer(r, source)
            if 'vanessa' == record:
                hora = datetime.datetime.now().hour
                s = ''
                if hora < 12:
                    s = 'Buenos días ' + name
                elif hora >= 12 and hora <= 18:
                    s = 'Buenas tardes ' + name
                else:
                    s = 'Buenas noches ' + name

                speak(s)
                os.system('cls')
                cmd = f'python .\\voice.py'
                p = subprocess.Popen(cmd, shell=True)
                out, err = p.communicate()
if __name__ == '__main__':
    WakeVanessa(r, m)


