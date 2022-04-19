import urllib.request

r = urllib.request.urlopen("https://www.reddit.com/r/place/?cx=824&cy=431&px=7")


with open('place.html', 'w', encoding='utf-8') as file:
    mybytes = r.read()

    mystr = mybytes.decode("utf-8")
    r.close()
    file.write(mystr)