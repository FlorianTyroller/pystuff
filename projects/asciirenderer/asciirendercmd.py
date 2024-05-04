import curses
from PIL import ImageGrab, ImageEnhance, Image, ImageFilter
from screeninfo import get_monitors  # Install: pip install screeninfo
import time
import pygetwindow as gw
import numpy as np
import matplotlib.pyplot as plt
import os
import io



chars = "#@W$9876543210?!abc;:+=-,._ "
chars2 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
chars3 = "#@%+=-:."
 # Characters representing brightness levels
ASCII_CHARS = np.array(list(chars)[::-1])

def take_screenshot():
    return ImageGrab.grab()

def adjust_colors(sc):
    result = sc.convert('L')
    return result

def resize_sc_1d(sc, width, height):
    return np.array(sc.resize((width, height), Image.ANTIALIAS)).ravel()

def map_brightness_1d(arr):
    brightness_levels = np.linspace(0, 255, len(ASCII_CHARS))
    ascii_indices = (arr / 255 * len(ASCII_CHARS)).astype(int) - 1
    ascii_image = np.take(ASCII_CHARS, ascii_indices)

    return ascii_image

def combine_rows_1d(ai):
    res = ai.tobytes().decode().replace('\x00', '')

    return res

def screenshot_to_ascii(width, height):
    
    screenshot = take_screenshot()

    grayscale_image = adjust_colors(screenshot)

    # Resize
    grayscale_array_1d = resize_sc_1d(grayscale_image, width, height)

    # Map brightness to ASCII characters
    ascii_image_1d = map_brightness_1d(grayscale_array_1d)

    # Combine rows into a single string
    ascii_image_1dd = combine_rows_1d(ascii_image_1d)

    return ascii_image_1dd

if __name__ == "__main__":

    # Calculate the width and height of the ASCII art grid
    asc_w = 475
    asc_h = 131
    
        
    
    try:
        # Initialize curses
        stdscr = curses.initscr()
        
        #curses.curs_set(0)  # Hide the cursor


        # Add content to the window
        while True:
            #stdscr.clear()  # Clear the screen
            stdscr.addstr(0, 0,screenshot_to_ascii(asc_w,asc_h))

            # Refresh the window
            stdscr.refresh()

            
    except Exception as ex:
        print(ex)
    finally:
        # Clean up curses
        curses.endwin()
