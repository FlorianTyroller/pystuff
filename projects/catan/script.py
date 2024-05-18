import subprocess
import time

# Command to run server.py
server_command = ["python", "projects/catan/server.py"]

# Command to run tkintertest.py
tkinter_command = ["python", "projects/catan/tkintertest.py"]

# Open the first shell and run server.py
server_process = subprocess.Popen(server_command, shell=True)
print("Started server.py")

# Wait for 1 second
time.sleep(1)

# Open the second shell and run tkintertest.py
tkinter_process1 = subprocess.Popen(tkinter_command, shell=True)
print("Started first instance of tkintertest.py")

# Open the third shell and run tkintertest.py
tkinter_process2 = subprocess.Popen(tkinter_command, shell=True)
print("Started second instance of tkintertest.py")
