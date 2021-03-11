import numpy
import random
import sys
import PySimpleGUI as sg



i = 0

layout = [
    [   

        sg.Text("",key=i)

    ]
]
# Create the window
window = sg.Window("Board Analyzer", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break