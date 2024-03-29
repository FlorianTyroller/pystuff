import os
import json
import re


COMBINE_LIST_FILE = "projects/infinitecraft/discov_list.json"
COMBINE_LIST_FILE_NO_NUMBER = "projects/infinitecraft/discov_list_no_number.json"

def load_combine_list():
    if os.path.exists(COMBINE_LIST_FILE):
        with open(COMBINE_LIST_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_combine_list(combine_list):
    with open(COMBINE_LIST_FILE_NO_NUMBER, "w") as f:
        json.dump(combine_list, f)



def convert_to_no_number(combine_list):
    new_combine_list = {}
    for i,key in enumerate(combine_list):
        split_k = key.split(" ")
        e_part = split_k[0]
        # combine the other parts
        n_part = " ".join(split_k[1:])
        # check if a digit is in the key
        if not bool(re.search(r"\d", n_part)):
            n_key = e_part + " " + n_part
            new_combine_list[n_key] = combine_list[key]
        
    return new_combine_list
        

    # return new_combine_list



if __name__ == "__main__":
    l = load_combine_list()
    e = convert_to_no_number(l)
    save_combine_list(e)
    """
    l_keys = l.keys()
    # sort l_keys by length
    l_keys = list(l_keys)
    l_keys.sort(key=len, reverse=True)

    for i,key in enumerate(l_keys):
        print(key, l[key])
        if i > 10:
            break
    """