import tkinter as tk
import socket
import threading
import json

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                json_message = json.loads(message)
                chat_log.insert(tk.END, "Server > " + json_message['content'] + '\n')
        except Exception as e:
            print("Error receiving message: ", e)
            break

def send(event=None):
    message = my_message.get()
    my_message.set("")  # Clears input field.
    json_message = json.dumps({'type': 'message', 'content': message})
    client_socket.sendall(json_message.encode('utf-8'))
    if message == "exit":
        client_socket.close()
        window.quit()
        
def on_closing():
    """Handle the window closing event."""
    try:
        client_socket.sendall(json.dumps({'type': 'exit', 'content': 'exit'}).encode('utf-8'))
    finally:
        client_socket.close()
    window.quit()
window = tk.Tk()
window.title("Game Client")

frame = tk.Frame(window)
scrollbar = tk.Scrollbar(frame)
chat_log = tk.Text(frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH)
chat_log.pack()
frame.pack()

my_message = tk.StringVar()  # For the messages to be sent.
entry_field = tk.Entry(window, textvariable=my_message)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tk.Button(window, text="Send", command=send)
send_button.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.178.21', 34742))
receive_thread = threading.Thread(target=receive)
receive_thread.start()

tk.mainloop()
