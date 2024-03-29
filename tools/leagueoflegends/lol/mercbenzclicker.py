import pyautogui
import time
from PIL import Image

# Function to check if a pixel is white
def is_white(pixel):
    return pixel[0] >= 200 and pixel[1] >= 200 and pixel[2] >= 200

# Main loop
while True:
    # Take a screenshot
    screenshot = pyautogui.screenshot()

    # Define 9 coordinates to check (you can modify these coordinates)
    coordinates_to_check = [(775, 392), (935, 392), (1090, 392),
                            (775, 534), (935, 534), (1090, 534),
                            (775, 680), (935, 680), (1090, 680)]

    # Loop through the coordinates and check if they are white
    for coord in coordinates_to_check:
        pixel_color = screenshot.getpixel((coord[0], coord[1]))
        if is_white(pixel_color):
            # If the pixel is white, click the coordinate
            pyautogui.click(coord)
            #break
            #print(f"Clicked coordinate {coord}")

    # Wait for a moment before repeating the loop (you can adjust the duration)


# highscore 5006