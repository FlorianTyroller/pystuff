from board.board import Board
from players.player import Player
from game_config import standard_board_config

import tkinter as tk
import math
import random
import threading
import time

from typing import Tuple, List
from PIL import Image, ImageTk

class Game:
    def __init__(self, clients, states):
        self.gamephase = 0
        self.clients = clients
        self.states = states
        self.config = standard_board_config
        self.starting_player = None
        self.board = Board(self.config)
        self.players = {}
        self.dice_rolls = {}  # Store dice rolls
        self.lock = threading.Lock()  # Synchronize access to shared resources
        self.allowed_commands = {
            0: ["roll"], 1: ["build", "end"], 2: ["roll", "build", "trade", "use", "end"]
        }
        for i,client in enumerate(clients):
            new_player = Player(str(i), i, self.config, client, self.states[i])
            self.players[client.getpeername()] = new_player


    def run(self):
        
        if self.gamephase == 0:
            for state in self.states:
                state.set_commands(self.allowed_commands[self.gamephase])
            self.phase_zero()
        # Additional phases would be handled here

    def process_command(self, client_socket, command):
        if command == "help":
            self.broadcast("test")
        if command == "roll":
            self.handle_roll(client_socket)
        elif command.startswith("build"):
            self.handle_build(client_socket, command)
        elif command.startswith("trade"):
            self.handle_trade(client_socket, command)

    def handle_roll(self, client_socket):
        # Logic to handle a dice roll
        roll_result = random.randint(1, 6)
        self.broadcast(f"Player {client_socket.getpeername()} rolled a {roll_result}")

    def phase_zero(self):
        # Ask each player to roll the dice
        for client in self.clients:
            self.ask_for_dice_roll(client)

        # Wait for all players to roll the dice
        while len(self.dice_rolls) < len(self.clients):
            time.sleep(0.1)  # Avoid busy waiting

        # Determine who had the highest roll
        self.starting_player = max(self.dice_rolls, key=self.dice_rolls.get)
        self.current_player = self.starting_player
        print(f"The starting player is {self.starting_player}")

        # Move to the next phase
        self.gamephase = 1

    def ask_for_dice_roll(self, client):
        # Send a message to the client asking for a dice roll
        message = "Please roll the dice (type 'roll')."
        client.sendall(message.encode('utf-8'))
                
        # Wait for client response, here assuming response handled elsewhere
        # Simulate dice roll response for now
        roll = self.simulate_dice_roll()
        self.lock.acquire()
        self.dice_rolls[client] = roll
        self.lock.release()

    def simulate_dice_roll(self):
        return random.randint(1, 6)  # Simulate a dice roll

    def update_player_states(self):
        for state in self.states:
            state.state = "in_game"

    def broadcast(self, message):
        for client in self.clients:
            client.sendall(message.encode('utf-8'))




def main(): # start game
    pass



if __name__ == "__main__":
    main()
