import os



ais = ["code_magic_flat_reduce.py","codemagic2.py","codemagic_best_choice.py","codemagic_half_reduce.py"]
dicti = {}

for i,ai in enumerate(ais):
    dicti[i] = [ai,1000]

# get all unique pairings of ais
pairings = []
for i in range(len(ais)):
    for j in range(i+1,len(ais)):
        pairings.append([i,j])


stream = os.popen('java --add-opens java.base/java.lang=ALL-UNNAMED C:/Users/Flori/Desktop/LegendsOfCodeAndMagic-master/src/test/java/Main.java a b')
output = stream.read()

print(output)