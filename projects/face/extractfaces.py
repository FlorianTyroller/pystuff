import cv2
import os
import dlib
import dlib.cuda as cuda
from multiprocessing import Pool

image_folder = 'hasface'
images = []

for filename in os.listdir(image_folder):
    # update progression
    if len(images) % 100 == 0:
        print(f"Processing image #{len(images)} out of {len(os.listdir(image_folder))}")
    img = cv2.imread(os.path.join(image_folder, filename))
    images.append(img)

detector = dlib.get_frontal_face_detector()

faces = []

def process_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = cuda.detect_faces(gray)
    faces = []
    for det in dets:
        x1, y1, x2, y2, _ = det
        face = img[y1:y2, x1:x2]
        resized = cv2.resize(face, (64, 64))
        faces.append(resized)
    return faces

if __name__ == '__main__':
    with Pool() as p:
        p.map(process_image, range(len(images)))

for i, face in enumerate(faces):
    # update progression
    if i % 100 == 0:
        print(f"Processing 3 image #{i} out of {len(faces)}")
    cv2.imwrite(f'faces/1/{i}.png', face)
