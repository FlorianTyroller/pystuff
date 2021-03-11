import socket
import sys
import time

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)

name = input('Enter name:')
new_socket.listen(1)

conn, add= new_socket.accept()
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])