import os
from PIL import Image
import hashlib

# Specify the folder containing the images to be processed
folder_path = "data"

# Create a dictionary to store image hashes and file paths
image_dict = {}

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        with Image.open(file_path) as im:
            # Check if the file is a JPEG image
            if im.format == "JPEG":
                # Calculate the hash of the image
                image_hash = hashlib.md5(im.tobytes()).hexdigest()
                # Check if the hash is already in the dictionary
                if image_hash in image_dict:
                    # Delete the file if it is a duplicate
                    os.remove(file_path)
                    print(f"Deleted duplicate file: {filename}")
                else:
                    # Add the hash and file path to the dictionary
                    image_dict[image_hash] = file_path
            else:
                # Delete the file if it is not a JPEG image
                os.remove(file_path)
                print(f"Deleted non-JPEG file: {filename}")
    except:
        # Delete the file if it cannot be opened or processed
        os.remove(file_path)
        print(f"Deleted invalid file: {filename}")
