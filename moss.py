from pathlib import Path
import pywintypes, win32file, win32api

# Import the os module
import os


filename = 'C:/Users/Flori/Desktop/MOSS/2021-10-22_181629_927242934_1246407802.zip'

stats = os.stat(filename)

f = open(filename +"_stats.txt", "w")
for stat in stats:
    f.write(str(stat) + "\n")
f.close()

f = open(filename +"_stats.txt", "r")
print(f.read())
f.close()



def changeFileStats(fname, newStats):
    win32api.SetFileAttributes(fname, )



changeFileStats(filename +"_stats.txt", ())