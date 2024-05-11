import socket
import threading
import time

from main import Game

class Lobby:
    def __init__(self, name):
        self.is_joinable = True
        self.name = name
        self.clients = []
        self.states = []
        self.game = None

    def add_client(self, client_socket, state):
        if not self.is_joinable:
            return False
        self.clients.append(client_socket)
        self.states.append(state)
        print(f"Added client to {self.name}. Total clients: {len(self.clients)}")
        self.broadcast(f"a client joined the lobby, there are {len(self.clients)} in the lobby")
        return True

    def remove_client(self, client_socket, state):
        self.clients.remove(client_socket)
        self.state.remove(state)
        print(f"Client left {self.name}. Remaining clients: {len(self.clients)}")
        self.broadcast(f"a client left the lobby, there are {len(self.clients)} in the lobby")
        return len(self.clients)

    def start_game(self):
        self.is_joinable = False
        self.broadcast(f"starting game with {len(self.clients)} players in 5 seconds")
        for i in range(5):
            self.broadcast(f"{5-i}..")
            time.sleep(1)
        self.update_player_states()
        self.game = Game(self.clients, self.states)
        game_thread = threading.Thread(target=self.game.run)
        game_thread.start()

    def update_player_states(self):
        for state in self.states:
            state.state = "in_game"

    def broadcast(self, message):
        for client in self.clients:
            client.sendall(message.encode('utf-8'))

class ClientState:
    def __init__(self):
        self.current_lobby = None
        self.state = "no_lobby"
        self.commands = {
            "no_lobby": ["create", "join", "list", "exit"],
            "in_lobby": ["leave", "start", "list", "exit"],
            "in_game": []
        }

    def join_lobby(self, lobby):
        self.current_lobby = lobby
        self.state = "in_lobby"

    def leave_lobby(self):
        old_lobby = self.lobby
        self.lobby = None
        self.state = "no_lobby"
        return old_lobby

    def set_commands(self, commands):
        self.commands[self.state] = commands 

    def get_commands(self):
        return self.commands[self.state]

    def send_commands(self, client_socket):
        available_commands = ', '.join(self.get_commands())
        client_socket.sendall(f"Available commands: {available_commands}".encode('utf-8'))

class GameServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lobbies = set()
        self.client_states = {}

    def handle_client(self, client_socket, address):
        state = ClientState()
        self.client_states[client_socket] = state
        state.send_commands(client_socket)

        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                args = message.split(" ")

                cmd = args[0]
                args = args[1:]
                
                if cmd == "help": # universal command
                    state.send_commands(client_socket)
                    continue
                
                if state.state == "in_game":
                    state.current_lobby.game.process_command(client_socket, message)
                    continue

                if cmd in state.get_commands():
                    client_socket.sendall(f"{cmd} is a valid command".encode('utf-8'))
                    if cmd == "join":
                        if args:
                            for lobby in self.lobbies:
                                if lobby.name == args[0]:
                                    result = lobby.add_client(client_socket, state)
                                    if result:
                                        client_socket.sendall(f"joining lobby {args[0]}".encode('utf-8'))
                                        state.join_lobby(lobby)
                                    else:
                                        client_socket.sendall(f"lobby {args[0]} is not joinable".encode('utf-8'))
                                    
                    elif cmd == "create":
                        if args:
                            for lobby in self.lobbies:
                                if lobby.name == args[0]:
                                    client_socket.sendall(f"lobby already exists, try join".encode('utf-8'))
                                    break
                            else:
                                new_lobby = Lobby(args[0])
                                new_lobby.add_client(client_socket, state)
                                state.join_lobby(new_lobby)
                                self.lobbies.add(new_lobby)

                    elif cmd == "leave":
                        lobby = state.leave_lobby()
                        lobby.remove_client(client_socket, state)
                    
                    elif cmd == "list":
                        if len(self.lobbies) > 0:
                            client_socket.sendall(f"Currently open Lobbies:".encode('utf-8'))
                            for lobby in self.lobbies:
                                client_socket.sendall(f"{lobby.name} with {len(lobby.clients)}".encode('utf-8'))
                    
                    elif cmd == "start":
                        state.current_lobby.start_game()
                else:
                    client_socket.sendall(f"{cmd} is not a valid command, type \"help\" for a list of valid commands".encode('utf-8'))
                
        finally:
            """if state.current_lobby:
                state.current_lobby.remove_client(client_socket)
            del self.client_states[client_socket]"""
            client_socket.close()

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                thread.start()
        finally:
            self.server_socket.close()

if __name__ == "__main__":
    server = GameServer('192.168.178.21', 34742)
    server.start()
