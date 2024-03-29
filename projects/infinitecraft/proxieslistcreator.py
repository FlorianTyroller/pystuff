import os
import json


def load_proxies(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if the file is not found or corrupt

def save_proxies(filename, proxies):
    with open(filename, 'w') as f:
        data = {} 
        for proxy, score in proxies.items():
            data[proxy] = score
        json.dump(data, f, indent=2) 
    
if __name__ == '__main__':
    proxies = load_proxies('projects/infinitecraft/proxies.json')
    """
    proxies2 = load_proxies('projects/infinitecraft/Free_Proxy_List.json')
    print(proxies)
    for p in proxies2:
        prox = p["ip"] + ":" + p["port"]
        if prox not in proxies:
            proxies[prox] = 1
    save_proxies('projects/infinitecraft/proxies.json', proxies)
    """
    pk = list(proxies.keys())
    for p in pk:
        if p[0] != "h":
            print(p)
            new_p = "https://" + p
            proxies[new_p] = proxies[p]
            del proxies[p]
    save_proxies('projects/infinitecraft/proxies.json', proxies)
