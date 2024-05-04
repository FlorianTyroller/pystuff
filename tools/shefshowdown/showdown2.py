import pyscreenshot as ImageGrab
import pyautogui
import numpy as np
import os


def take_game_screenshot():
    """Captures a screenshot of the specified game region."""
    im = ImageGrab.grab(bbox=(730, 230, 1520, 950))
    return im

def search_for_images(screenshot, images_to_find):
    """Searches for provided images within a screenshot."""
    screenshot_arr = np.array(screenshot)  # Convert screenshot to a NumPy array

    for image_path in images_to_find:
        # Use PIL to open the image
        from PIL import Image 
        image_to_find = np.array(Image.open(image_path))

        # The rest of your search logic remains the same...
        result = pyautogui.locateOnScreen(image_to_find, region=(815, 270, 585, 130)) 

        if result:
            print(f"Image '{image_path}' found at coordinates: {result}")
        else:
            print(f"Image '{image_path}' not found.")

# -------- Main Execution --------
if __name__ == "__main__":
    game_screenshot = take_game_screenshot()

    # Load all images from the provided folder
    image_folder = "tools/shefshowdown/assets/sushi/"
    images_to_find = [image_folder + image_file for image_file in os.listdir(image_folder) if image_file.endswith(".png")]

    search_for_images(game_screenshot, images_to_find)
