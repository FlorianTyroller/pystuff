import PIL.ImageGrab
import pytesseract
from PIL import Image
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
x = 294
y = 403
width = 911


#im.show()

#355,501,792+355,501+792
#392,537,428,579

gsize = 7
grid = []

#(329, 519, 329 + 843, 519 + 843)

ilen = width
klen = width//7



nxoff = 47
nyoff = 43

nwidth = 35
nheight = 50



def solve(g,su=13):
    dir = ((-1,0),(1,0),(0,-1),(0,1))
    if su < 19:
        for y,i in enumerate(g):
            for x,j in enumerate(i):
                if j >= su/2:
                    for d in dir:
                        xnew = x + d[0]
                        ynew = y + d[1]
                        if xnew in range(len(g)) and ynew in range(len(g)):
                            if g[ynew][xnew] + j == su:
                                move(x,y,xnew,ynew)
                                print(g[ynew][xnew],j)
                                return

def move(x1,y1,x2,y2):
    pyautogui.moveTo(x+x1*klen+nxoff,y+y1*klen+nyoff)
    
    pyautogui.dragTo(x+x2*klen+nxoff,y+y2*klen+nyoff, button='left',duration=0.2)



while True:
    im = PIL.ImageGrab.grab(bbox=(x, y, x + width, y + width))
    new_image = Image.new('RGB',(gsize*nwidth, gsize*nheight), (250,250,250))
    for i in range(gsize):
        for j in range(gsize):
            a = im.crop((klen*j+nxoff,klen*i+nyoff,klen*j+nxoff+nwidth,klen*i+nyoff+nheight))
            new_image.paste(a,(j*nwidth,i*nheight))



    s = pytesseract.image_to_string(new_image)
    print("scan")
    print(s)
    grid = []
    for i in range(gsize):
        a = list(map(lambda x: int(x) if x.isnumeric() else 99, s[i*8:i*8+7]))
        grid.append(a)
    print(grid)

    solve(grid)




'''
for i in range(gsize):
    for j in range(gsize):

        if im.getpixel((round(p1x + j*klen), round(p1y + i*klen)))[0] < 100:
            grid[i][j] = 6
        else:
            grid[i][j] = 0
            #print(im.getpixel((p1x, p1y + i*10)))

for i in grid:
    print(i)
'''
