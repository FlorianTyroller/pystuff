

import os
import random
from PIL import Image, UnidentifiedImageError

# Set the directory path to process

directory = "C:/Users/Flori/Desktop/r map 2"

# Define the function for creating the acid effect


def acid_effect(image):
    # Get the number of channels in the image
    num_channels = len(image.getbands())
    # Check if the image has exactly three channels
    if num_channels == 3:
        # Split the image into RGB channels
        r, g, b = image.split()
        # Get the dimensions of the image
        width, height = image.size
        # Create new RGB channels with random colors
        r_pixels = Image.new("L", (width, height), (random.randint(0, 255)))
        g_pixels = Image.new("L", (width, height), (random.randint(0, 255)))
        b_pixels = Image.new("L", (width, height), (random.randint(0, 255)))
        # Combine the new RGB channels into a single image
        new_image = Image.merge("RGB", (r_pixels, g_pixels, b_pixels))
    else:
        # If the image doesn't have exactly three channels, convert it to RGB mode
        new_image = image.convert("RGB")
        # Split the image into RGB channels
        r, g, b = new_image.split()
        # Get the dimensions of the image
        width, height = new_image.size
        # Create new RGB channels with random colors
        r_pixels = Image.new("L", (width, height), (random.randint(0, 255)))
        g_pixels = Image.new("L", (width, height), (random.randint(0, 255)))
        b_pixels = Image.new("L", (width, height), (random.randint(0, 255)))
        # Combine the new RGB channels into a single image
        new_image = Image.merge("RGB", (r_pixels, g_pixels, b_pixels))
    # Return the new image
    return new_image


for root, dirs, files in os.walk(directory):
    for file in files:
        # Check if the file is a .dds file
        if file.endswith('.dds'):
            try:
                # Open the image file using Pillow
                with Image.open(os.path.join(root, file)) as image:
                    # Set the color to white if the filename contains "chunk", otherwise set it to black
                    if "chunk" in file or "grnd" in file:
                        color = (255, 255, 255)
                    else:
                        color = (0, 0, 0)
                    # Create a new image with the same size and mode as the original, filled with the selected color
                    new_image = Image.new(image.mode, image.size, color)
                    # Copy over the original image's encoding
                    new_image.info = image.info
                    # Save the new image to the same path as the original
                    new_image.save(os.path.join(root, file))
            except UnidentifiedImageError as e:
                # If there's an error opening the image, skip over it and print an error message
                print(f"Error processing {file}: {e}")
                continue

        else:
            # Remove non-folder files that don't end with ".dds"
            pass
        """
            if not os.path.isdir(os.path.join(root, file)):
                if not file.endswith(".dds"):
                    os.remove(os.path.join(root, file)) """
