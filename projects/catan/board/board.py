from typing import Dict, Tuple
from game_config import standard_board_config
from board.tile import Tile
from board.edge import Edge
from board.corner import Corner

class Board:
    def __init__(self, config: Dict[str, any] = standard_board_config) -> None:
        self.tiles: Dict[Tuple[int, int], Tile] = {}
        self.edges: Dict[Tuple[Tuple[int, int], Tuple[int, int]], Edge] = {}
        self.corners: Dict[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]], Corner] = {}
        self.setup_tiles(config)
        self.setup_edges()
        self.setup_corners()

    def setup_tiles(self, config: Dict[str, any]) -> None:
        resources: list = config['resources']
        numbers: list = config['numbers']
        layout: list = config['layout']

        for coord, resource, number in zip(layout, resources, numbers):
            self.tiles[coord] = Tile(coord, resource, number)

    def setup_edges(self) -> None:

        neighbor_offsets = [(1,0), (0,1), (1,-1),(-1,0), (-1,1), (0,-1)]
        for coord in self.tiles:
            for offset in neighbor_offsets:
                adj_coord = (coord[0] + offset[0], coord[1] + offset[1])
                edge_key = tuple(sorted((coord, adj_coord)))
                if edge_key not in self.edges:
                    self.edges[edge_key] = Edge(coord, adj_coord)
    
    def setup_corners(self) -> None:
        # Offsets for each corner from the perspective of each tile
        corner_offsets = [
            ((0, 0), (1, 0), (0, 1)),        # Right corner
            ((0, 0), (0, 1), (-1, 1)),       # Upper-right corner
            ((0, 0), (-1, 1), (-1, 0)),      # Upper-left corner
            ((0, 0), (-1, 0), (0, -1)),      # Left corner
            ((0, 0), (0, -1), (1, -1)),      # Lower-left corner
            ((0, 0), (1, -1), (1, 0)),       # Lower-right corner
        ]

        for coord in self.tiles:
            for offsets in corner_offsets:
                # Generate each corner as a tuple of tile coordinates
                corner_key = tuple(sorted((coord[0] + dx, coord[1] + dy) for dx, dy in offsets))
                if corner_key not in self.corners:
                    self.corners[corner_key] = Corner(corner_key[0], corner_key[1], corner_key[2])



    def __repr__(self) -> str:
        return f"Board(Tiles count: {self.tiles}, Edges count: {len(self.edges)}, Corners count: {len(self.corners)} \n \
        Tiles: {self.tiles} \n Edges: {self.edges} \n Corners: {self.corners})"
