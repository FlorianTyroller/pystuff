import os
import cv2


# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Loop through each image in the dataset
for i,filename in enumerate(os.listdir('hasface')):
    # update progression
    if i % 100 == 0:
        print(f"Processing image #{i} out of {len(os.listdir('hasface'))}")
        

    # Load the image
    img = cv2.imread(os.path.join('hasface', filename))

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)

    # Loop through each face and extract it
    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        # Resize the face to 64x64
        face = cv2.resize(face, (64, 64))
        # Save the face as a new image
        cv2.imwrite(os.path.join('faces/2', filename), face)
