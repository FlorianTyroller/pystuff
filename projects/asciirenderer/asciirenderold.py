from PIL import ImageGrab, ImageEnhance, Image, ImageFilter
import tkinter as tk
from screeninfo import get_monitors  # Install: pip install screeninfo
import time
import pygetwindow as gw
import numpy as np
import matplotlib.pyplot as plt
import win32gui
import win32con
import win32api
from collections import defaultdict
import io

ASCII_CHARS2 = np.array(list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."))  # Characters representing brightness levels
ASCII_CHARS = np.array(list("@%#*+=-:."))

execution_times = dict()

def time_function(func, args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    # Check if the function is already in the dictionary
    if func.__name__ in execution_times:
        # If it is, update the accumulated time
        execution_times[func.__name__]['total_time'] += elapsed_time
        execution_times[func.__name__]['num_calls'] += 1
    else:
        # If it's not, initialize the entry in the dictionary
        execution_times[func.__name__] = {'total_time': elapsed_time, 'num_calls': 1}
    
    return result

def take_screenshot():
    return ImageGrab.grab()

def adjust_colors(sc):
    result = sc.convert('L')
    return result

def resize_sc(sc, width, height):
    return np.array(sc.resize((width, height), Image.ANTIALIAS))


def resize_sc_1d(sc, width, height):
    return np.array(sc.resize((width, height), Image.ANTIALIAS)).ravel()

def map_brightness_1d(arr):
    brightness_levels = np.linspace(0, 255, len(ASCII_CHARS))
    ascii_indices = (arr / 255 * len(ASCII_CHARS)).astype(int) - 1
    ascii_image = np.take(ASCII_CHARS, ascii_indices)

    return ascii_image

def map_brightness(arr):
    brightness_levels = np.linspace(0, 255, len(ASCII_CHARS))
    ascii_indices = (arr / 255 * len(ASCII_CHARS)).astype(int) - 1
    ascii_image = np.take(ASCII_CHARS, ascii_indices)

    return ascii_image

def combine_rows(ai):
    return '\n'.join(''.join(row) for row in ai)

def combine_rows_1d(ai):
    res = ai.tobytes().decode().replace('\x00', '')

    return res

    


def combine_rows_new(ai):
    flattened = np.array([char for row in ai for char in row])  # Flatten into a 1D NumPy array
    return flattened.reshape(-1, len(ai[0])).tobytes().decode('utf-8')


def screenshot_to_ascii(width, height):

    screenshot = time_function(take_screenshot,())

    grayscale_image = time_function(adjust_colors,(screenshot,))

    # Resize
    grayscale_array_1d = time_function(resize_sc_1d,(grayscale_image, width, height))
    #grayscale_array = time_function(resize_sc,(grayscale_image, width, height))
    # Resize
    

    # Map brightness to ASCII characters
    ascii_image_1d = time_function(map_brightness_1d,(grayscale_array_1d,))
    #ascii_image = time_function(map_brightness,(grayscale_array,))

    # Combine rows into a single string
    ascii_image_1dd = time_function(combine_rows_1d,(ascii_image_1d,))
    #ascii_image = time_function(combine_rows,(ascii_image,))

    return ascii_image_1dd


def update_ascii_old2():
    global ascii_image, canvas, scale
    
    ascii_image = screenshot_to_ascii(asc_w, asc_h)
    
    canvas.delete("ascii_text")  # Clear previous ASCII art
    
    for i, row in enumerate(ascii_image):
        canvas.create_text(screen_w / 2, i * scale, text=row, font=("Consolas", scale-1), fill="white", tags="ascii_text")
            

    root.after(100, update_ascii) 

def update_ascii():
    global label, scale
    # Capture ASCII art
    ascii_image = screenshot_to_ascii(asc_w, asc_h)
    # print(ascii_image)
    # Clear previous ASCII art by updating the label's text attribute
    
    # Display new ASCII art
    #print(len(ascii_image))
    #c = ascii_image
    label.config(text=ascii_image)
    # Print timing information
    """for func_name, data in execution_times.items():
        avg_time = data['total_time'] / data['num_calls']
        print(f"Function {func_name}: Total time={data['total_time']}, Num calls={data['num_calls']}, Avg time={avg_time}")"""

    # Schedule next update
    root.after(1, update_ascii)  # Update every 10 milliseconds

def estimate_wrap_length(font, max_characters):
    average_character_width = font.measure('0')  # Measure the width of a typical character
    wrap_length_pixels = average_character_width * max_characters
    return wrap_length_pixels


def close_window(event):
    root.destroy()

if __name__ == "__main__":
    screen_w, screen_h = 1920, 1080
    scale = 10
    

    # Calculate the width and height of the ASCII art grid
    asc_w = screen_w // scale
    asc_h = screen_h // scale
    asc_w += int(asc_h * 0.4)

    

    root = tk.Tk() 
    canvas = tk.Canvas(root, width=screen_w, height=screen_h, bg="black")
    canvas.pack()

    font = tk.font.Font(family="Courier New", size=scale)

    # Estimate wrap length based on character count (e.g., wrap after 20 characters)
    max_characters = asc_w
    wrap_length = estimate_wrap_length(font, max_characters)


    # Create the label with the canvas as parent
    label = tk.Label(canvas, text="", font=("Courier New", scale), fg="white", wraplength=wrap_length, justify="center", bg="black")
    label.place(relx=0.5, rely=0.5, anchor="center")

    update_ascii()  # Start the function to continuously update the ASCII art

    root.bind("<Escape>", close_window)
    root.mainloop()


