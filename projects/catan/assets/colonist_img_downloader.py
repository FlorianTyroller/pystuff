import httpx
import os


#alist = ["red", "green", "orange", "blue", "yellow", "brown", "black", "white"]
#blist = ["city", "road", "settlement"]
alist = ["tile", "card"]
blist = ["book","books","knowledge","paper"]
url = "https://colonist.io/dist/images/road_green.svg"

with httpx.Client() as client:
    for a in alist:
        for b in blist:
            url = f"https://colonist.io/dist/images/{a}_{b}.svg"
            filename = f"{a}_{b}.svg"
            response = client.get(url)


            print(response.status_code)
            
            if response.status_code == 200:
                with open(f"C:/Users/Flori/Desktop/pypy/projects/catan/assets/images/{filename}", 'wb') as file:
                    file.write(response.content)
