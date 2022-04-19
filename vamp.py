import plyvel

path  = r'C:\Users\Flori\AppData\Roaming\Vampire_Survivors\Local Storage\leveldb'

db = plyvel.DB(path, create_if_missing=False)


print(bytes('\x01["GREED","GREED","GROWTH","GROWTH","GROWTH","AMOUNT","COOLDOWN","LUCK","LUCK","LUCK","POWER","POWER","POWER","AREA","SPEED","DURATION","REGEN","MAGNET","MAGNET","AREA","DURATION","GREED","GREED","GREED","SPEED","MOVESPEED","MOVESPEED","POWER","POWER","ARMOR","ARMOR","ARMOR","MAXHEALTH","MAXHEALTH","MAXHEALTH","REGEN","REGEN","REGEN","REGEN","GROWTH","GROWTH"]'))

#db.put(b'_file://\x00\x01CapacitorStorage.BoughtPowerups', b'\x01["GREED","GREED","GROWTH","GROWTH","GROWTH","AMOUNT","COOLDOWN","LUCK","LUCK","LUCK","POWER","POWER","POWER","AREA","SPEED","DURATION","REGEN","MAGNET","MAGNET","AREA","DURATION","GREED","GREED","GREED","SPEED","MOVESPEED","MOVESPEED","POWER","POWER","ARMOR","ARMOR","ARMOR","MAXHEALTH","MAXHEALTH","MAXHEALTH","REGEN","REGEN","REGEN","REGEN","GROWTH","GROWTH"]')



#print(db.get(b'_file://\x00\x01CapacitorStorage.BoughtPowerups'))