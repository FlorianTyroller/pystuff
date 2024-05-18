import socket
import threading
import time
import json
import logging

from main import Game

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(threadName)s] %(levelname)s: %(message)s')

class Lobby:
    def __init__(self, name, l_id):
        self.l_id = l_id
        self.is_joinable = True
        self.name = name
        self.participants = {} # key = client, value = (name, state)
        self.game = None

    def get_info(self):
        info = dict()
        info['id'] = self.l_id
        info['name'] = self.name
        names = []
        for p in self.participants.values():
            names.append(p[0])
        info['participants'] = names

        return info

    def add_client(self, client_socket, state, name):
        if not self.is_joinable:
            return False
        self.participants[client_socket] = (name, state)
        self.broadcast('recieve_lobby_chat', {'user': 'Lobby', 'chat': f'{name} joined the lobby'})
        self.broadcast('lobby_info', self.get_info())
        return True

    def remove_client(self, client_socket, state):
        self.participants.pop(client_socket)
        self.broadcast('recieve_lobby_chat', {'user': 'Lobby', 'chat': f'{name} left the lobby'})
        self.broadcast('lobby_info', self.get_info())
        return len(self.clients)

    def start_game(self):
        self.is_joinable = False
        self.broadcast('recieve_lobby_chat', {'user': 'Lobby', 'chat': f'Starting Game in 5 Seconds'})
        for i in range(5):
            self.broadcast('recieve_lobby_chat', {'user': 'Lobby', 'chat': f"{5-i}.."})
            time.sleep(1)
        
        self.broadcast('show_game', None)
        self.update_player_states()
        self.game = Game(self.participants)
        game_thread = threading.Thread(target=self.game.run)
        game_thread.start()

    def update_player_states(self):
        for p in self.participants.values():
            p[1].state = "in_game"

    def broadcast(self, mtype,  message):
        json_m = json.dumps({'type': mtype, 'content': message}) + '\n'
        encoded_json = json_m.encode('utf-8')
        for client in self.participants:
            client.sendall(encoded_json)

class ClientState:
    def __init__(self):
        self.state = "no_lobby"
        self.commands = {
            "no_lobby": ["create", "join", "list", "exit"],
            "in_lobby": ["leave", "start", "list", "exit"],
            "in_game": []
        }

    def set_commands(self, commands):
        self.commands[self.state] = commands 

    def get_commands(self):
        return self.commands[self.state]

    def send_commands(self, client_socket):
        available_commands = ', '.join(self.get_commands())
        client_socket.sendall(f"Available commands: {available_commands}".encode('utf-8'))

class GameServer:
    def __init__(self, host, port):
        self.current_lobby_id = 0
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lobbies = dict()
        self.client_states = {}

    def send_response(self, client_socket, rtype, content):
        msg = {'type': rtype, 'content': content}
        json_message = json.dumps(msg) + '\n'
        client_socket.sendall(json_message.encode('utf-8'))


    def handle_client(self, client_socket, address):
        logging.info(f"Connected to {address}")
        client_name = None
        state = ClientState()
        c_lobby = None
        self.client_states[client_socket] = state
        

        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                message = json.loads(message)
                logging.info(f"Received: {message}")

                if 'type' not in message:
                    self.send_response(client_socket, "error", "key \"type\" not in msg")
                    continue

                if state.state == "in_game":
                    if c_lobby is not None:
                        c_lobby.game.process_command(client_socket, message)
                    continue
                if message['type'] == "set_name":
                    client_name = message['content']
                    self.send_response(client_socket,'show_menu', None)
                
                elif message['type'] == 'start_game':
                    self.lobbies[message['content']].start_game()

                elif message['type'] == 'get_lobbies':
                    lobbies_info = []
                    if len(self.lobbies) > 0:
                        for v in self.lobbies.values():
                            lobbies_info.append(v.get_info())
                    self.send_response(client_socket,'get_lobbies',lobbies_info)
                
                elif message['type'] == 'join_lobby':
                    lobby_id = int(message['content'])
                    self.lobbies[lobby_id].add_client(client_socket,state,client_name)
                    c_lobby = self.lobbies[lobby_id]
                    #response
                    self.send_response(client_socket, 'join_lobby', None)
                    self.send_response(client_socket, 'lobby_info', self.lobbies[lobby_id].get_info())

                elif message['type'] == 'create_lobby':
                    # create lobby
                    lobby_name = message['content']
                    lobby_id = self.current_lobby_id
                    self.current_lobby_id += 1
                    newLobby = Lobby(lobby_name,lobby_id)
                    c_lobby = newLobby
                    self.lobbies[lobby_id] = newLobby

                    # add client
                    newLobby.add_client(client_socket,state,client_name)

                    #response
                    self.send_response(client_socket, 'join_lobby', None)
                    self.send_response(client_socket, 'lobby_info', newLobby.get_info())
    
                elif message['type'] == 'send_lobby_chat':
                    chat = message['content']['chat']
                    lobby_id =  message['content']['lobby_id']
                    self.lobbies[lobby_id].broadcast('recieve_lobby_chat', {'user': client_name, 'chat': chat})

                else:
                    self.send_response(client_socket, "error", f"{cmd} is not a valid command, type \"help\" for a list of valid commands")
                
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
