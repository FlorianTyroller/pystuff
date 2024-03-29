import cv2
import os

# Specify the folder containing the images to be processed
folder_path = "data"

# Create a CascadeClassifier object to detect faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create the "hasface" and "noface" folders if they do not exist
if not os.path.exists("hasface"):
    os.makedirs("hasface")
if not os.path.exists("noface"):
    os.makedirs("noface")

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        # Read the image using OpenCV
        img = cv2.imread(file_path)
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))
        # If no faces are detected, move the file to the "noface" folder
        if len(faces) == 0:
            os.rename(file_path, os.path.join("noface", filename))
            print(f"Moved file with no faces: {filename}")
        # If faces are detected, move the file to the "hasface" folder
        else:
            os.rename(file_path, os.path.join("hasface", filename))
            print(f"Moved file with faces: {filename}")
    except:
        # Delete the file if it cannot be opened or processed
        os.remove(file_path)
        print(f"Deleted invalid file: {filename}")
