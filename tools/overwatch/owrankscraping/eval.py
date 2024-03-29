import os
import cv2
import numpy as np
import pyautogui
import time
import matplotlib.pyplot as plt



def main():
    champs1 =  {'ana': 91, 'bap': 2, 'brig': 9, 'kiriko': 258, 'lucio': 66, 'mercy': 60, 'moira': 3, 'zen': 11}
    champs2 =  {'ana': 208, 'bap': 12, 'brig': 12, 'kiriko': 132, 'lucio': 66, 'mercy': 13, 'moira': 10, 'zen': 40}
    champs3 =  {'ana': 115, 'bap': 64, 'brig': 15, 'kiriko': 46, 'lucio': 89, 'mercy': 20, 'moira': 10, 'zen': 122}

    ratios = [(1,0,0), (1,1,1), (4,2,1), (1,0.75,0.5)]
    for ratio in ratios:
        evaluate(champs1, champs2, champs3,ratio)

def evaluate(champs1, champs2, champs3, ratio):
    

    # The input dictionary
    # combine dicts according to ratio
    data = dict()
    for key in champs1:
        data[key] = champs1[key] * ratio[0] + champs2[key] * ratio[1] + champs3[key] * ratio[2]
    
    # Sort the dictionary by value
    sorted_data = sorted(data.items(), key=lambda x: -x[1])

    # Extract the keys and values from the sorted dictionary
    keys = [item[0].replace('.png', '') for item in sorted_data]
    values = [item[1] for item in sorted_data]

    # Set the figure size
    plt.figure(figsize=(10, 5))



    # Plot the data as a bar chart
    plt.bar(keys, values)

    # Set the x-axis labels
    plt.xticks(rotation=90)

    code = str(ratio).replace(',','').replace('(','').replace(')','').replace('.','').replace(' ', '')
    # Save the plot
    plt.savefig('imgs/figs/supp/12.01.2023/as_supp' + code + '.png')




if __name__ == '__main__':
    main()
