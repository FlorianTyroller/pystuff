import base64
import hashlib
import json
from pyblake2 import blake2s

def base64_encode(input_string):
    encoded_bytes = base64.b64encode(input_string.encode())
    return encoded_bytes.decode()

def base64_decode(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes.decode()



def md5_hash(input_string):
    hash_object = hashlib.md5(input_string.encode())
    return hash_object.hexdigest()

def sha256_hash(input_string):
    hash_object = hashlib.sha256(input_string.encode())
    return hash_object.hexdigest()

def custom_encode(input_string):
    # Implement your custom encoding algorithm here
    encoded_string = input_string.replace('2', 'a').replace('d', 'b').replace('r', 'c')
    return encoded_string

def custom_decode(encoded_string):
    # Implement your custom decoding algorithm here
    decoded_string = encoded_string.replace('a', '2').replace('b', 'd').replace('c', 'r')
    return decoded_string

def base36_to_int(base36_string):
    return int(base36_string, 36)

def convert_base36_to_base64(base36_number):
    # Pad the base36 number to 12 digits
    padded_base36 = base36_number.zfill(12)
    # Encode the padded base36 number using base64
    base64_encoded = base64.b64encode(padded_base36.encode()).decode()
    return base64_encoded

def custom_base64_encode(input_number):
    # Define the base64 characters
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    
    # Convert the input number to base64
    result = ""
    while input_number > 0:
        digit = input_number % 64
        result = base64_chars[digit] + result
        input_number //= 64
    
    return result

def custom_base6e_encode(chars, input_string):
    base6e_chars = chars

    # Convert hexadecimal input string to decimal integer
    decimal_value = int(input_string, 16)

    # Encode the decimal value to base-6e
    result = ""
    while decimal_value > 0:
        digit = decimal_value % 64
        result = base6e_chars[digit] + result
        decimal_value //= 64
    
    return result

def sha1_hash(input_string):
    hash_object = hashlib.sha1(input_string.encode())
    return hash_object.hexdigest()

def blake2s_hash(input_string):
    hash_object = blake2s(input_string.encode())
    return hash_object.hexdigest()

if __name__ == '__main__':
    filename = "projects/prntscr/table.json"
    prnt_base64_chars_v1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
    prnt_base64_chars_v2 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
    prnt_base36_chars = "0123456789abcdefghijklmnopqrstuvwxyz"

    strs = ["2drju61","2drjyi5","2drk2j8", "2drk3ns", "2drkt5b", "2drkwz3", "2drl0c2", "2drl6f9"]
    stren = ["y-1-M_S5FN3x","d0-sQc83gD0C","0sQT3q0wBQcf", "-gv_Z3m6IJKV", "SssDaO4LO6yp","XDJXIGdO3RWX", "IY9bbjVdZ50B", "viXv4kpTdzJt"] 

    jdict = dict()

    for i, s in enumerate(zip(strs, stren)):
        jdict[i] = {"input":{"id": s[0],"id_base10": base36_to_int(s[0])}, "output": {"hash": s[1], "hash_base10_v1": s[1], "hash_base10_v2": s[1]}}
    
    with open(filename, 'w') as f:
        json.dump(jdict, f, indent=4)  # Use indent for pretty-printing

