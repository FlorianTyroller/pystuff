import os
import pygame
import time
import math
import PIL.ImageGrab as ig
from PIL import Image
import pytesseract


size = 480

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Flori\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'



def updateGrid():

    x = 318
    y = 298
    s = ig.grab((x,y,x+size,y+size))
    qlen = 68
    z = (23,50) 
    glen = 7
    grid = [[0 for i in range(glen)] for j in range(glen)]

   
    for i in range(glen):
        for j in range(glen):
            zz = s.crop((j*qlen+z[0], i*qlen+z[0],j*qlen+z[1], i*qlen+z[1]))
     
            grid[j][i] = pytesseract.image_to_string(zz)
    
    print(grid)

    
  







def main():
    updateGrid()
                
    
    
    
                

        



    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")