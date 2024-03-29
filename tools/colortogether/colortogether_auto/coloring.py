
import pyautogui
import time
import PIL.ImageGrab





# Function to check if two RGB values are approximately equal
def is_color_match(colorin, tolerance=1):
    col1 = (200, 200, 200) # "c8c8c8"
    col2 = (142, 142, 142) # "8e8e8e"
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(colorin, col1)) or all(abs(c1 - c2) <= tolerance for c1, c2 in zip(colorin, col2))


# Specify the minimum area of matching pixels required
min_area_threshold = 100  # Example: at least 100 matching pixels

# Calculate the coordinates of the center 800x800 square
screen_width, screen_height = pyautogui.size()
square_size = 900
start_x = (screen_width // 2) - square_size // 2
start_y = (screen_height // 2) - square_size // 2
end_x = start_x + square_size
end_y = start_y + square_size

while True:
    # Take a screenshot of the center 800x800 square
    screenshot = PIL.ImageGrab.grab(bbox=(start_x, start_y, end_x, end_y))

    # Initialize variables to track the matching region
    matching_region = []
    matched_pixels = 0

    clicked = False
    # Loop through each pixel in the screenshot
    offset = 5
    for oc in range(offset):
        if clicked:
            break
        for x in range(1 + oc, screenshot.width - 1, offset):
            if clicked:
                break
            for y in range(1 + oc, screenshot.height - 1, offset):
                if clicked:
                    break
                # Get the RGB value of the pixel
                pixel_color = screenshot.getpixel((x, y))[:3]
                
                # Check if the pixel matches the target color
                if is_color_match(pixel_color):
                    # Check if the neighboring pixels also match the target color
                    neighbors = [
                        screenshot.getpixel((x, y-1))[:3],  # pixel above
                        screenshot.getpixel((x, y+1))[:3],  # pixel below
                        screenshot.getpixel((x-1, y))[:3],  # pixel to the left
                        screenshot.getpixel((x+1, y))[:3]   # pixel to the right
                    ]
                    
                    if all(is_color_match(neighbor) for neighbor in neighbors):
                        # Calculate the absolute position of the pixel on the screen
                        absolute_x = start_x + x
                        absolute_y = start_y + y
                        
                        # Click on the pixel
                        pyautogui.click(absolute_x, absolute_y)
                        clicked = True
                        # time.sleep(0.5)  # Pause for a moment after clicking (adjust as needed)