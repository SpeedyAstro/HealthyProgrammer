# Healthy Programmer 
# 9AM TO  5PM
# water  - water.mp3  -[3.5l] 200ml - drank - log file [3.5l - 3500] [540 min 32400sec] [30min every 1800sec]
# Eyes - eyes.mp3 - [30 min] - Eydone -log file
# physical activity - physical.mp3 [45 MIN] - Exdone - log
# pygame module
#  9 - 10 - 11 - 12 - 1 - 2 - 3 - 4 - 5  [9h]
from pygame import mixer
from time import time
from datetime import datetime
#def getdate() :
 #   import datetime
  #  return datetime.datetime.now
def set_alarm(file,stopper) :
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True :
        query = input()
        if query == stopper :
            mixer.music.stop()
            break

def set_log(msg) :
    with open("mylog.txt" , 'a') as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == "__main__" :
    initwater = time()
    initeyes = time()
    initexcer = time()
    watersecs = 10
    eyesecs = 10*60
    exsecs = 45*60
    while True:
        if time() - initwater > watersecs :
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            set_alarm("soundeffect.mp3", "drank")
            initwater = time()
            set_log("Drank water at ")
        if time() - initeyes > eyesecs :
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            set_alarm("soundeffect.mp3", "Eyedone")
            initeyes = time()
            set_log("Eyes relaxed at ")
        if time() - initexcer > exsecs :
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            set_alarm("soundeffect.mp3" , "Exdone")
            initexcer = time()
            set_log("excersice done at ")
