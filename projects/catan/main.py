from board.board import Board
from players.player import Player
from game_config import standard_board_config, standard_board_config_big

import tkinter as tk
import math
import random
import threading
import time
import json

from collections import defaultdict
from typing import Tuple, List
from PIL import Image, ImageTk

class Game:
    def __init__(self, participants):
        self.participants = participants # key = client, value = (name, state)
        self.gamephase = 0
        self.config = standard_board_config
        self.starting_player_id = -1
        self.board = Board(self.config)
        self.players = {}
        self.dice_rolls = {}  # Store dice rolls
        self.lock = threading.Lock()  # Synchronize access to shared resources
        self.allowed_commands = {
            0: ["roll"], 1: ["build", "end"], 2: ["roll", "build", "trade", "use", "end"]
        }
        for i,p in enumerate(self.participants):
            new_player = Player(self.participants[p][0], i, self.config, p,self.participants[p][1])
            self.players[i] = new_player

        self.client_to_player = {}
        for p in self.players.values():
            self.client_to_player[p.client] = p

        self.phase_zero_rolls = []
        self.phase_two_roll = None
        self.end_turn = False
        self.player_waiting = False  # is the player waiting for new actions

    def run(self):
        self.broadcast('init_board',self.board.to_small_dict())
        # Phase 0
        self.gamephase = 0
        self.broadcast(f'game_info', f'Phase {self.gamephase}: roll play order')
        self.phase_zero()
        
        # Phase 1 
        self.gamephase = 1
        self.broadcast(f'game_info', f'Phase {self.gamephase}: place first settlements and roads')
        self.phase_one()

        # Phase 2, Main Phase
        self.gamephase = 2
        self.broadcast(f'game_info', f'Phase {self.gamephase}: Main gamephase')
        self.phase_two()



    def process_command(self, client_socket, command):
        if command['type'] == 'roll':
            self.handle_roll(client_socket)
        elif command['type'] == 'build':
            self.handle_build(client_socket, command['content'], command['building'])
            self.player_waiting = True
        elif command['type'] == 'trade':
            self.handle_trade(client_socket, command)
            self.player_waiting = True
        elif command['type'] == 'end_turn':
            self.handle_end_turn(client_socket)
        
        self.update_all_players()
    
    def handle_end_turn(self, client_socket):
        self.end_turn = True

    def handle_build(self, client_socket, coords, building):
        player = self.client_to_player[client_socket]
        if building == 'settlement':
            k = ((coords[0][0], coords[0][1]), (coords[1][0], coords[1][1]), (coords[2][0], coords[2][1]))
            # update board
            self.board.corners[k].set_building(building)
            self.board.corners[k].set_owner(player.player_id)
            # update player
            player.build(building = building, gamephase = self.gamephase, placement = k)

            self.update_corners(k)
        
        if building == 'city':
            k = ((coords[0][0], coords[0][1]), (coords[1][0], coords[1][1]), (coords[2][0], coords[2][1]))
            # update board
            self.board.corners[k].set_building(building)
            self.board.corners[k].set_owner(player.player_id)
            # update player
            player.build(building = building, gamephase = self.gamephase, placement = k)

            self.update_corners(k)

        elif building == 'road':
            k = ((coords[0][0], coords[0][1]), (coords[1][0], coords[1][1]))
            # update board
            self.board.edges[k].set_owner(player.player_id)
            # update player
            player.build(building = building, gamephase = self.gamephase, placement = k)

            self.update_edges(k)

    


    def handle_roll(self, client_socket):
        # Logic to handle a dice roll
        """
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        r = d1+d2
        """
        d1 = 3
        d2 = 4
        r = 7

        if self.gamephase == 0:
            self.lock.acquire()
            self.phase_zero_rolls.append((self.client_to_player[client_socket].player_id, r))
            self.lock.release()
            self.broadcast('game_info', f'Player {self.client_to_player[client_socket].name} rolled a {r} > ({d1},{d2})')
        elif self.gamephase == 2:
            self.phase_two_roll = r
            self.broadcast('game_info', f'Player {self.client_to_player[client_socket].name} rolled a {r} > ({d1},{d2})')

    def phase_zero(self):
        self.broadcast('allow_actions', {'roll': None})
        while len(self.phase_zero_rolls) < len(self.players):
            time.sleep(0.5)

        # determin who goes first
        self.starting_player_id = sorted(self.phase_zero_rolls, key=lambda x: x[1], reverse=True)[0][0]
        self.broadcast(f'game_info', f'Player {self.players[self.starting_player_id].name} begins')
        self.player_order = [i%len(self.players) for i in range(self.starting_player_id, self.starting_player_id + len(self.players))]

    def phase_one(self):
        player_order_one = self.player_order + self.player_order[::-1]

        while len(player_order_one) > 0:
            current_player_id = player_order_one.pop()
            current_player = self.players[current_player_id]

            settlement_pos = current_player.get_valid_corner_pos(self.board.corners)
            self.send_message(current_player, 'allow_actions', {'build': {'settlement': settlement_pos}})
            # wait till settlement placed
            if len(player_order_one) >= len(self.players):
                while len(current_player.buildings['settlement']) < 1:
                    time.sleep(0.4)
            else:
                while len(current_player.buildings['settlement']) < 2:
                    time.sleep(0.4)

            road_pos = current_player.get_valid_road_pos(self.board.edges, self.board.corners)
            self.send_message(current_player, 'allow_actions', {'build': {'road': road_pos}})

            while len(current_player.buildings['road']) < len(current_player.buildings['settlement']):
                time.sleep(0.4)


    def phase_two(self):
        counter = 0
        number_players = len(self.players)
        while True:
            # get current_player
            current_player_id = self.player_order[counter%number_players]
            current_player = self.players[current_player_id]

            self.broadcast(f'game_info', f'Player {current_player.name}\'s turn')
            # enable roll, wait for roll
            self.phase_two_roll = None
            self.send_message(current_player, 'allow_actions', {'roll': None})
            while self.phase_two_roll is None:
                time.sleep(0.5)

            # handle resource distribution
            self.distribute_resources(self.phase_two_roll)
            # update players
            self.update_all_players()

            # enable correct actions then wait for end turn
            self.end_turn = False
            self.player_waiting = True
            while self.end_turn == False:
                if self.player_waiting:
                    actions = current_player.get_legal_moves(True, self.board.edges, self.board.corners)
                    self.send_message(current_player, 'allow_actions', actions)
                    self.player_waiting = False
                time.sleep(0.5)
            

            # increment counter
            counter += 1



    def distribute_resources(self, r):
        # get tiles with rolled number
        res_tracker = defaultdict(lambda: defaultdict(int))
        print(self.board.number_to_tiles)
        tiles = self.board.number_to_tiles[r]
        # get all 6 corner_keys for each tile
        for t in tiles:
            tile = t.coord
            # adj tile keys:
            top_left = (tile[0] - 1, tile[1] + 1)
            top_right = (tile[0], tile[1] + 1)
            right = (tile[0] + 1, tile[1])
            bottom_right = (tile[0] + 1, tile[1] - 1)
            bottom_left = (tile[0], tile[1] - 1)
            left = (tile[0] - 1, tile[1])

            # corner keys:
            c_top_left = (left, top_left, tile)
            c_top = (top_left, tile, top_right)
            c_top_right = (tile, top_right, right)
            c_bottom_right = (tile, bottom_right, right)
            c_bottom = (bottom_left, tile, bottom_right)
            c_bottom_left = (left, bottom_left, tile)

            l = [c_top_left,c_top,c_top_right,c_bottom_right,c_bottom,c_bottom_left]

            # get owner_id of each corner
            for corner_key in l:
                # skip if no owner
                corner = self.board.corners[corner_key]
                if corner.is_available():
                    continue
                
                # 1 res for settlment, 2 for city sus
                if corner.building == 'settlement':
                    self.players[corner.owner_id].resources[t.resource] += 1
                    res_tracker[self.players[corner.owner_id].name][t.resource] += 1
                elif corner.building == 'city':
                    self.players[corner.owner_id].resources[t.resource] += 2
                    res_tracker[self.players[corner.owner_id].name][t.resource] += 2
        
        # broadcast resources
        for player, v in res_tracker.items():
            for res, r_v in v.items():
                self.broadcast('game_info', f'{r_v} {res} for {player}')

    def update_player_states(self):
        for state in self.states:
            state.state = "in_game"

    def send_message(self, player, mtype, message):
        json_m = json.dumps({'type': mtype, 'content': message}) + '\n'
        encoded_json = json_m.encode('utf-8')
        player.client.sendall(encoded_json)

    def broadcast(self, mtype,  message):
        json_m = json.dumps({'type': mtype, 'content': message}) + '\n'
        encoded_json = json_m.encode('utf-8')
        for player in self.players.values():
            player.client.sendall(encoded_json)
    
    def update_all_players(self):
        for player1 in self.players.values():
            d = {'other_players':[]}
            for player2 in self.players.values():
                if player1.player_id == player2.player_id:
                    d['main_player'] = player2.get_all_info()
                else:
                    d['other_players'].append(player2.get_public_info())
            
            json_m = json.dumps({'type': 'update_players', 'content': d})  + '\n'
            encoded_json = json_m.encode('utf-8')
            player1.client.sendall(encoded_json)
    
    def update_corners(self, corner_key):
        d = {'Corners': [self.board.corners[corner_key].to_dict(),]}
        self.broadcast('update_board_corners', d)

    def update_edges(self, edge_key):
        d = {'Edges': [self.board.edges[edge_key].to_dict(),]}
        self.broadcast('update_board_edges', d)




def main(): # start game
    return
    board = Board(config=standard_board_config)
    print(board.to_dict())



if __name__ == "__main__":
    main()
