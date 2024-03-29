import pydirectinput
import time
import keyboard

# define the positions to click on
positions = [(601, 700), (628, 564), (607, 430), (580, 330)]

# loop until user presses 'q' to quit
while True:
    # move mouse to each position and press 'a'
    for i in range(24):
        pydirectinput.press('f')
        time.sleep(0.5)
        
    # check if user pressed 'q' to quit
    if keyboard.is_pressed('q'):
        break
    


    # press ctrl+shift+o

    pydirectinput.keyDown('shift')
    pydirectinput.press('\'')
    pydirectinput.keyUp('shift')

    time.sleep(3)