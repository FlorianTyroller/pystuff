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
import threading
from queue import Queue 
import random

chars = "#@W$9876543210?!abc;:+=-,._"
chars2 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
chars3 = "#@%+=-:."
 # Characters representing brightness levels
ASCII_CHARS = np.array(list(chars)[::-1])

execution_times = dict()

MAX_QUEUE_SIZE = 5  # Example - adjust as needed
MIN_QUEUE_SIZE = 1  # Example
MAX_WORKERS_PER_TYPE = 4  # Example


screenshot_queue = Queue()
color_adjust_queue = Queue()
resize_queue = Queue()
brightness_map_queue = Queue()
final_assembly_queue = Queue() #combine rows
render_queue = Queue() 


def manage_workers(all_queues):
    active_workers = {}  

    # Initial worker startup
    for queue, worker_type, num_workers in all_queues:
        for _ in range(min(num_workers, 1)):  # Start at least one worker per type
            thread = threading.Thread(target=worker_type, daemon=True)  
            thread.start()
            active_workers.setdefault(worker_type, []).append(thread)
            print("active_workers")

    while True:
        stats = {}
        for queue, worker_type, num_workers in all_queues:  # Include num_workers
            num_active = len(active_workers.get(worker_type, []))
            stats[worker_type] = {'queue_size': queue.qsize(), 'num_workers': num_active}

            if queue.qsize() > MAX_QUEUE_SIZE and num_active < num_workers:
                # Start additional workers up to 'num_workers' limit
                for _ in range(min(num_workers - num_active, MAX_WORKERS_PER_TYPE - num_active)):  
                    thread = threading.Thread(target=worker_type, daemon=True)  # Replace *queue_args
                    thread.start()
                    active_workers.setdefault(worker_type, []).append(thread)

            elif queue.qsize() < MIN_QUEUE_SIZE and num_active > 1:
                # Pause or terminate excess workers
                for _ in range(num_active - 1):
                    worker_thread = active_workers[worker_type].pop()
                    # ... Logic to pause or terminate 'worker_thread'
        print("Pipeline Statistics:", stats)
        print("render queue size:", render_queue.qsize())
        time.sleep(1) 

def sleep_rand():
    time.sleep(random.randint(9, 35)/100)
    

def update_ascii_o():
    if not render_queue.empty():

        ascii_image = render_queue.get()
        label.config(text=ascii_image)

    root.after(1, lambda: update_ascii())   # Schedule next update

def update_ascii():
    if not render_queue.empty():
        ascii_image = render_queue.get()
        label.config(text=ascii_image)
    
    # Schedule next update
    root.after(1, update_ascii) 

def update_ascii_thread(worker_id):
    # Continuously update the GUI with ASCII art
    while True:
        update_ascii()

def screenshot_worker():
    while True:
        screenshot = take_screenshot()
        screenshot_queue.put(screenshot)

def color_adjust_worker():
    while True:
        screenshot = screenshot_queue.get()
        adjusted_image = adjust_colors(screenshot)
        color_adjust_queue.put(adjusted_image)

def resize_worker():
    while True:
        image = color_adjust_queue.get()
        resized_array = resize_sc_1d(image, asc_w, asc_h)  # Assuming width, height are globally accessible
        resize_queue.put(resized_array)

def map_brightness_worker():
    while True:
        array = resize_queue.get()
        ascii_image = map_brightness_1d(array)
        brightness_map_queue.put(ascii_image)

def combine_rows_worker():
    while True:
        ascii_image = brightness_map_queue.get()
        ascii_image_str = combine_rows_1d(ascii_image)
        render_queue.put(ascii_image_str)





def screenshot_worker_t(queue):
    while True:
        start_time = time.time()
        ascii_image = screenshot_to_ascii(asc_w, asc_h)
        queue.put((ascii_image, time.time() - start_time))  # Pass both image and render time
        time.sleep(0.1)  

def update_ascii_t(queue):
    if not queue.empty():
        ascii_image, render_time = queue.get()
        label.config(text=ascii_image)
        print(f"Total frame render time: {render_time:.4f} seconds")  # Print with formatting
    root.after(1, lambda: update_ascii(queue)) 

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

def screenshot_to_ascii_time(width, height):

    screenshot = time_function(take_screenshot,())

    grayscale_image = time_function(adjust_colors,(screenshot,))

    # Resize
    grayscale_array_1d = time_function(resize_sc_1d,(grayscale_image, width, height))


    # Map brightness to ASCII characters
    ascii_image_1d = time_function(map_brightness_1d,(grayscale_array_1d,))


    # Combine rows into a single string
    ascii_image_1dd = time_function(combine_rows_1d,(ascii_image_1d,))


    return ascii_image_1dd

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

def estimate_wrap_length(font, max_characters):
    average_character_width = font.measure('0')  # Measure the width of a typical character
    wrap_length_pixels = average_character_width * max_characters
    return wrap_length_pixels

def close_window(event):
    root.destroy()

if __name__ == "__main__":
    screen_w, screen_h = 1920, 1080
    scale = 5
    

    # Calculate the width and height of the ASCII art grid
    asc_w = screen_w // scale
    asc_h = screen_h // scale
    asc_w += int(asc_h * 0.4)
    asc_h -= int(asc_h * 0.4)

    

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

  # Start the function to continuously update the ASCII art

    root.bind("<Escape>", close_window)

    
    NUM_SCREENSHOT_WORKERS = 5
    NUM_COLOR_ADJUST_WORKERS = 3
    NUM_RESIZE_WORKERS = 3
    NUM_BRIGHTNESS_MAP_WORKERS = 3
    NUM_FINAL_ASSEMBLY_WORKERS = 5
    all_queues = [
        (screenshot_queue, screenshot_worker, NUM_SCREENSHOT_WORKERS),
        (color_adjust_queue, color_adjust_worker, NUM_COLOR_ADJUST_WORKERS),
        (resize_queue, resize_worker, NUM_RESIZE_WORKERS),
        (brightness_map_queue, map_brightness_worker, NUM_BRIGHTNESS_MAP_WORKERS),
        (final_assembly_queue, combine_rows_worker, NUM_FINAL_ASSEMBLY_WORKERS),
        # ... Add others similarly
    ]


    # Start the worker management thread
    manager_thread = threading.Thread(target=manage_workers, args=(all_queues,), daemon=True)
    manager_thread.start()

    # Create multiple threads for updating the GUI
    num_workers = 4  # Choose the number of workers
    ascii_threads = []
    for i in range(num_workers):
        thread = threading.Thread(target=update_ascii_thread, args=(i,))
        thread.daemon = True  # Set the thread as a daemon so it terminates when the main thread exits
        thread.start()
        ascii_threads.append(thread)
    #update_ascii()  
    root.mainloop()


