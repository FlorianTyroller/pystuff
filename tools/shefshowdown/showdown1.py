import os
import pyautogui
import time
from PIL import Image
import numpy as np

# Define the region to capture
top_left_x, top_left_y = 730, 230
bottom_right_x, bottom_right_y = 1520, 950

# Define the region to search for the images
search_region = (881 - top_left_x, 316 - top_left_y, 1356 - top_left_x, 359 - top_left_y)

# Load all images from the provided folder
image_folder = "tools/shefshowdown/assets/sushi/"
images_to_find = [Image.open(os.path.join(image_folder, image_file)) for image_file in os.listdir(image_folder) if image_file.endswith(".png")]


# Iterate over each image and search for it in the defined region
while True:
    #time.sleep(1)
    # Take a screenshot of the game
    screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, bottom_right_x - top_left_x, bottom_right_y - top_left_y))
    screenshot.save("tools/shefshowdown/assets/screenshot.png")
    # Crop the screenshot to the search region
    cropped_screenshot = screenshot.crop(search_region)
    # Save the cropped screenshot
    cropped_screenshot.save("cropped_screenshot.png")

    for image_to_find in images_to_find:
        
        found_location = pyautogui.locate(image_to_find, screenshot, region=search_region)
        if found_location:
            print(f"Image {image_to_find.filename} found at:", found_location)
        else:
            print(f"Image {image_to_find.filename} not found.")
    break