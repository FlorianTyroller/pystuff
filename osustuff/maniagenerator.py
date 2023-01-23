
import sys
import os
import time
import keyboard
import math
from collections import defaultdict


def clean_keys(d):
    total_l = []

    for k in d.keys():
        if k in ['s', 'd', 'k', 'l']:
            down = False
            d_i = None 
            for i,v in enumerate(d[k]):
                if v[0] == 'down':
                    if not down:
                        down = True
                        d_i = i 
                    else:
                        # d[k].remove(v)
                        pass
                elif v[0] == 'up':
                    if down:
                        down = False
                        l = list(d[k][d_i])
                        l.append(v[1])
                        total_l.append(l)
                        d_i = None
                    # d[k].remove(v)


    # sort the list by the second value of the tuple
    total_l.sort(key=lambda x: x[1])
    # remove the first value of the tuples
    total_l = [l[1:] for l in total_l]
    return total_l

def write_to_file(l, file_name):
    columnCount = 4
    hold_threshold = 0.4
    y = 192
    key_to_x = dict()
    key_to_x['s'] = 64
    key_to_x['d'] = 192
    key_to_x['k'] = 320
    key_to_x['l'] = 448
    with open(r"0 testing - tyt/testing.osu" , 'w') as f:
        # write the header
        with open('osuheader.txt', 'r') as header:
            f.write(header.read())
        # write the hitobjects
        for i in l:
            x = key_to_x[i[1]]

            # determin if hold or not
            if i[2] - i[0] > hold_threshold:
                hit_type = 7
                s_t = math.floor(i[0] * 1000)
                e_t = math.floor(i[2] * 1000)
                # write line to file
                # x,y,time,type,hitSound,endTime:hitSample
                # 448,192,9092,128,0,9376:0:0:0:0:
                f.write('{},{},{},{},{},{}:0:0:0:0:\n'.format(x, y, t, hit_type, 0, e_t, 0))
            else:
                hit_type = 1
                # x,y,time,type,hitSound,objectParams,hitSample
                # convert time to milliseconds
                t = math.floor(i[0] * 1000)
                # write line to file
                f.write('{},{},{},{},{},{}:0:0:0:\n'.format(x, y, t, hit_type, 0, 1))
                
            


recording = False
start_time = None
end_time = None
key_strokes = defaultdict(list)
while True:
    # detect space key press
    if keyboard.is_pressed('space') and not recording:
        print("Recording")
        recording = True

        start_time = time.time()
        key_strokes = defaultdict(list)

    if keyboard.is_pressed('esc') and recording:

        recording = False
        end_time = time.time()

        print("stopped recording at", end_time - start_time, "seconds") 
        l = clean_keys(key_strokes)
        write_to_file(l, 'testing.osu')


    if recording:
        ev = keyboard.read_event()
        ev_time = time.time() - start_time
        key_strokes[ev.name].append((ev.event_type,ev_time,ev.name))




