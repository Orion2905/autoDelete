import pyautogui
import time
from art import *
import datetime
import keyboard
import sys

def end():
    print(f"[{dataTime()}] > Programma terminato")
    tprint("End")
    pyautogui.alert(title="End", text="Programma terminato")

def dataTime():
    x = datetime.datetime.now()
    return x

def sleep(x):
    time.sleep(x)

def quit():
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        end()
        sys.exit() # finishing the loop

def ebay_move():
    sleep(1)
    # pyautogui.keyDown('down')
    # pyautogui.keyUp('down')
    # pyautogui.keyDown('down')
    # pyautogui.keyUp('down')
    quit()
    try:
        azione_1 = pyautogui.locateCenterOnScreen('img/azione11.PNG') # coordinate prima azione
        x, y = int(azione_1[0]), int(azione_1[1])
        print(f"[{dataTime()}] > [X;Y]:[{x};{y}]")
        azione_1 = x,y
        print(f"[{dataTime()}] > Coordinate prima azione : {azione_1}")
        pyautogui.moveTo(azione_1, duration=1)
        pyautogui.click()
        quit()
        sleep(1)
        quit()

        azione_2 = pyautogui.locateCenterOnScreen('img/azione2222.PNG') # coordinate seconda azione
        print(f"[{dataTime()}] > Coordinate seconda azione : {azione_2}")
        pyautogui.moveTo(azione_2, duration=1)
        pyautogui.click()
        quit()
        elimina = pyautogui.locateCenterOnScreen('img/elimina3.PNG') # coordinate elimina
        if elimina:
            print(f"[{dataTime()}] > Coordinate terza azione : {elimina}")
            pyautogui.moveTo(elimina, duration=1)
            pyautogui.click()
            elimina2 = pyautogui.locateCenterOnScreen('img/elimina222.PNG') # coordinate elimina 2
            print(f"[{dataTime()}] > coordinate elimina2 : {elimina2}")
            if elimina2 == None: # Definizione valore di default
                elimina2 = 1281, 368
            quit()
            pyautogui.moveTo(elimina2, duration=1)
            pyautogui.click()
        else:
            print(f"[{dataTime()}] > Non trovato {elimina}")
            elimina = 838, 496
            pyautogui.moveTo(elimina, duration=1)
            pyautogui.click()
            elimina2 = pyautogui.locateCenterOnScreen('img/eliminayes.PNG')
            if elimina2 == None:
                elimina2 = 1281, 368
            pyautogui.moveTo(elimina2, duration=1)
            pyautogui.click()
            quit()
        sleep(1)
        quit()
    except Exception as e:
        print(f"Errore: {e}\n ...Continuo...")

# Inizio del programma

tprint("Start...")
print(f"[{dataTime()}] > Programma inizializzato, per terminare il programma premi q. Grandezza schermo : {pyautogui.size()}")
quit()
print(f"[{dataTime()}] > Cercando icona chrome...")
quit()

#
# while True:
#     print(pyautogui.position())
#
#

# Ricerca dell'icona di chrome

chrome = pyautogui.locateCenterOnScreen('img/chrome2.JPG')
quit()
if chrome:
    print(f"[{dataTime()}] > Coordinate chrome:", chrome)
    pyautogui.moveTo(chrome, duration=1)
else:
    chrome = (714, 1059)
    print(f"[{dataTime()}] > Icona chrome non trovata. Posizione predefinita:", chrome)
    pyautogui.moveTo(chrome, duration=1)
quit()
pyautogui.click()
quit()
#

sleep(1) # Funzione per dare l'intervallo di tempo
quit()
# Ciclo che esegue le stesse azioni per ogni scheda chrome per j volte

j = 600 # range di esecuzione
for x in range(j):
    tprint(str(x))
    reset = 113, 14 # coordinate di default
    print(f"[{dataTime()}] > Coordinate quarta azione:", reset)
    pyautogui.moveTo(reset, duration=1)
    pyautogui.click()
    quit()
    # ciclo che esegue le stesse azioni per ogni scheda di ebay individuata

    for i in pyautogui.locateAllOnScreen('img/ebay34.png'):
        cords = i[0], i[1]
        print(f"[{dataTime()}] > Coordinate icone Ebay trovate:", i, cords)
        pyautogui.moveTo(cords, duration=1)
        pyautogui.click()
        ebay_move() # chiamata alla funzione con le istruzioni per ebay
        quit()
    #
    quit()
    reset = 113, 14
    print(f"[{dataTime()}] > Coordinate quarta azione:", reset)
    pyautogui.moveTo(reset, duration=1)
    pyautogui.click()
    quit()
#

# Fine programma
quit()
end()

#