import json

# Read the file containing the byte array
with open('tools/logisticsinc/barrayimp.json', 'r') as file:
    byteArray = json.load(file)

# Convert byte array to string
byteString = ''.join(chr(byteArray[str(key)]) for key in range(len(byteArray)))

print(byteString)
"""
# Convert byte string to JSON
try:
    jsonObject = json.loads(byteString)
    print(jsonObject)
except json.JSONDecodeError as e:
    print("Error decoding byte string to JSON:", e)
"""