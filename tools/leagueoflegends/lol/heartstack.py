import pydirectinput
import time
import keyboard

# define the positions to click on
positions = [(601, 700), (628, 564), (607, 430), (580, 330)]

# loop until user presses 'q' to quit
while True:
    # move mouse to each position and press 'a'
    for pos in positions:
        pydirectinput.moveTo(pos[0], pos[1], duration=0.25)
        pydirectinput.press('a')
        time.sleep(0.5)
        
        # check if user pressed 'q' to quit
        if keyboard.is_pressed('q'):
            break
    
    # check if user pressed 'q' to quit
    if keyboard.is_pressed('q'):
        break

    # press ctrl+shift+o
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('shift')
    pydirectinput.press('o')
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('ctrl')
    time.sleep(2.3)
