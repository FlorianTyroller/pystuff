import pyautogui
import cv2
import numpy as np
import pytesseract
import tkinter as tk
import spellnoiv

def take_screenshot():
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')
    return screenshot

def read_screenshot():
    # Read the screenshot image
    img = cv2.imread('screenshot.png')
    return img

def convert_to_grayscale(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def apply_thresholding(gray):
    # Apply thresholding to convert the background pixels to white
    _, background_thresholded = cv2.threshold(gray, 9, 255, cv2.THRESH_BINARY)

    # Invert the thresholded image
    background_thresholded = cv2.bitwise_not(background_thresholded)

    # Apply a lower threshold to the grayscale image to keep the letters intact
    _, letters_thresholded = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

    # Combine the background and letters thresholded images
    thresholded = cv2.bitwise_or(background_thresholded, letters_thresholded)

    '''# Dilate the image to increase the size of the letters
    kernel = np.ones((3, 3), np.uint8)
    thresholded = cv2.dilate(thresholded, kernel, iterations=1)
    '''
    #show the image
    '''cv2.imshow('thresholded', thresholded)
    cv2.waitKey(0)'''

    return thresholded

def crop_center_square(img):
    # Crop it down to a centered square
    # Width: 400, Height: 400
    # Center of the square is the center of the image
    image_center = (img.shape[1] // 2, img.shape[0] // 2)
    cropped = img[image_center[1] - 250:image_center[1] + 250, image_center[0] - 250:image_center[0] + 250]
    '''#show the image
    cv2.imshow('cropped', cropped)
    cv2.waitKey(0)'''
    return cropped

def find_contours(thresholded):
    # Find contours
    contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # show the image
    return contours, thresholded

def filter_contours(contours, thresholded):
    # Filter contours based on distance
    # show contours on canva
    canvas = np.zeros_like(thresholded)
    cv2.drawContours(canvas, contours, -1, (255, 255, 255), 1)
    cv2.imshow('contours', canvas)
    cv2.waitKey(0)

    filtered_contours = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        contour_center = (x + w // 2, y + h // 2)
        is_close = False
        for filtered_contour in filtered_contours:
            filtered_x, filtered_y, filtered_w, filtered_h = cv2.boundingRect(filtered_contour)
            filtered_center = (filtered_x + filtered_w // 2, filtered_y + filtered_h // 2)
            if np.linalg.norm(np.array(contour_center) - np.array(filtered_center)) < 20:
                is_close = True
                break
        if not is_close:
            filtered_contours.append(contour)
    
    canvas = np.zeros_like(thresholded)
    cv2.drawContours(canvas, filtered_contours, -1, (255, 255, 255), 1)
    cv2.imshow('contours', canvas)
    cv2.waitKey(0)


    return filtered_contours

def detect_letters(filtered_contours, thresholded):
    """canvas = np.zeros_like(thresholded)
    cv2.drawContours(canvas, filtered_contours, -1, (255, 255, 255), 1)
    cv2.imshow('contours', canvas)
    cv2.waitKey(0)"""
    # Detect and add letters to the canvas at contour coordinates
    detected = ""
    # Try different configurations for better results
    custom_config = r'-l eng --oem 3 --psm 10 -c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZ"'

    # Create a blank canvas with the same dimensions as the thresholded image
    canvas = np.zeros_like(thresholded)
    lss = []
    for contour in filtered_contours:
        x, y, w, h = cv2.boundingRect(contour)
        ratio = h / w
        area = cv2.contourArea(contour)
        if ratio > 0.2 and 200 < area < 1000:
            letter = thresholded[y:y + h, x:x + w]
            # add black bars to every side of the letter
            letter = cv2.copyMakeBorder(letter, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            segment = cv2.bitwise_not(letter)
            c = pytesseract.image_to_string(segment, config=custom_config)

            # Check if c is a letter
            if len(c) == 0:
                # if not show the image
                """cv2.imshow('letter', segment)
                cv2.waitKey(0)"""
                continue

            # Check c if there are any non-letters, remove them
            """print(c)
            cv2.imshow('letter', segment)
            cv2.waitKey(0)"""
            c2 = ''
            for i in range(len(c)):
                if c[i].isalpha():
                    c2 += c[i]
            c = c2

            # If c is "DL" or "TL", continue
            if c == "DL" or c == "TL":
                continue

            if len(c) > 1:
                c = c[0]
            
            detected += c
            # Add the detected character to the canvas at the contour's bounding box
            cv2.putText(canvas, c, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2, cv2.LINE_AA)

            lss.append(((x, y), c))
        else:
            ''' show the image
            cv2.imshow('rejected', thresholded[y:y + h, x:x + w])
            cv2.waitKey(0)'''
            pass

    return detected, canvas, lss

def letters_to_grid(detected_letters):
    grid_size = 5

    # Calculate the scaling factors based on the available letter coordinates
    max_x = max(x for (x, _), _ in detected_letters)
    max_y = max(y for (_, y), _ in detected_letters)
    min_x = min(x for (x, _), _ in detected_letters)
    min_y = min(y for (_, y), _ in detected_letters)
    x_scaling_factor = (max_x - min_x) / (grid_size - 1)
    y_scaling_factor = (max_y - min_y) / (grid_size - 1)

    # Create a 5x5 array filled with empty strings
    grid = [[''] * grid_size for _ in range(grid_size)]

    # Place the detected letters in the grid based on the scaled coordinates
    for (x, y), letter in detected_letters:
        scaled_x = round(x / x_scaling_factor) - 1
        scaled_y = round(y / y_scaling_factor) - 1
        print(scaled_x, scaled_y, letter)
        grid[scaled_y][scaled_x] = letter

    # Print the resulting grid
    for row in grid:
        print(row)

    return grid





#------------------------ GUI ------------------------#




class GridGUI:
    def __init__(self, grid_size, characters):
        self.grid_size = grid_size
        self.characters = characters
        self.special_positions = {
            'dw': None,
            'tl': None,
            'dl': None
        }
        self.special_coordinates = {
            'dw': None,
            'tl': None,
            'dl': None
        }

        # Create the main window
        self.window = tk.Tk()

        # Create the letter grid on the left
        self.create_letter_grid()

        # Create the special position buttons below the letter grid
        self.create_special_position_buttons()

        # Create the buttons in the middle
        self.create_middle_buttons()

        # Create the result list on the right
        self.create_result_list()

        # create swap list on the far right
        self.create_swap_list()

    def create_swap_list(self):
        # Create a frame to hold the result list
        self.swap_frame = tk.Frame(self.window)
        self.swap_frame.grid(row=0, column=3, padx=10, pady=10, rowspan=self.grid_size+1)

        # Create the result list
        self.swap_list = tk.Listbox(self.swap_frame, width=80)
        self.swap_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.swap_scrollbar = tk.Scrollbar(self.swap_frame)
        self.swap_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.swap_list.config(yscrollcommand=self.swap_scrollbar.set)
        self.swap_scrollbar.config(command=self.swap_list.yview)

    def create_letter_grid(self):
        # Create a frame to hold the letter grid
        self.grid_frame = tk.Frame(self.window)
        self.grid_frame.grid(row=0, column=0, rowspan=self.grid_size, padx=10, pady=10)

        # Create the grid of text fields
        self.entries = [[None] * self.grid_size for _ in range(self.grid_size)]

        for y in range(self.grid_size):
            for x in range(self.grid_size):
                entry = tk.Entry(self.grid_frame, width=5)
                entry.grid(row=y, column=x)
                self.entries[y][x] = entry

            
        # Populate the grid with the characters
        self.populate_grid()

    def create_special_position_buttons(self):
        # Create a frame to hold the special position buttons
        self.special_frame = tk.Frame(self.window)
        self.special_frame.grid(row=self.grid_size, column=0, padx=10, pady=10)

        # Create the special position buttons
        self.dw_button = tk.Button(self.special_frame, text="DW", command=self.handle_special_position_button('dw'))
        self.dw_button.grid(row=0, column=0, padx=5, pady=5)

        self.tl_button = tk.Button(self.special_frame, text="TL", command=self.handle_special_position_button('tl'))
        self.tl_button.grid(row=0, column=1, padx=5, pady=5)

        self.dl_button = tk.Button(self.special_frame, text="DL", command=self.handle_special_position_button('dl'))
        self.dl_button.grid(row=0, column=2, padx=5, pady=5)

        # Create labels for special coordinates
        self.dw_coordinates_label = tk.Label(self.special_frame, text="")
        self.dw_coordinates_label.grid(row=1, column=0, padx=5, pady=5)

        self.tl_coordinates_label = tk.Label(self.special_frame, text="")
        self.tl_coordinates_label.grid(row=1, column=1, padx=5, pady=5)

        self.dl_coordinates_label = tk.Label(self.special_frame, text="")
        self.dl_coordinates_label.grid(row=1, column=2, padx=5, pady=5)

    def create_middle_buttons(self):
        # Create a frame to hold the middle buttons
        self.middle_frame = tk.Frame(self.window)
        self.middle_frame.grid(row=0, column=1, padx=10, pady=10, rowspan=self.grid_size+1)

        # Create the middle buttons
        button1 = tk.Button(self.middle_frame, text="Rescan", command=self.handle_button1)
        button1.grid(row=0, column=0, padx=5, pady=5)

        button2 = tk.Button(self.middle_frame, text="Get TOP 10", command=self.handle_button2)
        button2.grid(row=1, column=0, padx=5, pady=5)

        button3 = tk.Button(self.middle_frame, text="Button 3", command=self.handle_button3)
        button3.grid(row=2, column=0, padx=5, pady=5)

    def create_result_list(self):
        # Create a frame to hold the result list
        self.result_frame = tk.Frame(self.window)
        self.result_frame.grid(row=0, column=2, padx=10, pady=10, rowspan=self.grid_size+1)

        # Create the result list
        self.results_list = tk.Listbox(self.result_frame, width=50)
        self.results_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.results_scrollbar = tk.Scrollbar(self.result_frame)
        self.results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_list.config(yscrollcommand=self.results_scrollbar.set)
        self.results_scrollbar.config(command=self.results_list.yview)

    def populate_grid(self):
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                self.entries[y][x].delete(0, tk.END)
                self.entries[y][x].insert(tk.END, self.characters[y][x])

    def handle_button1(self):
        self.characters = get_grid()
        self.populate_grid()

    def handle_button2(self):
        self.characters = self.get_character_grid()
        results = spellnoiv.split_code(
            self.characters,
            self.special_coordinates['dw'],
            self.special_coordinates['tl'],
            self.special_coordinates['dl']
        )
        self.update_results_list(results)

    def handle_button3(self):
        self.characters = self.get_character_grid()
        results = spellnoiv.split_code_swap(
            self.characters,
            self.special_coordinates['dw'],
            self.special_coordinates['tl'],
            self.special_coordinates['dl']
        )
        self.update_swap_list(results)

    def handle_special_position_button(self, position):
        def handle_click():
            # Create a new window for selecting the special position
            selection_window = tk.Toplevel(self.window)
            selection_window.title(position.upper() + " Selection")

            # Create a 5x5 button grid
            buttons = [[None] * self.grid_size for _ in range(self.grid_size)]

            def handle_button_click(x, y):
                # Update the special position coordinates
                self.special_positions[position] = (x, y)
                self.special_coordinates[position] = (x, y)

                # Update the label with the selected coordinates
                coordinates_label = self.get_coordinates_label(position)
                coordinates_label.config(text=position.upper() + "({},{})".format(x, y))

                # Close the selection window
                selection_window.destroy()

            def handle_none_button_click():
                # Set the special position coordinates to None
                self.special_positions[position] = None
                self.special_coordinates[position] = None

                # Update the label with the selected coordinates
                coordinates_label = self.get_coordinates_label(position)
                coordinates_label.config(text=position.upper() + "")

                # Close the selection window
                selection_window.destroy()

            # Populate the button grid
            for y in range(self.grid_size):
                for x in range(self.grid_size):
                    button = tk.Button(selection_window, text="({},{})".format(x, y), command=lambda x=x, y=y: handle_button_click(x, y))
                    button.grid(row=y, column=x)
                    buttons[y][x] = button

            # Add a "None" button to clear the special position
            none_button = tk.Button(selection_window, text="None", command=handle_none_button_click)
            none_button.grid(row=self.grid_size, column=self.grid_size)

        return handle_click

    def get_coordinates_label(self, position):
        if position == 'dw':
            return self.dw_coordinates_label
        elif position == 'tl':
            return self.tl_coordinates_label
        elif position == 'dl':
            return self.dl_coordinates_label

    def update_results_list(self, results):
        # Clear previous results
        self.results_list.delete(0, tk.END)

        # Insert results into the list
        for result in results:
            self.results_list.insert(tk.END, '{result[0]} ({result[1]})'.format(result=result))
        
    def update_swap_list(self, swaps):
        # Clear previous swaps
        self.swap_list.delete(0, tk.END)

        # Insert swaps into the list
        for swap in swaps:
            self.swap_list.insert(tk.END, '{swap[2]} at ({swap[1]},{swap[0]}) for {swap[3][0]} ({swap[3][1]}))'.format(swap=swap))

    def get_character_grid(self):
        character_grid = [[''] * self.grid_size for _ in range(self.grid_size)]
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                character = self.entries[y][x].get()
                character_grid[y][x] = character
        return character_grid

    def start(self):
        # Start the GUI event loop
        self.window.mainloop()


 

def get_grid():
    take_screenshot()
    img = read_screenshot()
    gray = convert_to_grayscale(img)
    thresholded = apply_thresholding(gray)
    cropped = crop_center_square(thresholded)
    contours, _ = find_contours(cropped)
    # filtered_contours = filter_contours(contours, thresholded)
    # detected, canvas, lss = detect_letters(filtered_contours, cropped)
    detected, canvas, lss = detect_letters(contours, cropped)
    grid = letters_to_grid(lss)
    return grid

def main():
    grid = get_grid()

    gui = GridGUI(5, grid)
    gui.start()



if __name__ == "__main__":
    main()