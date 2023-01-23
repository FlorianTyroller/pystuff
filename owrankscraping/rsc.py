import os
import cv2
import numpy as np
import pyautogui
import time
import matplotlib.pyplot as plt

def main():
    type = "supp"
    """evaluate(None, None, None)
    return"""
    champs1= dict()
    champs2= dict()
    champs3= dict()
    for i in range(50):
        cs1, cs2, cs3 = take_screenshot(type)
        champs1 = add_dicts(champs1, cs1)
        champs2 = add_dicts(champs2, cs2)
        champs3 = add_dicts(champs3, cs3)
        next_page()
        time.sleep(1)
    
    print("champs1 = ", str(champs1).replace(".png", ""))
    print("champs2 = ", str(champs2).replace(".png", ""))
    print("champs3 = ", str(champs3).replace(".png", ""))

    # evaluate(champs1, champs2, champs3)


def next_page():
    # click the next page button
    # run the code below
    pyautogui.click(x=1020, y=880)

def take_screenshot(type):
    # take a screenshot of the game
    # extrace three smaller images from the screen shot
    # coordinates for the first smaller one: (x, y, w, h) = (1276, 292, 60, 600)
    # coordinates for the second smaller one: (x, y, w, h) = (1325, 292, 60, 600)
    # coordinates for the third smaller one: (x, y, w, h) = (1376, 292, 60, 600)
    # save the three smaller images to a folder
    # run the code below

    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')

    # Extract the first image
    left, top, width, height = (1296, 292, 60, 600)
    right, bottom = left + width, top + height
    image1 = screenshot.crop((left, top, right, bottom))
    image1.save('image1.png')

    # Extract the second image
    left, top, width, height = (1345, 292, 60, 600)
    right, bottom = left + width, top + height
    image2 = screenshot.crop((left, top, right, bottom))
    image2.save('image2.png')

    # Extract the third image
    left, top, width, height = (1396, 292, 60, 600)
    right, bottom = left + width, top + height
    image3 = screenshot.crop((left, top, right, bottom))
    image3.save('image3.png')

    big_image_path = "image1.png"
    small_image_path = f"imgs/{type}/"
    cs1 = get_counts(big_image_path, small_image_path)

    big_image_path = "image2.png"
    small_image_path = f"imgs/{type}/"
    cs2 = get_counts(big_image_path, small_image_path)

    big_image_path = "image3.png"
    small_image_path = f"imgs/{type}/"
    cs3 = get_counts(big_image_path, small_image_path)

    return cs1, cs2, cs3

def get_counts(big_image_path, small_image_path):
    # Load the larger image
    big_image = cv2.imread(big_image_path)

    path = small_image_path

    # counts 
    counts = dict()

    # Get a list of all the small images in the directory
    small_image_filenames = os.listdir(path)

    # Loop over the small images
    for small_image_filename in small_image_filenames:
        # Create a copy of the big image to draw on
        result_image = big_image.copy()
        # Load the small image
        small_image = cv2.imread(f"{path}{small_image_filename}")

        # Use cv2.matchTemplate() to search for the small image in the big image
        result = cv2.matchTemplate(big_image, small_image, cv2.TM_CCOEFF_NORMED)

        # Use cv2.minMaxLoc() to find the locations with the highest correlation coefficient
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Use a threshold to only consider matches above a certain level of confidence
        threshold = 0.8
        loc = np.where(result >= threshold)

        
        # Loop over the matches
        for pt in zip(*loc[::-1]):
            # Draw a rectangle around the match
            cv2.rectangle(result_image, pt, (pt[0] + small_image.shape[0], pt[1] + small_image.shape[1]), (0,0,255), 2)

        # Save the image with the rectangles drawn on it
        cv2.imwrite(f"imgs/temps/{small_image_filename}_highlighted.jpg", result_image)
        
        th = 40
        newloc = []
        for i in range(len(loc[0])):
            dupe = False
            for cords in newloc:
                if abs(cords[0] - loc[0][i]) <= th and abs(cords[1] - loc[1][i]) <= th:
                    dupe = True
                    break
            if dupe:
                pass
            else:
                newloc.append((loc[0][i], loc[1][i]))
        count = len(newloc)
        
        #print(f"{small_image_filename}: {count}")
        counts[small_image_filename] = count
    
    return counts

def add_dicts(dict1, dict2):
    result = {}
    # Add the keys and values from the first dictionary
    for key, value in dict1.items():
        result[key] = value
    # Add the keys and values from the second dictionary
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


if __name__ == "__main__":
    main()