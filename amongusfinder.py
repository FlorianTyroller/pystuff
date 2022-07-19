from PIL import Image
import concurrent.futures
import numpy as np
import itertools

amogi_1_4 = [
    [1,0,0,0],  
    [0,0,0,0]
]

amogi_2_4 = [
    [0,0,2,2],
    [0,0,0,2],
    [0,0,2,22],
    [22,0,2,2],
    [22,0,0,2],
    [222,0,2,22]
]

amogi_3_4 = [
    [0,0,0,0],
    [3,0,0,0]
]

amogi_4_4 = [
    [0,0,0,0],
    [4,0,0,0],
    [4,0,44,0]
]

amogi_5_4 = [
    [5,0,55,0],
    "x"
]

def build_amogi(a1,a2,a3,a4,a5):
    a = [a1,a2,a3,a4,a5]
    return list(itertools.product(*a))




    

scale = 1
iName = "amogus3.png"
dName = "allAmogi.png"
s = Image.open(iName)

def scaleAmogusUp(a, scale):
    scaledA = list()

    for t in a:
        row = list()
        for tt in t:
            for i in range(scale):
                row.append(tt)
            
        for i in range(scale):
            scaledA.append(row)
    
    return scaledA

def reverse(am):
    ra = list()
    for a in am:
        ra.append(a[::-1])
    return ra


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))



def main():
    amogi = build_amogi(amogi_1_4, amogi_2_4, amogi_3_4, amogi_4_4, amogi_5_4)
    l = list()
    
    for a in amogi:
        a = list(a)
        try:
            a.remove("x")
        except Exception:
            None

        l.append(a)
        l.append(reverse(a))


    
    width, height = s.size
    dGrid = np.zeros((height, width, 4), dtype=np.uint8)


    n = 10
    
    for e in split(l,n):
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(start, e)

            for result in results:
                dGrid = np.add(f.result(), dGrid)



    d = Image.fromarray(dGrid, 'RGBA')


    d.save(dName)

    d.show()
    
    d.close()



def printAmogus(a):
    for i in a:
        print(i)

def start(amogus):
    counter = 0
    width, height = s.size
    if scale > 1:
        amog = scaleAmogusUp(amogus, 2)
    else: 
        amog = amogus
    aHeight, aWidth = len(amog), len(amog[0])

    #d  = Image.new(mode = "P", size = (width, height), color = 255)
    
    dGrid = np.zeros((height, width, 4), dtype=np.uint8)

    for y in range(height):
        for x in range(width):

            cDict = dict()
            valid = True
            for ay in range(aHeight):
                if not valid:
                    break
                for ax in range(aWidth):
                    if not valid:
                        break
                    v = amog[ay][ax]
                    try:
                        p = s.getpixel((x+ax,y+ay))
                    except:
                        valid = False
                        break
                    if v in cDict.keys():
                        if cDict[v] != p:
                            valid = False
                            break
                    else:
                        cDict[v] = p
                    
                    if 0 in cDict.keys():
                        if list(cDict.values()).count(cDict[0]) > 1:
                            valid = False
                            break
                

                    




            if valid:
                counter += 1
                for ay in range(aHeight):
                    for ax in range(aWidth):
                        dGrid[y+ay,x+ax] = s.getpixel((x+ax,y+ay))


    s.close()
    print("added %i amogi" % (counter))
    return dGrid
    
    
    

if __name__ == "__main__":
    main()