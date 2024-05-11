import socket
import threading

def listen_to_server(client_socket):
    """
    Continuously listen to messages from the server and print them.
    """
    try:
        while True:
            response = client_socket.recv(1024).decode('utf-8')
            if not response:
                print("Server connection was lost.")
                break
            print("Server >", response)
    finally:
        client_socket.close()

def send_commands_to_server(client_socket):
    """
    Send commands to the server based on user input.
    """
    try:
        while True:
            user_input = input("> ")
            client_socket.sendall(user_input.encode('utf-8'))
            if user_input == "exit":
                break
    finally:
        client_socket.close()

def connect_to_server(host, port):
    """
    Establish connection to the server and initiate listening and sending threads.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server.")

    # Thread for listening to server messages
    listening_thread = threading.Thread(target=listen_to_server, args=(client_socket,))
    listening_thread.start()

    # Function to handle sending user commands to the server
    send_commands_to_server(client_socket)

if __name__ == "__main__":
    connect_to_server('192.168.178.21', 34742)
