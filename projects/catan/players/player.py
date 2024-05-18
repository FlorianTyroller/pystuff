import random
from board.edge import Edge
from board.corner import Corner 
from typing import Dict, List, Tuple, Optional, Set

class Player:
    def __init__(self, name: str, player_id: int, config: Dict, client, state) -> bool:
        self.name: str = name
        self.player_id: int = player_id
        self.config: Dict = config
        self.resources: Dict[str, int] = {res: 0 for res in config['resource_types']}
        self.development_cards: List[str] = []
        self.buildings: Dict[str, Set] = {building: set() for building in config['buildings']}
        self.victory_points: int = 0
        self.can_roll_dice: bool = False
        self.can_end_turn: bool = False
        self.can_trade: bool = False
        self.can_build: bool = False
        self.is_at_turn: bool = False
        self.client = client
        self.state = state
        

    def build(self, building: str, gamephase: int, placement: Optional[Tuple] = None) -> bool:
        
        if gamephase == 2:
            recipe = self.config['buildings'][building]['recipe']
            for res in recipe['resources']:
                self.resources[res] -= recipe['resources'][res]
            for build in recipe['buildings']:
                if placement is not None:
                    self.buildings[build].remove(placement)
        
        if placement is not None:
            self.buildings[building].add(placement)
        else:
            self.buildings[building] += 1

        return True

    def start_turn(self, gamephase: int):
        self.is_at_turn = True
        if gamephase == 1:
            self.can_build = True
            return
        self.can_roll_dice = True

    def roll_dice(self, gamephase: int, amount: int = 2):
        self.can_roll_dice = False
        self.can_end_turn = True
        if gamephase == 2:
            self.can_build = True
            self.can_trade = True
        return [random.randint(1, 6) for _ in range(amount)]

    def end_turn(self, gamephase: int):
        self.can_roll_dice = False
        self.can_end_turn = False
        self.can_trade = False
        self.is_at_turn = False
        self.can_build = False
    
    def get_valid_corner_pos(self, corners: Dict[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]], Corner]):
        # check all corners
        valid_corners = []
        for corner in corners:
            if not corners[corner].is_available():
                continue

            #check if corner of upsiode down or normal triangle

            #if y coordinate of middle coord > than y coordinate of other two -> normal, otherwise, upside down
            keys_to_check = []
            a = corner[0]
            b = corner[1]
            c = corner[2]
            if c[1] > b[1]:
                # normal triangle
                # check corner bottom left, bottom right and up
                
                bottom_left_key = ((b[0]-1,b[1]),a, b)
                bottom_right_key = (b,c,(b[0]+1,b[1]))
                up_key = (a,(a[0],a[1]+1),c)

                keys_to_check = [bottom_left_key, bottom_right_key, up_key]

            else:
                # upsidedown
                # check corner top left, top right, bottom

                top_left_key = ((b[0]-1,b[1]),a,b)
                top_right_key = (b,c,(b[0]+1,b[1]))
                bottom_key = (a,(c[0],c[1]-1),c)

                keys_to_check = [top_left_key, top_right_key, bottom_key]

            is_valid = True
            for key in keys_to_check:
                if key in corners:
                    if not corners[key].is_available():
                        is_valid = False
                        break

            if is_valid:
                valid_corners.append(corner)

        return valid_corners  

    def get_valid_settlement_pos(self, edges: Dict[Tuple[Tuple[int, int], Tuple[int, int]], Edge], corners: Dict[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]], Corner]):
        valid_corner_pos = self.get_valid_corner_pos(corners)
        valid_settlement_pos = []
        # check if there is a road to this village
        # iterate over valid corner pos
        for corner in valid_corner_pos:
            a = corner[0]
            b = corner[1]
            c = corner[2]

            # top left or bottom left is a and b
            key_1 = (a,b)
            # top roght or bottom right is b and c
            key_2 = (b,c)
            # top or bottom is a and c
            key_3 = (a,c)

            keys_to_check = [key_1,key_2,key_3]

            for key in keys_to_check:
                if key in edges:
                    if edges[key].owner_id == self.player_id:
                        valid_settlement_pos.append(corner)
                        break
        
        return valid_settlement_pos

    def get_valid_road_pos(self, edges: Dict[Tuple[Tuple[int, int], Tuple[int, int]], Edge], corners: Dict[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]], Corner]):
        valid_edges = []
        # iterate over all edges
        # 2 cases:
        # 1. one of the corners the sdge is connecting is owned by the player
        # 2. one of the four edges connected to the 2 corners to the edge is owned by the player
        # in both cases get the coordinates of all 4 tiles a, b, c, d
        for edge in edges:

            if not edges[edge].is_available():
                continue

            # case if the edge is vertical -> tiles are one apart on x, and the same on y 
            if edge[1][0] - edge[0][0] == 1 and edge[0][1] == edge[1][1]:
                a = edge[0]
                d = edge[1]
                # b is to the topright of a 
                b = (a[0],a[1]+1)
                # c is to the bottom left of d
                c = (d[0],d[1]-1)
                # keys case 1
                corner_keys = [(a,b,d),(a,c,d)]
                # keys case 2 
                edge_keys = [(a,b),(a,c),(b,d),(c,d)]

            else: # edge is not vertical
                b = edge[0]
                c = edge[1]
                # a is to the left of c
                a = (c[0]-1, c[1])
                # d is to the right of b
                d = (b[0]+1, b[1])
                # check case 1
                corner_keys = [(a,b,c),(b,c,d)]
                # keys case 2 
                edge_keys = [(a,b),(a,c),(b,d),(c,d)]

            is_valid = False
            # check if one of the corners is owned
            for key in corner_keys:
                if key in corners:
                    if corners[key].owner_id == self.player_id:
                        is_valid = True
                        break
            
            if is_valid:
                valid_edges.append(edge)
                continue

            # check case 2
            # check if one of the 4 edges is owned
            for key in edge_keys:
                if key in edges:
                    if edges[key].owner_id == self.player_id:
                        is_valid = True
                        break
            
            if is_valid:
                valid_edges.append(edge)
                continue

        return valid_edges
   
    def get_valid_city_pos(self, corners: Dict[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]], Corner]):
        valid_pos = []
        # return all corners owned by the player 
        for corner in corners:
            if corners[corner].owner_id == self.player_id and corners[corner].building == 'settlement':
                valid_pos.append(corner)
                
        return valid_pos

    def get_legal_moves(self, has_rolled: bool, edges: Dict[Tuple[Tuple[int, int], Tuple[int, int]], Edge], corners: Dict[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]], Corner]):
        actions = {}

        if not has_rolled:
            # for now only allow to roll, later play certain development cards that trigger before rolling
            return {'roll': None}

        # player can end turn, build, buy or trade

        # end turn
        actions['end_turn'] = None
        actions['build'] = {}

        # build 
        # iterate over all buildings in the config, check if they can be build
        for k, v in self.config['buildings'].items():
            # skip development cards, or buildings with no position
            if v['placement'] is None:
                continue
            
            # iterate of recipe check if resources/buildings are available
            is_buildable = True
            for r_k, r_v in v['recipe']['buildings'].items():
                if len(self.buildings[r_k]) < r_v:
                    is_buildable = False
                    break
            
            if not is_buildable:
                continue
            
            for r_k, r_v in v['recipe']['resources'].items():
                if self.resources[r_k] < r_v:
                    is_buildable = False
                    break
            
            if not is_buildable:
                continue

            # check all hardcoced buildings, not ideal, 
            if k == 'road':
                actions['build'][k] = self.get_valid_road_pos(edges, corners)
            elif k == 'settlement':
                actions['build'][k] = self.get_valid_settlement_pos(edges, corners)
            elif k == 'city':
                actions['build'][k] = self.get_valid_city_pos(corners)
            else:
                print(f'unknown building: {k}')

        return actions

    def get_all_info(self):
        d = dict()
        d['name'] = self.name
        d['id'] = self.player_id
        d['victory_points'] = self.get_victory_points()
        d['resources'] = self.resources
        d['development_cards'] = self.development_cards
        d['buildings_left'] = {}
        for building, v in self.config['buildings'].items():
            d['buildings_left'][building] = v['limit'] - len(self.buildings[building])
        
        return d

    def get_public_info(self):
        d = dict()
        d['name'] = self.name
        d['id'] = self.player_id
        d['victory_points'] = self.get_victory_points()
        d['resources'] = 0
        for r in self.resources.values():
            d['resources'] += r
        d['development_cards'] = len(self.development_cards)

        return d
    
    def get_victory_points(self):
        points = 0
        for k,v in self.buildings.items():
            points += self.config['buildings'][k]['points'] * len(v)

        return points

    def __repr__(self) -> str:
        return (f"Player({self.name}, Victory Points: {self.victory_points}, Resources: {self.resources}, "
                f"Buildings: {self.buildings}, Development Cards: {len(self.development_cards)})")
