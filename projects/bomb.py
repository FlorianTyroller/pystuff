import tkinter as tk
from tkinter import ttk

class InputGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Input Fields")
        self.root.geometry("400x300")

        self.input_labels = ["Input 1", "Input 2", "Input 3", "Input 4", "Input 5", "Input 6"]
        self.color_options = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
        self.inputs = []
        self.input_menus = []

        for i in range(len(self.input_labels)):
            label = tk.Label(self.root, text=self.input_labels[i])
            label.grid(row=i, column=0, padx=10, pady=10)

            var = tk.StringVar()
            var.set(self.color_options[0])
            menu = ttk.Combobox(self.root, textvariable=var, values=self.color_options)
            menu.grid(row=i, column=1, padx=10, pady=10)

            self.inputs.append(var)
            self.input_menus.append(menu)

            menu.bind("<<ComboboxSelected>>", self.update_output)

        self.output_label = tk.Label(self.root, text="Output:")
        self.output_label.grid(row=len(self.input_labels), column=0, padx=10, pady=10)

        self.output_text = tk.Text(self.root, height=5, width=30)
        self.output_text.grid(row=len(self.input_labels), column=1, padx=10, pady=10)

    def update_output(self, event):
        inputs = [input.get() for input in self.inputs]
        output = " ".join(inputs)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output)

    def run(self):
        self.root.mainloop()

gui = InputGUI()
gui.run()
