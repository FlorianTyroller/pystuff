from PIL import Image

input_img = "c:\\Users\\Flori\\Desktop\\pypy\\ffzeug\\inp.jpg"
output_folder = "c:\\Users\\Flori\\Desktop\\pypy\\ffzeug\\jpegs\\"

# load the image with pil
img = Image.open(input_img)
# get the image size
width, height = img.size
length = 100
for i in range(length):
    img2 = img.resize((int(width), int(height)))
    img2.save(output_folder + "out" + str(i) + ".jpg")
    width = width * 0.95
    height = height * 0.95
