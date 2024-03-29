import pygame
import pydirectinput
from screeninfo import get_monitors


pydirectinput.FAILSAFE = False

def get_screen_center():
    monitors = get_monitors()
    
    if monitors:
        # Assuming the first monitor is the primary monitor
        primary_monitor = monitors[0]
        
        center_x = primary_monitor.width // 2
        center_y = primary_monitor.height // 2
        
        return center_x, center_y
    else:
        print("No monitors found.")
        return None

# Get the center coordinates of the screen
center_coordinates = get_screen_center()


pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True
c = 0
# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize the appended joystick (-1 means last array item)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print ("Detected joystick "),joysticks[-1].get_name(),"'"

axis_values = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
threshold = 0.2  # Adjust this threshold value based on your needs
button_map = {0: "w", 1: "e", 2: "q", 3: "r", 4: "d", 5: "f", 6: "p", 7: "b", 8: "4", 9: "y"}
button_map_state = {0: False, 1: False, 2: False, 3: False}
map_move_state = {'up': False, 'down': False, 'left': False, 'right': False}
cursor_move_state = {"x" : 0, "y": 0}
player_move_state = {"attack": -2, "move": -2}
dpad_states = {'up': False, 'down': False, 'left': False, 'right': False} # down == strg
max_cursor_radius = center_coordinates[1]//1.35
centered = True
while keepPlaying:
    clock.tick(10)
    for event in pygame.event.get():
        # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
        # print(event)
        if event.type == 1540:
            if event.button <= 3:
                pydirectinput.keyUp(button_map[event.button],_pause=False)
                #print("key Up")
        elif event.type == 1539:
            # print(button_map[event.button])
            if event.button <= 3:
                if dpad_states["down"] == True:
                    pydirectinput.keyDown('ctrl',_pause=False)
                    pydirectinput.press(button_map[event.button],_pause=False)
                    pydirectinput.keyUp('ctrl',_pause=False)
                    #print("key pressed")
                else:
                    pydirectinput.keyDown(button_map[event.button],_pause=True)
                    #print("key down")
            else:
                pydirectinput.press(button_map[event.button],_pause=False)

                 
        elif event.type == 1536:  # Adjust this value based on your joystick events
            if event.axis == 2:
                if event.value < -threshold:
                    map_move_state['left'] = True
                    map_move_state['right'] = False
                elif event.value > threshold:
                    map_move_state['right'] = True
                    map_move_state['left'] = False
                else:
                    map_move_state['left'] = False
                    map_move_state['right'] = False
            elif event.axis == 3:
                if event.value < -threshold:
                    map_move_state['up'] = True
                    map_move_state['down'] = False
                elif event.value > threshold:
                    map_move_state['down'] = True
                    map_move_state['up'] = False
                else:
                    map_move_state['up'] = False
                    map_move_state['down'] = False
            elif event.axis == 0:
                # pydirectinput.moveTo(center_coordinates[0],center_coordinates[1],_pause=False)
                if abs(event.value) > threshold:
                    cursor_move_state['x'] = event.value
                else: 
                    cursor_move_state['x'] = 0
            elif event.axis == 1:
                if abs(event.value) > threshold:
                    cursor_move_state['y'] = event.value
                else: 
                    cursor_move_state['y'] = 0
            elif event.axis == 4:
                player_move_state["attack"] = event.value
            elif event.axis == 5:
                player_move_state["move"] = event.value
        elif event.type == 1538: # key up = (0,0), left = (-1,0), right = (1,0), up = (0,1), down = (0,-1)
            if event.value == (0,0):
                for k in dpad_states.keys():
                    dpad_states[k] = False
            elif event.value == (-1,0):
                pydirectinput.press("1",_pause=False)
            elif event.value == (0,1):
                pydirectinput.press("2",_pause=False)
            elif event.value == (1,0):
                pydirectinput.press("3",_pause=False)
            elif event.value == (0,-1):
                dpad_states["down"] = True

    if player_move_state["attack"] > -1 + threshold:
        pydirectinput.keyDown("a",_pause=False)
        pydirectinput.keyUp("a",_pause=False)
    elif player_move_state["move"] > -1 + threshold:
        pydirectinput.mouseDown(button='right',_pause=False)
        pydirectinput.mouseUp(button='right',_pause=False)
    
    if cursor_move_state['x'] == 0 and cursor_move_state['y'] == 0:
        if not centered:
            centered = True
            pydirectinput.moveTo(center_coordinates[0],center_coordinates[1],_pause=False)
    else:
        centered = False
        pydirectinput.moveTo(center_coordinates[0] + int(max_cursor_radius*cursor_move_state['x']),center_coordinates[1]+ int(max_cursor_radius*cursor_move_state['y']),_pause=False)

    for key, state in map_move_state.items():
        if state:
            pydirectinput.keyDown(key,_pause=False)
        else:
            pydirectinput.keyUp(key,_pause=False)
                

# skill
# items313213213332123